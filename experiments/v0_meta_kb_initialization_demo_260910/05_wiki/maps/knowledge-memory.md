---
uid: wiki-page:map-knowledge-memory
title: Knowledge Memory
slug: maps/knowledge-memory
page_type: map
status: review
summary: Candidate map of knowledge memory sources and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:ef04f2ebbd2da425
- claim:419c77c89a471f8e
- claim:bc85c4d0c6801c3a
- claim:d6556415105fc41e
- claim:12237a4df4847d59
- claim:633b28ce5aca37bd
- claim:a67432ee7afb1535
- claim:d13d2fd07c92af58
- claim:3cc1779eadd83a8c
- claim:998499c6fa41effe
source_refs: &id001
- arxiv-1706.08840
- arxiv-2306.15626
- arxiv:2410.05779
- arxiv:2501.13956
- github:getzep/graphiti
page_refs: []
outgoing_links: []
sections: []
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:v0-meta-kb-260910:88936dc16ae2c769
  generated_by_agent: agent:deterministic-v0-builder
  generated_by_model: null
  prompt_or_skill_version: deterministic-v0.1
  compiled_from_revisions: *id001
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific and semantic review required before publication.
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
    one_line: Candidate map of knowledge memory sources and claims.
    short: Candidate map of knowledge memory sources and claims.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# Knowledge Memory

This map is compiled from candidate source assertions and collection assessments.

## `claim:ef04f2ebbd2da425`

**Scope:** source-reported assertion

We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases.

## `claim:419c77c89a471f8e`

**Scope:** collector assessment, not source-authored scientific fact

A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships.

## `claim:bc85c4d0c6801c3a`

**Scope:** source-reported assertion

- Commit: `c035afb7990b6077331a81e98b04efcfd9bf8184` - Default branch: `main` - Description: getzep/graphiti - Selected evidence files: 8 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## `claim:d6556415105fc41e`

**Scope:** collector assessment, not source-authored scientific fact

Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history.

## `claim:12237a4df4847d59`

**Scope:** source-reported assertion

One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks.

## `claim:633b28ce5aca37bd`

**Scope:** collector assessment, not source-authored scientific fact

Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates.

## `claim:a67432ee7afb1535`

**Scope:** source-reported assertion

Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements.

## `claim:d13d2fd07c92af58`

**Scope:** collector assessment, not source-authored scientific fact

Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents.

## `claim:3cc1779eadd83a8c`

**Scope:** source-reported assertion

Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex inter-dependencies.

## `claim:998499c6fa41effe`

**Scope:** collector assessment, not source-authored scientific fact

Introduces graph-based indexing plus an incremental update algorithm for timely integration of new data; directly relevant to an evolving external knowledge base.
