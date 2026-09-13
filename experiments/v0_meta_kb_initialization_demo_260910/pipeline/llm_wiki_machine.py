#!/usr/bin/env python3
"""Machine artifacts, validation, review, release, and manifest outputs."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from llm_wiki_common import *

def write_pages(pages: list[dict[str, Any]], build: str, at: str, sources: list[dict[str, Any]]) -> None:
    revisions = {str(item["uid"]): f"{item['uid']}@{item.get('revision')}" if item.get("revision") else str(item["uid"]) for item in sources}
    for p in pages:
        front = fm(uid=p["uid"], title=p["title"], path=p["path"], ptype=p["type"], summary=p["summary"], claims=p["claims"], sources=p["sources"], outgoing=p["outgoing"], sections=p["sections"], build=build, at=at, revisions=revisions, body=p["body"])
        path = WIKI / p["path"]; path.parent.mkdir(parents=True, exist_ok=True); path.write_text("---\n" + ydump(front) + "---\n\n" + p["body"].rstrip() + "\n", encoding="utf-8")


def machine(pages: list[dict[str, Any]], claims: list[dict[str, Any]], evidence: list[dict[str, Any]], sources: list[dict[str, Any]], build: str, at: str) -> dict[str, Any]:
    ppath = {p["uid"]: p["path"] for p in pages}; cpath = {str(c["uid"]): f"claims/{slug(str(c['uid']))}.md" for c in claims}; spath = {str(s["uid"]): f"sources/{slug(str(s['uid']))}.md" for s in sources}
    jwrite(WIKI / "catalog/pages.jsonl", ({"uid": p["uid"], "title": p["title"], "path": p["path"], "page_type": p["type"], "summary": p["summary"], "claim_refs": p["claims"], "source_refs": p["sources"]} for p in pages))
    jwrite(WIKI / "catalog/claims.jsonl", ({"uid": str(c["uid"]), "text": ctext(c), "scope": cscope(c), "domain": cdomain(c), "source_refs": srcs(c), "evidence_refs": evrefs(c), "page": cpath[str(c["uid"])]} for c in claims))
    jwrite(WIKI / "catalog/sources.jsonl", ({"uid": str(s["uid"]), "title": text(s.get("title")), "source_type": s.get("source_type"), "content_tier": s.get("content_tier"), "revision": s.get("revision"), "page": spath{str(s["uid"])]} for s in sources))
    nodes = [{"id": p["uid"], "kind": "page", "path": p["path"], "label": p["title"]} for p in pages] + [{"id": str(c["uid"]), "kind": "claim", "label": ctext(c)[:180]} for c in claims] + [{"id": str(e["uid"]), "kind": "evidence", "label": text(prop(e).get("selector"))} for e in evidence] + [{"id": str(s["uid"]), "kind": "source", "label": text(s.get("title"))} for s in sources]
    edges: list[dict[str, Any]] = []
    for p in pages:
        edges += [{"from": p["uid"], "to": cid, "relation": "uses_claim"} for cid in p["claims"]]
        edges += [{"from": p["uid"], "to": sid, "relation": "uses_source"} for sid in p["sources"]]
        edges += [{"from": p["uid"], "to": x["target"], "relation": x["relation"]} for x in p["outgoing"]]
    for c in claims:
        edges += [{"from": str(c["uid"]), "to": eid, "relation": "supported_by"} for eid in evrefs(c)]
        edges += [{"from": str(c["uid"]), "to": sid, "relation": "reported_by"} for sid in srcs(c)]
    jwrite(WIKI / "graph/nodes.jsonl", nodes); jwrite(WIKI / "graph/edges.jsonl", edges)
    backlinks: dict[str, list[dict[str, str]]] = defaultdict(list)
    for edge in edges: backlinks[edge["to"]].append({"from": edge["from"], "relation": edge["relation"]})
    jwrite(WIKI / "graph/backlinks.jsonl", ({"target": target, "backlinks": rows} for target, rows in sorted(backlinks.items())))
    ywrite(WIKI / "graph/dependency_graph.yaml", {"build_id": build, "generated_at": at, "nodes": len(nodes), "edges": len(edges), "page_dependencies": {p["uid"]: {"path": p["path"], "claim_refs": p["claims"], "source_refs": p["sources"], "page_refs": [x["target"] for x in p["outgoing"]]} for p in pages}})
    jwrite(WIKI / "search/page_index.jsonl", ({"uid": p["uid"], "path": p["path"], "title": p["title"], "page_type": p["type"], "summary": p["summary"], "search_text": text(p["title"] + " " + p["summary"] + " " + re.sub(r"[`#>*|]", " ", p["body"]))[:6000]} for p in pages))
    packs = [
        {"pack_id": "context-pack:v0-collection-overview", "task": "Orient a reader to the corpus and LLM Wiki architecture.", "pages": ["wiki-page:v0-meta-kb-index", "wiki-page:llm-wiki-overview", "wiki-page:v0-corpus", "wiki-page:llm-wiki-reference-system"]},
        {"pack_id": "context-pack:v0-evidence-and-governance", "task": "Explain evidence, trust, evaluation, and review boundaries.", "pages": ["wiki-page:epistemic-separation", "wiki-page:claim-evidence-page-compilation", "wiki-page:v0-quality-gates", "wiki-page:automation-vs-editorial-review"]},
        {"pack_id": "context-pack:v0-research-frontier", "task": "Identify gaps and next research questions.", "pages": ["wiki-page:knowledge-frontier", "wiki-page:materialization-and-trust-gaps", "wiki-page:knowledge-evolution-loop", "wiki-page:map-open-implementations"]},
    ]
    claim_lookup = {str(c["uid"]): c for c in claims}
    for pack in packs:
        ids = unique(cid for pid in pack["pages"] for cid in next(p for p in pages if p["uid"] == pid)["claims"][:6]); sids = unique(ref for cid in ids for ref in srcs(claim_lookup[cid])); pack.update({"as_of": at, "wiki_release": build, "ontology_version": "experiment:meta-kb-v0", "claims": ids, "sources": sids, "open_conflicts": [], "freshness": "fresh", "token_budget": 6000, "build_manifest": "../../../08_release/wiki_build_manifest.yaml"}); ywrite(WIKI / f"context_packs/{slug(pack['pack_id'])}.yaml", pack)
    return {"nodes": len(nodes), "edges": len(edges), "packs": packs, "page_paths": ppath}


