---
uid: wiki-page:map-automated-research
title: Automated Research
slug: maps/automated-research
page_type: map
status: review
summary: Candidate map of automated research sources and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:38c95b3e2bcfcf51
- claim:d3a0d3c2f4fd45d4
- claim:2f8ebd974fc7b5fd
- claim:3d07597b1776b0bd
- claim:3c6cef89711e89f2
- claim:852bc42ef50e89c7
- claim:9077f46d7f30e565
- claim:8798b3dc1ae125ea
source_refs: &id001
- arxiv:2408.06292
- arxiv:2501.04227
- arxiv:2504.08066
- arxiv:2505.13400
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
    one_line: Candidate map of automated research sources and claims.
    short: Candidate map of automated research sources and claims.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
---

# Automated Research

This map is compiled from candidate source assertions and collection assessments.

## `claim:38c95b3e2bcfcf51`

**Scope:** source-reported assertion

One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g.

## `claim:d3a0d3c2f4fd45d4`

**Scope:** collector assessment, not source-authored scientific fact

Extends self-evolution from improving an agent to automating the research loop itself: idea generation, implementation, experiment, paper writing, and automated review can be iterated to create new knowledge.

## `claim:2f8ebd974fc7b5fd`

**Scope:** source-reported assertion

Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory , an autonomous LLM-based framework capable of completing the entire research process.

## `claim:3d07597b1776b0bd`

**Scope:** collector assessment, not source-authored scientific fact

A practical end-to-end autonomous research workflow spanning literature review, experimentation and report writing, with explicit human feedback points.

## `claim:3c6cef89711e89f2`

**Scope:** source-reported assertion

Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow.

## `claim:852bc42ef50e89c7`

**Scope:** collector assessment, not source-authored scientific fact

One of the strongest demonstrations of a lab-in-the-loop discovery cycle: background research, hypothesis generation, experimental planning, human-executed wet-lab experiments, data analysis, and updated hypotheses.

## `claim:9077f46d7f30e565`

**Scope:** source-reported assertion

AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper.

## `claim:8798b3dc1ae125ea`

**Scope:** collector assessment, not source-authored scientific fact

End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process.
