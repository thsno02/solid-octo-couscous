#!/usr/bin/env python3
"""Read-only coverage checks with a fixed P1 collection anchor and phase-specific execution metadata."""
from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from materialize_all_sources import discover_records, filter_selectors_for_document
from validate_materialization_completeness import load_yaml, pdf_page_sections, scoped_path, validate_pdf_supplement
from validate_publication_rights import validate_pdf_supplement_rights

ROOT = Path(__file__).resolve().parents[1]
COLLECTION_BASE = "5458fbdffc95444cc26d5e9346fc2f9ab96e09c5"
PLAN = ROOT / "docs/plans/260916-corpus-completion-main-convergence/plan.yaml"
LEDGER = ROOT / "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml"
P1_REPORT = ROOT / "docs/plans/260916-corpus-completion-main-convergence/coverage-baseline.md"
RIGHTS = "raw_data/audits/materialization_rights_review.yaml"
CLAIMS = "experiments/v0_meta_kb_initialization_demo_260910/04_claims/claims.jsonl"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.PIPE)


def execution_report(ledger: dict) -> Path:
    execution = ledger["execution"]
    base = execution.get("base_sha")
    if not isinstance(base, str) or not base:
        raise ValueError("Missing execution.base_sha")
    try:
        commit = git("rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}").strip()
        git("merge-base", "--is-ancestor", commit, "HEAD")
    except subprocess.CalledProcessError:
        raise ValueError("Execution base must be a local commit and an ancestor of HEAD") from None
    report_path = execution.get("report_path")
    if report_path is None and ledger.get("phase") == "P1":
        report_path = P1_REPORT.relative_to(ROOT).as_posix()
    if not isinstance(report_path, str) or not report_path or Path(report_path).is_absolute():
        raise ValueError("Missing or non-relative execution.report_path")
    report = (ROOT / report_path).resolve()
    if not report.is_relative_to(ROOT) or report.suffix.lower() != ".md" or not report.is_file():
        raise ValueError("Execution report must be an existing Markdown file inside the repository")
    return report


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.is_file() else []


