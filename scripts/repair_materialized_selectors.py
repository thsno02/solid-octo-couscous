#!/usr/bin/env python3
"""Repair locally unresolvable generic selectors without refetching sources."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from materialize_all_sources import (
    AUDIT_ROOT,
    CORPUS_ROOT,
    MATERIALIZED_ROOT,
    ROOT,
    discover_records,
    filter_selectors_for_document,
    finalize_capsule,
    has_substantive_document_text,
    load_yaml,
    rebuild_registry,
    write_indexes_and_audit,
    write_jsonl,
    write_yaml,
)

REPAIR_AUDIT = AUDIT_ROOT / "materialization_selector_repair_2026-09-16.yaml"


def load_selectors(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            if isinstance(row, dict):
                rows.append(row)
    return rows


def sample_selector_cases(records: list[Any], manifests: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    limits = {"arxiv": 10, "github": 10, "web_or_standard": 5}
    counts: Counter[str] = Counter()
    cases: list[dict[str, Any]] = []
    for record in sorted(records, key=lambda item: (item.source_type, item.uid)):
        if record.priority != "P0":
            continue
        category = (
            record.source_type
            if record.source_type in {"arxiv", "github"}
            else "web_or_standard"
        )
        if counts[category] >= limits[category]:
            continue
        manifest = manifests[record.uid]
        if manifest.get("content_tier") == "metadata_capsule":
            continue
        selectors = load_selectors(record.capsule_root / "selectors.jsonl")
        if not selectors:
            continue
        selector = selectors[0]
        local_path = selector.get("local_path")
        local_file = ROOT / str(local_path)
        declared = {
            item.get("path")
            for item in manifest.get("local_files", [])
            if isinstance(item, dict)
        }
        text = local_file.read_text(encoding="utf-8") if local_file.is_file() else ""
        preview = selector.get("text_preview")
        start_line = selector.get("start_line")
        end_line = selector.get("end_line")
        page = selector.get("page")
        checks = {
            "local_file_exists": local_file.is_file(),
            "target_is_hashed": local_path in declared,
            "preview_resolves": preview is None or (isinstance(preview, str) and preview in text),
            "line_range_resolves": start_line is None
            or (
                isinstance(start_line, int)
                and isinstance(end_line, int)
                and 1 <= start_line <= end_line <= max(1, len(text.splitlines()))
            ),
            "page_resolves": page is None or f"## Page {page}" in text,
        }
        cases.append(
            {
                "category": category,
                "uid": record.uid,
                "local_path": local_path,
                "selector": selector.get("selector"),
                "result": "pass" if all(checks.values()) else "fail",
                "checks": checks,
            }
        )
        counts[category] += 1
        if all(counts[key] >= value for key, value in limits.items()):
            break
    return cases


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Write repairs; default is a dry run.")
    args = parser.parse_args()

    records = discover_records()
    changes: list[dict[str, Any]] = []
    manifests: dict[str, dict[str, Any]] = {}
    for record in records:
        manifest_path = record.capsule_root / "manifest.yaml"
        manifest = load_yaml(manifest_path)
        if not isinstance(manifest, dict):
            raise SystemExit(f"invalid manifest: {manifest_path.relative_to(ROOT)}")
        manifests[record.uid] = manifest
        if manifest.get("adapter") != "generic_web_or_document_v2":
            continue
        materialization = manifest.get("materialization")
        if not isinstance(materialization, dict) or not materialization.get("document"):
            continue
        document_path = record.capsule_root / str(materialization["document"])
        if not document_path.is_file():
            continue
        document_text = document_path.read_text(encoding="utf-8")
        selectors_path = record.capsule_root / "selectors.jsonl"
        original = load_selectors(selectors_path)
        filtered, omitted = filter_selectors_for_document(original, document_text)
        substantive = has_substantive_document_text(document_text)
        old_status = manifest.get("status")
        old_tier = manifest.get("content_tier")
        open_truncated = any(
            "Open text exceeded the configured local character budget" in str(warning)
            for warning in manifest.get("warnings", [])
        )
        if not substantive:
            filtered = []
            manifest["status"] = "metadata_only"
            manifest["content_tier"] = "metadata_capsule"
            manifest["selectors"] = []
            warning = (
                "Retrieved document contained no substantive non-heading text; "
                "retained only as acquisition evidence."
            )
            if warning not in manifest.setdefault("warnings", []):
                manifest["warnings"].append(warning)
        elif open_truncated:
            manifest["status"] = "partial"
            manifest["content_tier"] = "excerpt_capsule"
        changed = (
            filtered != original
            or manifest.get("status") != old_status
            or manifest.get("content_tier") != old_tier
        )
        if not changed:
            continue
        materialization["selector_count"] = len(filtered)
        materialization["substantive_text"] = substantive
        materialization["content_was_truncated"] = bool(open_truncated or omitted)
        materialization["omitted_selector_count"] = omitted
        if filtered:
            manifest["selectors"] = ["selectors.jsonl"]
        repair_warning = f"Offline selector repair omitted {omitted} locally unresolvable selectors."
        if omitted and repair_warning not in manifest.setdefault("warnings", []):
            manifest["warnings"].append(repair_warning)
        changes.append(
            {
                "uid": record.uid,
                "old_status": old_status,
                "new_status": manifest.get("status"),
                "old_content_tier": old_tier,
                "new_content_tier": manifest.get("content_tier"),
                "selectors_before": len(original),
                "selectors_after": len(filtered),
                "selectors_omitted": omitted,
                "substantive_text": substantive,
            }
        )
        if args.apply:
            write_jsonl(selectors_path, filtered)
            manifests[record.uid] = finalize_capsule(record, record.capsule_root, manifest)

    mode = "apply" if args.apply else "dry-run"
    print(f"selector_repair mode={mode} capsules={len(changes)} omitted={sum(c['selectors_omitted'] for c in changes)}")
    for change in changes:
        print(
            f"- {change['uid']}: {change['old_status']}/{change['old_content_tier']} -> "
            f"{change['new_status']}/{change['new_content_tier']}; "
            f"selectors {change['selectors_before']} -> {change['selectors_after']}"
        )
    if not args.apply:
        return 0

    index = load_yaml(MATERIALIZED_ROOT / "index.yaml")
    generated_at = str(index.get("generated_at")) if isinstance(index, dict) else "offline-repair"
    rebuild_registry(records, manifests, generated_at)
    write_indexes_and_audit(records, manifests, generated_at)
    samples = sample_selector_cases(records, manifests)
    sample_counts = Counter(case["category"] for case in samples if case["result"] == "pass")
    write_yaml(
        REPAIR_AUDIT,
        {
            "audit_id": "materialization-selector-repair-2026-09-16",
            "mode": "offline-no-refetch",
            "changed_capsules": len(changes),
            "selectors_omitted": sum(change["selectors_omitted"] for change in changes),
            "changes": changes,
            "p0_selector_sample_requirements": {"arxiv": 10, "github": 10, "web_or_standard": 5},
            "p0_selector_sample_pass_counts": dict(sample_counts),
            "p0_selector_samples": samples,
        },
    )
    if sample_counts != Counter({"arxiv": 10, "github": 10, "web_or_standard": 5}):
        raise SystemExit(f"P0 selector sample incomplete: {dict(sample_counts)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
