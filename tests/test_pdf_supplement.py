"""Offline regressions for an optional PDF beside a retained TeX capsule."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "experiments/v0_meta_kb_initialization_demo_260910/pipeline"))

import build_demo
import materialize_all_sources as materializer
from audit_non_repo_coverage import target_version_matches
from rights_propagation import DECLARED, make_rights_ref, rights_snapshot, validate_rights_chain
from test_materialization_integrity import minimal_pdf_pages
from validate_materialization_completeness import validate_pdf_supplement
from validate_publication_rights import validate_pdf_supplement_rights, validate_publication_rights


class PdfSupplementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.capsule = self.root / "materialized_sources/corpus/arxiv-example"
        self.capsule.mkdir(parents=True)
        (self.capsule / "normalized").mkdir()
        (self.capsule / "pdf-supplement").mkdir()
        self.manifest_path = self.capsule / "manifest.yaml"
        self.metadata_path = self.root / "raw_data/arxiv/example/metadata.yaml"
        self.metadata_path.parent.mkdir(parents=True)
        self.audit_path = self.root / "raw_data/audits/materialization_rights_review.yaml"
        self.audit_path.parent.mkdir(parents=True)
        self.item = {"uid": "arxiv:2408.08435", "manifest": self.rel(self.manifest_path)}
        (self.capsule / "normalized/document.txt").write_text("Original retained TeX document remains usable.\n")
        (self.capsule / "selectors.jsonl").write_text(json.dumps({
            "selector": "tex://old#L1-L1", "local_path": self.rel(self.capsule / "normalized/document.txt"),
            "start_line": 1, "end_line": 1, "text_preview": "Original retained TeX",
        }) + "\n")
        self.pdf = minimal_pdf_pages([
            "This first PDF page explains a bounded source method with stable evidence references.",
            "This second PDF page contains an independent conclusion and references for the same source.",
        ])
        self.pdf_hash = hashlib.sha256(self.pdf).hexdigest()
        (self.capsule / "pdf-supplement/document.pdf").write_bytes(self.pdf)
        notice = self.root / "raw_data/licenses/cc-by-4.0.md"
        notice.parent.mkdir(parents=True)
        notice.write_text("Complete reviewed license notice.\n")
        (self.capsule / "pdf-supplement/NOTICE.md").write_text(notice.read_text())
        self.rights = {
            "license_spdx": "CC-BY-4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
            "license_verified_at": "2026-09-16",
            "redistribution_package": {
                "source_revision": f"sha256:{self.pdf_hash}",
                "source_version_url": "https://arxiv.org/pdf/2408.08435v2",
                "notice_path": self.rel(notice), "attribution": "Example authors, fixed v2 PDF.",
                "modifications": "Converted PDF text without OCR; original PDF unchanged.",
                "scope": "Only the official fixed v2 PDF and its paged text/selectors.",
            },
            "publication_gate": {
                "decision": "allow", "reason": "Independently checked the official PDF terms.",
                "approved_scope": "Only the official fixed v2 PDF and its paged text/selectors.",
            },
        }
        self.metadata = {
            "uid": self.item["uid"], "versioning": {"source_version": "v2"},
            "rights": {"pdf_supplement": copy.deepcopy(self.rights)},
        }
        self.write_metadata()
        self.manifest = {
            "uid": self.item["uid"], "canonical_id": "2408.08435", "source_type": "arxiv",
            "adapter": "arxiv_latex_v2", "archive_container": "tar", "revision": "old-tex-revision",
            "metadata_path": self.rel(self.metadata_path), "content_tier": "full_text", "status": "materialized",
            "rights": {"old_package_marker": "unchanged"}, "selectors": ["selectors.jsonl"],
            "materialization": {"document": "normalized/document.txt", "normalized_document": "normalized/document.txt", "selector_count": 1},
        }
        self.write(self.manifest_path, self.manifest)
        self.legacy = {name: (self.capsule / name).read_bytes() for name in ("normalized/document.txt", "selectors.jsonl")}
        self.retrieval = {
            "requested_urls": ["https://arxiv.org/pdf/2408.08435v2"],
            "resolved_url": "https://arxiv.org/pdf/2408.08435v2", "content_type": "application/pdf",
            "bytes": len(self.pdf), "sha256": self.pdf_hash, "retrieved_at": "2026-09-16T04:00:00Z",
        }
        with mock.patch.object(materializer, "ROOT", self.root):
            self.supplement = materializer.build_pdf_supplement(
                self.capsule, "v2", self.retrieval, self.rights, body_quality_verified=True,
                limitations=["The PDF is the original; graphic-only regions are not OCR text."],
            )
        self.manifest["pdf_supplement"] = self.supplement
        self.review = {
            "uid": self.item["uid"], "manifest_path": self.item["manifest"],
            "source_revision": "old-tex-revision", "publication_gate": {"decision": "allow"},
            "pdf_supplement": copy.deepcopy(self.rights),
        }
        self.write_audit()
        self.refresh_inventory()

    def rel(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def write(self, path: Path, value: object) -> None:
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def write_metadata(self) -> None:
        self.write(self.metadata_path, self.metadata)
        self.write(self.capsule / "source-metadata.yaml", self.metadata)

    def write_audit(self) -> None:
        self.write(self.audit_path, {"scope": {"baseline_full_text_count": 1}, "items": [self.review]})

    def refresh_inventory(self) -> None:
        with mock.patch.object(materializer, "ROOT", self.root):
            self.manifest["local_files"] = materializer.local_file_inventory(self.capsule)
        self.manifest["local_bytes"] = sum(row["bytes"] for row in self.manifest["local_files"])
        self.write(self.manifest_path, self.manifest)

    def integrity_errors(self) -> list[str]:
        inventory = self.manifest["local_files"]
        hashes = {row["path"]: hashlib.sha256((self.root / row["path"]).read_bytes()).hexdigest() for row in inventory}
        errors = []
        validate_pdf_supplement(self.manifest, self.capsule, set(hashes), hashes, errors, repository_root=self.root)
        return errors

    def selector_rows(self) -> list[dict]:
        return [json.loads(line) for line in (self.capsule / "pdf-supplement/selectors.jsonl").read_text().splitlines()]

    def set_selector_rows(self, rows: list[dict]) -> None:
        with mock.patch.object(materializer, "ROOT", self.root):
            materializer.write_jsonl(self.capsule / "pdf-supplement/selectors.jsonl", rows)
        self.refresh_inventory()

    def chosen(self) -> tuple[Path | None, Path]:
        with mock.patch.object(build_demo, "ROOT", self.root):
            return build_demo.choose_local_document(self.item, self.manifest), build_demo.choose_local_selectors(self.item, self.manifest)

    def journal_fixture(self, *, required_si: bool = True) -> dict | None:
        """Convert only this isolated fixture to an explicitly declared publisher work."""
        self.item["uid"] = "journal:10.1038/example.2024.1"
        self.version = "publisher-vor:2024-01-11"
        self.main_url = "https://www.nature.com/articles/example.2024.1.pdf"
        self.si_url = "https://media.springernature.com/original/example-SI.pdf"
        self.rights["redistribution_package"].update({
            "source_version": self.version, "source_version_url": self.main_url,
            "scope": "Only the official main publisher PDF and its page text/selectors.",
        })
        self.rights["publication_gate"]["approved_scope"] = self.rights["redistribution_package"]["scope"]
        self.retrieval.update({
            "requested_urls": [self.main_url],
            "resolved_url": self.main_url + "?error=cookies_not_supported&code=12345678-1234-1234-1234-123456789abc",
        })
        self.metadata = {
            "uid": self.item["uid"], "source_type": "journal", "canonical_id": "doi:10.1038/example.2024.1",
            "canonical_url": "https://doi.org/10.1038/example.2024.1",
            "versioning": {"source_version": None, "publisher_pdf": {
                "doi": "10.1038/example.2024.1", "source_version": self.version, "source_pdf_url": self.main_url,
                "supplementary_information": {"required": required_si, "source_pdf_url": self.si_url if required_si else None},
            }},
            "rights": {"pdf_supplement": copy.deepcopy(self.rights)},
        }
        self.manifest.update({
            "uid": self.item["uid"], "source_type": "journal", "canonical_id": self.metadata["canonical_id"],
            "canonical_url": self.metadata["canonical_url"], "adapter": "generic_web_or_document_v2",
            "content_tier": "excerpt_capsule", "status": "partial", "revision": "old-journal-revision",
            "retrievals": [{"requested_url": "https://example.org/historical-article", "sha256": "old-excerpt-hash"}],
            "generated_at": "old-fixed-time",
            "materialization": {"document": "document.md", "selector_count": 1, "stored_characters": 40},
        })
        self.manifest.pop("pdf_supplement")
        self.manifest.pop("archive_container")
        (self.capsule / "document.md").write_bytes(b"Bounded historical journal excerpt.\r\n")
        (self.capsule / "selectors.jsonl").write_bytes(
            (json.dumps({"selector": "local://old#L1-L1", "kind": "file", "start_line": 1, "end_line": 1,
                         "local_path": self.rel(self.capsule / "document.md"),
                         "text_preview": "Bounded historical journal excerpt."}) + "\n").encode()
        )
        self.review = {
            "uid": self.item["uid"], "manifest_path": self.item["manifest"], "source_revision": "old-journal-revision",
            "publication_gate": {"decision": "unknown", "reason": "Old excerpt has no full-document allowance."},
            "pdf_supplement": copy.deepcopy(self.rights),
        }
        si_input = None
        if required_si:
            base = self.capsule / "pdf-supplement/supplementary-information"
            base.mkdir()
            payload = minimal_pdf_pages([
                "Supplementary methods explain the algorithm details belonging to the same parent paper.",
                "Supplementary information provides further notes and a stable final appendix conclusion.",
            ])
            (base / "document.pdf").write_bytes(payload)
            (base / "NOTICE.md").write_bytes((self.capsule / "pdf-supplement/NOTICE.md").read_bytes())
            grant = copy.deepcopy(self.rights)
            grant["redistribution_package"].update({
                "source_revision": "sha256:" + hashlib.sha256(payload).hexdigest(),
                "source_version_url": self.si_url, "scope": "Only the official SI PDF and its page text/selectors.",
            })
            grant["publication_gate"]["approved_scope"] = grant["redistribution_package"]["scope"]
            self.metadata["rights"]["supplementary_information"] = copy.deepcopy(grant)
            self.review["supplementary_information"] = copy.deepcopy(grant)
            si_input = {
                "retrieval": {"requested_urls": [self.si_url], "resolved_url": self.si_url,
                              "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest(),
                              "content_type": "application/pdf", "retrieved_at": self.retrieval["retrieved_at"]},
                "rights": grant, "body_quality_verified": True, "limitations": ["Graphic-only content is not OCR text."],
            }
        self.write_metadata()
        self.write_audit()
        self.refresh_inventory()
        self.legacy = {
            name: (self.capsule / name).read_bytes()
            for name in ("document.md", "normalized/document.txt", "selectors.jsonl", "source-metadata.yaml")
        }
        return si_input

    def build_journal(self, si_input: dict | None) -> None:
        with mock.patch.object(materializer, "ROOT", self.root):
            self.supplement = materializer.build_pdf_supplement(
                self.capsule, self.version, self.retrieval, self.rights,
                body_quality_verified=True, limitations=["Native PDF text may not cover graphic-only labels."],
                supplementary_information=si_input,
            )
        self.manifest["pdf_supplement"] = self.supplement
        self.refresh_inventory()

    def arxiv_publisher_fixture(self) -> None:
        """Keep the arXiv identity while declaring an unrelated synthetic publisher."""
        self.version = "publisher-vor:doi:10.5555/published-work.2024.7"
        self.main_url = "https://publisher.example/articles/published-work.2024.7.pdf"
        correspondence = {
            "originating_arxiv_id": "2408.08435", "publisher_doi": "10.5555/published-work.2024.7",
            "reviewed": True, "audit_evidence_kind": "reviewed_published_work",
        }
        self.rights["redistribution_package"].update({
            "source_version": self.version, "source_version_url": self.main_url,
            "publisher_correspondence": copy.deepcopy(correspondence),
            "notice_path": self.rel(self.capsule / "pdf-supplement/NOTICE.md"),
            "attribution": "Synthetic authors, the official published work, DOI 10.5555/published-work.2024.7.",
            "scope": "Only the published PDF and its page text/selectors; no retained TeX extensions.",
        })
        self.rights["publication_gate"]["approved_scope"] = self.rights["redistribution_package"]["scope"]
        (self.capsule / "pdf-supplement/NOTICE.md").write_text(
            "Synthetic authors, fixed published work. Original PDF unchanged; page text is derived.\n"
            "Only the published representation; retained TeX is not granted.\nComplete reviewed license notice.\n"
        )
        for name in ("document.txt", "selectors.jsonl"):
            (self.capsule / "pdf-supplement" / name).unlink()
        (self.capsule / "source").mkdir()
        (self.capsule / "source/main.tex").write_text("Retained historical TeX extension outside the published PDF.\n")
        (self.capsule / "README.md").write_text("Retained historical capsule description.\n")
        (self.capsule / "files.jsonl").write_text("Retained historical source inventory.\n")
        (self.capsule / "NOTICE.md").write_text("Retained historical notice; public permission is unresolved.\n")
        self.metadata.update({
            "source_type": "arxiv", "canonical_id": "2408.08435", "canonical_url": "https://arxiv.org/abs/2408.08435",
            "versioning": {"source_version": None, "publisher_pdf": {
                "doi": correspondence["publisher_doi"], "source_version": self.version, "source_pdf_url": self.main_url,
                "correspondence": correspondence,
                "supplementary_information": {"required": False, "source_pdf_url": None},
            }},
        })
        self.manifest.update({
            "canonical_url": self.metadata["canonical_url"], "generated_at": "old-fixed-time",
            "retrievals": [{"resolved_url": "https://export.arxiv.org/src/2408.08435", "sha256": "old-tex-revision"}],
        })
        self.manifest.pop("pdf_supplement")
        self.retrieval.update({"requested_urls": [self.main_url], "resolved_url": self.main_url})
        self.review.update({
            "publication_gate": {"decision": "block", "reason": "The retained TeX extensions remain unreviewed."},
            "evidence": [{
                "kind": correspondence["audit_evidence_kind"], "checked_at": "2026-09-16",
                "doi": "https://doi.org/10.5555/published-work.2024.7", "url": "https://publisher.example/articles/published-work.2024.7/",
                "related_urls": [self.main_url], "supports_public_redistribution": False,
            }],
        })
        self.sync_publisher_grants()
        self.legacy = {
            path.relative_to(self.capsule).as_posix(): path.read_bytes()
            for path in self.capsule.rglob("*") if path.is_file() and path != self.manifest_path
        }
        fetch = mock.patch.object(materializer, "fetch_bytes", side_effect=AssertionError("publisher fixture must remain offline"))
        self.offline_fetch = fetch.start()
        self.addCleanup(fetch.stop)

    def sync_publisher_grants(self) -> None:
        self.metadata["rights"]["pdf_supplement"] = copy.deepcopy(self.rights)
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        if isinstance(self.manifest.get("pdf_supplement"), dict):
            self.manifest["pdf_supplement"]["rights"] = self.rights
        self.write_metadata()
        self.write_audit()
        self.refresh_inventory()

    def build_arxiv_publisher(self) -> None:
        with mock.patch.object(materializer, "ROOT", self.root):
            self.supplement = materializer.build_pdf_supplement(
                self.capsule, self.version, self.retrieval, self.rights, body_quality_verified=True,
                limitations=["Native PDF text may omit graphic-only labels; the legacy TeX is separate."],
            )
        self.manifest["pdf_supplement"] = self.supplement
        self.refresh_inventory()
        self.offline_fetch.assert_not_called()

    def assert_publisher_preflight_refused(self, *, supplementary_information: dict | None = None) -> None:
        before = self.snapshot()
        with mock.patch.object(materializer, "ROOT", self.root), self.assertRaises(materializer.RedistributionPackageError):
            materializer.build_pdf_supplement(
                self.capsule, self.version, self.retrieval, self.rights, body_quality_verified=True,
                supplementary_information=supplementary_information,
            )
        self.assertEqual(self.snapshot(), before)
        self.offline_fetch.assert_not_called()

    def test_arxiv_publisher_keeps_source_identity_legacy_bytes_and_root_block(self) -> None:
        self.arxiv_publisher_fixture()
        root_fields = {field: copy.deepcopy(value) for field, value in self.manifest.items() if field not in ("local_files", "local_bytes")}
        self.build_arxiv_publisher()
        self.assertEqual(self.integrity_errors(), [])
        self.assertEqual(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review), ([], []))
        self.assertEqual(self.chosen(), (self.capsule / "pdf-supplement/document.txt", self.capsule / "pdf-supplement/selectors.jsonl"))
        for name, old in self.legacy.items():
            self.assertEqual((self.capsule / name).read_bytes(), old)
        for field, value in root_fields.items():
            self.assertEqual(self.manifest[field], value)
        self.assertNotIn("source_version", self.manifest)
        self.assertIsNone(self.metadata["versioning"]["source_version"])
        self.assertNotIn("supplementary_information", self.supplement)
        self.assertEqual(self.review["publication_gate"]["decision"], "block")
        self.assertFalse(self.review["evidence"][0]["supports_public_redistribution"])
        errors, blocked, _, _ = validate_publication_rights(self.audit_path, self.root / "materialized_sources/corpus")
        self.assertEqual(errors, [])
        self.assertEqual(len(blocked), 1)
        source = {**self.item, "revision": self.supplement["revision"], "source_representation": "pdf_supplement",
                  "rights_status": DECLARED, "rights": rights_snapshot(self.rights)}
        self.assertEqual(validate_rights_chain(root=self.root, claims=[], evidence=[], sources=[source]), [])
        self.offline_fetch.assert_not_called()

    def test_arxiv_publisher_normalizes_only_doi_prefix_and_case_for_correspondence(self) -> None:
        self.arxiv_publisher_fixture()
        declaration = self.metadata["versioning"]["publisher_pdf"]
        declaration["doi"] = "DOI:10.5555/PUBLISHED-WORK.2024.7"
        declaration["correspondence"]["publisher_doi"] = "https://doi.org/10.5555/published-work.2024.7"
        self.rights["redistribution_package"]["publisher_correspondence"] = copy.deepcopy(declaration["correspondence"])
        self.sync_publisher_grants()
        self.build_arxiv_publisher()
        self.assertEqual(self.integrity_errors(), [])

    def test_arxiv_publisher_invalid_correspondence_is_not_a_normal_arxiv_fallback(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        original = copy.deepcopy(self.metadata)
        for field, value in (
            ("originating_arxiv_id", "2408.99999"), ("publisher_doi", "10.5555/different-work"),
            ("reviewed", False), ("reviewed", 1), ("reviewed", "true"), ("audit_evidence_kind", ""),
        ):
            with self.subTest(field=field, value=value):
                self.metadata = copy.deepcopy(original)
                self.metadata["versioning"]["publisher_pdf"]["correspondence"][field] = value
                self.write_metadata()
                self.refresh_inventory()
                self.assertTrue(self.integrity_errors())
                self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")
                self.assert_publisher_preflight_refused()
        for value in (None, [], {"reviewed": True}):
            with self.subTest(correspondence=value):
                self.metadata = copy.deepcopy(original)
                self.metadata["versioning"]["publisher_pdf"]["correspondence"] = value
                self.write_metadata()
                self.refresh_inventory()
                self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_identity_declaration_version_and_metadata_mismatch_fail_closed(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        original = copy.deepcopy(self.metadata)
        for field, value in (("uid", "arxiv:2408.99999"), ("source_type", "journal"),
                             ("canonical_id", "2408.99999"), ("canonical_url", "https://arxiv.org/abs/2408.99999")):
            with self.subTest(identity=field):
                self.metadata = copy.deepcopy(original)
                self.metadata[field] = value
                self.write_metadata()
                self.refresh_inventory()
                self.assert_publisher_preflight_refused()
        for field, value in (("source_version", "publisher-vor:wrong-version"), ("doi", "10.5555/wrong-work"),
                             ("source_pdf_url", "https://publisher.example/wrong-work.pdf"), ("supplementary_information", None)):
            with self.subTest(declaration=field):
                self.metadata = copy.deepcopy(original)
                self.metadata["versioning"]["publisher_pdf"][field] = value
                self.write_metadata()
                self.refresh_inventory()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()
        self.metadata = copy.deepcopy(original)
        for versioning in (None, 0, False, 7, [], {"source_version": "v2"}, {**original["versioning"], "source_version": "v2"}):
            with self.subTest(capsule_versioning=versioning):
                self.write_metadata()
                capsule = copy.deepcopy(original)
                capsule["versioning"] = versioning
                self.write(self.capsule / "source-metadata.yaml", capsule)
                self.refresh_inventory()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()
        self.write_metadata()
        for value in (None, [], {}):
            with self.subTest(publisher_declaration=value):
                self.metadata = copy.deepcopy(original)
                self.metadata["versioning"]["publisher_pdf"] = value
                self.write_metadata()
                self.refresh_inventory()
                self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_four_synchronized_bad_grants_still_fail(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        original = copy.deepcopy(self.rights)
        for field, value in (
            ("publisher_correspondence", {"originating_arxiv_id": "2408.99999", "reviewed": True}),
            ("publisher_correspondence", {**original["redistribution_package"]["publisher_correspondence"], "reviewed": 1}),
            ("source_version", None), ("source_version", "publisher-vor:wrong-version"),
            ("source_version_url", "https://publisher.example/different.pdf"),
        ):
            with self.subTest(package=field, value=value):
                self.rights = copy.deepcopy(original)
                self.rights["redistribution_package"][field] = value
                self.sync_publisher_grants()
                self.assertEqual(self.rights, self.metadata["rights"]["pdf_supplement"])
                self.assertEqual(self.rights, self.review["pdf_supplement"])
                self.assertEqual(self.rights, self.manifest["pdf_supplement"]["rights"])
                self.assertTrue(self.integrity_errors())
                self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")
                self.assert_publisher_preflight_refused()
        self.rights = copy.deepcopy(original)
        self.rights["redistribution_package"].pop("source_version")
        self.sync_publisher_grants()
        self.assert_publisher_preflight_refused()
        for field, value in (("decision", "block"), ("approved_scope", "Only unrelated retained TeX.")):
            with self.subTest(gate=field):
                self.rights = copy.deepcopy(original)
                self.rights["publication_gate"][field] = value
                self.sync_publisher_grants()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()
        self.rights = copy.deepcopy(original)
        declaration = self.metadata["versioning"]["publisher_pdf"]
        declaration["doi"] = "10.5555/different-reviewed-work"
        declaration["correspondence"]["publisher_doi"] = declaration["doi"]
        self.rights["redistribution_package"]["publisher_correspondence"] = copy.deepcopy(declaration["correspondence"])
        self.sync_publisher_grants()
        self.assertTrue(any("DOI/URL evidence" in error for error in self.integrity_errors()))
        self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_requires_own_grant_and_checked_doi_url_evidence(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        original = copy.deepcopy(self.review)
        for field, value in (("kind", "different_review"), ("checked_at", ""), ("doi", "https://doi.org/10.5555/wrong-work"),
                             ("related_urls", [])):
            with self.subTest(evidence=field):
                self.review = copy.deepcopy(original)
                self.review["evidence"][0][field] = value
                self.write_audit()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()
        for field, value in (("evidence", []), ("evidence", None), ("uid", "arxiv:2408.99999")):
            with self.subTest(review=field):
                self.review = copy.deepcopy(original)
                self.review[field] = value
                self.write_audit()
                self.assert_publisher_preflight_refused()
        self.review = copy.deepcopy(original)
        self.review.pop("pdf_supplement")
        self.write_audit()
        self.assertTrue(self.integrity_errors())
        self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_reviewed_is_strict_in_each_metadata_and_each_grant(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        metadata, rights, review = (copy.deepcopy(value) for value in (self.metadata, self.rights, self.review))
        for path in (self.metadata_path, self.capsule / "source-metadata.yaml"):
            with self.subTest(declaration=path.name, parent=path.parent.name):
                self.metadata = copy.deepcopy(metadata)
                self.write_metadata()
                changed = copy.deepcopy(metadata)
                changed["versioning"]["publisher_pdf"]["correspondence"]["reviewed"] = 1
                self.assertEqual(changed["versioning"]["publisher_pdf"], metadata["versioning"]["publisher_pdf"])
                self.write(path, changed)
                self.refresh_inventory()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()
        for location in ("canonical", "capsule", "manifest", "audit"):
            with self.subTest(grant=location):
                self.metadata, self.rights, self.review = (copy.deepcopy(value) for value in (metadata, rights, review))
                self.sync_publisher_grants()
                if location in ("canonical", "capsule"):
                    changed = copy.deepcopy(self.metadata)
                    changed["rights"]["pdf_supplement"]["redistribution_package"]["publisher_correspondence"]["reviewed"] = 1
                    self.write(self.metadata_path if location == "canonical" else self.capsule / "source-metadata.yaml", changed)
                elif location == "manifest":
                    self.rights["redistribution_package"]["publisher_correspondence"]["reviewed"] = 1
                else:
                    self.review["pdf_supplement"]["redistribution_package"]["publisher_correspondence"]["reviewed"] = 1
                    self.write_audit()
                self.refresh_inventory()
                # Ordinary Python mapping equality says True == 1; each reviewed flag must still be rejected.
                for allowance in (
                    materializer.load_yaml(self.metadata_path)["rights"]["pdf_supplement"],
                    materializer.load_yaml(self.capsule / "source-metadata.yaml")["rights"]["pdf_supplement"],
                    self.review["pdf_supplement"], self.manifest["pdf_supplement"]["rights"],
                ):
                    self.assertEqual(allowance, rights)
                self.assertTrue(self.integrity_errors())
                self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")
                self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_rejects_unsafe_urls_even_when_all_inputs_agree(self) -> None:
        self.arxiv_publisher_fixture()
        original = tuple(copy.deepcopy(value) for value in (self.metadata, self.rights, self.review, self.retrieval))
        for url in (
            self.main_url.replace("https:", "http:"), self.main_url + "?download=1", self.main_url + "#page=1",
            self.main_url.replace("https://", "https://user@"), self.main_url.replace("https://", "https://@"),
            self.main_url.replace("https://", "https://:secret@"), self.main_url.replace("https://", "https://:@"),
        ):
            with self.subTest(url=url):
                self.metadata, self.rights, self.review, self.retrieval = (copy.deepcopy(value) for value in original)
                self.metadata["versioning"]["publisher_pdf"]["source_pdf_url"] = url
                self.rights["redistribution_package"]["source_version_url"] = url
                self.review["evidence"][0]["related_urls"] = [url]
                self.retrieval.update({"requested_urls": [url], "resolved_url": url})
                self.sync_publisher_grants()
                self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_rejects_requested_and_resolved_redirect_substitution(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        original = copy.deepcopy(self.retrieval)
        for field, value in (
            ("requested_urls", ["https://publisher.example/other.pdf"]), ("requested_urls", [self.main_url, self.main_url]),
            ("resolved_url", "https://attacker.example/articles/published-work.2024.7.pdf"),
            ("resolved_url", self.main_url.replace("2024.7", "2024.8")),
            ("resolved_url", self.main_url + "?error=cookies_not_supported&code=12345678-1234-1234-1234-123456789abc"),
        ):
            with self.subTest(retrieval=field, value=value):
                self.retrieval = copy.deepcopy(original)
                self.retrieval[field] = value
                self.supplement["retrievals"] = [copy.deepcopy(self.retrieval)]
                self.refresh_inventory()
                self.assertTrue(self.integrity_errors())
                self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_inventory_drift_or_undeclared_si_cannot_write_derivatives(self) -> None:
        self.arxiv_publisher_fixture()
        self.build_arxiv_publisher()
        source = self.capsule / "source/main.tex"
        original = source.read_bytes()
        source.write_bytes(original + b"Changed after inventory approval.\n")
        # Legacy inventory protection belongs to builder preflight, not the child-only validator.
        self.assert_publisher_preflight_refused()
        source.write_bytes(original)
        self.assert_publisher_preflight_refused(supplementary_information={})
        (self.capsule / "pdf-supplement/supplementary-information").mkdir()
        self.assertTrue(self.integrity_errors())
        self.assert_publisher_preflight_refused()

    def test_arxiv_publisher_missing_manifest_supplement_without_pdf_is_not_legacy_success(self) -> None:
        self.arxiv_publisher_fixture()
        self.manifest.pop("pdf_supplement", None)
        (self.capsule / "pdf-supplement/document.pdf").unlink()
        original = copy.deepcopy(self.metadata)
        for declared_in in ("canonical", "capsule", "both"):
            with self.subTest(declared_in=declared_in):
                canonical, capsule = copy.deepcopy(original), copy.deepcopy(original)
                if declared_in == "canonical":
                    capsule["versioning"].pop("publisher_pdf")
                elif declared_in == "capsule":
                    canonical["versioning"].pop("publisher_pdf")
                self.write(self.metadata_path, canonical)
                self.write(self.capsule / "source-metadata.yaml", capsule)
                self.refresh_inventory()
                errors = self.integrity_errors()
                rights_errors, _ = validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)
                self.assertTrue(any("DECLARATION_MISSING" in error for error in errors), errors)
                self.assertTrue(any("DECLARATION_MISSING" in error for error in rights_errors), rights_errors)
                self.assertFalse(any("UNDECLARED" in error for error in errors + rights_errors))
                self.assert_publisher_preflight_refused()

    def test_arxiv_without_publisher_or_pdf_supplement_keeps_ordinary_metadata_valid(self) -> None:
        self.manifest.pop("pdf_supplement")
        (self.capsule / "pdf-supplement/document.pdf").unlink()
        for versioning in ({"source_version": "v2"}, {"source_version": None}, None, {}):
            with self.subTest(versioning=versioning):
                self.metadata["versioning"] = versioning
                self.write_metadata()
                self.refresh_inventory()
                self.assertEqual(self.integrity_errors(), [])
                self.assertEqual(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review), ([], []))

    def journal_record(self) -> mock.Mock:
        return mock.Mock(
            uid=self.item["uid"], source_type="journal", canonical_id=self.metadata["canonical_id"],
            canonical_url=self.metadata["canonical_url"], relative_metadata_path=self.rel(self.metadata_path),
            capsule_root=self.capsule, metadata=self.metadata,
        )

    def snapshot(self) -> dict[str, bytes]:
        return {self.rel(path): path.read_bytes() for path in self.capsule.rglob("*") if path.is_file()}

    def test_journal_main_and_si_are_independent_and_parent_excerpt_is_default(self) -> None:
        self.build_journal(self.journal_fixture())
        self.assertEqual(self.integrity_errors(), [])
        child = self.supplement["supplementary_information"]
        self.assertNotEqual(child["revision"], self.supplement["revision"])
        self.assertEqual(child["materialization"]["pdf_page_count"], 2)
        self.assertEqual(child["selectors"], ["pdf-supplement/supplementary-information/selectors.jsonl"])
        self.assertEqual(self.chosen(), (self.capsule / "pdf-supplement/document.txt", self.capsule / "pdf-supplement/selectors.jsonl"))
        excerpt, _, _ = build_demo.source_excerpt((self.capsule / "pdf-supplement/document.txt").read_text(), "Parent", self.supplement)
        self.assertIn("first PDF page", excerpt)
        self.assertNotIn("Supplementary", excerpt)
        for name, old in self.legacy.items():
            self.assertEqual((self.capsule / name).read_bytes(), old)
        self.assertEqual(self.metadata["versioning"]["source_version"], None)
        self.assertEqual(self.manifest["revision"], "old-journal-revision")
        errors, blocked, active, _ = validate_publication_rights(self.audit_path, self.root / "materialized_sources/corpus")
        self.assertEqual((errors, blocked, active), ([], [], 1))

    def test_journal_explicit_no_si_and_amended_version_are_supported(self) -> None:
        si = self.journal_fixture(required_si=False)
        self.version = "publisher-vor:2016-03-15;amended:addendum-2019-03-19"
        self.metadata["versioning"]["publisher_pdf"]["source_version"] = self.version
        self.rights["redistribution_package"]["source_version"] = self.version
        self.metadata["rights"]["pdf_supplement"] = copy.deepcopy(self.rights)
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        self.write_metadata()
        self.write_audit()
        self.refresh_inventory()
        self.build_journal(si)
        self.assertEqual(self.integrity_errors(), [])
        self.assertNotIn("supplementary_information", self.supplement)

    def test_native_carriage_returns_are_preserved_and_real_text_drift_is_rejected(self) -> None:
        original_extract = materializer.extract_pdf_text

        def extract_with_native_cr(*args, **kwargs):
            text, rows, count = original_extract(*args, **kwargs)
            for row in rows:
                preview = row["text_preview"]
                with_cr = preview.replace(" ", "\r", 1)
                text = text.replace(preview, with_cr, 1)
                row["text_preview"] = with_cr
            return text, rows, count

        with mock.patch.object(materializer, "extract_pdf_text", side_effect=extract_with_native_cr):
            self.build_journal(self.journal_fixture())
            self.assertEqual(self.integrity_errors(), [])
            self.assertEqual(self.chosen()[0], self.capsule / "pdf-supplement/document.txt")
            for directory in ("pdf-supplement", "pdf-supplement/supplementary-information"):
                with self.subTest(directory=directory):
                    document = self.capsule / directory / "document.txt"
                    original = document.read_bytes()
                    native = original.decode("utf-8")
                    self.assertIn("\r", native)
                    self.assertNotEqual(document.read_text(encoding="utf-8"), native)
                    rows = [json.loads(line) for line in (self.capsule / directory / "selectors.jsonl").read_text().splitlines()]
                    self.assertTrue(all("\r" in row["text_preview"] and row["text_preview"] in native for row in rows))
                    document.write_bytes(original.replace(b"\r", b"\n"))
                    self.refresh_inventory()
                    errors = self.integrity_errors()
                    self.assertTrue(any("NATIVE_TEXT_DRIFT" in error for error in errors), errors)
                    self.assertFalse(any("FILE_INVENTORY_DRIFT" in error for error in errors), errors)
                    self.assertEqual(self.chosen()[0], self.capsule / "document.md")
                    document.write_bytes(original)
                    self.refresh_inventory()
            self.assertEqual(self.integrity_errors(), [])
            for name, old in self.legacy.items():
                self.assertEqual((self.capsule / name).read_bytes(), old)

    def test_journal_cookie_redirect_requires_exact_official_identity_and_query(self) -> None:
        self.build_journal(self.journal_fixture())
        original = self.supplement["retrievals"][0]["resolved_url"]
        for url in (
            self.main_url + "?error=other&code=12345678-1234-1234-1234-123456789abc",
            original + "&download=other",
            original.replace("www.nature.com", "attacker.example"),
            original.replace("example.2024.1.pdf", "different.pdf"),
            self.main_url + "?error=cookies_not_supported&code=not-a-uuid",
            original + "&code=12345678-1234-1234-1234-123456789abc",
        ):
            with self.subTest(url=url):
                self.supplement["retrievals"][0]["resolved_url"] = url
                self.assertTrue(self.integrity_errors())
                self.assertEqual(self.chosen()[0], self.capsule / "document.md")
        self.supplement["retrievals"][0]["resolved_url"] = original
        self.assertEqual(self.integrity_errors(), [])

    def test_journal_missing_si_declaration_or_bytes_fails_before_any_derivative_write(self) -> None:
        si_input = self.journal_fixture()
        before = self.snapshot()
        with mock.patch.object(materializer, "ROOT", self.root), self.assertRaises(materializer.RedistributionPackageError):
            materializer.build_pdf_supplement(self.capsule, self.version, self.retrieval, self.rights)
        self.assertEqual(self.snapshot(), before)
        self.build_journal(si_input)
        self.supplement.pop("supplementary_information")
        self.assertTrue(any("SI" in error for error in self.integrity_errors()))
        self.assertEqual(self.chosen()[0], self.capsule / "document.md")

    def test_journal_wrong_doi_version_or_approved_url_is_not_admitted(self) -> None:
        self.build_journal(self.journal_fixture())
        declaration = self.metadata["versioning"]["publisher_pdf"]
        for field, value in (
            ("doi", "10.1038/wrong-work"), ("source_version", "publisher-vor:1900-01-01"),
            ("source_pdf_url", "https://www.nature.com/articles/wrong-work.pdf"),
        ):
            with self.subTest(field=field):
                original = declaration[field]
                declaration[field] = value
                self.write_metadata()
                self.assertTrue(self.integrity_errors())
                declaration[field] = original
        self.write_metadata()
        self.refresh_inventory()
        self.assertEqual(self.integrity_errors(), [])

    def test_journal_si_actual_bytes_are_checked_even_when_consumer_passes_manifest_hashes(self) -> None:
        self.build_journal(self.journal_fixture())
        hashes = {row["path"]: row["sha256"] for row in self.manifest["local_files"]}
        for name in ("document.pdf", "NOTICE.md", "document.txt", "selectors.jsonl"):
            with self.subTest(name=name):
                path = self.capsule / "pdf-supplement/supplementary-information" / name
                original = path.read_bytes()
                path.write_bytes(original + b"\n")
                errors = []
                validate_pdf_supplement(self.manifest, self.capsule, set(hashes), hashes, errors, repository_root=self.root)
                self.assertTrue(any("FILE_INVENTORY_DRIFT" in error for error in errors))
                self.assertEqual(self.chosen()[0], self.capsule / "document.md")
                path.write_bytes(original)
        self.assertEqual(self.integrity_errors(), [])

    def test_journal_si_cannot_borrow_main_grant_or_drop_page(self) -> None:
        self.build_journal(self.journal_fixture())
        child = self.supplement["supplementary_information"]
        grant = self.review.pop("supplementary_information")
        self.write_audit()
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])
        self.assertEqual(self.chosen()[0], self.capsule / "document.md")
        self.review["supplementary_information"] = grant
        self.write_audit()
        path = self.capsule / "pdf-supplement/supplementary-information/selectors.jsonl"
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        with mock.patch.object(materializer, "ROOT", self.root):
            materializer.write_jsonl(path, rows[:1])
        child["materialization"].update({"selector_count": 1, "pdf_text_page_count": 1})
        self.refresh_inventory()
        self.assertTrue(any("SI_PAGE_COVERAGE" in error for error in self.integrity_errors()))
        before = self.snapshot()
        with mock.patch.object(materializer, "ROOT", self.root), self.assertRaises(materializer.RedistributionPackageError):
            materializer.materialize_one(self.journal_record(), {}, "ignored")
        self.assertEqual(self.snapshot(), before)

    def test_journal_two_offline_replays_preserve_all_capsule_bytes_and_legacy_time(self) -> None:
        self.build_journal(self.journal_fixture())
        before = self.snapshot()
        with mock.patch.multiple(materializer, ROOT=self.root, CORPUS_ROOT=self.root / "materialized_sources/corpus"), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("offline replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("must preserve legacy")), mock.patch.object(
            materializer, "finalize_capsule", side_effect=AssertionError("must not rewrite legacy packaging"),
        ):
            for _ in range(2):
                self.manifest = materializer.materialize_one(self.journal_record(), {}, "not-the-legacy-time")
                self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.manifest["generated_at"], "old-fixed-time")
        self.assertEqual(self.manifest["retrievals"], [{"requested_url": "https://example.org/historical-article", "sha256": "old-excerpt-hash"}])

    def test_journal_si_failure_propagates_through_wrapper_and_executor_without_prepare(self) -> None:
        self.build_journal(self.journal_fixture())
        (self.capsule / "pdf-supplement/supplementary-information/document.pdf").unlink()
        before = self.snapshot()
        self.write(self.root / "config.yaml", {"workers": 1, "generated_at": "ignored-new-time"})
        record = self.journal_record()
        with mock.patch.multiple(materializer, ROOT=self.root, CORPUS_ROOT=self.root / "materialized_sources/corpus"), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("preflight must be offline"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("cannot clean failed retained PDFs")), mock.patch.object(
            materializer, "finalize_capsule", side_effect=AssertionError("cannot downgrade retained PDFs"),
        ):
            with self.assertRaises(materializer.RedistributionPackageError):
                materializer.materialize_one(record, {}, "ignored")
            with mock.patch.object(sys, "argv", ["materializer", "--config", "config.yaml", "--workers", "1"]), mock.patch.object(
                materializer, "discover_records", return_value=[record],
            ), self.assertRaises(materializer.RedistributionPackageError):
                materializer.main()
        self.assertEqual(self.snapshot(), before)

    def test_journal_decoder_exception_and_invalid_manifest_cannot_downgrade_retained_capsule(self) -> None:
        self.build_journal(self.journal_fixture())
        self.write(self.root / "config.yaml", {"workers": 1})
        record = self.journal_record()
        with mock.patch.multiple(materializer, ROOT=self.root, CORPUS_ROOT=self.root / "materialized_sources/corpus"), mock.patch.object(
            materializer, "prepare_capsule", side_effect=AssertionError("cannot clean retained capsule"),
        ), mock.patch.object(materializer, "finalize_capsule", side_effect=AssertionError("cannot downgrade retained capsule")):
            before = self.snapshot()
            with mock.patch.object(materializer, "extract_pdf_text", side_effect=RuntimeError("synthetic decoder failure")):
                with self.assertRaises(materializer.RedistributionPackageError):
                    materializer.materialize_one(record, {}, "ignored")
                with mock.patch.object(sys, "argv", ["materializer", "--config", "config.yaml", "--workers", "1"]), mock.patch.object(
                    materializer, "discover_records", return_value=[record],
                ), self.assertRaises(materializer.RedistributionPackageError):
                    materializer.main()
            self.assertEqual(self.snapshot(), before)
            self.manifest_path.write_bytes(b"pdf_supplement: [malformed\n")
            before = self.snapshot()
            with self.assertRaises(materializer.RedistributionPackageError):
                materializer.materialize_one(record, {}, "ignored")
            self.assertEqual(self.snapshot(), before)

    def test_journal_invalid_versioning_is_fail_closed_through_wrapper_and_executor(self) -> None:
        self.build_journal(self.journal_fixture())
        self.metadata["versioning"] = 7
        self.write_metadata()
        self.refresh_inventory()
        self.write(self.root / "config.yaml", {"workers": 1, "generated_at": "ignored-new-time"})
        record = self.journal_record()
        before = self.snapshot()
        inventory = copy.deepcopy(self.manifest["local_files"])
        with mock.patch.multiple(materializer, ROOT=self.root, CORPUS_ROOT=self.root / "materialized_sources/corpus"), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("invalid retained declaration must not fetch"),
        ) as fetch, mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("must preserve retained PDF")) as prepare, mock.patch.object(
            materializer, "finalize_capsule", side_effect=AssertionError("must not downgrade retained PDF"),
        ) as finalize:
            with self.assertRaisesRegex(materializer.RedistributionPackageError, "versioning"):
                materializer.materialize_one(record, {}, "ignored")
            with mock.patch.object(sys, "argv", ["materializer", "--config", "config.yaml", "--workers", "1"]), mock.patch.object(
                materializer, "discover_records", return_value=[record],
            ), self.assertRaisesRegex(materializer.RedistributionPackageError, "versioning"):
                materializer.main()
            fetch.assert_not_called()
            prepare.assert_not_called()
            finalize.assert_not_called()
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.manifest["local_files"], inventory)

    def test_journal_si_grant_drift_is_rejected_before_rewriting_any_derived_file(self) -> None:
        si = self.journal_fixture()
        si["rights"]["redistribution_package"]["attribution"] = "Silently substituted SI attribution."
        before = self.snapshot()
        with mock.patch.object(materializer, "ROOT", self.root), self.assertRaises(materializer.RedistributionPackageError):
            materializer.build_pdf_supplement(
                self.capsule, self.version, self.retrieval, self.rights, supplementary_information=si,
            )
        self.assertEqual(self.snapshot(), before)

    def test_journal_entire_manifest_supplement_removal_is_not_a_legacy_success(self) -> None:
        self.build_journal(self.journal_fixture())
        del self.manifest["pdf_supplement"]
        self.write(self.manifest_path, self.manifest)
        self.assertTrue(any("DECLARATION_MISSING" in error for error in self.integrity_errors()))
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])
        before = self.snapshot()
        with mock.patch.object(materializer, "ROOT", self.root), mock.patch.object(
            materializer, "prepare_capsule", side_effect=AssertionError("missing opt-in must not clear old files"),
        ), mock.patch.object(materializer, "fetch_bytes", side_effect=AssertionError("missing opt-in must not fetch")), self.assertRaises(
            materializer.RedistributionPackageError,
        ):
            materializer.materialize_one(self.journal_record(), {}, "ignored")
        self.assertEqual(self.snapshot(), before)

    def test_journal_pdf_does_not_bypass_true_legacy_full_document_gates(self) -> None:
        self.build_journal(self.journal_fixture())
        for field, value in (
            ("content_tier", "full_text"), ("source_pdf", "legacy-original.pdf"),
            ("retained_markdown_source", "source/legacy.md"), ("retained_text_sources", [{"source": "source/legacy.html"}]),
        ):
            with self.subTest(field=field):
                target = self.manifest if field == "content_tier" else self.manifest["materialization"]
                original = target.get(field)
                target[field] = value
                self.write(self.manifest_path, self.manifest)
                errors, blocked, _, _ = validate_publication_rights(self.audit_path, self.root / "materialized_sources/corpus")
                self.assertEqual(errors, [])
                self.assertEqual(len(blocked), 1)
                if original is None:
                    del target[field]
                else:
                    target[field] = original

    def test_coverage_version_selection_is_explicit_and_fail_closed(self) -> None:
        version = "publisher-vor:2024-01-11"
        observed = {"source_version_recorded": None, "pdf_supplement": {
            "source_version": version, "validation_errors": [], "public_package_valid": True,
        }}
        target = {"representation": "pdf_supplement", "selected_version": version}
        self.assertTrue(target_version_matches(target, observed))
        self.assertTrue(target_version_matches({"selected_version": None}, observed))
        self.assertFalse(target_version_matches({"selected_version": version}, observed))
        self.assertFalse(target_version_matches({"representation": "unknown", "selected_version": None}, observed))
        self.assertFalse(target_version_matches(target, {"source_version_recorded": None}))
        for field, value in (
            ("source_version", ""), ("source_version", None), ("validation_errors", ["invalid SI"]),
            ("validation_errors", None), ("public_package_valid", False),
        ):
            invalid = copy.deepcopy(observed)
            invalid["pdf_supplement"][field] = value
            self.assertFalse(target_version_matches(target, invalid))
        self.assertFalse(target_version_matches({"selected_version": "v1"}, {"source_version_recorded": "v2"}))

    def test_helper_preserves_legacy_and_produces_revision_bound_pages(self) -> None:
        self.assertEqual(self.integrity_errors(), [])
        for name, old in self.legacy.items():
            self.assertEqual((self.capsule / name).read_bytes(), old)
        self.assertEqual(self.manifest["revision"], "old-tex-revision")
        self.assertEqual(self.manifest["rights"], {"old_package_marker": "unchanged"})
        self.assertEqual(self.manifest["selectors"], ["selectors.jsonl"])
        self.assertEqual([row["page"] for row in self.selector_rows()], [1, 2])
        self.assertIn("graphic-only", self.supplement["limitations"][0])
        self.assertNotIn("text_extraction_complete", self.supplement)
        self.assertEqual(self.chosen(), (self.capsule / "pdf-supplement/document.txt", self.capsule / "pdf-supplement/selectors.jsonl"))

    def test_fixed_version_and_effective_retrieval_are_required(self) -> None:
        for field, value in (("source_version", "v3"), ("source_version", None), ("revision", "old-tex-revision")):
            with self.subTest(field=field, value=value):
                old = self.supplement[field]
                self.supplement[field] = value
                self.assertTrue(self.integrity_errors())
                self.supplement[field] = old
        self.supplement["retrievals"][0]["resolved_url"] = "https://arxiv.org/pdf/2408.08435v1"
        self.assertTrue(any("RETRIEVAL" in error for error in self.integrity_errors()))
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")

    def test_dropped_page_fails_even_when_counts_are_changed(self) -> None:
        self.set_selector_rows(self.selector_rows()[:1])
        self.supplement["materialization"].update({"selector_count": 1, "pdf_text_page_count": 1})
        self.assertTrue(any("PAGE_COVERAGE" in error for error in self.integrity_errors()))

    def test_preview_cannot_come_from_another_page(self) -> None:
        rows = self.selector_rows()
        rows[0]["text_preview"] = rows[1]["text_preview"]
        self.set_selector_rows(rows)
        self.assertTrue(any("PREVIEW_CROSS_PAGE" in error for error in self.integrity_errors()))
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")

    def test_nonpage_old_selector_cannot_enter_the_new_page_file(self) -> None:
        rows = self.selector_rows()
        rows.append({"selector": "local://old#L1-L1", "local_path": self.rel(self.capsule / "normalized/document.txt"), "start_line": 1, "end_line": 1, "text_preview": "Original retained TeX"})
        self.set_selector_rows(rows)
        self.supplement["materialization"]["selector_count"] = 3
        self.assertTrue(any("NON_PAGE_SELECTOR" in error for error in self.integrity_errors()))

    def test_uninventoried_or_drifted_text_is_not_accepted(self) -> None:
        self.manifest["local_files"] = [row for row in self.manifest["local_files"] if not row["path"].endswith("pdf-supplement/document.txt")]
        self.assertTrue(any("FILE_UNHASHED" in error for error in self.integrity_errors()))
        self.refresh_inventory()
        path = self.capsule / "pdf-supplement/document.txt"
        path.write_text(path.read_text().replace("first PDF page", "silently edited page"))
        self.refresh_inventory()
        self.assertTrue(any("NATIVE_TEXT_DRIFT" in error for error in self.integrity_errors()))

    def test_pdf_requires_its_own_allowance_and_exact_approved_scope(self) -> None:
        self.assertEqual(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review), ([], []))
        del self.review["pdf_supplement"]
        self.write_audit()
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        self.rights["publication_gate"]["approved_scope"] = "Only old TeX text."
        self.metadata["rights"]["pdf_supplement"] = copy.deepcopy(self.rights)
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        self.write_metadata()
        self.write_audit()
        self.assertTrue(any("scope" in error for error in validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0]))

    def test_package_drift_or_missing_body_check_keeps_old_consumption(self) -> None:
        self.supplement["body_quality_verified"] = False
        self.assertEqual(self.chosen(), (self.capsule / "normalized/document.txt", self.capsule / "selectors.jsonl"))
        self.supplement["body_quality_verified"] = True
        self.review["pdf_supplement"]["redistribution_package"]["scope"] = "Different reviewed bytes."
        self.write_audit()
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")

    def test_pdf_scope_block_cannot_borrow_the_old_tex_allow(self) -> None:
        self.rights["publication_gate"]["decision"] = "block"
        self.metadata["rights"]["pdf_supplement"] = copy.deepcopy(self.rights)
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        self.write_metadata()
        self.write_audit()
        errors, blocked = validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)
        self.assertEqual(errors, [])
        self.assertEqual(len(blocked), 1)
        self.assertEqual(self.review["publication_gate"]["decision"], "allow")
        self.assertTrue(any("UNADMITTED" in error for error in self.integrity_errors()))
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")

    def test_notice_footer_and_pdf_revision_are_each_fail_closed(self) -> None:
        notice = self.capsule / "pdf-supplement/NOTICE.md"
        expected_notice = notice.read_text()
        notice.write_text("Substituted notice.\n")
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])
        notice.write_text(expected_notice)
        document = self.capsule / "pdf-supplement/document.txt"
        expected_text = document.read_text()
        document.write_text(expected_text.split("<!-- materialization-redistribution-notice -->", 1)[0])
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])
        document.write_text(expected_text)
        self.rights["redistribution_package"]["source_revision"] = "old-tex-revision"
        self.metadata["rights"]["pdf_supplement"] = copy.deepcopy(self.rights)
        self.review["pdf_supplement"] = copy.deepcopy(self.rights)
        self.write_metadata()
        self.write_audit()
        self.assertTrue(validate_pdf_supplement_rights(self.manifest, self.manifest_path, self.root, self.review)[0])

    def test_new_original_and_extraction_mode_cannot_be_undeclared(self) -> None:
        self.supplement["materialization"]["pdf_text_extraction_mode"] = "layout"
        self.assertTrue(any("EXTRACTION_MODE" in error for error in self.integrity_errors()))
        self.supplement["materialization"]["pdf_text_extraction_mode"] = "plain"
        del self.manifest["pdf_supplement"]
        self.assertTrue(any("UNDECLARED" in error for error in self.integrity_errors()))

    def test_primary_excerpt_must_remain_inside_the_parent_first_page(self) -> None:
        self.supplement["primary_excerpt"] = {"start_line": 3, "end_line": 3}
        self.assertEqual(self.integrity_errors(), [])
        self.assertEqual(build_demo.source_excerpt(
            (self.capsule / "pdf-supplement/document.txt").read_text(), "Parent", self.supplement,
        )[1:], (3, 3))
        self.supplement["primary_excerpt"] = {"start_line": 3, "end_line": 8}
        self.assertTrue(any("PRIMARY_EXCERPT" in error for error in self.integrity_errors()))
        self.assertEqual(self.chosen()[0], self.capsule / "normalized/document.txt")

    def test_publication_gate_checks_pdf_even_at_partial_or_metadata_tier(self) -> None:
        for tier in ("excerpt_capsule", "metadata_capsule"):
            with self.subTest(tier=tier):
                self.manifest["content_tier"] = tier
                self.write(self.manifest_path, self.manifest)
                errors, blocked, active, audited = validate_publication_rights(self.audit_path, self.root / "materialized_sources/corpus")
                self.assertEqual((errors, blocked, active, audited), ([], [], 1, 1))
                review = copy.deepcopy(self.review)
                review.pop("pdf_supplement")
                self.write(self.audit_path, {"scope": {"baseline_full_text_count": 1}, "items": [review]})
                errors, _, _, _ = validate_publication_rights(self.audit_path, self.root / "materialized_sources/corpus")
                self.assertTrue(any("PDF_SUPPLEMENT" in error for error in errors))
                self.write_audit()

    def test_pdf_rights_chain_uses_its_revision_and_package_path(self) -> None:
        source = {**self.item, "revision": self.supplement["revision"], "source_representation": "pdf_supplement", "rights_status": DECLARED, "rights": rights_snapshot(self.rights)}
        ref = make_rights_ref(source, usage="source_excerpt", transformation="Bounded PDF text excerpt.")
        self.assertEqual(ref["source_revision"], self.supplement["revision"])
        self.assertTrue(ref["package_path"].endswith("#pdf_supplement.rights.redistribution_package"))
        self.assertEqual(validate_rights_chain(root=self.root, claims=[], evidence=[], sources=[source]), [])
        source["revision"] = self.manifest["revision"]
        self.assertTrue(any("REVISION_MISMATCH" in error for error in validate_rights_chain(root=self.root, claims=[], evidence=[], sources=[source])))

    def test_helper_rejects_wrong_version_before_touching_legacy(self) -> None:
        with mock.patch.object(materializer, "ROOT", self.root):
            with self.assertRaises(ValueError):
                materializer.build_pdf_supplement(self.capsule, "v1", self.retrieval, self.rights)
        for name, old in self.legacy.items():
            self.assertEqual((self.capsule / name).read_bytes(), old)

    def test_primary_pdf_extraction_still_defaults_to_layout(self) -> None:
        page = mock.Mock()
        page.extract_text.return_value = "Original readable page text."
        reader = mock.Mock(pages=[page])
        with mock.patch("pypdf.PdfReader", return_value=reader):
            materializer.extract_pdf_text(self.pdf)
        page.extract_text.assert_called_once_with(extraction_mode="layout", layout_mode_strip_rotated=False)

    def test_plain_mode_extracts_body_embedded_in_a_form_xobject(self) -> None:
        from pypdf import PdfWriter
        from pypdf.generic import ArrayObject, DecodedStreamObject, DictionaryObject, NameObject, NumberObject
        writer = PdfWriter()
        page = writer.add_blank_page(width=612, height=792)
        font = writer._add_object(DictionaryObject({
            NameObject("/Type"): NameObject("/Font"), NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        }))
        form = DecodedStreamObject()
        form.set_data(b"BT /F1 12 Tf 72 720 Td (Embedded source body has substantial readable text and a stable conclusion.) Tj ET")
        form.update({
            NameObject("/Type"): NameObject("/XObject"), NameObject("/Subtype"): NameObject("/Form"),
            NameObject("/BBox"): ArrayObject([NumberObject(n) for n in (0, 0, 612, 792)]),
            NameObject("/Resources"): DictionaryObject({NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})}),
        })
        page[NameObject("/Resources")] = DictionaryObject({NameObject("/XObject"): DictionaryObject({NameObject("/Embedded"): writer._add_object(form)})})
        stream = DecodedStreamObject()
        stream.set_data(b"q /Embedded Do Q")
        page[NameObject("/Contents")] = writer._add_object(stream)
        output = io.BytesIO()
        writer.write(output)
        payload = output.getvalue()
        document, _, pages = materializer.extract_pdf_text(payload, extraction_mode="plain")
        self.assertEqual(pages, 1)
        self.assertIn("Embedded source body has substantial readable text", document)
        source_hash = hashlib.sha256(payload).hexdigest()
        (self.capsule / "pdf-supplement/document.pdf").write_bytes(payload)
        rights = copy.deepcopy(self.rights)
        rights["redistribution_package"]["source_revision"] = f"sha256:{source_hash}"
        retrieval = {**self.retrieval, "bytes": len(payload), "sha256": source_hash}
        with mock.patch.object(materializer, "ROOT", self.root):
            supplement = materializer.build_pdf_supplement(self.capsule, "v2", retrieval, rights)
        self.assertEqual(supplement["materialization"]["pdf_text_extraction_mode"], "plain")
        self.assertEqual(supplement["materialization"]["pdf_pages_without_extractable_text"], [])
        self.assertEqual(supplement["materialization"]["pdf_text_page_count"], 1)
        self.assertIn("Embedded source body", (self.capsule / "pdf-supplement/document.txt").read_text())


if __name__ == "__main__":
    unittest.main()
