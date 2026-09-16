---
uid: wiki-page:source-f4f68942b55357ed
title: 'Zep: A Temporal Knowledge Graph Architecture for Agent Memory'
slug: sources/arxiv-2501.13956
page_type: source
status: review
summary: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:419c77c89a471f8e
- claim:ef04f2ebbd2da425
source_refs: &id002
- arxiv:2501.13956
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-7781d7df52d59b86
- wiki-page:evidence-410ef6d7fb5163de
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-7781d7df52d59b86
  relation: evidenced_by
  claim_refs:
  - claim:419c77c89a471f8e
  notes: null
- target: wiki-page:evidence-410ef6d7fb5163de
  relation: evidenced_by
  claim_refs:
  - claim:ef04f2ebbd2da425
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ef04f2ebbd2da425
  source_refs:
  - arxiv:2501.13956
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:419c77c89a471f8e
  source_refs:
  - arxiv:2501.13956
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:464b90323fe86f3e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence
      expansion.'
    short: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence expansion.'
    full: null
  estimated_tokens: 199
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Zep: A Temporal Knowledge Graph Architecture for Agent Memory

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2501.13956`
- Canonical ID: `2501.13956`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt`

## Source-reported candidate statements

- We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕

## Collection assessments

- A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships. 〔[claim:419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:419c77c89a471f8e` | `evidence:82efa10dc6344376` | `local://raw_data/arxiv/Zep: A Temporal Knowledge Graph Architecture for Agent Memory/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ef04f2ebbd2da425` | `evidence:420fd60b33cee2a7` | `local://materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt#L73-L73` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim 419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md) — `evidenced_by`
- [Claim ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md) — `evidenced_by`
