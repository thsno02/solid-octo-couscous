from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest import mock

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

import verify_demo_reproducibility as replay


class ReproducibilityGuardTests(unittest.TestCase):
    def test_changed_paths_detects_added_removed_and_changed_files(self) -> None:
        before = {"same.txt": b"same", "changed.txt": b"old", "removed.txt": b"gone"}
        after = {"same.txt": b"same", "changed.txt": b"new", "added.txt": b"new"}

        self.assertEqual(
            replay.changed_paths(before, after),
            ["added.txt", "changed.txt", "removed.txt"],
        )

    def test_main_rejects_stale_committed_generated_artifacts(self) -> None:
        committed = {"05_wiki/index.md": b"old"}
        rebuilt = {"05_wiki/index.md": b"new"}

        with mock.patch.object(replay, "snapshot", side_effect=[committed, rebuilt]), mock.patch.object(
            replay, "make"
        ) as make:
            with self.assertRaisesRegex(SystemExit, "committed_tree_replay"):
                replay.main()

        make.assert_called_once_with("demo")


if __name__ == "__main__":
    unittest.main()
