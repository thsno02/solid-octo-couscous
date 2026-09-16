---
uid: wiki-page:evidence-c0a3f9f9a75f6453
title: Claim 633b28ce5aca37bd
slug: claims/claim-633b28ce5aca37bd
page_type: evidence
status: review
summary: Connects memory retention to constrained updates and positive backward transfer, directly informing governed
  knowledge updates.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:633b28ce5aca37bd
source_refs: &id001
- arxiv-1706.08840
page_refs:
- wiki-page:source-644f51e7e354fe05
- wiki-page:map-knowledge-memory
outgoing_links:
- target: wiki-page:source-644f51e7e354fe05
  relation: evidenced_by
  claim_refs:
  - claim:633b28ce5aca37bd
  notes: null
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs:
  - claim:633b28ce5aca37bd
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:633b28ce5aca37bd
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:633b28ce5aca37bd
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:096e2cb4557cf60c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
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
    one_line: Connects memory retention to constrained updates and positive backward transfer, directly informing
      governed knowledge updates.
    short: Connects memory retention to constrained updates and positive backward transfer, directly informing governed
      knowledge updates.
    full: null
  estimated_tokens: 129
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:633b28ce5aca37bd
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Gradient Episodic Memory for Continual Learning

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates.

## Scope

- Claim ID: `claim:633b28ce5aca37bd`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:68121f105d3012a3` | `local://raw_data/arxiv/Gradient Episodic Memory for Continual Learning/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Gradient Episodic Memory for Continual Learning/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) — `evidenced_by`
- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
