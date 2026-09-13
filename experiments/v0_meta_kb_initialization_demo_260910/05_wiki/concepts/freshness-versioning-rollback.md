---
uid: wiki-page:freshness-versioning-and-rollback
title: Freshness, versioning, and rollback
slug: concepts/freshness-versioning-rollback
page_type: concept
status: review
summary: Page, claim, and source revisions evolve separately through dependency-aware rebuilds.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:dcf2fa8645f61032
- claim:ecdd2719fa55751c
- claim:12237a4df4847d59
- claim:3cc1779eadd83a8c
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:07439fdff0cc0aa3
- claim:1f22b83092edba2b
- claim:84c91602bd1dfb78
- claim:e7026275c099e7e2
source_refs: &id001
- arxiv:2502.14499
- standard:w3c-odrl-2.2
- arxiv:2602.06855
- arxiv-1706.08840
- arxiv:2410.05779
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2503.18102
- standard:apache-ossie
- arxiv:2406.06769
- github:VectifyAI/OpenKB
page_refs: []
outgoing_links: []
sections:
- heading: Purpose
  claim_refs: []
  source_refs: *id001
  editorial_intent: State the page's editorial purpose.
- heading: Candidate evidence
  claim_refs: *id002
  source_refs: *id001
  editorial_intent: Expose claim-backed signals without automatic admission.
- heading: Review boundary
  claim_refs: []
  source_refs: *id001
  editorial_intent: Declare unresolved review work.
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
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - standard:w3c-odrl-2.2@sha256:af187a2c26b2429a579039403f34d9a5d5f29a1e01019662043068fa1ca2beaa
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv:2410.05779@sha256:6f60088ffe7b1735ac670bfd67e7230ccfb2724bbabb7471db9854feac4733a7
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - standard:apache-ossie@sha256:ee15e76e9196d569d57ad8b65a3865e333d1891ff04791e2b2772b1edbb32eb4
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
    one_line: Page, claim, and source revisions evolve separately through dependency-aware rebuilds.
    short: Page, claim, and source revisions evolve separately through dependency-aware rebuilds.
    full: null
  estimated_tokens: 626
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# Freshness, versioning, and rollback

## Purpose

Page, claim, and source revisions evolve separately through dependency-aware rebuilds.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): amssymb amsmath adjustbox soul enumitem booktabs color xcolor bbding listings multicol xspace lmodern tablefootnote 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **ODRL Information Model 2.2** (source assertion): The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): graphicx booktabs makecell subcaption hyperref url array xcolor tikz calc xcolor amssymb comment lipsum enumitem multirow xcolor caption pifont xcolor longtable 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LightRAG: Simple and Fast Retrieval-Augmented Generation** (source assertion): Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex i 〔[claim:3cc1779eadd83a8c](../claims/claim-3cc1779eadd83a8c.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): - Commit: `c035afb7990b6077331a81e98b04efcfd9bf8184` - Default branch: `main` - Description: getzep/graphiti - Selected evidence files: 8 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Apache Ossie (incubating), formerly Open Semantic Interchange** (source assertion): # Home 〔[claim:1f22b83092edba2b](../claims/claim-1f22b83092edba2b.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **VectifyAI/OpenKB** (source assertion): - Commit: `ff54396e575ee6feb0113b631a34caa082b441cc` - Default branch: `main` - Description: VectifyAI/OpenKB - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.
