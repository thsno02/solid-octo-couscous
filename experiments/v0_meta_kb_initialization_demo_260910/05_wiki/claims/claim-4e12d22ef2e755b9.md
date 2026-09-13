---
uid: wiki-page:evidence-8e4da1fb1bc5010b
title: Claim 4e12d22ef2e755b9
slug: claims/claim-4e12d22ef2e755b9
page_type: evidence
status: review
summary: Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory
  and knowledge-sharding design.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:4e12d22ef2e755b9
source_refs: &id001
- arxiv:2405.14768
page_refs:
- wiki-page:source-1fec3cb1e7f11c84
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-1fec3cb1e7f11c84
  relation: evidenced_by
  claim_refs:
  - claim:4e12d22ef2e755b9
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:4e12d22ef2e755b9
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:4e12d22ef2e755b9
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:4e12d22ef2e755b9
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory
      and knowledge-sharding design.
    short: Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory
      and knowledge-sharding design.
    full: null
  estimated_tokens: 159
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Collection assessment for WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory and knowledge-sharding design.

## Scope

- Claim ID: `claim:4e12d22ef2e755b9`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:e0913f0daf8ec1e2` | `local://raw_data/arxiv/WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models/metadata.yaml#collection-inclusion-reason` | `raw_data/arxiv/WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](../sources/arxiv-2405.14768.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
