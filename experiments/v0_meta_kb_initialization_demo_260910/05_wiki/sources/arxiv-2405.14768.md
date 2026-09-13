---
uid: wiki-page:source-1fec3cb1e7f11c84
title: 'WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models'
slug: sources/arxiv-2405.14768
page_type: source
status: review
summary: 'Source page for WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models
  with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:37a1c59affa857e1
- claim:4e12d22ef2e755b9
source_refs: &id002
- arxiv:2405.14768
page_refs:
- wiki-page:map-knowledge-editing
- wiki-page:evidence-a448e75882dfd050
- wiki-page:evidence-8e4da1fb1bc5010b
outgoing_links:
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-a448e75882dfd050
  relation: evidenced_by
  claim_refs:
  - claim:37a1c59affa857e1
  notes: null
- target: wiki-page:evidence-8e4da1fb1bc5010b
  relation: evidenced_by
  claim_refs:
  - claim:4e12d22ef2e755b9
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:37a1c59affa857e1
  source_refs:
  - arxiv:2405.14768
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:4e12d22ef2e755b9
  source_refs:
  - arxiv:2405.14768
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
  - arxiv:2405.14768@sha256:60420a5c24efe0a4ea70983fb86ae62aaa3342d538d30e020d73efcf6d105ea5
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
    one_line: 'Source page for WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language
      Models with claim/evidence expansion.'
    short: 'Source page for WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models
      with claim/evidence expansion.'
    full: null
  estimated_tokens: 200
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2405.14768`
- Canonical ID: `2405.14768`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:60420a5c24efe0a4ea70983fb86ae62aaa3342d538d30e020d73efcf6d105ea5`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Local document: `materialized_sources/corpus/arxiv-2405.14768--80dba2af/normalized/document.txt`

## Source-reported candidate statements

- Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides in memories is a fundamental question for model editing. 〔[claim:37a1c59affa857e1](../claims/claim-37a1c59affa857e1.md)〕

## Collection assessments

- Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory and knowledge-sharding design. 〔[claim:4e12d22ef2e755b9](../claims/claim-4e12d22ef2e755b9.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:37a1c59affa857e1` | `evidence:d28db69c6cf6c420` | `local://materialized_sources/corpus/arxiv-2405.14768--80dba2af/normalized/document.txt#L137-L137` | `full_text` |
| `claim:4e12d22ef2e755b9` | `evidence:e0913f0daf8ec1e2` | `local://raw_data/arxiv/WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
- [Claim 37a1c59affa857e1](../claims/claim-37a1c59affa857e1.md) — `evidenced_by`
- [Claim 4e12d22ef2e755b9](../claims/claim-4e12d22ef2e755b9.md) — `evidenced_by`
