---
uid: wiki-page:map-knowledge-editing
title: Knowledge Editing
slug: maps/knowledge-editing
page_type: map
status: review
summary: Candidate map of knowledge editing sources and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:4715a4ff3b1706fd
- claim:69e9059578125358
- claim:37a1c59affa857e1
- claim:4e12d22ef2e755b9
source_refs: &id001
- arxiv-2104.00405
- arxiv:2405.14768
page_refs: []
outgoing_links: []
sections: []
temporal:
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:43:07Z'
provenance:
  build_id: build:v0-meta-kb-260910:88936dc16ae2c769
  generated_by_agent: agent:deterministic-v0-builder
  generated_by_model: null
  prompt_or_skill_version: deterministic-v0.1
  compiled_from_revisions: *id001
  created_at: '2026-09-13T17:43:07Z'
  updated_at: '2026-09-13T17:43:07Z'
  manual_edits_preserved: true
review:
  state: needs_human
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Scientific and semantic review required before publication.
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
    one_line: Candidate map of knowledge editing sources and claims.
    short: Candidate map of knowledge editing sources and claims.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# Knowledge Editing

This map is compiled from candidate source assertions and collection assessments.

## `claim:4715a4ff3b1706fd`

**Scope:** source-reported assertion

Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community.

## `claim:69e9059578125358`

**Scope:** collector assessment, not source-authored scientific fact

Provides an implementation and benchmark substrate for comparing retention, transfer and forgetting across continual-learning strategies.

## `claim:37a1c59affa857e1`

**Scope:** source-reported assertion

Large language models (LLMs) need knowledge updates to meet the ever-growing world facts and correct the hallucinated responses, facilitating the methods of lifelong model editing. Where the updated knowledge resides in memories is a fundamental question for model editing.

## `claim:4e12d22ef2e755b9`

**Scope:** collector assessment, not source-authored scientific fact

Targets continual knowledge updates and knowledge conflicts in lifelong model editing via a dual-memory and knowledge-sharding design.
