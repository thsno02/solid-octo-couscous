---
uid: wiki-page:evidence-a18720ee17068661
title: Claim 1f22b83092edba2b
slug: claims/claim-1f22b83092edba2b
page_type: evidence
status: review
summary: '# Home'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:1f22b83092edba2b
source_refs: &id001
- standard:apache-ossie
page_refs:
- wiki-page:source-fee7c775085eb729
- wiki-page:map-ontology-semantic-architecture
outgoing_links:
- target: wiki-page:source-fee7c775085eb729
  relation: evidenced_by
  claim_refs:
  - claim:1f22b83092edba2b
  notes: null
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs:
  - claim:1f22b83092edba2b
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:1f22b83092edba2b
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:1f22b83092edba2b
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
  - standard:apache-ossie@sha256:ee15e76e9196d569d57ad8b65a3865e333d1891ff04791e2b2772b1edbb32eb4
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
    one_line: '# Home'
    short: '# Home'
    full: null
  estimated_tokens: 105
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from Apache Ossie (incubating), formerly Open Semantic Interchange

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

# Home

## Scope

- Claim ID: `claim:1f22b83092edba2b`
- Scope: `source-reported assertion`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:7955be302ab59fa7` | `local://materialized_sources/corpus/standard-apache-ossie--ae9e548a/document.md#L1-L1` | `materialized_sources/corpus/standard-apache-ossie--ae9e548a/document.md` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Apache Ossie (incubating), formerly Open Semantic Interchange](../sources/standard-apache-ossie.md) — `evidenced_by`
- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
