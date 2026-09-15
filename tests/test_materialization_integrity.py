from __future__ import annotations

import contextlib
import hashlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

import materialize_all_sources as materializer
import validate_materialization_completeness as validator


class MaterializerBoundaryTests(unittest.TestCase):
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
        for path in sorted(self.capsule.iterdir()):
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

    def test_valid_fixture_passes(self) -> None:
        result, output = self._run_validator()
        self.assertEqual(result, 0, output)

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


if __name__ == "__main__":
    unittest.main()
