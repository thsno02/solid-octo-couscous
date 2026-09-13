---
uid: wiki-page:evidence-a448e75882dfd050
title: Claim 37a1c59affa857e1
slug: claims/claim-37a1c59affa857e1
page_type: evidence
status: review
summary: 'Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the
  hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides
  in '
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:37a1c59affa857e1
source_refs: &id001
- arxiv:2405.14768
page_refs:
- wiki-page:source-1fec3cb1e7f11c84
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-1fec3cb1e7f11c84
  relation: evidenced_by
  claim_refs:
  - claim:37a1c59affa857e1
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:37a1c59affa857e1
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:37a1c59affa857e1
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:37a1c59affa857e1
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
  - arxiv:2405.14768@sha256:60420a5c24efe0a4ea70983fb86ae62aaa3342d538d30e020d73efcf6d105ea5
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
    one_line: 'Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct
      the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge
      resides in '
    short: 'Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct
      the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge
      resides in '
    full: null
  estimated_tokens: 153
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides in memories is a fundamental question for model editing.

## Scope

- Claim ID: `claim:37a1c59affa857e1`
- Scope: `source-reported assertion`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:d28db69c6cf6c420` | `local://materialized_sources/corpus/arxiv-2405.14768--80dba2af/normalized/document.txt#L137-L137` | `materialized_sources/corpus/arxiv-2405.14768--80dba2af/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](../sources/arxiv-2405.14768.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`
