---
uid: wiki-page:source-2672a50bc210b0f4
title: getzep/graphiti
slug: sources/github-getzep-graphiti
page_type: source
status: review
summary: Source page for getzep/graphiti with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:bc85c4d0c6801c3a
- claim:d6556415105fc41e
source_refs: &id002
- github:getzep/graphiti
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-db6f515f9effd011
- wiki-page:evidence-caedbc6d92b92e05
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-db6f515f9effd011
  relation: evidenced_by
  claim_refs:
  - claim:bc85c4d0c6801c3a
  notes: null
- target: wiki-page:evidence-caedbc6d92b92e05
  relation: evidenced_by
  claim_refs:
  - claim:d6556415105fc41e
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:bc85c4d0c6801c3a
  source_refs:
  - github:getzep/graphiti
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:d6556415105fc41e
  source_refs:
  - github:getzep/graphiti
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:3c4b53aa61004c0b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
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
    one_line: Source page for getzep/graphiti with claim/evidence expansion.
    short: Source page for getzep/graphiti with claim/evidence expansion.
    full: null
  estimated_tokens: 229
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:bc85c4d0c6801c3a
- claim:d6556415105fc41e
rights_refs: []
rights_unavailable_source_refs:
- github:getzep/graphiti
---

# getzep/graphiti

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `github:getzep/graphiti`
- Canonical ID: `getzep/graphiti`
- Source type: `github`
- Content tier: `semantic_capsule`
- Revision: `c035afb7990b6077331a81e98b04efcfd9bf8184`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/github-getzep-graphiti--e9af10ca/evidence/files/README.md`

## Source-reported candidate statements

- ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕

## Collection assessments

- Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history. 〔[claim:d6556415105fc41e](../claims/claim-d6556415105fc41e.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:bc85c4d0c6801c3a` | `evidence:2d2d6e2c4b39b026` | `local://materialized_sources/corpus/github-getzep-graphiti--e9af10ca/evidence/files/README.md#L33-L33` | `semantic_capsule` |
| `claim:d6556415105fc41e` | `evidence:d4d7cd076e23b0d2` | `local://raw_data/githubs/getzep--graphiti/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md) — `evidenced_by`
- [Claim d6556415105fc41e](../claims/claim-d6556415105fc41e.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
