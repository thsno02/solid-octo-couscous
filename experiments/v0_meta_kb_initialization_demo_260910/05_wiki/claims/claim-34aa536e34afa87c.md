---
uid: wiki-page:evidence-d59b262288fdbed0
title: Claim 34aa536e34afa87c
slug: claims/claim-34aa536e34afa87c
page_type: evidence
status: review
summary: A self-correcting multi-agent architecture that converts scientific instructions into executable experimental
  protocols and validates/corrects them before hardware execution.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:34aa536e34afa87c
source_refs: &id001
- arxiv:2509.25651
page_refs:
- wiki-page:source-5b06dbb06d02d1f5
- wiki-page:map-cross-cutting
outgoing_links:
- target: wiki-page:source-5b06dbb06d02d1f5
  relation: evidenced_by
  claim_refs:
  - claim:34aa536e34afa87c
  notes: null
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs:
  - claim:34aa536e34afa87c
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:34aa536e34afa87c
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:34aa536e34afa87c
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:c01527f77acde651
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2509.25651@sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803
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
    one_line: A self-correcting multi-agent architecture that converts scientific instructions into executable experimental
      protocols and validates/corrects them before hardware execution.
    short: A self-correcting multi-agent architecture that converts scientific instructions into executable experimental
      protocols and validates/corrects them before hardware execution.
    full: null
  estimated_tokens: 148
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:34aa536e34afa87c
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A self-correcting multi-agent architecture that converts scientific instructions into executable experimental protocols and validates/corrects them before hardware execution.

## Scope

- Claim ID: `claim:34aa536e34afa87c`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:51eb00707ccc813c` | `local://raw_data/arxiv/AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation](../sources/arxiv-2509.25651.md) — `evidenced_by`
- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
