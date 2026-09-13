---
uid: wiki-page:source-a41aba6e720b278f
title: xoai/sage-wiki
slug: sources/github-xoai-sage-wiki
page_type: source
status: review
summary: Source page for xoai/sage-wiki with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:c4f2def09ea56d98
- claim:e7ac7da9ac39e47d
source_refs: &id002
- github:xoai/sage-wiki
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-9c76bfd457bcf341
- wiki-page:evidence-11f3f7762e882a4a
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-9c76bfd457bcf341
  relation: evidenced_by
  claim_refs:
  - claim:c4f2def09ea56d98
  notes: null
- target: wiki-page:evidence-11f3f7762e882a4a
  relation: evidenced_by
  claim_refs:
  - claim:e7ac7da9ac39e47d
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:e7ac7da9ac39e47d
  source_refs:
  - github:xoai/sage-wiki
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:c4f2def09ea56d98
  source_refs:
  - github:xoai/sage-wiki
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
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: Source page for xoai/sage-wiki with claim/evidence expansion.
    short: Source page for xoai/sage-wiki with claim/evidence expansion.
    full: null
  estimated_tokens: 173
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# xoai/sage-wiki

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:xoai/sage-wiki`
- Canonical ID: `xoai/sage-wiki`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `ab36031ace701fb1e3c620323d138a90a450f48d`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/document.md`

## Source-reported candidate statements

- - Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕

## Collection assessments

- A graph-aware compiled wiki emphasizing evidenced relations, source spans, bi-temporal edges, review-gated entity resolution, output quarantine and agent access through MCP. 〔[claim:c4f2def09ea56d98](../claims/claim-c4f2def09ea56d98.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:c4f2def09ea56d98` | `evidence:c7abfedf00195f99` | `local://raw_data/githubs/xoai--sage-wiki/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:e7ac7da9ac39e47d` | `evidence:27bcae6d97e234f4` | `local://materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/document.md#L3-L6` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim c4f2def09ea56d98](../claims/claim-c4f2def09ea56d98.md) — `evidenced_by`
- [Claim e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md) — `evidenced_by`
