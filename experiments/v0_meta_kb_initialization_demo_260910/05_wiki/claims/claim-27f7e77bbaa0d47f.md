---
uid: wiki-page:evidence-b0da231e5faa8371
title: Claim 27f7e77bbaa0d47f
slug: claims/claim-27f7e77bbaa0d47f
page_type: evidence
status: review
summary: Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:27f7e77bbaa0d47f
source_refs: &id001
- methodology:linkml-schema-first
page_refs:
- wiki-page:source-93365d53a252ec8d
- wiki-page:map-ontology-semantic-architecture
outgoing_links:
- target: wiki-page:source-93365d53a252ec8d
  relation: evidenced_by
  claim_refs:
  - claim:27f7e77bbaa0d47f
  notes: null
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs:
  - claim:27f7e77bbaa0d47f
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:27f7e77bbaa0d47f
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:27f7e77bbaa0d47f
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:0f0b56605b4756b3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
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
    one_line: Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other
      artifacts.
    short: Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts.
    full: null
  estimated_tokens: 124
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Collection assessment for LinkML schema-first knowledge modeling

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts.

## Scope

- Claim ID: `claim:27f7e77bbaa0d47f`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:d3ebb3860ae3f34c` | `local://raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml#collection.inclusion_reason` | `raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [LinkML schema-first knowledge modeling](../sources/methodology-linkml-schema-first.md) — `evidenced_by`
- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
