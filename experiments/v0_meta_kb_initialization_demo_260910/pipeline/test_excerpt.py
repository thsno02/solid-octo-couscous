"""Offline regressions for source quotation and stable evidence locations."""
import unittest
import tempfile
from pathlib import Path
from unittest import mock

import build_demo
from build_demo import choose_local_document, choose_local_selectors, domain_bucket, inclusion_reason_field, meaningful_excerpt, source_excerpt


class ExcerptTests(unittest.TestCase):
    def assert_located(self, text, result):
        excerpt, first, last = result
        self.assertTrue(excerpt)
        self.assertGreaterEqual(first, 1)
        self.assertLessEqual(last, len(text.splitlines()))
        self.assertIn(excerpt, " ".join("\n".join(text.splitlines()[first - 1:last]).split()))

    def test_multiline_abstract(self):
        text = "package junk\n\n## Abstract\n\n" + "\n".join(
            ["This study describes a source based method", "for building evidence linked knowledge with stable references.",
             "The resulting candidate remains subject to independent human review."])
        result = meaningful_excerpt(text, "A paper")
        self.assert_located(text, result)
        self.assertEqual(result[1], 5)

    def test_does_not_quote_repository_header_or_html(self):
        text = "# Repository semantic capsule\n\n- Commit: abcdef\n- Description: metadata only\n\n<p align='center'>\nSome badges and links are not prose.\n</p>\n\n" + (
            "This repository provides a method for collecting local source evidence and producing reviewable knowledge pages.\n")
        result = meaningful_excerpt(text, "repository")
        self.assert_located(text, result)
        self.assertTrue(result[0].startswith("This repository provides"))

    def test_no_fabricated_excerpt_for_nonprose(self):
        self.assertEqual(meaningful_excerpt("article\n\nusepackage\n\n# Heading\n", "Paper")[0], "")

    def test_opt_in_skips_whole_fences_with_internal_blank_lines_and_fake_abstract(self):
        hidden = "This hidden template or inactive branch contains enough detailed prose to look like a source assertion."
        actual = "This current paper describes a locally retained method with source evidence and stable boundaries for a reviewable derived view."
        for fence in ("```latex", "````latex", "~~~latex"):
            closing = fence.split("latex")[0]
            text = f"{fence}\n\n## Abstract\n\n{hidden}\n\n```\n\nMore hidden code.\n{closing}\n\n## Abstract\n\n{actual}\n"
            # For triple-backtick fences that intermediate triple closes the block;
            # do not manufacture a malformed fixture for the ordinary valid case.
            if fence == "```latex":
                text = f"{fence}\n\n## Abstract\n\n{hidden}\n{closing}\n\n## Abstract\n\n{actual}\n"
            with self.subTest(fence=fence):
                result = source_excerpt(text, "Paper", reading_view=True)
                self.assertTrue(result[0].startswith("This current paper"))
                self.assert_located(text, result)

    def test_opt_in_never_quotes_only_fallback_or_unterminated_fence(self):
        paragraph = "This internal code example describes a false source statement that should never become an automatically generated assertion."
        self.assertEqual(source_excerpt("# Derived view\n\n> Collector description is not source prose.\n\n```latex\n\n" + paragraph + "\n```\n", "Paper", reading_view=True)[0], "")
        self.assertEqual(source_excerpt("```latex\n\n" + paragraph, "Paper", reading_view=True)[0], "")

    def test_explicit_reading_consumer_is_chosen_and_missing_view_never_uses_legacy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            legacy = capsule / "normalized/document.txt"
            legacy.write_text("Legacy document is still retained.\n")
            reading = capsule / "normalized/reading.md"
            reading.write_text("Chosen conservative reading view.\n")
            item = {"uid": "arxiv:synthetic", "manifest": "materialized_sources/corpus/example/manifest.yaml"}
            view = {"enabled": True, "profile": "conservative-v1", "document": "normalized/reading.md"}
            manifest = {"materialization": {"document": "normalized/reading.md", "tex_reading_view": view}}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), reading)
                self.assertEqual(choose_local_selectors(item, manifest), capsule / "selectors.jsonl")
                reading.unlink()
                with self.assertRaises(ValueError):
                    choose_local_document(item, manifest)
                manifest = {"materialization": {"document": "normalized/document.txt"}}
                self.assertEqual(choose_local_document(item, manifest), legacy)

    def test_long_wrapped_paragraph(self):
        text = "\n".join(["Evidence locations must cover every quoted word in the original local source"] * 20) + "."
        result = meaningful_excerpt(text, "Paper")
        self.assert_located(text, result)
        self.assertLessEqual(len(result[0]), 700)

    def test_short_first_sentence_is_not_silently_removed(self):
        text = "This is a test. The rest of this paragraph explains how evidence locations preserve a contiguous source quotation."
        result = meaningful_excerpt(text, "Paper")
        self.assert_located(text, result)
        self.assertTrue(result[0].startswith("This is a test."))

    def test_metadata_selector_tracks_fallback_field(self):
        self.assertEqual(inclusion_reason_field({"summary": "  Collected   context. "}), ("summary", "Collected context."))
        with self.assertRaises(ValueError):
            inclusion_reason_field({})

    def test_acronyms_do_not_match_inside_unrelated_words(self):
        self.assertEqual(domain_bucket({"title": "Data Catalog Vocabulary Version 3", "canonical_id": "DCAT"}, {}), "cross-cutting")
        self.assertEqual(domain_bucket({"title": "Knowledge compilation paragraph"}, {}), "cross-cutting")
        self.assertEqual(domain_bucket({"title": "RSI research"}, {}), "recursive-self-improvement")
        self.assertEqual(domain_bucket({"title": "Self-improving systems"}, {}), "recursive-self-improvement")

    def test_optional_unadmitted_pdf_does_not_replace_the_old_document_or_selectors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            old = capsule / "normalized/document.txt"
            old.write_text("Original retained document remains available.\n")
            item = {"uid": "arxiv:2408.08435", "manifest": "materialized_sources/corpus/example/manifest.yaml"}
            manifest = {"materialization": {"document": "normalized/document.txt"}}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), old)
                manifest["pdf_supplement"] = {"body_quality_verified": True, "rights": {"publication_gate": {"decision": "allow"}}}
                self.assertEqual(choose_local_document(item, manifest), old)
                self.assertEqual(choose_local_selectors(item, manifest), capsule / "selectors.jsonl")

    def test_new_pdf_default_cannot_quote_an_embedded_paper_abstract(self):
        text = (
            "## Page 1\n\n# Parent paper\n\n"
            "This parent study describes a source method with enough contiguous prose to support its own bounded excerpt.\n\n"
            "## Page 2\n\n## Abstract\n\n"
            "This embedded different paper describes adaptive dual scale methods and is not the parent work's assertion.\n"
        )
        self.assertTrue(meaningful_excerpt(text, "Parent")[0].startswith("This embedded"))
        result = source_excerpt(text, "Parent", {})
        self.assertTrue(result[0].startswith("This parent"))
        self.assert_located(text, result)
        self.assertLess(result[2], 7)

    def test_explicit_primary_pdf_range_skips_author_block_and_retains_global_offsets(self):
        text = (
            "## Page 1\n\n# Parent paper\n"
            + "Author affiliations and metadata are not the verified abstract. " * 20 + "\n\n"
            "This parent paper proposes an evidence linked method with sufficient prose and a verified continuous statement.\n"
            "The resulting system remains a source reported candidate rather than an independently established scientific fact.\n\n"
            "## Page 2\n\n## Abstract\n\n"
            "An embedded separate paper makes a different assertion that must not become this source's default claim.\n"
        )
        result = source_excerpt(text, "Parent", {"primary_excerpt": {"start_line": 6, "end_line": 7}})
        self.assertTrue(result[0].startswith("This parent paper"))
        self.assert_located(text, result)
        self.assertEqual(result[1], 6)
        self.assertLessEqual(result[2], 7)
        for declaration in ({"start_line": 6, "end_line": 12}, {"start_line": 1, "end_line": 7}, {"start_line": True, "end_line": 7}):
            with self.subTest(declaration=declaration), self.assertRaises(ValueError):
                source_excerpt(text, "Parent", {"primary_excerpt": declaration})


if __name__ == "__main__":
    unittest.main()
