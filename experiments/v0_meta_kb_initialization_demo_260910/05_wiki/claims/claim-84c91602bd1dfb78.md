---
uid: wiki-page:evidence-7251138bb2057919
title: Claim 84c91602bd1dfb78
slug: claims/claim-84c91602bd1dfb78
page_type: evidence
status: review
summary: Automated scientific discovery promises to accelerate progress across scientific domains. However, developing
  and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:84c91602bd1dfb78
source_refs: &id001
- arxiv:2406.06769
page_refs:
- wiki-page:source-18c791741aa4bcd7
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-18c791741aa4bcd7
  relation: evidenced_by
  claim_refs:
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:84c91602bd1dfb78
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:84c91602bd1dfb78
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:84c91602bd1dfb78
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
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
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
    one_line: Automated scientific discovery promises to accelerate progress across scientific domains. However,
      developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running
      real-world
    short: Automated scientific discovery promises to accelerate progress across scientific domains. However, developing
      and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world
    full: null
  estimated_tokens: 146
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible.

## Scope

- Claim ID: `claim:84c91602bd1dfb78`
- Scope: `source-reported assertion`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:69559f8937311f42` | `local://materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt#L89-L90` | `materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
