#!/usr/bin/env python3
"""Normalize only structurally invalid legacy source types before full migration.

The original value is preserved as ``legacy_source_type``. This script does not
claim bibliographic verification and does not overwrite valid source types.
"""
from __future__ import annotations
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_data"
SCHEMA = RAW / "schemas" / "item.schema.yaml"
DIR_TO_TYPE = {
    "arxiv": "arxiv",
    "biorxiv": "biorxiv",
    "journal": "journal",
    "paper": "paper",
    "standard": "standard",
    "methodology": "methodology",
    "industry": "industry_doc",
    "blog": "blog",
    "githubs": "github",
    "dataset": "dataset",
    "benchmark": "benchmark",
    "incident": "incident",
    "x": "x",
}


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(data) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=110)


def main() -> int:
    schema = load(SCHEMA)
    allowed = set(schema["properties"]["source_type"]["enum"])
    if "biorxiv" not in allowed:
        allowed.add("biorxiv")
        enum = schema["properties"]["source_type"]["enum"]
        enum.insert(1, "biorxiv")
        SCHEMA.write_text(dump(schema), encoding="utf-8")

    changed = 0
    unresolved: list[str] = []
    for path in sorted(RAW.rglob("metadata.yaml")):
        data = load(path)
        if not isinstance(data, dict):
            continue
        parts = path.relative_to(RAW).parts
        directory_type = DIR_TO_TYPE.get(parts[0]) if parts else None
        current = data.get("source_type")
        normalized = str(current).lower().replace("-", "_") if current is not None else None
        if current is not None and current in allowed:
            continue
        if normalized in allowed:
            data["legacy_source_type"] = current
            data["source_type"] = normalized
        elif directory_type in allowed:
            if current is not None:
                data["legacy_source_type"] = current
            data["source_type"] = directory_type
        else:
            unresolved.append(path.relative_to(ROOT).as_posix())
            continue
        path.write_text(dump(data), encoding="utf-8")
        changed += 1

    print(f"legacy_source_type_normalization changed={changed} unresolved={len(unresolved)}")
    for item in unresolved:
        print(f"UNRESOLVED_SOURCE_TYPE {item}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    raise SystemExit(main())
