---
uid: wiki-page:map-ontology-semantic-architecture
title: Ontology Semantic Architecture
slug: maps/ontology-semantic-architecture
page_type: map
status: review
summary: Routing map for ontology semantic architecture sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:068d86487f332a77
- claim:07439fdff0cc0aa3
- claim:1f22b83092edba2b
- claim:3adb88340e0eb2b6
- claim:714e301e8b2162bc
- claim:84c91602bd1dfb78
- claim:bde139a533f9483a
- claim:e7026275c099e7e2
- claim:f5d2f5be4a498ca2
- claim:fc57f26307cefee3
source_refs: &id001
- standard:apache-ossie
- arxiv:2503.18102
- github:linkml/linkml
- github:VectifyAI/OpenKB
- arxiv:2406.06769
page_refs:
- wiki-page:source-fee7c775085eb729
- wiki-page:source-81e58c8add4ce203
- wiki-page:source-8a8c72b9ad5bf51d
- wiki-page:source-332922100755365f
- wiki-page:source-18c791741aa4bcd7
- wiki-page:claim-evidence-page-compilation
- wiki-page:llm-wiki-reference-system
outgoing_links:
- target: wiki-page:source-fee7c775085eb729
  relation: explains
  claim_refs:
  - claim:1f22b83092edba2b
  - claim:068d86487f332a77
  notes: null
- target: wiki-page:source-81e58c8add4ce203
  relation: explains
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:f5d2f5be4a498ca2
  notes: null
- target: wiki-page:source-8a8c72b9ad5bf51d
  relation: explains
  claim_refs:
  - claim:fc57f26307cefee3
  - claim:3adb88340e0eb2b6
  notes: null
- target: wiki-page:source-332922100755365f
  relation: explains
  claim_refs:
  - claim:e7026275c099e7e2
  - claim:714e301e8b2162bc
  notes: null
- target: wiki-page:source-18c791741aa4bcd7
  relation: explains
  claim_refs:
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  notes: null
- target: wiki-page:claim-evidence-page-compilation
  relation: related
  claim_refs:
  - claim:068d86487f332a77
  - claim:07439fdff0cc0aa3
  - claim:1f22b83092edba2b
  - claim:3adb88340e0eb2b6
  - claim:714e301e8b2162bc
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:llm-wiki-reference-system
  relation: related
  claim_refs:
  - claim:068d86487f332a77
  - claim:07439fdff0cc0aa3
  - claim:1f22b83092edba2b
  - claim:3adb88340e0eb2b6
  - claim:714e301e8b2162bc
  - claim:84c91602bd1dfb78
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:1f22b83092edba2b
  - claim:84c91602bd1dfb78
  - claim:e7026275c099e7e2
  - claim:fc57f26307cefee3
  source_refs:
  - arxiv:2503.18102
  - standard:apache-ossie
  - arxiv:2406.06769
  - github:VectifyAI/OpenKB
  - github:linkml/linkml
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:068d86487f332a77
  - claim:3adb88340e0eb2b6
  - claim:714e301e8b2162bc
  - claim:bde139a533f9483a
  - claim:f5d2f5be4a498ca2
  source_refs:
  - standard:apache-ossie
  - github:linkml/linkml
  - github:VectifyAI/OpenKB
  - arxiv:2406.06769
  - arxiv:2503.18102
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
  - standard:apache-ossie@sha256:ee15e76e9196d569d57ad8b65a3865e333d1891ff04791e2b2772b1edbb32eb4
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
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
    one_line: Routing map for ontology semantic architecture sources, questions, and claims.
    short: Routing map for ontology semantic architecture sources, questions, and claims.
    full: null
  estimated_tokens: 537
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Ontology Semantic Architecture

Stable identity, schema, typed relations, provenance, and semantic change.

## Routing questions

- Which identifiers remain stable?
- How are schema changes migrated and rolled back?
- How are source, claim, evidence, page, time, and policy separated?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Apache Ossie (incubating), formerly Open Semantic Interchange](../sources/standard-apache-ossie.md) | `standard` | `full_text` | 2 |
| [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) | `arxiv` | `full_text` | 2 |
| [linkml/linkml](../sources/github-linkml-linkml.md) | `github` | `semantic_capsule` | 2 |
| [VectifyAI/OpenKB](../sources/github-vectifyai-openkb.md) | `github` | `semantic_capsule` | 2 |
| [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Apache Ossie (incubating), formerly Open Semantic Interchange** (source assertion): # Home 〔[claim:1f22b83092edba2b](../claims/claim-1f22b83092edba2b.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **VectifyAI/OpenKB** (source assertion): - Commit: `ff54396e575ee6feb0113b631a34caa082b441cc` - Default branch: `main` - Description: VectifyAI/OpenKB - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **linkml/linkml** (source assertion): - Commit: `0e401cef2711b0f12f5a1870805c5cfa999b0858` - Default branch: `main` - Description: linkml/linkml - Selected evidence files: 8 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Collector assessments

- **Apache Ossie (incubating), formerly Open Semantic Interchange** (collection assessment): A new vendor-neutral semantic-model interchange effort for analytics, BI and AI agents. 〔[claim:068d86487f332a77](../claims/claim-068d86487f332a77.md)〕
- **linkml/linkml** (collection assessment): Modern schema-first bridge between developer data models and linked-data/ontology artifacts. 〔[claim:3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md)〕
- **VectifyAI/OpenKB** (collection assessment): A CLI knowledge compiler with wiki foundation and downstream generators, hierarchical long-document retrieval, linting, source removal and skill compilation. 〔[claim:714e301e8b2162bc](../claims/claim-714e301e8b2162bc.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (collection assessment): A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses, run experiments, analyze results and discover explanatory knowledge. 〔[claim:bde139a533f9483a](../claims/claim-bde139a533f9483a.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (collection assessment): A direct bridge between autonomous research and knowledge self-evolution: agent laboratories upload, retrieve and build on each others research, creating cumulative improvement across generations of work. 〔[claim:f5d2f5be4a498ca2](../claims/claim-f5d2f5be4a498ca2.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Apache Ossie (incubating), formerly Open Semantic Interchange](../sources/standard-apache-ossie.md) — `explains`
- [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) — `explains`
- [linkml/linkml](../sources/github-linkml-linkml.md) — `explains`
- [VectifyAI/OpenKB](../sources/github-vectifyai-openkb.md) — `explains`
- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `explains`
- [Claim–evidence–page compilation](../methods/claim-evidence-page.md) — `related`
- [LLM Wiki reference system](../systems/reference-system.md) — `related`
