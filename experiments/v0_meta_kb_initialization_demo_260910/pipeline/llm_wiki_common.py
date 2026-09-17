#!/usr/bin/env python3
"""Deterministically compile the v0 LLM Wiki from local claims and evidence."""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import shutil
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator

EXP = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
WIKI = EXP / "05_wiki"
VERSION = "deterministic-llm-wiki-v0.2"

DOMAINS: dict[str, tuple[str, list[str]]] = {
    "automated-research": ("Automated research systems and their evidence, evaluation, and governance.", ["Which research stages are automated?", "How are experiments and negative results retained?", "What prevents unsupported research narratives?"]),
    "cross-cutting": ("Infrastructure and evidence that spans several knowledge modules.", ["Which interfaces connect the modules?", "Which sources are true bridges rather than weakly classified?", "Where are shared dependencies fragile?"]),
    "governance-evaluation": ("Admission, factuality, review, rollback, and policy controls.", ["What evidence is sufficient for admission?", "How are citation and factual precision measured?", "Which changes require independent review?"]),
    "knowledge-editing": ("Modification of model or knowledge state with locality and rollback controls.", ["What object is edited?", "How are locality and generalization measured?", "How do edits propagate to dependent pages?"]),
    "knowledge-memory": ("Persistent memory, retrieval, graph organization, and temporal context.", ["What is stored and versioned?", "How are lexical, graph, and vector retrieval combined?", "How are freshness and provenance exposed?"]),
    "llm-wiki": ("Grounded long-form compilation, citation-aware writing, and human-steerable exploration.", ["How should research precede writing?", "How do paragraph citations expand to atomic evidence?", "How are multiple perspectives and unknown unknowns handled?"]),
    "ontology-semantic-architecture": ("Stable identity, schema, typed relations, provenance, and semantic change.", ["Which identifiers remain stable?", "How are schema changes migrated and rolled back?", "How are source, claim, evidence, page, time, and policy separated?"]),
    "open-ended-evolution": ("Processes that retain diversity, novelty, archives, and expanding repertoires.", ["What varies and what is retained?", "How does an archive prevent destructive forgetting?", "What keeps the process open-ended?"]),
    "recursive-self-improvement": ("Systems that modify agents, programs, prompts, or search processes under evaluation.", ["What can modify itself?", "What evaluator and archive constrain change?", "How are regressions and unsafe changes detected?"]),
}
REQ_TYPES = {"map", "overview", "concept", "method", "system", "comparison", "debate", "evidence", "source", "research_question", "collection", "gap", "evaluation"}


