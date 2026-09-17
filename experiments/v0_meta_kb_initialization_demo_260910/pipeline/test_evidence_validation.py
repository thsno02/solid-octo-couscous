from __future__ import annotations

import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from evidence_validation import validate_evidence_chain


def evidence(local_path: str, selector: str, excerpt: str) -> dict:
    return {
        "uid": "evidence:1",
        "provenance": {
            "source_refs": ["source:1"],
            "method": "deterministic-local-excerpt",
        },
        "semantics": {
            "property_assertions": {
                "local_path": local_path,
                "selector": selector,
                "excerpt": excerpt,
                "excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                "evidence_role": "source-text",
            }
        },
    }


def claim(text: str) -> dict:
    return {
        "uid": "claim:1",
        "provenance": {
            "method": "source-assertion-extraction-without-model",
            "source_refs": ["source:1"],
        },
        "epistemic": {"evidence_refs": ["evidence:1"]},
        "governance": {"promotion_state": "candidate"},
        "semantics": {
            "property_assertions": {
                "claim_scope": "source-reported assertion",
                "text": text,
            }
        },
    }


class EvidenceValidationTest(unittest.TestCase):
    def validate(self, root: Path, claim_row: dict, evidence_row: dict, source: dict | None = None) -> dict:
        return validate_evidence_chain(
            root=root,
            claims=[claim_row],
            evidence=[evidence_row],
            sources=[source or {"uid": "source:1", "status": "materialized", "content_tier": "full_text"}],
        )

    def test_line_selector_normalizes_whitespace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.txt").write_text("header\nEvidence  with\nwrapped whitespace.\n", encoding="utf-8")
            excerpt = "Evidence with wrapped whitespace."
            result = self.validate(root, claim(excerpt), evidence("source.txt", "local://source.txt#L2-L3", excerpt))
            self.assertEqual([], result["errors"])

    def test_hash_range_and_excerpt_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.txt").write_text("first\nsecond\n", encoding="utf-8")
            row = evidence("source.txt", "local://source.txt#L1-L1", "missing")
            row["semantics"]["property_assertions"]["excerpt_sha256"] = "0" * 64
            errors = self.validate(root, claim("missing"), row)["errors"]
            self.assertTrue(any(item.startswith("EVIDENCE_EXCERPT_HASH") for item in errors))
            self.assertTrue(any(item.startswith("EVIDENCE_SELECTOR_EXCERPT_MISMATCH") for item in errors))
            row["semantics"]["property_assertions"]["selector"] = "local://source.txt#L1-L3"
            errors = self.validate(root, claim("missing"), row)["errors"]
            self.assertTrue(any(item.startswith("EVIDENCE_SELECTOR_RANGE") for item in errors))

    def test_metadata_selector_resolves_exact_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "metadata.yaml").write_text("collection:\n  inclusion_reason: Selected evidence.\n", encoding="utf-8")
            excerpt = "Selected evidence."
            row = evidence(
                "metadata.yaml",
                "local://metadata.yaml#collection.inclusion_reason",
                excerpt,
            )
            self.assertEqual([], self.validate(root, claim(excerpt), row)["errors"])
            legacy = copy.deepcopy(row)
            legacy["semantics"]["property_assertions"]["selector"] = (
                "local://metadata.yaml#collection-inclusion-reason"
            )
            errors = self.validate(root, claim(excerpt), legacy)["errors"]
            self.assertTrue(any(item.startswith("EVIDENCE_SELECTOR_UNSUPPORTED_FRAGMENT") for item in errors))

    def test_claim_binding_metadata_policy_and_trust_are_checked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "source.txt").write_text("Supported text.\n", encoding="utf-8")
            row = evidence("source.txt", "local://source.txt#L1-L1", "Supported text.")
            claim_row = claim("Changed claim.")
            claim_row["provenance"]["source_refs"] = ["source:2"]
            claim_row["governance"]["promotion_state"] = "trusted"
            source = {"uid": "source:2", "status": "metadata_only", "content_tier": "metadata_capsule"}
            errors = self.validate(root, claim_row, row, source)["errors"]
            self.assertTrue(any(item.startswith("CLAIM_EVIDENCE_TEXT_MISMATCH") for item in errors))
            self.assertTrue(any(item.startswith("CLAIM_EVIDENCE_SOURCE_MISMATCH") for item in errors))
            self.assertTrue(any(item.startswith("METADATA_ONLY_SOURCE_REPORTED_CLAIM") for item in errors))
            self.assertTrue(any(item.startswith("TRUSTED_CLAIMS_MUST_BE_ZERO") for item in errors))


if __name__ == "__main__":
    unittest.main()
