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
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:0edb741be0f31f6f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
- arxiv:2511.02824
- methodology:linkml-schema-first
- github:linkml/linkml
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
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  notes: null
- target: wiki-page:grounded-long-form-synthesis
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  notes: null
- target: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
  relation: compares_with
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  notes: null
- target: wiki-page:materialization-and-trust-gaps
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
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
  created_at: '2026-09-13T17:38:21Z'
  updated_at: '2026-09-13T17:38:21Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-13T17:38:21Z'
provenance:
  build_id: build:llm-wiki-v0:9406f28f613dfbd5
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  - arxiv:2511.02824@sha256:6c71312f8e88b313baf4eeb44a39fefa9f09ad5bd247e176e49824310cf5fb5e
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
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
    one_line: Evidence-linked, review-gated knowledge compilation layer.
    short: Evidence-linked, review-gated knowledge compilation layer.
    full: null
  estimated_tokens: 710
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LLM Wiki overview

## Purpose

Evidence-linked, review-gated knowledge compilation layer.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depth of their findings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕
- **LinkML schema-first knowledge modeling** (source assertion): LinkML is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Current release

This candidate build covers **36** selected sources and **71** claims. Trusted claims remain **0**.

## Related pages

- [LLM Wiki reference system](../systems/reference-system.md) — `explains`
- [Grounded long-form synthesis](../methods/grounded-synthesis.md) — `explains`
- [LLM Wiki versus vector RAG versus knowledge graph](../comparisons/wiki-rag-kg.md) — `compares_with`
- [Materialization, evidence, and trust gaps](../gaps/evidence-and-trust.md) — `depends_on`
