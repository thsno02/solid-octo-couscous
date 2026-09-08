#!/usr/bin/env python3
"""Replace unstable arXiv @latest selectors with content-hash revisions."""
from __future__ import annotations
import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "materialized_sources" / "arxiv"


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(value) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def main() -> int:
    changed = 0
    if not BASE.exists():
        print("No arXiv materializations; selector pinning skipped.")
        return 0
    for manifest_path in sorted(BASE.glob("*/manifest.yaml")):
        manifest = load(manifest_path)
        if not isinstance(manifest, dict) or manifest.get("status") == "failed":
            continue
        archive_hash = ((manifest.get("download") or {}).get("archive_sha256"))
        if not archive_hash:
            raise RuntimeError(f"Missing archive hash: {manifest_path}")
        revision = f"sha256-{archive_hash}"
        selectors_path = manifest_path.parent / "selectors.jsonl"
        rows = []
        for line in selectors_path.read_text(encoding="utf-8").splitlines():
            if not line:
                continue
            row = json.loads(line)
            row["selector"] = str(row["selector"]).replace("@latest/", f"@{revision}/")
            row["source_revision"] = revision
            rows.append(row)
        with selectors_path.open("w", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
        manifest["source_revision"] = {
            "identity": manifest.get("canonical_id"),
            "revision_scheme": "content-sha256",
            "revision": revision,
            "arxiv_version": None,
            "note": "The exact arXiv version was not independently resolved; the downloaded bytes are pinned by hash.",
        }
        materialization = manifest.setdefault("materialization", {})
        materialization["selector_revision"] = revision
        materialization["selector_count"] = len(rows)
        manifest_path.write_text(dump(manifest), encoding="utf-8")
        changed += 1
    print(f"pinned_arxiv_selector_manifests={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
