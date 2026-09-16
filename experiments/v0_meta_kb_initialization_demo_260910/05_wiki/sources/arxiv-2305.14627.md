---
uid: wiki-page:source-51388aa8e2e8587f
title: Enabling Large Language Models to Generate Text with Citations
slug: sources/arxiv-2305.14627
page_type: source
status: review
summary: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:9a3b21da11a96956
- claim:bed2f056ecd73c69
source_refs: &id002
- arxiv:2305.14627
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-acf3f9a285c1d147
- wiki-page:evidence-12cbeb94dfbfbe21
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-acf3f9a285c1d147
  relation: evidenced_by
  claim_refs:
  - claim:9a3b21da11a96956
  notes: null
- target: wiki-page:evidence-12cbeb94dfbfbe21
  relation: evidenced_by
  claim_refs:
  - claim:bed2f056ecd73c69
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:bed2f056ecd73c69
  source_refs:
  - arxiv:2305.14627
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:9a3b21da11a96956
  source_refs:
  - arxiv:2305.14627
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9406f28f613dfbd5
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
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
  checked_at: '2026-09-13T17:38:21Z'
  max_age_days: 30
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence
      expansion.
    short: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence expansion.
    full: null
  estimated_tokens: 194
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Enabling Large Language Models to Generate Text with Citations

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2305.14627`
- Canonical ID: `2305.14627`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/normalized/document.txt`

## Source-reported candidate statements

- Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕

## Collection assessments

- ALCE provides reproducible citation-quality metrics across correctness, completeness, and fluency, directly applicable to wiki admission gates. 〔[claim:9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:9a3b21da11a96956` | `evidence:cff53a88da30fbec` | `local://raw_data/arxiv/Enabling Large Language Models to Generate Text with Citations/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:bed2f056ecd73c69` | `evidence:4527dd12000fe21f` | `local://materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/normalized/document.txt#L140-L143` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim 9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md) — `evidenced_by`
- [Claim bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md) — `evidenced_by`
