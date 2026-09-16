from __future__ import annotations

import contextlib
import gzip
import hashlib
import io
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

import materialize_all_sources as materializer
import validate_materialization_completeness as validator


def minimal_pdf_pages(texts: list[str]) -> bytes:
    """Build a small text PDF fixture without adding a test-only dependency."""

    page_ids = list(range(3, 3 + len(texts)))
    font_id = 3 + len(texts)
    content_ids = list(range(font_id + 1, font_id + 1 + len(texts)))
    kids = " ".join(f"{page_id} 0 R" for page_id in page_ids).encode("ascii")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [" + kids + b"] /Count " + str(len(texts)).encode("ascii") + b" >>",
    ]
    for content_id in content_ids:
        objects.append(
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            + f"/Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>".encode("ascii")
        )
    objects.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    for text in texts:
        escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        stream = f"BT\n/F1 12 Tf\n72 720 Td\n({escaped}) Tj\nET\n".encode("ascii")
        objects.append(
            b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"endstream"
        )
    payload = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, value in enumerate(objects, 1):
        offsets.append(len(payload))
        payload.extend(f"{number} 0 obj\n".encode("ascii"))
        payload.extend(value)
        payload.extend(b"\nendobj\n")
    xref_offset = len(payload)
    payload.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    payload.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        payload.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    payload.extend(
        f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    return bytes(payload)


def minimal_text_pdf(text: str = "Readable arXiv PDF regression evidence for the materializer.") -> bytes:
    return minimal_pdf_pages([text])


class MaterializerBoundaryTests(unittest.TestCase):
    def _run_arxiv(
        self,
        payload: bytes,
        content_type: str,
        *,
        source_version: str | None = None,
        first_invalid: tuple[bytes, str] | None = None,
        extract_result: tuple[str, list[dict[str, object]], int] | None = None,
        redistribution_package: dict[str, str] | None = None,
    ) -> tuple[tempfile.TemporaryDirectory[str], Path, Path, dict[str, object], list[str]]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        metadata_path = root / "raw_data" / "arxiv" / "example" / "metadata.yaml"
        metadata_path.parent.mkdir(parents=True)
        metadata = {
            "uid": "arxiv:1234.5678",
            "title": "Example",
            "url": "https://arxiv.org/abs/1234.5678",
            "versioning": {"source_version": source_version},
        }
        if redistribution_package is not None:
            metadata["rights"] = {
                "access": "open",
                "redistribution_package": redistribution_package,
            }
            notice_source = root / redistribution_package["notice_path"]
            notice_source.parent.mkdir(parents=True, exist_ok=True)
            notice_source.write_text("Complete test license.\n", encoding="utf-8")
        metadata_path.write_text(yaml.safe_dump(metadata), encoding="utf-8")
        record = materializer.SourceRecord(
            uid="arxiv:1234.5678",
            source_type="arxiv",
            canonical_id="1234.5678",
            title="Example",
            canonical_url="https://arxiv.org/abs/1234.5678",
            metadata_path=metadata_path,
            metadata=metadata,
            priority="P0",
            rights_access="open" if redistribution_package is not None else "unknown",
        )
        requested: list[str] = []
        eprint_calls = 0

        def fetch(url: str, **_: object) -> tuple[bytes, str, dict[str, str]]:
            nonlocal eprint_calls
            requested.append(url)
            if "/e-print/" in url:
                eprint_calls += 1
                if first_invalid is not None and eprint_calls == 1:
                    invalid_payload, invalid_type = first_invalid
                    return invalid_payload, url, {"content-type": invalid_type}
                return payload, url, {"content-type": content_type}
            return (
                b"Bounded abstract fallback evidence, not the complete paper.\n",
                url,
                {"content-type": "text/plain"},
            )

        with contextlib.ExitStack() as stack:
            stack.enter_context(
                mock.patch.multiple(
                    materializer,
                    ROOT=root,
                    MATERIALIZED_ROOT=root / "materialized_sources",
                    CORPUS_ROOT=root / "materialized_sources" / "corpus",
                )
            )
            stack.enter_context(mock.patch.object(materializer, "fetch_bytes", side_effect=fetch))
            if extract_result is not None:
                stack.enter_context(
                    mock.patch.object(materializer, "extract_pdf_text", return_value=extract_result)
                )
            manifest = materializer.materialize_arxiv(
                record,
                {"restricted_excerpt_chars": 1500, "generic_max_candidate_urls": 1},
                "2026-09-16T00:00:00Z",
            )
            capsule = record.capsule_root
        return temporary, root, capsule, manifest, requested

    def test_reviewed_notice_survives_rebuild_without_shifting_source_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            payload = b"Source evidence remains at its original location.\n" * 10
            package = {
                "source_revision": "sha256:" + hashlib.sha256(payload).hexdigest(),
                "source_version_url": "https://example.test/fixed-version",
                "notice_path": "license.md",
                "attribution": "Copyright example author; derived from the fixed version.",
                "modifications": "Converted to plain text.",
                "scope": "Text only.",
            }
            (root / "license.md").write_text("Complete test license.\n", encoding="utf-8")
            metadata = {"rights": {"access": "open", "redistribution_package": package}}
            record = materializer.SourceRecord(
                uid="paper:example", source_type="paper", canonical_id="example", title="Example",
                canonical_url="https://example.test/fixed-version", metadata_path=root / "metadata.yaml",
                metadata=metadata, priority="P0", rights_access="open",
            )
            with mock.patch.multiple(materializer, ROOT=root, CORPUS_ROOT=root / "materialized_sources/corpus"), mock.patch.object(
                materializer, "fetch_bytes", return_value=(payload, record.canonical_url, {"content-type": "text/plain"}),
            ):
                for _ in range(2):
                    manifest = materializer.materialize_generic(record, {}, "2026-09-16T00:00:00Z")
                    document = record.capsule_root / "document.txt"
                    before = document.read_text(encoding="utf-8")
                    materializer.finalize_capsule(record, record.capsule_root, manifest)
                    self.assertEqual(document.read_text(encoding="utf-8"), before)
                    self.assertTrue(before.startswith(payload.decode()))
                    self.assertEqual(before.count("<!-- materialization-redistribution-notice -->"), 1)
                    self.assertEqual((record.capsule_root / "NOTICE.md").read_text(), "Complete test license.\n")
                    self.assertEqual(manifest["rights"]["redistribution_package"], package)
                package["source_revision"] = "sha256:unreviewed-revision"
                with self.assertRaises(materializer.RedistributionPackageError):
                    materializer.materialize_one(record, {}, "2026-09-16T00:00:00Z")

    def test_filter_drops_truncated_preview_and_clamps_line_selector_uri(self) -> None:
        document = "alpha\nbeta\n"
        selectors = [
            {
                "selector": "text://sha256-example#L1-L9",
                "start_line": 1,
                "end_line": 9,
                "text_preview": "alpha",
            },
            {"selector": "web://example#B2", "ordinal": 2, "text_preview": "removed"},
            {"selector": "pdf://example#page=2", "page": 2, "text_preview": "removed"},
        ]

        filtered, omitted = materializer.filter_selectors_for_document(selectors, document)

        self.assertEqual(omitted, 2)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0]["end_line"], 2)
        self.assertEqual(filtered[0]["selector"], "text://sha256-example#L1-L2")

    def test_open_text_clipped_by_budget_is_not_labeled_full_text(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            metadata_path = root / "raw_data" / "paper" / "example" / "metadata.yaml"
            metadata_path.parent.mkdir(parents=True)
            metadata = {"uid": "paper:example", "title": "Example", "url": "https://example.test/text"}
            metadata_path.write_text(yaml.safe_dump(metadata), encoding="utf-8")
            record = materializer.SourceRecord(
                uid="paper:example",
                source_type="paper",
                canonical_id="example",
                title="Example",
                canonical_url="https://example.test/text",
                metadata_path=metadata_path,
                metadata=metadata,
                priority="P0",
                rights_access="open",
            )
            payload = (b"alpha beta gamma delta\n" * 20)
            with mock.patch.multiple(
                materializer,
                ROOT=root,
                MATERIALIZED_ROOT=root / "materialized_sources",
                CORPUS_ROOT=root / "materialized_sources" / "corpus",
            ), mock.patch.object(
                materializer,
                "fetch_bytes",
                return_value=(payload, "https://example.test/text", {"content-type": "text/plain"}),
            ):
                manifest = materializer.materialize_generic(
                    record,
                    {"open_full_text_max_chars": 260, "generic_max_candidate_urls": 1},
                    "2026-09-16T00:00:00Z",
                )

            self.assertEqual(manifest["status"], "partial")
            self.assertEqual(manifest["content_tier"], "excerpt_capsule")
            self.assertTrue(manifest["materialization"]["content_was_truncated"])

    def test_heading_only_document_is_not_substantive(self) -> None:
        self.assertFalse(materializer.has_substantive_document_text("# Home\n"))
        self.assertTrue(materializer.has_substantive_document_text("# Home\n\nActual source evidence is present.\n"))

    def test_arxiv_landing_fallback_is_bounded_even_on_open_domain(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            metadata_path = root / "raw_data" / "arxiv" / "example" / "metadata.yaml"
            metadata_path.parent.mkdir(parents=True)
            metadata = {
                "uid": "arxiv:1234.5678",
                "title": "Example",
                "url": "https://arxiv.org/abs/1234.5678",
            }
            metadata_path.write_text(yaml.safe_dump(metadata), encoding="utf-8")
            record = materializer.SourceRecord(
                uid="arxiv:1234.5678",
                source_type="arxiv",
                canonical_id="1234.5678",
                title="Example",
                canonical_url="https://arxiv.org/abs/1234.5678",
                metadata_path=metadata_path,
                metadata=metadata,
                priority="P0",
                rights_access="open",
            )
            payload = b"Abstract evidence from the landing page, but not the complete paper.\n"
            def fetch(url: str, **_: object) -> tuple[bytes, str, dict[str, str]]:
                if "/e-print/" in url:
                    raise RuntimeError("offline archive failure")
                return (
                    payload,
                    "https://arxiv.org/abs/1234.5678",
                    {"content-type": "text/plain"},
                )

            with mock.patch.multiple(
                materializer,
                ROOT=root,
                MATERIALIZED_ROOT=root / "materialized_sources",
                CORPUS_ROOT=root / "materialized_sources" / "corpus",
            ), mock.patch.object(
                materializer,
                "fetch_bytes",
                side_effect=fetch,
            ):
                manifest = materializer.materialize_arxiv(
                    record,
                    {"restricted_excerpt_chars": 1500, "open_full_text_domains": ["arxiv.org"]},
                    "2026-09-16T00:00:00Z",
                )

            self.assertTrue(manifest["rights"]["full_text_redistribution_assumed"])
            self.assertEqual(manifest["status"], "partial")
            self.assertEqual(manifest["content_tier"], "excerpt_capsule")
            reason = manifest["materialization"]["forced_excerpt_reason"]
            self.assertIn("fallback evidence, not full text", reason)
            self.assertIn(reason, manifest["warnings"])

    def test_arxiv_raw_pdf_uses_fixed_version_and_page_selectors(self) -> None:
        pdf = minimal_text_pdf()
        temporary, _, capsule, manifest, requested = self._run_arxiv(
            pdf, "text/html", source_version="v2"
        )
        with temporary:
            pdf_hash = hashlib.sha256(pdf).hexdigest()
            self.assertEqual(requested[0], "https://export.arxiv.org/e-print/1234.5678v2")
            self.assertEqual(manifest["adapter"], "arxiv_pdf_v1")
            self.assertEqual(manifest["archive_container"], "pdf")
            self.assertEqual(manifest["media_type"], "application/pdf")
            self.assertEqual(manifest["revision"], f"sha256:{pdf_hash}")
            self.assertEqual(manifest["status"], "materialized")
            self.assertEqual(manifest["content_tier"], "full_text")
            self.assertEqual((capsule / "source/document.pdf").read_bytes(), pdf)
            self.assertIn("Readable arXiv PDF regression evidence", (capsule / "document.txt").read_text())
            selectors = [json.loads(line) for line in (capsule / "selectors.jsonl").read_text().splitlines()]
            self.assertEqual(len(selectors), 1)
            self.assertTrue(selectors[0]["selector"].startswith(f"pdf://sha256-{pdf_hash[:16]}#page=1"))

    def test_arxiv_gzip_pdf_keeps_transport_revision_and_pdf_selector_hash(self) -> None:
        pdf = minimal_text_pdf()
        response = gzip.compress(pdf, mtime=0)
        temporary, _, capsule, manifest, _ = self._run_arxiv(response, "application/gzip")
        with temporary:
            response_hash = hashlib.sha256(response).hexdigest()
            pdf_hash = hashlib.sha256(pdf).hexdigest()
            self.assertEqual(manifest["archive_container"], "gzip-pdf")
            self.assertEqual(manifest["revision"], f"sha256:{response_hash}")
            self.assertEqual(manifest["materialization"]["source_pdf_sha256"], pdf_hash)
            self.assertEqual((capsule / "source/document.pdf").read_bytes(), pdf)
            selector = json.loads((capsule / "selectors.jsonl").read_text().splitlines()[0])
            self.assertTrue(selector["selector"].startswith(f"pdf://sha256-{pdf_hash[:16]}#page=1"))

    def test_arxiv_single_tex_and_gzip_single_tex_still_materialize(self) -> None:
        tex = b"\\documentclass{article}\n\\begin{document}\nSource text.\n\\end{document}\n"
        archive_buffer = io.BytesIO()
        with tarfile.open(fileobj=archive_buffer, mode="w") as archive:
            member = tarfile.TarInfo("main.tex")
            member.size = len(tex)
            archive.addfile(member, io.BytesIO(tex))
        for payload, content_type, container in (
            (tex, "application/x-tex", "single"),
            (gzip.compress(tex, mtime=0), "application/gzip", "gzip-single"),
            (archive_buffer.getvalue(), "application/x-tar", "tar"),
        ):
            with self.subTest(container=container):
                temporary, _, capsule, manifest, _ = self._run_arxiv(payload, content_type)
                with temporary:
                    self.assertEqual(manifest["adapter"], "arxiv_latex_v2")
                    self.assertEqual(manifest["archive_container"], container)
                    self.assertEqual(manifest["content_tier"], "full_text")
                    self.assertEqual((capsule / "source/main.tex").read_bytes(), tex)

    def test_tex_root_selection_uses_document_structure_not_name_or_size(self) -> None:
        document = "\\documentclass{article}\n\\begin{document}\nReal body.\n\\end{document}\n"
        for suffix in ("tex", "ltx", "txt"):
            with self.subTest(suffix=suffix):
                files = {
                    "main.tex": "\\section{Oversized fragment}\n" * 100,
                    f"draft/unusual-root.{suffix}": document,
                    "readme.txt": "An ordinary text file, not a TeX document.\n",
                    "layout.cls": document,
                }
                self.assertEqual(materializer.choose_main_tex(files), f"draft/unusual-root.{suffix}")

    def test_tex_root_selection_rejects_fragments_comments_and_ambiguity(self) -> None:
        document = "\\documentclass{article}\n\\begin{document}\nReal body.\n\\end{document}\n"
        for files in (
            {"main.tex": "\\section{Fragment}\n"},
            {"notes.txt": "\\begin{document}\nA fragment.\n\\end{document}\n"},
            {"notes.txt": "% \\documentclass{article}\n% \\begin{document}\n% \\end{document}\n"},
            {"main.tex": "\\documentclass{article}\n\\begin{document}\nTruncated.\n"},
            {"paper.tex": document, "larger.txt": document + "Unrelated trailing text.\n" * 100},
        ):
            with self.subTest(files=list(files)):
                self.assertIsNone(materializer.choose_main_tex(files))

    def test_tex_root_selection_excludes_only_explicit_non_target_roles(self) -> None:
        document = "\\documentclass{article}\n\\title{Research findings}\n\\begin{document}\nEvidence.\n\\end{document}\n"
        files = {
            "unusual.txt": document,
            "assets/drawing.tex": document.replace("{article}", "{standalone}"),
            "sample.tex": document.replace("Research findings", "Formatting Instructions for Example Conference Submissions"),
            "guide.ltx": document.replace("Research findings", "\\LaTeX\\ Author Guidelines for Example Proceedings"),
            "style.tex": document.replace("Research findings", "A new style for Example papers"),
            "revision-history/dated.tex": document,
            "history/whole-paper-pre_final_revision.tex": document,
        }
        exclusions: list[dict[str, str]] = []
        self.assertEqual(materializer.tex_root_candidates(files, exclusions=exclusions), ["unusual.txt"])
        self.assertEqual(len(exclusions), 6)
        self.assertTrue(all(item["evidence"] for item in exclusions))
        for companion in ("si.tex", "neurips_2022.tex", "template.tex", "history/research.tex"):
            with self.subTest(companion=companion):
                # A suggestive name, different research title, or genuine supplement is not a template.
                candidates = {"main.tex": document, companion: document.replace("Research findings", "Supporting Information - Research findings")}
                self.assertIsNone(materializer.choose_main_tex(candidates))
                self.assertEqual(len(materializer.tex_root_candidates(candidates)), 2)

    def test_tex_comment_parity_is_shared_by_roots_includes_and_plain_text(self) -> None:
        for slash_count in range(5):
            with self.subTest(backslashes=slash_count):
                line = "Line end" + "\\" * slash_count + "% \\input{not-body}\n"
                is_comment = slash_count % 2 == 0
                stripped = materializer.tex_without_comments(line)
                self.assertEqual("\\input{not-body}" not in stripped, is_comment)
                graph: list[dict[str, str]] = []
                errors: list[dict[str, str]] = []
                flattened = materializer.flatten_tex("paper.tex", {
                    "paper.tex": line, "not-body.tex": "INCLUDED EVIDENCE.\n",
                }, diagnostics=errors, include_graph=graph)
                self.assertEqual(errors, [])
                self.assertEqual(bool(graph), not is_comment)
                self.assertEqual("INCLUDED EVIDENCE." in materializer.tex_to_plain(flattened), not is_comment)
                fake_root = line.replace("\\input{not-body}", "\\begin{document} Fake. \\end{document}")
                self.assertEqual(bool(materializer.tex_root_candidates({"paper.tex": fake_root})), not is_comment)
        self.assertEqual(materializer.tex_without_comments("escaped \\% retained % omitted\r\nnext\n"), "escaped \\% retained \r\nnext\n")

    def test_tex_include_expansion_handles_nested_relative_paths_and_comments(self) -> None:
        files = {
            "draft/paper.txt": (
                "\\documentclass{article}\n\\begin{document}\n"
                "% \\input{not-body}\n\\input{../body}\n\\include{sections/appendix}\n\\end{document}\n"
            ),
            "body.tex": "\\section{Introduction}\nBody evidence.\n\\input{sections/detail.ltx}\n",
            "sections/detail.ltx": "Detailed evidence.\n",
            "draft/sections/appendix.tex": "\\appendix\n\\section{Appendix}\nAppendix evidence.\n",
            "not-body.tex": "COMMENTED CONTENT MUST NOT ENTER THE BODY.\n",
        }
        diagnostics: list[dict[str, str]] = []
        graph: list[dict[str, str]] = []
        flattened = materializer.flatten_tex("draft/paper.txt", files, diagnostics=diagnostics, include_graph=graph)
        self.assertEqual(diagnostics, [])
        self.assertEqual(graph, [
            {"from": "draft/paper.txt", "to": "body.tex"},
            {"from": "body.tex", "to": "sections/detail.ltx"},
            {"from": "draft/paper.txt", "to": "draft/sections/appendix.tex"},
        ])
        self.assertLess(flattened.index("Body evidence."), flattened.index("Detailed evidence."))
        self.assertLess(flattened.index("Detailed evidence."), flattened.index("Appendix evidence."))
        self.assertNotIn("COMMENTED CONTENT", flattened)
        self.assertIsNone(materializer.resolve_tex_include("draft/paper.txt", "../../not-body.tex", files))
        self.assertIsNone(materializer.resolve_tex_include("paper.txt", "/not-body.tex", files))

    def test_tex_include_diagnostics_keep_missing_cycles_and_depth_visible(self) -> None:
        for files, depth, expected in (
            ({"main.txt": "\\input{missing}"}, 20, "missing_include"),
            ({"main.txt": "\\input{body}", "body.tex": "\\input{main.txt}"}, 20, "cycle"),
            ({"main.txt": "\\input{body}", "body.tex": "Evidence."}, 1, "depth_limit"),
        ):
            with self.subTest(kind=expected):
                diagnostics: list[dict[str, str]] = []
                flattened = materializer.flatten_tex("main.txt", files, max_depth=depth, diagnostics=diagnostics)
                self.assertEqual([item["kind"] for item in diagnostics], [expected])
                if expected == "missing_include":
                    self.assertIn("\\input{missing}", flattened)
                else:
                    self.assertIn("omitted" if expected == "cycle" else "depth exceeded", flattened)

    def test_tex_plain_normalization_excludes_preamble_and_trailing_material(self) -> None:
        tex = (
            "\\documentclass{article}\n\\newcommand{\\layout}{PREAMBLE MUST NOT ENTER BODY}\n"
            "% \\begin{document}\n\\begin {document}\n"
            "\\begin{abstract}\nAbstract evidence.\n\\end{abstract}\n"
            "\\section{Introduction}\\label{sec:introduction}\nBody evidence.\n\\appendix\n"
            "\\section{Appendix}\nAppendix evidence.\n\\end {document}\n"
            "TRAILING BUILD MATERIAL\n"
        )
        plain = materializer.tex_to_plain(tex)
        self.assertNotIn("PREAMBLE", plain)
        self.assertNotIn("TRAILING", plain)
        self.assertNotIn("sec:introduction", plain)
        self.assertIn("## Abstract\n", plain)
        self.assertIn("## Introduction\n", plain)
        self.assertIn("Appendix evidence.", plain)

    def test_tex_plain_reports_semantic_abstract_omitted_from_preamble(self) -> None:
        for abstract in ("\\abstract{Preamble abstract evidence.}\n", "\\begin{abstract}Preamble abstract evidence.\\end{abstract}\n"):
            with self.subTest(abstract=abstract):
                diagnostics: list[dict[str, str]] = []
                tex = "\\documentclass{article}\n" + abstract + "\\begin{document}\nBody evidence.\n\\end{document}\n"
                plain = materializer.tex_to_plain(tex, diagnostics=diagnostics, path="unusual.tex")
                self.assertNotIn("Preamble abstract evidence", plain)
                self.assertEqual(diagnostics, [{"kind": "preamble_semantic_abstract_omitted", "path": "unusual.tex"}])
                temporary, _, capsule, manifest, _ = self._run_arxiv(tex.encode(), "application/x-tex")
                with temporary:
                    self.assertEqual(manifest["status"], "partial")
                    self.assertEqual(manifest["materialization"]["tex_normalization_diagnostics"], [
                        {"kind": "preamble_semantic_abstract_omitted", "path": "main.tex"},
                    ])
                    self.assertIn("Preamble abstract evidence.", (capsule / "normalized/document.tex").read_text())
                    self.assertTrue(any("not a full TeX parser" in item for item in manifest["limitations"]))

    def test_arxiv_new_payload_ambiguity_preserves_retained_capsule_and_raises(self) -> None:
        document = b"\\documentclass{article}\n\\begin{document}\nOriginal evidence.\n\\end{document}\n"
        temporary, root, capsule, _, _ = self._run_arxiv(document, "application/x-tex")
        with temporary:
            metadata_path = root / "raw_data/arxiv/example/metadata.yaml"
            record = materializer.SourceRecord(
                uid="arxiv:1234.5678", source_type="arxiv", canonical_id="1234.5678", title="Example",
                canonical_url="https://arxiv.org/abs/1234.5678", metadata_path=metadata_path,
                metadata=yaml.safe_load(metadata_path.read_text()), priority="P0", rights_access="unknown",
            )
            before = {path.relative_to(capsule).as_posix(): path.read_bytes() for path in capsule.rglob("*") if path.is_file()}
            archive_buffer = io.BytesIO()
            with tarfile.open(fileobj=archive_buffer, mode="w") as archive:
                for path in ("new-target.tex", "real-supplement.tex"):
                    member = tarfile.TarInfo(path)
                    member.size = len(document)
                    archive.addfile(member, io.BytesIO(document))
            with mock.patch.multiple(materializer, ROOT=root, CORPUS_ROOT=root / "materialized_sources/corpus"), mock.patch.object(
                materializer, "fetch_bytes", return_value=(archive_buffer.getvalue(), record.canonical_url, {"content-type": "application/x-tar"}),
            ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("preflight must preserve old capsule")), mock.patch.object(
                materializer, "finalize_capsule", side_effect=AssertionError("preflight must not rewrite old manifest"),
            ), mock.patch.object(materializer.time, "sleep"):
                with self.assertRaisesRegex(materializer.ArxivPreflightError, "new-target.tex"):
                    materializer.materialize_one(record, {}, "2026-09-16T00:00:00Z")
                # The executor must also propagate a preflight failure rather than prepare a fallback capsule.
                with mock.patch.object(sys, "argv", ["materializer", "--workers", "1"]), mock.patch.object(
                    materializer, "load_yaml", return_value={"workers": 1},
                ), mock.patch.object(materializer, "discover_records", return_value=[record]):
                    with self.assertRaises(materializer.ArxivPreflightError):
                        materializer.main()
            after = {path.relative_to(capsule).as_posix(): path.read_bytes() for path in capsule.rglob("*") if path.is_file()}
            self.assertEqual(before, after)

    def test_arxiv_txt_root_derivatives_preserve_source_and_finalize_offline(self) -> None:
        files = {
            "unusual-root.txt": (
                "\\documentclass{article}\n\\newcommand{\\layout}{PREAMBLE NOT BODY}\n"
                "\\begin{document}\n\\begin{abstract}\nAbstract evidence.\n\\end{abstract}\n"
                "\\input{sections/body}\n\\include{appendix}\n\\end{document}\n"
            ),
            "sections/body.tex": "\\section{Introduction}\nBody evidence.\n",
            "appendix.tex": "\\appendix\n\\section{Appendix}\nAppendix evidence.\n",
        }
        archive_buffer = io.BytesIO()
        with tarfile.open(fileobj=archive_buffer, mode="w") as archive:
            for path, text in files.items():
                payload = text.encode()
                member = tarfile.TarInfo(path)
                member.size = len(payload)
                archive.addfile(member, io.BytesIO(payload))
        temporary, root, capsule, manifest, _ = self._run_arxiv(archive_buffer.getvalue(), "application/x-tar")
        with temporary:
            before_manifest = yaml.safe_load((capsule / "manifest.yaml").read_text())
            original = {path: (capsule / "source" / path).read_bytes() for path in files}
            original["files.jsonl"] = (capsule / "files.jsonl").read_bytes()
            metadata_path = root / "raw_data/arxiv/example/metadata.yaml"
            record = materializer.SourceRecord(
                uid="arxiv:1234.5678", source_type="arxiv", canonical_id="1234.5678", title="Example",
                canonical_url="https://arxiv.org/abs/1234.5678", metadata_path=metadata_path,
                metadata=yaml.safe_load(metadata_path.read_text()), priority="P0", rights_access="unknown",
            )
            with mock.patch.multiple(materializer, ROOT=root, CORPUS_ROOT=root / "materialized_sources/corpus"), mock.patch.object(
                materializer, "fetch_bytes", side_effect=AssertionError("offline derivatives must not fetch"),
            ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("retain the capsule")):
                derivatives = materializer.write_arxiv_tex_derivatives(record, capsule, files, revision=manifest["revision"])
                manifest["materialization"].update(derivatives)
                manifest["status"] = "partial"
                manifest["warnings"].append("Fixture original assets/version remain unresolved.")
                materializer.finalize_capsule(record, capsule, manifest)
                first = {path.relative_to(capsule).as_posix(): path.read_bytes() for path in capsule.rglob("*") if path.is_file()}
                materializer.finalize_capsule(record, capsule, manifest)
                second = {path.relative_to(capsule).as_posix(): path.read_bytes() for path in capsule.rglob("*") if path.is_file()}
            self.assertEqual(first, second)
            self.assertEqual(derivatives["main_tex"], "unusual-root.txt")
            self.assertEqual(derivatives["tex_include_errors"], [])
            self.assertEqual(manifest["status"], "partial")
            for field in ("retrievals", "revision", "rights"):
                self.assertEqual(manifest[field], before_manifest[field])
            for path, expected in original.items():
                target = capsule / path if path == "files.jsonl" else capsule / "source" / path
                self.assertEqual(target.read_bytes(), expected)
            plain = (capsule / "normalized/document.txt").read_text()
            self.assertNotIn("PREAMBLE", plain)
            self.assertIn("Body evidence.", plain)
            self.assertIn("Appendix evidence.", plain)
            selectors = [json.loads(line) for line in (capsule / "selectors.jsonl").read_text().splitlines()]
            self.assertEqual(len(selectors), derivatives["selector_count"])
            for selector in selectors:
                lines = (root / selector["local_path"]).read_text().splitlines()
                self.assertLessEqual(selector["end_line"], len(lines))
                if "derived_from" in selector:
                    span = "\n".join(lines[selector["start_line"] - 1:selector["end_line"]])
                    self.assertIn(selector["text_preview"], span)

    def test_arxiv_missing_and_unsupported_include_syntax_remain_partial(self) -> None:
        for include, expected in (("\\input{missing}", "missing_include"), ("\\input body.tex", "unsupported_include_syntax")):
            with self.subTest(kind=expected):
                tex = ("\\documentclass{article}\n\\begin{document}\n" + include + "\n\\end{document}\n").encode()
                temporary, _, capsule, manifest, _ = self._run_arxiv(tex, "application/x-tex")
                with temporary:
                    self.assertEqual(manifest["status"], "partial")
                    self.assertEqual(manifest["materialization"]["tex_include_errors"][0]["kind"], expected)
                    self.assertIn(include, (capsule / "normalized/document.tex").read_text())
                    self.assertTrue(any("include expansion is incomplete" in warning for warning in manifest["warnings"]))

    def test_arxiv_multiple_documents_are_not_resolved_by_file_size(self) -> None:
        document = b"\\documentclass{article}\n\\begin{document}\nEvidence.\n\\end{document}\n"
        archive_buffer = io.BytesIO()
        with tarfile.open(fileobj=archive_buffer, mode="w") as archive:
            for path, payload in (("main.tex", document), ("larger.txt", document + b"Trailing text.\n" * 100)):
                member = tarfile.TarInfo(path)
                member.size = len(payload)
                archive.addfile(member, io.BytesIO(payload))
        temporary, _, capsule, manifest, _ = self._run_arxiv(archive_buffer.getvalue(), "application/x-tar")
        with temporary:
            self.assertIsNone(manifest["materialization"]["main_tex"])
            self.assertIsNone(manifest["materialization"]["normalized_document"])
            self.assertEqual(manifest["status"], "partial")
            self.assertFalse((capsule / "normalized/document.txt").exists())
            self.assertTrue(any("Multiple TeX document roots" in warning for warning in manifest["warnings"]))

    def test_arxiv_tex_package_links_nested_notice_idempotently(self) -> None:
        tex = b"\\documentclass{article}\n\\begin{document}\nSource text.\n\\end{document}\n"
        package = {
            "source_revision": "sha256:" + hashlib.sha256(tex).hexdigest(),
            "source_version_url": "https://arxiv.org/e-print/1234.5678v2",
            "notice_path": "license.md",
            "attribution": "Copyright example authors; derived from the fixed version.",
            "modifications": "Converted TeX to plain text.",
            "scope": "Article text only.",
        }
        temporary, root, capsule, manifest, _ = self._run_arxiv(
            tex,
            "application/x-tex",
            source_version="v2",
            redistribution_package=package,
        )
        with temporary:
            document = capsule / "normalized/document.txt"
            expected_footer = materializer.redistribution_footer(package, "../NOTICE.md")
            wrapped = document.read_text(encoding="utf-8")
            self.assertEqual(manifest["materialization"]["document"], "normalized/document.txt")
            self.assertTrue(wrapped.endswith(expected_footer))
            self.assertIn("[NOTICE.md](../NOTICE.md)", wrapped)
            self.assertEqual(wrapped.count("<!-- materialization-redistribution-notice -->"), 1)

            metadata_path = root / "raw_data/arxiv/example/metadata.yaml"
            metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
            record = materializer.SourceRecord(
                uid="arxiv:1234.5678",
                source_type="arxiv",
                canonical_id="1234.5678",
                title="Example",
                canonical_url="https://arxiv.org/abs/1234.5678",
                metadata_path=metadata_path,
                metadata=metadata,
                priority="P0",
                rights_access="open",
            )
            with mock.patch.multiple(
                materializer,
                ROOT=root,
                MATERIALIZED_ROOT=root / "materialized_sources",
                CORPUS_ROOT=root / "materialized_sources/corpus",
            ):
                materializer.finalize_capsule(record, capsule, manifest)
                refinalized = document.read_text(encoding="utf-8")
                materializer.finalize_capsule(record, capsule, manifest)

            self.assertEqual(refinalized, wrapped)
            self.assertEqual(document.read_text(encoding="utf-8"), wrapped)
            self.assertEqual(wrapped.count("<!-- materialization-redistribution-notice -->"), 1)

    def test_arxiv_rejects_error_pages_and_tries_the_second_eprint_host(self) -> None:
        tex = b"\\documentclass{article}\n\\begin{document}\nValid source.\n\\end{document}\n"
        temporary, _, capsule, manifest, requested = self._run_arxiv(
            tex,
            "application/x-tex",
            first_invalid=(
                b"<!doctype html><title>temporary error</title>\\documentclass{article}",
                "text/html",
            ),
        )
        with temporary:
            self.assertEqual(requested[:2], [
                "https://export.arxiv.org/e-print/1234.5678",
                "https://arxiv.org/e-print/1234.5678",
            ])
            self.assertEqual(manifest["content_tier"], "full_text")
            self.assertEqual((capsule / "source/main.tex").read_bytes(), tex)
            self.assertTrue(any("rejected unsupported" in warning for warning in manifest["warnings"]))

    def test_arxiv_raw_and_gzip_error_pages_fall_back_without_fake_tex(self) -> None:
        error_page = b'{"error":"not an e-print: \\\\documentclass{article}"}'
        for payload in (error_page, gzip.compress(error_page, mtime=0)):
            with self.subTest(gzip=payload.startswith(b"\x1f\x8b")):
                temporary, _, capsule, manifest, _ = self._run_arxiv(payload, "application/pdf")
                with temporary:
                    self.assertEqual(manifest["adapter"], "generic_web_or_document_v2")
                    self.assertEqual(manifest["status"], "partial")
                    self.assertEqual(manifest["content_tier"], "excerpt_capsule")
                    self.assertFalse((capsule / "source/main.tex").exists())

    def test_arxiv_pdf_image_only_page_is_recorded_without_selector(self) -> None:
        pdf = minimal_text_pdf()
        extracted = (
            "## Page 1\n\nReadable source evidence remains locally available.\n\n## Page 2\n",
            [
                {"selector": "pdf://sha256-PENDING#page=1", "kind": "page", "page": 1,
                 "text_preview": "Readable source evidence remains locally available."},
                {"selector": "pdf://sha256-PENDING#page=2", "kind": "page", "page": 2,
                 "text_preview": ""},
            ],
            2,
        )
        temporary, _, capsule, manifest, _ = self._run_arxiv(
            pdf, "application/pdf", extract_result=extracted
        )
        with temporary:
            self.assertEqual((manifest["status"], manifest["content_tier"]), ("partial", "full_text"))
            self.assertEqual(manifest["materialization"]["pdf_pages_without_extractable_text"], [2])
            self.assertEqual(manifest["materialization"]["selector_count"], 1)
            self.assertEqual(len((capsule / "selectors.jsonl").read_text().splitlines()), 1)
            self.assertIn("no OCR was performed", manifest["limitations"][0])

    def test_arxiv_empty_or_unparseable_pdf_is_not_full_text(self) -> None:
        for pdf in (minimal_pdf_pages([]), b"%PDF-1.4\ntruncated"):
            with self.subTest(bytes=len(pdf)):
                with contextlib.redirect_stderr(io.StringIO()):
                    temporary, _, capsule, manifest, _ = self._run_arxiv(pdf, "application/pdf")
                with temporary:
                    self.assertEqual((manifest["status"], manifest["content_tier"]), (
                        "partial", "metadata_capsule"
                    ))
                    self.assertEqual((capsule / "source/document.pdf").read_bytes(), pdf)
                    self.assertFalse((capsule / "selectors.jsonl").exists())

    def test_arxiv_page_extraction_failure_is_not_full_text(self) -> None:
        pdf = minimal_text_pdf()
        extracted = (
            "## Page 1\n\nReadable source evidence remains locally available.\n\n"
            "## Page 2\n\n[page extraction failed: fixture failure]\n",
            [
                {"selector": "pdf://sha256-PENDING#page=1", "kind": "page", "page": 1,
                 "text_preview": "Readable source evidence remains locally available."},
                {"selector": "pdf://sha256-PENDING#page=2", "kind": "page", "page": 2,
                 "text_preview": "[page extraction failed: fixture failure]"},
            ],
            2,
        )
        temporary, _, capsule, manifest, _ = self._run_arxiv(
            pdf, "application/pdf", extract_result=extracted
        )
        with temporary:
            self.assertEqual((manifest["status"], manifest["content_tier"]), (
                "partial", "excerpt_capsule"
            ))
            self.assertEqual(manifest["materialization"]["pdf_page_extraction_failures"], [2])
            self.assertEqual(len((capsule / "selectors.jsonl").read_text().splitlines()), 1)


class ValidatorIntegrityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.raw = self.root / "raw_data"
        self.corpus = self.root / "materialized_sources" / "corpus"
        self.index = self.root / "materialized_sources" / "index.yaml"
        self.registry = self.root / "source_registry" / "registry.yaml"
        self.audit = self.raw / "audits" / "materialization_completeness_2026-09-10.yaml"
        self.metadata_path = self.raw / "paper" / "example" / "metadata.yaml"
        self.capsule = self.corpus / "paper-example"
        self.metadata = {"uid": "paper:example", "title": "Example"}
        self.metadata_path.parent.mkdir(parents=True)
        self.capsule.mkdir(parents=True)
        self.metadata_path.write_text(yaml.safe_dump(self.metadata), encoding="utf-8")
        (self.capsule / "source-metadata.yaml").write_text(yaml.safe_dump(self.metadata), encoding="utf-8")
        (self.capsule / "README.md").write_text("# Example\n", encoding="utf-8")
        (self.capsule / "document.md").write_text("source evidence\n", encoding="utf-8")
        (self.capsule / "selectors.jsonl").write_text(
            '{"selector":"web://example#B1","local_path":"materialized_sources/corpus/paper-example/document.md","ordinal":1,"text_preview":"source evidence"}\n',
            encoding="utf-8",
        )
        self._write_consistent_artifacts()
        self.patch = mock.patch.multiple(
            validator,
            ROOT=self.root,
            RAW=self.raw,
            CORPUS=self.corpus,
            INDEX=self.index,
            REGISTRY=self.registry,
            AUDIT=self.audit,
        )
        self.patch.start()

    def tearDown(self) -> None:
        self.patch.stop()
        self.temporary.cleanup()

    def _write_yaml(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")

    def _write_consistent_artifacts(self) -> None:
        local_files = []
        for path in sorted(self.capsule.rglob("*")):
            if path.is_file() and path.name != "manifest.yaml":
                payload = path.read_bytes()
                local_files.append(
                    {
                        "path": path.relative_to(self.root).as_posix(),
                        "bytes": len(payload),
                        "sha256": hashlib.sha256(payload).hexdigest(),
                    }
                )
        local_bytes = sum(item["bytes"] for item in local_files)
        manifest = {
            "uid": "paper:example",
            "source_type": "paper",
            "metadata_path": self.metadata_path.relative_to(self.root).as_posix(),
            "status": "materialized",
            "content_tier": "full_text",
            "revision": "revision-1",
            "selectors": ["selectors.jsonl"],
            "materialization": {"selector_count": 1},
            "local_files": local_files,
            "local_bytes": local_bytes,
            "warnings": [],
            "errors": [],
        }
        self._write_yaml(self.capsule / "manifest.yaml", manifest)
        manifest_ref = (self.capsule / "manifest.yaml").relative_to(self.root).as_posix()
        self._write_yaml(
            self.index,
            {
                "items": [
                    {
                        "uid": "paper:example",
                        "manifest": manifest_ref,
                        "status": "materialized",
                        "content_tier": "full_text",
                        "revision": "revision-1",
                        "local_bytes": local_bytes,
                    }
                ]
            },
        )
        self._write_yaml(
            self.registry,
            {
                "entry_count": 1,
                "entries": [
                    {
                        "uid": "paper:example",
                        "metadata_path": self.metadata_path.relative_to(self.root).as_posix(),
                        "materialization": {
                            "manifest": manifest_ref,
                            "state": "materialized",
                            "content_tier": "full_text",
                            "evidence_role": "source-text",
                            "revision": "revision-1",
                            "local_bytes": local_bytes,
                        },
                    }
                ],
            },
        )
        self._write_yaml(
            self.audit,
            {
                "collection_records": 1,
                "local_capsules": 1,
                "all_records_local": True,
                "status_counts": {"materialized": 1},
                "content_tier_counts": {"full_text": 1},
                "metadata_only_count": 0,
                "partial_count": 0,
                "hashed_files": len(local_files),
                "acceptance": {
                    "all_metadata_records_have_local_manifest": True,
                    "no_unclassified_missing_capsule": True,
                    "full_content_gaps_are_explicit": True,
                },
            },
        )

    def _run_validator(self) -> tuple[int, str]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validator.main()
        return result, output.getvalue()

    def _configure_arxiv_pdf_fixture(self) -> Path:
        (self.capsule / "document.md").unlink()
        document = self.capsule / "document.txt"
        document.write_text(
            "## Page 1\n\nEvidence that belongs only to the first PDF page.\n\n"
            "## Page 2\n\nEvidence that belongs only to the second PDF page.\n",
            encoding="utf-8",
        )
        source_pdf = self.capsule / "source" / "document.pdf"
        source_pdf.parent.mkdir()
        source_pdf.write_bytes(minimal_pdf_pages(["First PDF page", "Second PDF page"]))
        pdf_hash = hashlib.sha256(source_pdf.read_bytes()).hexdigest()
        document_path = document.relative_to(self.root).as_posix()
        selectors = self.capsule / "selectors.jsonl"
        selectors.write_text(
            "\n".join(
                json.dumps(row)
                for row in (
                    {
                        "selector": f"pdf://sha256-{pdf_hash[:16]}#page=1",
                        "local_path": document_path,
                        "kind": "page",
                        "page": 1,
                        "text_preview": "Evidence that belongs only to the first PDF page.",
                    },
                    {
                        "selector": f"pdf://sha256-{pdf_hash[:16]}#page=2",
                        "local_path": document_path,
                        "kind": "page",
                        "page": 2,
                        "text_preview": "Evidence that belongs only to the second PDF page.",
                    },
                )
            ) + "\n",
            encoding="utf-8",
        )
        self._write_consistent_artifacts()

        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest.update(
            {
                "source_type": "arxiv",
                "adapter": "arxiv_pdf_v1",
                "archive_container": "pdf",
                "media_type": "application/pdf",
                "revision": f"sha256:{pdf_hash}",
                "retrievals": [{"sha256": pdf_hash}],
                "materialization": {
                    "document": "document.txt",
                    "source_pdf": "source/document.pdf",
                    "source_pdf_sha256": pdf_hash,
                    "selector_count": 2,
                    "pdf_page_count": 2,
                    "pdf_text_page_count": 2,
                    "pdf_pages_without_extractable_text": [],
                    "pdf_page_extraction_failures": [],
                    "substantive_text": True,
                },
            }
        )
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))
        index = yaml.safe_load(self.index.read_text())
        index["items"][0]["revision"] = f"sha256:{pdf_hash}"
        self._write_yaml(self.index, index)
        registry = yaml.safe_load(self.registry.read_text())
        registry["entries"][0]["materialization"]["revision"] = f"sha256:{pdf_hash}"
        self._write_yaml(self.registry, registry)
        return selectors

    def _configure_arxiv_image_transcription_fixture(self, *, extra_image_page: bool = False) -> Path:
        selectors = self._configure_arxiv_pdf_fixture()
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        (self.capsule / "document.txt").write_text(
            "## Page 1\n\nEvidence that belongs only to the first PDF page.\n\n## Page 2\n\n" + ("## Page 3\n\n" if extra_image_page else ""),
            encoding="utf-8",
        )
        source_pdf = self.capsule / "source/document.pdf"
        source_pdf.write_bytes(minimal_pdf_pages(["First PDF page", ""] + ([""] if extra_image_page else [])))
        pdf_hash = hashlib.sha256(source_pdf.read_bytes()).hexdigest()
        derived = self.capsule / "derived/image-pages-transcription.md"
        derived.parent.mkdir()
        derived.write_text(
            "## Image page 2\n\nVisible diagram labels.\n\n" + ("Visible page 3 labels.\n" if extra_image_page else "Other page 2 labels.\n"),
            encoding="utf-8",
        )
        rows = [json.loads(line) for line in selectors.read_text().splitlines()][:1]
        rows[0]["selector"] = f"pdf://sha256-{pdf_hash[:16]}#page=1"
        rows.append({
            "selector": "derived://example/image-pages#L1-L3",
            "local_path": derived.relative_to(self.root).as_posix(),
            "kind": "line_range", "source_page": 2, "start_line": 1, "end_line": 3,
            "text_preview": "Visible diagram labels.", "extraction_method": "agent_visual_transcription",
        })
        if extra_image_page:
            rows.append({
                "selector": "derived://example/image-pages#L5-L5", "local_path": derived.relative_to(self.root).as_posix(),
                "kind": "line_range", "source_page": 3, "start_line": 5, "end_line": 5,
                "text_preview": "Visible page 3 labels.", "extraction_method": "agent_visual_transcription",
            })
        selectors.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")
        self._write_consistent_artifacts()
        inventory = yaml.safe_load(manifest_path.read_text())
        manifest.update({
            "status": "partial", "revision": f"sha256:{pdf_hash}", "retrievals": [{"sha256": pdf_hash}],
            "local_files": inventory["local_files"], "local_bytes": inventory["local_bytes"],
            "warnings": ["Page 2 has no native text; visual transcription is an incomplete derived representation."],
        })
        manifest["materialization"].update({
            "source_pdf_sha256": pdf_hash, "pdf_text_page_count": 1,
            "pdf_page_count": 3 if extra_image_page else 2, "selector_count": len(rows),
            "pdf_pages_without_extractable_text": [2, 3] if extra_image_page else [2],
            "image_page_transcription": {
                "document": "derived/image-pages-transcription.md", "source_pages": [2, 3] if extra_image_page else [2],
                "method": "agent_visual_transcription", "renderer": "Poppler pdftoppm test fixture",
                "render_dpi": {2: 180, 3: 180} if extra_image_page else {2: 180}, "model_revision": "not_exposed",
                "native_text_extraction_changed": False, "conventional_ocr_performed": False,
                "complete_image_representation": False, "scope": "Visible diagram text only; not layout or plotted values.",
            },
        })
        self._write_yaml(manifest_path, manifest)
        index = yaml.safe_load(self.index.read_text())
        index["items"][0].update({"status": "partial", "revision": manifest["revision"], "local_bytes": manifest["local_bytes"]})
        self._write_yaml(self.index, index)
        registry = yaml.safe_load(self.registry.read_text())
        registry["entries"][0]["materialization"].update({
            "state": "partial", "evidence_role": "bounded-excerpt", "revision": manifest["revision"], "local_bytes": manifest["local_bytes"],
        })
        self._write_yaml(self.registry, registry)
        audit = yaml.safe_load(self.audit.read_text())
        audit.update({"status_counts": {"partial": 1}, "partial_count": 1})
        self._write_yaml(self.audit, audit)
        return selectors

    def test_valid_fixture_passes(self) -> None:
        result, output = self._run_validator()
        self.assertEqual(result, 0, output)

    def test_valid_arxiv_pdf_fixture_passes_page_binding(self) -> None:
        self._configure_arxiv_pdf_fixture()

        result, output = self._run_validator()

        self.assertEqual(result, 0, output)

    def test_declared_pdf_image_transcription_passes_without_changing_native_coverage(self) -> None:
        self._configure_arxiv_image_transcription_fixture()
        result, output = self._run_validator()
        self.assertEqual(result, 0, output)

    def test_declared_multi_page_image_transcription_passes(self) -> None:
        self._configure_arxiv_image_transcription_fixture(extra_image_page=True)
        result, output = self._run_validator()
        self.assertEqual(result, 0, output)

    def test_pdf_derived_selectors_require_an_explicit_complete_declaration(self) -> None:
        self._configure_arxiv_image_transcription_fixture()
        manifest_path = self.capsule / "manifest.yaml"
        original = yaml.safe_load(manifest_path.read_text())
        for field in (None, "renderer", "model_revision", "scope", "render_dpi", "native_text_extraction_changed", "conventional_ocr_performed", "complete_image_representation"):
            with self.subTest(missing_field=field):
                manifest = yaml.safe_load(yaml.safe_dump(original))
                if field is None:
                    del manifest["materialization"]["image_page_transcription"]
                else:
                    del manifest["materialization"]["image_page_transcription"][field]
                self._write_yaml(manifest_path, manifest)
                result, output = self._run_validator()
                self.assertEqual(result, 1)
                self.assertIn("ARXIV_PDF_NON_PAGE_SELECTOR", output)
                if field is not None:
                    self.assertIn("ARXIV_PDF_TRANSCRIPTION_PROVENANCE", output)

    def test_pdf_transcription_declared_source_pages_and_document_are_scoped(self) -> None:
        self._configure_arxiv_image_transcription_fixture()
        manifest_path = self.capsule / "manifest.yaml"
        original = yaml.safe_load(manifest_path.read_text())
        for field, value in (("source_pages", [1]), ("source_pages", [3]), ("source_pages", [True]), ("source_pages", [2, 2]), ("document", "document.txt"), ("document", "../outside.md"), ("document", "derived/missing.md"), ("method", "native_pdf_text"), ("render_dpi", {2: True}), ("conventional_ocr_performed", True)):
            with self.subTest(field=field, value=value):
                manifest = yaml.safe_load(yaml.safe_dump(original))
                manifest["materialization"]["image_page_transcription"][field] = value
                self._write_yaml(manifest_path, manifest)
                result, output = self._run_validator()
                self.assertEqual(result, 1)
                self.assertIn("ARXIV_PDF_TRANSCRIPTION_PROVENANCE", output)

    def test_pdf_transcription_selectors_require_legal_ranges_and_matching_provenance(self) -> None:
        selectors = self._configure_arxiv_image_transcription_fixture()
        original = [json.loads(line) for line in selectors.read_text().splitlines()]
        for field, value in (("source_page", 1), ("source_page", True), ("source_page", 3), ("kind", "file"), ("page", None), ("extraction_method", "native_pdf_text"), ("start_line", None), ("end_line", 100), ("selector", "derived://example/image-pages#L1-L5"), ("local_path", original[0]["local_path"])):
            with self.subTest(field=field, value=value):
                rows = [dict(row) for row in original]
                rows[1][field] = value
                selectors.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
                result, output = self._run_validator()
                self.assertEqual(result, 1)
                self.assertIn("ARXIV_PDF_TRANSCRIPTION_SELECTOR", output)
                self.assertIn("ARXIV_PDF_NON_PAGE_SELECTOR", output)

    def test_pdf_transcription_preview_must_resolve_inside_its_declared_range(self) -> None:
        selectors = self._configure_arxiv_image_transcription_fixture()
        rows = [json.loads(line) for line in selectors.read_text().splitlines()]
        rows[1]["text_preview"] = "Other page 2 labels."
        selectors.write_text("\n".join(json.dumps(row) for row in rows) + "\n")
        result, output = self._run_validator()
        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_TRANSCRIPTION_PREVIEW_RANGE", output)

    def test_pdf_transcription_declaration_requires_each_declared_source_page_to_have_selectors(self) -> None:
        selectors = self._configure_arxiv_image_transcription_fixture()
        selectors.write_text(selectors.read_text().splitlines()[0] + "\n")
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest["materialization"]["selector_count"] = 1
        self._write_yaml(manifest_path, manifest)
        result, output = self._run_validator()
        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_TRANSCRIPTION_PAGE_COVERAGE", output)

    def test_pdf_transcription_cannot_drop_one_of_multiple_declared_image_pages(self) -> None:
        selectors = self._configure_arxiv_image_transcription_fixture(extra_image_page=True)
        selectors.write_text("\n".join(selectors.read_text().splitlines()[:2]) + "\n")
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest["materialization"]["selector_count"] = 2
        self._write_yaml(manifest_path, manifest)
        result, output = self._run_validator()
        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_TRANSCRIPTION_PAGE_COVERAGE", output)
        self.assertIn("declared=[2, 3] actual=[2]", output)

    def test_pdf_transcription_does_not_replace_native_page_coverage_or_gap_honesty(self) -> None:
        selectors = self._configure_arxiv_image_transcription_fixture()
        selectors.write_text(selectors.read_text().splitlines()[1] + "\n")
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest["materialization"]["selector_count"] = 1
        self._write_yaml(manifest_path, manifest)
        result, output = self._run_validator()
        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_PAGE_COVERAGE", output)
        self.assertIn("ARXIV_PDF_TEXT_PAGE_COUNT", output)
        manifest["status"] = "materialized"
        self._write_yaml(manifest_path, manifest)
        result, output = self._run_validator()
        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_UNACKNOWLEDGED_TEXT_GAPS", output)

    def test_arxiv_pdf_selector_uri_page_must_match_page_field(self) -> None:
        selectors = self._configure_arxiv_pdf_fixture()
        rows = [json.loads(line) for line in selectors.read_text().splitlines()]
        rows[0]["selector"] = rows[0]["selector"].replace("page=1", "page=2")
        selectors.write_text("\n".join(json.dumps(row) for row in rows) + "\n")

        result, output = self._run_validator()

        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_SELECTOR_HASH_OR_PAGE", output)

    def test_arxiv_pdf_preview_must_resolve_inside_its_page(self) -> None:
        selectors = self._configure_arxiv_pdf_fixture()
        rows = [json.loads(line) for line in selectors.read_text().splitlines()]
        rows[0]["text_preview"] = "Evidence that belongs only to the second PDF page."
        selectors.write_text("\n".join(json.dumps(row) for row in rows) + "\n")

        result, output = self._run_validator()

        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_SELECTOR_PREVIEW_CROSS_PAGE", output)

    def test_arxiv_pdf_page_count_and_coverage_are_complete(self) -> None:
        selectors = self._configure_arxiv_pdf_fixture()
        selectors.write_text(selectors.read_text().splitlines()[0] + "\n")
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest["materialization"]["pdf_page_count"] = 1
        manifest["materialization"]["pdf_text_page_count"] = 1
        manifest["materialization"]["selector_count"] = 1
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))

        result, output = self._run_validator()

        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_PAGE_COUNT", output)
        self.assertIn("ARXIV_PDF_PAGE_COVERAGE", output)

    def test_unresolved_preview_and_unhashed_file_fail(self) -> None:
        selectors = self.capsule / "selectors.jsonl"
        selectors.write_text(
            selectors.read_text(encoding="utf-8").replace("source evidence", "missing evidence"),
            encoding="utf-8",
        )
        (self.capsule / "untracked.txt").write_text("not inventoried\n", encoding="utf-8")

        result, output = self._run_validator()

        self.assertEqual(result, 1)
        self.assertIn("SELECTOR_PREVIEW_UNRESOLVED", output)
        self.assertIn("UNHASHED_LOCAL_FILE", output)

    def test_pdf_bytes_disguised_as_arxiv_tex_fail(self) -> None:
        (self.capsule / "document.md").unlink()
        source = self.capsule / "source" / "main.tex"
        source.parent.mkdir()
        source.write_bytes(b"%PDF-1.4\nsource evidence\n")
        local_path = source.relative_to(self.root).as_posix()
        (self.capsule / "selectors.jsonl").write_text(
            json.dumps({
                "selector": "arxiv://example#L1-L2",
                "local_path": local_path,
                "start_line": 1,
                "end_line": 2,
                "text_preview": "%PDF-1.4",
            }) + "\n",
            encoding="utf-8",
        )
        self._write_consistent_artifacts()
        manifest_path = self.capsule / "manifest.yaml"
        manifest = yaml.safe_load(manifest_path.read_text())
        manifest.update({"source_type": "arxiv", "adapter": "arxiv_latex_v2", "archive_container": "single"})
        manifest_path.write_text(yaml.safe_dump(manifest, sort_keys=False))

        result, output = self._run_validator()

        self.assertEqual(result, 1)
        self.assertIn("ARXIV_PDF_AS_TEX", output)


if __name__ == "__main__":
    unittest.main()
