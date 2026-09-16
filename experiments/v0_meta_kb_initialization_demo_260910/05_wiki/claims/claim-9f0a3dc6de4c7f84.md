---
uid: wiki-page:evidence-5e75e0811c5a35ff
title: Claim 9f0a3dc6de4c7f84
slug: claims/claim-9f0a3dc6de4c7f84
page_type: evidence
status: review
summary: Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki pages
  rather than judging a page as one block.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:9f0a3dc6de4c7f84
source_refs: &id001
- arxiv:2305.14251
page_refs:
- wiki-page:source-dd60addc5fe69a87
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-dd60addc5fe69a87
  relation: evidenced_by
  claim_refs:
  - claim:9f0a3dc6de4c7f84
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:9f0a3dc6de4c7f84
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:9f0a3dc6de4c7f84
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:9f0a3dc6de4c7f84
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
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
    one_line: Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki
      pages rather than judging a page as one block.
    short: Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki pages
      rather than judging a page as one block.
    full: null
  estimated_tokens: 160
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:9f0a3dc6de4c7f84
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Supplies an atomic-fact evaluation primitive needed to assess factual precision of long-form wiki pages rather than judging a page as one block.

## Scope

- Claim ID: `claim:9f0a3dc6de4c7f84`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:2e4d8e4355522153` | `local://raw_data/arxiv/FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](../sources/arxiv-2305.14251.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
