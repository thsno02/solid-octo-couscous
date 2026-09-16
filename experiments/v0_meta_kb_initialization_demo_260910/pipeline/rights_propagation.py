"""Preserve declared source rights through claims, pages, and machine views.

This module records terms declared by a source capsule.  It does not decide
whether a use is permitted and it never treats a missing package as approval.
"""
from __future__ import annotations

import copy
import posixpath
from pathlib import Path
from typing import Any, Iterable

import yaml


PACKAGE_FIELDS = (
    "source_revision",
    "source_version_url",
    "notice_path",
    "attribution",
    "modifications",
    "scope",
)
REF_FIELDS = (
    "source_uid",
    "source_revision",
    "source_version_url",
    "license_spdx",
    "license_url",
    "notice_path",
    "package_path",
)
DECLARED = "declared-redistribution-package"
UNAVAILABLE = "unavailable"

EVIDENCE_USE = "source_excerpt"
CLAIM_USE = "source_excerpt_claim"
PAGE_USE = "rendered_source_claims"
PACK_USE = "context_pack_claim_reference"

EVIDENCE_TRANSFORMATION = (
    "A bounded excerpt was selected from the pinned local source; whitespace may be normalized. "
    "See the referenced redistribution package for source-level modifications and scope."
)
CLAIM_TRANSFORMATION = (
    "The claim reproduces its bounded evidence excerpt with whitespace normalized and remains an "
    "unverified source assertion."
)
PAGE_TRANSFORMATION = (
    "The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page."
)
PACK_TRANSFORMATION = (
    "The context pack references source-authored claims; expand each claim and package_path before reuse."
)


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def rights_snapshot(value: Any) -> dict[str, Any] | None:
    """Return the portable rights package, or ``None`` when it is not complete.

    ``value`` may be either a rights mapping or an object containing ``rights``.
    Incomplete packages are deliberately not upgraded into usable references;
    validators report them separately.
    """
    if not isinstance(value, dict):
        return None
    rights = value.get("rights") if isinstance(value.get("rights"), dict) else value
    package = rights.get("redistribution_package")
    if not isinstance(package, dict):
        return None
    if not all(_nonempty_string(package.get(field)) for field in PACKAGE_FIELDS):
        return None
    if not _nonempty_string(rights.get("license_spdx")) or not _nonempty_string(rights.get("license_url")):
        return None
    result: dict[str, Any] = {
        "license_spdx": str(rights["license_spdx"]),
        "license_url": str(rights["license_url"]),
        "redistribution_package": {field: str(package[field]) for field in PACKAGE_FIELDS},
    }
    if _nonempty_string(rights.get("license_verified_at")):
        result["license_verified_at"] = str(rights["license_verified_at"])
    return result


def source_rights(source: dict[str, Any]) -> dict[str, Any] | None:
    """Read only the rights snapshot persisted in a compiler source record."""
    return rights_snapshot(source.get("rights"))


def rights_status(source: dict[str, Any]) -> str:
    return DECLARED if source_rights(source) else UNAVAILABLE


def make_rights_ref(
    source: dict[str, Any],
    *,
    usage: str,
    transformation: str,
    claim_refs: Iterable[str] | None = None,
) -> dict[str, Any] | None:
    rights = source_rights(source)
    if rights is None:
        return None
    package = rights["redistribution_package"]
    manifest = source.get("manifest")
    if not _nonempty_string(manifest):
        return None
    result: dict[str, Any] = {
        "source_uid": str(source.get("uid") or ""),
        "source_revision": package["source_revision"],
        "source_version_url": package["source_version_url"],
        "license_spdx": rights["license_spdx"],
        "license_url": rights["license_url"],
        "notice_path": package["notice_path"],
        "package_path": f"{manifest}#rights.redistribution_package",
        "usage": usage,
        "transformation": transformation,
    }
    refs = sorted({str(ref) for ref in claim_refs or [] if str(ref)})
    if refs:
        result["claim_refs"] = refs
    return result


