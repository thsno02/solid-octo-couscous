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

    def test_dated_html_uses_only_its_paired_document_and_selector_sidecar(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            legacy = capsule / "document.md"
            legacy.write_bytes(b"Historical excerpt and rights footer remain unchanged.\r\n")
            (capsule / "selectors.jsonl").write_bytes(b'{"selector":"historical"}\n')
            document = capsule / "normalized/document.md"
            document.write_text("New structural HTML consumer.\n")
            selectors = capsule / "normalized/selectors.jsonl"
            selectors.write_text('{"selector":"derived"}\n')
            item = {"manifest": "materialized_sources/corpus/example/manifest.yaml"}
            manifest = {"selectors": ["selectors.jsonl", "normalized/selectors.jsonl"], "materialization": {
                "retained_text_binding": "dated_html_response", "document": "normalized/document.md", "normalized_document": "normalized/document.md",
                "retained_text_selectors": "normalized/selectors.jsonl",
                "retained_text_sources": [{"source": "source/specification.html", "format": "html"}],
            }}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), document)
                self.assertEqual(choose_local_selectors(item, manifest), selectors)
                for field, value in (("retained_text_binding", "unknown"), ("retained_text_selectors", "selectors.jsonl"), ("document", "document.md")):
                    original = manifest["materialization"][field]
                    manifest["materialization"][field] = value
                    for chooser in (choose_local_document, choose_local_selectors):
                        with self.subTest(field=field, chooser=chooser.__name__), self.assertRaises(ValueError):
                            chooser(item, manifest)
                    manifest["materialization"][field] = original
                materialization = manifest["materialization"]
                manifest["materialization"] = 7
                for chooser in (choose_local_document, choose_local_selectors):
                    with self.subTest(chooser=chooser.__name__), self.assertRaises(ValueError):
                        chooser(item, manifest)
                manifest["materialization"] = materialization
                selectors.unlink()
                for chooser in (choose_local_document, choose_local_selectors):
                    with self.subTest(chooser=chooser.__name__), self.assertRaises(ValueError):
                        chooser(item, manifest)
                old = {"materialization": {"document": "document.md"}}
                self.assertEqual(choose_local_document(item, old), legacy)
                self.assertEqual(choose_local_selectors(item, old), capsule / "selectors.jsonl")
            self.assertEqual(legacy.read_bytes(), b"Historical excerpt and rights footer remain unchanged.\r\n")

    def test_dated_html_excerpt_reuses_whole_fence_mask_without_tex_assumptions(self):
        text = (
            "# Retained specification text (collector assembly)\n\n"
            "```\n\n## Abstract\n\nThis hidden HTML code example describes an impossible unconditional result with enough prose to look like source evidence.\n\n```\n\n"
            "## Abstract\n\nThis dated specification defines a reviewable local source boundary while retaining explicit attribution and stable structural text for readers.\n"
        )
        result = source_excerpt(text, "Dated specification", reading_view=True)
        self.assertTrue(result[0].startswith("This dated specification"))
        self.assert_located(text, result)

    def test_wiki_revision_set_consumer_is_paired_and_uses_html_reading_boundaries(self):
        actual = "This documentation explains a stable revision boundary and preserves the surrounding source context so readers can verify the retained method locally."
        hidden = "This literal teaching example claims that the system always returns a correct answer for every possible question without any validation."
        text = ("# Retained wiki page revision set (collector assembly)\n\n> Collector snapshot label is not source prose.\n\n"
                "```\n==Soup==\n\n# Fake source heading\n\n" + hidden + "\n```\n\n"
                '<a id="page-1-same"></a>\n\n## Real source chapter\n\n' + actual + "\n")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            legacy = capsule / "document.md"
            legacy.write_bytes(b"Historical bounded text remains unchanged.\r\n")
            (capsule / "selectors.jsonl").write_bytes(b'{"selector":"historical"}\n')
            document = capsule / "normalized/document.md"
            document.write_text(text)
            sidecar = capsule / "normalized/selectors.jsonl"
            sidecar.write_text('{"selector":"derived"}\n')
            manifest = {"selectors": ["selectors.jsonl", "normalized/selectors.jsonl"], "materialization": {
                "retained_text_binding": "wiki_page_revision_set", "document": "normalized/document.md", "normalized_document": "normalized/document.md",
                "retained_text_selectors": "normalized/selectors.jsonl", "retained_text_sources": [{"source": f"source/page-{number}.html", "format": "html", "content_selector": "#mw-content-text .mw-parser-output"} for number in (1, 2)],
            }}
            item = {"manifest": "materialized_sources/corpus/example/manifest.yaml"}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), document)
                self.assertEqual(choose_local_selectors(item, manifest), sidecar)
                result = source_excerpt(text, "Wiki documentation", reading_view=True, wiki_page_revision_set=True)
                self.assertEqual(result[0], actual)
                self.assert_located(text, result)
                sidecar.unlink()
                for chooser in (choose_local_document, choose_local_selectors):
                    with self.assertRaises(ValueError):
                        chooser(item, manifest)
            self.assertEqual(legacy.read_bytes(), b"Historical bounded text remains unchanged.\r\n")

    def test_wiki_excerpt_takes_only_complete_bounded_paragraphs_and_keeps_legacy_sentence_output(self):
        actual = 'The property used in a statement determines both the meaning of the statement (i.e. the nature of the relationship between the subject and the object), as well as which values may be used, as specified by its data type.'
        text = '## Original chapter\n\n' + actual + '\n'
        result = source_excerpt(text, 'Wiki documentation', reading_view=True, wiki_page_revision_set=True)
        self.assertEqual(result[0], actual)
        self.assert_located(text, result)
        self.assertEqual(source_excerpt(text, 'Legacy view', reading_view=True)[0], actual.split('i.e.')[0] + 'i.e.')
        oversized = ('This original paragraph states an important condition that cannot be detached from the surrounding context. ' * 9).strip()
        self.assertGreater(len(oversized), 700)
        short = 'This next original paragraph provides sufficient continuous evidence to describe the method while retaining its full conditions and reviewed source context.'
        text = oversized + '\n\n' + short + '\n'
        result = source_excerpt(text, 'Wiki documentation', reading_view=True, wiki_page_revision_set=True)
        self.assertEqual(result[0], short)
        self.assert_located(text, result)
        hidden = '> Collector source role: hatnote (original text and links follow).\n> ' + short + '\n'
        self.assertEqual(source_excerpt(oversized + '\n\n' + hidden, 'Wiki documentation', reading_view=True, wiki_page_revision_set=True), ('', 1, 1))

    def test_git_text_consumer_uses_sidecar_and_excludes_yaml_example_and_anchors(self):
        actual = "This fixed specification defines an explicit native contract boundary with stable source evidence and retained original attribution for readers."
        hidden = "This hidden YAML example describes an impossible unconditional result with enough prose to resemble automatically quoted source evidence."
        text = ("# Retained specification text (collector assembly)\n\n> Collector assembly labels are not source prose.\n\n"
                "```yaml\n\n# Fake heading\n\n" + hidden + "\n```\n\n"
                '<a id="chapter-L1"></a>\n\n## Native chapter\n\n' + actual + "\n")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            legacy = capsule / "document.md"
            legacy.write_bytes(b"Historical excerpt and footer remain unchanged.\r\n")
            (capsule / "selectors.jsonl").write_bytes(b'{"selector":"historical"}\n')
            document = capsule / "normalized/document.md"
            document.write_text(text)
            selectors = capsule / "normalized/selectors.jsonl"
            selectors.write_text('{"selector":"derived"}\n')
            item = {"manifest": "materialized_sources/corpus/example/manifest.yaml"}
            manifest = {"selectors": ["selectors.jsonl", "normalized/selectors.jsonl"], "materialization": {
                "retained_text_binding": "git_snapshot", "document": "normalized/document.md", "normalized_document": "normalized/document.md",
                "retained_text_selectors": "normalized/selectors.jsonl",
                "retained_text_sources": [{"source": "source/docs/chapter.md", "format": "md"},
                    {"source": "source/docs/full-example.contract.yaml", "format": "yaml", "role": "example"}],
            }}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), document)
                self.assertEqual(choose_local_selectors(item, manifest), selectors)
                result = source_excerpt(document.read_text(), "Native contract", reading_view=True)
                self.assertEqual(result[0], actual)
                self.assert_located(text, result)
                for name in ("retained_text_binding", "retained_text_selectors"):
                    original = manifest["materialization"].pop(name)
                    for chooser in (choose_local_document, choose_local_selectors):
                        with self.subTest(missing=name, chooser=chooser.__name__), self.assertRaises(ValueError):
                            chooser(item, manifest)
                    manifest["materialization"][name] = original
                selectors.unlink()
                for chooser in (choose_local_document, choose_local_selectors):
                    with self.subTest(chooser=chooser.__name__), self.assertRaises(ValueError):
                        chooser(item, manifest)
            self.assertEqual(legacy.read_bytes(), b"Historical excerpt and footer remain unchanged.\r\n")

    def test_metadata_only_git_consumer_uses_single_sidecar_without_legacy_files(self):
        actual = "This native document states its actual source boundary with sufficient continuous prose to support an exact consumer excerpt without collector metadata."
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            capsule = root / "materialized_sources/corpus/example"
            (capsule / "normalized").mkdir(parents=True)
            document = capsule / "normalized/document.md"
            document.write_text("# Retained documentation text (collector assembly)\n\n> Collector include provenance is not source prose.\n\n## Native overview\n\n" + actual + "\n")
            selectors = capsule / "normalized/selectors.jsonl"
            selectors.write_text('{"selector":"derived"}\n')
            item = {"manifest": "materialized_sources/corpus/example/manifest.yaml"}
            manifest = {"selectors": ["normalized/selectors.jsonl"], "materialization": {
                "retained_text_binding": "git_snapshot", "document": "normalized/document.md", "normalized_document": "normalized/document.md",
                "retained_text_selectors": "normalized/selectors.jsonl", "retained_text_sources": [{"source": "source/docs/overview.md", "format": "md"}],
            }}
            with mock.patch.object(build_demo, "ROOT", root):
                self.assertEqual(choose_local_document(item, manifest), document)
                self.assertEqual(choose_local_selectors(item, manifest), selectors)
                self.assertEqual(source_excerpt(document.read_text(), "Native overview", reading_view=True)[0], actual)
                selectors.unlink()
                with self.assertRaises(ValueError):
                    choose_local_document(item, manifest)
            self.assertFalse((capsule / "document.md").exists())
            self.assertFalse((capsule / "selectors.jsonl").exists())

    def test_reading_view_skips_whole_anchor_contaminated_candidate_without_cleaning(self):
        anchored = (
            "This anchored source paragraph provides enough contiguous prose to satisfy the existing excerpt length and word criteria.\n"
            '<a id="specification-ref-for-term-1"></a>\n'
            "The paragraph continues with source words, but its collector locator must not become an automatically quoted statement."
        )
        actual = "This next source paragraph states the explicit document scope in continuous prose without any collector markup or inferred sentence joining."
        text = "## Abstract\n\n" + anchored + "\n\n" + actual + "\n"
        result = source_excerpt(text, "Specification", reading_view=True)
        self.assertEqual(result[0], actual)
        self.assertEqual((result[1], result[2]), (7, 7))
        self.assert_located(text, result)
        self.assertEqual(source_excerpt("## Abstract\n\n" + anchored, "Specification", reading_view=True), ("", 1, 1))
        # The non-opt-in quotation path remains exactly the legacy selection.
        self.assertTrue(source_excerpt(text, "Specification")[0].startswith("This anchored source paragraph"))

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
