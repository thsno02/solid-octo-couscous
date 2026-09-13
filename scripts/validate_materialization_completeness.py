#!/usr/bin/env python3
"""Validate that every collected source has an honest, locally consumable capsule."""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_data"
CORPUS = ROOT / "materialized_sources" / "corpus"
INDEX = ROOT / "materialized_sources" / "index.yaml"
REGISTRY = ROOT / "source_registry" / "registry.yaml"
AUDIT = ROOT / "raw_data" / "audits" / "materialization_completeness_2026-09-10.yaml"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    metadata_paths = sorted(RAW.rglob("metadata.yaml"))
    manifests = sorted(CORPUS.glob("*/manifest.yaml")) if CORPUS.exists() else []
    if len(manifests) != len(metadata_paths):
        errors.append(f"CAPSULE_COUNT metadata={len(metadata_paths)} manifests={len(manifests)}")

    seen_uids: set[str] = set()
    tiers: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    hashed_files = 0
    selector_count = 0

    for manifest_path in manifests:
        manifest = load_yaml(manifest_path)
        if not isinstance(manifest, dict):
            errors.append(f"MANIFEST_NOT_OBJECT {manifest_path.relative_to(ROOT)}")
            continue
        uid = str(manifest.get("uid") or "")
        if not uid:
            errors.append(f"MANIFEST_UID_MISSING {manifest_path.relative_to(ROOT)}")
        elif uid in seen_uids:
            errors.append(f"DUPLICATE_UID {uid}")
        seen_uids.add(uid)
        tier = str(manifest.get("content_tier") or "")
        status = str(manifest.get("status") or "")
        if tier not in {"full_text", "semantic_capsule", "excerpt_capsule", "metadata_capsule"}:
            errors.append(f"BAD_CONTENT_TIER {uid} {tier}")
        if status not in {"materialized", "partial", "metadata_only", "failed"}:
            errors.append(f"BAD_STATUS {uid} {status}")
        tiers[tier] += 1
        statuses[status] += 1

        metadata_path = manifest.get("metadata_path")
        if not isinstance(metadata_path, str) or not (ROOT / metadata_path).exists():
            errors.append(f"BROKEN_METADATA_PATH {uid} {metadata_path}")

        local_files = manifest.get("local_files")
        if not isinstance(local_files, list):
            errors.append(f"LOCAL_FILES_MISSING {uid}")
            continue
        for item in local_files:
            if not isinstance(item, dict):
                errors.append(f"LOCAL_FILE_BAD_ENTRY {uid}")
                continue
            raw_path = item.get("path")
            expected_hash = item.get("sha256")
            if not isinstance(raw_path, str) or not isinstance(expected_hash, str):
                errors.append(f"LOCAL_FILE_FIELDS {uid} {item}")
                continue
            path = ROOT / raw_path
            if not path.exists():
                errors.append(f"LOCAL_FILE_MISSING {uid} {raw_path}")
                continue
            actual = sha256_file(path)
            hashed_files += 1
            if actual != expected_hash:
                errors.append(f"HASH_MISMATCH {uid} {raw_path}")

        selectors_path = manifest_path.parent / "selectors.jsonl"
        if tier != "metadata_capsule" and not selectors_path.exists():
            errors.append(f"SELECTORS_MISSING {uid}")
        if selectors_path.exists():
            with selectors_path.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, 1):
                    if not line.strip():
                        continue
                    try:
                        selector = json.loads(line)
                    except json.JSONDecodeError as exc:
                        errors.append(f"SELECTOR_JSON {uid}:{line_number}: {exc}")
                        continue
                    selector_count += 1
                    local_path = selector.get("local_path")
                    if not isinstance(local_path, str) or not (ROOT / local_path).exists():
                        errors.append(f"SELECTOR_TARGET {uid}:{line_number}: {local_path}")

        if tier == "metadata_capsule" and not manifest.get("errors") and not manifest.get("warnings"):
            warnings.append(f"METADATA_ONLY_WITHOUT_DIAGNOSTIC {uid}")

    for path, label in ((INDEX, "INDEX"), (REGISTRY, "REGISTRY"), (AUDIT, "AUDIT")):
        if not path.exists():
            errors.append(f"{label}_MISSING {path.relative_to(ROOT)}")

    if INDEX.exists():
        index = load_yaml(INDEX)
        items = index.get("items") if isinstance(index, dict) else None
        if not isinstance(items, list) or len(items) != len(metadata_paths):
            errors.append(f"INDEX_COUNT expected={len(metadata_paths)} actual={len(items) if isinstance(items, list) else 'invalid'}")
        else:
            for item in items:
                path = item.get("manifest") if isinstance(item, dict) else None
                if not isinstance(path, str) or not (ROOT / path).exists():
                    errors.append(f"INDEX_MANIFEST_BROKEN {path}")

    if REGISTRY.exists():
        registry = load_yaml(REGISTRY)
        count = registry.get("entry_count") if isinstance(registry, dict) else None
        if count != len(metadata_paths):
            errors.append(f"REGISTRY_COUNT expected={len(metadata_paths)} actual={count}")

    if AUDIT.exists():
        audit = load_yaml(AUDIT)
        if not isinstance(audit, dict) or audit.get("local_capsules") != len(metadata_paths):
            errors.append("AUDIT_LOCAL_CAPSULE_COUNT")
        if isinstance(audit, dict) and not audit.get("all_records_local"):
            errors.append("AUDIT_ALL_RECORDS_LOCAL_FALSE")

    print(
        "materialization_completeness_validation "
        f"metadata={len(metadata_paths)} manifests={len(manifests)} "
        f"tiers={dict(tiers)} statuses={dict(statuses)} "
        f"hashes={hashed_files} selectors={selector_count} "
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
    print("\nAll collected source records have validated local capsules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
