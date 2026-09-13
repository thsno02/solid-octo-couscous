---
uid: wiki-page:evidence-e62b2407c3534929
title: Claim dcf2fa8645f61032
slug: claims/claim-dcf2fa8645f61032
page_type: evidence
status: review
summary: The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable
  information model, vocabulary, and encoding mechanisms for representing statements about the usage of con
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:dcf2fa8645f61032
source_refs: &id001
- standard:w3c-odrl-2.2
page_refs:
- wiki-page:source-ea7b53bbdfb3ba7f
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-ea7b53bbdfb3ba7f
  relation: evidenced_by
  claim_refs:
  - claim:dcf2fa8645f61032
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:dcf2fa8645f61032
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:dcf2fa8645f61032
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:dcf2fa8645f61032
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and
      interoperable information model, vocabulary, and encoding mechanisms for representing statements about the
      usage of con
    short: The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and
      interoperable information model, vocabulary, and encoding mechanisms for representing statements about the
      usage of con
    full: null
  estimated_tokens: 152
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from ODRL Information Model 2.2

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies.

## Scope

- Claim ID: `claim:dcf2fa8645f61032`
- Scope: `source-reported assertion`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:a56d32108a0cbc0e` | `local://materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/document.md#L17-L19` | `materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/document.md` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [ODRL Information Model 2.2](../sources/standard-w3c-odrl-2.2.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
