#!/usr/bin/env python3
"""Run source-family parallel materialization with optimized repo capsules."""
from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


parallel = load("materialize_parallel", ROOT / "scripts" / "materialize_parallel.py")
repo_wiki = load("repo_wiki_materializer", ROOT / "scripts" / "repo_wiki_materializer.py")
parallel.core.repo = lambda item, metadata_paths, timestamp: repo_wiki.materialize(
    item, metadata_paths, timestamp, parallel.core
)
raise SystemExit(parallel.main())
