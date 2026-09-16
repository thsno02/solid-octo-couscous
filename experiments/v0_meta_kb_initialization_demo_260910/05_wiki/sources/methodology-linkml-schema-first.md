---
uid: wiki-page:source-93365d53a252ec8d
title: LinkML schema-first knowledge modeling
slug: sources/methodology-linkml-schema-first
page_type: source
status: review
summary: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:27f7e77bbaa0d47f
- claim:583280271287ef9c
source_refs: &id002
- methodology:linkml-schema-first
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-b0da231e5faa8371
- wiki-page:evidence-1e92251bcd39495b
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-b0da231e5faa8371
  relation: evidenced_by
  claim_refs:
  - claim:27f7e77bbaa0d47f
  notes: null
- target: wiki-page:evidence-1e92251bcd39495b
  relation: evidenced_by
  claim_refs:
  - claim:583280271287ef9c
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:583280271287ef9c
  source_refs:
  - methodology:linkml-schema-first
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:27f7e77bbaa0d47f
  source_refs:
  - methodology:linkml-schema-first
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9c2a89d879277c9e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
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
  checked_at: '2026-09-13T17:38:21Z'
  max_age_days: 30
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
    short: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
    full: null
  estimated_tokens: 164
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LinkML schema-first knowledge modeling

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `methodology:linkml-schema-first`
- Canonical ID: `METHODOLOGY-LINKML`
- Source type: `methodology`
- Content tier: `full_text`
- Revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/document.md`

## Source-reported candidate statements

- LinkML is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕

## Collection assessments

- Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts. 〔[claim:27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:27f7e77bbaa0d47f` | `evidence:d3ebb3860ae3f34c` | `local://raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:583280271287ef9c` | `evidence:b0f0f32b0b4cc957` | `local://materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/document.md#L6-L7` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md) — `evidenced_by`
- [Claim 583280271287ef9c](../claims/claim-583280271287ef9c.md) — `evidenced_by`
