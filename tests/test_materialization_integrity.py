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
from dataclasses import replace
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


class RetainedMarkdownTests(unittest.TestCase):
    @contextlib.contextmanager
    def _dated_html_capsule(self, *, unretained: bool = False):
        with self._retained_capsule() as (root, record, _, _, asset, document):
            document.unlink()
            capsule = record.capsule_root
            (capsule / "document.md").write_bytes(b"# Historical excerpt\r\n\r\nOld bounded body and its original attribution.\r\n")
            materializer.write_jsonl(capsule / "selectors.jsonl", [{
                "selector": "historical://excerpt#L1-L3", "local_path": (capsule / "document.md").relative_to(root).as_posix(),
                "kind": "section", "start_line": 1, "end_line": 3, "text_preview": "Historical excerpt",
            }])
            old = materializer.load_yaml(capsule / "manifest.yaml")
            old.pop("source_version")
            old["content_tier"] = "excerpt_capsule"
            old["materialization"] = {"document": "document.md", "selector_count": 1}
            old["selectors"] = ["selectors.jsonl"]
            old["local_files"] = materializer.local_file_inventory(capsule)
            original = "\r\n".join([
                '<!DOCTYPE html><html><head><title>Dated specification</title></head><body>',
                '<div class="head"><h1 id="title">Fixed specification</h1><p>Author identity and copyright retained.</p>',
                '<img src="https://example.test/logo.svg" alt="UI_LOGO"><a class="orcid"><svg>UI_ORCID</svg>Author name</a></div>',
                '<nav id="toc">UI_TOC</nav><p id="back-to-top">UI_BACK_TOP</p><div class="dfn-panel">UI_DEFINITION_PANEL</div>',
                '<h2 id="status">Status of This Document</h2><p>This dated specification records a stable source boundary with explicit local evidence and reviewed attribution for readers.</p>',
                '<dl><dt>TERM_ONE</dt><dt>TERM_TWO</dt><dd>DEFINITION_ONE<dl><dt>NESTED_TERM</dt><dd>NESTED_DEFINITION</dd></dl></dd><dd>DEFINITION_TWO</dd></dl>',
                '<h2 id="figures">Figures</h2><figure><a href="figure.svg"><object data="figure.svg" type="image/svg+xml" aria-label="asserted graph"></object></a><figcaption>ASSERTED_CAPTION</figcaption></figure>',
                '<figure><object data="figure.svg" type="image/svg+xml" aria-describedby="figure-description"><p id="figure-description">FALLBACK_GRAPH_DESCRIPTION</p></object><figcaption>UNASSERTED_CAPTION and <a href="#annex">Annex description</a></figcaption></figure>',
                '<button>Compacted (Input)</button><button>Expanded (Result)</button>',
                '<pre class="header-value">Header value<br>&nbsp;&nbsp;continuation<br><span>final line</span></pre>',
                '<table><tr><th>PROPERTY</th><th>CONSTRAINT</th></tr><tr><td>authentication</td><td rowspan="5" colspan="2">SHARED_CONSTRAINT</td></tr><tr><td>assertionMethod</td></tr></table>',
                '<img src="figure.svg" alt="MULTILINE_ALT\nsecond line retains graph meaning">',
                '<pre>literal {ticker} and {% template %}\n\nThis hidden code example claims an impossible result without any source verification.\n# Fake heading</pre>',
                '<h2 id="annex">Annex A</h2><p>Detailed graph meaning remains part of the original specification body.</p>',
                '</body></html>', '',
            ]).encode()
            if unretained:
                original = original.replace(b'</body>', b'<figure><img src="./images/unlicensed-map.png" alt="Map extent"><figcaption>Original map credit and caption retained.</figcaption></figure></body>')
            source = capsule / "source/specification.html"
            source.write_bytes(original)
            revision = "sha256:" + hashlib.sha256(original).hexdigest()
            package = {**record.metadata["rights"]["redistribution_package"],
                "source_revision": revision, "modifications": "Declared UI removal and structural HTML text; original response unchanged.",
                "scope": "Dated HTML and explicitly retained scientific figure.",
            }
            record.metadata["full_text_url"] = package["source_version_url"]
            record.metadata["rights"]["redistribution_package"] = package
            materializer.write_yaml(record.metadata_path, record.metadata)
            materializer.write_yaml(capsule / "source-metadata.yaml", record.metadata)
            notice = b"Historical attribution remains complete.\n\nCurrent dated HTML grant and original rights links.\n"
            (root / "license.md").write_bytes(notice)
            (capsule / "NOTICE.md").write_bytes(notice)
            manifest = materializer.base_manifest(record, "generic_web_or_document_v2", "fixed-time")
            manifest.update({"status": "materialized", "content_tier": "full_text", "revision": revision, "source_version": "1.2", "historical_acquisition": old})
            manifest["rights"]["redistribution_package"] = package
            manifest["materialization"] = {
                "retained_text_binding": "dated_html_response", "document": "normalized/document.md", "normalized_document": "normalized/document.md",
                "retained_text_selectors": "normalized/selectors.jsonl",
                "retained_text_sources": [{"source": "source/specification.html", "format": "html", "exclude_selectors": ["nav#toc", "p#back-to-top", ".dfn-panel", ".head img", ".head a.orcid svg"]}],
                "link_rewrites": {"figure.svg": "../source/assets/img/figure.svg"},
            }
            if unretained:
                manifest["status"] = "partial"
                manifest["materialization"]["retained_text_sources"][0]["unretained_assets"] = ["./images/unlicensed-map.png"]
                manifest["limitations"] = ["Image basemap credit lacks a confirmed public persistence grant."]
            manifest["selectors"] = ["selectors.jsonl", "normalized/selectors.jsonl"]
            manifest["retrievals"] = [{
                "local_path": path.relative_to(capsule).as_posix(), "requested_url": url, "resolved_url": url,
                "sha256": materializer.sha256_file(path), "bytes": path.stat().st_size,
                "http_status": 200, "content_type": media, "retrieved_at": "fixed-acquisition-time",
            } for path, url, media in (
                (source, package["source_version_url"], "text/html; charset=utf-8"),
                (asset, package["source_version_url"] + "figure.svg", "image/svg+xml"),
            )]
            manifest["local_files"] = materializer.local_file_inventory(capsule)
            materializer.write_yaml(capsule / "manifest.yaml", manifest)
            audit = root / "raw_data/audits/materialization_rights_review.yaml"
            audit.parent.mkdir(parents=True)
            materializer.write_yaml(audit, {"items": [{
                "uid": record.uid, "manifest_path": (capsule / "manifest.yaml").relative_to(root).as_posix(), "source_revision": revision,
                "redistribution_package": package, "publication_gate": {"decision": "allow"},
            }]})
            yield root, record, source, asset, document, manifest

    def test_dated_html_explicit_unretained_figure_is_a_link_not_an_image(self) -> None:
        with self._dated_html_capsule(unretained=True) as (root, record, source, _, document, manifest), mock.patch.object(materializer, "fetch_bytes", side_effect=AssertionError("explicit unretained figures must not be fetched")), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("dated replay must retain the legacy capsule")):
            original = source.read_bytes()
            materializer.replay_retained_text_sources(record, manifest, "fixed-time", check_derived=False)
            result = materializer.materialize_one(record, {}, "fixed-time")
            before = {path.relative_to(record.capsule_root): path.read_bytes() for path in record.capsule_root.rglob("*") if path.is_file()}
            materializer.materialize_one(record, {}, "fixed-time")
            self.assertEqual({path.relative_to(record.capsule_root): path.read_bytes() for path in record.capsule_root.rglob("*") if path.is_file()}, before)
            text = document.read_bytes().decode()
            self.assertEqual(result["status"], "partial")
            self.assertIn("[Original figure not retained locally: Map extent](https://example.test/specification/1.2/images/unlicensed-map.png)", text)
            self.assertIn("Original map credit and caption retained.", text)
            self.assertIn("> Collector asset gap:", text)
            self.assertNotIn("![Map extent]", text)
            self.assertFalse(list(record.capsule_root.rglob("*.png")))
            self.assertEqual(source.read_bytes(), original)
            errors: list[str] = []
            validator.validate_retained_markdown_binding(result, record.capsule_root, {source.relative_to(root).as_posix(): materializer.sha256_file(source)}, errors, repository_root=root)
            self.assertEqual(errors, [])

    def test_dated_html_unretained_assets_do_not_relax_other_originals(self) -> None:
        for change in ("absent", "both-routes", "wrong-type", "complete-status", "undeclared", "other-asset-missing"):
            with self.subTest(change=change), self._dated_html_capsule(unretained=True) as (root, record, source, asset, _, manifest):
                item = manifest["materialization"]["retained_text_sources"][0]
                if change == "absent":
                    item["unretained_assets"] = ["./images/not-in-dom.png"]
                elif change == "both-routes":
                    manifest["materialization"]["link_rewrites"]["./images/unlicensed-map.png"] = "../source/assets/img/figure.svg"
                elif change == "wrong-type":
                    item["unretained_assets"] = "./images/unlicensed-map.png"
                elif change == "complete-status":
                    manifest["status"] = "materialized"
                elif change == "undeclared":
                    del item["unretained_assets"]
                else:
                    asset.unlink()
                materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
                before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                with mock.patch.object(materializer, "fetch_bytes") as fetch, mock.patch.object(materializer, "prepare_capsule") as prepare, mock.patch.object(materializer, "finalize_capsule") as finalize:
                    with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                        materializer.materialize_one(record, {}, "fixed-time")
                    fetch.assert_not_called()
                    prepare.assert_not_called()
                    finalize.assert_not_called()
                self.assertEqual({path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}, before)

    def test_dated_html_first_build_and_two_offline_replays_preserve_legacy_bytes(self) -> None:
        with self._dated_html_capsule() as (root, record, source, asset, document, manifest), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("dated HTML replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("dated HTML replay must not clear originals")):
            preserved = {path: path.read_bytes() for path in (source, asset, record.capsule_root / "document.md", record.capsule_root / "selectors.jsonl")}
            materializer.replay_retained_text_sources(record, manifest, "fixed-time", check_derived=False)
            first = {path.relative_to(record.capsule_root): path.read_bytes() for path in record.capsule_root.rglob("*") if path.is_file()}
            for executor in (materializer.materialize_generic, materializer.materialize_one):
                replayed = executor(record, {}, "fixed-time")
                self.assertEqual({path.relative_to(record.capsule_root): path.read_bytes() for path in record.capsule_root.rglob("*") if path.is_file()}, first)
                self.assertNotIn("source_version", replayed["historical_acquisition"])
                self.assertEqual(replayed["historical_acquisition"], manifest["historical_acquisition"])
                rows = [json.loads(line) for line in (record.capsule_root / "normalized/selectors.jsonl").read_text().splitlines()]
                self.assertEqual(replayed["materialization"]["selector_count"], 1 + len(rows))
                errors: list[str] = []
                validator.validate_retained_markdown_binding(replayed, record.capsule_root, {source.relative_to(root).as_posix(): materializer.sha256_file(source)}, errors, repository_root=root)
                self.assertEqual(errors, [])
            self.assertEqual({path: path.read_bytes() for path in preserved}, preserved)
            text = document.read_bytes().decode()
            for token in ("Author identity and copyright retained.", "Author name", "Status of This Document", "Compacted (Input)", "Expanded (Result)", "Annex A", "FALLBACK_GRAPH_DESCRIPTION", "UNASSERTED_CAPTION"):
                self.assertEqual(text.count(token), 1)
            self.assertEqual(text.count("\nASSERTED_CAPTION\n"), 1)
            for token in ("UI_TOC", "UI_BACK_TOP", "UI_DEFINITION_PANEL", "UI_LOGO", "UI_ORCID"):
                self.assertNotIn(token, text)
            terms = ("TERM_ONE", "TERM_TWO", "DEFINITION_ONE", "NESTED_TERM", "NESTED_DEFINITION", "DEFINITION_TWO")
            self.assertEqual([text.index(token) for token in terms], sorted(text.index(token) for token in terms))
            for token in terms:
                self.assertIn("\n\n" + token, text)
            self.assertIn("![asserted graph](../source/assets/img/figure.svg)", text)
            self.assertIn("![figure.svg](../source/assets/img/figure.svg)", text)
            self.assertIn("[Enclosing object link](../source/assets/img/figure.svg)", text)
            self.assertIn("[aria-describedby: figure-description](#specification-figure-description)", text)
            self.assertIn("[Annex description](#specification-annex)", text)
            self.assertIn("literal {ticker} and {% template %}\n\nThis hidden code", text)
            self.assertIn("```\nHeader value\n\u00a0\u00a0continuation\nfinal line\n```", text)
            self.assertIn("- authentication | SHARED_CONSTRAINT [rowspan=5] [colspan=2]", text)
            self.assertIn("- assertionMethod", text)
            self.assertIn("![MULTILINE_ALT second line retains graph meaning](../source/assets/img/figure.svg)", text)
            self.assertNotIn("snapshot_commit", record.metadata["versioning"])

    def test_dated_html_failed_preflight_preserves_all_bytes_through_wrapper_and_executor(self) -> None:
        changes = ("version", "metadata-version-type", "cached-package", "url", "requested-url", "resolved-url", "main-hash", "asset-drift", "missing-main", "missing-asset", "notice", "package", "audit", "exclude", "binding-type", "materialization-type", "missing-main-bad-mapping", "declaration", "legacy-drift")
        for change in changes:
            with self.subTest(change=change), self._dated_html_capsule() as (root, record, source, asset, _, manifest):
                materializer.replay_retained_text_sources(record, manifest, "fixed-time", check_derived=False)
                manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
                if change == "version":
                    manifest["source_version"] = "1.3"
                elif change == "metadata-version-type":
                    record.metadata["versioning"] = 7
                elif change == "cached-package":
                    record.metadata["rights"]["redistribution_package"]["scope"] = "Cached but unreviewed grant"
                elif change == "url":
                    record.metadata["full_text_url"] = "https://example.test/specification/latest/"
                    materializer.write_yaml(record.metadata_path, record.metadata)
                elif change in {"requested-url", "resolved-url"}:
                    manifest["retrievals"][0][change.replace("-", "_")] += "wrong/"
                elif change == "main-hash":
                    manifest["retrievals"][0]["sha256"] = "stale"
                elif change == "asset-drift":
                    asset.write_bytes(asset.read_bytes() + b"Drift")
                elif change in {"missing-main", "missing-asset"}:
                    (source if change == "missing-main" else asset).unlink()
                elif change == "notice":
                    (record.capsule_root / "NOTICE.md").write_bytes(b"Truncated notice")
                elif change == "package":
                    manifest["rights"]["redistribution_package"]["scope"] = "Unreviewed grant"
                elif change == "audit":
                    audit = root / "raw_data/audits/materialization_rights_review.yaml"
                    value = materializer.load_yaml(audit)
                    value["items"][0]["redistribution_package"]["scope"] = "Unreviewed grant"
                    materializer.write_yaml(audit, value)
                elif change == "exclude":
                    manifest["materialization"]["retained_text_sources"][0]["exclude_selectors"] = ["body"]
                elif change == "binding-type":
                    manifest["materialization"]["retained_text_binding"] = 7
                elif change == "materialization-type":
                    manifest["materialization"] = 7
                elif change == "missing-main-bad-mapping":
                    source.unlink()
                    manifest["materialization"] = 7
                elif change == "declaration":
                    del manifest["materialization"]["retained_text_sources"]
                else:
                    (record.capsule_root / "document.md").write_bytes(b"Changed historical body")
                materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
                before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                with mock.patch.object(materializer, "fetch_bytes") as fetch, mock.patch.object(materializer, "prepare_capsule") as prepare, mock.patch.object(materializer, "finalize_capsule") as finalize:
                    for executor in (materializer.materialize_generic, materializer.materialize_one):
                        with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                            executor(record, {}, "fixed-time")
                        self.assertEqual({path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}, before)
                    fetch.assert_not_called()
                    prepare.assert_not_called()
                    finalize.assert_not_called()

    def test_dated_html_skip_absent_derivatives_is_not_a_wrapper_fallback(self) -> None:
        for change in ("missing-sidecar", "wrong-pair", "invalid-selector", "absent-exclusion", "not-opted-in"):
            with self.subTest(change=change), self._dated_html_capsule() as (root, record, source, _, _, manifest):
                materializer.replay_retained_text_sources(record, manifest, "fixed-time", check_derived=False)
                manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
                sidecar = record.capsule_root / "normalized/selectors.jsonl"
                if change == "missing-sidecar":
                    sidecar.unlink()
                elif change == "wrong-pair":
                    manifest["materialization"]["retained_text_selectors"] = "selectors.jsonl"
                elif change == "invalid-selector":
                    rows = [json.loads(line) for line in sidecar.read_text().splitlines()]
                    rows[0]["derived_from"] = "imaginary/source.html"
                    materializer.write_jsonl(sidecar, rows)
                elif change == "absent-exclusion":
                    # Supported syntax still has to match the actual original.
                    source.write_bytes(source.read_bytes().replace(b'id="toc"', b'id="other-nav"'))
                    with self.assertRaisesRegex(ValueError, "declared HTML exclusion is absent"):
                        materializer.retained_html_body(source.read_bytes().decode(), dated_html_response=True, exclude_selectors=["nav#toc"])
                else:
                    del manifest["materialization"]["retained_text_binding"]
                    del manifest["materialization"]["retained_text_selectors"]
                materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
                before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                errors: list[str] = []
                validator.validate_retained_markdown_binding(manifest, record.capsule_root, {source.relative_to(root).as_posix(): materializer.sha256_file(source)}, errors, repository_root=root, check_derived=False)
                self.assertTrue(errors)
                with mock.patch.object(materializer, "fetch_bytes") as fetch, mock.patch.object(materializer, "prepare_capsule") as prepare, mock.patch.object(materializer, "finalize_capsule") as finalize:
                    with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                        materializer.materialize_one(record, {}, "fixed-time")
                    fetch.assert_not_called()
                    prepare.assert_not_called()
                    finalize.assert_not_called()
                self.assertEqual({path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}, before)

    def test_dated_html_sidecar_declaration_preserves_capsule_without_physical_sentinels(self) -> None:
        with self._dated_html_capsule() as (root, record, source, _, _, manifest):
            materializer.replay_retained_text_sources(record, manifest, "fixed-time", check_derived=False)
            manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
            source.unlink()
            (record.capsule_root / "normalized/selectors.jsonl").unlink()
            manifest["materialization"] = 7
            self.assertEqual(manifest["selectors"], ["selectors.jsonl", "normalized/selectors.jsonl"])
            materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
            before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
            with mock.patch.object(materializer, "fetch_bytes") as fetch, mock.patch.object(materializer, "prepare_capsule") as prepare, mock.patch.object(materializer, "finalize_capsule") as finalize:
                for executor in (materializer.materialize_generic, materializer.materialize_one):
                    with self.subTest(executor=executor.__name__), self.assertRaisesRegex(materializer.RetainedMarkdownPreflightError, "materialization must be a mapping"):
                        executor(record, {}, "fixed-time")
                    self.assertEqual({path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}, before)
                fetch.assert_not_called()
                prepare.assert_not_called()
                finalize.assert_not_called()

    def test_ordinary_unknown_source_without_dated_declaration_keeps_generic_fallback(self) -> None:
        with self._retained_capsule() as (_, record, _, _, _, _):
            manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
            manifest["materialization"] = 7
            manifest["selectors"] = ["selectors.jsonl"]
            materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
            ordinary = replace(record, source_type="unknown", canonical_url=None, metadata={})
            with mock.patch.object(materializer, "fetch_bytes") as fetch, mock.patch.object(materializer, "prepare_capsule", return_value=record.capsule_root) as prepare, mock.patch.object(materializer, "finalize_capsule", side_effect=lambda _record, _root, current: current) as finalize:
                result = materializer.materialize_generic(ordinary, {}, "fixed-time")
                self.assertIn("no retrievable URL in metadata", result["errors"])
                prepare.assert_called_once_with(ordinary)
                finalize.assert_called_once()
                fetch.assert_not_called()

    def test_dated_html_table_cell_pre_has_standalone_fences_and_is_not_excerpted(self) -> None:
        code = "NAME\tVALUE\n# Fake code heading\n\n## Abstract\n\nThis code comment falsely guarantees perfect answers for every possible question without any additional validation.\n{% template %} {ticker}  \n"
        last_code = 'owl:onDatatype xsd:string ;\n  xsd:pattern "--(0[1-9]|1[0-9]|20)"^^xsd:string ;  '
        actual = "This actual specification defines a bounded source method whose explicit restrictions and local evidence remain available for independent review by readers."
        original = (
            '<html><body><h2>Introduction</h2><table><tr><td>TABLE_LABEL</td><td></td>'
            '<td rowspan="5" colspan="2">TEXT_BEFORE<pre>' + code + '</pre>TEXT_AFTER</td><td>FINAL_CELL</td></tr>'
            '<tr><td>Subclass of:</td><td><pre><code>' + last_code + '</code></pre></td></tr></table>'
            '<h2>Current body</h2><p>' + actual + '</p></body></html>\n'
        ).encode()
        with tempfile.TemporaryDirectory() as directory, mock.patch.object(materializer, "ROOT", Path(directory)):
            root = Path(directory)
            source = root / "capsule/source/specification.html"
            source.parent.mkdir(parents=True)
            source.write_bytes(original)
            document = root / "capsule/normalized/document.md"
            rows = materializer.derive_retained_text_sources([(source, "html")], document, {}, source_options={source.resolve(): {"dated_html_response": True}})
            text = document.read_bytes().decode()
            self.assertIn("\n```\n" + code + "```\n", text)
            self.assertIn("\n```\n" + last_code + "\n```\n", text)
            self.assertIn("> Collector cell 2 of 4: (empty)", text)
            self.assertIn("> Collector cell span: [rowspan=5] [colspan=2]\n\nTEXT_BEFORE", text)
            ordered = ("TABLE_LABEL", "> Collector cell 2 of 4: (empty)", "TEXT_BEFORE", code, "TEXT_AFTER", "FINAL_CELL", "Subclass of:", last_code)
            self.assertEqual([text.index(value) for value in ordered], sorted(text.index(value) for value in ordered))
            self.assertEqual(text.count("> Collector table row:"), 2)
            headings = materializer.extract_markdown_headings(text, "document.md", structured=True)
            self.assertNotIn("Abstract", [row["heading"] for row in headings])
            self.assertNotIn("Fake code heading", [row["heading"] for row in headings])
            pipeline = REPOSITORY_ROOT / "experiments/v0_meta_kb_initialization_demo_260910/pipeline"
            with mock.patch.object(sys, "path", [str(pipeline), *sys.path]):
                from build_demo import source_excerpt
            excerpt, first, last = source_excerpt(text, "Specification", reading_view=True)
            self.assertEqual(excerpt, actual)
            self.assertIn(excerpt, "\n".join(text.splitlines()[first - 1:last]))
            for row in rows:
                self.assertIn(row["text_preview"], "\n".join(text.splitlines()[row["start_line"] - 1:row["end_line"]]))
            legacy = root / "capsule/normalized/legacy.md"
            materializer.derive_retained_text_sources([(source, "html")], legacy, {})
            self.assertIn("- TABLE_LABEL |  | TEXT_BEFORE", legacy.read_bytes().decode())
            self.assertNotIn("> Collector table row:", legacy.read_bytes().decode())
            self.assertEqual(source.read_bytes(), original)

    def test_structured_headings_recognize_setext_atx_and_ignore_fenced_examples(self) -> None:
        text = "\n".join([
            "Document title", "==============", "", "Section name", "------------",
            "   ### Actual ATX ###", "``` {.json}", "# example not a heading",
            "Example Setext", "--------------", "``", "## still example", "~~~~", "```",
            "~~~ {.text}", "### tilde example", "Tilde Setext", "============", "~~~",
            "    # indented example", "    Indented Setext", "    ----", "## Final ATX",
        ])
        headings = materializer.extract_markdown_headings(text, "document.md", structured=True)
        self.assertEqual([(row["line"], row["level"], row["heading"]) for row in headings], [
            (1, 1, "Document title"), (4, 2, "Section name"), (6, 3, "Actual ATX"), (23, 2, "Final ATX"),
        ])

    def test_default_headings_preserve_legacy_github_output(self) -> None:
        text = "Title\n=====\n   ### Indented\n```\n# Example\n```\n## Actual ##\n"
        self.assertEqual(materializer.extract_markdown_headings(text, "README.md"), [
            {"path": "README.md", "line": 5, "level": 1, "heading": "Example"},
            {"path": "README.md", "line": 7, "level": 2, "heading": "Actual ##"},
        ])

    def test_pandoc_simple_table_border_is_not_a_setext_heading(self) -> None:
        text = "\n".join([
            "Document title", "==============", "", "  -----------------------",
            "  Name      Media type", "  --------  ------------", "  First     text/plain",
            "", "  Last      text/turtle", "  -----------------------", "", "### After table",
        ])
        headings = materializer.extract_markdown_headings(text, "document.md", structured=True)
        self.assertEqual([(row["line"], row["heading"]) for row in headings], [(1, "Document title"), (12, "After table")])

    def test_derivation_rewrites_only_four_img_paths_and_preserves_source_and_line_endings(self) -> None:
        names = ("crate1-folders.svg", "introduction-figure-1.png", "introduction-figure-2.png", "ro-crate-preview-example.png")
        rewrites = {f"../../assets/img/{name}": f"../source/assets/img/{name}" for name in names}
        lines = [
            "<!-- Preamble remains -->", "", "Native title", "============", "",
            "### Example {#example}", "``` {.json}", "# not a heading",
            '"literal\\nnewline": "unchanged 中文"', "```", "",
            *[f'`<img src="../../assets/img/{name}" alt="Reference {index}" />`{{=html}}' for index, name in enumerate(names)],
            "[External link unchanged](https://example.test/doc#title)",
            "[Asset link unchanged](../../assets/img/crate1-folders.svg)",
            '<img data-src="../../assets/img/crate1-folders.svg" src="unmapped.png" />',
            "## End", "Last real paragraph without a final newline.",
        ]
        original = "\r\n".join(lines).encode("utf-8")
        expected = original
        for old, new in rewrites.items():
            expected = expected.replace(f'<img src="{old}"'.encode(), f'<img src="{new}"'.encode())
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(materializer, "ROOT", Path(temporary)):
            root = Path(temporary)
            source = root / "capsule/source/specification/1.2/document.md"
            document = root / "capsule/normalized/document.md"
            source.parent.mkdir(parents=True)
            source.write_bytes(original)
            rows = materializer.derive_retained_markdown(source, document, rewrites)
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(document.read_bytes(), expected)
            self.assertEqual([(row["start_line"], row["end_line"]) for row in rows], [(1, 5), (6, 18), (19, 20)])
            for row in rows:
                self.assertEqual(root / row["local_path"], document)
                cited = "\n".join(expected.decode().splitlines()[row["start_line"] - 1:row["end_line"]])
                self.assertIn(row["text_preview"], cited)
                self.assertEqual(row["selector"], f"derived://{row['local_path']}#L{row['start_line']}-L{row['end_line']}")
            filtered, omitted = materializer.filter_selectors_for_document(rows, expected.decode())
            self.assertEqual((filtered, omitted), (rows, 0))
            with self.assertRaises(ValueError):
                materializer.derive_retained_markdown(source, source, rewrites)
            self.assertEqual(source.read_bytes(), original)

    @contextlib.contextmanager
    def _retained_capsule(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with mock.patch.multiple(materializer, ROOT=root, CORPUS_ROOT=root / "materialized_sources/corpus"):
                original = b'Native title\n============\n\n<img src="../../assets/img/figure.svg" alt="Figure" />\n\n## Final section\nActual retained body.\n'
                revision = "sha256:" + hashlib.sha256(original).hexdigest()
                package = {
                    "source_revision": revision, "source_version_url": "https://example.test/specification/1.2/",
                    "notice_path": "license.md", "attribution": "Copyright specification author.",
                    "modifications": "Rebased explicitly retained image paths.", "scope": "Specification Markdown and assets.",
                }
                metadata = {
                    "uid": "standard:example-1.2", "title": "Example specification",
                    "url": package["source_version_url"], "versioning": {"source_version": "1.2"},
                    "rights": {"access": "open", "redistribution_package": package},
                }
                record = materializer.SourceRecord(
                    uid=metadata["uid"], source_type="standard", canonical_id="example-1.2", title=metadata["title"],
                    canonical_url=metadata["url"], metadata_path=root / "metadata.yaml", metadata=metadata,
                    priority="P0", rights_access="open",
                )
                source = record.capsule_root / "source/specification/1.2/document.md"
                source.parent.mkdir(parents=True)
                source.write_bytes(original)
                html = source.with_suffix(".html")
                html.write_bytes(b"<html>Complete retained HTML snapshot.</html>\n")
                asset = record.capsule_root / "source/assets/img/figure.svg"
                asset.parent.mkdir(parents=True)
                asset.write_bytes(b"<svg>Retained figure</svg>\n")
                document = record.capsule_root / "normalized/document.md"
                document.parent.mkdir()
                document.write_text("Previous consumer document.\n", encoding="utf-8")
                (root / "license.md").write_text("Complete test license.\n", encoding="utf-8")
                materializer.write_yaml(record.metadata_path, metadata)
                materializer.write_yaml(record.capsule_root / "source-metadata.yaml", metadata)
                manifest = materializer.base_manifest(record, "generic_web_or_document_v2", "fixed-time")
                manifest.update({"status": "materialized", "content_tier": "full_text", "revision": revision, "source_version": "1.2"})
                manifest["materialization"] = {
                    "retained_markdown_source": "source/specification/1.2/document.md", "document": "normalized/document.md",
                    "retained_html_source": "source/specification/1.2/document.html",
                    "asset_rewrites": {"../../assets/img/figure.svg": "../source/assets/img/figure.svg"},
                }
                manifest["retrievals"] = [{
                    "local_path": "source/specification/1.2/document.md",
                    "sha256": revision.removeprefix("sha256:"), "bytes": len(original),
                }]
                manifest["local_files"] = materializer.local_file_inventory(record.capsule_root)
                manifest["local_bytes"] = sum(item["bytes"] for item in manifest["local_files"])
                materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
                yield root, record, source, html, asset, document

    def test_generic_replays_fixed_snapshot_offline_and_restores_notice(self) -> None:
        with self._retained_capsule() as (_, record, source, html, asset, document), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("snapshot replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("snapshot replay must not clear originals")):
            originals = {path: path.read_bytes() for path in (source, html, asset)}
            for _ in range(2):
                manifest = materializer.materialize_one(record, {}, "fixed-time")
                text = document.read_text(encoding="utf-8")
                self.assertEqual(text.count("<!-- materialization-redistribution-notice -->"), 1)
                self.assertTrue(text.endswith(materializer.redistribution_footer(record.metadata["rights"]["redistribution_package"], "../NOTICE.md")))
                self.assertEqual(manifest["materialization"]["selector_count"], 2)
                readme = (record.capsule_root / "README.md").read_text(encoding="utf-8")
                for target in ("normalized/document.md", "source/specification/1.2/document.md", "source/specification/1.2/document.html"):
                    self.assertIn(f"]({target})", readme)
                for path, payload in originals.items():
                    self.assertEqual(path.read_bytes(), payload)

    def test_replay_rejects_changed_version_or_identity_without_touching_retained_files(self) -> None:
        with self._retained_capsule() as (_, record, source, html, asset, document), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("failed replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("failed replay must not clear originals")):
            before = {path: path.read_bytes() for path in (source, html, asset, document, record.capsule_root / "manifest.yaml")}
            changed_records = (
                replace(record, metadata={**record.metadata, "versioning": {"source_version": "1.3"}}),
                replace(record, canonical_url="https://example.test/specification/1.3/"),
            )
            for changed in changed_records:
                with self.subTest(version=changed.metadata["versioning"], canonical_url=changed.canonical_url):
                    with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                        materializer.materialize_one(changed, {}, "fixed-time")
                    for path, payload in before.items():
                        self.assertEqual(path.read_bytes(), payload)

    def test_replay_rejects_source_drift_before_changing_any_derived_file(self) -> None:
        with self._retained_capsule() as (_, record, source, html, asset, document), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("drifted replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("drifted replay must not clear originals")):
            source.write_bytes(source.read_bytes() + b"External source drift.\n")
            before = {path: path.read_bytes() for path in (source, html, asset, document, record.capsule_root / "manifest.yaml")}
            with self.assertRaisesRegex(materializer.RetainedMarkdownPreflightError, "RETAINED_MARKDOWN_REVISION"):
                materializer.materialize_one(record, {}, "fixed-time")
            for path, payload in before.items():
                self.assertEqual(path.read_bytes(), payload)

    def test_source_binding_rejects_stale_revision_or_retrieval_even_with_updated_inventory(self) -> None:
        with self._retained_capsule() as (root, record, source, _, _, _):
            original_manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
            actual = {source.relative_to(root).as_posix(): materializer.sha256_file(source)}
            for field in ("revision", "retrievals"):
                manifest = dict(original_manifest)
                if field == "revision":
                    manifest[field] = "sha256:stale"
                else:
                    manifest[field] = [{**manifest[field][0], "sha256": "stale"}]
                errors: list[str] = []
                validator.validate_retained_markdown_binding(manifest, record.capsule_root, actual, errors, repository_root=root)
                self.assertTrue(any(f"RETAINED_MARKDOWN_{'REVISION' if field == 'revision' else 'RETRIEVAL'}" in error for error in errors))

    @contextlib.contextmanager
    def _retained_text_capsule(self):
        with self._retained_capsule() as (root, record, _, _, _, document):
            commit = "a" * 40
            record.metadata["versioning"]["snapshot_commit"] = commit
            record.metadata["rights"]["redistribution_package"]["source_revision"] = f"git:{commit}"
            record.metadata["rights"]["redistribution_package"]["modifications"] = "Collector assembly and explicit local href rewrites."
            materializer.write_yaml(record.metadata_path, record.metadata)
            materializer.write_yaml(record.capsule_root / "source-metadata.yaml", record.metadata)
            names = ("spec-intro", "spec-model", "chaining-rules", "spec-formats", "spec-formats-tsv", "spec-formats-owl", "spec-formats-json")
            intro = "\r\n".join([
                "Shared title", "============", "", "[Model](spec-model.md)",
                "`[Inline](spec-model.md)` and ``[Wide](spec-model.md)``",
                "`[Multiline](spec-model.md)", "still code`",
                "[External](https://example.test/spec-model.md)", "```tsv", "# Fake heading",
                "subject\tobject", "[Fenced](spec-model.md)", "```", "## Details", "[Own](#details)", "",
            ]).encode("utf-8")
            originals: dict[Path, bytes] = {}
            sources: list[tuple[Path, str]] = []
            for name in names:
                source = record.capsule_root / f"source/src/docs/{name}.md"
                source.parent.mkdir(parents=True, exist_ok=True)
                body = intro if name == "spec-intro" else (
                    f"# Shared title\n\n{name} retained normative body.\n\n## Details\n"
                    "[Class](Mapping.md), [Mapping slots](Mapping.md#slots), [Set slots](MappingSet.md#slots).\n"
                ).encode("utf-8")
                source.write_bytes(body)
                originals[source] = body
                sources.append((source, "md"))
            schema = record.capsule_root / "source/src/sssom_schema/schema/sssom_schema.yaml"
            schema.parent.mkdir(parents=True)
            schema.write_bytes(b"classes:\n  mapping:\n    slots:\n    - subject_id\n    - object_id\n# YAML comment is not a Markdown heading\n")
            originals[schema] = schema.read_bytes()
            sources.append((schema, "yaml"))
            evidence: list[Path] = []
            for name in ("Mapping", "MappingSet"):
                html = record.capsule_root / f"source/rendered/1.0/{name}.html"
                html.parent.mkdir(parents=True, exist_ok=True)
                html.write_bytes(f'<html><table id="slots"><tr><td>{name} original Slots order</td></tr></table></html>\n'.encode())
                originals[html] = html.read_bytes()
                evidence.append(html)
            manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
            manifest["revision"] = f"git:{commit}"
            manifest["materialization"] = {
                "document": "normalized/document.md",
                "retained_text_sources": [{"source": path.relative_to(record.capsule_root).as_posix(), "format": format_name} for path, format_name in sources],
                "link_rewrites": {
                    "spec-model.md": "#spec-model-L1", "#details": "#spec-intro-L14",
                    "Mapping.md": "../source/src/sssom_schema/schema/sssom_schema.yaml#L2-L6",
                    "Mapping.md#slots": "../source/rendered/1.0/Mapping.html#slots",
                    "MappingSet.md#slots": "../source/rendered/1.0/MappingSet.html#slots",
                },
            }
            manifest["retrievals"] = [{
                "local_path": path.relative_to(record.capsule_root).as_posix(),
                "sha256": materializer.sha256_file(path), "bytes": path.stat().st_size,
                **({"commit": commit} if path not in evidence else {}),
            } for path in originals]
            manifest["local_files"] = materializer.local_file_inventory(record.capsule_root)
            manifest["local_bytes"] = sum(item["bytes"] for item in manifest["local_files"])
            materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
            yield root, record, sources, originals, document

    def test_ordered_text_replay_is_offline_complete_and_preserves_code_and_origins(self) -> None:
        with self._retained_text_capsule() as (root, record, sources, originals, document), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("assembly replay must not fetch"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("assembly replay must not clear originals")):
            previous = None
            for _ in range(2):
                manifest = materializer.materialize_one(record, {}, "fixed-time")
                text = document.read_bytes().decode("utf-8")
                selectors = [json.loads(line) for line in (record.capsule_root / "selectors.jsonl").read_text().splitlines()]
                self.assertEqual(len(selectors), 15)
                self.assertIn("[Model](#spec-model-L1)", text)
                self.assertIn("[Own](#spec-intro-L14)", text)
                for code in ("`[Inline](spec-model.md)`", "``[Wide](spec-model.md)``", "`[Multiline](spec-model.md)\r\nstill code`", "```tsv\r\n# Fake heading\r\nsubject\tobject\r\n[Fenced](spec-model.md)\r\n```"):
                    self.assertIn(code, text)
                self.assertIn("[External](https://example.test/spec-model.md)", text)
                self.assertNotIn('id="spec-intro-L10"', text)
                self.assertIn("```yaml\n" + originals[sources[-1][0]].decode("utf-8") + "```\n", text)
                for source, format_name in sources:
                    rows = [row for row in selectors if root / row["derived_from"] == source]
                    self.assertEqual(rows[0]["source_start_line"], 1)
                    self.assertEqual(rows[-1]["source_end_line"], len(originals[source].decode().splitlines()))
                    for left, right in zip(rows, rows[1:]):
                        self.assertEqual(left["source_end_line"] + 1, right["source_start_line"])
                    for row in rows:
                        self.assertEqual(row["source_format"], format_name)
                        self.assertEqual(root / row["local_path"], document)
                        self.assertIn(row["text_preview"], "\n".join(text.splitlines()[row["start_line"] - 1:row["end_line"]]))
                self.assertEqual(text.count("<!-- materialization-redistribution-notice -->"), 1)
                readme = (record.capsule_root / "README.md").read_text()
                for path in originals:
                    self.assertEqual(path.read_bytes(), originals[path])
                    self.assertIn(f"]({path.relative_to(record.capsule_root).as_posix()})", readme)
                actual = {path.relative_to(root).as_posix(): materializer.sha256_file(path) for path in originals}
                errors: list[str] = []
                validator.validate_retained_markdown_binding(manifest, record.capsule_root, actual, errors, repository_root=root)
                self.assertEqual(errors, [])
                current = (document.read_bytes(), (record.capsule_root / "selectors.jsonl").read_bytes())
                if previous is not None:
                    self.assertEqual(current, previous)
                previous = current

    def test_ordered_text_drift_or_commit_change_rejects_before_any_derived_write(self) -> None:
        for change in ("last-source", "html-evidence", "commit", "version", "identity", "retrieval", "anchor"):
            with self.subTest(change=change), self._retained_text_capsule() as (_, record, sources, originals, document), mock.patch.object(
                materializer, "fetch_bytes", side_effect=AssertionError("failed assembly must not fetch"),
            ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("failed assembly must not clear originals")):
                manifest_path = record.capsule_root / "manifest.yaml"
                if change in {"last-source", "html-evidence"}:
                    path = sources[-1][0] if change == "last-source" else next(path for path in originals if path.name == "Mapping.html")
                    path.write_bytes(path.read_bytes() + b"External drift.\n")
                elif change in {"commit", "version"}:
                    field, value = ("snapshot_commit", "b" * 40) if change == "commit" else ("source_version", "1.3")
                    record = replace(record, metadata={**record.metadata, "versioning": {**record.metadata["versioning"], field: value}})
                elif change == "identity":
                    record = replace(record, canonical_url="https://example.test/other/")
                else:
                    manifest = materializer.load_yaml(manifest_path)
                    if change == "retrieval":
                        manifest["retrievals"][0]["commit"] = "b" * 40
                    else:
                        manifest["materialization"]["link_rewrites"]["spec-model.md"] = "#spec-model-L999"
                    materializer.write_yaml(manifest_path, manifest)
                before = {path: path.read_bytes() for path in (*originals, document, manifest_path)}
                with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                    materializer.materialize_one(record, {}, "fixed-time")
                self.assertEqual({path: path.read_bytes() for path in before}, before)

    def test_ordered_text_keeps_preamble_and_only_separates_missing_final_newlines(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, mock.patch.object(materializer, "ROOT", Path(temporary)):
            root = Path(temporary)
            source = root / "capsule/source/native.md"
            source.parent.mkdir(parents=True)
            original = "\r\n".join([
                "<!-- native preamble -->", "", "Native title", "============", "",
                "```text", "a\tb", "```", "", "## End", "Last body without a final newline.",
            ]).encode("utf-8")
            source.write_bytes(original)
            schema = source.with_name("schema.yaml")
            yaml_original = b"classes:\n  mapping:\n    slots: [subject_id]"
            schema.write_bytes(yaml_original)
            document = root / "capsule/normalized/document.md"
            rows = materializer.derive_retained_text_sources([(source, "md"), (schema, "yaml")], document, {"native.md": "#native-L3"})
            text = document.read_bytes().decode("utf-8")
            self.assertEqual(source.read_bytes(), original)
            self.assertEqual(schema.read_bytes(), yaml_original)
            self.assertEqual([(row["source_start_line"], row["source_end_line"]) for row in rows], [(1, 9), (10, 11), (1, 3)])
            self.assertEqual(rows[0]["text_preview"], "<!-- native preamble -->")
            self.assertIn('<a id="native-L3"></a>\n\nNative title\r\n============', text)
            self.assertIn("```text\r\na\tb\r\n```", text)
            self.assertIn("Last body without a final newline.\n\nOriginal YAML", text)
            self.assertIn("```yaml\n" + yaml_original.decode() + "\n```\n", text)
            for row in rows:
                self.assertIn(row["text_preview"], "\n".join(text.splitlines()[row["start_line"] - 1:row["end_line"]]))

    @contextlib.contextmanager
    def _retained_html_capsule(self):
        with self._retained_text_capsule() as (root, record, _, _, document):
            sources: list[Path] = []
            originals: dict[Path, bytes] = {}
            for stem in ("dpv", "risk", "rights"):
                relative = f"source/2.3/dpv/{stem}.html" if stem == "dpv" else f"source/2.3/dpv/modules/{stem}.html"
                source = record.capsule_root / relative
                source.parent.mkdir(parents=True, exist_ok=True)
                cross = "modules/risk#same" if stem == "dpv" else ("rights#same" if stem == "risk" else "risk#same")
                src = "../diagrams/diagram.svg" if stem == "dpv" else "../../diagrams/diagram.svg"
                body = "\n".join([
                    "<!DOCTYPE html>", "<html><head>", '<script>var respecConfig = {localBiblio: "CONFIG_NOT_ASSEMBLED"};</script>', "</head>", "<body>",
                    f'BARE_{stem}<span class="concept-item" id="same">CONCEPT_{stem}<span class="definition"> DEFINITION_{stem} [[REF]] [=term=]</span></span>',
                    f'<h4 id="chapter">Chapter {stem}</h4>',
                    f'<p><a href="#same">Self {stem}</a> <a href="{cross}">Cross {stem}</a> <a href="outside.html#X">Outside</a></p>',
                    '<p><a href="https://external.test/#same">External</a> <a href="https://official.test/concept">Explicit route</a></p>',
                    '<p><code>[fake](modules/risk#same)\tX</code></p>',
                    '<pre><span>A\tB</span>\n<span>C\tD</span>\n<span># fake heading</span></pre>',
                    f'<table><caption>CAPTION_{stem}</caption>TABLE_OUTSIDE_{stem}<tr><th>Usage Note</th><td>FIRST_{stem}</td></tr><tr><th>Usage Note</th><td>SECOND_{stem}</td></tr><th>Examples</th><td>ORPHAN_{stem}</td></table>',
                    f'<ul><li>OUTER_{stem}<p>NESTED_{stem}</p><ul><li>INNER_{stem}</li></ul></li></ul>',
                    f'<img src="{src}">', "</body></html>",
                ]).encode("utf-8")
                source.write_bytes(body)
                sources.append(source)
                originals[source] = body
            asset = record.capsule_root / "source/2.3/diagrams/diagram.svg"
            asset.parent.mkdir(parents=True)
            asset.write_bytes(b'<svg><text>Retained diagram text</text><path d="M0 0"/></svg>\n')
            originals[asset] = asset.read_bytes()
            manifest = materializer.load_yaml(record.capsule_root / "manifest.yaml")
            manifest["materialization"] = {
                "document": "normalized/document.md",
                "retained_text_sources": [{"source": source.relative_to(record.capsule_root).as_posix(), "format": "html", "config_range": {"start_line": 3, "end_line": 3}} for source in sources],
                "link_rewrites": {
                    "../diagrams/diagram.svg": "../source/2.3/diagrams/diagram.svg",
                    "https://official.test/concept": "#dpv-same",
                },
            }
            manifest["retrievals"] = [{
                "local_path": path.relative_to(record.capsule_root).as_posix(), "sha256": materializer.sha256_file(path),
                "bytes": path.stat().st_size, "commit": "a" * 40,
                "resolved_url": "https://example.test/frozen/" + path.relative_to(record.capsule_root / "source/2.3").as_posix(),
            } for path in originals]
            manifest["local_files"] = materializer.local_file_inventory(record.capsule_root)
            manifest["local_bytes"] = sum(item["bytes"] for item in manifest["local_files"])
            materializer.write_yaml(record.capsule_root / "manifest.yaml", manifest)
            yield root, record, sources, originals, document, asset

    def test_html_replay_preserves_every_structural_atom_and_source_context(self) -> None:
        from bs4 import BeautifulSoup
        with self._retained_html_capsule() as (root, record, sources, originals, document, _), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("HTML replay must stay offline"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("HTML replay must retain originals")):
            previous = None
            for _ in range(2):
                manifest = materializer.materialize_one(record, {}, "fixed-time")
                text = document.read_bytes().decode("utf-8")
                selectors = [json.loads(line) for line in (record.capsule_root / "selectors.jsonl").read_text().splitlines()]
                self.assertNotIn("CONFIG_NOT_ASSEMBLED", text)
                self.assertEqual(text.count("```\nA\tB\nC\tD\n# fake heading\n```"), 3)
                self.assertEqual(text.count("`[fake](modules/risk#same)\tX`"), 3)
                self.assertEqual(text.count("[[REF]] [=term=]"), 3)
                for source in sources:
                    stem = source.stem
                    for label in ("BARE", "CONCEPT", "DEFINITION", "FIRST", "SECOND", "ORPHAN", "OUTER", "NESTED", "INNER", "CAPTION", "TABLE_OUTSIDE"):
                        self.assertEqual(text.count(f"{label}_{stem}"), 1)
                    self.assertIn(f"[Self {stem}](#{stem}-same)", text)
                    self.assertIn(f'- Usage Note | FIRST_{stem}', text)
                    self.assertIn(f'- Usage Note | SECOND_{stem}', text)
                    self.assertIn(f'id="{stem}-chapter"', text)
                    rows = [row for row in selectors if root / row["derived_from"] == source]
                    self.assertEqual(len([row for row in rows if row["kind"] == "configuration"]), 1)
                    soup = BeautifulSoup(originals[source], "html.parser")
                    for row in rows:
                        self.assertEqual(row["source_format"], "html")
                        self.assertTrue(1 <= row["source_start_line"] <= row["source_end_line"] <= len(originals[source].splitlines()))
                        target = (root / row["local_path"]).read_bytes().decode()
                        self.assertIn(row["text_preview"], "\n".join(target.splitlines()[row["start_line"] - 1:row["end_line"]]))
                        if row.get("source_heading_line"):
                            self.assertEqual(row["source_heading_line"], soup.h4.sourceline)
                            self.assertIn(f'id="{stem}-L{soup.h4.sourceline}"', text)
                self.assertIn("[Cross dpv](#risk-same)", text)
                self.assertIn("[Cross risk](#rights-same)", text)
                self.assertIn("[Cross rights](#risk-same)", text)
                self.assertIn("[Outside](https://example.test/frozen/dpv/modules/outside.html#X)", text)
                self.assertIn("[External](https://external.test/#same)", text)
                self.assertIn("[Explicit route](#dpv-same)", text)
                self.assertEqual(text.count("![](../source/2.3/diagrams/diagram.svg)"), 3)
                self.assertEqual({path: path.read_bytes() for path in originals}, originals)
                errors: list[str] = []
                validator.validate_retained_markdown_binding(manifest, record.capsule_root, {path.relative_to(root).as_posix(): materializer.sha256_file(path) for path in originals}, errors, repository_root=root)
                self.assertEqual(errors, [])
                current = (document.read_bytes(), (record.capsule_root / "selectors.jsonl").read_bytes())
                if previous is not None:
                    self.assertEqual(current, previous)
                previous = current

    def test_html_replay_uses_document_url_instead_of_api_download_url_for_unretained_links(self) -> None:
        with self._retained_html_capsule() as (_, record, sources, originals, document, _), mock.patch.object(
            materializer, "fetch_bytes", side_effect=AssertionError("HTML replay must stay offline"),
        ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("HTML replay must retain originals")):
            manifest_path = record.capsule_root / "manifest.yaml"
            manifest = materializer.load_yaml(manifest_path)
            for retrieval in manifest["retrievals"]:
                local_path = retrieval["local_path"]
                endpoint = "https://api.github.com/repos/w3c-cg/dpv/contents/" + local_path.removeprefix("source/") + "?ref=" + "a" * 40
                retrieval.update({"requested_url": endpoint, "resolved_url": endpoint})
                if local_path.endswith(".html"):
                    retrieval["document_url"] = "https://w3c-cg.github.io/dpv/" + local_path.removeprefix("source/")
            manifest["retrievals"][1]["document_url"] = "https://w3c-cg.github.io/dpv/2.3/dpv/modules/purposes.html"
            materializer.write_yaml(manifest_path, manifest)
            materializer.materialize_one(record, {}, "fixed-time")
            text = document.read_bytes().decode("utf-8")
            self.assertIn("[Outside](https://w3c-cg.github.io/dpv/2.3/dpv/modules/outside.html#X)", text)
            self.assertNotIn("api.github.com", text)
            for source in sources:
                self.assertIn(f"[Self {source.stem}](#{source.stem}-same)", text)
            self.assertIn("[Cross dpv](#risk-same)", text)
            self.assertEqual({path: path.read_bytes() for path in originals}, originals)

    def test_html_preflight_rejects_missing_original_or_asset_before_writing_consumer(self) -> None:
        for change in ("missing-original", "missing-asset", "asset-drift", "asset-commit", "config-range", "namespace"):
            with self.subTest(change=change), self._retained_html_capsule() as (_, record, sources, _, _, asset), mock.patch.object(
                materializer, "fetch_bytes", side_effect=AssertionError("failed HTML replay must stay offline"),
            ), mock.patch.object(materializer, "prepare_capsule", side_effect=AssertionError("failed HTML replay must retain originals")):
                manifest_path = record.capsule_root / "manifest.yaml"
                if change in {"missing-original", "missing-asset"}:
                    (sources[-1] if change == "missing-original" else asset).unlink()
                elif change == "asset-drift":
                    asset.write_bytes(asset.read_bytes() + b"External source drift.\n")
                else:
                    manifest = materializer.load_yaml(manifest_path)
                    if change == "asset-commit":
                        manifest["retrievals"][-1]["commit"] = "b" * 40
                    elif change == "config-range":
                        manifest["materialization"]["retained_text_sources"][0]["config_range"]["end_line"] = 999
                    else:
                        manifest["materialization"]["link_rewrites"]["https://official.test/concept"] = "#risk-missing"
                    materializer.write_yaml(manifest_path, manifest)
                before = {path: path.read_bytes() for path in record.capsule_root.rglob("*") if path.is_file()}
                with self.assertRaises(materializer.RetainedMarkdownPreflightError):
                    materializer.materialize_one(record, {}, "fixed-time")
                self.assertEqual({path: path.read_bytes() for path in before}, before)

    def test_default_html_to_sections_keeps_legacy_output(self) -> None:
        text, selectors, title = materializer.html_to_sections(b"<html><title>Legacy</title><body><h1>Root</h1><span>omitted</span><pre><span>A</span>\n<span>B</span></pre></body></html>", "https://example.test/legacy")
        self.assertEqual((text, title), ("# Root\n\nA B\n", "Legacy"))
        self.assertEqual([row["text_preview"] for row in selectors], ["Root", "A B"])


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

    def test_tex_import_directories_and_nested_subimport_use_explicit_context(self) -> None:
        files = {
            "draft/paper.txt": "\\import{chapters/}{intro}\n\\import{}{closing}\n",
            "draft/chapters/intro.tex": (
                "Introduction evidence.\n\\input{detail}\n"
                "\\subimport{nested/}{detail.ltx}\n\\import{shared/}{recap}\n"
            ),
            "draft/chapters/detail.tex": "Local input evidence.\n",
            "draft/chapters/nested/detail.ltx": "Nested evidence.\n\\subimport{}{tail}\n",
            "draft/chapters/nested/tail.tex": "Nested tail evidence.\n",
            "draft/shared/recap.tex": "Reset import evidence.\n",
            "draft/closing.tex": "Closing evidence.\n",
            "chapters/intro.tex": "WRONG PACKAGE ROOT COPY.\n",
        }
        diagnostics: list[dict[str, str]] = []
        graph: list[dict[str, str]] = []
        flattened = materializer.flatten_tex("draft/paper.txt", files, diagnostics=diagnostics, include_graph=graph)
        self.assertEqual(diagnostics, [])
        self.assertEqual(graph, [
            {"from": "draft/paper.txt", "to": "draft/chapters/intro.tex"},
            {"from": "draft/chapters/intro.tex", "to": "draft/chapters/detail.tex"},
            {"from": "draft/chapters/intro.tex", "to": "draft/chapters/nested/detail.ltx"},
            {"from": "draft/chapters/nested/detail.ltx", "to": "draft/chapters/nested/tail.tex"},
            {"from": "draft/chapters/intro.tex", "to": "draft/shared/recap.tex"},
            {"from": "draft/paper.txt", "to": "draft/closing.tex"},
        ])
        for evidence in ("Introduction", "Local input", "Nested tail", "Reset import", "Closing"):
            self.assertIn(f"{evidence} evidence.", flattened)
        self.assertNotIn("WRONG PACKAGE ROOT", flattened)

    def test_tex_import_comment_parity_and_repeated_legal_references(self) -> None:
        for command in ("import", "subimport"):
            for slash_count in range(5):
                with self.subTest(command=command, backslashes=slash_count):
                    files = {
                        "main.tex": "Line end" + "\\" * slash_count + f"% \\{command}{{parts/}}{{body}}\n",
                        "parts/body.tex": "Imported evidence.\n",
                    }
                    errors: list[dict[str, str]] = []
                    graph: list[dict[str, str]] = []
                    flattened = materializer.flatten_tex("main.tex", files, diagnostics=errors, include_graph=graph)
                    self.assertEqual(errors, [])
                    self.assertEqual(bool(graph), slash_count % 2 == 1)
                    self.assertEqual("Imported evidence." in materializer.tex_to_plain(flattened), slash_count % 2 == 1)
        graph = []
        errors = []
        flattened = materializer.flatten_tex("main.tex", {
            "main.tex": "\\import{parts/}{body}\n\\import{parts/}{body}\n",
            "parts/body.tex": "Repeated legal evidence.\n",
        }, diagnostics=errors, include_graph=graph)
        self.assertEqual(errors, [])
        self.assertEqual(flattened.count("Repeated legal evidence."), 2)
        self.assertEqual(graph, [{"from": "main.tex", "to": "parts/body.tex"}] * 2)

    def test_tex_import_diagnostics_do_not_hide_missing_unsafe_or_unsupported_calls(self) -> None:
        for files, depth, expected in (
            ({"main.txt": "\\import{parts/}{missing}"}, 20, "missing_include"),
            ({"main.txt": "\\import{../outside/}{body}", "../outside/body.tex": "UNSAFE EVIDENCE."}, 20, "missing_include"),
            ({"main.txt": "\\import{/absolute/}{body}", "/absolute/body.tex": "UNSAFE EVIDENCE."}, 20, "missing_include"),
            ({"main.txt": "\\import{}{../outside.tex}", "../outside.tex": "UNSAFE EVIDENCE."}, 20, "missing_include"),
            ({"main.txt": "\\import{}{loop}", "loop.tex": "\\subimport{}{main.txt}"}, 20, "cycle"),
            ({"main.txt": "\\import{}{body}", "body.tex": "Evidence."}, 1, "depth_limit"),
            ({
                "main.txt": "\\import{parts/}{body}", "parts/body.tex": "\\input{shared}",
                "shared.tex": "WRONG ROOT FALLBACK.",
            }, 20, "missing_include"),
            ({"main.txt": "\\import{\\folder}{body}"}, 20, "unsupported_include_syntax"),
            ({"main.txt": "\\import*{}{body}"}, 20, "unsupported_include_syntax"),
            ({"main.txt": "\\subimport{parts/}"}, 20, "unsupported_include_syntax"),
        ):
            with self.subTest(files=files, kind=expected):
                diagnostics: list[dict[str, str]] = []
                flattened = materializer.flatten_tex("main.txt", files, max_depth=depth, diagnostics=diagnostics)
                self.assertEqual([item["kind"] for item in diagnostics], [expected])
                self.assertNotIn("UNSAFE EVIDENCE.", flattened)
                self.assertNotIn("WRONG ROOT FALLBACK.", flattened)
                if expected in {"missing_include", "unsupported_include_syntax"}:
                    self.assertIn("\\", flattened)

    def test_retained_graphrag_imports_cover_appendix_tables_and_prompt_boundaries(self) -> None:
        source = REPOSITORY_ROOT / "materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/source"
        stored = {path.relative_to(source).as_posix(): path.read_text() for path in source.rglob("*") if path.is_file()}
        self.assertEqual(materializer.tex_root_candidates(stored), ["graph_rag.tex"])
        diagnostics: list[dict[str, str]] = []
        graph: list[dict[str, str]] = []
        flattened = materializer.flatten_tex("graph_rag.tex", stored, diagnostics=diagnostics, include_graph=graph)
        self.assertEqual(diagnostics, [])
        self.assertEqual(graph, [
            {"from": "graph_rag.tex", "to": "flow_figure.tex"},
            {"from": "graph_rag.tex", "to": "question_table.tex"},
            {"from": "graph_rag.tex", "to": "measures_figure.tex"},
            {"from": "graph_rag.tex", "to": "community_table.tex"},
            {"from": "graph_rag.tex", "to": "claim_comp_table.tex"},
            {"from": "graph_rag.tex", "to": "claim_div_table.tex"},
            {"from": "graph_rag.tex", "to": "acks.tex"},
            {"from": "graph_rag.tex", "to": "appendix.tex"},
            {"from": "appendix.tex", "to": "self_reflection_figure.tex"},
            {"from": "appendix.tex", "to": "communities_figure.tex"},
            {"from": "appendix.tex", "to": "answer_table.tex"},
            {"from": "appendix.tex", "to": "system_prompts.tex"},
            {"from": "appendix.tex", "to": "evaluation_prompts.tex"},
            {"from": "appendix.tex", "to": "stats_table.tex"},
        ])
        self.assertNotIn("\\import{", materializer.tex_without_comments(flattened))
        plain = materializer.tex_to_plain(flattened)
        self.assertTrue(plain.startswith("## Abstract\n"))
        self.assertNotIn("authoryear, sort", plain)
        self.assertNotIn("Microsoft Office of the CTO", plain)
        self.assertTrue(plain.split("## Statistical Analysis\n", 1)[1].lstrip().startswith("Pairwise comparisons"))
        for heading in (
            "Entity and Relationship Extraction Approach", "Example Community Detection", "Context Window Selection",
            "Example Answer Comparison", "System Prompts", "Evaluation Prompts", "Statistical Analysis",
        ):
            self.assertIn(f"## {heading}\n", plain)
        for evidence in (
            "Average number of extracted claims", "Average number of clusters across different distance thresholds",
            "Example question, answers, and LLM-generated assessments", "Comprehensiveness: Winner=1 (Graph RAG)",
            "Given a text document that is potentially relevant to this activity", "Write a comprehensive report of a community",
            "Note: the prompts for SS (semantic search) and TS (text summarization) conditions",
            "You are a helpful assistant responsible for grading two answers", '"winner": <1, 2, or 0>',
            "quality of answer as it relates to clearly explaining", "Pairwise comparisons of six conditions",
            "58.64 & 41.36 & -3.68", "43.6 & 56.4 & -3.96",
        ):
            self.assertIn(evidence, plain)
        self.assertIn("\\bibliography{bibliography}", flattened)  # Automatic .bbl loading is not implemented.
        self.assertIn("Level0Multihop.jpg", flattened)
        self.assertIn("Level1Multihop.jpg", flattened)

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
                "\\import{sections/}{body}\n\\include{appendix}\n\\end{document}\n"
            ),
            "sections/body.tex": "\\section{Introduction}\nBody evidence.\n\\subimport{}{detail}\n",
            "sections/detail.tex": "Nested import evidence.\n",
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
            source_selector_bytes = b"".join(
                line for line in (capsule / "selectors.jsonl").read_bytes().splitlines(keepends=True)
                if "derived_from" not in json.loads(line)
            )
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
            self.assertIn("Nested import evidence.", plain)
            self.assertIn("Appendix evidence.", plain)
            self.assertTrue((capsule / "selectors.jsonl").read_bytes().startswith(source_selector_bytes))
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

    def test_primary_pdf_still_rejects_an_undeclared_nonpage_selector(self) -> None:
        selectors = self._configure_arxiv_pdf_fixture()
        with selectors.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({
                "selector": "local://native#L1-L1", "local_path": "materialized_sources/corpus/paper-example/document.txt",
                "start_line": 1, "end_line": 1, "text_preview": "## Page 1",
            }) + "\n")
        result, output = self._run_validator()
        self.assertEqual(result, 1, output)
        self.assertIn("ARXIV_PDF_NON_PAGE_SELECTOR", output)

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