def object_rights_refs(value: dict[str, Any]) -> list[dict[str, Any]]:
    props = value.get("semantics", {}).get("property_assertions", {})
    refs = props.get("rights_refs", []) if isinstance(props, dict) else []
    return [copy.deepcopy(ref) for ref in refs if isinstance(ref, dict)] if isinstance(refs, list) else []


def object_unavailable_sources(value: dict[str, Any]) -> list[str]:
    props = value.get("semantics", {}).get("property_assertions", {})
    refs = props.get("rights_unavailable_source_refs", []) if isinstance(props, dict) else []
    return sorted({str(ref) for ref in refs}) if isinstance(refs, list) else []


def is_source_authored(claim: dict[str, Any]) -> bool:
    props = claim.get("semantics", {}).get("property_assertions", {})
    method = claim.get("provenance", {}).get("method")
    return method == "source-assertion-extraction-without-model" or (
        isinstance(props, dict) and props.get("claim_scope") == "source-reported assertion"
    )


def is_source_evidence(item: dict[str, Any]) -> bool:
    props = item.get("semantics", {}).get("property_assertions", {})
    role = props.get("evidence_role") if isinstance(props, dict) else None
    return item.get("provenance", {}).get("method") == "deterministic-local-excerpt" or role in {
        "source-text",
        "bounded-excerpt",
        "static-repository-evidence",
    }


def infer_rendered_claim_refs(
    body: str,
    claim_ids: Iterable[str],
    claims_by_uid: dict[str, dict[str, Any]],
) -> list[str]:
    """Infer rendered claims from the text emitted by the deterministic renderer."""
    rendered_body = str(body).split("## Source text rights and attribution", 1)[0]
    normalized_body = " ".join(rendered_body.split())
    rendered: list[str] = []
    for claim_id in claim_ids:
        uid = str(claim_id)
        claim = claims_by_uid.get(uid, {})
        props = claim.get("semantics", {}).get("property_assertions", {})
        claim_text = props.get("text") if isinstance(props, dict) else None
        if not _nonempty_string(claim_text):
            continue
        normalized_claim = " ".join(str(claim_text).split())
        # Synthesis pages intentionally render bounded previews, currently up
        # to 420 characters.  A 160-character prefix remains specific enough
        # to distinguish a rendered statement from a frontmatter-only ref.
        needle = normalized_claim[:160]
        if needle and needle in normalized_body and uid in rendered_body:
            rendered.append(uid)
    return rendered


