---
uid: wiki-page:evidence-d3f9114eb1b08abf
title: Claim 4fd96c70e0c625fd
slug: claims/claim-4fd96c70e0c625fd
page_type: evidence
status: review
summary: A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring
  ideation, implementation, experimentation, analysis and iterative improvement.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:4fd96c70e0c625fd
source_refs: &id001
- arxiv:2502.14499
page_refs:
- wiki-page:source-3dda2384308efbda
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-3dda2384308efbda
  relation: evidenced_by
  claim_refs:
  - claim:4fd96c70e0c625fd
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:4fd96c70e0c625fd
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:4fd96c70e0c625fd
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:4fd96c70e0c625fd
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
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
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
    one_line: A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks
      requiring ideation, implementation, experimentation, analysis and iterative improvement.
    short: A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks
      requiring ideation, implementation, experimentation, analysis and iterative improvement.
    full: null
  estimated_tokens: 155
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Collection assessment for MLGym: A New Framework and Benchmark for Advancing AI Research Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring ideation, implementation, experimentation, analysis and iterative improvement.

## Scope

- Claim ID: `claim:4fd96c70e0c625fd`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:751adf7b39d39c48` | `local://raw_data/arxiv/MLGym: A New Framework and Benchmark for Advancing AI Research Agents/metadata.yaml#collection-inclusion-reason` | `raw_data/arxiv/MLGym: A New Framework and Benchmark for Advancing AI Research Agents/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
