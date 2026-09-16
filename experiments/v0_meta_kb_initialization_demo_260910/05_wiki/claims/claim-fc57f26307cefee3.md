---
uid: wiki-page:evidence-c558445f37ca3e5f
title: Claim fc57f26307cefee3
slug: claims/claim-fc57f26307cefee3
page_type: evidence
status: review
summary: LinkML is a linked data modeling language following object-oriented and ontological principles.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:fc57f26307cefee3
source_refs: &id001
- github:linkml/linkml
page_refs:
- wiki-page:source-8a8c72b9ad5bf51d
- wiki-page:map-ontology-semantic-architecture
outgoing_links:
- target: wiki-page:source-8a8c72b9ad5bf51d
  relation: evidenced_by
  claim_refs:
  - claim:fc57f26307cefee3
  notes: null
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs:
  - claim:fc57f26307cefee3
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:fc57f26307cefee3
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:fc57f26307cefee3
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:05e882fced13f0e1
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
    one_line: LinkML is a linked data modeling language following object-oriented and ontological principles.
    short: LinkML is a linked data modeling language following object-oriented and ontological principles.
    full: null
  estimated_tokens: 185
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:fc57f26307cefee3
rights_refs: []
rights_unavailable_source_refs:
- github:linkml/linkml
---

# Source assertion from linkml/linkml

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

LinkML is a linked data modeling language following object-oriented and ontological principles.

## Scope

- Claim ID: `claim:fc57f26307cefee3`
- Scope: `source-reported assertion`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:e35d83f60d15f992` | `local://materialized_sources/corpus/github-linkml-linkml--5f0806ef/evidence/files/README.md#L13-L13` | `materialized_sources/corpus/github-linkml-linkml--5f0806ef/evidence/files/README.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [linkml/linkml](../sources/github-linkml-linkml.md) — `evidenced_by`
- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
