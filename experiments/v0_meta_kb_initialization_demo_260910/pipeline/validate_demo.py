#!/usr/bin/env python3
"""Validate the v0 meta-KB experiment and its local evidence chain."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from evidence_validation import validate_evidence_chain
from rights_propagation import rights_snapshot, source_rights, validate_page_rights

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
KNOWLEDGE_SCHEMA = ROOT / "raw_data" / "schemas" / "knowledge_model.schema.yaml"
WIKI_SCHEMA = ROOT / "raw_data" / "schemas" / "wiki_page.schema.yaml"
REGISTRY = ROOT / "source_registry" / "registry.yaml"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_yaml(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110), encoding="utf-8")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{line_number} is not an object")
            rows.append(value)
    return rows


def parse_frontmatter_and_body(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    value = yaml.safe_load(text[4:end])
    if not isinstance(value, dict):
        raise ValueError("frontmatter is not an object")
    return value, text[end + 5 :]


def parse_frontmatter(path: Path) -> dict[str, Any]:
    return parse_frontmatter_and_body(path)[0]


def schema_errors(validator: Draft202012Validator, value: dict[str, Any], prefix: str) -> list[str]:
    errors: list[str] = []
    for issue in sorted(validator.iter_errors(value), key=lambda error: list(error.path)):
        pointer = "/".join(str(part) for part in issue.path) or "<root>"
        errors.append(f"{prefix} at {pointer}: {issue.message}")
    return errors


def main(*, write_reports: bool = False) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [
        "00_inputs/materialization_snapshot.yaml",
        "00_inputs/selected_sources.yaml",
        "01_ontology/meta_kb_ontology.yaml",
        "01_ontology/schema_bindings.yaml",
        "02_entities/sources.jsonl",
        "02_entities/domains.jsonl",
        "03_evidence/evidence.jsonl",
        "04_claims/claims.jsonl",
        "04_claims/contradictions.jsonl",
        "05_wiki/index.md",
        "06_evaluation/report.yaml",
        "07_review/queue.yaml",
        "08_release/manifest.yaml",
    ]
    for relative in required:
        if not (EXPERIMENT_ROOT / relative).exists():
            errors.append(f"MISSING {relative}")

    if errors:
        for error in errors:
            print(error)
        return 1

    knowledge_schema = load_yaml(KNOWLEDGE_SCHEMA)
    wiki_schema = load_yaml(WIKI_SCHEMA)
    knowledge_validator = Draft202012Validator(knowledge_schema, format_checker=FormatChecker())
    wiki_validator = Draft202012Validator(wiki_schema, format_checker=FormatChecker())

    source_entities = load_jsonl(EXPERIMENT_ROOT / "02_entities" / "sources.jsonl")
    domain_entities = load_jsonl(EXPERIMENT_ROOT / "02_entities" / "domains.jsonl")
    evidence = load_jsonl(EXPERIMENT_ROOT / "03_evidence" / "evidence.jsonl")
    claims = load_jsonl(EXPERIMENT_ROOT / "04_claims" / "claims.jsonl")
    contradictions = load_jsonl(EXPERIMENT_ROOT / "04_claims" / "contradictions.jsonl")
    all_objects = source_entities + domain_entities + evidence + claims + contradictions

    object_ids: set[str] = set()
    for obj in all_objects:
        uid = str(obj.get("uid") or "")
        if not uid:
            errors.append("OBJECT_WITHOUT_UID")
            continue
        if uid in object_ids:
            errors.append(f"DUPLICATE_OBJECT_UID {uid}")
        object_ids.add(uid)
        errors.extend(schema_errors(knowledge_validator, obj, f"OBJECT {uid}"))

    evidence_by_uid = {str(item["uid"]): item for item in evidence}
    claims_by_uid = {str(item["uid"]): item for item in claims}
    for claim in claims:
        uid = str(claim["uid"])
        refs = claim.get("epistemic", {}).get("evidence_refs", [])
        if not refs:
            errors.append(f"CLAIM_WITHOUT_EVIDENCE {uid}")
        for ref in refs:
            if ref not in evidence_by_uid:
                errors.append(f"CLAIM_BROKEN_EVIDENCE {uid} -> {ref}")

    registry = load_yaml(REGISTRY)
    source_uids = {
        str(entry.get("uid"))
        for entry in registry.get("entries", [])
        if isinstance(registry, dict) and isinstance(entry, dict)
    }
    selected = load_yaml(EXPERIMENT_ROOT / "00_inputs" / "selected_sources.yaml")
    selected_sources = selected.get("sources") if isinstance(selected, dict) else []
    selected_by_uid = {
        str(item.get("uid")): item for item in selected_sources if isinstance(item, dict)
    }
    selected_uids = {str(item.get("uid")) for item in selected_sources if isinstance(item, dict)}
    missing_registry = sorted(selected_uids - source_uids)
    if missing_registry:
        errors.append(f"SELECTED_NOT_IN_REGISTRY {missing_registry}")

    source_entities_by_uid = {
        str(item.get("semantics", {}).get("property_assertions", {}).get("source_uid") or ""): item
        for item in source_entities
    }
    for source_uid, source in selected_by_uid.items():
        entity = source_entities_by_uid.get(source_uid)
        props = entity.get("semantics", {}).get("property_assertions", {}) if entity else {}
        if not entity:
            errors.append(f"RIGHTS_SOURCE_ENTITY_MISSING {source_uid}")
        elif props.get("rights_status") != source.get("rights_status") or rights_snapshot(props.get("rights")) != source_rights(source):
            errors.append(f"RIGHTS_SOURCE_ENTITY_MISMATCH {source_uid}")

    evidence_validation = validate_evidence_chain(
        root=ROOT,
        claims=claims,
        evidence=evidence,
        sources=[item for item in selected_sources if isinstance(item, dict)],
    )
    for error in evidence_validation["errors"]:
        if error not in errors:
            errors.append(error)
    trusted_claims = int(evidence_validation["trusted_claims"])

    wiki_pages = sorted((EXPERIMENT_ROOT / "05_wiki").rglob("*.md"))
    page_ids: set[str] = set()
    referenced_claims: Counter[str] = Counter()
    for path in wiki_pages:
        try:
            frontmatter, body = parse_frontmatter_and_body(path)
        except Exception as exc:
            errors.append(f"WIKI_FRONTMATTER {path.relative_to(EXPERIMENT_ROOT)}: {exc}")
            continue
        uid = str(frontmatter.get("uid") or "")
        if uid in page_ids:
            errors.append(f"DUPLICATE_PAGE_UID {uid}")
        page_ids.add(uid)
        errors.extend(schema_errors(wiki_validator, frontmatter, f"PAGE {path.relative_to(EXPERIMENT_ROOT)}"))
        for ref in frontmatter.get("claim_refs", []):
            referenced_claims[str(ref)] += 1
            if ref not in claims_by_uid:
                errors.append(f"PAGE_BROKEN_CLAIM {path.relative_to(EXPERIMENT_ROOT)} -> {ref}")
        for source_ref in frontmatter.get("source_refs", []):
            if source_ref not in source_uids:
                errors.append(f"PAGE_BROKEN_SOURCE {path.relative_to(EXPERIMENT_ROOT)} -> {source_ref}")
        rendered = frontmatter.get("rendered_claim_refs", [])
        if not isinstance(rendered, list) or not set(str(ref) for ref in rendered).issubset(
            set(str(ref) for ref in frontmatter.get("claim_refs", []))
        ):
            errors.append(f"PAGE_RENDERED_CLAIMS_MISMATCH {path.relative_to(EXPERIMENT_ROOT)}")
        errors.extend(
            validate_page_rights(
                owner=path.relative_to(EXPERIMENT_ROOT).as_posix(),
                frontmatter=frontmatter,
                body=body,
                claims_by_uid=claims_by_uid,
                sources_by_uid=selected_by_uid,
            )
        )

    unreferenced_claims = sorted(set(claims_by_uid) - set(referenced_claims))
    if unreferenced_claims:
        warnings.append(f"UNREFERENCED_CLAIMS count={len(unreferenced_claims)}")

    review_queue = load_yaml(EXPERIMENT_ROOT / "07_review" / "queue.yaml")
    review_items = review_queue.get("items") if isinstance(review_queue, dict) else []
    queued_claims = {str(item.get("claim_ref")) for item in review_items if isinstance(item, dict)}
    if queued_claims != set(claims_by_uid):
        errors.append(
            f"REVIEW_QUEUE_MISMATCH claims={len(claims_by_uid)} queued={len(queued_claims)}"
        )

    release = load_yaml(EXPERIMENT_ROOT / "08_release" / "manifest.yaml")
    if not isinstance(release, dict) or release.get("release_state") != "candidate":
        errors.append("RELEASE_STATE_MUST_BE_CANDIDATE")
    release_trusted_claims = release.get("trusted_claims") if isinstance(release, dict) else None
    if trusted_claims != 0 or release_trusted_claims != 0:
        errors.append("V0_MUST_NOT_AUTO_PROMOTE_TRUSTED_CLAIMS")

    validation = {
        "validation_id": "validation:v0-meta-kb-initialization-demo-260910",
        "status": "passed" if not errors else "failed",
        "counts": {
            "selected_sources": len(selected_uids),
            "source_entities": len(source_entities),
            "domain_entities": len(domain_entities),
            "evidence": len(evidence),
            "claims": len(claims),
            "wiki_pages": len(wiki_pages),
            "review_items": len(review_items),
            "trusted_claims": trusted_claims,
        },
        "checks": {
            "knowledge_object_schema": "pass" if not any(error.startswith("OBJECT ") for error in errors) else "fail",
            "wiki_page_schema": "pass" if not any(error.startswith("PAGE ") or error.startswith("WIKI_") for error in errors) else "fail",
            "claim_to_evidence_integrity": "pass" if not (
                evidence_validation["evidence_errors"]
                or evidence_validation["claim_errors"]
                or evidence_validation["rights_errors"]
                or any(
                    error.startswith(("CLAIM_WITHOUT_EVIDENCE", "CLAIM_BROKEN_EVIDENCE"))
                    for error in errors
                )
            ) else "fail",
            "local_evidence_resolution": "pass" if not evidence_validation["evidence_errors"] else "fail",
            "evidence_content_integrity": "pass" if not evidence_validation["evidence_errors"] else "fail",
            "rights_propagation": "pass" if not any(
                error.startswith(("RIGHTS_", "CLAIM_RIGHTS_", "CLAIM_SCOPE_", "CLAIM_EVIDENCE_", "EVIDENCE_RIGHTS_", "COLLECTOR_"))
                for error in errors
            ) else "fail",
            "metadata_only_source_policy": "pass" if not any(
                error.startswith("METADATA_ONLY_SOURCE_REPORTED_CLAIM")
                for error in evidence_validation["policy_errors"]
            ) else "fail",
            "source_registry_integrity": "pass" if not missing_registry else "fail",
            "review_queue_complete": "pass" if queued_claims == set(claims_by_uid) else "fail",
            "no_automatic_trust_promotion": "pass" if trusted_claims == 0 and release_trusted_claims == 0 else "fail",
        },
        "warnings": warnings,
        "errors": errors,
        "interpretation": "Passing proves structural and referential integrity, not scientific truth.",
    }
    if write_reports:
        write_yaml(EXPERIMENT_ROOT / "06_evaluation" / "validation.yaml", validation)

        report_path = EXPERIMENT_ROOT / "06_evaluation" / "report.yaml"
        report = load_yaml(report_path)
        if isinstance(report, dict) and isinstance(report.get("checks"), dict):
            report_counts = report.get("counts")
            if isinstance(report_counts, dict):
                report_counts.update(
                    {
                        "selected_sources": validation["counts"]["selected_sources"],
                        "source_entities": validation["counts"]["source_entities"],
                        "domain_entities": validation["counts"]["domain_entities"],
                        "evidence_objects": validation["counts"]["evidence"],
                        "claim_objects": validation["counts"]["claims"],
                        "wiki_pages": validation["counts"]["wiki_pages"],
                        "review_items": validation["counts"]["review_items"],
                        "trusted_claims": validation["counts"]["trusted_claims"],
                    }
                )
            report["checks"].update(
                {
                    "evidence_created_for_every_claim": validation["checks"]["claim_to_evidence_integrity"],
                    "claim_schema": validation["checks"]["knowledge_object_schema"],
                    "wiki_page_schema": validation["checks"]["wiki_page_schema"],
                    "local_evidence_resolution": validation["checks"]["local_evidence_resolution"],
                    "evidence_content_integrity": validation["checks"]["evidence_content_integrity"],
                }
            )
            report["validation_status"] = validation["status"]
            write_yaml(report_path, report)

    print(
        "demo_validation "
        f"sources={len(selected_uids)} objects={len(all_objects)} claims={len(claims)} "
        f"evidence={len(evidence)} wiki_pages={len(wiki_pages)} "
        f"warnings={len(warnings)} errors={len(errors)}"
    )
    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nThe v0 meta-KB demo passed deterministic validation.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write-report",
        action="store_true",
        help="write validation.yaml and update report.yaml (builders only)",
    )
    sys.exit(main(write_reports=parser.parse_args().write_report))
