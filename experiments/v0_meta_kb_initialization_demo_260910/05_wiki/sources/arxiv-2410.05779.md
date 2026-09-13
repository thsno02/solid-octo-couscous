---
uid: wiki-page:source-5813488b61b511ca
title: 'LightRAG: Simple and Fast Retrieval-Augmented Generation'
slug: sources/arxiv-2410.05779
page_type: source
status: review
summary: 'Source page for LightRAG: Simple and Fast Retrieval-Augmented Generation with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:3cc1779eadd83a8c
- claim:998499c6fa41effe
source_refs: &id002
- arxiv:2410.05779
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-9fa3d5cb64e9e047
- wiki-page:evidence-4c38ccf79b6beb65
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-9fa3d5cb64e9e047
  relation: evidenced_by
  claim_refs:
  - claim:3cc1779eadd83a8c
  notes: null
- target: wiki-page:evidence-4c38ccf79b6beb65
  relation: evidenced_by
  claim_refs:
  - claim:998499c6fa41effe
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:3cc1779eadd83a8c
  source_refs:
  - arxiv:2410.05779
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:998499c6fa41effe
  source_refs:
  - arxiv:2410.05779
  editorial_intent: Keep collector interpretation separate.
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
  - arxiv:2410.05779@sha256:6f60088ffe7b1735ac670bfd67e7230ccfb2724bbabb7471db9854feac4733a7
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for LightRAG: Simple and Fast Retrieval-Augmented Generation with claim/evidence expansion.'
    short: 'Source page for LightRAG: Simple and Fast Retrieval-Augmented Generation with claim/evidence expansion.'
    full: null
  estimated_tokens: 206
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LightRAG: Simple and Fast Retrieval-Augmented Generation

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2410.05779`
- Canonical ID: `2410.05779`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:6f60088ffe7b1735ac670bfd67e7230ccfb2724bbabb7471db9854feac4733a7`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-2410.05779--5b53b22b/normalized/document.txt`

## Source-reported candidate statements

- Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex i 〔[claim:3cc1779eadd83a8c](../claims/claim-3cc1779eadd83a8c.md)〕

## Collection assessments

- Introduces graph-based indexing plus an incremental update algorithm for timely integration of new data; directly relevant to an evolving external knowledge base. 〔[claim:998499c6fa41effe](../claims/claim-998499c6fa41effe.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:3cc1779eadd83a8c` | `evidence:747a176e71d84297` | `local://materialized_sources/corpus/arxiv-2410.05779--5b53b22b/normalized/document.txt#L85-L85` | `full_text` |
| `claim:998499c6fa41effe` | `evidence:818da658f6f6089d` | `local://raw_data/arxiv/LightRAG: Simple and Fast Retrieval-Augmented Generation/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim 3cc1779eadd83a8c](../claims/claim-3cc1779eadd83a8c.md) — `evidenced_by`
- [Claim 998499c6fa41effe](../claims/claim-998499c6fa41effe.md) — `evidenced_by`
