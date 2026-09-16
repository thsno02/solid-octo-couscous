---
uid: wiki-page:evidence-6e6d202159e49cd6
title: Claim bde139a533f9483a
slug: claims/claim-bde139a533f9483a
page_type: evidence
status: review
summary: A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses,
  run experiments, analyze results and discover explanatory knowledge.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:bde139a533f9483a
source_refs: &id001
- arxiv:2406.06769
page_refs:
- wiki-page:source-18c791741aa4bcd7
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-18c791741aa4bcd7
  relation: evidenced_by
  claim_refs:
  - claim:bde139a533f9483a
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:bde139a533f9483a
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:bde139a533f9483a
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:bde139a533f9483a
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:bf1b13c8baaa32ad
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
    one_line: A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses,
      run experiments, analyze results and discover explanatory knowledge.
    short: A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses,
      run experiments, analyze results and discover explanatory knowledge.
    full: null
  estimated_tokens: 160
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:bde139a533f9483a
rights_refs: []
rights_unavailable_source_refs: []
---

# Collection assessment for DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses, run experiments, analyze results and discover explanatory knowledge.

## Scope

- Claim ID: `claim:bde139a533f9483a`
- Scope: `collector assessment, not source-authored scientific fact`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:fdf8b5c29b9da39e` | `local://raw_data/arxiv/DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents/metadata.yaml#collection.inclusion_reason` | `raw_data/arxiv/DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents/metadata.yaml` | `metadata_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`
