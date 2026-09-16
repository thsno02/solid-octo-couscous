"""Offline tests for the fail-closed publication gate."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import yaml

from validate_publication_rights import validate_publication_rights
from materialize_all_sources import redistribution_footer


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

    def test_retained_source_pdf_is_gated_even_when_text_tier_is_incomplete(self):
        for tier in ("metadata_capsule", "excerpt_capsule"):
            with self.subTest(tier=tier):
                temporary, root, audit = self.fixture(decision="block")
                with temporary:
                    manifest_path = root / "materialized_sources/corpus/item/manifest.yaml"
                    manifest = yaml.safe_load(manifest_path.read_text())
                    manifest["content_tier"] = tier
                    manifest["materialization"] = {"source_pdf": "source/document.pdf"}
                    manifest_path.write_text(yaml.safe_dump(manifest))

                    errors, blocked, active, audited = validate_publication_rights(
                        audit, root / "materialized_sources/corpus"
                    )

                self.assertEqual(errors, [])
                self.assertEqual((len(blocked), active, audited), (1, 1, 1))

    def test_undeclared_supplement_pdf_is_not_hidden_by_metadata_tier(self):
        temporary, root, audit = self.fixture()
        with temporary:
            capsule = root / "materialized_sources/corpus/item"
            (capsule / "pdf-supplement").mkdir()
            (capsule / "pdf-supplement/document.pdf").write_bytes(b"%PDF-1.4\n")
            manifest_path = capsule / "manifest.yaml"
            manifest = yaml.safe_load(manifest_path.read_text())
            manifest["content_tier"] = "metadata_capsule"
            manifest_path.write_text(yaml.safe_dump(manifest))
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
        self.assertTrue(any("PDF_SUPPLEMENT_UNDECLARED" in error for error in errors))

    def test_packaged_allowance_requires_notice_and_attribution(self):
        temporary, root, audit = self.fixture()
        with temporary:
            capsule = root / "materialized_sources/corpus/item"
            package = {
                "source_revision": "rev-1", "source_version_url": "https://example.test/v1",
                "notice_path": "license.md", "attribution": "Copyright example.",
                "modifications": "Text conversion.", "scope": "Document text.",
            }
            expected = "Complete test license.\n"
            (root / "license.md").write_text(expected)
            notice = capsule / "NOTICE.md"
            notice.write_text(expected)
            document = capsule / "document.md"
            document.write_text("Original source text.\n" + redistribution_footer(package))
            manifest_path = capsule / "manifest.yaml"
            manifest = yaml.safe_load(manifest_path.read_text())
            metadata = {"rights": {"redistribution_package": package}}
            (root / "metadata.yaml").write_text(yaml.safe_dump(metadata))
            (capsule / "source-metadata.yaml").write_text(yaml.safe_dump(metadata))
            manifest.update({"metadata_path": "metadata.yaml", "rights": {"redistribution_package": package}, "materialization": {"document": "document.md"}})
            manifest_path.write_text(yaml.safe_dump(manifest))
            reviewed = yaml.safe_load(audit.read_text())
            reviewed["items"][0]["redistribution_package"] = package
            audit.write_text(yaml.safe_dump(reviewed))
            errors, blocked, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertEqual((errors, blocked), ([], []))
            del reviewed["items"][0]["redistribution_package"]
            audit.write_text(yaml.safe_dump(reviewed))
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))
            reviewed["items"][0]["redistribution_package"] = package
            audit.write_text(yaml.safe_dump(reviewed))
            notice.unlink()
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))
            notice.write_text("Shortened or substituted license.")
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))
            notice.write_text(expected)
            document.write_text(redistribution_footer(package) + redistribution_footer(package))
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))
            document.write_text("Original source text, but attribution was lost.\n")
            errors, _, _, _ = validate_publication_rights(audit, root / "materialized_sources/corpus")
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))

    def test_packaged_nested_document_requires_relative_notice_link(self):
        temporary, root, audit = self.fixture()
        with temporary:
            capsule = root / "materialized_sources/corpus/item"
            package = {
                "source_revision": "rev-1",
                "source_version_url": "https://example.test/v1",
                "notice_path": "license.md",
                "attribution": "Copyright example.",
                "modifications": "Converted TeX to plain text.",
                "scope": "Document text.",
            }
            expected_notice = "Complete test license.\n"
            (root / "license.md").write_text(expected_notice, encoding="utf-8")
            (capsule / "NOTICE.md").write_text(expected_notice, encoding="utf-8")
            document = capsule / "normalized/document.txt"
            document.parent.mkdir(parents=True)
            document.write_text(
                "Original source text.\n" + redistribution_footer(package, "../NOTICE.md"),
                encoding="utf-8",
            )

            metadata = {"rights": {"redistribution_package": package}}
            (root / "metadata.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
            (capsule / "source-metadata.yaml").write_text(
                yaml.safe_dump(metadata), encoding="utf-8"
            )
            manifest_path = capsule / "manifest.yaml"
            manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
            manifest.update(
                {
                    "metadata_path": "metadata.yaml",
                    "rights": {"redistribution_package": package},
                    "materialization": {"document": "normalized/document.txt"},
                }
            )
            manifest_path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
            reviewed = yaml.safe_load(audit.read_text(encoding="utf-8"))
            reviewed["items"][0]["redistribution_package"] = package
            audit.write_text(yaml.safe_dump(reviewed), encoding="utf-8")

            errors, blocked, _, _ = validate_publication_rights(
                audit, root / "materialized_sources/corpus"
            )
            self.assertEqual((errors, blocked), ([], []))

            document.write_text(
                "Original source text.\n" + redistribution_footer(package),
                encoding="utf-8",
            )
            errors, _, _, _ = validate_publication_rights(
                audit, root / "materialized_sources/corpus"
            )
            self.assertTrue(any("PACKAGE_INVALID" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
