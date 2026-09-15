"""Offline tests for the fail-closed publication gate."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from validate_publication_rights import validate_publication_rights


class PublicationRightsTests(unittest.TestCase):
    def fixture(self, *, decision: str = "allow", reviewed_revision: str = "rev-1"):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        corpus = root / "materialized_sources/corpus/item"
        corpus.mkdir(parents=True)
        manifest = root / "materialized_sources/corpus/item/manifest.yaml"
        manifest.write_text(
            yaml.safe_dump({"uid": "source:one", "content_tier": "full_text", "revision": "rev-1"}),
            encoding="utf-8",
        )
        audit = root / "rights.yaml"
        audit.write_text(
            yaml.safe_dump(
                {
                    "scope": {"baseline_full_text_count": 1},
                    "items": [
                        {
                            "uid": "source:one",
                            "manifest_path": "materialized_sources/corpus/item/manifest.yaml",
                            "source_revision": reviewed_revision,
                            "publication_gate": {"decision": decision, "reason": "test decision"},
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        return temporary, root, audit

    def test_missing_audit_blocks(self):
        with tempfile.TemporaryDirectory() as directory:
            errors, _, _, _ = validate_publication_rights(
                Path(directory) / "missing.yaml", Path(directory) / "corpus"
            )
        self.assertTrue(any("AUDIT_MISSING" in error for error in errors))

    def test_explicit_block_blocks(self):
        temporary, root, audit = self.fixture(decision="block")
        with temporary:
            errors, blocked, _, _ = validate_publication_rights(
                audit, root / "materialized_sources/corpus"
            )
        self.assertEqual(errors, [])
        self.assertEqual(len(blocked), 1)

    def test_exact_revision_allows(self):
        temporary, root, audit = self.fixture()
        with temporary:
            errors, blocked, active, audited = validate_publication_rights(
                audit, root / "materialized_sources/corpus"
            )
        self.assertEqual((errors, blocked, active, audited), ([], [], 1, 1))

    def test_stale_revision_blocks(self):
        temporary, root, audit = self.fixture(reviewed_revision="rev-0")
        with temporary:
            errors, _, _, _ = validate_publication_rights(
                audit, root / "materialized_sources/corpus"
            )
        self.assertTrue(any("REVISION_MISMATCH" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
