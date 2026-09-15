#!/usr/bin/env python3
"""Offline byte-for-byte replay of the demo, compiler and read-only validators."""
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


def make(target: str) -> None:
    subprocess.run(["make", target, f"PYTHON={sys.executable}"], cwd=ROOT, check=True)


def assert_equal(before: dict[str, bytes], label: str) -> None:
    after = snapshot()
    changed = sorted(key for key in before.keys() | after.keys() if before.get(key) != after.get(key))
    if changed:
        raise SystemExit(f"{label}: changed generated files: {changed}")
    print(f"{label}: {len(after)} generated files byte-identical", flush=True)


def main() -> None:
    make("demo")
    first = snapshot()
    make("demo")
    assert_equal(first, "full_demo_replay")
    make("build-wiki")
    assert_equal(first, "compiler_only_replay")
    make("validate")
    assert_equal(first, "read_only_validation")


if __name__ == "__main__":
    main()
