from __future__ import annotations

import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

import yaml

from rights_propagation import (
    CLAIM_TRANSFORMATION,
    CLAIM_USE,
    DECLARED,
    EVIDENCE_TRANSFORMATION,
    EVIDENCE_USE,
    UNAVAILABLE,
    _validate_evidence_representation,
    make_rights_ref,
    pack_rights_payload,
    page_rights_payload,
    rights_markdown,
    validate_page_rights,
    validate_payload,
    validate_rights_chain,
)


def package() -> dict:
    return {
        "license_spdx": "CC-BY-4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "license_verified_at": "2026-09-16",
        "redistribution_package": {
            "source_revision": "revision-1",
            "source_version_url": "https://example.test/source/v1",
            "notice_path": "licenses/NOTICE.md",
            "attribution": "Example Author, Example Source.",
            "modifications": "Excerpted and whitespace-normalized.",
            "scope": "Only the pinned source text and selector excerpts.",
        },
    }


def source(*, wrapped: bool) -> dict:
    row = {
        "uid": "source:wrapped" if wrapped else "source:unwrapped",
        "manifest": "capsule/manifest.yaml",
        "revision": "revision-1",
        "title": "Wrapped Source" if wrapped else "Unwrapped Source",
        "rights_status": DECLARED if wrapped else UNAVAILABLE,
    }
    if wrapped:
        row["rights"] = package()
    return row


def object_row(uid: str, source_row: dict, *, kind: str, collector: bool = False) -> dict:
    props = {
        "text": "A bounded source sentence.",
        "excerpt": "A bounded source sentence.",
        "claim_scope": (
            "collector assessment, not source-authored scientific fact"
            if collector
            else "source-reported assertion"
        ),
    }
    if not collector:
        usage = CLAIM_USE if kind == "claim" else EVIDENCE_USE
        transformation = CLAIM_TRANSFORMATION if kind == "claim" else EVIDENCE_TRANSFORMATION
        ref = make_rights_ref(source_row, usage=usage, transformation=transformation)
        if ref:
            props["rights_refs"] = [ref]
        else:
            props["rights_unavailable_source_refs"] = [source_row["uid"]]
        if kind == "evidence":
            props["evidence_role"] = "source-text"
    return {
        "uid": uid,
        "provenance": {
            "source_refs": [source_row["uid"]],
            "method": (
                "collection-assessment-extraction"
                if kind == "claim" and collector
                else "source-assertion-extraction-without-model"
                if kind == "claim"
                else "collection-metadata-read"
                if collector
                else "deterministic-local-excerpt"
            ),
        },
        "epistemic": {"evidence_refs": ["evidence:1"] if kind == "claim" else []},
        "semantics": {"property_assertions": props},
    }


READING_TRANSFORMATIONS = {
    "retained_html_response": "Collector-derived static HTML structural text; excerpt is not a raw-source quotation.",
    "retained_git_text_sources": "Collector assembly of retained Git Markdown/YAML with line anchors and explicit local href routes; excerpt is not a raw-source quotation.",
    "tex_reading_view": "Collector-derived static TeX reading view; excerpt is not a raw-source quotation.",
}


