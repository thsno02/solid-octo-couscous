---
uid: wiki-page:evidence-980bd5a6e6fb27d5
title: Claim f159011ee6ccddaf
slug: claims/claim-f159011ee6ccddaf
page_type: evidence
status: review
summary: DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the
  Web. This document defines the schema and provides examples for its use.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:f159011ee6ccddaf
source_refs: &id001
- standard:w3c-dcat-3
page_refs:
- wiki-page:source-608b8babe77a1d70
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-608b8babe77a1d70
  relation: evidenced_by
  claim_refs:
  - claim:f159011ee6ccddaf
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:f159011ee6ccddaf
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:f159011ee6ccddaf
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:f159011ee6ccddaf
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
  - standard:w3c-dcat-3@sha256:068b43f7814525ea784b7d565ada8de2b4538f5377517c4f0ec9b162a34dedfb
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
    one_line: DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published
      on the Web. This document defines the schema and provides examples for its use.
    short: DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on
      the Web. This document defines the schema and provides examples for its use.
    full: null
  estimated_tokens: 130
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from Data Catalog Vocabulary (DCAT) - Version 3

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web. This document defines the schema and provides examples for its use.

## Scope

- Claim ID: `claim:f159011ee6ccddaf`
- Scope: `source-reported assertion`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:a47bb9683733bcba` | `local://materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/document.md#L19-L29` | `materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/document.md` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Data Catalog Vocabulary (DCAT) - Version 3](../sources/standard-w3c-dcat-3.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
