---
uid: wiki-page:evidence-bc3556337b5ca353
title: Claim ecf45fd3f4ab576a
slug: claims/claim-ecf45fd3f4ab576a
page_type: evidence
status: review
summary: While large language model (LLM) agents can effectively use external tools for complex real-world tasks,
  they require memory systems to leverage historical experiences. Current memory systems enable basic storage and
  ret
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:ecf45fd3f4ab576a
source_refs: &id001
- arxiv:2502.12110
page_refs:
- wiki-page:source-1aacba116cbe3c5b
- wiki-page:map-open-ended-evolution
outgoing_links:
- target: wiki-page:source-1aacba116cbe3c5b
  relation: evidenced_by
  claim_refs:
  - claim:ecf45fd3f4ab576a
  notes: null
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs:
  - claim:ecf45fd3f4ab576a
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:ecf45fd3f4ab576a
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:ecf45fd3f4ab576a
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:7709fc4901bbe1d3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.12110@sha256:d112e92606a562a0369e2e8cddadad88ac8d448d66c24ee9b63e808c2c84e42b
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
    one_line: While large language model (LLM) agents can effectively use external tools for complex real-world
      tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic
      storage and ret
    short: While large language model (LLM) agents can effectively use external tools for complex real-world tasks,
      they require memory systems to leverage historical experiences. Current memory systems enable basic storage
      and ret
    full: null
  estimated_tokens: 144
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from A-MEM: Agentic Memory for LLM Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases.

## Scope

- Claim ID: `claim:ecf45fd3f4ab576a`
- Scope: `source-reported assertion`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:23f9dcda024ab01e` | `local://materialized_sources/corpus/arxiv-2502.12110--d27d79d8/normalized/document.txt#L194-L194` | `materialized_sources/corpus/arxiv-2502.12110--d27d79d8/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [A-MEM: Agentic Memory for LLM Agents](../sources/arxiv-2502.12110.md) — `evidenced_by`
- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`
