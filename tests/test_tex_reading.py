"""Offline, isolated regressions for the opt-in conservative TeX reading view."""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import materialize_all_sources as materializer
import validate_materialization_completeness as validator
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experiments/v0_meta_kb_initialization_demo_260910/pipeline"))
from build_demo import source_excerpt


def document(body: str, preamble: str = "") -> str:
    return "\\documentclass{article}\n" + preamble + "\n\\begin{document}\n" + body + "\n\\end{document}\n"


class TexReadingTests(unittest.TestCase):
    def render(self, body: str, preamble: str = "", extra: dict[str, str] | None = None):
        files = {"entry.tex": document(body, preamble), **(extra or {})}
        return materializer.derive_tex_reading("entry.tex", files, [])

    def test_arbitrary_static_names_nested_wrappers_and_aliases(self):
        text, assessment = self.render(
            r"The \nebula{} method uses \alias{} evidence and \textbf{nested \emph{formatting}}.",
            "\\newcommand{\\nebula}{Local}\n\\newcommand{\\alias}{\\nebula}")
        self.assertIn("The Local method uses Local evidence and nested formatting.", text)
        self.assertFalse(assessment["diagnostics"])

    def test_arbitrary_proven_empty_argument_macro_suppresses_nested_old_body(self):
        text, _ = self.render(
            "\\eraseAnything{\\begin{abstract}\nOLD inactive {nested} statement.\n\\end{abstract}}\n"
            "\\begin{abstract}\nCurrent retained statement.\n\\end{abstract}",
            r"\newcommand{\eraseAnything}[1]{}")
        self.assertNotIn("OLD inactive", text)
        self.assertIn("Current retained statement.", text)
        self.assertIn(r"\newcommand{\eraseAnything}[1]{}", text)

    def test_cycle_dynamic_definition_and_redefinition_remain_fallback(self):
        cases = [
            (r"\newcommand{\a}{\b}\newcommand{\b}{\a}", r"Before \a after."),
            (r"\newcommand{\a}{\def\b{hidden}value}", r"Before \a after."),
            (r"\newcommand{\a}{first}\renewcommand{\a}{second}", r"Before \a after."),
            (r"\renewcommand{\textbf}[1]{different meaning}", r"Before \textbf{original} after."),
            (r"\newcommand{\textbf}{\textbf{not safely expanded}}", r"Before \textbf after."),
        ]
        for preamble, body in cases:
            with self.subTest(preamble=preamble):
                text, assessment = self.render(body, preamble)
                self.assertIn("```latex\n" + body, text)
                self.assertTrue(assessment["diagnostics"])

    def test_macro_depth_limit_never_falls_through_a_redefined_builtin(self):
        preamble = "\n".join(r"\newcommand{\alias" + chr(65 + index) + "}{\\alias" + chr(66 + index) + "}" for index in range(20))
        preamble += r"\newcommand{\aliasU}{\textbf}\newcommand{\textbf}{\textbf{unsafe meaning}}"
        body = r"Before \aliasA after."
        text, _ = self.render(body, preamble)
        self.assertIn("```latex\n" + body, text)

    def test_retained_fence_does_not_strip_literal_tail_spaces_or_blank_lines(self):
        raw = "Literal {ticker} {% ... %}  \n\n   \n"
        self.assertIn(raw, materializer.tex_reading_fence(raw))
        self.assertIn("tail  \n", materializer.tex_reading_fence("tail  "))

    def test_math_qualifier_is_not_split_into_an_unconditional_automatic_claim(self):
        body = "Under the assumptions $p>0$, the estimator is guaranteed to return an unbiased result for every target population, including previously omitted low-resource cases."
        text, assessment = self.render(body)
        self.assertIn("```latex\n" + body + "\n```", text)
        self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
        self.assertTrue(assessment["diagnostics"])

    def test_unknown_balanced_multiline_argument_never_exposes_hidden_prose(self):
        hidden = "This hidden historical statement asserts that the current system always guarantees accurate answers for every possible question without any additional validation."
        body = "\\cacheOnly{\n\n" + hidden + "\n\n}"
        for preamble in [r"\newcommand{\cacheOnly}[1]{\iffalse#1\fi}", ""]:
            with self.subTest(preamble=preamble):
                text, assessment = self.render(body, preamble)
                self.assertIn("```latex\n" + body + "\n```", text)
                self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
                self.assertTrue(assessment["diagnostics"])

    def test_unsafe_multiline_heading_is_whole_raw_fallback_not_markdown(self):
        hidden = "This hidden historical statement asserts that the current system always guarantees accurate answers for every possible question without any additional validation."
        body = "\\section{Current heading \\cacheOnly{\n\n" + hidden + "\n\n}}"
        text, assessment = self.render(body, r"\newcommand{\cacheOnly}[1]{\iffalse#1\fi}")
        self.assertIn("```latex\n" + body + "\n```", text)
        self.assertNotIn("## Current heading", text)
        self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
        self.assertIn("retained_unsafe_heading", [item["kind"] for item in assessment["diagnostics"]])

    def test_reference_and_url_groups_admit_only_finite_literal_values(self):
        hidden = "This hidden historical statement asserts that the current system always guarantees accurate answers for every possible question without any additional validation."
        for name in ["citep", "ref", "url", "href"]:
            body = "\\" + name + "{\\unknown{\n\n" + hidden + "\n\n}}"
            if name == "href":
                body += "{visible label}"
            with self.subTest(name=name):
                text, assessment = self.render(body)
                self.assertIn("```latex\n" + body + "\n```", text)
                self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
                self.assertTrue(assessment["diagnostics"])
        text, assessment = self.render(r"Literal citation \citep{smith2025, doe2024} and reference \ref{thm:any} remain explicit keys.")
        self.assertIn("[cite: smith2025, doe2024]", text)
        self.assertIn("[ref: thm:any]", text)
        self.assertFalse(assessment["diagnostics"])

    def test_literal_url_tilde_is_preserved_while_prose_nonbreaking_space_is_rendered(self):
        value, admissible = materializer.tex_reading_inline(r"Prose~label \url{https://example.org/~author/notes}", {})
        self.assertTrue(admissible)
        self.assertEqual(value, "Prose label https://example.org/~author/notes")

    def test_literal_url_percent_is_explicitly_unadmitted_before_comment_processing(self):
        with self.assertRaisesRegex(ValueError, "literal percent in TeX url"):
            self.render(r"\url{https://example.org/a%20b}")
        listing = "\\begin{lstlisting}\n\\url{https://example.org/a%20b}\n\\end{lstlisting}"
        text, _ = self.render(listing + "\n% \\url{https://example.org/a%20b}\nActual body.")
        self.assertIn(listing, text)
        self.assertIn("Actual body.", text)

    def test_starred_static_macro_and_optional_citation_qualifiers_remain_exact(self):
        cases = [
            (r"\newcommand{\status}{APPROVED}", r"The \status* result is a statement with enough detailed prose to be incorrectly treated as an automatic source assertion."),
            ("", r"We claim this estimator is valid for every target case \citep[only under positive support][Theorem 2]{smith2025}."),
        ]
        for preamble, body in cases:
            with self.subTest(body=body):
                text, assessment = self.render(body, preamble)
                self.assertIn("```latex\n" + body + "\n```", text)
                self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
                self.assertTrue(assessment["diagnostics"])

    def test_group_local_and_body_definitions_are_never_global_proven_noops(self):
        visible = "This current statement is visible after the local group closes and describes the actual result rather than a historical draft."
        for definition in [r"{\def\relax#1{}}", r"\def\relax#1{}", r"{\newcommand{\local}[1]{}}"]:
            name = "local" if "newcommand" in definition else "relax"
            body = definition + "\n\n\\" + name + "{" + visible + "}"
            with self.subTest(definition=definition):
                text, assessment = self.render(body)
                self.assertIn(visible, text)
                self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")
                self.assertTrue(assessment["diagnostics"])

    def test_grouped_preamble_definition_is_not_static(self):
        text, assessment = self.render(r"\local{must remain visible}", r"{\newcommand{\local}[1]{}}")
        self.assertIn(r"\local{must remain visible}", text)
        self.assertTrue(assessment["diagnostics"])

    def test_escaped_literal_braces_are_not_unbalanced_body_groups(self):
        text, _ = self.render(r"The literal \{entity\} placeholder and 25\% marker remain visible.")
        self.assertIn("The literal {entity} placeholder and 25% marker remain visible.", text)

    def test_redefined_layout_and_heading_commands_are_retained_not_interpreted(self):
        for preamble, body in [(r"\renewcommand{\maketitle}{The final reported result is negative rather than positive.}", r"\maketitle"),
                               (r"\renewcommand{\section}[1]{}", r"\section{inactive heading}"),
                               (r"\renewcommand{\item}[1]{}", r"\item{inactive item}")]:
            with self.subTest(preamble=preamble):
                text, _ = self.render(body, preamble)
                self.assertIn("```latex\n" + body + "\n```", text)

    def test_structured_environment_end_in_comment_or_literal_never_ends_the_block(self):
        sentence = "This theorem statement asserts that the estimator is uniformly accurate for every population and requires no additional assumptions about sample quality."
        for fake in [r"% \end{theorem}", r"\verb|\end{theorem}|", "\\begin{lstlisting}\n\\end{theorem}\n\\end{lstlisting}"]:
            block = "\\begin{theorem}\n" + fake + "\n\n" + sentence + "\n\n\\end{theorem}"
            with self.subTest(fake=fake):
                text, _ = self.render(block)
                self.assertIn("```latex\n" + block + "\n```", text)
                self.assertEqual(source_excerpt(text, "Paper", reading_view=True)[0], "")

    def test_conditional_and_unknown_environment_are_whole_retained_blocks(self):
        for block in [
            "\\iffalse\n\nThis inactive branch must not become current prose.\n\\else\nOther branch.\n\\fi",
            "\\begin{mysterious}\n\nUnknown environment prose is not statically established.\n\\end{mysterious}",
        ]:
            with self.subTest(block=block):
                text, _ = self.render(block)
                self.assertIn("```latex\n" + block + "\n```", text)

    def test_literals_preserve_percent_template_braces_and_fake_input(self):
        listing = "\\begin{lstlisting}[caption={Literal {example}}]\n{ticker}\n{% template %}\n"
        listing += "Line end\\\\% \\input{not-body}\n\nLiteral paragraph.\n\\end{lstlisting}"
        inline = r"\verb|{%...%} \input{also-not-body}|"
        text, assessment = self.render(listing + "\n\n" + inline)
        self.assertIn(listing, text)
        self.assertIn(inline, text)
        self.assertFalse(assessment["include_graph"])
        self.assertFalse(assessment["diagnostics"])

    def test_ordinary_comment_parity_does_not_expand_commented_input(self):
        text, assessment = self.render("Line end\\\\% \\input{absent}\nActual body.")
        self.assertNotIn("absent", text)
        self.assertIn("Actual body.", text)
        self.assertFalse(assessment["include_graph"])

    def test_math_algorithm_and_table_are_exact_retained_expressions(self):
        blocks = [
            r"$x_{t} \geq y \cdot z + \sum_{i=1}^{n} a_i \setminus b$",
            "\\begin{equation}\n\\frac{x}{y} \\leq \\expect[Z] \\to \\reals\n\\end{equation}",
            "\\begin{algorithm}\n\\begin{algorithmic}\n\\IF{$x \\geq y$}\n\\STATE \\pt \\gets x\n\\ENDIF\n\\end{algorithmic}\n\\end{algorithm}",
            "\\begin{table}\n\\begin{tabular}{@{}lr@{}}\n\\textbf{Metric} & \\score \\\\\nA & 3{,}000 \\\\\n\\end{tabular}\n\\end{table}",
        ]
        text, _ = self.render("\n\n".join(blocks), r"\newcommand{\expect}{\mathbb{E}}")
        for block in blocks:
            self.assertIn("```latex\n" + block + "\n```", text)
        self.assertIn(r"\newcommand{\expect}{\mathbb{E}}", text)

    def test_real_nested_reference_titles_and_body_boundary(self):
        text, assessment = self.render(
            r"\subsection{Proof of \textbf{Theorem~\ref{thm:any}}}" + "\nActual proof.\n",
            "Preamble must not be active prose.\n\\newcommand{\\unused}{definition}")
        self.assertIn("### Proof of Theorem [ref: thm:any]", text)
        self.assertNotIn("Preamble must not be active prose", text)
        self.assertNotIn(r"\end{document}", text)
        source = document(r"\subsection{Proof of \textbf{Theorem~\ref{thm:any}}}" + "\nActual proof.\n", "Preamble must not be active prose.\n\\newcommand{\\unused}{definition}")
        self.assertEqual(assessment["body_end_line"], len(source.splitlines()))

    def test_safe_literal_include_and_import_reuse_existing_resolver(self):
        text, assessment = self.render(
            r"\input{chapter}\import{appendix/}{proof}",
            extra={"chapter.tex": r"\section{Included body}" + "\nIncluded prose.", "appendix/proof.tex": "Local proof."})
        self.assertIn("## Included body", text)
        self.assertIn("Local proof.", text)
        self.assertEqual([row["to"] for row in assessment["include_graph"]], ["chapter.tex", "appendix/proof.tex"])

    def test_macro_definition_input_and_conditional_input_are_not_expanded(self):
        text, assessment = self.render(
            "\\iffalse\n\\input{missing-inactive}\n\\fi",
            r"\newcommand{\example}{\input{missing-in-definition}}")
        self.assertIn(r"\input{missing-inactive}", text)
        self.assertIn(r"\input{missing-in-definition}", text)
        self.assertFalse(assessment["include_graph"])

    def test_missing_include_cycle_and_unterminated_literal_raise_before_output(self):
        for files in [
            {"entry.tex": document(r"\input{absent}")},
            {"entry.tex": document(r"\input{loop}"), "loop.tex": r"\input{loop}"},
            {"entry.tex": document(r"\begin{lstlisting} never closed")},
        ]:
            with self.subTest(files=files), self.assertRaises(ValueError):
                materializer.derive_tex_reading("entry.tex", files, [])


class ReadingReplayTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        self.patches = mock.patch.multiple(materializer, ROOT=self.root, CORPUS_ROOT=self.root / "materialized_sources/corpus")
        self.patches.start()
        metadata_path = self.root / "raw_data/arxiv/example/metadata.yaml"
        metadata_path.parent.mkdir(parents=True)
        metadata = {"uid": "arxiv:9912.12345", "title": "Synthetic retained work", "canonical_id": "9912.12345", "versioning": {"source_version": "v8"}}
        self.record = materializer.SourceRecord(uid=metadata["uid"], source_type="arxiv", canonical_id=metadata["canonical_id"], title=metadata["title"], canonical_url="https://arxiv.org/abs/9912.12345v8", metadata_path=metadata_path, metadata=metadata, priority="P0", rights_access="open")
        self.capsule = self.record.capsule_root
        (self.capsule / "source").mkdir(parents=True)
        (self.capsule / "normalized").mkdir()
        self.original = document("\\begin{abstract}\nThis current paper describes a local method with stable source evidence and explicitly retained mathematical expressions.\n\\end{abstract}\n\\subsection{Proof of Theorem~\\ref{thm:any}}\n\\begin{equation}\nx \\geq y\\cdot z\n\\end{equation}\n\\bibliography{refs}", r"\newcommand{\support}{\mathbb{R}}")
        (self.capsule / "source/entry.tex").write_text(self.original)
        (self.capsule / "source/refs.bib").write_text("@article{local, title={A retained citation}}\n@misc{uncited, title={Uncited local support}}\n")
        (self.capsule / "normalized/document.tex").write_bytes(b"Historical TEX bytes\r\n")
        (self.capsule / "normalized/document.txt").write_bytes(b"Historical TXT and footer bytes\r\n")
        (self.capsule / "source-metadata.yaml").write_text(yaml.safe_dump(metadata))
        originals = [{"path": path.relative_to(self.root).as_posix(), "bytes": path.stat().st_size, "sha256": materializer.sha256_file(path)} for path in sorted((self.capsule / "source").iterdir())]
        materializer.write_jsonl(self.capsule / "files.jsonl", originals)
        self.prefix = b'{ "selector": "original://retained#L1", "local_path": "unused-test-path", "kind": "file", "start_line": 1, "end_line": 1 }\n'
        (self.capsule / "selectors.jsonl").write_bytes(self.prefix)
        self.manifest = materializer.base_manifest(self.record, "arxiv_latex_v2", "fixed-time")
        self.manifest.update({"revision": "sha256:retained-archive-revision", "status": "partial", "content_tier": "full_text", "selectors": ["selectors.jsonl"], "retrievals": [{"historical": "unchanged"}], "materialization": {"document": "normalized/document.txt", "tex_reading_view": {"enabled": True, "profile": "conservative-v1", "source_root": "source/entry.tex", "document": "normalized/reading.md", "citation_support": ["source/refs.bib"]}}})
        self.refresh_inventory()

    def tearDown(self):
        self.patches.stop()
        self.temporary.cleanup()

    def refresh_inventory(self):
        self.manifest["local_files"] = materializer.local_file_inventory(self.capsule)
        self.manifest["local_bytes"] = sum(row["bytes"] for row in self.manifest["local_files"])
        materializer.write_yaml(self.capsule / "manifest.yaml", self.manifest)

    def snapshot(self):
        return {path.relative_to(self.capsule).as_posix(): path.read_bytes() for path in self.capsule.rglob("*") if path.is_file()}

    def validate(self):
        errors = []
        actual = {row["path"]: materializer.sha256_file(self.root / row["path"]) for row in self.manifest["local_files"]}
        validator.validate_tex_reading_view(self.manifest, self.capsule, actual, errors, repository_root=self.root)
        return errors

    def test_replay_preserves_original_legacy_prefix_and_is_byte_idempotent(self):
        before = self.snapshot()
        with mock.patch.object(materializer, "fetch_bytes", side_effect=AssertionError("network prohibited")), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("prepare prohibited")), mock.patch.object(materializer, "write_arxiv_tex_derivatives", side_effect=AssertionError("legacy writer prohibited")):
            self.manifest = materializer.materialize_arxiv(self.record, {}, "not-a-new-time")
            first = self.snapshot()
            self.manifest = materializer.replay_arxiv_tex_reading(self.record)
            self.assertEqual(first, self.snapshot())
        for name, content in before.items():
            if name.startswith("source/") or name in {"files.jsonl", "normalized/document.tex", "normalized/document.txt"}:
                self.assertEqual(content, self.snapshot()[name])
        self.assertTrue((self.capsule / "selectors.jsonl").read_bytes().startswith(self.prefix))
        self.assertEqual(self.manifest["generated_at"], "fixed-time")
        self.assertEqual(self.manifest["retrievals"], [{"historical": "unchanged"}])
        self.assertEqual(self.manifest["status"], "partial")
        self.assertIn("may include uncited entries", (self.capsule / "normalized/reading.md").read_text())
        self.assertFalse(self.validate())
        rows = [json.loads(line) for line in (self.capsule / "selectors.jsonl").read_text().splitlines()][1:]
        proof = next(row for row in rows if row.get("heading") == "Proof of Theorem [ref: thm:any]")
        self.assertEqual(proof["source_heading_path"], (self.capsule / "source/entry.tex").relative_to(self.root).as_posix())
        self.assertIn(r"\begin{equation}", "\n".join((self.capsule / "normalized/reading.md").read_text().splitlines()[proof["start_line"] - 1:proof["end_line"]]))

    def test_nonroot_style_newif_is_not_parsed_and_all_source_bytes_remain_intact(self):
        style = self.capsule / "source/layout.sty"
        style.write_bytes(b"\\newif\\ifdraft\r\n\\drafttrue\r\n")
        metadata = self.capsule / "source/00README.json"
        metadata.write_bytes(b'{"note": "\\\\newif\\\\ifdraft is auxiliary text"}\r\n')
        rows = [json.loads(line) for line in (self.capsule / "files.jsonl").read_text().splitlines()]
        for path in (style, metadata):
            rows.append({"path": path.relative_to(self.root).as_posix(), "bytes": path.stat().st_size, "sha256": materializer.sha256_file(path)})
        materializer.write_jsonl(self.capsule / "files.jsonl", rows)
        self.refresh_inventory()
        before = self.snapshot()
        with mock.patch.object(materializer, "fetch_bytes", side_effect=AssertionError("network prohibited")), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("prepare prohibited")):
            self.manifest = materializer.replay_arxiv_tex_reading(self.record, self.manifest)
        after = self.snapshot()
        for name, content in before.items():
            if name.startswith("source/") or name in {"files.jsonl", "normalized/document.tex", "normalized/document.txt"}:
                self.assertEqual(content, after[name])
        self.assertTrue(after["selectors.jsonl"].startswith(self.prefix))
        self.assertFalse(self.validate())

    def test_absent_wrong_ambiguous_root_or_changed_inventory_preflight_preserves_every_byte(self):
        for mutation in ("root", "ambiguous", "bytes", "missing", "include"):
            with self.subTest(mutation=mutation):
                saved = self.snapshot()
                if mutation == "root":
                    self.manifest["materialization"]["tex_reading_view"]["source_root"] = "source/wrong.tex"
                elif mutation == "ambiguous":
                    path = self.capsule / "source/second.tex"
                    path.write_text(document("Another actual work."))
                    rows = [json.loads(line) for line in (self.capsule / "files.jsonl").read_text().splitlines()]
                    rows.append({"path": path.relative_to(self.root).as_posix(), "bytes": path.stat().st_size, "sha256": materializer.sha256_file(path)})
                    materializer.write_jsonl(self.capsule / "files.jsonl", rows)
                    self.refresh_inventory()
                elif mutation == "bytes":
                    (self.capsule / "normalized/document.txt").write_text("changed legacy")
                elif mutation == "missing":
                    (self.capsule / "source/entry.tex").unlink()
                else:
                    (self.capsule / "source/entry.tex").write_text(document(r"\input{absent}"))
                before = self.snapshot()
                with self.assertRaises(materializer.ArxivPreflightError):
                    materializer.replay_arxiv_tex_reading(self.record, self.manifest)
                self.assertEqual(before, self.snapshot())
                for path in self.capsule.rglob("*"):
                    if path.is_file() and path.relative_to(self.capsule).as_posix() not in saved:
                        path.unlink()
                for name, content in saved.items():
                    (self.capsule / name).write_bytes(content)
                self.manifest = materializer.load_yaml(self.capsule / "manifest.yaml")

    def test_reading_validator_rejects_missing_derived_provenance_wrong_span_and_raw_uri(self):
        self.manifest = materializer.replay_arxiv_tex_reading(self.record, self.manifest)
        selector_file = self.capsule / "selectors.jsonl"
        original = selector_file.read_bytes()
        for field, value in [("derived_from", ""), ("transformation", ""), ("source_paths", []), ("text_preview", "NOT IN OWN RANGE"), ("end_line", 999999), ("selector", "arxiv://raw#L1")]:
            with self.subTest(field=field):
                rows = [json.loads(line) for line in original.splitlines()]
                rows[-1][field] = value
                materializer.write_jsonl(selector_file, rows)
                self.assertTrue(self.validate())
        selector_file.write_bytes(self.prefix)
        self.assertTrue(self.validate())

    def test_new_footer_only_changes_reading_and_is_double_finalized_idempotently(self):
        old = {"source_revision": self.manifest["revision"], "source_version_url": self.record.canonical_url,
               "notice_path": (self.capsule / "NOTICE.md").relative_to(self.root).as_posix(),
               "attribution": "Synthetic attribution.", "modifications": "Historical lossy normalization.", "scope": "Historical source/TXT."}
        new = {**old, "modifications": "Added conservative collector-derived reading view.", "scope": "Retained sources, legacy normalized files and reading view."}
        (self.capsule / "NOTICE.md").write_text("Complete synthetic notice.\n")
        old_text = "Historical TXT.\n" + materializer.redistribution_footer(old, "../NOTICE.md")
        (self.capsule / "normalized/document.txt").write_text(old_text)
        self.manifest["rights"]["redistribution_package"] = old
        self.record.metadata["rights"] = {"access": "open", "redistribution_package": new}
        self.refresh_inventory()
        self.manifest = materializer.replay_arxiv_tex_reading(self.record, self.manifest, "explicit-fixed-time")
        first = self.snapshot()
        self.manifest = materializer.replay_arxiv_tex_reading(self.record, generated_at="explicit-fixed-time")
        self.assertEqual(first, self.snapshot())
        self.assertEqual((self.capsule / "normalized/document.txt").read_text(), old_text)
        reading = (self.capsule / "normalized/reading.md").read_text()
        self.assertEqual(reading.count("<!-- materialization-redistribution-notice -->"), 1)
        self.assertTrue(reading.endswith(materializer.redistribution_footer(new, "../NOTICE.md")))
        self.assertEqual(self.manifest["rights"]["redistribution_package"], new)


if __name__ == "__main__":
    unittest.main()
