#!/usr/bin/env python3
"""Fail closed unless every retained full document has a publication allowance."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from materialize_all_sources import (
    normalize_publisher_doi, pdf_supplement_retrieval_url_matches, pdf_supplement_version_urls,
    preflight_original_retention, redistribution_footer, redistribution_notice_href,
)
from validate_materialization_completeness import sha256_file


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "raw_data/audits/materialization_rights_review.yaml"
CORPUS_ROOT = ROOT / "materialized_sources/corpus"


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_original_retention_rights(
    manifest: dict[str, Any], manifest_path: Path, publication_root: Path,
    review: dict[str, Any] | None,
) -> tuple[list[str], list[str]]:
    """Check the independent copy allowance even when the legacy root is filtered out."""
    errors: list[str] = []
    blocked: list[str] = []
    try:
        part = preflight_original_retention(
            manifest, manifest_path.parent, repository_root=publication_root,
            review=review, require_allow=False,
        )
        if part is not None and part["rights"]["publication_gate"].get("decision") != "allow":
            blocked.append(f"{manifest.get('uid')} original_retention: missing independent audited allow decision")
    except (KeyError, TypeError, AttributeError, ValueError, OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"PUBLICATION_ORIGINAL_RETENTION_INVALID {manifest.get('uid')}: {exc}")
    return errors, blocked


def validate_pdf_supplement_rights(
    manifest: dict[str, Any], manifest_path: Path, publication_root: Path,
    review: dict[str, Any] | None, *, check_derived: bool = True,
) -> tuple[list[str], list[str]]:
    """Check independent main/SI allowances; build preflight may precede derived files."""
    errors: list[str] = []
    blocked: list[str] = []
    supplement = manifest.get("pdf_supplement")
    supplement_root = manifest_path.parent / "pdf-supplement"
    uid = str(manifest.get("uid") or "")
    if supplement is None:
        if (supplement_root / "document.pdf").is_file():
            errors.append(f"PUBLICATION_PDF_SUPPLEMENT_UNDECLARED {uid}")
        if manifest.get("source_type") == "journal" or (
            manifest.get("source_type") == "arxiv" and manifest.get("adapter") == "arxiv_latex_v2"
        ):
            try:
                for path in (publication_root / manifest["metadata_path"], manifest_path.parent / "source-metadata.yaml"):
                    metadata = load_yaml(path)
                    versioning = metadata.get("versioning")
                    if versioning is not None and not isinstance(versioning, dict):
                        raise ValueError("publisher versioning must be a mapping or null")
                    if isinstance(versioning, dict) and "publisher_pdf" in versioning:
                        errors.append(f"PUBLICATION_PDF_SUPPLEMENT_DECLARATION_MISSING {uid}")
                        break
            except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
                errors.append(f"PUBLICATION_PDF_SUPPLEMENT_PACKAGE_INVALID {uid}: {exc}")
        return errors, blocked
    try:
        if not isinstance(supplement, dict):
            raise ValueError("PDF supplement must be an explicitly declared representation")
        actual_manifest = manifest_path.resolve().relative_to(publication_root.resolve()).as_posix()
        if not review or review.get("uid") != uid or review.get("manifest_path") != actual_manifest:
            raise ValueError("PDF review is missing or points to another manifest")
        metadata_path = (publication_root / manifest["metadata_path"]).resolve()
        metadata_path.relative_to(publication_root.resolve())
        canonical_metadata = load_yaml(metadata_path)
        capsule_metadata = load_yaml(manifest_path.parent / "source-metadata.yaml")
        version = supplement.get("source_version")
        version_url, si_url = pdf_supplement_version_urls(manifest, canonical_metadata, capsule_metadata, version)
        publisher = version.startswith("publisher-vor:")
        correspondence = None
        if publisher and manifest.get("source_type") == "arxiv":
            declaration = canonical_metadata["versioning"]["publisher_pdf"]
            correspondence = declaration["correspondence"]
            evidence = review.get("evidence")
            if not isinstance(evidence, list) or not any(
                isinstance(row, dict) and row.get("kind") == correspondence["audit_evidence_kind"]
                and isinstance(row.get("checked_at"), str) and row["checked_at"].strip()
                and normalize_publisher_doi(row.get("doi")) == normalize_publisher_doi(declaration["doi"])
                and (row.get("url") == version_url or (
                    isinstance(row.get("related_urls"), list) and version_url in row["related_urls"]
                ))
                for row in evidence
            ):
                raise ValueError("publisher PDF correspondence lacks its reviewed DOI/URL evidence")
        si = supplement.get("supplementary_information")
        if (si_url is not None) != (si is not None):
            raise ValueError("required publisher SI is missing or an undeclared SI is present")
        if (supplement_root / "supplementary-information").exists() and si_url is None:
            raise ValueError("retained SI files have no explicit publisher declaration")
        parts = [(supplement, "pdf-supplement", "pdf_supplement", version_url)]
        if si_url is not None:
            if not isinstance(si, dict) or "supplementary_information" in si:
                raise ValueError("only one explicitly declared SI PDF is supported")
            parts.append((si, "pdf-supplement/supplementary-information", "supplementary_information", si_url))
        for part, directory, grant_key, approved_url in parts:
            rights = part.get("rights")
            canonical = canonical_metadata.get("rights", {}).get(grant_key)
            capsule = capsule_metadata.get("rights", {}).get(grant_key)
            if not isinstance(rights, dict) or not (rights == review.get(grant_key) == canonical == capsule):
                raise ValueError(f"{grant_key}: canonical, capsule, manifest and audited PDF allowances differ")
            package = rights.get("redistribution_package")
            if not isinstance(package, dict) or not all(isinstance(package.get(field), str) and package[field].strip() for field in (
                "source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope",
            )):
                raise ValueError(f"{grant_key}: PDF redistribution package is incomplete")
            if correspondence is not None:
                for allowance in (rights, review.get(grant_key), canonical, capsule):
                    bound = (allowance.get("redistribution_package") or {}).get("publisher_correspondence")
                    if not isinstance(bound, dict) or bound.get("reviewed") is not True or bound != correspondence:
                        raise ValueError(f"{grant_key}: PDF allowance differs from its declared publisher correspondence")
            if any(not isinstance(rights.get(field), str) or not rights[field].strip() for field in ("license_spdx", "license_url", "license_verified_at")):
                raise ValueError(f"{grant_key}: PDF rights declaration lacks its reviewed license")
            gate = rights.get("publication_gate")
            if not isinstance(gate, dict) or gate.get("decision") != "allow":
                blocked.append(f"{uid} {grant_key} PDF supplement: missing explicit audited allow decision")
            if not isinstance(gate, dict) or gate.get("approved_scope") != package["scope"] or not isinstance(gate.get("reason"), str) or not gate["reason"].strip():
                raise ValueError(f"{grant_key}: PDF allowance does not explicitly approve its own retained scope")
            base = manifest_path.parent / directory
            base.resolve().relative_to(manifest_path.parent.resolve())
            source = (base / "document.pdf").resolve()
            source.relative_to(base.resolve())
            materialization = part.get("materialization") or {}
            source_hash = sha256_file(source)
            retrievals = part.get("retrievals")
            retrieval = retrievals[0] if isinstance(retrievals, list) and len(retrievals) == 1 and isinstance(retrievals[0], dict) else {}
            if (
                part.get("source_version") != version or (publisher and package.get("source_version") != version)
                or package["source_revision"] != part.get("revision") or part.get("revision") != f"sha256:{source_hash}"
                or materialization.get("source_pdf") != f"{directory}/document.pdf"
                or materialization.get("source_pdf_sha256") != source_hash or package["source_version_url"] != approved_url
                or not pdf_supplement_retrieval_url_matches(retrieval, approved_url, publisher=publisher)
                or retrieval.get("sha256") != source_hash or retrieval.get("bytes") != source.stat().st_size
            ):
                raise ValueError(f"{grant_key}: PDF allowance does not cover the retained PDF revision/version/URL")
            license_path = (publication_root / package["notice_path"]).resolve()
            license_path.relative_to(publication_root.resolve())
            expected_notice = license_path.read_text(encoding="utf-8")
            if not expected_notice.strip() or (base / "NOTICE.md").read_text(encoding="utf-8") != expected_notice:
                raise ValueError(f"{grant_key}: PDF notice is absent or differs from its reviewed original")
            if materialization.get("document") != f"{directory}/document.txt":
                raise ValueError(f"{grant_key}: PDF text document is not independently declared")
            if check_derived:
                text = (base / "document.txt").read_text(encoding="utf-8")
                if text.count("<!-- materialization-redistribution-notice -->") != 1 or not text.endswith(redistribution_footer(package)):
                    raise ValueError(f"{grant_key}: PDF attribution or modification footer is absent")
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
        errors.append(f"PUBLICATION_PDF_SUPPLEMENT_PACKAGE_INVALID {uid}: {exc}")
    return errors, blocked


def validate_publication_rights(
    audit_path: Path = AUDIT_PATH,
    corpus_root: Path = CORPUS_ROOT,
) -> tuple[list[str], list[str], int, int]:
    errors: list[str] = []
    blocked: list[str] = []
    if not audit_path.is_file():
        return [f"PUBLICATION_RIGHTS_AUDIT_MISSING {audit_path}"], blocked, 0, 0

    audit = load_yaml(audit_path)
    if not isinstance(audit, dict) or not isinstance(audit.get("items"), list):
        return ["PUBLICATION_RIGHTS_AUDIT_INVALID"], blocked, 0, 0
    items = audit["items"]
    scope = audit.get("scope") if isinstance(audit.get("scope"), dict) else {}
    baseline_count = scope.get("baseline_full_text_count")
    additional_count = scope.get("additional_full_text_review_count", 0)
    if not isinstance(additional_count, int) or isinstance(additional_count, bool) or additional_count < 0:
        fail(
            f"PUBLICATION_RIGHTS_AUDIT_COUNT invalid additional_full_text_review_count={additional_count!r}",
            errors,
        )
    elif not isinstance(baseline_count, int) or baseline_count + additional_count != len(items):
        expected_count = baseline_count + additional_count if isinstance(baseline_count, int) else baseline_count
        fail(
            f"PUBLICATION_RIGHTS_AUDIT_COUNT expected={expected_count} actual={len(items)}",
            errors,
        )

    audited: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("uid"), str):
            fail("PUBLICATION_RIGHTS_AUDIT_ITEM_INVALID", errors)
            continue
        uid = item["uid"]
        if uid in audited:
            fail(f"PUBLICATION_RIGHTS_AUDIT_DUPLICATE {uid}", errors)
            continue
        audited[uid] = item

    active_full_text: dict[str, Path] = {}
    supplemental_uids: set[str] = set()
    original_uids: set[str] = set()
    for manifest_path in sorted(corpus_root.glob("*/manifest.yaml")):
        manifest = load_yaml(manifest_path)
        if isinstance(manifest, dict):
            original_errors, original_blocks = validate_original_retention_rights(
                manifest, manifest_path, corpus_root.parents[1], audited.get(manifest.get("uid")),
            )
            errors.extend(original_errors)
            blocked.extend(original_blocks)
            if "original_retention" in manifest:
                original_uids.add(str(manifest.get("uid") or ""))
            supplement_errors, supplement_blocks = validate_pdf_supplement_rights(
                manifest, manifest_path, corpus_root.parents[1], audited.get(manifest.get("uid")),
            )
            errors.extend(supplement_errors)
            blocked.extend(supplement_blocks)
            if isinstance(manifest.get("pdf_supplement"), dict):
                supplemental_uids.add(str(manifest.get("uid") or ""))
        materialization = manifest.get("materialization") if isinstance(manifest, dict) else None
        retained_source_pdf = (
            isinstance(materialization, dict)
            and isinstance(materialization.get("source_pdf"), str)
            and bool(materialization["source_pdf"])
        )
        retained_source_markdown = (
            isinstance(materialization, dict)
            and (
                isinstance(materialization.get("retained_markdown_source"), str)
                and bool(materialization["retained_markdown_source"])
                or "retained_text_sources" in materialization
            )
        )
        if not isinstance(manifest, dict) or (
            manifest.get("content_tier") != "full_text" and not retained_source_pdf
            and not retained_source_markdown
        ):
            continue
        uid = manifest.get("uid")
        if not isinstance(uid, str) or not uid:
            fail(f"PUBLICATION_MANIFEST_UID_MISSING {manifest_path.relative_to(ROOT)}", errors)
            continue
        if uid in active_full_text:
            fail(f"PUBLICATION_MANIFEST_UID_DUPLICATE {uid}", errors)
            continue
        active_full_text[uid] = manifest_path

    for uid, manifest_path in sorted(active_full_text.items()):
        review = audited.get(uid)
        if review is None:
            fail(f"PUBLICATION_RIGHTS_REVIEW_MISSING {uid}", errors)
            continue
        reviewed_manifest = review.get("manifest_path")
        publication_root = corpus_root.parents[1]
        actual_manifest = manifest_path.relative_to(publication_root).as_posix()
        if reviewed_manifest != actual_manifest:
            fail(
                f"PUBLICATION_RIGHTS_MANIFEST_MISMATCH {uid} "
                f"reviewed={reviewed_manifest} actual={actual_manifest}",
                errors,
            )
        source_revision = review.get("source_revision")
        manifest = load_yaml(manifest_path)
        actual_revision = manifest.get("revision") if isinstance(manifest, dict) else None
        if not isinstance(source_revision, str) or source_revision != actual_revision:
            fail(
                f"PUBLICATION_RIGHTS_REVISION_MISMATCH {uid} "
                f"reviewed={source_revision} actual={actual_revision}",
                errors,
            )
        gate = review.get("publication_gate")
        decision = gate.get("decision") if isinstance(gate, dict) else None
        if decision != "allow":
            reason = gate.get("reason") if isinstance(gate, dict) else "missing publication gate"
            blocked.append(f"{uid}: {reason}")
        else:
            # An allowance with packaging conditions is not valid when a later
            # materialization silently discards the reviewed notice/attribution.
            package = review.get("redistribution_package")
            actual_package = manifest.get("rights", {}).get("redistribution_package")
            try:
                metadata_path = manifest.get("metadata_path")
                canonical_package = None
                if metadata_path:
                    metadata_file = (publication_root / metadata_path).resolve()
                    metadata_file.relative_to(publication_root.resolve())
                    canonical_package = load_yaml(metadata_file).get("rights", {}).get("redistribution_package")
                if not (package or actual_package or canonical_package):
                    continue
                capsule_package = load_yaml(manifest_path.parent / "source-metadata.yaml").get("rights", {}).get("redistribution_package")
                if not package or not (package == canonical_package == capsule_package == actual_package) or package["source_revision"] != actual_revision:
                    raise ValueError("reviewed and materialized license packages differ")
                license_path = (publication_root / package["notice_path"]).resolve()
                license_path.relative_to(publication_root.resolve())
                expected_notice = license_path.read_text(encoding="utf-8")
                notice = manifest_path.parent / "NOTICE.md"
                if not expected_notice.strip() or notice.read_text(encoding="utf-8") != expected_notice:
                    raise ValueError("full notice is absent or differs from the reviewed license")
                document = (manifest_path.parent / manifest["materialization"]["document"]).resolve()
                document.relative_to(manifest_path.parent.resolve())
                text = document.read_text(encoding="utf-8")
                notice_href = redistribution_notice_href(manifest_path.parent, document)
                if text.count("<!-- materialization-redistribution-notice -->") != 1 or not text.endswith(
                    redistribution_footer(package, notice_href)
                ):
                    raise ValueError("attribution or modification notice is absent")
            except (KeyError, TypeError, AttributeError, ValueError, OSError) as exc:
                fail(f"PUBLICATION_RIGHTS_PACKAGE_INVALID {uid}: {exc}", errors)

    if not active_full_text and not supplemental_uids and not original_uids:
        fail("PUBLICATION_FULL_TEXT_SET_EMPTY", errors)
    return errors, blocked, len(set(active_full_text) | supplemental_uids | original_uids), len(audited)


def main() -> int:
    errors, blocked, active_count, audited_count = validate_publication_rights()

    print(
        "publication_rights_gate "
        f"active_full_text={active_count} audited={audited_count} "
        f"blocked={len(blocked)} errors={len(errors)}"
    )
    if errors:
        print("\nAudit errors:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    if blocked:
        print("\nPublication blocks:", file=sys.stderr)
        for message in blocked:
            print(f"- {message}", file=sys.stderr)
    if errors or blocked:
        print(
            "\nPublic redistribution remains blocked until every active full-text capsule "
            "or retained full document has an explicit audited allow decision.",
            file=sys.stderr,
        )
        return 1
    print("\nEvery active full-text capsule or retained full document has an explicit audited publication allowance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
