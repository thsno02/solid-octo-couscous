---
uid: wiki-page:source-003e063d0c302d83
title: 'Knowledge Editing for Large Language Models: A Survey'
slug: sources/arxiv-2310.16218
page_type: source
status: review
summary: 'Source page for Knowledge Editing for Large Language Models: A Survey with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:65d2f5de5c0ecdfd
- claim:d6b9ad7b6c2678cc
source_refs: &id002
- arxiv:2310.16218
page_refs:
- wiki-page:map-knowledge-editing
- wiki-page:evidence-c78374ec4210e21f
- wiki-page:evidence-82279bc33118e4a9
outgoing_links:
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-c78374ec4210e21f
  relation: evidenced_by
  claim_refs:
  - claim:65d2f5de5c0ecdfd
  notes: null
- target: wiki-page:evidence-82279bc33118e4a9
  relation: evidenced_by
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  source_refs:
  - arxiv:2310.16218
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:65d2f5de5c0ecdfd
  source_refs:
  - arxiv:2310.16218
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
  - arxiv:2310.16218@sha256:be80105279b0f4acf0e1817a727c0de41b57db523e6a7bc5369b0e062139f52f
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
    one_line: 'Source page for Knowledge Editing for Large Language Models: A Survey with claim/evidence expansion.'
    short: 'Source page for Knowledge Editing for Large Language Models: A Survey with claim/evidence expansion.'
    full: null
  estimated_tokens: 280
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:65d2f5de5c0ecdfd
- claim:d6b9ad7b6c2678cc
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2310.16218
---

# Knowledge Editing for Large Language Models: A Survey

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2310.16218`
- Canonical ID: `2310.16218`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:be80105279b0f4acf0e1817a727c0de41b57db523e6a7bc5369b0e062139f52f`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Local document: `materialized_sources/corpus/arxiv-2310.16218--21c4a191/normalized/document.txt`

## Source-reported candidate statements

- Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and reasoning ability. 〔[claim:d6b9ad7b6c2678cc](../claims/claim-d6b9ad7b6c2678cc.md)〕

## Collection assessments

- Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems needed to govern knowledge updates rather than treating updates as an unconstrained write operation. 〔[claim:65d2f5de5c0ecdfd](../claims/claim-65d2f5de5c0ecdfd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:65d2f5de5c0ecdfd` | `evidence:3846199ea839fba4` | `local://raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:d6b9ad7b6c2678cc` | `evidence:c5cfc0bf91f61fb4` | `local://materialized_sources/corpus/arxiv-2310.16218--21c4a191/normalized/document.txt#L214-L214` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
- [Claim 65d2f5de5c0ecdfd](../claims/claim-65d2f5de5c0ecdfd.md) — `evidenced_by`
- [Claim d6b9ad7b6c2678cc](../claims/claim-d6b9ad7b6c2678cc.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Knowledge Editing for Large Language Models: A Survey (`arxiv:2310.16218`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