def yload(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def ydump(value: Any) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def ywrite(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ydump(value), encoding="utf-8")


def jread(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def jwrite(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def sha_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def h(value: str) -> str:
    return sha_text(value)[:16]


def slug(value: str) -> str:
    value = value.lower().replace("/", "-").replace(":", "-")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9._-]+", "-", value)).strip("-._") or "item"


def text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def prop(obj: dict[str, Any]) -> dict[str, Any]:
    value = obj.get("semantics", {}).get("property_assertions", {})
    return value if isinstance(value, dict) else {}


def srcs(obj: dict[str, Any]) -> list[str]:
    value = obj.get("provenance", {}).get("source_refs", [])
    return [str(item) for item in value] if isinstance(value, list) else []


def evrefs(claim: dict[str, Any]) -> list[str]:
    value = claim.get("epistemic", {}).get("evidence_refs", [])
    return [str(item) for item in value] if isinstance(value, list) else []


def ctext(claim: dict[str, Any]) -> str:
    return text(prop(claim).get("text"))


def cscope(claim: dict[str, Any]) -> str:
    return text(prop(claim).get("claim_scope"))


def cdomain(claim: dict[str, Any]) -> str:
    return text(prop(claim).get("domain")) or "cross-cutting"


def reported(claim: dict[str, Any]) -> bool:
    return cscope(claim) == "source-reported assertion"


def unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set(); result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value); result.append(value)
    return result


def link(current: str, target: str, label: str) -> str:
    relative = posixpath.relpath(target, posixpath.dirname(current) or ".")
    return f"[{label}]({relative})"


def fm(*, uid: str, title: str, path: str, ptype: str, summary: str, claims: list[str], sources: list[str], outgoing: list[dict[str, Any]], sections: list[dict[str, Any]], build: str, at: str, revisions: dict[str, str], body: str) -> dict[str, Any]:
    return {
        "uid": uid, "title": title, "slug": path[:-3] if path.endswith(".md") else path,
        "page_type": ptype, "status": "review", "summary": summary[:500], "aliases": [],
        "ontology_refs": ["experiment:meta-kb-v0"], "claim_refs": claims, "source_refs": sources,
        "page_refs": [item["target"] for item in outgoing], "outgoing_links": outgoing, "sections": sections,
        "temporal": {"created_at": at, "updated_at": at, "valid_from": None, "valid_to": None, "as_of": at},
        "provenance": {"build_id": build, "generated_by_agent": "pipeline/build_llm_wiki.py", "generated_by_model": None, "prompt_or_skill_version": VERSION, "compiled_from_revisions": [revisions.get(ref, ref) for ref in sources], "created_at": at, "updated_at": at, "manual_edits_preserved": False},
        "review": {"state": "needs_human", "reviewers": [], "decision_ref": None, "checked_claim_refs": [], "unresolved_issues": ["Scientific, semantic, neutrality, and due-weight review remain required before publication."]},
        "freshness": {"status": "fresh", "checked_at": at, "max_age_days": 30, "source_dependencies": sources, "staleness_reasons": []},
        "consumption": {"audiences": ["human", "agent"], "summary_tiers": {"one_line": summary[:220], "short": summary[:500], "full": None}, "estimated_tokens": max(1, len(body.split())), "machine_entry_points": [posixpath.relpath("04_claims/claims.jsonl", posixpath.dirname("05_wiki/" + path)), posixpath.relpath("03_evidence/evidence.jsonl", posixpath.dirname("05_wiki/" + path)), posixpath.relpath("05_wiki/catalog/pages.jsonl", posixpath.dirname("05_wiki/" + path))]},
    }


def add(page: dict[str, Any], target: str, relation: str, claims: list[str] | None = None, notes: str | None = None) -> None:
    page["outgoing"].append({"target": target, "relation": relation, "claim_refs": claims or [], "notes": notes})


def choose(claims: list[dict[str, Any]], domains: list[str] | None = None, limit: int = 10, source_only: bool | None = None) -> list[dict[str, Any]]:
    rows = claims
    if domains:
        rows = [item for item in rows if cdomain(item) in domains]
    if source_only is not None:
        rows = [item for item in rows if reported(item) is source_only]
    rows = sorted(rows, key=lambda item: (not reported(item), cdomain(item), str(item.get("uid"))))
    return rows[:limit]


def signals(rows: list[dict[str, Any]], current: str, claim_paths: dict[str, str], titles: dict[str, str]) -> str:
    if not rows:
        return "No claim-backed signal was selected for this section."
    out = []
    for claim in rows:
        uid = str(claim["uid"]); refs = srcs(claim); title = titles.get(refs[0], refs[0]) if refs else "Unknown source"
        out.append(f"- **{title}** ({'source assertion' if reported(claim) else 'collection assessment'}): {ctext(claim)[:420]} 〔{link(current, claim_paths[uid], uid)}〕")
    return "\n".join(out)


def page(path: str, uid: str, title: str, ptype: str, summary: str, body: str = "") -> dict[str, Any]:
    return {
        "path": path,
        "uid": uid,
        "title": title,
        "type": ptype,
        "summary": summary,
        "body": body,
        "claims": [],
        "rendered_claims": [],
        "sources": [],
        "rights_refs": [],
        "rights_unavailable_source_refs": [],
        "outgoing": [],
        "sections": [],
    }
