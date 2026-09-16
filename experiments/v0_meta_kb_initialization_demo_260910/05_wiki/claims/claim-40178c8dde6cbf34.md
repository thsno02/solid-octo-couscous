---
uid: wiki-page:evidence-2b2c67dbc05789e0
title: Claim 40178c8dde6cbf34
slug: claims/claim-40178c8dde6cbf34
page_type: evidence
status: review
summary: MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for governed
  knowledge editing.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:40178c8dde6cbf34
source_refs: &id001
- arxiv-2110.11309
page_refs:
- wiki-page:source-c707950005ce916a
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-c707950005ce916a
  relation: evidenced_by
  claim_refs:
  - claim:40178c8dde6cbf34
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:40178c8dde6cbf34
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:40178c8dde6cbf34
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:40178c8dde6cbf34
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:b04c61704bd4b7be
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2110.11309@sha256:e838a729a34c09a9044b334ef91e3c1ea36030b9e9e35ba6d6f11747e2b4b570
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
    one_line: MEND makes the update mechanism itself learnable and exposes generalization/locality requirements
      for governed knowledge editing.
    short: MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for
      governed knowledge editing.
    full: null
  estimated_tokens: 125
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:40178c8dde6cbf34
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for Fast Model Editing at Scale

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for governed knowledge editing.

## Scope

- Claim ID: `claim:40178c8dde6cbf34`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:402b8b7c9c3c6921` | `local://raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