def collect_facts() -> dict:
    baseline = yaml.safe_load(git("show", f"{COLLECTION_BASE}:materialized_sources/index.yaml"))["items"]
    current = load_yaml(ROOT / "materialized_sources/index.yaml")["items"]
    registry = load_yaml(ROOT / "source_registry/registry.yaml")["entries"]
    records = discover_records()
    assert len({r.uid for r in records}) == len(records), "Duplicate discovered UID"
    assert {r.uid for r in records} == {x["uid"] for x in baseline}, "Collection changed from P1 base"
    index_by_uid = {x["uid"]: x for x in current}
    registry_by_uid = {x["uid"]: x for x in registry}
    rights = {x["uid"]: x for x in load_yaml(ROOT / RIGHTS)["items"]}
    claims = defaultdict(Counter)
    for claim in read_jsonl(ROOT / CLAIMS):
        for uid in claim["provenance"]["source_refs"]:
            claims[uid][claim["governance"]["promotion_state"]] += 1
    tracked = set(git("ls-files", "-z").split("\0"))
    by_uid = {r.uid: r for r in records}
    facts = []
    for item in baseline:
        if item["source_type"] == "github":
            continue
        uid = item["uid"]
        record = by_uid[uid]
        manifest_path = ROOT / item["manifest"]
        manifest = load_yaml(manifest_path)
        root = manifest_path.parent
        materialization = manifest.get("materialization") or {}
        declared = {x["path"] for x in manifest["local_files"]}
        document = materialization.get("document") or materialization.get("normalized_document")
        document_path = root / document if document else None
        document_text = document_path.read_text() if document_path and document_path.is_file() else ""
        selectors_path = root / "selectors.jsonl"
        selectors = read_jsonl(selectors_path)
        invalid = 0
        by_path = defaultdict(list)
        for selector in selectors:
            by_path[selector.get("local_path")].append(selector)
        for local_path, group in by_path.items():
            path = scoped_path(local_path, root)
            if path is None or not path.is_file() or local_path not in declared:
                invalid += len(group)
                continue
            retained, omitted = filter_selectors_for_document(group, path.read_text())
            invalid += omitted + sum(a != b for a, b in zip(retained, group))
        pages, duplicates = pdf_page_sections(document_text)
        review = rights.get(uid)
        gate = (review or {}).get("publication_gate") or {}
        public = gate.get("decision", "unknown")
        state_counts = dict(sorted(claims[uid].items()))
        mt_root = materialization.get("main_tex")
        retrievals = manifest.get("retrievals") or []
        observed = {
            "reported_status": manifest["status"],
            "reported_content_tier": manifest["content_tier"],
            "source_version_recorded": (record.metadata.get("versioning") or {}).get("source_version"),
            "local_revision": manifest.get("revision"),
            "document_path": document_path.relative_to(ROOT).as_posix() if document_path and document_path.is_file() else None,
            "document_lines": len(document_text.splitlines()),
            "document_characters": len(document_text),
            "main_tex_path": (root / "source" / mt_root).relative_to(ROOT).as_posix() if mt_root else None,
            "normalized_document": materialization.get("normalized_document"),
            "source_pdf": (root / materialization["source_pdf"]).relative_to(ROOT).as_posix() if materialization.get("source_pdf") else None,
            "retained_original_html_paths": sorted(path for path in declared if path.lower().endswith((".html", ".htm"))),
            "inventory_file_count": len(declared),
            "all_declared_files_present": all((ROOT / path).is_file() for path in declared),
            "all_declared_files_tracked": declared <= tracked,
            "selector_path": selectors_path.relative_to(ROOT).as_posix() if selectors_path.is_file() else None,
            "selector_count": len(selectors),
            "invalid_selector_count": invalid,
            "pdf_page_count_reported": materialization.get("pdf_page_count"),
            "pdf_text_page_headings": sorted(pages),
            "pdf_empty_text_pages": [page for page, text in pages.items() if not text.strip()],
            "pdf_duplicate_page_headings": sorted(duplicates),
            "content_was_truncated": materialization.get("content_was_truncated"),
            "omitted_member_count": len(manifest.get("omitted") or []),
            "errors": manifest.get("errors") or [],
            "warnings": manifest.get("warnings") or [],
            "limitations": manifest.get("limitations") or [],
            "requested_urls": [url for x in retrievals for url in (x.get("requested_urls") or [x.get("requested_url")]) if url],
            "resolved_urls": [x["resolved_url"] for x in retrievals if x.get("resolved_url")],
            "index_registry_consistent": all(
                index_by_uid[uid].get(field) == manifest.get(field)
                for field in ("status", "content_tier", "revision")
            ) and all(
                registry_by_uid[uid]["materialization"].get(field) == manifest.get(target)
                for field, target in (("state", "status"), ("content_tier", "content_tier"), ("revision", "revision"))
            ),
            "public_gate": public,
            "public_gate_revision_matches": review.get("source_revision") == manifest.get("revision") if review else None,
            "knowledge_claim_state_counts": state_counts,
        }
        supplement = manifest.get("pdf_supplement")
        if isinstance(supplement, dict):
            supplement_document = root / "pdf-supplement/document.txt"
            supplement_text = supplement_document.read_text() if supplement_document.is_file() else ""
            supplement_pages, supplement_duplicates = pdf_page_sections(supplement_text.split("<!-- materialization-redistribution-notice -->", 1)[0])
            supplement_selectors = root / "pdf-supplement/selectors.jsonl"
            supplement_errors = []
            validate_pdf_supplement(manifest, root, declared, {row["path"]: row["sha256"] for row in manifest["local_files"]}, supplement_errors)
            rights_errors, rights_blocks = validate_pdf_supplement_rights(manifest, manifest_path, ROOT, review)
            observed["pdf_supplement"] = {
                "source_version": supplement.get("source_version"),
                "local_revision": supplement.get("revision"),
                "source_pdf": (root / "pdf-supplement/document.pdf").relative_to(ROOT).as_posix(),
                "document_path": supplement_document.relative_to(ROOT).as_posix(),
                "document_lines": len(supplement_text.splitlines()),
                "document_characters": len(supplement_text),
                "selector_path": supplement_selectors.relative_to(ROOT).as_posix(),
                "selector_count": len(read_jsonl(supplement_selectors)),
                "pdf_page_count_reported": (supplement.get("materialization") or {}).get("pdf_page_count"),
                "pdf_text_page_headings": sorted(supplement_pages),
                "pdf_empty_text_pages": [page for page, text in supplement_pages.items() if not text.strip()],
                "pdf_duplicate_page_headings": sorted(supplement_duplicates),
                "body_quality_verified": supplement.get("body_quality_verified"),
                "limitations": supplement.get("limitations") or [],
                "validation_errors": supplement_errors,
                "public_gate": ((supplement.get("rights") or {}).get("publication_gate") or {}).get("decision", "unknown"),
                "public_package_valid": not rights_errors and not rights_blocks,
                "public_package_errors": rights_errors + rights_blocks,
            }
            if supplement.get("primary_excerpt") is not None:
                observed["pdf_supplement"]["primary_excerpt"] = supplement["primary_excerpt"]
        facts.append({"uid": uid, "source_type": record.source_type, "manifest": item["manifest"],
                      "metadata_path": record.relative_metadata_path, "title": record.title,
                      "canonical_id": record.canonical_id, "canonical_url": record.canonical_url, "observed": observed})
    return {"collection_anchor_sha": COLLECTION_BASE, "github_repo_excluded": sum(x["source_type"] == "github" for x in baseline), "items": facts}


