#!/usr/bin/env python3
"""Materialize source families concurrently with bounded failure domains.

arXiv and GitHub use separate worker pools so a slow scholarly-source endpoint
cannot block repository semanticization, and a large repository cannot block
paper acquisition. Outputs remain deterministic per frozen revision.
"""
from __future__ import annotations
import argparse
import importlib.util
import time
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "materialize_pipeline.py"
SPEC = importlib.util.spec_from_file_location("materialize_pipeline", TARGET)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load {TARGET}")
core = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(core)


def bounded_curl(url: str):
    request = urllib.request.Request(url, headers={"User-Agent": core.UA, "Accept": "*/*"})
    last_error = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                return response.read(), response.geturl(), dict(response.headers)
        except Exception as exc:
            last_error = exc
            if attempt == 0:
                time.sleep(2)
    raise RuntimeError(f"{url}: {last_error}")


core.curl = bounded_curl


def failed(kind: str, canonical_id: str, timestamp: str, error: Exception):
    root = core.OUT / kind / core.key(canonical_id)
    record = {
        "manifest_version": 1,
        "source_type": kind,
        "canonical_id": canonical_id,
        "status": "failed",
        "generated_at": timestamp,
        "errors": [f"unhandled-materializer-error: {type(error).__name__}: {error}"],
    }
    core.write(root / "manifest.yaml", record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="pipeline/materialization.yaml")
    parser.add_argument("--arxiv-workers", type=int, default=2)
    parser.add_argument("--github-workers", type=int, default=3)
    args = parser.parse_args()

    config = yaml.safe_load((ROOT / args.config).read_text(encoding="utf-8"))
    timestamp = str(config.get("generated_at") or core.now())
    core.ensure_schema()
    core.migrate("2026-09-09")
    metadata_paths = core.metapaths()
    results = []
    futures = {}

    with ThreadPoolExecutor(max_workers=max(1, args.arxiv_workers)) as arxiv_pool, \
         ThreadPoolExecutor(max_workers=max(1, args.github_workers)) as github_pool:
        for position, item in enumerate(config.get("arxiv", {}).get("items", [])):
            def arxiv_task(record=item, stagger=position):
                time.sleep(min(stagger, max(1, args.arxiv_workers)) * 1.5)
                return core.arxiv(record, metadata_paths, timestamp)
            futures[arxiv_pool.submit(arxiv_task)] = ("arxiv", str(item["id"]))
        for item in config.get("github", {}).get("items", []):
            futures[github_pool.submit(core.repo, item, metadata_paths, timestamp)] = (
                "github", str(item["repo"])
            )

        for future in as_completed(futures):
            kind, canonical_id = futures[future]
            try:
                result = future.result()
            except Exception as exc:
                result = failed(kind, canonical_id, timestamp, exc)
            results.append(result)
            print(f"completed {kind} {canonical_id} status={result.get('status')}", flush=True)

    results.sort(key=lambda value: (str(value.get("source_type")), str(value.get("canonical_id"))))
    core.OUT.mkdir(exist_ok=True)
    core.write(
        core.OUT / "index.yaml",
        {
            "materialization_index_version": 1,
            "generated_at": timestamp,
            "execution": {
                "mode": "source-family-isolated-parallel",
                "arxiv_workers": args.arxiv_workers,
                "github_workers": args.github_workers,
            },
            "summary": dict(Counter(str(item.get("status")) for item in results)),
            "items": [
                {
                    "source_type": item.get("source_type"),
                    "canonical_id": item.get("canonical_id"),
                    "status": item.get("status"),
                    "manifest": (
                        f"materialized_sources/{item.get('source_type')}/"
                        f"{core.key(item.get('canonical_id'))}/manifest.yaml"
                    ),
                }
                for item in results
            ],
        },
    )
    (core.OUT / "README.md").write_text(
        "# Materialized sources\n\n"
        "Source-specific frozen artifacts. arXiv stores TeX and selectors; GitHub stores "
        "commit-pinned semantic capsules, not repository contents. Source families execute in "
        "separate bounded worker pools.\n",
        encoding="utf-8",
    )
    core.registry(timestamp)
    usable = sum(item.get("status") in {"materialized", "partial"} for item in results)
    print(f"parallel_materialization usable={usable} total={len(results)}")
    return 0 if usable >= int(config.get("minimum_usable_items", 1)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
