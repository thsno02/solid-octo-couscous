---
uid: wiki-page:evidence-99cfc321f0f45e32
title: Claim 334565c7ebb30cb5
slug: claims/claim-334565c7ebb30cb5
page_type: evidence
status: review
summary: '- Commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb` - Default branch: `main` - Description: SakanaAI/AI-Scientist
  - Selected evidence files: 1 of 21 files observed - Interpretation: maintainer documentation and static r'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:334565c7ebb30cb5
source_refs: &id001
- github:SakanaAI/AI-Scientist
page_refs:
- wiki-page:source-11d8f2a43bca42c2
- wiki-page:map-cross-cutting
outgoing_links:
- target: wiki-page:source-11d8f2a43bca42c2
  relation: evidenced_by
  claim_refs:
  - claim:334565c7ebb30cb5
  notes: null
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs:
  - claim:334565c7ebb30cb5
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:334565c7ebb30cb5
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:334565c7ebb30cb5
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
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
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
    one_line: '- Commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb` - Default branch: `main` - Description: SakanaAI/AI-Scientist
      - Selected evidence files: 1 of 21 files observed - Interpretation: maintainer documentation and static r'
    short: '- Commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb` - Default branch: `main` - Description: SakanaAI/AI-Scientist
      - Selected evidence files: 1 of 21 files observed - Interpretation: maintainer documentation and static r'
    full: null
  estimated_tokens: 122
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Source assertion from SakanaAI/AI-Scientist

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

- Commit: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb` - Default branch: `main` - Description: SakanaAI/AI-Scientist - Selected evidence files: 1 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## Scope

- Claim ID: `claim:334565c7ebb30cb5`
- Scope: `source-reported assertion`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:63f97f6fe4380c7d` | `local://materialized_sources/corpus/github-SakanaAI-AI-Scientist--2b41a05d/document.md#L3-L6` | `materialized_sources/corpus/github-SakanaAI-AI-Scientist--2b41a05d/document.md` | `semantic_capsule` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [SakanaAI/AI-Scientist](../sources/github-sakanaai-ai-scientist.md) — `evidenced_by`
- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
