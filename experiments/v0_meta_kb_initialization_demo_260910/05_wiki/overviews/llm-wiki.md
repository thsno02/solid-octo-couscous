---
uid: wiki-page:llm-wiki-overview
title: LLM Wiki overview
slug: overviews/llm-wiki
page_type: overview
status: review
summary: Evidence-linked, review-gated knowledge compilation layer.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:dcf2fa8645f61032
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bed2f056ecd73c69
- claim:d9cc223138eb5da3
- claim:e7ac7da9ac39e47d
- claim:07439fdff0cc0aa3
- claim:1f22b83092edba2b
- claim:84c91602bd1dfb78
- claim:e7026275c099e7e2
source_refs: &id001
- arxiv:2502.14499
- standard:w3c-odrl-2.2
- arxiv:2602.06855
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2408.15232
- github:xoai/sage-wiki
- arxiv:2503.18102
- standard:apache-ossie
- arxiv:2406.06769
- github:VectifyAI/OpenKB
page_refs:
- wiki-page:llm-wiki-reference-system
- wiki-page:grounded-long-form-synthesis
- wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
- wiki-page:materialization-and-trust-gaps
outgoing_links:
- target: wiki-page:llm-wiki-reference-system
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bed2f056ecd73c69
  notes: null
- target: wiki-page:grounded-long-form-synthesis
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bed2f056ecd73c69
  notes: null
- target: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
  relation: compares_with
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bed2f056ecd73c69
  notes: null
- target: wiki-page:materialization-and-trust-gaps
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bed2f056ecd73c69
  notes: null
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
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - arxiv:2408.15232@sha256:19f115dc7b47921012b68ca5b991bf5f63c5b5ca54f3faddf895ea8e963b54fa
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
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
    one_line: Evidence-linked, review-gated knowledge compilation layer.
    short: Evidence-linked, review-gated knowledge compilation layer.
    full: null
  estimated_tokens: 691
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LLM Wiki overview

## Purpose

Evidence-linked, review-gated knowledge compilation layer.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): amssymb amsmath adjustbox soul enumitem booktabs color xcolor bbding listings multicol xspace lmodern tablefootnote 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **ODRL Information Model 2.2** (source assertion): The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): graphicx booktabs makecell subcaption hyperref url array xcolor tikz calc xcolor amssymb comment lipsum enumitem multirow xcolor caption pifont xcolor longtable 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations** (source assertion): While language model (LM)-powered chatbots and generative search engines excel at answering concrete queries, discovering information in the terrain of unknown unknowns remains challenging for users. To emulate the common educational scenario where children/students learn by listening to and participating in conversations with their parents/teachers, we create Collaborative STORM ( ). 〔[claim:d9cc223138eb5da3](../claims/claim-d9cc223138eb5da3.md)〕
- **xoai/sage-wiki** (source assertion): - Commit: `ab36031ace701fb1e3c620323d138a90a450f48d` - Default branch: `main` - Description: xoai/sage-wiki - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Apache Ossie (incubating), formerly Open Semantic Interchange** (source assertion): # Home 〔[claim:1f22b83092edba2b](../claims/claim-1f22b83092edba2b.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **VectifyAI/OpenKB** (source assertion): - Commit: `ff54396e575ee6feb0113b631a34caa082b441cc` - Default branch: `main` - Description: VectifyAI/OpenKB - Selected evidence files: 4 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Current release

This candidate build covers **36** selected sources and **72** claims. Trusted claims remain **0**.

## Related pages

- [LLM Wiki reference system](../systems/reference-system.md) — `explains`
- [Grounded long-form synthesis](../methods/grounded-synthesis.md) — `explains`
- [LLM Wiki versus vector RAG versus knowledge graph](../comparisons/wiki-rag-kg.md) — `compares_with`
- [Materialization, evidence, and trust gaps](../gaps/evidence-and-trust.md) — `depends_on`
