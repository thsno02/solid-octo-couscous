---
uid: wiki-page:map-recursive-self-improvement
title: Recursive Self Improvement
slug: maps/recursive-self-improvement
page_type: map
status: review
summary: Routing map for recursive self improvement sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:1b6ae1229c17cacd
- claim:2a05950fe0a0b64d
- claim:822962fc261c9559
- claim:90ae7352bb085ae8
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:d38b49dc4376d4b0
- claim:f43359e01e4c4b0b
- claim:f810d086e0a4a305
source_refs: &id001
- github:jennyzzt/dgm
- arxiv:cs/0309048
- arxiv:2406.04268
- arxiv:2505.22954
- arxiv:2410.04444
page_refs:
- wiki-page:source-e3fe88d81aab6499
- wiki-page:source-0e73b118b5b15597
- wiki-page:source-13964b2db9a9f793
- wiki-page:source-c29f716871f80314
- wiki-page:source-d04ae5d37f10547b
- wiki-page:knowledge-evolution-loop
- wiki-page:automation-vs-editorial-review
outgoing_links:
- target: wiki-page:source-e3fe88d81aab6499
  relation: explains
  claim_refs:
  - claim:d38b49dc4376d4b0
  - claim:1b6ae1229c17cacd
  notes: null
- target: wiki-page:source-0e73b118b5b15597
  relation: explains
  claim_refs:
  - claim:2a05950fe0a0b64d
  - claim:9243c79fad41f2cb
  notes: null
- target: wiki-page:source-13964b2db9a9f793
  relation: explains
  claim_refs:
  - claim:822962fc261c9559
  notes: null
- target: wiki-page:source-c29f716871f80314
  relation: explains
  claim_refs:
  - claim:ae45b8d667e29552
  - claim:90ae7352bb085ae8
  notes: null
- target: wiki-page:source-d04ae5d37f10547b
  relation: explains
  claim_refs:
  - claim:f810d086e0a4a305
  - claim:f43359e01e4c4b0b
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:2a05950fe0a0b64d
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:ae45b8d667e29552
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:2a05950fe0a0b64d
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:ae45b8d667e29552
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:2a05950fe0a0b64d
  - claim:ae45b8d667e29552
  - claim:d38b49dc4376d4b0
  - claim:f810d086e0a4a305
  source_refs:
  - arxiv:cs/0309048
  - arxiv:2505.22954
  - github:jennyzzt/dgm
  - arxiv:2410.04444
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:1b6ae1229c17cacd
  - claim:822962fc261c9559
  - claim:90ae7352bb085ae8
  - claim:9243c79fad41f2cb
  - claim:f43359e01e4c4b0b
  source_refs:
  - github:jennyzzt/dgm
  - arxiv:2406.04268
  - arxiv:2505.22954
  - arxiv:cs/0309048
  - arxiv:2410.04444
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:b04c61704bd4b7be
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
  - arxiv:cs/0309048@sha256:ab75c69deb1c4b41ae77f5f817735922ad52fc9a8d51ec5184f4978a88b4052e
  - arxiv:2406.04268@sha256:151c2d39de074a44985b681977a2a5383b91932b87eb734709948e9eb1607871
  - arxiv:2505.22954@sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
  - arxiv:2410.04444@sha256:d33fb4b64b53231411e0d14e65e6a3fc4f3dbfbcfe3ab4b5113f8ffa8c16cd52
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
    one_line: Routing map for recursive self improvement sources, questions, and claims.
    short: Routing map for recursive self improvement sources, questions, and claims.
    full: null
  estimated_tokens: 893
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:1b6ae1229c17cacd
- claim:2a05950fe0a0b64d
- claim:822962fc261c9559
- claim:90ae7352bb085ae8
- claim:9243c79fad41f2cb
- claim:ae45b8d667e29552
- claim:d38b49dc4376d4b0
- claim:f43359e01e4c4b0b
- claim:f810d086e0a4a305
rights_refs: []
rights_unavailable_source_refs:
- arxiv:2410.04444
- arxiv:2505.22954
- arxiv:cs/0309048
- github:jennyzzt/dgm
---

