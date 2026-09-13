---
uid: wiki-page:source-332922100755365f
title: VectifyAI/OpenKB
slug: sources/github-vectifyai-openkb
page_type: source
status: review
summary: Source page for VectifyAI/OpenKB with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:714e301e8b2162bc
- claim:e7026275c099e7e2
source_refs: &id002
- github:VectifyAI/OpenKB
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-ae02e6dd19d86e7a
- wiki-page:evidence-2c4497b2c6a0f960
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-ae02e6dd19d86e7a
  relation: evidenced_by
  claim_refs:
  - claim:714e301e8b2162bc
  notes: null
- target: wiki-page:evidence-2c4497b2c6a0f960
  relation: evidenced_by
  claim_refs:
  - claim:e7026275c099e7e2
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:e7026275c099e7e2
  source_refs:
  - github:VectifyAI/OpenKB
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:714e301e8b2162bc
  source_refs:
  - github:VectifyAI/OpenKB
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
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
    one_line: Source page for VectifyAI/OpenKB with claim/evidence expansion.
    short: Source page for VectifyAI/OpenKB with claim/evidence expansion.
    full: null
  estimated_tokens: 172
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# VectifyAI/OpenKB

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:VectifyAI/OpenKB`
- Canonical ID: `VectifyAI/OpenKB`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `ff54396e575ee6feb0113b631a34caa082b441cc`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/github-VectifyAI-OpenKB--fd455ce8/document.md`

## Source-reported candidate statements

- - Commit: `ff54396e575ee6feb0113b631a34caa082b441cc` - Default branch: `main` - Description: VectifyAI/OpenKB - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕

## Collection assessments

- A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:714e301e8b2162bc` | `evidence:4458920402fcefd8` | `local://raw_data/githubs/VectifyAI--OpenKB/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:e7026275c099e7e2` | `evidence:314e31b69b572671` | `local://materialized_sources/corpus/github-VectifyAI-OpenKB--fd455ce8/document.md#L3-L6` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md) — `evidenced_by`
- [Claim e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md) — `evidenced_by`
