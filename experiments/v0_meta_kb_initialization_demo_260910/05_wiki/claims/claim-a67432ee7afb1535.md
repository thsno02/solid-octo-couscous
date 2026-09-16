---
uid: wiki-page:evidence-ed313fbe55c04de9
title: Claim a67432ee7afb1535
slug: claims/claim-a67432ee7afb1535
page_type: evidence
status: review
summary: Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such
  as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large
  compu
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:a67432ee7afb1535
source_refs: &id001
- arxiv-2306.15626
page_refs:
- wiki-page:source-5be112b896547169
- wiki-page:map-knowledge-memory
outgoing_links:
- target: wiki-page:source-5be112b896547169
  relation: evidenced_by
  claim_refs:
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs:
  - claim:a67432ee7afb1535
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:a67432ee7afb1535
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:a67432ee7afb1535
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:bfe1ec178597b638
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
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
    one_line: Large language models (LLMs) have shown promise in proving formal theorems using proof assistants
      such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data,
      and large compu
    short: Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such
      as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and
      large compu
    full: null
  estimated_tokens: 226
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:a67432ee7afb1535
rights_refs: []
rights_unavailable_source_refs:
- arxiv-2306.15626
---

# Source assertion from LeanDojo: Theorem Proving with Retrieval-Augmented Language Models

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements.

## Scope

- Claim ID: `claim:a67432ee7afb1535`
- Scope: `source-reported assertion`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:7638a9216c6f2bd1` | `local://materialized_sources/corpus/arxiv-2306.15626--438dfbd9/normalized/document.txt#L118-L118` | `materialized_sources/corpus/arxiv-2306.15626--438dfbd9/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) — `evidenced_by`
- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (`arxiv-2306.15626`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
