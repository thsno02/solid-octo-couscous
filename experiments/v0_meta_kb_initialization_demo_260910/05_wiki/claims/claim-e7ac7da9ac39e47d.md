---
uid: wiki-page:evidence-11f3f7762e882a4a
title: Claim e7ac7da9ac39e47d
slug: claims/claim-e7ac7da9ac39e47d
page_type: evidence
status: review
summary: '**sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together.
  Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it
  throu'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:e7ac7da9ac39e47d
source_refs: &id001
- github:xoai/sage-wiki
page_refs:
- wiki-page:source-a41aba6e720b278f
- wiki-page:map-llm-wiki
outgoing_links:
- target: wiki-page:source-a41aba6e720b278f
  relation: evidenced_by
  claim_refs:
  - claim:e7ac7da9ac39e47d
  notes: null
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs:
  - claim:e7ac7da9ac39e47d
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:e7ac7da9ac39e47d
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:e7ac7da9ac39e47d
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
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: '**sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together.
      Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query
      it throu'
    short: '**sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together.
      Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query
      it throu'
    full: null
  estimated_tokens: 217
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:e7ac7da9ac39e47d
rights_refs: []
rights_unavailable_source_refs:
- github:xoai/sage-wiki
---

# Source assertion from xoai/sage-wiki

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

**sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown.

## Scope

- Claim ID: `claim:e7ac7da9ac39e47d`
- Scope: `source-reported assertion`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:27bcae6d97e234f4` | `local://materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/evidence/files/README.md#L5-L5` | `materialized_sources/corpus/github-xoai-sage-wiki--5289f5d0/evidence/files/README.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [xoai/sage-wiki](../sources/github-xoai-sage-wiki.md) — `evidenced_by`
- [Llm Wiki](../maps/llm-wiki.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