def page_rights_payload(
    claim_ids: Iterable[str],
    claims_by_uid: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Group persisted claim references by source for a rendered page or pack."""
    grouped: dict[tuple[str, str, str], dict[str, Any]] = {}
    unavailable: set[str] = set()
    for claim_id in claim_ids:
        claim = claims_by_uid.get(str(claim_id))
        if not claim or not is_source_authored(claim):
            continue
        unavailable.update(object_unavailable_sources(claim))
        for ref in object_rights_refs(claim):
            key = (
                str(ref.get("source_uid") or ""),
                str(ref.get("source_revision") or ""),
                str(ref.get("package_path") or ""),
            )
            if key not in grouped:
                grouped[key] = {
                    field: copy.deepcopy(ref.get(field))
                    for field in REF_FIELDS
                }
                grouped[key].update(
                    {
                        "usage": PAGE_USE,
                        "transformation": PAGE_TRANSFORMATION,
                        "claim_refs": [],
                    }
                )
            grouped[key]["claim_refs"].append(str(claim_id))
    result = []
    for key in sorted(grouped):
        ref = grouped[key]
        ref["claim_refs"] = sorted(set(ref["claim_refs"]))
        result.append(ref)
    return result, sorted(unavailable)


def pack_rights_payload(
    claim_ids: Iterable[str],
    claims_by_uid: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[str]]:
    refs, unavailable = page_rights_payload(claim_ids, claims_by_uid)
    for ref in refs:
        ref["usage"] = PACK_USE
        ref["transformation"] = PACK_TRANSFORMATION
    return refs, unavailable


def rights_markdown(
    *,
    current_repo_path: str,
    rights_refs: list[dict[str, Any]],
    unavailable_source_refs: list[str],
    sources_by_uid: dict[str, dict[str, Any]],
) -> str:
    if not rights_refs and not unavailable_source_refs:
        return ""
    lines = [
        "## Source text rights and attribution",
        "",
        "The terms below apply only to the listed source-authored claim components. They do not "
        "relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.",
    ]
    current_dir = posixpath.dirname(current_repo_path)
    for ref in rights_refs:
        source_uid = str(ref.get("source_uid") or "")
        source = sources_by_uid.get(source_uid, {})
        rights = source_rights(source)
        package = rights["redistribution_package"] if rights else {}
        title = str(source.get("title") or source.get("canonical_id") or source_uid)
        license_url = str(ref.get("license_url") or "")
        notice_path = str(ref.get("notice_path") or "")
        notice_link = posixpath.relpath(notice_path, current_dir) if notice_path else ""
        source_url = str(ref.get("source_version_url") or "")
        claim_refs = ", ".join(f"`{claim}`" for claim in ref.get("claim_refs", [])) or "none"
        lines.extend(
            [
                "",
                f"### {title} (`{source_uid}`)",
                "",
                f"- Components: {claim_refs}",
                f"- Source revision: `{ref.get('source_revision')}`",
                f"- Source version: [pinned upstream version]({source_url})",
                f"- License: [{ref.get('license_spdx')}]({license_url})",
                f"- NOTICE: [{notice_path}]({notice_link})",
                f"- Attribution: {package.get('attribution')}",
                f"- Excerpt/page transformation: {ref.get('transformation')} {package.get('modifications')}",
                f"- Scope: {package.get('scope')}",
            ]
        )
    for source_uid in unavailable_source_refs:
        source = sources_by_uid.get(source_uid, {})
        title = str(source.get("title") or source.get("canonical_id") or source_uid)
        lines.extend(
            [
                "",
                f"### {title} (`{source_uid}`)",
                "",
                "- Rights status: No complete redistribution package is recorded for this source. "
                "No license or permission is inferred by this compiler.",
                "- Excerpt note: The page identifies the component as a source-reported candidate and preserves its "
                "pinned source reference; downstream reuse must resolve rights separately.",
            ]
        )
    return "\n".join(lines)


def _load_yaml_mapping(path: Path, label: str, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"RIGHTS_{label}_READ {path}: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"RIGHTS_{label}_FORMAT {path}")
        return None
    return value


def _repo_file(root: Path, relative: Any, label: str, errors: list[str]) -> Path | None:
    if not _nonempty_string(relative) or Path(str(relative)).is_absolute():
        errors.append(f"RIGHTS_{label}_PATH {relative}")
        return None
    root = root.resolve()
    path = (root / str(relative)).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        errors.append(f"RIGHTS_{label}_PATH {relative}")
        return None
    if not path.is_file():
        errors.append(f"RIGHTS_{label}_MISSING {relative}")
        return None
    return path


def _incomplete_package(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    rights = value.get("rights") if isinstance(value.get("rights"), dict) else value
    package = rights.get("redistribution_package")
    if package is None:
        return False
    if not isinstance(package, dict):
        return True
    return not (
        all(_nonempty_string(package.get(field)) for field in PACKAGE_FIELDS)
        and _nonempty_string(rights.get("license_spdx"))
        and _nonempty_string(rights.get("license_url"))
    )


def _validate_ref(
    ref: dict[str, Any],
    *,
    source: dict[str, Any],
    rights: dict[str, Any],
    usage: str,
    owner: str,
    errors: list[str],
) -> None:
    expected = make_rights_ref(source, usage=usage, transformation="validated")
    if expected is None:
        errors.append(f"RIGHTS_REF_UNRESOLVABLE {owner} -> {source.get('uid')}")
        return
    for field in REF_FIELDS:
        if ref.get(field) != expected.get(field):
            errors.append(
                f"RIGHTS_REF_MISMATCH {owner} -> {source.get('uid')} field={field}"
            )
    if ref.get("usage") != usage:
        errors.append(f"RIGHTS_REF_USAGE {owner} -> {source.get('uid')}")
    if not _nonempty_string(ref.get("transformation")):
        errors.append(f"RIGHTS_REF_TRANSFORMATION {owner} -> {source.get('uid')}")
    package = rights["redistribution_package"]
    if ref.get("source_revision") != package.get("source_revision"):
        errors.append(f"RIGHTS_REF_REVISION {owner} -> {source.get('uid')}")


def validate_rights_chain(
    *,
    root: Path,
    claims: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    sources: list[dict[str, Any]],
) -> list[str]:
    """Validate canonical package persistence and claim/evidence propagation."""
    errors: list[str] = []
    sources_by_uid = {str(source.get("uid") or ""): source for source in sources}
    managed_sources = {
        source_uid
        for source_uid, source in sources_by_uid.items()
        if _nonempty_string(source.get("manifest")) or _nonempty_string(source.get("rights_status"))
    }
    canonical: dict[str, dict[str, Any] | None] = {}

    for source_uid, source in sources_by_uid.items():
        persisted = source_rights(source)
        manifest_rel = source.get("manifest")
        manifest: dict[str, Any] | None = None
        metadata: dict[str, Any] | None = None
        if _nonempty_string(manifest_rel):
            manifest_path = _repo_file(root, manifest_rel, "MANIFEST", errors)
            if manifest_path:
                manifest = _load_yaml_mapping(manifest_path, "MANIFEST", errors)
        manifest_rights = rights_snapshot(manifest.get("rights")) if manifest else persisted
        canonical[source_uid] = manifest_rights

        if manifest and _incomplete_package(manifest.get("rights")):
            errors.append(f"RIGHTS_PACKAGE_INCOMPLETE {source_uid}")
        if manifest_rights != persisted:
            errors.append(f"RIGHTS_SELECTED_MANIFEST_MISMATCH {source_uid}")

        if manifest:
            metadata_rel = manifest.get("metadata_path")
            metadata_path = _repo_file(root, metadata_rel, "METADATA", errors)
            if metadata_path:
                metadata = _load_yaml_mapping(metadata_path, "METADATA", errors)
            metadata_rights = rights_snapshot(metadata.get("rights")) if metadata else None
            if metadata and _incomplete_package(metadata.get("rights")):
                errors.append(f"RIGHTS_PACKAGE_INCOMPLETE {source_uid} metadata")
            if metadata_rights != manifest_rights:
                errors.append(f"RIGHTS_METADATA_MANIFEST_MISMATCH {source_uid}")

        if manifest_rights:
            package = manifest_rights["redistribution_package"]
            if source.get("rights_status") != DECLARED:
                errors.append(f"RIGHTS_STATUS_MISMATCH {source_uid}")
            if source.get("revision") != package["source_revision"]:
                errors.append(f"RIGHTS_SOURCE_REVISION_MISMATCH {source_uid}")
            if manifest and manifest.get("revision") != package["source_revision"]:
                errors.append(f"RIGHTS_MANIFEST_REVISION_MISMATCH {source_uid}")
            _repo_file(root, package["notice_path"], "NOTICE", errors)
        elif _nonempty_string(manifest_rel) and source.get("rights_status") != UNAVAILABLE:
            errors.append(f"RIGHTS_STATUS_MISMATCH {source_uid}")

    evidence_by_uid = {str(item.get("uid") or ""): item for item in evidence}
    for evidence_uid, item in evidence_by_uid.items():
        item_source_uids = [
            str(value) for value in item.get("provenance", {}).get("source_refs", [])
        ]
        refs = object_rights_refs(item)
        item_unavailable = object_unavailable_sources(item)
        if not is_source_evidence(item):
            if item.get("provenance", {}).get("method") == "collection-metadata-read" and (
                refs or item_unavailable
            ):
                errors.append(f"COLLECTOR_EVIDENCE_RIGHTS_INHERITANCE {evidence_uid}")
            continue
        tracked_source_uids = [uid for uid in item_source_uids if uid in managed_sources]
        wrapped = [uid for uid in tracked_source_uids if canonical.get(uid)]
        unavailable = sorted(uid for uid in tracked_source_uids if not canonical.get(uid))
        actual_sources = [str(ref.get("source_uid") or "") for ref in refs]
        if sorted(actual_sources) != sorted(wrapped) or item_unavailable != unavailable:
            errors.append(f"EVIDENCE_RIGHTS_COVERAGE {evidence_uid}")
        for ref in refs:
            source_uid = str(ref.get("source_uid") or "")
            source = sources_by_uid.get(source_uid)
            rights = canonical.get(source_uid)
            if source is None or rights is None:
                errors.append(f"EVIDENCE_RIGHTS_UNKNOWN_SOURCE {evidence_uid} -> {source_uid}")
            else:
                _validate_ref(
                    ref,
                    source=source,
                    rights=rights,
                    usage=EVIDENCE_USE,
                    owner=evidence_uid,
                    errors=errors,
                )

    for claim in claims:
        claim_uid = str(claim.get("uid") or "<missing-uid>")
        source_uids = [str(value) for value in claim.get("provenance", {}).get("source_refs", [])]
        claim_refs = object_rights_refs(claim)
        claim_unavailable = object_unavailable_sources(claim)
        bound_evidence = [evidence_by_uid[uid] for uid in claim.get("epistemic", {}).get("evidence_refs", []) if uid in evidence_by_uid]

        props = claim.get("semantics", {}).get("property_assertions", {})
        scope = props.get("claim_scope") if isinstance(props, dict) else None
        method = claim.get("provenance", {}).get("method")
        if method == "source-assertion-extraction-without-model" and scope != "source-reported assertion":
            errors.append(f"CLAIM_SCOPE_METHOD_MISMATCH {claim_uid} source")
        if method == "collection-assessment-extraction" and scope != "collector assessment, not source-authored scientific fact":
            errors.append(f"CLAIM_SCOPE_METHOD_MISMATCH {claim_uid} collector")
        if scope == "source-reported assertion" and method != "source-assertion-extraction-without-model":
            errors.append(f"CLAIM_SCOPE_METHOD_MISMATCH {claim_uid} source")
        if scope == "collector assessment, not source-authored scientific fact" and method != "collection-assessment-extraction":
            errors.append(f"CLAIM_SCOPE_METHOD_MISMATCH {claim_uid} collector")

        if not is_source_authored(claim):
            if claim_refs or claim_unavailable:
                errors.append(f"COLLECTOR_RIGHTS_INHERITANCE {claim_uid}")
            for item in bound_evidence:
                if object_rights_refs(item) or object_unavailable_sources(item):
                    errors.append(f"COLLECTOR_EVIDENCE_RIGHTS_INHERITANCE {claim_uid} -> {item.get('uid')}")
                if item.get("provenance", {}).get("method") != "collection-metadata-read" or is_source_evidence(item):
                    errors.append(f"CLAIM_EVIDENCE_METHOD_MISMATCH {claim_uid} -> {item.get('uid')}")
            continue

        tracked_source_uids = [uid for uid in source_uids if uid in managed_sources]
        wrapped = [uid for uid in tracked_source_uids if canonical.get(uid)]
        unavailable = sorted(uid for uid in tracked_source_uids if not canonical.get(uid))
        actual_sources = [str(ref.get("source_uid") or "") for ref in claim_refs]
        if sorted(actual_sources) != sorted(wrapped) or claim_unavailable != unavailable:
            errors.append(f"CLAIM_RIGHTS_COVERAGE {claim_uid}")
        for ref in claim_refs:
            source_uid = str(ref.get("source_uid") or "")
            source = sources_by_uid.get(source_uid)
            rights = canonical.get(source_uid)
            if source is None or rights is None:
                errors.append(f"CLAIM_RIGHTS_UNKNOWN_SOURCE {claim_uid} -> {source_uid}")
            else:
                _validate_ref(ref, source=source, rights=rights, usage=CLAIM_USE, owner=claim_uid, errors=errors)

        for item in bound_evidence:
            evidence_uid = str(item.get("uid") or "<missing-uid>")
            evidence_method = item.get("provenance", {}).get("method")
            expected_evidence_method = "deterministic-local-excerpt"
            if evidence_method != expected_evidence_method:
                errors.append(f"CLAIM_EVIDENCE_METHOD_MISMATCH {claim_uid} -> {evidence_uid}")
    return errors


def validate_payload(
    *,
    owner: str,
    claim_ids: Iterable[str],
    claims_by_uid: dict[str, dict[str, Any]],
    actual_refs: Any,
    actual_unavailable: Any,
    pack: bool = False,
) -> list[str]:
    expected_refs, expected_unavailable = (
        pack_rights_payload(claim_ids, claims_by_uid)
        if pack
        else page_rights_payload(claim_ids, claims_by_uid)
    )
    if actual_refs != expected_refs:
        return [f"RIGHTS_PAYLOAD_MISMATCH {owner}"]
    if actual_unavailable != expected_unavailable:
        return [f"RIGHTS_UNAVAILABLE_MISMATCH {owner}"]
    return []


def validate_page_rights(
    *,
    owner: str,
    frontmatter: dict[str, Any],
    body: str,
    claims_by_uid: dict[str, dict[str, Any]],
    sources_by_uid: dict[str, dict[str, Any]],
) -> list[str]:
    rendered = frontmatter.get("rendered_claim_refs", [])
    if not isinstance(rendered, list):
        return [f"RIGHTS_RENDERED_CLAIMS_FORMAT {owner}"]
    inferred = infer_rendered_claim_refs(
        body,
        frontmatter.get("claim_refs", []),
        claims_by_uid,
    )
    if sorted(str(value) for value in rendered) != sorted(inferred):
        errors = [f"RIGHTS_RENDERED_CLAIMS_MISMATCH {owner}"]
    else:
        errors = []
    errors.extend(validate_payload(
        owner=owner,
        claim_ids=[str(value) for value in rendered],
        claims_by_uid=claims_by_uid,
        actual_refs=frontmatter.get("rights_refs"),
        actual_unavailable=frontmatter.get("rights_unavailable_source_refs"),
    ))
    expected_refs, expected_unavailable = page_rights_payload(rendered, claims_by_uid)
    if expected_refs or expected_unavailable:
        if "## Source text rights and attribution" not in body:
            errors.append(f"RIGHTS_PAGE_NOTICE_MISSING {owner}")
        if "apply only to the listed source-authored claim components" not in body:
            errors.append(f"RIGHTS_PAGE_SCOPE_BOUNDARY_MISSING {owner}")
        if "do not relicense collector assessments" not in body:
            errors.append(f"RIGHTS_PAGE_MIXED_SCOPE_MISSING {owner}")
    for ref in expected_refs:
        source_uid = str(ref.get("source_uid") or "")
        rights = source_rights(sources_by_uid.get(source_uid, {}))
        package = rights["redistribution_package"] if rights else {}
        for field, value in (
            ("license_url", ref.get("license_url")),
            ("notice_path", ref.get("notice_path")),
            ("attribution", package.get("attribution")),
            ("modifications", package.get("modifications")),
            ("scope", package.get("scope")),
        ):
            if not _nonempty_string(value) or str(value) not in body:
                errors.append(f"RIGHTS_PAGE_{field.upper()}_MISSING {owner} -> {source_uid}")
    if expected_unavailable and "No complete redistribution package is recorded" not in body:
        errors.append(f"RIGHTS_PAGE_UNAVAILABLE_NOTICE_MISSING {owner}")
    return errors
