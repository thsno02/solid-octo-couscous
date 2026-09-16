---
uid: wiki-page:source-9923ee576cd59e46
title: 'Avalanche: an End-to-End Library for Continual Learning'
slug: sources/arxiv-2104.00405
page_type: source
status: review
summary: 'Source page for Avalanche: an End-to-End Library for Continual Learning with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:4715a4ff3b1706fd
- claim:69e9059578125358
source_refs: &id002
- arxiv-2104.00405
page_refs:
- wiki-page:map-knowledge-editing
- wiki-page:evidence-771e19057a6e4a77
- wiki-page:evidence-fe4ad66514964285
outgoing_links:
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-771e19057a6e4a77
  relation: evidenced_by
  claim_refs:
  - claim:4715a4ff3b1706fd
  notes: null
- target: wiki-page:evidence-fe4ad66514964285
  relation: evidenced_by
  claim_refs:
  - claim:69e9059578125358
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:4715a4ff3b1706fd
  source_refs:
  - arxiv-2104.00405
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:69e9059578125358
  source_refs:
  - arxiv-2104.00405
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
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
    one_line: 'Source page for Avalanche: an End-to-End Library for Continual Learning with claim/evidence expansion.'
    short: 'Source page for Avalanche: an End-to-End Library for Continual Learning with claim/evidence expansion.'
    full: null
  estimated_tokens: 270
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4715a4ff3b1706fd
- claim:69e9059578125358
rights_refs: []
rights_unavailable_source_refs:
- arxiv-2104.00405
---

# Avalanche: an End-to-End Library for Continual Learning

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv-2104.00405`
- Canonical ID: `2104.00405`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Local document: `materialized_sources/corpus/arxiv-2104.00405--93b3bffb/normalized/document.txt`

## Source-reported candidate statements

- Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community. 〔[claim:4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md)〕

## Collection assessments

- Provides an implementation and benchmark substrate for comparing retention, transfer and forgetting across continual-learning strategies. 〔[claim:69e9059578125358](../claims/claim-69e9059578125358.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:4715a4ff3b1706fd` | `evidence:f6e341ae267fd83f` | `local://materialized_sources/corpus/arxiv-2104.00405--93b3bffb/normalized/document.txt#L114-L114` | `full_text` |
| `claim:69e9059578125358` | `evidence:5588c577f1f93f1c` | `local://raw_data/arxiv/Avalanche an End-to-End Library for Continual Learning/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
- [Claim 4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md) — `evidenced_by`
- [Claim 69e9059578125358](../claims/claim-69e9059578125358.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Avalanche: an End-to-End Library for Continual Learning (`arxiv-2104.00405`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
