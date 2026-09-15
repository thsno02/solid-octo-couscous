#!/usr/bin/env python3
"""Machine artifacts, validation, review, release, and manifest outputs."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from evidence_validation import validate_evidence_chain
from llm_wiki_common import *

def parse_page(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_text(encoding="utf-8"); end = raw.find("\n---\n", 4)
    if not raw.startswith("---\n") or end < 0: raise ValueError("invalid frontmatter")
    value = yaml.safe_load(raw[4:end]); return value, raw[end + 5:]


def validate(claims: list[dict[str, Any]], evidence: list[dict[str, Any]], sources: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []; warnings: list[str] = []; cids = {str(c["uid"]) for c in claims}; eids = {str(e["uid"]) for e in evidence}; sids = {str(s["uid"]) for s in sources}
    evidence_validation = validate_evidence_chain(
        root=ROOT,
        claims=claims,
        evidence=evidence,
        sources=sources,
    )
    errors.extend(evidence_validation["errors"])
    trusted_claims = int(evidence_validation["trusted_claims"])
    pv = Draft202012Validator(yload(ROOT / "raw_data/schemas/wiki_page.schema.yaml")); cv = Draft202012Validator(yload(ROOT / "raw_data/schemas/wiki_change.schema.yaml"))
    pages: dict[str, tuple[Path, dict[str, Any], str]] = {}; slugs: set[str] = set(); types = Counter(); incoming = Counter()
    for path in sorted(WIKI.rglob("*.md")):
        try: front, body = parse_page(path)
        except Exception as exc: errors.append(f"WIKI_FRONTMATTER {path}: {exc}"); continue
        uid = str(front.get("uid") or ""); sl = str(front.get("slug") or ""); rel = path.relative_to(WIKI).as_posix()
        if not uid: errors.append(f"PAGE_WITHOUT_UID {rel}"); continue
        if uid in pages: errors.append(f"DUPLICATE_PAGE_UID {uid}")
        if sl in slugs: errors.append(f"DUPLICATE_PAGE_SLUG {sl}")
        pages[uid] = (path, front, body); slugs.add(sl); types[str(front.get("page_type"))] += 1
        for issue in pv.iter_errors(front): errors.append(f"PAGE_SCHEMA {rel}: {issue.message}")
        for ref in front.get("claim_refs", []):
            if str(ref) not in cids: errors.append(f"PAGE_BROKEN_CLAIM {rel} -> {ref}")
        for ref in front.get("source_refs", []):
            if str(ref) not in sids: errors.append(f"PAGE_BROKEN_SOURCE {rel} -> {ref}")
    for uid, (path, front, body) in pages.items():
        rel = path.relative_to(WIKI).as_posix()
        for item in front.get("outgoing_links", []):
            target = str(item.get("target") or "")
            if target not in pages: errors.append(f"PAGE_BROKEN_TYPED_LINK {rel} -> {target}")
            else: incoming[target] += 1
            for ref in item.get("claim_refs", []):
                if str(ref) not in cids: errors.append(f"PAGE_LINK_BROKEN_CLAIM {rel} -> {ref}")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
            if target.startswith(("http://", "https://", "mailto:", "#")): continue
            clean = target.split("#", 1)[0]
            if clean and not (path.parent / clean).resolve().exists(): errors.append(f"BROKEN_MARKDOWN_LINK {rel} -> {target}")
    missing = REQ_TYPES - set(types)
    if missing: errors.append(f"MISSING_REQUIRED_PAGE_TYPES {sorted(missing)}")
    claim_pages = {str(front.get("claim_refs", [""])[0]) for _, front, _ in pages.values() if front.get("page_type") == "evidence" and len(front.get("claim_refs", [])) == 1}
    source_pages = {str(front.get("source_refs", [""])[0]) for _, front, _ in pages.values() if front.get("page_type") == "source" and len(front.get("source_refs", [])) == 1}
    if claim_pages != cids: errors.append(f"CLAIM_PAGE_COVERAGE expected={len(cids)} actual={len(claim_pages)}")
    if source_pages != sids: errors.append(f"SOURCE_PAGE_COVERAGE expected={len(sids)} actual={len(source_pages)}")
    orphans = sorted(uid for uid in pages if uid != "wiki-page:v0-meta-kb-index" and incoming[uid] == 0)
    if orphans: errors.append(f"ORPHAN_PAGES {orphans[:10]}")
    required = ["catalog/pages.jsonl", "catalog/claims.jsonl", "catalog/sources.jsonl", "graph/nodes.jsonl", "graph/edges.jsonl", "graph/backlinks.jsonl", "graph/dependency_graph.yaml", "search/page_index.jsonl", "context_packs/context-pack-v0-collection-overview.yaml", "context_packs/context-pack-v0-evidence-and-governance.yaml", "context_packs/context-pack-v0-research-frontier.yaml"]
    for rel in required:
        if not (WIKI / rel).exists(): errors.append(f"MISSING_MACHINE_ARTIFACT {rel}")
    questions = yload(EXP / "06_evaluation/questions.yaml", {}) or {}
    if len(questions.get("questions", [])) != 5: errors.append("FIXED_QUESTION_SUITE_MUST_HAVE_FIVE_QUESTIONS")
    change = yload(EXP / "08_release/wiki_change.yaml", {}) or {}
    for issue in cv.iter_errors(change): errors.append(f"WIKI_CHANGE_SCHEMA: {issue.message}")
    if set(change.get("affected_pages", [])) != set(pages): errors.append("WIKI_CHANGE_PAGE_SET_MISMATCH")
    if set(change.get("affected_claims", [])) != cids: errors.append("WIKI_CHANGE_CLAIM_SET_MISMATCH")
    result = {"validation_id": "validation:llm-wiki-compiler-v0.2", "status": "passed" if not errors else "failed", "counts": {"pages": len(pages), "pages_by_type": dict(sorted(types.items())), "claims": len(cids), "evidence": len(eids), "sources": len(sids), "orphan_pages": len(orphans), "warnings": len(warnings), "errors": len(errors), "trusted_claims": trusted_claims}, "checks": {"wiki_page_schema": "pass" if not any(x.startswith("PAGE_SCHEMA") for x in errors) else "fail", "wiki_change_schema": "pass" if not any(x.startswith("WIKI_CHANGE_SCHEMA") for x in errors) else "fail", "claim_and_source_references": "pass" if not any("BROKEN_CLAIM" in x or "BROKEN_SOURCE" in x for x in errors) else "fail", "evidence_chain_integrity": "pass" if not (evidence_validation["evidence_errors"] or evidence_validation["claim_errors"]) else "fail", "metadata_only_source_policy": "pass" if not any(x.startswith("METADATA_ONLY_SOURCE_REPORTED_CLAIM") for x in evidence_validation["policy_errors"]) else "fail", "typed_and_markdown_links": "pass" if not any("LINK" in x for x in errors) else "fail", "claim_page_coverage": "pass" if claim_pages == cids else "fail", "source_page_coverage": "pass" if source_pages == sids else "fail", "page_type_coverage": "pass" if not missing else "fail", "fixed_question_suite": "pass" if len(questions.get("questions", [])) == 5 else "fail", "no_automatic_trust_promotion": "pass" if trusted_claims == 0 else "fail"}, "warnings": warnings, "errors": errors, "interpretation": "Deterministic structure and reference integrity, not scientific truth or editorial neutrality."}
    if errors: raise RuntimeError("LLM Wiki validation failed:\n- " + "\n- ".join(errors))
    return result


# Public aliases used by the standalone release validator.
EXPERIMENT_ROOT = EXP
WIKI_ROOT = WIKI
load_yaml = yload
load_jsonl = jread
parse_frontmatter_and_body = parse_page
sha256_file = sha_file

def validate_compiler_output(*, claims: list[dict[str, Any]], evidence: list[dict[str, Any]], selected_sources: list[dict[str, Any]]) -> dict[str, Any]:
    return validate(claims, evidence, selected_sources)


def manifest(build: str, at: str, inputs: list[Path]) -> None:
    outputs = []
    for base in [WIKI, EXP / "06_evaluation", EXP / "07_review"]:
        for path in sorted(base.rglob("*")):
            if path.is_file(): outputs.append({"path": path.relative_to(EXP).as_posix(), "bytes": path.stat().st_size, "sha256": sha_file(path)})
    rows = [{"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": sha_file(path)} for path in inputs]
    ywrite(EXP / "08_release/wiki_build_manifest.yaml", {"manifest_id": f"wiki-build-manifest:{h(build)}", "build_id": build, "compiler_version": VERSION, "generated_at": at, "inputs": rows, "outputs": outputs, "determinism": {"build_key": h("|".join(x["sha256"] for x in rows) + "|" + VERSION), "timestamps_derived_from": "00_inputs/materialization_snapshot.yaml", "model_calls": 0}, "rollback": "Restore the previous experiment tree and rebuild catalogs/context packs from pinned inputs."})
    jwrite(EXP / "08_release/change_feed.jsonl", [{"change_id": f"wiki-change:{h(build)}", "build_id": build, "generated_at": at, "status": "validated", "change_ref": "wiki_change.yaml", "manifest_ref": "wiki_build_manifest.yaml"}])

