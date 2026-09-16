---
uid: wiki-page:evidence-e923ecfc4b63b02d
title: Claim 90ae7352bb085ae8
slug: claims/claim-90ae7352bb085ae8
page_type: evidence
status: review
summary: 'A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and
  preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone
  pat'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:90ae7352bb085ae8
source_refs: &id001
- arxiv:2505.22954
page_refs:
- wiki-page:source-c29f716871f80314
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-c29f716871f80314
  relation: evidenced_by
  claim_refs:
  - claim:90ae7352bb085ae8
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:90ae7352bb085ae8
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:90ae7352bb085ae8
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:90ae7352bb085ae8
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:487f888f4db7dee3
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2505.22954@sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
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
    one_line: 'A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes,
      and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone
      pat'
    short: 'A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes,
      and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone
      pat'
    full: null
  estimated_tokens: 152
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Collection assessment for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths.

## Scope

- Claim ID: `claim:90ae7352bb085ae8`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:e71040c37751e493` | `local://raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
