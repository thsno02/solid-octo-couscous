---
uid: wiki-page:evidence-410ef6d7fb5163de
title: Claim ef04f2ebbd2da425
slug: claims/claim-ef04f2ebbd2da425
page_type: evidence
status: review
summary: 'We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art
  system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and '
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:ef04f2ebbd2da425
source_refs: &id001
- arxiv:2501.13956
page_refs:
- wiki-page:source-f4f68942b55357ed
- wiki-page:map-knowledge-memory
outgoing_links:
- target: wiki-page:source-f4f68942b55357ed
  relation: evidenced_by
  claim_refs:
  - claim:ef04f2ebbd2da425
  notes: null
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs:
  - claim:ef04f2ebbd2da425
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:ef04f2ebbd2da425
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:ef04f2ebbd2da425
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
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
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
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
    one_line: 'We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art
      system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive
      and '
    short: 'We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art
      system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive
      and '
    full: null
  estimated_tokens: 149
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from Zep: A Temporal Knowledge Graph Architecture for Agent Memory

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases.

## Scope

- Claim ID: `claim:ef04f2ebbd2da425`
- Scope: `source-reported assertion`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:420fd60b33cee2a7` | `local://materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt#L73-L73` | `materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) — `evidenced_by`
- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
