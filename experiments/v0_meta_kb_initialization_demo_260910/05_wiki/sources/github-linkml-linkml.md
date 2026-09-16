---
uid: wiki-page:source-8a8c72b9ad5bf51d
title: linkml/linkml
slug: sources/github-linkml-linkml
page_type: source
status: review
summary: Source page for linkml/linkml with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:3adb88340e0eb2b6
- claim:fc57f26307cefee3
source_refs: &id002
- github:linkml/linkml
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-2764359fa43284d2
- wiki-page:evidence-c558445f37ca3e5f
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-2764359fa43284d2
  relation: evidenced_by
  claim_refs:
  - claim:3adb88340e0eb2b6
  notes: null
- target: wiki-page:evidence-c558445f37ca3e5f
  relation: evidenced_by
  claim_refs:
  - claim:fc57f26307cefee3
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:fc57f26307cefee3
  source_refs:
  - github:linkml/linkml
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:3adb88340e0eb2b6
  source_refs:
  - github:linkml/linkml
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:ac56ea43f6b5393c
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for linkml/linkml with claim/evidence expansion.
    short: Source page for linkml/linkml with claim/evidence expansion.
    full: null
  estimated_tokens: 225
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:3adb88340e0eb2b6
- claim:fc57f26307cefee3
rights_refs: []
rights_unavailable_source_refs:
- github:linkml/linkml
---

# linkml/linkml

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:linkml/linkml`
- Canonical ID: `linkml/linkml`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `0e401cef2711b0f12f5a1870805c5cfa999b0858`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/github-linkml-linkml--5f0806ef/evidence/files/README.md`

## Source-reported candidate statements

- LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Collection assessments

- Modern schema-first bridge between developer data models and linked-data/ontology artifacts. 〔[claim:3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:3adb88340e0eb2b6` | `evidence:253deb651ed5a168` | `local://raw_data/githubs/linkml--linkml/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:fc57f26307cefee3` | `evidence:e35d83f60d15f992` | `local://materialized_sources/corpus/github-linkml-linkml--5f0806ef/evidence/files/README.md#L13-L13` | `semantic_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md) — `evidenced_by`
- [Claim fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