# Recursive Self Improvement

Systems that modify agents, programs, prompts, or search processes under evaluation.

## Routing questions

- What can modify itself?
- What evaluator and archive constrain change?
- How are regressions and unsafe changes detected?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) | `github` | `semantic_capsule` | 2 |
| [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) | `arxiv` | `full_text` | 2 |
| [Position: Open-Endedness is Essential for Artificial Superhuman Intelligence](../sources/arxiv-2406.04268.md) | `arxiv` | `full_text` | 1 |
| [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) | `arxiv` | `full_text` | 2 |
| [Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](../sources/arxiv-2410.04444.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (source assertion): We present the first class of mathematically rigorous, general, fully self-referential, self-improving, optimally efficient problem solvers. Inspired by Kurt G\" o del's celebrated self-referential formulas (1931), such a problem solver rewrites any part of its own code as soon as it has found a proof that the rewrite is useful, where the problem-dependent utility function and the hardware and the entire initial code 〔[claim:2a05950fe0a0b64d](../claims/claim-2a05950fe0a0b64d.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (source assertion): Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕
- **jennyzzt/dgm** (source assertion): Repository for **Darwin Gödel Machine (DGM)**, a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. 〔[claim:d38b49dc4376d4b0](../claims/claim-d38b49dc4376d4b0.md)〕
- **Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement** (source assertion): The rapid advancement of large language models (LLMs) has significantly enhanced the capabilities of agents across various tasks. However, existing agentic systems, whether based on fixed pipeline algorithms or pre-defined meta-learning frameworks, cannot search the whole agent design space due to the restriction of human-designed components, and thus might miss the more optimal agent design. 〔[claim:f810d086e0a4a305](../claims/claim-f810d086e0a4a305.md)〕

## Collector assessments

- **jennyzzt/dgm** (collection assessment): One of the clearest open implementations of a system that edits its own agent code, evaluates variants, and keeps an archive instead of overwriting a single lineage. 〔[claim:1b6ae1229c17cacd](../claims/claim-1b6ae1229c17cacd.md)〕
- **Position: Open-Endedness is Essential for Artificial Superhuman Intelligence** (collection assessment): Provides a modern formal framing of open-endedness via novelty and learnability and argues that open-ended systems are a necessary ingredient for artificial superhuman intelligence. 〔[claim:822962fc261c9559](../claims/claim-822962fc261c9559.md)〕
- **Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents** (collection assessment): A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths. 〔[claim:90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md)〕
- **Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements** (collection assessment): Foundational formal RSI work: a self-referential problem solver rewrites any part of its own code after proving that the rewrite improves expected utility. 〔[claim:9243c79fad41f2cb](../claims/claim-9243c79fad41f2cb.md)〕
- **Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement** (collection assessment): Modernizes the Goedel-machine idea for LLM agents: the agent dynamically modifies its own logic and behavior under high-level objectives rather than following a fixed human-designed optimization routine. 〔[claim:f43359e01e4c4b0b](../claims/claim-f43359e01e4c4b0b.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [jennyzzt/dgm](../sources/github-jennyzzt-dgm.md) — `explains`
- [Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](../sources/arxiv-cs-0309048.md) — `explains`
- [Position: Open-Endedness is Essential for Artificial Superhuman Intelligence](../sources/arxiv-2406.04268.md) — `explains`
- [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](../sources/arxiv-2505.22954.md) — `explains`
- [Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](../sources/arxiv-2410.04444.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement (`arxiv:2410.04444`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (`arxiv:2505.22954`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements (`arxiv:cs/0309048`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### jennyzzt/dgm (`github:jennyzzt/dgm`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