def summarize(items: list[dict], excluded: int) -> dict:
    return {
        "collection_records": len(items) + excluded, "non_repo_total": len(items), "github_repo_excluded": excluded,
        "reported_content_tier_counts": dict(sorted(Counter(x["observed"]["reported_content_tier"] for x in items).items())),
        "source_type_counts": dict(sorted(Counter(x["source_type"] for x in items).items())),
        "original_artifact_counts": dict(sorted(Counter(x["original_artifact_coverage"]["state"] for x in items).items())),
        "text_extraction_counts": dict(sorted(Counter(x["text_extraction_coverage"]["state"] for x in items).items())),
        "action_bucket_counts": dict(sorted(Counter(x["action_bucket"] for x in items).items())),
        "public_redistribution_counts": dict(sorted(Counter(x["public_redistribution"]["state"] for x in items).items())),
        "content_inspected_full_text": sum(x["observed"]["reported_content_tier"] == "full_text" and bool(x["content_inspection"]) for x in items),
        "structure_only_full_text": sum(x["observed"]["reported_content_tier"] == "full_text" and not x["content_inspection"] for x in items),
        "locally_persisted_complete": sum(x["local_persistence"]["complete_target_consumable"] is True for x in items),
        "knowledge_candidate_sources": sum("candidate" in x["observed"]["knowledge_claim_state_counts"] for x in items),
        "knowledge_trusted_sources": sum("trusted" in x["observed"]["knowledge_claim_state_counts"] for x in items),
        "knowledge_sources_without_demo_claims": sum(not x["observed"]["knowledge_claim_state_counts"] for x in items),
        "unresolved_sources": sum(x["resolution"] == "unresolved" for x in items),
    }


