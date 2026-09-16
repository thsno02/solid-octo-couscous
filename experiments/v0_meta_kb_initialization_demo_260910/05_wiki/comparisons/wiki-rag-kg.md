---
uid: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
title: LLM Wiki versus vector RAG versus knowledge graph
slug: comparisons/wiki-rag-kg
page_type: comparison
status: review
summary: Compare admission, provenance, organization, freshness, and consumption.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id002
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:0edb741be0f31f6f
source_refs: &id001
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2402.14207
- arxiv:2305.14251
- arxiv:2509.23233
- arxiv:2305.14627
- github:VectifyAI/OpenKB
- github:xoai/sage-wiki
- arxiv:2511.02824
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
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:a907f5d1be8430c2
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv:2402.14207@sha256:28b57e9821da798bf8ccfa3f144bfa37cd96ff3582c2211c83eff5ffcf0ccfc2
  - arxiv:2305.14251@sha256:57414a8d80031dceed44fb17efa562cab7e1490390ce95d8753480fba9686795
  - arxiv:2509.23233@sha256:8570de4224cfc829f7478411feca2ecec5f50d6e7ceb7cc62fd15fa07f20c921
  - arxiv:2305.14627@sha256:6902aae852b39f761a60dc2cf36b7d2ed9e615755f413b7daa8b52f5c1eae3ea
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  - arxiv:2511.02824@sha256:6c71312f8e88b313baf4eeb44a39fefa9f09ad5bd247e176e49824310cf5fb5e
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
    one_line: Compare admission, provenance, organization, freshness, and consumption.
    short: Compare admission, provenance, organization, freshness, and consumption.
    full: null
  estimated_tokens: 1692
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:1929edca74fa3fa5
- claim:b281f7d7bc21b10d
- claim:bc9a34bd8a9c7154
- claim:bed2f056ecd73c69
- claim:e7026275c099e7e2
- claim:e7ac7da9ac39e47d
- claim:0edb741be0f31f6f
rights_refs:
- source_uid: arxiv:2501.13956
  source_revision: sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  source_version_url: https://arxiv.org/abs/2501.13956v1
  license_spdx: CC-BY-NC-SA-4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
  notice_path: raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md
  package_path: materialized_sources/corpus/arxiv-2501.13956--b93a114f/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ef04f2ebbd2da425
rights_unavailable_source_refs:
- arxiv-1706.08840
- arxiv-2306.15626
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2402.14207
- arxiv:2503.18102
- arxiv:2509.23233
- arxiv:2511.02824
- github:VectifyAI/OpenKB
- github:getzep/graphiti
- github:xoai/sage-wiki
---

# LLM Wiki versus vector RAG versus knowledge graph

## Purpose

Compare admission, provenance, organization, freshness, and consumption.

## Candidate evidence

- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models** (source assertion): We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. 〔[claim:1929edca74fa3fa5](../claims/claim-1929edca74fa3fa5.md)〕
- **FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation** (source assertion): Evaluating the factuality of long-form text generated by large language models (LMs) is non-trivial because (1) generations often contain a mixture of supported and unsupported pieces of information, making binary judgments of quality inadequate, and (2) human evaluation is time-consuming and costly. In this paper, we introduce , a new evaluation that breaks a generation into a series of atomic facts and computes the 〔[claim:b281f7d7bc21b10d](../claims/claim-b281f7d7bc21b10d.md)〕
- **Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models** (source assertion): Wikipedia is the largest open knowledge corpus, widely used worldwide and serving as a key resource for training large language models (LLMs) and retrieval-augmented generation (RAG) systems. Ensuring its accuracy is therefore critical. 〔[claim:bc9a34bd8a9c7154](../claims/claim-bc9a34bd8a9c7154.md)〕
- **Enabling Large Language Models to Generate Text with Citations** (source assertion): Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to hallucination. In this work, our aim is to allow LLMs to generate text with citations , improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕
- **VectifyAI/OpenKB** (source assertion): **OpenKB (Open Knowledge Base)** is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs, powered by [**PageIndex**](https://github.com/VectifyAI/PageIndex)'s vectorless, reasoning-based retrieval for long documents. 〔[claim:e7026275c099e7e2](../claims/claim-e7026275c099e7e2.md)〕
- **xoai/sage-wiki** (source assertion): **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together. Drop in documents; an LLM compiler turns them into an interlinked wiki with a knowledge graph — agents query it through MCP, humans browse it as plain markdown. 〔[claim:e7ac7da9ac39e47d](../claims/claim-e7ac7da9ac39e47d.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depth of their findings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Comparison axes

| Layer | Primary strength | Admission | Provenance | Human navigation |
|---|---|---|---|---|
| vector RAG | recall | usually none | chunk-level | weak |
| knowledge graph | typed relations | implementation-dependent | edge/node-level | moderate |
| LLM Wiki | governed synthesis | proposal/review/merge | page→claim→evidence | strong |

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory (`arxiv:2501.13956`)

- Components: `claim:ef04f2ebbd2da425`
- Source revision: `sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51`
- Source version: [pinned upstream version](https://arxiv.org/abs/2501.13956v1)
- License: [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- NOTICE: [raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md](../../../../raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md)
- Attribution: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory", arXiv:2501.13956v1, by Preston Rasmussen; Pavlo Paliychuk; Travis Beauvais; Jack Ryan; and Daniel Chalef. Source: https://arxiv.org/abs/2501.13956v1. The article-author material is licensed under CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/. This repository has not yet verified that its intended publication is NonCommercial; this package is not a publication approval. source/PRIMEarxiv.sty corresponds to the Arxiv & PRIME AI Style Template adapted by Moulay A. Akhloufi, https://www.overleaf.com/latex/templates/arxiv-and-prime-ai-style-template/qdnhqytdqzsc, licensed under CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. That adaptation is based on George Kour's arxiv-style, https://github.com/kourgeorge/arxiv-style; its base portions retain Copyright (c) 2020 George Kour and the MIT License. The retained Zep style enables the page footer that the otherwise matching PaperQA2 copy comments out; the modifier of this one-line variant is unknown and is not attributed to the paper authors.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The fixed v1 source archive is unpacked and its four text members—source/main.tex, source/main.bbl, source/references.bib, and source/PRIMEarxiv.sty—are retained without modification. main.tex is copied to normalized/document.tex and converted to normalized/document.txt; 29 selectors are generated; the article attribution, Moulay A. Akhloufi template attribution, George Kour MIT notice, modification statement, and NOTICE link are appended to normalized/document.txt. For provenance, the retained Zep PRIMEarxiv.sty is recorded as differing from the otherwise matching PaperQA2 copy only at line 35 by enabling the page footer; this packaging does not identify the author of that pre-existing variant.
- Scope: 本组合包仅覆盖固定 arXiv v1 胶囊实际保存的四个 source 文字成员、normalized/document.tex、normalized/document.txt 与 29 个 selector。论文作者材料及其文本转换和 selector 派生物按 CC BY-NC-SA 4.0 履约，任何共享仅限非商业用途，派生输出须采用同一或兼容许可；当前仓库用途尚未完成非商业核实，故本包不表示发布已获准，未来商业用途须另行取得授权。source/PRIMEarxiv.sty 作为 Moulay A. Akhloufi 改编的 PRIME 模板按 CC BY 4.0 履约，并对其所基于的 George Kour arxiv-style 保留 MIT 版权和许可；Zep 所存版本相对 PaperQA2 对应副本仅启用第 35 行页脚，本包记录该差异但不把修改归给论文作者。main.bbl 与 references.bib 作为排版记录和引用元数据保留，不授权其所引用作品。许可不外推到外链论文、代码、数据或权利人无权许可的第三方材料。

### Gradient Episodic Memory for Continual Learning (`arxiv-1706.08840`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (`arxiv-2306.15626`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AgentRxiv: Towards Collaborative Autonomous Research (`arxiv:2503.18102`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models (`arxiv:2509.23233`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Kosmos: An AI Scientist for Autonomous Discovery (`arxiv:2511.02824`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
