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
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:419c77c89a471f8e
- claim:633b28ce5aca37bd
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:d13d2fd07c92af58
- claim:d6556415105fc41e
- claim:ef04f2ebbd2da425
- claim:f5d2f5be4a498ca2
source_refs: &id001
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv:2501.13956
- arxiv-2306.15626
- github:getzep/graphiti
page_refs:
- wiki-page:source-81e58c8add4ce203
- wiki-page:source-644f51e7e354fe05
- wiki-page:source-f4f68942b55357ed
- wiki-page:source-5be112b896547169
- wiki-page:source-2672a50bc210b0f4
- wiki-page:context-pack-routing
- wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
outgoing_links:
- target: wiki-page:source-81e58c8add4ce203
  relation: explains
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:f5d2f5be4a498ca2
  notes: null
- target: wiki-page:source-644f51e7e354fe05
  relation: explains
  claim_refs:
  - claim:12237a4df4847d59
  - claim:633b28ce5aca37bd
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
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  notes: null
- target: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
  relation: related
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  - claim:ef04f2ebbd2da425
  source_refs:
  - arxiv:2503.18102
  - arxiv-1706.08840
  - arxiv-2306.15626
  - github:getzep/graphiti
  - arxiv:2501.13956
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:d13d2fd07c92af58
  - claim:d6556415105fc41e
  - claim:f5d2f5be4a498ca2
  source_refs:
  - arxiv:2501.13956
  - arxiv-1706.08840
  - arxiv-2306.15626
  - github:getzep/graphiti
  - arxiv:2503.18102
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:7709fc4901bbe1d3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
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
    one_line: Routing map for knowledge memory sources, questions, and claims.
    short: Routing map for knowledge memory sources, questions, and claims.
    full: null
  estimated_tokens: 585
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
| [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) | `arxiv` | `full_text` | 2 |
| [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) | `arxiv` | `full_text` | 2 |
| [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) | `arxiv` | `full_text` | 2 |
| [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) | `arxiv` | `full_text` | 2 |
| [getzep/graphiti](../sources/github-getzep-graphiti.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕

## Collector assessments

- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (collection assessment): A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships. 〔[claim:419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md)〕
- **Gradient Episodic Memory for Continual Learning** (collection assessment): Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates. 〔[claim:633b28ce5aca37bd](../claims/claim-633b28ce5aca37bd.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (collection assessment): Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents. 〔[claim:d13d2fd07c92af58](../claims/claim-d13d2fd07c92af58.md)〕
- **getzep/graphiti** (collection assessment): Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history. 〔[claim:d6556415105fc41e](../claims/claim-d6556415105fc41e.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (collection assessment): A direct bridge between autonomous research and knowledge self-evolution: agent laboratories upload, retrieve and build on each others research, creating cumulative improvement across generations of work. 〔[claim:f5d2f5be4a498ca2](../claims/claim-f5d2f5be4a498ca2.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) — `explains`
- [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) — `explains`
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) — `explains`
- [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) — `explains`
- [getzep/graphiti](../sources/github-getzep-graphiti.md) — `explains`
- [Context-pack routing](../methods/context-pack-routing.md) — `related`
- [LLM Wiki versus vector RAG versus knowledge graph](../comparisons/wiki-rag-kg.md) — `related`
