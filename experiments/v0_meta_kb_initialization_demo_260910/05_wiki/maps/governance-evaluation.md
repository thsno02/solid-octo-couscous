---
uid: wiki-page:map-governance-evaluation
title: Governance Evaluation
slug: maps/governance-evaluation
page_type: map
status: review
summary: Routing map for governance evaluation sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:17c715b34b0f0c68
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
- claim:84c91602bd1dfb78
- claim:bde139a533f9483a
- claim:ecdd2719fa55751c
source_refs: &id001
- arxiv:2602.06855
- arxiv:2502.14499
- arxiv:2406.06769
page_refs:
- wiki-page:source-a264f295a5ce5604
- wiki-page:source-3dda2384308efbda
- wiki-page:source-18c791741aa4bcd7
- wiki-page:v0-quality-gates
- wiki-page:automation-vs-editorial-review
outgoing_links:
- target: wiki-page:source-a264f295a5ce5604
  relation: explains
  claim_refs:
  - claim:ecdd2719fa55751c
  - claim:17c715b34b0f0c68
  notes: null
- target: wiki-page:source-3dda2384308efbda
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  notes: null
- target: wiki-page:source-18c791741aa4bcd7
  relation: explains
  claim_refs:
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  notes: null
- target: wiki-page:v0-quality-gates
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  - claim:ecdd2719fa55751c
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  - claim:ecdd2719fa55751c
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  source_refs:
  - arxiv:2502.14499
  - arxiv:2406.06769
  - arxiv:2602.06855
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4fd96c70e0c625fd
  - claim:bde139a533f9483a
  source_refs:
  - arxiv:2602.06855
  - arxiv:2502.14499
  - arxiv:2406.06769
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9c2a89d879277c9e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
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
  checked_at: '2026-09-13T17:38:21Z'
  max_age_days: 30
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Routing map for governance evaluation sources, questions, and claims.
    short: Routing map for governance evaluation sources, questions, and claims.
    full: null
  estimated_tokens: 455
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Governance Evaluation

Admission, factuality, review, rollback, and policy controls.

## Routing questions

- What evidence is sufficient for admission?
- How are citation and factual precision measured?
- Which changes require independent review?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) | `arxiv` | `full_text` | 2 |
| [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) | `arxiv` | `full_text` | 2 |
| [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕

## Collector assessments

- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (collection assessment): A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (collection assessment): A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring ideation, implementation, experimentation, analysis and iterative improvement. 〔[claim:4fd96c70e0c625fd](../claims/claim-4fd96c70e0c625fd.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (collection assessment): A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses, run experiments, analyze results and discover explanatory knowledge. 〔[claim:bde139a533f9483a](../claims/claim-bde139a533f9483a.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) — `explains`
- [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) — `explains`
- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `explains`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `related`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`
