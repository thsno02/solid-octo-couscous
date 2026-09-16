#!/usr/bin/env python3
"""Fail closed unless every retained full document has a publication allowance."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

from materialize_all_sources import redistribution_footer


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "raw_data/audits/materialization_rights_review.yaml"
CORPUS_ROOT = ROOT / "materialized_sources/corpus"


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate_publication_rights(
    audit_path: Path = AUDIT_PATH,
    corpus_root: Path = CORPUS_ROOT,
) -> tuple[list[str], list[str], int, int]:
    errors: list[str] = []
    blocked: list[str] = []
    if not audit_path.is_file():
        return [f"PUBLICATION_RIGHTS_AUDIT_MISSING {audit_path}"], blocked, 0, 0

    audit = load_yaml(audit_path)
    if not isinstance(audit, dict) or not isinstance(audit.get("items"), list):
        return ["PUBLICATION_RIGHTS_AUDIT_INVALID"], blocked, 0, 0
    items = audit["items"]
    scope = audit.get("scope") if isinstance(audit.get("scope"), dict) else {}
    baseline_count = scope.get("baseline_full_text_count")
    if not isinstance(baseline_count, int) or baseline_count != len(items):
        fail(
            f"PUBLICATION_RIGHTS_AUDIT_COUNT expected={baseline_count} actual={len(items)}",
            errors,
        )

    audited: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("uid"), str):
            fail("PUBLICATION_RIGHTS_AUDIT_ITEM_INVALID", errors)
            continue
        uid = item["uid"]
        if uid in audited:
            fail(f"PUBLICATION_RIGHTS_AUDIT_DUPLICATE {uid}", errors)
            continue
        audited[uid] = item

    active_full_text: dict[str, Path] = {}
    for manifest_path in sorted(corpus_root.glob("*/manifest.yaml")):
        manifest = load_yaml(manifest_path)
        materialization = manifest.get("materialization") if isinstance(manifest, dict) else None
        retained_source_pdf = (
            isinstance(materialization, dict)
            and isinstance(materialization.get("source_pdf"), str)
            and bool(materialization["source_pdf"])
        )
        if not isinstance(manifest, dict) or (
            manifest.get("content_tier") != "full_text" and not retained_source_pdf
        ):
            continue
        uid = manifest.get("uid")
        if not isinstance(uid, str) or not uid:
            fail(f"PUBLICATION_MANIFEST_UID_MISSING {manifest_path.relative_to(ROOT)}", errors)
            continue
        if uid in active_full_text:
            fail(f"PUBLICATION_MANIFEST_UID_DUPLICATE {uid}", errors)
            continue
        active_full_text[uid] = manifest_path

    for uid, manifest_path in sorted(active_full_text.items()):
        review = audited.get(uid)
        if review is None:
            fail(f"PUBLICATION_RIGHTS_REVIEW_MISSING {uid}", errors)
            continue
        reviewed_manifest = review.get("manifest_path")
        publication_root = corpus_root.parents[1]
        actual_manifest = manifest_path.relative_to(publication_root).as_posix()
        if reviewed_manifest != actual_manifest:
            fail(
                f"PUBLICATION_RIGHTS_MANIFEST_MISMATCH {uid} "
                f"reviewed={reviewed_manifest} actual={actual_manifest}",
                errors,
            )
        source_revision = review.get("source_revision")
        manifest = load_yaml(manifest_path)
        actual_revision = manifest.get("revision") if isinstance(manifest, dict) else None
        if not isinstance(source_revision, str) or source_revision != actual_revision:
            fail(
                f"PUBLICATION_RIGHTS_REVISION_MISMATCH {uid} "
                f"reviewed={source_revision} actual={actual_revision}",
                errors,
            )
        gate = review.get("publication_gate")
        decision = gate.get("decision") if isinstance(gate, dict) else None
        if decision != "allow":
            reason = gate.get("reason") if isinstance(gate, dict) else "missing publication gate"
            blocked.append(f"{uid}: {reason}")
        else:
            # An allowance with packaging conditions is not valid when a later
            # materialization silently discards the reviewed notice/attribution.
            package = review.get("redistribution_package")
            actual_package = manifest.get("rights", {}).get("redistribution_package")
            try:
                metadata_path = manifest.get("metadata_path")
                canonical_package = None
                if metadata_path:
                    metadata_file = (publication_root / metadata_path).resolve()
                    metadata_file.relative_to(publication_root.resolve())
                    canonical_package = load_yaml(metadata_file).get("rights", {}).get("redistribution_package")
                if not (package or actual_package or canonical_package):
                    continue
                capsule_package = load_yaml(manifest_path.parent / "source-metadata.yaml").get("rights", {}).get("redistribution_package")
                if not package or not (package == canonical_package == capsule_package == actual_package) or package["source_revision"] != actual_revision:
                    raise ValueError("reviewed and materialized license packages differ")
                license_path = (publication_root / package["notice_path"]).resolve()
                license_path.relative_to(publication_root.resolve())
                expected_notice = license_path.read_text(encoding="utf-8")
                notice = manifest_path.parent / "NOTICE.md"
                if not expected_notice.strip() or notice.read_text(encoding="utf-8") != expected_notice:
                    raise ValueError("full notice is absent or differs from the reviewed license")
                document = (manifest_path.parent / manifest["materialization"]["document"]).resolve()
                document.relative_to(manifest_path.parent.resolve())
                text = document.read_text(encoding="utf-8")
                if text.count("<!-- materialization-redistribution-notice -->") != 1 or not text.endswith(redistribution_footer(package)):
                    raise ValueError("attribution or modification notice is absent")
            except (KeyError, TypeError, AttributeError, ValueError, OSError) as exc:
                fail(f"PUBLICATION_RIGHTS_PACKAGE_INVALID {uid}: {exc}", errors)

    if not active_full_text:
        fail("PUBLICATION_FULL_TEXT_SET_EMPTY", errors)
    return errors, blocked, len(active_full_text), len(audited)


def main() -> int:
    errors, blocked, active_count, audited_count = validate_publication_rights()

    print(
        "publication_rights_gate "
        f"active_full_text={active_count} audited={audited_count} "
        f"blocked={len(blocked)} errors={len(errors)}"
    )
    if errors:
        print("\nAudit errors:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
    if blocked:
        print("\nPublication blocks:", file=sys.stderr)
        for message in blocked:
            print(f"- {message}", file=sys.stderr)
    if errors or blocked:
        print(
            "\nPublic redistribution remains blocked until every active full-text capsule "
            "or retained full document has an explicit audited allow decision.",
            file=sys.stderr,
        )
        return 1
    print("\nEvery active full-text capsule or retained full document has an explicit audited publication allowance.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
