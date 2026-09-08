#!/usr/bin/env python3
"""Validate raw_data YAML syntax, references, identifiers, and migrated metadata.

Legacy metadata is allowed during migration. A metadata record is validated against
item.schema.yaml only when all required top-level fields are present; incomplete
legacy records produce warnings rather than blocking the collection.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = REPO_ROOT / "raw_data"
ITEM_SCHEMA_PATH = RAW_ROOT / "schemas" / "item.schema.yaml"


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def collect_index_paths(index: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for section in (
        "additive_manifests",
        "collections",
        "audits",
        "schemas",
        "guides",
        "quarantine",
    ):
        value = index.get(section, [])
        if isinstance(value, dict):
            value = [value]
        for item in value or []:
            if isinstance(item, dict) and isinstance(item.get("path"), str):
                refs.append(item["path"])
    return refs


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    parsed: dict[Path, Any] = {}

    yaml_paths = sorted(RAW_ROOT.rglob("*.yaml"))
    for path in yaml_paths:
        try:
            parsed[path] = load_yaml(path)
        except Exception as exc:  # PyYAML emits several useful subclasses.
            errors.append(f"YAML_PARSE {relative(path)}: {exc}")

    if errors:
        print("\n".join(errors))
        return 1

    item_schema = parsed.get(ITEM_SCHEMA_PATH)
    if not isinstance(item_schema, dict):
        errors.append(f"SCHEMA_MISSING {relative(ITEM_SCHEMA_PATH)}")
        print("\n".join(errors))
        return 1

    required = set(item_schema.get("required", []))
    validator = Draft202012Validator(item_schema, format_checker=FormatChecker())

    migrated_count = 0
    legacy_count = 0
    canonical_occurrences: dict[tuple[str, str], list[str]] = defaultdict(list)

    for path, data in parsed.items():
        if path.name != "metadata.yaml" or not isinstance(data, dict):
            continue

        source_type = str(data.get("source_type") or data.get("source") or "unknown")
        canonical_id = data.get("canonical_id")
        if canonical_id is None:
            canonical_id = data.get("arxiv_id") or data.get("doi") or data.get("repo")
        if canonical_id:
            canonical_occurrences[(source_type.lower(), str(canonical_id).lower())].append(relative(path))

        missing = sorted(required.difference(data.keys()))
        if missing:
            legacy_count += 1
            warnings.append(f"MIGRATION_PENDING {relative(path)} missing={','.join(missing)}")
            continue

        migrated_count += 1
        for validation_error in sorted(validator.iter_errors(data), key=lambda err: list(err.path)):
            pointer = "/".join(str(part) for part in validation_error.path) or "<root>"
            errors.append(
                f"SCHEMA {relative(path)} at {pointer}: {validation_error.message}"
            )

    for key, locations in sorted(canonical_occurrences.items()):
        if len(locations) > 1:
            errors.append(
                f"DUPLICATE_CANONICAL_ID source={key[0]} id={key[1]} files={' | '.join(locations)}"
            )

    index_path = RAW_ROOT / "index.yaml"
    index = parsed.get(index_path)
    if not isinstance(index, dict):
        errors.append(f"INDEX_MISSING {relative(index_path)}")
    else:
        for referenced in collect_index_paths(index):
            target = RAW_ROOT / referenced
            if not target.exists():
                errors.append(f"BROKEN_INDEX_REFERENCE {referenced}")

        for manifest_ref in index.get("additive_manifests", []) or []:
            if not isinstance(manifest_ref, dict) or not manifest_ref.get("path"):
                continue
            manifest_path = RAW_ROOT / str(manifest_ref["path"])
            manifest = parsed.get(manifest_path)
            if not isinstance(manifest, dict):
                continue
            for item in manifest.get("items", []) or []:
                if not isinstance(item, dict) or not item.get("path"):
                    continue
                item_path = RAW_ROOT / str(item["path"])
                if not item_path.exists():
                    errors.append(
                        f"BROKEN_MANIFEST_REFERENCE {relative(manifest_path)} -> {item['path']}"
                    )

    print(
        "validation_summary "
        f"yaml_files={len(yaml_paths)} "
        f"metadata_migrated={migrated_count} "
        f"metadata_legacy={legacy_count} "
        f"warnings={len(warnings)} "
        f"errors={len(errors)}"
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

    print("\nRaw data validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
