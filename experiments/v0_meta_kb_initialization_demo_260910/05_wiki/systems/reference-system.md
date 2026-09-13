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
- claim:dcf2fa8645f61032
- claim:ecdd2719fa55751c
- claim:12237a4df4847d59
- claim:3cc1779eadd83a8c
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bed2f056ecd73c69
- claim:d9cc223138eb5da3
source_refs: &id001
- arxiv:2502.14499
- standard:w3c-odrl-2.2
- arxiv:2602.06855
- arxiv-1706.08840
- arxiv:2410.05779
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2408.15232
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
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:context-pack-routing
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
  - claim:a67432ee7afb1535
  notes: null
- target: wiki-page:v0-quality-gates
  relation: evaluates
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:dcf2fa8645f61032
  - claim:ecdd2719fa55751c
  - claim:12237a4df4847d59
  - claim:3cc1779eadd83a8c
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
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - arxiv:2408.15232@sha256:19f115dc7b47921012b68ca5b991bf5f63c5b5ca54f3faddf895ea8e963b54fa
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
    one_line: End-to-end architecture from frozen sources to reviewed pages and context packs.
    short: End-to-end architecture from frozen sources to reviewed pages and context packs.
    full: null
  estimated_tokens: 781
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
---

# LLM Wiki reference system

## Purpose

End-to-end architecture from frozen sources to reviewed pages and context packs.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): amssymb amsmath adjustbox soul enumitem booktabs color xcolor bbding listings multicol xspace lmodern tablefootnote 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **ODRL Information Model 2.2** (source assertion): The Open Digital Rights Language (ODRL) is a policy expression language that provides a flexible and interoperable information model, vocabulary, and encoding mechanisms for representing statements about the usage of content and services. The ODRL Information Model describes the underlying concepts, entities, and relationships that form the foundational basis for the semantics of the ODRL policies. 〔[claim:dcf2fa8645f61032](../claims/claim-dcf2fa8645f61032.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): graphicx booktabs makecell subcaption hyperref url array xcolor tikz calc xcolor amssymb comment lipsum enumitem multirow xcolor caption pifont xcolor longtable 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LightRAG: Simple and Fast Retrieval-Augmented Generation** (source assertion): Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex i 〔[claim:3cc1779eadd83a8c](../claims/claim-3cc1779eadd83a8c.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): - Commit: `c035afb7990b6077331a81e98b04efcfd9bf8184` - Default branch: `main` - Description: getzep/graphiti - Selected evidence files: 8 of 21 files observed - Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations** (source assertion): While language model (LM)-powered chatbots and generative search engines excel at answering concrete queries, discovering information in the terrain of unknown unknowns remains challenging for users. To emulate the common educational scenario where children/students learn by listening to and participating in conversations with their parents/teachers, we create Collaborative STORM ( ). 〔[claim:d9cc223138eb5da3](../claims/claim-d9cc223138eb5da3.md)〕

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
