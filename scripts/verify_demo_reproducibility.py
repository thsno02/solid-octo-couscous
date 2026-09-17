#!/usr/bin/env python3
"""Offline byte-for-byte replay of committed demo artifacts and validators."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments/v0_meta_kb_initialization_demo_260910"


def snapshot() -> dict[str, bytes]:
    return {
        path.relative_to(EXPERIMENT).as_posix(): path.read_bytes()
        for directory in sorted(EXPERIMENT.iterdir())
        if directory.is_dir() and directory.name[:2].isdigit()
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }


def changed_paths(before: dict[str, bytes], after: dict[str, bytes]) -> list[str]:
    """Return added, removed, or byte-changed generated paths."""

    return sorted(key for key in before.keys() | after.keys() if before.get(key) != after.get(key))


def make(target: str) -> None:
    subprocess.run(["make", target, f"PYTHON={sys.executable}"], cwd=ROOT, check=True)


def assert_equal(before: dict[str, bytes], label: str) -> None:
    after = snapshot()
    changed = changed_paths(before, after)
    if changed:
        raise SystemExit(f"{label}: changed generated files: {changed}")
    print(f"{label}: {len(after)} generated files byte-identical", flush=True)


def main() -> None:
    # The committed tree is part of the reproducibility contract.  Comparing
    # only two post-build snapshots can hide stale checked-in artifacts because
    # the first build may silently rewrite them before the comparison begins.
    committed = snapshot()
    make("demo")
    assert_equal(committed, "committed_tree_replay")

    first = snapshot()
    make("demo")
    assert_equal(first, "full_demo_replay")
    make("build-wiki")
    assert_equal(first, "compiler_only_replay")
    make("validate")
    assert_equal(first, "read_only_validation")


if __name__ == "__main__":
    main()
