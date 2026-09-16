---
uid: wiki-page:map-open-implementations
title: Open implementations
slug: maps/open-implementations
page_type: map
status: review
summary: Commit-pinned repositories relevant to the LLM Wiki architecture.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:d38b49dc4376d4b0
- claim:1b6ae1229c17cacd
- claim:334565c7ebb30cb5
- claim:21bdaa7b130a7cc4
- claim:bc85c4d0c6801c3a
- claim:d6556415105fc41e
- claim:e7ac7da9ac39e47d
- claim:c4f2def09ea56d98
- claim:fc57f26307cefee3
- claim:3adb88340e0eb2b6
- claim:e7026275c099e7e2
- claim:714e301e8b2162bc
source_refs: &id001
- github:jennyzzt/dgm
- github:SakanaAI/AI-Scientist
- github:getzep/graphiti
- github:xoai/sage-wiki
- github:linkml/linkml
- github:VectifyAI/OpenKB
page_refs:
- wiki-page:source-specific-consumption
- wiki-page:llm-wiki-reference-system
outgoing_links:
- target: wiki-page:source-specific-consumption
  relation: depends_on
  claim_refs:
  - claim:d38b49dc4376d4b0
  - claim:1b6ae1229c17cacd
  - claim:334565c7ebb30cb5
  - claim:21bdaa7b130a7cc4
  - claim:bc85c4d0c6801c3a
  - claim:d6556415105fc41e
  notes: null
- target: wiki-page:llm-wiki-reference-system
  relation: related
  claim_refs:
  - claim:d38b49dc4376d4b0
  - claim:1b6ae1229c17cacd
  - claim:334565c7ebb30cb5
  - claim:21bdaa7b130a7cc4
  - claim:bc85c4d0c6801c3a
  - claim:d6556415105fc41e
  notes: null
sections:
- heading: Purpose
  claim_refs: []
  source_refs: *id001
  editorial_intent: State the page's editorial purpose.
- heading: Candidate evidence
  claim_refs: *id002
  source_refs: *id001
  editorial_intent: Expose claim-backed signals without automatic admission.
- heading: Review boundary
  claim_refs: []
  source_refs: *id001
  editorial_intent: Declare unresolved review work.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:052e92babb00da4b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  manual_edits_preserved: false
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific, semantic, neutrality, and due-weight review remain required before publication.
freshness:
  status: fresh
  checked_at: '2026-09-16T04:30:26Z'
  max_age_days: 30
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Commit-pinned repositories relevant to the LLM Wiki architecture.
    short: Commit-pinned repositories relevant to the LLM Wiki architecture.
    full: null
  estimated_tokens: 728
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:d38b49dc4376d4b0
- claim:1b6ae1229c17cacd
- claim:334565c7ebb30cb5
- claim:21bdaa7b130a7cc4
- claim:bc85c4d0c6801c3a
- claim:d6556415105fc41e
- claim:e7ac7da9ac39e47d
- claim:c4f2def09ea56d98
- claim:fc57f26307cefee3
- claim:3adb88340e0eb2b6
- claim:e7026275c099e7e2
- claim:714e301e8b2162bc
rights_refs: []
rights_unavailable_source_refs:
- github:SakanaAI/AI-Scientist
- github:VectifyAI/OpenKB
- github:getzep/graphiti
- github:jennyzzt/dgm
- github:linkml/linkml
- github:xoai/sage-wiki
---

# Open implementations

## Purpose

Commit-pinned repositories relevant to the LLM Wiki architecture.

## Candidate evidence

- **jennyzzt/dgm** (source assertion): Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. 〔[claim:d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md)〕
- **jennyzzt/dgm** (collection assessment): One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage. 〔[claim:1b6ae1229c17cacd](../claims/claim-1b6ae1229c17cacd.md)〕
- **SakanaAI/AI-Scientist** (source assertion): One of the grand challenges of artificial intelligence is developing agents capable of conducting scientific research and discovering new knowledge. 〔[claim:334565c7ebb30cb5](../claims/claim-334565c7ebb30cb5.md)〕
- **SakanaAI/AI-Scientist** (collection assessment): Canonical open implementation of an end-to-end automated research loop where research artifacts become inputs to subsequent iterations. 〔[claim:21bdaa7b130a7cc4](../claims/claim-21bdaa7b130a7cc4.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **getzep/graphiti** (collection assessment): Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history. 〔[claim:d6556415105fc41e](../claims/claim-d6556415105fc41e.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **xoai/sage-wiki** (collection assessment): A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated entity resolution, output quarantine and agent access through MCP. 〔[claim:c4f2def09ea56d98](../claims/claim-c4f2def09ea56d98.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕
- **linkml/linkml** (collection assessment): Modern schema-first bridge between developer data models and linked-data/ontology artifacts. 〔[claim:3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **VectifyAI/OpenKB** (collection assessment): A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Related pages

- [Source-specific consumption](../concepts/source-specific-consumption.md) — `depends_on`
- [LLM Wiki reference system](../systems/reference-system.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### SakanaAI/AI-Scientist (`github:SakanaAI/AI-Scientist`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
