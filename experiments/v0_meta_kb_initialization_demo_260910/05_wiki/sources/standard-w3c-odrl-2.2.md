---
uid: wiki-page:source-ea7b53bbdfb3ba7f
title: ODRL Information Model 2.2
slug: sources/standard-w3c-odrl-2.2
page_type: source
status: review
summary: Source page for ODRL Information Model 2.2 with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:217f2f5a6220ec41
- claim:dcf2fa8645f61032
source_refs: &id002
- standard:w3c-odrl-2.2
page_refs:
- wiki-page:map-governance-evaluation
- wiki-page:evidence-8536e7c0fe02feee
- wiki-page:evidence-e62b2407c3534929
outgoing_links:
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-8536e7c0fe02feee
  relation: evidenced_by
  claim_refs:
  - claim:217f2f5a6220ec41
  notes: null
- target: wiki-page:evidence-e62b2407c3534929
  relation: evidenced_by
  claim_refs:
  - claim:dcf2fa8645f61032
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:dcf2fa8645f61032
  source_refs:
  - standard:w3c-odrl-2.2
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:217f2f5a6220ec41
  source_refs:
  - standard:w3c-odrl-2.2
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
  - standard:w3c-odrl-2.2@sha256:af187a2c26b2429a579039403f34d9a5d5f29a1e01019662043068fa1ca2beaa
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
    one_line: Source page for ODRL Information Model 2.2 with claim/evidence expansion.
    short: Source page for ODRL Information Model 2.2 with claim/evidence expansion.
    full: null
  estimated_tokens: 192
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# ODRL Information Model 2.2

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `standard:w3c-odrl-2.2`
- Canonical ID: `W3C-ODRL-2.2`
- Source type: `standard`
- Content tier: `full_text`
- Revision: `sha256:af187a2c26b2429a579039403f34d9a5d5f29a1e01019662043068fa1ca2beaa`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Local document: `materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/document.md`

## Source-reported candidate statements

- The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕

## Collection assessments

- Machine-readable permissions, prohibitions and duties for knowledge access and change. 〔[claim:217f2f5a6220ec41](../claims/claim-217f2f5a6220ec41.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:217f2f5a6220ec41` | `evidence:bccba911b8e6a530` | `local://raw_data/standard/ODRL Information Model 2.2/metadata.yaml#collection-inclusion-reason` | `metadata_capsule` |
| `claim:dcf2fa8645f61032` | `evidence:a56d32108a0cbc0e` | `local://materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/document.md#L17-L19` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
- [Claim 217f2f5a6220ec41](../claims/claim-217f2f5a6220ec41.md) — `evidenced_by`
- [Claim dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md) — `evidenced_by`
