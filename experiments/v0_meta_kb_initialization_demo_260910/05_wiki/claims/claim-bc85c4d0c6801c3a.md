---
uid: wiki-page:evidence-db6f515f9effd011
title: Claim bc85c4d0c6801c3a
slug: claims/claim-bc85c4d0c6801c3a
page_type: evidence
status: review
summary: ⭐ *Help us reach more developers and grow the Graphiti community.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:bc85c4d0c6801c3a
source_refs: &id001
- github:getzep/graphiti
page_refs:
- wiki-page:source-2672a50bc210b0f4
- wiki-page:map-knowledge-memory
outgoing_links:
- target: wiki-page:source-2672a50bc210b0f4
  relation: evidenced_by
  claim_refs:
  - claim:bc85c4d0c6801c3a
  notes: null
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs:
  - claim:bc85c4d0c6801c3a
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:bc85c4d0c6801c3a
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:bc85c4d0c6801c3a
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:7709fc4901bbe1d3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
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
    one_line: ⭐ *Help us reach more developers and grow the Graphiti community.
    short: ⭐ *Help us reach more developers and grow the Graphiti community.
    full: null
  estimated_tokens: 101
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from getzep/graphiti

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

⭐ *Help us reach more developers and grow the Graphiti community.

## Scope

- Claim ID: `claim:bc85c4d0c6801c3a`
- Scope: `source-reported assertion`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:2d2d6e2c4b39b026` | `local://materialized_sources/corpus/github-getzep-graphiti--e9af10ca/evidence/files/README.md#L33-L33` | `materialized_sources/corpus/github-getzep-graphiti--e9af10ca/evidence/files/README.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [getzep/graphiti](../sources/github-getzep-graphiti.md) — `evidenced_by`
- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
