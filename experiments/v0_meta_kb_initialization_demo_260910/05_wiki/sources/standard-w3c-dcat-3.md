---
uid: wiki-page:source-608b8babe77a1d70
title: Data Catalog Vocabulary (DCAT) - Version 3
slug: sources/standard-w3c-dcat-3
page_type: source
status: review
summary: Source page for Data Catalog Vocabulary (DCAT) - Version 3 with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:97fae8cc4d519755
- claim:f159011ee6ccddaf
source_refs: &id002
- standard:w3c-dcat-3
page_refs:
- wiki-page:map-recursive-self-improvement
- wiki-page:evidence-699a4b478e5ca869
- wiki-page:evidence-980bd5a6e6fb27d5
outgoing_links:
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-699a4b478e5ca869
  relation: evidenced_by
  claim_refs:
  - claim:97fae8cc4d519755
  notes: null
- target: wiki-page:evidence-980bd5a6e6fb27d5
  relation: evidenced_by
  claim_refs:
  - claim:f159011ee6ccddaf
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:f159011ee6ccddaf
  source_refs:
  - standard:w3c-dcat-3
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:97fae8cc4d519755
  source_refs:
  - standard:w3c-dcat-3
  editorial_intent: Keep collector interpretation separate.
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for Data Catalog Vocabulary (DCAT) - Version 3 with claim/evidence expansion.
    short: Source page for Data Catalog Vocabulary (DCAT) - Version 3 with claim/evidence expansion.
    full: null
  estimated_tokens: 166
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Data Catalog Vocabulary (DCAT) - Version 3

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `standard:w3c-dcat-3`
- Canonical ID: `W3C-DCAT-3`
- Source type: `standard`
- Content tier: `full_text`
- Revision: `sha256:068b43f7814525ea784b7d565ada8de2b4538f5377517c4f0ec9b162a34dedfb`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Local document: `materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/document.md`

## Source-reported candidate statements

- DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web. This document defines the schema and provides examples for its use. 〔[claim:f159011ee6ccddaf](../claims/claim-f159011ee6ccddaf.md)〕

## Collection assessments

- Catalog and dataset-series interoperability for a federated KB. 〔[claim:97fae8cc4d519755](../claims/claim-97fae8cc4d519755.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:97fae8cc4d519755` | `evidence:30dbaf3eec9450c9` | `local://raw_data/standard/Data Catalog Vocabulary DCAT 3/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:f159011ee6ccddaf` | `evidence:a47bb9683733bcba` | `local://materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/document.md#L19-L29` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
- [Claim 97fae8cc4d519755](../claims/claim-97fae8cc4d519755.md) — `evidenced_by`
- [Claim f159011ee6ccddaf](../claims/claim-f159011ee6ccddaf.md) — `evidenced_by`
