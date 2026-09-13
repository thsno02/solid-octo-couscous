---
uid: wiki-page:map-recursive-self-improvement
title: Recursive Self Improvement
slug: maps/recursive-self-improvement
page_type: map
status: review
summary: Candidate map of recursive self improvement sources and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2a05950fe0a0b64d
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:90ae7352bb085ae8
- claim:d38b49dc4376d4b0
- claim:1b6ae1229c17cacd
- claim:f159011ee6ccddaf
- claim:97fae8cc4d519755
- claim:f810d086e0a4a305
- claim:f43359e01e4c4b0b
source_refs: &id001
- arxiv:2410.04444
- arxiv:2505.22954
- arxiv:cs/0309048
- github:jennyzzt/dgm
- standard:w3c-dcat-3
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
    one_line: Candidate map of recursive self improvement sources and claims.
    short: Candidate map of recursive self improvement sources and claims.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# Recursive Self Improvement

This map is compiled from candidate source assertions and collection assessments.

## `claim:2a05950fe0a0b64d`

**Scope:** source-reported assertion

We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code are described by axioms encoded in an initial proof searcher which is also part of the initial code.

## `claim:9243c79fad41f2cb`

**Scope:** collector assessment, not source-authored scientific fact

Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after proving that the rewrite improves expected utility.

## `claim:ae45b8d667e29552`

**Scope:** source-reported assertion

Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries.

## `claim:90ae7352bb085ae8`

**Scope:** collector assessment, not source-authored scientific fact

A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths.

## `claim:d38b49dc4376d4b0`

**Scope:** source-reported assertion

- Commit: `a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2` - Default branch: `main` - Description: jennyzzt/dgm - Selected evidence files: 2 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.

## `claim:1b6ae1229c17cacd`

**Scope:** collector assessment, not source-authored scientific fact

One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage.

## `claim:f159011ee6ccddaf`

**Scope:** source-reported assertion

DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web. This document defines the schema and provides examples for its use.

## `claim:97fae8cc4d519755`

**Scope:** collector assessment, not source-authored scientific fact

Catalog and dataset-series interoperability for a federated KB.

## `claim:f810d086e0a4a305`

**Scope:** source-reported assertion

The rapid advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. However, existing agentic systems, whether based on fixed pipeline algorithms or pre-defined meta-learning frameworks, cannot search the whole agent design space due to the restriction of human-designed components, and thus might miss the more optimal agent design.

## `claim:f43359e01e4c4b0b`

**Scope:** collector assessment, not source-authored scientific fact

Modernizes the Goedel-machine idea for LLM agents: the agent dynamically modifies its own logic and behavior under high-level objectives rather than following a fixed human-designed optimization routine.
