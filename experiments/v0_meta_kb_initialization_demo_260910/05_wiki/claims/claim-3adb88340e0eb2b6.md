---
uid: wiki-page:evidence-2764359fa43284d2
title: Claim 3adb88340e0eb2b6
slug: claims/claim-3adb88340e0eb2b6
page_type: evidence
status: review
summary: Modern schema-first bridge between developer data models and linked-data/ontology artifacts.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:3adb88340e0eb2b6
source_refs: &id001
- github:linkml/linkml
page_refs:
- wiki-page:source-8a8c72b9ad5bf51d
- wiki-page:map-ontology-semantic-architecture
outgoing_links:
- target: wiki-page:source-8a8c72b9ad5bf51d
  relation: evidenced_by
  claim_refs:
  - claim:3adb88340e0eb2b6
  notes: null
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs:
  - claim:3adb88340e0eb2b6
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:3adb88340e0eb2b6
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:3adb88340e0eb2b6
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:45bd6c7288326476
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
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
    one_line: Modern schema-first bridge between developer data models and linked-data/ontology artifacts.
    short: Modern schema-first bridge between developer data models and linked-data/ontology artifacts.
    full: null
  estimated_tokens: 105
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:3adb88340e0eb2b6
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for linkml/linkml

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Modern schema-first bridge between developer data models and linked-data/ontology artifacts.

## Scope

- Claim ID: `claim:3adb88340e0eb2b6`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:253deb651ed5a168` | `local://raw_data/githubs/linkml--linkml/metadata.yaml#collection.inclusion_reason` | `raw_data/githubs/linkml--linkml/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [linkml/linkml](../sources/github-linkml-linkml.md) — `evidenced_by`
- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