def check(facts: dict) -> int:
    ledger = load_yaml(LEDGER)
    plan = load_yaml(PLAN)["controlled_values"]
    try:
        report_path = execution_report(ledger)
    except ValueError as error:
        print(error)
        return 1
    expected = {x["uid"]: x for x in facts["items"]}
    items = ledger["items"]
    errors = []
    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)
    require(facts["collection_anchor_sha"] == COLLECTION_BASE, "Wrong P1 collection anchor")
    require(len(items) == 131 and len(expected) == 131 and facts["github_repo_excluded"] == 84, "Wrong denominator")
    require(len({x["uid"] for x in items}) == len(items) and {x["uid"] for x in items} == set(expected), "UID coverage mismatch")
    for item in items:
        uid = item["uid"]
        if uid not in expected:
            continue
        for key in ("source_type", "manifest", "metadata_path", "observed"):
            require(item[key] == expected[uid][key], f"{uid}: stale {key}")
        target = item["target_document"]
        require(bool(target["boundary"]) and bool(target["version_reason"]) and "selected_version" in target, f"{uid}: missing boundary/version")
        require(all(target[key] == expected[uid][key] for key in ("title", "canonical_id", "canonical_url")), f"{uid}: target identity changed")
        require(target["source_kind"] in ("tex", "pdf", "html", "specification", "other"), f"{uid}: invalid source kind")
        require(target["boundary_verification_state"] in plan["coverage_verification_state"], f"{uid}: invalid boundary verification")
        require(target["selected_version"] == item["observed"]["source_version_recorded"], f"{uid}: invented version")
        require(bool(item["exact_limitation"]) and bool(item["next_action"]), f"{uid}: missing limitation/action")
        require(item["action_bucket"] in plan["action_bucket"], f"{uid}: invalid bucket")
        for key in ("original_artifact_coverage", "text_extraction_coverage"):
            coverage = item[key]
            require(coverage["state"] in plan[key] and coverage["verification_state"] in plan["coverage_verification_state"], f"{uid}: invalid {key}")
            require(bool(coverage["evidence"]), f"{uid}: missing {key} evidence")
            if coverage["state"] == "complete":
                require(coverage["verification_state"] == "verified" and target["selected_version"] is not None, f"{uid}: unverified complete")
                require(target["boundary_verification_state"] == "verified", f"{uid}: complete artifact without verified boundary")
            for evidence in coverage["evidence"] + item["content_inspection"]:
                path = ROOT / evidence["path"]
                require(path.is_file() and bool(evidence["result"]) and bool(evidence["locator"]), f"{uid}: broken evidence")
                if "start_line" in evidence:
                    lines = path.read_text().splitlines() if path.is_file() else []
                    require(1 <= evidence["start_line"] <= evidence["end_line"] <= len(lines), f"{uid}: invalid evidence range")
                    if "text_preview" in evidence:
                        first = next((line.strip() for line in lines[evidence["start_line"] - 1:evidence["end_line"]] if line.strip()), "")
                        require(evidence["text_preview"] == first[:140], f"{uid}: stale evidence preview")
        public = item["public_redistribution"]
        effective_gate = item["observed"]["public_gate"] if item["observed"]["public_gate_revision_matches"] is True else "unknown"
        require(public["state"] == effective_gate and public["reported_gate"] == item["observed"]["public_gate"], f"{uid}: stale rights gate treated as current")
        require(public["revision_matches"] == item["observed"]["public_gate_revision_matches"], f"{uid}: stale rights revision")
        require(item["observed"]["invalid_selector_count"] == 0 and item["observed"]["index_registry_consistent"], f"{uid}: local structural failure")
        supplement = item["observed"].get("pdf_supplement")
        if supplement:
            require(not supplement["validation_errors"] and supplement["public_package_valid"], f"{uid}: supplemental PDF integrity or independent allowance failure")
        if item["action_bucket"] == "complete_verified":
            require(all(item[key]["state"] == "complete" for key in ("original_artifact_coverage", "text_extraction_coverage")), f"{uid}: false complete bucket")
        if item["observed"]["reported_content_tier"] == "full_text" and not item["content_inspection"]:
            require(item["action_bucket"] == "needs_boundary_verification", f"{uid}: unchecked full_text")
    summary = summarize(items, facts["github_repo_excluded"])
    require(ledger["summary"] == summary, "Ledger summary mismatch")
    report = report_path.read_text()
    frontmatter = yaml.safe_load(report.split("---", 2)[1])
    require(frontmatter["coverage_summary"] == summary, "Report summary mismatch")
    require(summary["content_inspected_full_text"] >= 10, "Fewer than 10 full_text content inspections")
    require(all(x["content_inspection"] for x in items if x["observed"]["reported_content_tier"] in ("metadata_capsule", "excerpt_capsule")), "Gap UID lacks local content/absence check")
    for uid in ("arxiv:2406.04268", "arxiv:2502.18864"):
        require(any(x["uid"] == uid and x["known_parser_issue"] for x in items), f"Missing parser issue: {uid}")
    if errors:
        print("\n".join(errors))
        return 1
    print("PASS non_repo_coverage " + json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true", help="Print structural facts only; no coverage judgment and no writes.")
    args = parser.parse_args()
    facts = collect_facts()
    if args.probe:
        print(json.dumps(facts, ensure_ascii=False))
        return 0
    return check(facts)


if __name__ == "__main__":
    raise SystemExit(main())
