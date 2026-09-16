---
uid: wiki-page:llm-wiki-reference-system
title: LLM Wiki reference system
slug: systems/reference-system
page_type: system
status: review
summary: End-to-end architecture from frozen sources to reviewed pages and context packs.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
page_refs:
- wiki-page:claim-evidence-page-compilation
- wiki-page:context-pack-routing
- wiki-page:freshness-versioning-and-rollback
- wiki-page:v0-quality-gates
outgoing_links:
- target: wiki-page:claim-evidence-page-compilation
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:context-pack-routing
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
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
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:464b90323fe86f3e
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
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
    one_line: End-to-end architecture from frozen sources to reviewed pages and context packs.
    short: End-to-end architecture from frozen sources to reviewed pages and context packs.
    full: null
  estimated_tokens: 783
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LLM Wiki reference system

## Purpose

End-to-end architecture from frozen sources to reviewed pages and context packs.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Architecture

```text
immutable source revisions
→ normalized artifacts and selectors
→ atomic claims and evidence
→ identity and ontology mapping
→ PagePlan and candidate Markdown
→ deterministic and semantic evaluation
→ review and admission
→ indexes, graph, context packs, and change feed
```

## Related pages

- [Claim–evidence–page compilation](../methods/claim-evidence-page.md) — `depends_on`
- [Context-pack routing](../methods/context-pack-routing.md) — `depends_on`
- [Freshness, versioning, and rollback](../concepts/freshness-versioning-rollback.md) — `depends_on`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `evaluates`
