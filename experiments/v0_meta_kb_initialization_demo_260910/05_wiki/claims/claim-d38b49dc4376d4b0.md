---
uid: wiki-page:evidence-c7e5f49d25efb6ba
title: Claim d38b49dc4376d4b0
slug: claims/claim-d38b49dc4376d4b0
page_type: evidence
status: review
summary: '- Commit: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2` - Default branch: `main` - Description: jennyzzt/dgm
  - Selected evidence files: 2 of 21 files observed - Interpretation: maintainer documentation and static repository'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:d38b49dc4376d4b0
source_refs: &id001
- github:jennyzzt/dgm
page_refs:
- wiki-page:source-e3fe88d81aab6499
- wiki-page:map-recursive-self-improvement
outgoing_links:
- target: wiki-page:source-e3fe88d81aab6499
  relation: evidenced_by
  claim_refs:
  - claim:d38b49dc4376d4b0
  notes: null
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs:
  - claim:d38b49dc4376d4b0
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:d38b49dc4376d4b0
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:d38b49dc4376d4b0
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
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
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
    one_line: '- Commit: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2` - Default branch: `main` - Description: jennyzzt/dgm
      - Selected evidence files: 2 of 21 files observed - Interpretation: maintainer documentation and static repository'
    short: '- Commit: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2` - Default branch: `main` - Description: jennyzzt/dgm
      - Selected evidence files: 2 of 21 files observed - Interpretation: maintainer documentation and static repository'
    full: null
  estimated_tokens: 123
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from jennyzzt/dgm

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

- Commit: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2` - Default branch: `main` - Description: jennyzzt/dgm - Selected evidence files: 2 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## Scope

- Claim ID: `claim:d38b49dc4376d4b0`
- Scope: `source-reported assertion`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:86f2cb90e58dd2e2` | `local://materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/document.md#L3-L6` | `materialized_sources/corpus/github-jennyzzt-dgm--c8b75f99/document.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) — `evidenced_by`
- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
