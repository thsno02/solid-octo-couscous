#!/usr/bin/env python3
"""Compile core synthesis pages, typed links, and the root index."""
from __future__ import annotations

from typing import Any

from llm_wiki_common import *


def build_core_pages(ctx: dict[str, Any], snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    sources = ctx["sources"]; claims = ctx["claims"]; srow = ctx["srow"]
    titles = ctx["titles"]; by_source = ctx["by_source"]
    claim_paths = ctx["claim_paths"]; source_paths = ctx["source_paths"]
    map_ids = ctx["map_ids"]; pages = ctx["pages"]
    defs = [
        ("overviews/llm-wiki.md", "wiki-page:llm-wiki-overview", "LLM Wiki overview", "overview", "Evidence-linked, review-gated knowledge compilation layer.", ["llm-wiki", "ontology-semantic-architecture", "governance-evaluation"]),
        ("collections/v0-corpus.md", "wiki-page:v0-corpus", "v0 knowledge self-evolution corpus", "collection", "Scope, coverage, and limits of the selected candidate corpus.", []),
        ("systems/reference-system.md", "wiki-page:llm-wiki-reference-system", "LLM Wiki reference system", "system", "End-to-end architecture from frozen sources to reviewed pages and context packs.", ["llm-wiki", "knowledge-memory", "ontology-semantic-architecture", "governance-evaluation"]),
        ("methods/grounded-synthesis.md", "wiki-page:grounded-long-form-synthesis", "Grounded long-form synthesis", "method", "Research-before-writing, outline-first compilation, citations, and factuality checks.", ["llm-wiki"]),
        ("methods/claim-evidence-page.md", "wiki-page:claim-evidence-page-compilation", "Claim–evidence–page compilation", "method", "Compile pages from atomic claims while preserving selectors and scope.", ["llm-wiki", "ontology-semantic-architecture", "governance-evaluation"]),
        ("methods/context-pack-routing.md", "wiki-page:context-pack-routing", "Context-pack routing", "method", "Bounded retrieval through maps, lexical search, graph expansion, and evidence expansion.", ["knowledge-memory", "llm-wiki", "ontology-semantic-architecture"]),
        ("concepts/epistemic-separation.md", "wiki-page:epistemic-separation", "Epistemic separation", "concept", "Keep source assertions, assessments, synthesis, and verification distinguishable.", []),
        ("concepts/source-specific-consumption.md", "wiki-page:source-specific-consumption", "Source-specific consumption", "concept", "Different source families require different frozen units and selectors.", []),
        ("concepts/knowledge-evolution-loop.md", "wiki-page:knowledge-evolution-loop", "Knowledge evolution loop", "concept", "Evidence, conflict, review, admission, monitoring, and rollback form one governed loop.", ["recursive-self-improvement", "open-ended-evolution", "governance-evaluation"]),
        ("concepts/freshness-versioning-rollback.md", "wiki-page:freshness-versioning-and-rollback", "Freshness, versioning, and rollback", "concept", "Page, claim, and source revisions evolve separately through dependency-aware rebuilds.", ["knowledge-memory", "ontology-semantic-architecture", "governance-evaluation"]),
        ("comparisons/wiki-rag-kg.md", "wiki-page:llm-wiki-vs-rag-vs-knowledge-graph", "LLM Wiki versus vector RAG versus knowledge graph", "comparison", "Compare admission, provenance, organization, freshness, and consumption.", ["knowledge-memory", "llm-wiki", "ontology-semantic-architecture"]),
        ("comparisons/paper-repository.md", "wiki-page:paper-vs-repository-consumption", "Paper versus repository consumption", "comparison", "TeX-first papers and commit-pinned repositories need different evidence paths.", []),
        ("debates/automation-editorial-review.md", "wiki-page:automation-vs-editorial-review", "Automation versus editorial review", "debate", "Automation accelerates research and writing but requires independent evidence and governance gates.", ["automated-research", "llm-wiki", "governance-evaluation"]),
        ("gaps/evidence-and-trust.md", "wiki-page:materialization-and-trust-gaps", "Materialization, evidence, and trust gaps", "gap", "Known limits in content tiers, extraction, contradiction analysis, replication, and trust.", ["governance-evaluation", "llm-wiki"]),
        ("evaluations/v0-quality-gates.md", "wiki-page:v0-quality-gates", "v0 LLM Wiki quality gates", "evaluation", "Structural, citation, organization, freshness, governance, and utility checks.", ["governance-evaluation", "llm-wiki"]),
        ("research_questions/knowledge-frontier.md", "wiki-page:knowledge-frontier", "Knowledge frontier", "research_question", "Open questions requiring more evidence, testing, conflict analysis, or editorial decisions.", []),
        ("maps/open-implementations.md", "wiki-page:map-open-implementations", "Open implementations", "map", "Commit-pinned repositories relevant to the LLM Wiki architecture.", []),
    ]
    core: dict[str, dict[str, Any]] = {}
    for path, uid, title, ptype, summary, ds in defs:
        selected = choose(claims, ds or None, 12); refs = unique(ref for item in selected for ref in srcs(item))
        if uid == "wiki-page:v0-corpus": refs = list(srow); selected = choose(claims, limit=12)
        if uid == "wiki-page:map-open-implementations":
            refs = [ref for ref, row in srow.items() if str(row.get("source_type")) == "github"]; selected = [c for c in claims if any(ref in refs for ref in srcs(c))]
        core[uid] = page(path, uid, title, ptype, summary); core[uid]["claims"] = [str(x["uid"]) for x in selected]; core[uid]["sources"] = refs
        core[uid]["sections"] = [{"heading": "Purpose", "claim_refs": [], "source_refs": refs, "editorial_intent": "State the page's editorial purpose."}, {"heading": "Candidate evidence", "claim_refs": core[uid]["claims"], "source_refs": refs, "editorial_intent": "Expose claim-backed signals without automatic admission."}, {"heading": "Review boundary", "claim_refs": [], "source_refs": refs, "editorial_intent": "Declare unresolved review work."}]
        core[uid]["body"] = f"""# {title}\n\n## Purpose\n\n{summary}\n\n## Candidate evidence\n\n{signals(selected, path, claim_paths, titles)}\n\n## Compiled interpretation\n\nThis page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.\n\n## Review boundary\n\nCheck evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication."""
        pages.append(core[uid])

    # Add substantive structures to key pages.
    core["wiki-page:llm-wiki-overview"]["body"] += f"\n\n## Current release\n\nThis candidate build covers **{len(sources)}** selected sources and **{len(claims)}** claims. Trusted claims remain **0**."
    core["wiki-page:llm-wiki-reference-system"]["body"] += "\n\n## Architecture\n\n```text\nimmutable source revisions\n→ normalized artifacts and selectors\n→ atomic claims and evidence\n→ identity and ontology mapping\n→ PagePlan and candidate Markdown\n→ deterministic and semantic evaluation\n→ review and admission\n→ indexes, graph, context packs, and change feed\n```"
    core["wiki-page:grounded-long-form-synthesis"]["body"] += "\n\n## Method\n\nDiscover perspectives, ask questions, retrieve evidence, create a hierarchical outline, check source/viewpoint coverage, then draft. Every factual paragraph must cite; disputed or high-risk statements expand to atomic evidence."
    core["wiki-page:claim-evidence-page-compilation"]["body"] += "\n\n## Compiler contract\n\nInputs are pinned source revisions, atomic claims, evidence selectors, schema/identity versions, policy, and bounded scope. Outputs are candidate pages, typed links, semantic diff, validation, review queue, and rollback."
    core["wiki-page:context-pack-routing"]["body"] += "\n\n## Routing\n\n```text\nquery + freshness need\n→ maps and lexical index\n→ graph expansion\n→ rerank by support, freshness, authority, task fit\n→ bounded context pack\n→ claim/source expansion when needed\n```"
    core["wiki-page:epistemic-separation"]["body"] += "\n\n## Required separation\n\nSource assertion ≠ collector assessment ≠ generated synthesis ≠ independently verified observation. The compiler retains those scopes in claims, sections, and review queues."
    core["wiki-page:source-specific-consumption"]["body"] += "\n\n## Frozen units\n\n| Source family | Frozen unit | Evidence surface | Still unproven |\n|---|---|---|---|\n| paper | archive/hash | TeX or normalized lines | correctness and replication |\n| repository | commit SHA | selected docs/config/code | runtime and benchmark behavior |\n| web/industry | response hash | reusable text or bounded excerpt | inaccessible/omitted content |"
    core["wiki-page:llm-wiki-vs-rag-vs-knowledge-graph"]["body"] += "\n\n## Comparison axes\n\n| Layer | Primary strength | Admission | Provenance | Human navigation |\n|---|---|---|---|---|\n| vector RAG | recall | usually none | chunk-level | weak |\n| knowledge graph | typed relations | implementation-dependent | edge/node-level | moderate |\n| LLM Wiki | governed synthesis | proposal/review/merge | page→claim→evidence | strong |"
    core["wiki-page:automation-vs-editorial-review"]["body"] += "\n\n## Preserved disagreement\n\nAutomation is useful for perspective discovery, extraction, planning, drafting, and linting. Independent review remains necessary for identity merges, contested claims, source retractions, policy-sensitive content, and trust promotion."
    summary = snapshot.get("corpus_summary") if isinstance(snapshot.get("corpus_summary"), dict) else {}
    core["wiki-page:materialization-and-trust-gaps"]["body"] += f"\n\n## Measured gaps\n\n- Corpus records: **{summary.get('records', len(sources))}**\n- Selected sources: **{len(sources)}**\n- Trusted scientific claims: **0**\n- Runtime-tested repositories in this build: **0**\n- Independently replicated paper claims in this build: **0**"
    core["wiki-page:v0-quality-gates"]["body"] += "\n\n## Blocking gates\n\n- valid source/claim/page references;\n- every evidence selector resolves locally;\n- no broken typed or Markdown links;\n- complete claim/source page coverage;\n- no orphan required pages;\n- deterministic manifest;\n- no automatic trusted promotion."
    core["wiki-page:knowledge-frontier"]["body"] += "\n\n## Open questions\n\n- Which source assertions survive independent entailment and replication checks?\n- Which apparent conflicts are true contradictions rather than scope/time differences?\n- What page split/merge decisions improve navigation?\n- Which runtime claims require executable evaluation?\n- What thresholds justify promotion beyond candidate status?"

    # Cross-link core pages and maps.
    links = {
        "wiki-page:llm-wiki-overview": [("wiki-page:llm-wiki-reference-system", "explains"), ("wiki-page:grounded-long-form-synthesis", "explains"), ("wiki-page:llm-wiki-vs-rag-vs-knowledge-graph", "compares_with"), ("wiki-page:materialization-and-trust-gaps", "depends_on")],
        "wiki-page:llm-wiki-reference-system": [("wiki-page:claim-evidence-page-compilation", "depends_on"), ("wiki-page:context-pack-routing", "depends_on"), ("wiki-page:freshness-versioning-and-rollback", "depends_on"), ("wiki-page:v0-quality-gates", "evaluates")],
        "wiki-page:grounded-long-form-synthesis": [(map_ids.get("llm-wiki"), "part_of"), ("wiki-page:epistemic-separation", "depends_on"), ("wiki-page:v0-quality-gates", "evaluates")],
        "wiki-page:claim-evidence-page-compilation": [("wiki-page:epistemic-separation", "depends_on"), ("wiki-page:source-specific-consumption", "depends_on")],
        "wiki-page:context-pack-routing": [(map_ids.get("knowledge-memory"), "depends_on"), ("wiki-page:llm-wiki-vs-rag-vs-knowledge-graph", "compares_with")],
        "wiki-page:knowledge-evolution-loop": [(map_ids.get("recursive-self-improvement"), "related"), (map_ids.get("open-ended-evolution"), "related"), ("wiki-page:freshness-versioning-and-rollback", "extends")],
        "wiki-page:automation-vs-editorial-review": [(map_ids.get("automated-research"), "related"), (map_ids.get("governance-evaluation"), "related"), ("wiki-page:v0-quality-gates", "evaluates")],
        "wiki-page:knowledge-frontier": [("wiki-page:materialization-and-trust-gaps", "extends"), ("wiki-page:v0-quality-gates", "depends_on")],
        "wiki-page:map-open-implementations": [("wiki-page:source-specific-consumption", "depends_on"), ("wiki-page:llm-wiki-reference-system", "related")],
    }
    all_ids = {p["uid"] for p in pages}
    for uid, values in links.items():
        for target, relation in values:
            if target and target in all_ids: add(core[uid], target, relation, core[uid]["claims"][:6])
    domain_targets = {
        "automated-research": ["wiki-page:automation-vs-editorial-review", "wiki-page:knowledge-evolution-loop"], "cross-cutting": ["wiki-page:llm-wiki-reference-system", "wiki-page:knowledge-frontier"], "governance-evaluation": ["wiki-page:v0-quality-gates", "wiki-page:automation-vs-editorial-review"], "knowledge-editing": ["wiki-page:knowledge-evolution-loop", "wiki-page:freshness-versioning-and-rollback"], "knowledge-memory": ["wiki-page:context-pack-routing", "wiki-page:llm-wiki-vs-rag-vs-knowledge-graph"], "llm-wiki": ["wiki-page:llm-wiki-overview", "wiki-page:grounded-long-form-synthesis"], "ontology-semantic-architecture": ["wiki-page:claim-evidence-page-compilation", "wiki-page:llm-wiki-reference-system"], "open-ended-evolution": ["wiki-page:knowledge-evolution-loop", "wiki-page:knowledge-frontier"], "recursive-self-improvement": ["wiki-page:knowledge-evolution-loop", "wiki-page:automation-vs-editorial-review"],
    }
    by_page = {p["uid"]: p for p in pages}
    for d, targets in domain_targets.items():
        if map_ids.get(d) not in by_page: continue
        for target in targets:
            if target in by_page: add(by_page[map_ids[d]], target, "related", by_page[map_ids[d]]["claims"][:6])

    index = page("index.md", "wiki-page:v0-meta-kb-index", "v0 LLM Wiki index", "map", "Root index for the evidence-linked, review-gated candidate release.")
    index["claims"] = [str(x["uid"]) for x in claims]; index["sources"] = list(srow)
    pages.append(index); by_page[index["uid"]] = index
    groups = [
        ("Start here", ["wiki-page:llm-wiki-overview", "wiki-page:v0-corpus", "wiki-page:llm-wiki-reference-system"]),
        ("Methods", ["wiki-page:grounded-long-form-synthesis", "wiki-page:claim-evidence-page-compilation", "wiki-page:context-pack-routing"]),
        ("Concepts", ["wiki-page:epistemic-separation", "wiki-page:source-specific-consumption", "wiki-page:knowledge-evolution-loop", "wiki-page:freshness-versioning-and-rollback"]),
        ("Comparisons and debate", ["wiki-page:llm-wiki-vs-rag-vs-knowledge-graph", "wiki-page:paper-vs-repository-consumption", "wiki-page:automation-vs-editorial-review"]),
        ("Quality and frontier", ["wiki-page:v0-quality-gates", "wiki-page:materialization-and-trust-gaps", "wiki-page:knowledge-frontier"]),
    ]
    body = ["# v0 LLM Wiki", "", "> Candidate release. Pages are derived views; no scientific claim is automatically trusted.", ""]
    for heading, ids in groups:
        body += [f"## {heading}", ""]
        for uid in ids:
            p = by_page[uid]; body.append(f"- {link('index.md', p['path'], p['title'])} — {p['summary']}"); add(index, uid, "explains", p["claims"][:6])
        body.append("")
    body += ["## Maps of content", ""]
    for p in sorted([x for x in pages if x["type"] == "map" and x["uid"] != index["uid"]], key=lambda x: x["title"]):
        body.append(f"- {link('index.md', p['path'], p['title'])} — {p['summary']}"); add(index, p["uid"], "explains", p["claims"][:6])
    body += ["", "## Atomic expansion", "", f"- **{len(sources)}** source pages", f"- **{len(claims)}** claim/evidence pages", "- Machine catalogs, graph, lexical index, context packs, change proposal, and review queues"]
    index["body"] = "\n".join(body); index["sections"] = [{"heading": "Start here", "claim_refs": [], "source_refs": [], "editorial_intent": "Route to the core architecture."}, {"heading": "Maps of content", "claim_refs": [], "source_refs": list(srow), "editorial_intent": "Route by stable domain questions."}, {"heading": "Atomic expansion", "claim_refs": [], "source_refs": list(srow), "editorial_intent": "Expose source and claim expansion surfaces."}]

    # Append readable related links after all paths are known.
    paths = {p["uid"]: p["path"] for p in pages}; titles_by_page = {p["uid"]: p["title"] for p in pages}
    for p in pages:
        if p["uid"] == index["uid"] or not p["outgoing"]: continue
        related = [f"- {link(p['path'], paths[x['target']], titles_by_page[x['target']])} — `{x['relation']}`" for x in p["outgoing"] if x["target"] in paths]
        if related: p["body"] = p["body"].rstrip() + "\n\n## Related pages\n\n" + "\n".join(related)
    return pages
