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
- claim:217f2f5a6220ec41
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
- claim:dcf2fa8645f61032
- claim:ecdd2719fa55751c
source_refs: &id001
- arxiv:2602.06855
- standard:w3c-odrl-2.2
- arxiv:2502.14499
page_refs:
- wiki-page:source-a264f295a5ce5604
- wiki-page:source-ea7b53bbdfb3ba7f
- wiki-page:source-3dda2384308efbda
- wiki-page:v0-quality-gates
- wiki-page:automation-vs-editorial-review
outgoing_links:
- target: wiki-page:source-a264f295a5ce5604
  relation: explains
  claim_refs:
  - claim:ecdd2719fa55751c
  - claim:17c715b34b0f0c68
  notes: null
- target: wiki-page:source-ea7b53bbdfb3ba7f
  relation: explains
  claim_refs:
  - claim:dcf2fa8645f61032
  - claim:217f2f5a6220ec41
  notes: null
- target: wiki-page:source-3dda2384308efbda
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  notes: null
- target: wiki-page:v0-quality-gates
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:217f2f5a6220ec41
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:217f2f5a6220ec41
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:dcf2fa8645f61032
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
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  source_refs:
  - arxiv:2502.14499
  - standard:w3c-odrl-2.2
  - arxiv:2602.06855
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:217f2f5a6220ec41
  - claim:4fd96c70e0c625fd
  source_refs:
  - arxiv:2602.06855
  - standard:w3c-odrl-2.2
  - arxiv:2502.14499
  editorial_intent: Preserve collector scope.
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
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - standard:w3c-odrl-2.2@sha256:af187a2c26b2429a579039403f34d9a5d5f29a1e01019662043068fa1ca2beaa
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
    one_line: Routing map for governance evaluation sources, questions, and claims.
    short: Routing map for governance evaluation sources, questions, and claims.
    full: null
  estimated_tokens: 395
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
| [ODRL Information Model 2.2](../sources/standard-w3c-odrl-2.2.md) | `standard` | `full_text` | 2 |
| [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): amssymb amsmath adjustbox soul enumitem booktabs color xcolor bbding listings multicol xspace lmodern tablefootnote 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **ODRL Information Model 2.2** (source assertion): The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): graphicx booktabs makecell subcaption hyperref url array xcolor tikz calc xcolor amssymb comment lipsum enumitem multirow xcolor caption pifont xcolor longtable 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕

## Collector assessments

- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (collection assessment): A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕
- **ODRL Information Model 2.2** (collection assessment): Machine-readable permissions, prohibitions and duties for knowledge access and change. 〔[claim:217f2f5a6220ec41](../claims/claim-217f2f5a6220ec41.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (collection assessment): A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring ideation, implementation, experimentation, analysis and iterative improvement. 〔[claim:4fd96c70e0c625fd](../claims/claim-4fd96c70e0c625fd.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) — `explains`
- [ODRL Information Model 2.2](../sources/standard-w3c-odrl-2.2.md) — `explains`
- [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) — `explains`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `related`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`
