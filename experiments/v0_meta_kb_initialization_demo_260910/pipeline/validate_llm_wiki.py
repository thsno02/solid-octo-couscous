#!/usr/bin/env python3
"""Validate the compiled v0 LLM Wiki release and its deterministic manifest."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from build_llm_wiki import (
    EXPERIMENT_ROOT,
    ROOT,
    WIKI_ROOT,
    load_jsonl,
    load_yaml,
    parse_frontmatter_and_body,
    sha256_file,
    validate_compiler_output,
)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    claims = load_jsonl(EXPERIMENT_ROOT / "04_claims" / "claims.jsonl")
    evidence = load_jsonl(EXPERIMENT_ROOT / "03_evidence" / "evidence.jsonl")
    selected = load_yaml(EXPERIMENT_ROOT / "00_inputs" / "selected_sources.yaml", {})
    selected_sources = selected.get("sources") if isinstance(selected, dict) else None
    if not isinstance(selected_sources, list):
        print("selected_sources.yaml has no sources list", file=sys.stderr)
        return 1

    try:
        compiler_validation = validate_compiler_output(
            claims=claims,
            evidence=evidence,
            selected_sources=[item for item in selected_sources if isinstance(item, dict)],
        )
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    errors: list[str] = []
    required = [
        EXPERIMENT_ROOT / "00_inputs" / "wiki_build_request.yaml",
        EXPERIMENT_ROOT / "00_inputs" / "page_plan.yaml",
        EXPERIMENT_ROOT / "06_evaluation" / "wiki_metrics.yaml",
        EXPERIMENT_ROOT / "06_evaluation" / "questions.yaml",
        EXPERIMENT_ROOT / "06_evaluation" / "compiler_validation.yaml",
        EXPERIMENT_ROOT / "07_review" / "page_queue.yaml",
        EXPERIMENT_ROOT / "08_release" / "wiki_change.yaml",
        EXPERIMENT_ROOT / "08_release" / "wiki_build_manifest.yaml",
        EXPERIMENT_ROOT / "08_release" / "change_feed.jsonl",
    ]
    for path in required:
        if not path.exists():
            fail(f"MISSING_RELEASE_ARTIFACT {path.relative_to(EXPERIMENT_ROOT)}", errors)

    manifest_path = EXPERIMENT_ROOT / "08_release" / "wiki_build_manifest.yaml"
    manifest = load_yaml(manifest_path, {}) if manifest_path.exists() else {}
    build_id = str(manifest.get("build_id") or "") if isinstance(manifest, dict) else ""
    if not build_id:
        fail("BUILD_MANIFEST_WITHOUT_BUILD_ID", errors)

    if isinstance(manifest, dict):
        for item in manifest.get("inputs", []):
            if not isinstance(item, dict):
                fail("INVALID_MANIFEST_INPUT", errors)
                continue
            path = ROOT / str(item.get("path") or "")
            if not path.exists():
                fail(f"MANIFEST_INPUT_MISSING {item.get('path')}", errors)
                continue
            if path.stat().st_size != item.get("bytes") or sha256_file(path) != item.get("sha256"):
                fail(f"MANIFEST_INPUT_HASH_MISMATCH {item.get('path')}", errors)
        for item in manifest.get("outputs", []):
            if not isinstance(item, dict):
                fail("INVALID_MANIFEST_OUTPUT", errors)
                continue
            path = EXPERIMENT_ROOT / str(item.get("path") or "")
            if not path.exists():
                fail(f"MANIFEST_OUTPUT_MISSING {item.get('path')}", errors)
                continue
            if path.stat().st_size != item.get("bytes") or sha256_file(path) != item.get("sha256"):
                fail(f"MANIFEST_OUTPUT_HASH_MISMATCH {item.get('path')}", errors)

    report = load_yaml(EXPERIMENT_ROOT / "06_evaluation" / "report.yaml", {})
    change = load_yaml(EXPERIMENT_ROOT / "08_release" / "wiki_change.yaml", {})
    release = load_yaml(EXPERIMENT_ROOT / "08_release" / "manifest.yaml", {})
    if not isinstance(report, dict) or str(report.get("wiki_build_id") or "") != build_id:
        fail("BUILD_ID_MISMATCH report", errors)
    if not isinstance(change, dict) or str(change.get("build_id") or "") != build_id:
        fail("BUILD_ID_MISMATCH wiki_change", errors)
    if not isinstance(release, dict) or str(release.get("wiki_build_id") or "") != build_id:
        fail("BUILD_ID_MISMATCH release", errors)
    if not isinstance(release, dict) or release.get("trusted_claims") != 0:
        fail("RELEASE_TRUSTED_CLAIMS_MUST_BE_ZERO", errors)

    page_ids: set[str] = set()
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        frontmatter, _body = parse_frontmatter_and_body(path)
        page_ids.add(str(frontmatter.get("uid")))
        if str(frontmatter.get("provenance", {}).get("build_id") or "") != build_id:
            fail(f"PAGE_BUILD_ID_MISMATCH {path.relative_to(WIKI_ROOT)}", errors)

    page_queue = load_yaml(EXPERIMENT_ROOT / "07_review" / "page_queue.yaml", {})
    queued_pages = {
        str(item.get("page_ref"))
        for item in (page_queue.get("items", []) if isinstance(page_queue, dict) else [])
        if isinstance(item, dict)
    }
    if queued_pages != page_ids:
        fail(f"PAGE_REVIEW_QUEUE_MISMATCH pages={len(page_ids)} queued={len(queued_pages)}", errors)

    feed_path = EXPERIMENT_ROOT / "08_release" / "change_feed.jsonl"
    feed: list[dict[str, Any]] = load_jsonl(feed_path) if feed_path.exists() else []
    if len(feed) != 1 or str(feed[0].get("build_id") or "") != build_id or feed[0].get("status") != "validated":
        fail("CHANGE_FEED_MISMATCH", errors)

    print(
        "llm_wiki_release_validation "
        f"build_id={build_id} pages={len(page_ids)} claims={len(claims)} "
        f"manifest_inputs={len(manifest.get('inputs', [])) if isinstance(manifest, dict) else 0} "
        f"manifest_outputs={len(manifest.get('outputs', [])) if isinstance(manifest, dict) else 0} "
        f"warnings={len(compiler_validation.get('warnings', []))} errors={len(errors)}"
    )
    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\nThe compiled v0 LLM Wiki release passed deterministic manifest and reference validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
