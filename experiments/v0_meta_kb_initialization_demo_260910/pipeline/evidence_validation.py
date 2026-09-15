#!/usr/bin/env python3
"""Shared, offline validation for the demo's claim-to-evidence chain."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import yaml


LINE_SELECTOR = re.compile(r"L([1-9][0-9]*)-L([1-9][0-9]*)")
METADATA_FIELDS = {
    "collection.inclusion_reason",
    "why_collected",
    "knowledge_evolution_link",
    "summary",
}
DETERMINISTIC_CLAIM_METHODS = {
    "source-assertion-extraction-without-model",
    "collection-assessment-extraction",
}


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def properties(value: dict[str, Any]) -> dict[str, Any]:
    result = value.get("semantics", {}).get("property_assertions", {})
    return result if isinstance(result, dict) else {}


def source_refs(value: dict[str, Any]) -> list[str]:
    result = value.get("provenance", {}).get("source_refs", [])
    return [str(item) for item in result] if isinstance(result, list) else []


def evidence_refs(value: dict[str, Any]) -> list[str]:
    result = value.get("epistemic", {}).get("evidence_refs", [])
    return [str(item) for item in result] if isinstance(result, list) else []


def _local_file(root: Path, local_path: Any, uid: str, errors: list[str]) -> Path | None:
    if not isinstance(local_path, str) or not local_path:
        errors.append(f"EVIDENCE_LOCAL_PATH {uid} -> {local_path}")
        return None
    relative = Path(local_path)
    if relative.is_absolute():
        errors.append(f"EVIDENCE_LOCAL_PATH_OUTSIDE_ROOT {uid} -> {local_path}")
        return None
    root = root.resolve()
    path = (root / relative).resolve()
    try:
        path.relative_to(root)
    except ValueError:
        errors.append(f"EVIDENCE_LOCAL_PATH_OUTSIDE_ROOT {uid} -> {local_path}")
        return None
    if not path.is_file():
        errors.append(f"EVIDENCE_LOCAL_PATH {uid} -> {local_path}")
        return None
    return path


def _selector_parts(selector: Any, uid: str, errors: list[str]) -> tuple[str, str] | None:
    if not isinstance(selector, str) or not selector.startswith("local://") or "#" not in selector:
        errors.append(f"EVIDENCE_SELECTOR_FORMAT {uid} -> {selector}")
        return None
    selected_path, fragment = selector.removeprefix("local://").rsplit("#", 1)
    if not selected_path or not fragment:
        errors.append(f"EVIDENCE_SELECTOR_FORMAT {uid} -> {selector}")
        return None
    return selected_path, fragment


def _metadata_value(document: Any, fragment: str) -> Any:
    value = document
    for part in fragment.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def _validate_evidence(root: Path, item: dict[str, Any], errors: list[str]) -> None:
    uid = str(item.get("uid") or "<missing-uid>")
    props = properties(item)
    excerpt = props.get("excerpt")
    if not isinstance(excerpt, str) or not excerpt.strip():
        errors.append(f"EVIDENCE_EMPTY_EXCERPT {uid}")
        return

    expected_hash = hashlib.sha256(excerpt.encode("utf-8")).hexdigest()
    if props.get("excerpt_sha256") != expected_hash:
        errors.append(f"EVIDENCE_EXCERPT_HASH {uid}")

    local_path = props.get("local_path")
    path = _local_file(root, local_path, uid, errors)
    parts = _selector_parts(props.get("selector"), uid, errors)
    if path is None or parts is None:
        return
    selected_path, fragment = parts
    if selected_path != local_path:
        errors.append(
            f"EVIDENCE_SELECTOR_PATH_MISMATCH {uid} selector={selected_path} local_path={local_path}"
        )
        return

    line_match = LINE_SELECTOR.fullmatch(fragment)
    if line_match:
        start, end = (int(value) for value in line_match.groups())
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if start > end or end > len(lines):
            errors.append(
                f"EVIDENCE_SELECTOR_RANGE {uid} -> L{start}-L{end} lines={len(lines)}"
            )
            return
        selected_text = normalize_whitespace("\n".join(lines[start - 1 : end]))
        if normalize_whitespace(excerpt) not in selected_text:
            errors.append(f"EVIDENCE_SELECTOR_EXCERPT_MISMATCH {uid} -> L{start}-L{end}")
        return

    if fragment not in METADATA_FIELDS:
        errors.append(f"EVIDENCE_SELECTOR_UNSUPPORTED_FRAGMENT {uid} -> {fragment}")
        return
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"EVIDENCE_METADATA_PARSE {uid} -> {exc}")
        return
    selected_value = _metadata_value(document, fragment)
    if not isinstance(selected_value, str) or not selected_value.strip():
        errors.append(f"EVIDENCE_METADATA_FIELD {uid} -> {fragment}")
        return
    if normalize_whitespace(excerpt) != normalize_whitespace(selected_value):
        errors.append(f"EVIDENCE_METADATA_EXCERPT_MISMATCH {uid} -> {fragment}")


def validate_evidence_chain(
    *,
    root: Path,
    claims: list[dict[str, Any]],
    evidence: list[dict[str, Any]],
    sources: list[dict[str, Any]],
) -> dict[str, Any]:
    """Return deterministic errors without modifying repository artifacts."""
    evidence_errors: list[str] = []
    claim_errors: list[str] = []
    policy_errors: list[str] = []
    evidence_by_uid: dict[str, dict[str, Any]] = {}
    for item in evidence:
        uid = str(item.get("uid") or "")
        if uid in evidence_by_uid:
            evidence_errors.append(f"DUPLICATE_EVIDENCE_UID {uid}")
        evidence_by_uid[uid] = item
        _validate_evidence(root, item, evidence_errors)

    sources_by_uid = {str(item.get("uid") or ""): item for item in sources}
    trusted_claims = 0
    for claim in claims:
        uid = str(claim.get("uid") or "<missing-uid>")
        if claim.get("governance", {}).get("promotion_state") == "trusted":
            trusted_claims += 1

        claim_source_refs = source_refs(claim)
        claim_props = properties(claim)
        scope = claim_props.get("claim_scope")
        if scope == "source-reported assertion":
            for source_uid in claim_source_refs:
                source = sources_by_uid.get(source_uid)
                if source and (
                    source.get("status") == "metadata_only"
                    or source.get("content_tier") == "metadata_capsule"
                ):
                    policy_errors.append(f"METADATA_ONLY_SOURCE_REPORTED_CLAIM {uid} -> {source_uid}")

        refs = evidence_refs(claim)
        for evidence_uid in refs:
            if evidence_uid not in evidence_by_uid:
                claim_errors.append(f"CLAIM_BROKEN_EVIDENCE {uid} -> {evidence_uid}")

        method = claim.get("provenance", {}).get("method")
        if method not in DETERMINISTIC_CLAIM_METHODS:
            continue
        if len(refs) != 1 or refs[0] not in evidence_by_uid:
            claim_errors.append(f"DETERMINISTIC_CLAIM_EVIDENCE_CARDINALITY {uid} -> {len(refs)}")
            continue
        bound_evidence = evidence_by_uid[refs[0]]
        claim_text = claim_props.get("text")
        excerpt = properties(bound_evidence).get("excerpt")
        if not isinstance(claim_text, str) or not isinstance(excerpt, str) or (
            normalize_whitespace(claim_text) != normalize_whitespace(excerpt)
        ):
            claim_errors.append(f"CLAIM_EVIDENCE_TEXT_MISMATCH {uid} -> {refs[0]}")
        if set(claim_source_refs) != set(source_refs(bound_evidence)):
            claim_errors.append(f"CLAIM_EVIDENCE_SOURCE_MISMATCH {uid} -> {refs[0]}")

    if trusted_claims:
        policy_errors.append(f"TRUSTED_CLAIMS_MUST_BE_ZERO count={trusted_claims}")
    errors = evidence_errors + claim_errors + policy_errors
    return {
        "errors": errors,
        "evidence_errors": evidence_errors,
        "claim_errors": claim_errors,
        "policy_errors": policy_errors,
        "trusted_claims": trusted_claims,
        "evidence_count": len(evidence),
        "claim_count": len(claims),
    }
