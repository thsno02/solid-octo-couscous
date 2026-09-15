"""Offline regressions for source quotation and stable evidence locations."""
import unittest

from build_demo import domain_bucket, inclusion_reason_field, meaningful_excerpt


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


if __name__ == "__main__":
    unittest.main()
