---
uid: wiki-page:source-fee7c775085eb729
title: Apache Ossie (incubating), formerly Open Semantic Interchange
slug: sources/standard-apache-ossie
page_type: source
status: review
summary: Source page for Apache Ossie (incubating), formerly Open Semantic Interchange with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:068d86487f332a77
- claim:1f22b83092edba2b
source_refs: &id002
- standard:apache-ossie
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-6a249b035672c9ad
- wiki-page:evidence-a18720ee17068661
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-6a249b035672c9ad
  relation: evidenced_by
  claim_refs:
  - claim:068d86487f332a77
  notes: null
- target: wiki-page:evidence-a18720ee17068661
  relation: evidenced_by
  claim_refs:
  - claim:1f22b83092edba2b
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:1f22b83092edba2b
  source_refs:
  - standard:apache-ossie
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:068d86487f332a77
  source_refs:
  - standard:apache-ossie
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for Apache Ossie (incubating), formerly Open Semantic Interchange with claim/evidence
      expansion.
    short: Source page for Apache Ossie (incubating), formerly Open Semantic Interchange with claim/evidence expansion.
    full: null
  estimated_tokens: 145
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Apache Ossie (incubating), formerly Open Semantic Interchange

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `standard:apache-ossie`
- Canonical ID: `APACHE-OSSIE`
- Source type: `standard`
- Content tier: `full_text`
- Revision: `sha256:ee15e76e9196d569d57ad8b65a3865e333d1891ff04791e2b2772b1edbb32eb4`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/standard-apache-ossie--ae9e548a/document.md`

## Source-reported candidate statements

- # Home 〔[claim:1f22b83092edba2b](../claims/claim-1f22b83092edba2b.md)〕

## Collection assessments

- A new vendor-neutral semantic-model interchange effort for analytics, BI and AI agents. 〔[claim:068d86487f332a77](../claims/claim-068d86487f332a77.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:068d86487f332a77` | `evidence:16c9071134e85765` | `local://raw_data/standard/Apache Ossie Open Semantic Interchange/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:1f22b83092edba2b` | `evidence:7955be302ab59fa7` | `local://materialized_sources/corpus/standard-apache-ossie--ae9e548a/document.md#L1-L1` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 068d86487f332a77](../claims/claim-068d86487f332a77.md) — `evidenced_by`
- [Claim 1f22b83092edba2b](../claims/claim-1f22b83092edba2b.md) — `evidenced_by`
