---
uid: wiki-page:evidence-11f3f7762e882a4a
title: Claim e7ac7da9ac39e47d
slug: claims/claim-e7ac7da9ac39e47d
page_type: evidence
status: review
summary: '- Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki
  - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static reposito'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:e7ac7da9ac39e47d
source_refs: &id001
- github:xoai/sage-wiki
page_refs:
- wiki-page:source-a41aba6e720b278f
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-a41aba6e720b278f
  relation: evidenced_by
  claim_refs:
  - claim:e7ac7da9ac39e47d
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:e7ac7da9ac39e47d
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:e7ac7da9ac39e47d
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:e7ac7da9ac39e47d
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: '- Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki
      - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static reposito'
    short: '- Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki
      - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static reposito'
    full: null
  estimated_tokens: 122
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from xoai/sage-wiki

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

- Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## Scope

- Claim ID: `claim:e7ac7da9ac39e47d`
- Scope: `source-reported assertion`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:27bcae6d97e234f4` | `local://materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/document.md#L3-L6` | `materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/document.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [xoai/sage-wiki](../sources/github-xoai-sage-wiki.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
