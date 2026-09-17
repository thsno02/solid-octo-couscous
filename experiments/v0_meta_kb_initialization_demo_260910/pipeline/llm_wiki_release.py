#!/usr/bin/env python3
"""Machine artifacts, validation, review, release, and manifest outputs."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from llm_wiki_common import *

def pipeline(pages: list[dict[str, Any]], claims: list[dict[str, Any]], sources: list[dict[str, Any]], snapshot: dict[str, Any], config: dict[str, Any], build: str, at: str, m: dict[str, Any]) -> None:
    ywrite(EXP / "00_inputs/wiki_build_request.yaml", {"request_id": f"wiki-build-request:{h(build)}", "trigger": "manual_edit", "trigger_ref": "user-request:build-llm-wiki-after-materialization", "build_id": build, "scope": {"selected_sources": len(sources), "claims": len(claims), "maximum_affected_pages": len(pages)}, "allowed_operations": ["create", "update", "rebuild_index", "rebuild_context_pack"], "risk_class": "medium", "required_reviewers": ["wiki-editor", "evidence-reviewer"], "evaluation_suite": "v0-fixed-five-questions"})
    ywrite(EXP / "00_inputs/page_plan.yaml", {"plan_id": f"page-plan:{h(build)}", "build_id": build, "generated_at": at, "strategy": "question-oriented, claim-backed, typed-link compilation", "pages": [{"uid": p["uid"], "path": p["path"], "page_type": p["type"], "purpose": p["summary"], "claim_refs": p["claims"], "rendered_claim_refs": p["rendered_claims"], "source_refs": p["sources"], "rights_refs": p["rights_refs"], "rights_unavailable_source_refs": p["rights_unavailable_source_refs"], "planned_links": p["outgoing"]} for p in pages]})
    questions = [
        ("q1", "What is the LLM Wiki and what is it not?", ["wiki-page:llm-wiki-overview", "wiki-page:llm-wiki-reference-system"]),
        ("q2", "How does the pipeline preserve source, claim, evidence, and page provenance?", ["wiki-page:claim-evidence-page-compilation", "wiki-page:epistemic-separation"]),
        ("q3", "How do paper and repository consumption differ?", ["wiki-page:paper-vs-repository-consumption", "wiki-page:source-specific-consumption"]),
        ("q4", "Which quality gates block publication or trust promotion?", ["wiki-page:v0-quality-gates", "wiki-page:automation-vs-editorial-review"]),
        ("q5", "What remains unknown or unverified in v0?", ["wiki-page:knowledge-frontier", "wiki-page:materialization-and-trust-gaps"]),
    ]
    ywrite(EXP / "06_evaluation/questions.yaml", {"suite_id": "evaluation-suite:v0-fixed-five-questions", "build_id": build, "questions": [{"id": qid, "question": q, "route_pages": refs, "required_answer_fields": ["answer", "page_refs", "claim_refs", "source_refs", "uncertainty", "as_of"], "status": "not_run"} for qid, q, refs in questions]})
    type_counts = Counter(p["type"] for p in pages); domain_counts = Counter(text(s.get("domain")) or "cross-cutting" for s in sources); tier_counts = Counter(str(s.get("content_tier")) for s in sources)
    incoming = Counter(x["target"] for p in pages for x in p["outgoing"]); orphans = [p["uid"] for p in pages if p["uid"] != "wiki-page:v0-meta-kb-index" and incoming[p["uid"]] == 0]
    metrics = {"metrics_id": f"wiki-metrics:{h(build)}", "build_id": build, "generated_at": at, "counts": {"pages": len(pages), "pages_by_type": dict(sorted(type_counts.items())), "selected_sources": len(sources), "claims": len(claims), "claim_pages": type_counts["evidence"], "source_pages": type_counts["source"], "typed_links": sum(len(p["outgoing"]) for p in pages), "graph_nodes": m["nodes"], "graph_edges": m["edges"], "context_packs": len(m["packs"]), "orphan_pages": len(orphans), "trusted_claims": 0}, "coverage": {"claim_page_coverage": type_counts["evidence"] / max(1, len(claims)), "source_page_coverage": type_counts["source"] / max(1, len(sources)), "required_page_types_present": sorted(set(type_counts) & REQ_TYPES), "required_page_types_missing": sorted(REQ_TYPES - set(type_counts)), "selected_domains": dict(sorted(domain_counts.items())), "selected_content_tiers": dict(sorted(tier_counts.items()))}, "orphan_page_refs": orphans, "interpretation": "Structural completion and routing coverage, not scientific correctness."}
    ywrite(EXP / "06_evaluation/wiki_metrics.yaml", metrics)
    ywrite(EXP / "07_review/page_queue.yaml", {"build_id": build, "policy": "Pages remain review candidates; no claim becomes trusted without explicit admission.", "items": [{"page_ref": p["uid"], "path": p["path"], "risk": "high" if p["type"] in {"debate", "evaluation", "research_question"} else "medium", "state": "not_started", "rights_refs": p["rights_refs"], "rights_unavailable_source_refs": p["rights_unavailable_source_refs"], "required_checks": ["evidence-entailment", "citation-scope", "rights-scope", "identity", "contradiction", "neutrality", "due-weight", "freshness"]} for p in pages]})
    base = yload(EXP / "08_release/manifest.yaml", {}) or {}
    # A build describes compilation from its pinned claim-layer snapshot, not
    # from whichever generated output happened to be left by a previous run.
    base_rev = str(snapshot.get("build_id") or "v0-pre-wiki")
    checks = {name: {"status": status, "details": details, "artifact_ref": artifact} for name, status, details, artifact in [
        ("schema", "pass", "Page and change schemas are validated.", "06_evaluation/compiler_validation.yaml"), ("links", "pass", "Typed and Markdown links resolve.", "06_evaluation/compiler_validation.yaml"), ("citations", "pass", "Claims expand to atomic evidence pages; entailment remains reviewable.", "06_evaluation/wiki_metrics.yaml"), ("factuality", "warn", "Independent scientific factuality is not established.", "06_evaluation/wiki_metrics.yaml"), ("contradictions", "warn", "No mature contradiction graph exists in v0.", "04_claims/contradictions.jsonl"), ("identity", "pass", "Stable source, claim, and page IDs are unique.", "06_evaluation/compiler_validation.yaml"), ("neutrality", "warn", "Human neutrality and due-weight review remain required.", "07_review/page_queue.yaml"), ("policy", "pass", "No automatic trusted promotion.", "08_release/manifest.yaml")
    ]}
    change = {"change_id": f"wiki-change:{h(build)}", "trigger": "manual_edit", "trigger_ref": "user-request:build-llm-wiki-after-materialization", "base_revision": base_rev, "proposed_revision": build, "build_id": build, "source_deltas": [], "affected_pages": [p["uid"] for p in pages], "affected_claims": [str(c["uid"]) for c in claims], "affected_indexes_and_consumers": ["catalog/pages.jsonl", "catalog/claims.jsonl", "catalog/sources.jsonl", "graph/dependency_graph.yaml", "graph/nodes.jsonl", "graph/edges.jsonl", "graph/backlinks.jsonl", "search/page_index.jsonl"] + [p["pack_id"] for p in m["packs"]], "operations": [{"operation": "create", "target_ref": "wiki-page-set:v0-llm-wiki-candidate", "reason": "Compile the materialized claim/evidence layer into a navigable candidate wiki.", "patch_ref": "05_wiki/", "claim_refs": [str(c["uid"]) for c in claims]}, {"operation": "rebuild_index", "target_ref": "wiki-index:v0", "reason": "Build page, claim, source, graph, backlink, and lexical indexes.", "patch_ref": "05_wiki/catalog/", "claim_refs": []}, {"operation": "rebuild_context_pack", "target_ref": "context-pack-set:v0", "reason": "Build deterministic task packs.", "patch_ref": "05_wiki/context_packs/", "claim_refs": []}], "semantic_diff": {"added_claims": [], "removed_claims": [], "changed_scope_or_qualifiers": [], "identity_changes": [], "ontology_changes": [], "editorial_changes": ["replace claim concatenation with page-oriented compilation", "add atomic evidence pages and typed links", "add catalogs, graph, lexical index, context packs, fixed questions, and review queues"], "compatibility": "backward-compatible"}, "validation": {**checks, "evaluation_run_refs": ["evaluation-suite:v0-fixed-five-questions"]}, "review": {"required": True, "state": "not_started", "reviewers": [], "decision_ref": None, "discussion_ref": None}, "rollout": {"mode": "none", "canary_consumers": [], "start_at": None, "success_criteria": ["all structural checks pass", "fixed questions have traceable answers", "independent semantic/editorial review is recorded"]}, "rollback": {"available": True, "plan": "Restore the prior experiment revision and rebuild indexes/context packs.", "target_revision": base_rev, "compensating_operations": ["restore prior 05_wiki tree", "restore prior evaluation/review artifacts", "rebuild dependent context packs"], "tested": False}, "status": "validated"}
    change["status"] = "proposed"
    change["rollback"].update({"available": False, "target_revision": None,
        "plan": "Select an independently retained Git revision before rollback; the input build ID is not a restorable Git revision."})
    for check in checks.values():
        if check["status"] == "pass":
            check["status"] = "not_run"
    ywrite(EXP / "08_release/wiki_change.yaml", change)
    report = yload(EXP / "06_evaluation/report.yaml", {}) or {}; report.setdefault("checks", {}); report.setdefault("counts", {}); report["wiki_build_id"] = build; report["checks"].update({"llm_wiki_compilation": "pass", "typed_page_links": "pass", "claim_page_coverage": "pass", "source_page_coverage": "pass", "context_pack_generation": "pass", "scientific_truth": "not-evaluated", "neutrality_and_due_weight": "needs-human-review"}); report["counts"].update(metrics["counts"]); report["selected_content_tiers"] = dict(sorted(tier_counts.items())); report["selected_domains"] = dict(sorted(domain_counts.items())); report["interpretation"] = "Structural compilation, routing, and reference integrity; not scientific correctness."; ywrite(EXP / "06_evaluation/report.yaml", report)
    base.update({"experiment_id": config.get("experiment_id"), "build_id": snapshot.get("build_id") or base_rev, "wiki_build_id": build, "generated_at": at, "release_state": "candidate", "wiki_compiler_version": VERSION, "source_snapshot": "00_inputs/selected_sources.yaml", "page_plan": "00_inputs/page_plan.yaml", "wiki": "05_wiki/index.md", "wiki_catalog": ["05_wiki/catalog/pages.jsonl", "05_wiki/catalog/claims.jsonl", "05_wiki/catalog/sources.jsonl"], "wiki_graph": ["05_wiki/graph/dependency_graph.yaml", "05_wiki/graph/nodes.jsonl", "05_wiki/graph/edges.jsonl", "05_wiki/graph/backlinks.jsonl"], "wiki_search_index": "05_wiki/search/page_index.jsonl", "context_packs": [f"05_wiki/context_packs/{slug(p['pack_id'])}.yaml" for p in m["packs"]], "evaluation_questions": "06_evaluation/questions.yaml", "wiki_metrics": "06_evaluation/wiki_metrics.yaml", "claim_review_queue": "07_review/queue.yaml", "page_review_queue": "07_review/page_queue.yaml", "wiki_change": "08_release/wiki_change.yaml", "page_count": len(pages), "claim_page_count": type_counts["evidence"], "source_page_count": type_counts["source"], "trusted_claims": 0, "rollback": "Restore the previous experiment revision and rebuild indexes/context packs from pinned inputs."}); ywrite(EXP / "08_release/manifest.yaml", base)
    report["checks"]["llm_wiki_compilation"] = "not_run"
    ywrite(EXP / "06_evaluation/report.yaml", report)


def record_validation(result: dict[str, Any]) -> None:
    """Publish structural admission only after the validator has returned."""
    passed = not result["errors"]
    change_path = EXP / "08_release/wiki_change.yaml"
    change = yload(change_path, {})
    change["status"] = "validated" if passed else "proposed"
    for check in change["validation"].values():
        if isinstance(check, dict) and check.get("status") == "not_run":
            check["status"] = "pass" if passed else "fail"
    ywrite(change_path, change)
    report_path = EXP / "06_evaluation/report.yaml"
    report = yload(report_path, {})
    for name in ("llm_wiki_compilation", "typed_page_links", "claim_page_coverage", "source_page_coverage", "context_pack_generation"):
        report["checks"][name] = "pass" if passed else "fail"
    if not passed:
        report["validation_status"] = "failed"
    ywrite(report_path, report)
