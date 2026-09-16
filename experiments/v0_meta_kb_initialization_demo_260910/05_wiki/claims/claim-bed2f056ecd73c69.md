---
uid: wiki-page:evidence-12cbeb94dfbfbe21
title: Claim bed2f056ecd73c69
slug: claims/claim-bed2f056ecd73c69
page_type: evidence
status: review
summary: Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated
  outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , im
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:bed2f056ecd73c69
source_refs: &id001
- arxiv:2305.14627
page_refs:
- wiki-page:source-51388aa8e2e8587f
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-51388aa8e2e8587f
  relation: evidenced_by
  claim_refs:
  - claim:bed2f056ecd73c69
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:bed2f056ecd73c69
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:bed2f056ecd73c69
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:bed2f056ecd73c69
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:59348b6351fcf392
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
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
    one_line: Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their
      generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with
      citations , im
    short: Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated
      outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations
      , im
    full: null
  estimated_tokens: 238
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:bed2f056ecd73c69
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2305.14627
---

# Source assertion from Enabling Large Language Models to Generate Text with Citations

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability.

## Scope

- Claim ID: `claim:bed2f056ecd73c69`
- Scope: `source-reported assertion`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:4527dd12000fe21f` | `local://materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/normalized/document.txt#L140-L143` | `materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Enabling Large Language Models to Generate Text with Citations](../sources/arxiv-2305.14627.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
