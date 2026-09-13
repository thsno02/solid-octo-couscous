---
uid: wiki-page:map-knowledge-memory
title: Knowledge Memory
slug: maps/knowledge-memory
page_type: map
status: review
summary: Routing map for knowledge memory sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:12237a4df4847d59
- claim:3cc1779eadd83a8c
- claim:419c77c89a471f8e
- claim:633b28ce5aca37bd
- claim:998499c6fa41effe
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:d13d2fd07c92af58
- claim:d6556415105fc41e
- claim:ef04f2ebbd2da425
source_refs: &id001
- arxiv-1706.08840
- arxiv:2410.05779
- arxiv:2501.13956
- arxiv-2306.15626
- github:getzep/graphiti
page_refs:
- wiki-page:source-644f51e7e354fe05
- wiki-page:source-5813488b61b511ca
- wiki-page:source-f4f68942b55357ed
- wiki-page:source-5be112b896547169
- wiki-page:source-2672a50bc210b0f4
- wiki-page:context-pack-routing
- wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
outgoing_links:
- target: wiki-page:source-644f51e7e354fe05
  relation: explains
  claim_refs:
  - claim:12237a4df4847d59
  - claim:633b28ce5aca37bd
  notes: null
- target: wiki-page:source-5813488b61b511ca
  relation: explains
  claim_refs:
  - claim:3cc1779eadd83a8c
  - claim:998499c6fa41effe
  notes: null
- target: wiki-page:source-f4f68942b55357ed
  relation: explains
  claim_refs:
  - claim:ef04f2ebbd2da425
  - claim:419c77c89a471f8e
  notes: null
- target: wiki-page:source-5be112b896547169
  relation: explains
  claim_refs:
  - claim:a67432ee7afb1535
  - claim:d13d2fd07c92af58
  notes: null
- target: wiki-page:source-2672a50bc210b0f4
  relation: explains
  claim_refs:
  - claim:bc85c4d0c6801c3a
  - claim:d6556415105fc41e
  notes: null
- target: wiki-page:context-pack-routing
  relation: related
  claim_refs:
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:998499c6fa41effe
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
  relation: related
  claim_refs:
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:998499c6fa41effe
  - claim:a67432ee7afb1535
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  - claim:ef04f2ebbd2da425
  source_refs:
  - arxiv-1706.08840
  - arxiv:2410.05779
  - arxiv-2306.15626
  - github:getzep/graphiti
  - arxiv:2501.13956
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:998499c6fa41effe
  - claim:d13d2fd07c92af58
  - claim:d6556415105fc41e
  source_refs:
  - arxiv:2501.13956
  - arxiv-1706.08840
  - arxiv:2410.05779
  - arxiv-2306.15626
  - github:getzep/graphiti
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:llm-wiki-v0:196d848b07caf422
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv:2410.05779@sha256:6f60088ffe7b1735ac670bfd67e7230ccfb2724bbabb7471db9854feac4733a7
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific, semantic, neutrality, and due-weight review remain required before publication.
freshness:
  status: fresh
  checked_at: '2026-09-13T17:43:07Z'
  max_age_days: 30
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Routing map for knowledge memory sources, questions, and claims.
    short: Routing map for knowledge memory sources, questions, and claims.
    full: null
  estimated_tokens: 606
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Knowledge Memory

Persistent memory, retrieval, graph organization, and temporal context.

## Routing questions

- What is stored and versioned?
- How are lexical, graph, and vector retrieval combined?
- How are freshness and provenance exposed?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) | `arxiv` | `full_text` | 2 |
| [LightRAG: Simple and Fast Retrieval-Augmented Generation](../sources/arxiv-2410.05779.md) | `arxiv` | `full_text` | 2 |
| [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) | `arxiv` | `full_text` | 2 |
| [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) | `arxiv` | `full_text` | 2 |
| [getzep/graphiti](../sources/github-getzep-graphiti.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LightRAG: Simple and Fast Retrieval-Augmented Generation** (source assertion): Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex i 〔[claim:3cc1779eadd83a8c](../claims/claim-3cc1779eadd83a8c.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): - Commit: `c035afb7990b6077331a81e98b04efcfd9bf8184` - Default branch: `main` - Description: getzep/graphiti - Selected evidence files: 8 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕

## Collector assessments

- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (collection assessment): A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships. 〔[claim:419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md)〕
- **Gradient Episodic Memory for Continual Learning** (collection assessment): Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates. 〔[claim:633b28ce5aca37bd](../claims/claim-633b28ce5aca37bd.md)〕
- **LightRAG: Simple and Fast Retrieval-Augmented Generation** (collection assessment): Introduces graph-based indexing plus an incremental update algorithm for timely integration of new data; directly relevant to an evolving external knowledge base. 〔[claim:998499c6fa41effe](../claims/claim-998499c6fa41effe.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (collection assessment): Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents. 〔[claim:d13d2fd07c92af58](../claims/claim-d13d2fd07c92af58.md)〕
- **getzep/graphiti** (collection assessment): Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history. 〔[claim:d6556415105fc41e](../claims/claim-d6556415105fc41e.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) — `explains`
- [LightRAG: Simple and Fast Retrieval-Augmented Generation](../sources/arxiv-2410.05779.md) — `explains`
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) — `explains`
- [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) — `explains`
- [getzep/graphiti](../sources/github-getzep-graphiti.md) — `explains`
- [Context-pack routing](../methods/context-pack-routing.md) — `related`
- [LLM Wiki versus vector RAG versus knowledge graph](../comparisons/wiki-rag-kg.md) — `related`
