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
