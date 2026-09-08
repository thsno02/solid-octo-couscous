#!/usr/bin/env python3
"""Copy current materializations into immutable revision-addressed snapshots.

Git deduplicates identical blobs, so explicit revision paths improve addressability
without multiplying repository object storage for unchanged content.
"""
from __future__ import annotations
import json
import shutil
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "materialized_sources"
SNAPSHOTS = OUT / "snapshots"
REGISTRY = ROOT / "source_registry" / "registry.yaml"


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def dump(value) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def key(value: str) -> str:
    return value.replace("/", "--")


def rewrite_excerpt_paths(snapshot: Path, current: Path) -> None:
    path = snapshot / "evidence" / "excerpts.jsonl"
    if not path.exists():
        return
    current_prefix = current.relative_to(ROOT).as_posix()
    snapshot_prefix = snapshot.relative_to(ROOT).as_posix()
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        row = json.loads(line)
        local_path = row.get("local_path")
        if isinstance(local_path, str) and local_path.startswith(current_prefix):
            row["local_path"] = snapshot_prefix + local_path[len(current_prefix):]
        rows.append(row)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def snapshot_for(manifest: dict, current: Path) -> Path | None:
    source_type = manifest.get("source_type")
    canonical_id = str(manifest.get("canonical_id"))
    if source_type == "github":
        revision = ((manifest.get("source_revision") or {}).get("commit"))
        if not revision:
            return None
        return SNAPSHOTS / "github" / key(canonical_id) / str(revision)
    if source_type == "arxiv":
        revision = ((manifest.get("download") or {}).get("archive_sha256"))
        if not revision:
            return None
        return SNAPSHOTS / "arxiv" / key(canonical_id) / f"sha256-{revision}"
    return None


def main() -> int:
    archived = 0
    snapshot_by_uid: dict[tuple[str, str], str] = {}
    for source_type in ("arxiv", "github"):
        family = OUT / source_type
        if not family.exists():
            continue
        for manifest_path in sorted(family.glob("*/manifest.yaml")):
            manifest = load(manifest_path)
            if not isinstance(manifest, dict) or manifest.get("status") == "failed":
                continue
            current = manifest_path.parent
            snapshot = snapshot_for(manifest, current)
            if snapshot is None:
                raise RuntimeError(f"No immutable revision for {manifest_path}")
            if not snapshot.exists():
                snapshot.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(current, snapshot)
                rewrite_excerpt_paths(snapshot, current)
                snapshot_manifest_path = snapshot / "manifest.yaml"
                snapshot_manifest = load(snapshot_manifest_path)
                snapshot_manifest["immutable_snapshot"] = {
                    "path": snapshot.relative_to(ROOT).as_posix(),
                    "immutable": True,
                    "source_control": "git",
                }
                materialization = snapshot_manifest.setdefault("materialization", {})
                materialization["root"] = snapshot.relative_to(ROOT).as_posix()
                snapshot_manifest_path.write_text(dump(snapshot_manifest), encoding="utf-8")
                archived += 1
            snapshot_ref = snapshot.relative_to(ROOT).as_posix()
            manifest["immutable_snapshot"] = {
                "path": snapshot_ref,
                "immutable": True,
                "source_control": "git",
            }
            manifest_path.write_text(dump(manifest), encoding="utf-8")
            snapshot_by_uid[(source_type, str(manifest.get("canonical_id")).lower())] = snapshot_ref

    index_path = OUT / "index.yaml"
    if index_path.exists():
        index = load(index_path)
        for item in index.get("items", []):
            item["snapshot"] = snapshot_by_uid.get(
                (str(item.get("source_type")), str(item.get("canonical_id")).lower())
            )
        index["immutable_snapshots"] = {
            "root": "materialized_sources/snapshots",
            "created_in_this_run": archived,
            "addressed_by": "git-commit-or-content-sha256",
        }
        index_path.write_text(dump(index), encoding="utf-8")

    if REGISTRY.exists():
        registry = load(REGISTRY)
        for entry in registry.get("entries", []):
            ref = snapshot_by_uid.get(
                (str(entry.get("source_type")), str(entry.get("canonical_id")).lower())
            )
            if ref:
                entry.setdefault("materialization", {})["immutable_snapshot"] = ref
        REGISTRY.write_text(dump(registry), encoding="utf-8")

    print(f"immutable_materialization_snapshots_created={archived}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