class RightsPropagationTest(unittest.TestCase):
    def test_pdf_representation_uses_a_separate_package_pointer(self) -> None:
        row = source(wrapped=True)
        old = make_rights_ref(row, usage=EVIDENCE_USE, transformation=EVIDENCE_TRANSFORMATION)
        self.assertTrue(old["package_path"].endswith("#rights.redistribution_package"))
        row["source_representation"] = "pdf_supplement"
        pdf = make_rights_ref(row, usage=EVIDENCE_USE, transformation=EVIDENCE_TRANSFORMATION)
        self.assertTrue(pdf["package_path"].endswith("#pdf_supplement.rights.redistribution_package"))

    def write_capsule(self, root: Path, *, wrapped: bool) -> dict:
        (root / "capsule").mkdir()
        (root / "licenses").mkdir()
        (root / "licenses" / "NOTICE.md").write_text("License text.\n", encoding="utf-8")
        metadata = {"rights": package()} if wrapped else {"rights": {"license_spdx": None}}
        manifest = {
            "revision": "revision-1",
            "metadata_path": "metadata.yaml",
            "rights": package() if wrapped else {"declared_access": "unknown"},
        }
        (root / "metadata.yaml").write_text(yaml.safe_dump(metadata), encoding="utf-8")
        (root / "capsule" / "manifest.yaml").write_text(yaml.safe_dump(manifest), encoding="utf-8")
        return source(wrapped=wrapped)

    def write_reading_capsule(
        self, root: Path, representation: str = "retained_html_response", *,
        binding: str = "dated_html_response", wrapped: bool = True,
    ) -> tuple[dict, dict, dict, dict]:
        row = self.write_capsule(root, wrapped=wrapped)
        document = "normalized/reading.md" if representation == "tex_reading_view" else "normalized/document.md"
        path = root / "capsule" / document
        path.parent.mkdir()
        path.write_text("# Reading\nA bounded source sentence.\n", encoding="utf-8")
        manifest_path = root / row["manifest"]
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        materialization = {"document": document, "normalized_document": document}
        if representation == "tex_reading_view":
            materialization["tex_reading_view"] = {"enabled": True, "profile": "conservative-v1", "document": document}
        else:
            materialization["retained_text_binding"] = binding
        manifest["materialization"] = materialization
        manifest_path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
        metadata_path = root / "metadata.yaml"
        metadata = yaml.safe_load(metadata_path.read_text(encoding="utf-8"))
        metadata["collection"] = {"inclusion_reason": "A collector-authored assessment."}
        metadata_path.write_text(yaml.safe_dump(metadata), encoding="utf-8")
        row.update({"source_representation": representation, "local_document": f"capsule/{document}"})
        item = object_row("evidence:1", row, kind="evidence")
        item["provenance"]["method"] = "deterministic-derived-reading-excerpt"
        props = item["semantics"]["property_assertions"]
        props.update({
            "source_representation": representation,
            "transformation": READING_TRANSFORMATIONS[representation],
            "local_path": row["local_document"],
            "selector": f"local://{row['local_document']}#L2-L2",
            "excerpt_sha256": hashlib.sha256(props["excerpt"].encode("utf-8")).hexdigest(),
        })
        return row, manifest, item, object_row("claim:1", row, kind="claim")

    def validate_reading(self, root: Path, row: dict, item: dict, claims: list[dict]) -> list[str]:
        before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
        errors = validate_rights_chain(root=root, claims=claims, evidence=[item], sources=[row])
        after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)
        return errors

    def test_declared_reading_views_preserve_source_and_collector_rights(self) -> None:
        from evidence_validation import validate_evidence_chain

        for representation, binding in (
            ("retained_html_response", "dated_html_response"),
            ("retained_html_response", "wiki_page_revision_set"),
            ("retained_git_text_sources", "git_snapshot"),
            ("tex_reading_view", ""),
        ):
            for wrapped in (True, False):
                with self.subTest(representation=representation, binding=binding, wrapped=wrapped), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    row, _, item, claim = self.write_reading_capsule(root, representation, binding=binding, wrapped=wrapped)
                    self.assertEqual([], self.validate_reading(root, row, item, [claim]))
                    collector_item = object_row("evidence:collector", row, kind="evidence", collector=True)
                    collector_props = collector_item["semantics"]["property_assertions"]
                    collector_props.update({
                        "text": "A collector-authored assessment.",
                        "excerpt": "A collector-authored assessment.",
                        "local_path": "metadata.yaml",
                        "selector": "local://metadata.yaml#collection.inclusion_reason",
                        "excerpt_sha256": hashlib.sha256(b"A collector-authored assessment.").hexdigest(),
                    })
                    collector_item["provenance"].update({"source_hash": None, "source_version": None})
                    collector_claim = object_row("claim:collector", row, kind="claim", collector=True)
                    collector_claim["semantics"]["property_assertions"]["text"] = collector_props["excerpt"]
                    collector_claim["epistemic"]["evidence_refs"] = [collector_item["uid"]]
                    result = validate_evidence_chain(root=root, claims=[claim, collector_claim], evidence=[item, collector_item], sources=[row])
                    self.assertEqual([], result["errors"])
                    self.assertNotIn("rights_refs", collector_props)
                    self.assertNotIn("rights_unavailable_source_refs", collector_props)
                    self.assertEqual("collection-metadata-read", collector_item["provenance"]["method"])
                    self.assertIsNone(collector_item["provenance"]["source_hash"])
                    self.assertIsNone(collector_item["provenance"]["source_version"])

    def test_raw_pdf_method_is_not_classified_by_its_root_reading_view(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row, manifest, _, _ = self.write_reading_capsule(root)
            row["source_representation"] = "pdf_supplement"
            item = object_row("evidence:pdf", row, kind="evidence")
            errors = []
            # Test only the new method seam; the independent PDF rights gate is unchanged.
            _validate_evidence_representation(
                root=root, item=item, source_uids=[row["uid"]], sources_by_uid={row["uid"]: row},
                manifests={row["uid"]: (manifest, (root / row["manifest"]).resolve())}, errors=errors,
            )
            self.assertEqual([], errors)
            self.assertTrue(item["semantics"]["property_assertions"]["rights_refs"][0]["package_path"].endswith("#pdf_supplement.rights.redistribution_package"))

    def test_reading_methods_and_disclosures_are_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row, _, item, claim = self.write_reading_capsule(root)
            for method in (None, "unknown", "model-extraction", "deterministic-derived-reading-excerpt-v2", "deterministic-local-excerpt", "collection-metadata-read"):
                with self.subTest(method=method):
                    changed = copy.deepcopy(item)
                    changed["provenance"]["method"] = method
                    changed["semantics"]["property_assertions"].pop("evidence_role")
                    self.assertTrue(self.validate_reading(root, row, changed, [claim]))
            for field, values, prefix in (
                ("source_representation", (None, "", "unknown", {}, []), "EVIDENCE_DERIVED_REPRESENTATION"),
                ("transformation", (None, "", " ", {}, "Raw source quotation.", READING_TRANSFORMATIONS["tex_reading_view"]), "EVIDENCE_DERIVED_TRANSFORMATION"),
            ):
                for value in values:
                    with self.subTest(field=field, value=value):
                        changed = copy.deepcopy(item)
                        changed["semantics"]["property_assertions"][field] = value
                        errors = self.validate_reading(root, row, changed, [claim])
                        self.assertTrue(any(error.startswith(prefix) for error in errors), errors)
                changed = copy.deepcopy(item)
                changed["semantics"]["property_assertions"].pop(field)
                self.assertTrue(self.validate_reading(root, row, changed, [claim]))
            raw = copy.deepcopy(item)
            raw["provenance"]["method"] = "deterministic-local-excerpt"
            for field in ("source_representation", "transformation"):
                raw["semantics"]["property_assertions"].pop(field)
            changed_row = copy.deepcopy(row)
            changed_row.pop("source_representation")
            errors = self.validate_reading(root, changed_row, raw, [claim])
            self.assertTrue(any("raw-for-reading-view" in error for error in errors), errors)
            raw_row = copy.deepcopy(row)
            raw_row["source_representation"] = "pdf_supplement"
            errors = self.validate_reading(root, raw_row, item, [claim])
            self.assertTrue(any("selected-source" in error for error in errors), errors)

    def test_reading_views_require_the_manifest_and_actual_consumer(self) -> None:
        for representation, binding in (("retained_html_response", "dated_html_response"), ("retained_git_text_sources", "git_snapshot"), ("tex_reading_view", "")):
            with self.subTest(representation=representation), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                row, manifest, item, claim = self.write_reading_capsule(root, representation, binding=binding)
                for field, value in (("document", "document.md"), ("normalized_document", None), ("retained_text_binding", "unknown")):
                    with self.subTest(field=field):
                        changed = copy.deepcopy(manifest)
                        changed["materialization"][field] = value
                        (root / row["manifest"]).write_text(yaml.safe_dump(changed), encoding="utf-8")
                        errors = self.validate_reading(root, row, item, [claim])
                        self.assertTrue(any("manifest-consumer" in error for error in errors), errors)
                if representation == "tex_reading_view":
                    for field, value in (("enabled", 1), ("enabled", "true"), ("profile", "other"), ("document", "document.md")):
                        changed = copy.deepcopy(manifest)
                        changed["materialization"]["tex_reading_view"][field] = value
                        (root / row["manifest"]).write_text(yaml.safe_dump(changed), encoding="utf-8")
                        errors = self.validate_reading(root, row, item, [claim])
                        self.assertTrue(any("manifest-consumer" in error for error in errors), errors)
                changed = copy.deepcopy(manifest)
                if representation != "tex_reading_view":
                    changed["materialization"]["retained_text_binding"] = "git_snapshot" if representation == "retained_html_response" else "dated_html_response"
                    (root / row["manifest"]).write_text(yaml.safe_dump(changed), encoding="utf-8")
                    self.assertTrue(self.validate_reading(root, row, item, [claim]))
                    changed["materialization"].pop("retained_text_binding")
                    (root / row["manifest"]).write_text(yaml.safe_dump(changed), encoding="utf-8")
                    self.assertTrue(self.validate_reading(root, row, item, [claim]))
                changed = copy.deepcopy(manifest)
                changed.pop("materialization")
                (root / row["manifest"]).write_text(yaml.safe_dump(changed), encoding="utf-8")
                self.assertTrue(self.validate_reading(root, row, item, [claim]))
                (root / row["manifest"]).write_text(yaml.safe_dump(manifest), encoding="utf-8")
                (root / "capsule/source").mkdir()
                (root / "capsule/source/specification.html").write_text("A bounded source sentence.\n", encoding="utf-8")
                (root / "other").mkdir()
                (root / "other/document.md").write_text("A bounded source sentence.\n", encoding="utf-8")
                for local_path in ("capsule/source/specification.html", "other/document.md", "../outside.md", str(root / row["local_document"]), None):
                    with self.subTest(local_path=local_path):
                        changed = copy.deepcopy(item)
                        changed["semantics"]["property_assertions"]["local_path"] = local_path
                        changed_row = copy.deepcopy(row)
                        changed_row["local_document"] = local_path
                        errors = self.validate_reading(root, changed_row, changed, [claim])
                        self.assertTrue(any("local-consumer" in error for error in errors), errors)
                changed_row = copy.deepcopy(row)
                changed_row["source_representation"] = "retained_git_text_sources" if representation != "retained_git_text_sources" else "retained_html_response"
                self.assertTrue(self.validate_reading(root, changed_row, item, [claim]))
                changed_row = copy.deepcopy(row)
                changed_row["local_document"] = "capsule/document.md"
                self.assertTrue(self.validate_reading(root, changed_row, item, [claim]))
                chosen = root / row["local_document"]
                chosen.unlink()
                errors = self.validate_reading(root, row, item, [claim])
                self.assertTrue(any(error.startswith("RIGHTS_EVIDENCE_DERIVED_MISSING") for error in errors), errors)
                other = root / "other/document.md"
                chosen.symlink_to(other)
                errors = self.validate_reading(root, row, item, [claim])
                self.assertTrue(any("outside-capsule" in error for error in errors), errors)

    def test_standalone_derived_evidence_cannot_hide_rights_or_collector_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row, _, item, claim = self.write_reading_capsule(root)
            item["semantics"]["property_assertions"].pop("evidence_role")
            self.assertEqual([], self.validate_reading(root, row, item, []))
            for refs in ([], ["source:unknown"]):
                changed = copy.deepcopy(item)
                changed["provenance"]["source_refs"] = refs
                errors = self.validate_reading(root, row, changed, [])
                self.assertTrue(any(error.startswith("EVIDENCE_DERIVED_BINDING") for error in errors), errors)
            for role in (None, "collector-metadata", {}):
                changed = copy.deepcopy(item)
                props = changed["semantics"]["property_assertions"]
                props["evidence_role"] = role
                props.pop("rights_refs")
                errors = self.validate_reading(root, row, changed, [])
                self.assertTrue(any(error.startswith("EVIDENCE_RIGHTS_COVERAGE") for error in errors), errors)
            for field, value in (("usage", "other"), ("source_revision", "wrong"), ("license_spdx", "unknown")):
                changed = copy.deepcopy(item)
                changed["semantics"]["property_assertions"]["rights_refs"][0][field] = value
                self.assertTrue(self.validate_reading(root, row, changed, []))
            collector = object_row("claim:collector", row, kind="claim", collector=True)
            changed = copy.deepcopy(item)
            changed["semantics"]["property_assertions"].pop("rights_refs")
            errors = self.validate_reading(root, row, changed, [collector])
            self.assertTrue(any(error.startswith("CLAIM_EVIDENCE_METHOD_MISMATCH") for error in errors), errors)
            changed["provenance"]["method"] = "collection-metadata-read"
            errors = self.validate_reading(root, row, changed, [])
            self.assertTrue(any(error.startswith("EVIDENCE_METHOD_MISMATCH") for error in errors), errors)
            changed = copy.deepcopy(claim)
            changed["semantics"]["property_assertions"]["claim_scope"] = "collector assessment, not source-authored scientific fact"
            errors = self.validate_reading(root, row, item, [changed])
            self.assertTrue(any(error.startswith("CLAIM_SCOPE_METHOD_MISMATCH") for error in errors), errors)
            (root / "licenses/NOTICE.md").unlink()
            errors = self.validate_reading(root, row, item, [claim])
            self.assertTrue(any(error.startswith("RIGHTS_NOTICE_MISSING") for error in errors), errors)

    def test_derived_readings_keep_existing_evidence_and_policy_checks(self) -> None:
        from evidence_validation import validate_evidence_chain

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            row, _, item, claim = self.write_reading_capsule(root)
            cases = (
                ("evidence", "selector", f"local://{row['local_document']}#L2-L3", "EVIDENCE_SELECTOR_RANGE"),
                ("evidence", "selector", "local://capsule/other.md#L2-L2", "EVIDENCE_SELECTOR_PATH_MISMATCH"),
                ("evidence", "excerpt", "Missing source sentence.", "EVIDENCE_SELECTOR_EXCERPT_MISMATCH"),
                ("claim", "text", "Different claim.", "CLAIM_EVIDENCE_TEXT_MISMATCH"),
            )
            for owner, field, value, prefix in cases:
                changed_item, changed_claim = copy.deepcopy(item), copy.deepcopy(claim)
                target = changed_item if owner == "evidence" else changed_claim
                target["semantics"]["property_assertions"][field] = value
                errors = validate_evidence_chain(root=root, claims=[changed_claim], evidence=[changed_item], sources=[row])["errors"]
                self.assertTrue(any(error.startswith(prefix) for error in errors), errors)
            changed = copy.deepcopy(claim)
            changed["provenance"]["source_refs"] = ["source:other"]
            changed["governance"] = {"promotion_state": "trusted"}
            errors = validate_evidence_chain(root=root, claims=[changed], evidence=[item], sources=[row])["errors"]
            self.assertTrue(any(error.startswith("CLAIM_EVIDENCE_SOURCE_MISMATCH") for error in errors), errors)
            self.assertTrue(any(error.startswith("TRUSTED_CLAIMS_MUST_BE_ZERO") for error in errors), errors)

    def test_wrapped_source_propagates_to_evidence_and_claim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_row = self.write_capsule(root, wrapped=True)
            evidence = object_row("evidence:1", source_row, kind="evidence")
            claim = object_row("claim:1", source_row, kind="claim")
            self.assertEqual(
                [],
                validate_rights_chain(
                    root=root, claims=[claim], evidence=[evidence], sources=[source_row]
                ),
            )

    def test_unwrapped_source_is_explicit_without_inventing_a_license(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_row = self.write_capsule(root, wrapped=False)
            evidence = object_row("evidence:1", source_row, kind="evidence")
            claim = object_row("claim:1", source_row, kind="claim")
            self.assertNotIn("rights_refs", claim["semantics"]["property_assertions"])
            self.assertEqual(
                [],
                validate_rights_chain(
                    root=root, claims=[claim], evidence=[evidence], sources=[source_row]
                ),
            )

    def test_collector_assessment_does_not_inherit_source_rights(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_row = self.write_capsule(root, wrapped=True)
            evidence = object_row("evidence:1", source_row, kind="evidence", collector=True)
            claim = object_row("claim:1", source_row, kind="claim", collector=True)
            self.assertEqual(
                [],
                validate_rights_chain(
                    root=root, claims=[claim], evidence=[evidence], sources=[source_row]
                ),
            )
            claim["semantics"]["property_assertions"]["rights_refs"] = [
                make_rights_ref(
                    source_row,
                    usage=CLAIM_USE,
                    transformation=CLAIM_TRANSFORMATION,
                )
            ]
            errors = validate_rights_chain(
                root=root, claims=[claim], evidence=[evidence], sources=[source_row]
            )
            self.assertTrue(any(error.startswith("COLLECTOR_RIGHTS_INHERITANCE") for error in errors))

    def test_mixed_page_and_context_pack_scope_only_source_claim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_row = self.write_capsule(root, wrapped=True)
            source_claim = object_row("claim:source", source_row, kind="claim")
            collector_claim = object_row("claim:collector", source_row, kind="claim", collector=True)
            collector_claim["semantics"]["property_assertions"]["text"] = "A collector-authored assessment."
            claims = {row["uid"]: row for row in (source_claim, collector_claim)}
            refs, unavailable = page_rights_payload(claims, claims)
            body = (
                "A bounded source sentence. `claim:source`\n\n"
                "A collector-authored assessment. `claim:collector`\n\n"
                + rights_markdown(
                current_repo_path="wiki/mixed.md",
                rights_refs=refs,
                unavailable_source_refs=unavailable,
                sources_by_uid={source_row["uid"]: source_row},
                )
            )
            front = {
                "claim_refs": list(claims),
                "rendered_claim_refs": list(claims),
                "rights_refs": refs,
                "rights_unavailable_source_refs": unavailable,
            }
            self.assertEqual(
                [],
                validate_page_rights(
                    owner="mixed.md",
                    frontmatter=front,
                    body=body,
                    claims_by_uid=claims,
                    sources_by_uid={source_row["uid"]: source_row},
                ),
            )
            self.assertEqual(["claim:source"], refs[0]["claim_refs"])
            pack_refs, pack_unavailable = pack_rights_payload(claims, claims)
            self.assertEqual(["claim:source"], pack_refs[0]["claim_refs"])
            self.assertEqual([], validate_payload(
                owner="pack",
                claim_ids=list(claims),
                claims_by_uid=claims,
                actual_refs=pack_refs,
                actual_unavailable=pack_unavailable,
                pack=True,
            ))

    def test_missing_or_mismatched_propagation_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_row = self.write_capsule(root, wrapped=True)
            evidence = object_row("evidence:1", source_row, kind="evidence")
            claim = object_row("claim:1", source_row, kind="claim")
            broken_claim = copy.deepcopy(claim)
            broken_claim["semantics"]["property_assertions"]["rights_refs"] = []
            errors = validate_rights_chain(
                root=root, claims=[broken_claim], evidence=[evidence], sources=[source_row]
            )
            self.assertTrue(any(error.startswith("CLAIM_RIGHTS_COVERAGE") for error in errors))

            scope_tampered = copy.deepcopy(claim)
            scope_tampered["semantics"]["property_assertions"]["claim_scope"] = (
                "collector assessment, not source-authored scientific fact"
            )
            scope_tampered["semantics"]["property_assertions"].pop("rights_refs")
            broken_evidence = copy.deepcopy(evidence)
            broken_evidence["semantics"]["property_assertions"].pop("rights_refs")
            errors = validate_rights_chain(
                root=root,
                claims=[scope_tampered],
                evidence=[broken_evidence],
                sources=[source_row],
            )
            self.assertTrue(any(error.startswith("CLAIM_SCOPE_METHOD_MISMATCH") for error in errors))
            self.assertTrue(any(error.startswith("EVIDENCE_RIGHTS_COVERAGE") for error in errors))

            errors = validate_rights_chain(
                root=root, claims=[], evidence=[broken_evidence], sources=[source_row]
            )
            self.assertTrue(any(error.startswith("EVIDENCE_RIGHTS_COVERAGE") for error in errors))

            claims = {claim["uid"]: claim}
            refs, unavailable = page_rights_payload(claims, claims)
            errors = validate_payload(
                owner="missing-pack",
                claim_ids=list(claims),
                claims_by_uid=claims,
                actual_refs=[],
                actual_unavailable=unavailable,
                pack=True,
            )
            self.assertTrue(any(error.startswith("RIGHTS_PAYLOAD_MISMATCH") for error in errors))

            errors = validate_payload(
                owner="00_inputs/page_plan.yaml:claim-page",
                claim_ids=list(claims),
                claims_by_uid=claims,
                actual_refs=[],
                actual_unavailable=unavailable,
            )
            self.assertTrue(any(error.startswith("RIGHTS_PAYLOAD_MISMATCH") for error in errors))

            errors = validate_page_rights(
                owner="tampered-source-page.md",
                frontmatter={
                    "claim_refs": [claim["uid"]],
                    "rendered_claim_refs": [],
                    "rights_refs": [],
                    "rights_unavailable_source_refs": [],
                },
                body="A bounded source sentence. `claim:1`",
                claims_by_uid=claims,
                sources_by_uid={source_row["uid"]: source_row},
            )
            self.assertTrue(any(error.startswith("RIGHTS_RENDERED_CLAIMS_MISMATCH") for error in errors))

            mismatched_source = copy.deepcopy(source_row)
            mismatched_source["revision"] = "wrong-revision"
            errors = validate_rights_chain(
                root=root, claims=[claim], evidence=[evidence], sources=[mismatched_source]
            )
            self.assertTrue(any(error.startswith("RIGHTS_SOURCE_REVISION_MISMATCH") for error in errors))


if __name__ == "__main__":
    unittest.main()
