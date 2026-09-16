---
uid: wiki-page:source-50778f95d8e64d2e
title: A Survey on Self-Evolution of Large Language Models
slug: sources/arxiv-2404.14387
page_type: source
status: review
summary: Source page for A Survey on Self-Evolution of Large Language Models with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:2060aa1cdd09f8bd
- claim:df1b88d18276a319
source_refs: &id002
- arxiv:2404.14387
page_refs:
- wiki-page:map-open-ended-evolution
- wiki-page:evidence-5c91752d9f47111d
- wiki-page:evidence-91ede4d031c88f48
outgoing_links:
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-5c91752d9f47111d
  relation: evidenced_by
  claim_refs:
  - claim:2060aa1cdd09f8bd
  notes: null
- target: wiki-page:evidence-91ede4d031c88f48
  relation: evidenced_by
  claim_refs:
  - claim:df1b88d18276a319
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:df1b88d18276a319
  source_refs:
  - arxiv:2404.14387
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:2060aa1cdd09f8bd
  source_refs:
  - arxiv:2404.14387
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:699e317011de119b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2404.14387@sha256:afd13bcb8ce6f553dec268c0fb17bfb6b8a1ba80a4881a5b46d54b927ca9a418
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
    one_line: Source page for A Survey on Self-Evolution of Large Language Models with claim/evidence expansion.
    short: Source page for A Survey on Self-Evolution of Large Language Models with claim/evidence expansion.
    full: null
  estimated_tokens: 287
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2060aa1cdd09f8bd
- claim:df1b88d18276a319
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2404.14387
---

# A Survey on Self-Evolution of Large Language Models

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2404.14387`
- Canonical ID: `2404.14387`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:afd13bcb8ce6f553dec268c0fb17bfb6b8a1ba80a4881a5b46d54b927ca9a418`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Local document: `materialized_sources/corpus/arxiv-2404.14387--a0c7dbc0/normalized/document.txt`

## Source-reported candidate statements

- Large language models (LLMs) have significantly advanced in various fields and intelligent agent applications. However, current LLMs that learn from human or external model supervision are costly and may face performance ceilings as task complexity and diversity increase. 〔[claim:df1b88d18276a319](../claims/claim-df1b88d18276a319.md)〕

## Collection assessments

- Provides a useful process decomposition of LLM self-evolution into experience acquisition, experience refinement, updating, and evaluation; a natural reference taxonomy for later knowledge self-evolution pipelines. 〔[claim:2060aa1cdd09f8bd](../claims/claim-2060aa1cdd09f8bd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:2060aa1cdd09f8bd` | `evidence:13344d3141a1c2e3` | `local://raw_data/arxiv/A Survey on Self-Evolution of Large Language Models/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:df1b88d18276a319` | `evidence:fe677dd4add0eef4` | `local://materialized_sources/corpus/arxiv-2404.14387--a0c7dbc0/normalized/document.txt#L556-L556` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`
- [Claim 2060aa1cdd09f8bd](../claims/claim-2060aa1cdd09f8bd.md) — `evidenced_by`
- [Claim df1b88d18276a319](../claims/claim-df1b88d18276a319.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### A Survey on Self-Evolution of Large Language Models (`arxiv:2404.14387`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
