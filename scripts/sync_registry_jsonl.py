#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = ROOT / "source_registry" / "registry.yaml"
JSONL_PATH = ROOT / "source_registry" / "registry.jsonl"


def main() -> int:
    registry = yaml.safe_load(YAML_PATH.read_text(encoding="utf-8"))
    entries = registry.get("entries", []) if isinstance(registry, dict) else []
    with JSONL_PATH.open("w", encoding="utf-8") as handle:
        for entry in entries:
            handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"source_registry_jsonl_entries={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
