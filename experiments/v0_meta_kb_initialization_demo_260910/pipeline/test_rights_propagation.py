from __future__ import annotations

import copy
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


class RightsPropagationTest(unittest.TestCase):
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
