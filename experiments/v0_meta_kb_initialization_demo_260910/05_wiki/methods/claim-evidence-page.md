---
uid: wiki-page:claim-evidence-page-compilation
title: Claim–evidence–page compilation
slug: methods/claim-evidence-page
page_type: method
status: review
summary: Compile pages from atomic claims while preserving selectors and scope.
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
- wiki-page:epistemic-separation
- wiki-page:source-specific-consumption
outgoing_links:
- target: wiki-page:epistemic-separation
  relation: depends_on
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  - claim:1929edca74fa3fa5
  - claim:b281f7d7bc21b10d
  - claim:bc9a34bd8a9c7154
  notes: null
- target: wiki-page:source-specific-consumption
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
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
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
    one_line: Compile pages from atomic claims while preserving selectors and scope.
    short: Compile pages from atomic claims while preserving selectors and scope.
    full: null
  estimated_tokens: 1880
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
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
rights_refs:
- source_uid: arxiv:2406.06769
  source_revision: sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  source_version_url: https://arxiv.org/abs/2406.06769v2
  license_spdx: CC-BY-SA-4.0
  license_url: https://creativecommons.org/licenses/by-sa/4.0/
  notice_path: raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:84c91602bd1dfb78
- source_uid: methodology:linkml-schema-first
  source_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  source_version_url: https://linkml.io/linkml/
  license_spdx: Apache-2.0
  license_url: https://www.apache.org/licenses/LICENSE-2.0
  notice_path: raw_data/licenses/apache-2.0.md
  package_path: materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:583280271287ef9c
rights_unavailable_source_refs:
- arxiv:2305.14251
- arxiv:2305.14627
- arxiv:2402.14207
- arxiv:2502.14499
- arxiv:2509.23233
- arxiv:2511.02824
- arxiv:2602.06855
- github:VectifyAI/OpenKB
- github:linkml/linkml
- github:xoai/sage-wiki
---

# Claim–evidence–page compilation

## Purpose

Compile pages from atomic claims while preserving selectors and scope.

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

## Compiler contract

Inputs are pinned source revisions, atomic claims, evidence selectors, schema/identity versions, policy, and bounded scope. Outputs are candidate pages, typed links, semantic diff, validation, review queue, and rollback.

## Related pages

- [Epistemic separation](../concepts/epistemic-separation.md) — `depends_on`
- [Source-specific consumption](../concepts/source-specific-consumption.md) — `depends_on`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e`
- Source version: [pinned upstream version](https://arxiv.org/abs/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md](../../../../raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md)
- Attribution: "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents", arXiv:2406.06769v2, by Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord and Peter Clark, https://arxiv.org/abs/2406.06769v2, licensed under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/. source/neurips_data_2024.sty is an independent NeurIPS Data 2024 template component with its original Lora Aroyo credit and attribution to Roman Garnett and the many authors of nips15submit_e.sty, including MK and drstrip@sandia, retained. Its corresponding licensed original template expression is identified in the NeurIPS 2026 Program Chairs' official "Formatting Instructions For NeurIPS 2026", https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc, explicitly declared CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. The corresponding official current source is https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip, checked on 2026-09-16. The retained 2024 Data variant is packaged using this corresponding-expression/adaptation path, not a claim that the historical 2024 ZIP declared an overall CC BY 4.0 license. The retained member is also identified by the official 2024 Data bundle, https://media.neurips.cc/Conferences/NeurIPS2024/NeurIPS-Dataset-Styles.zip, linked from https://neurips.cc/Conferences/2024/CallForDatasetsBenchmarks. None of these attributions implies endorsement of this repository.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. All nine text source members of the fixed v2 archive are retained unchanged, including related_work-v1-old.tex. The existing normalized/document.tex and all 74 selectors are preserved byte-for-byte. The original 94,506-byte normalized/document.txt is preserved as an exact prefix; only the complete attribution, changes, scope and NOTICE link are appended to its end. Compared with the currently reviewed official NeurIPS 2026 style, the retained Data 2024 style has the Lora Aroyo header, its 2024/04/30 package identifier, the anonymous default/option and @submission boolean mapping, and the @submission test in the title block; its meeting identifiers are 38th/2024 and its existing location string is "Vancouver, USA". It retains "Preprint. Under review." and the Datasets and Benchmarks track footer. The lineno/amsmath compatibility block appears earlier in the retained style rather than at the current style's end; its closing-brace layout differs. The retained style uses the 2024 package warning identifier and a space between each checklist answer label and its argument. It lacks the current multi-track, position/eandd/creativeai/education/workshop/nonanonymous options, minimum font-size overrides, acknowledgement-hiding block and justificationTODO command. Long formatting and compatibility expressions correspond to the currently licensed original; version labels, short footer text and routine functional adaptations are separately disclosed. These differences are pre-existing and are not introduced, repaired or attributed to a newly asserted modifier by this repository. No historical template download identity, historical 2024 BY4 declaration or byte-identical correspondence to the complete current style is claimed.
- Scope: 本包仅覆盖固定 arXiv 2406.06769v2 的九个 source 文字成员、normalized/document.tex、normalized/document.txt 与 74 个定位器（selectors）。作者/提交者有权许可的论文源表达及其文本转换，包括保留的旧稿，按 CC BY-SA 4.0 共享；改编材料继续按该许可同方式共享。source/neurips_data_2024.sty 是独立第三方模板，按当前官方模板的对应授权表达及 CC BY 4.0 复制/改编路径分别署名，保留其既存短常规功能适配，不将历史 2024 ZIP 宣称为整体 BY4，也不将模板著作权归论文作者。两许可按组件分别适用，不将整仓库重新许可为 BY-SA4 或 BY4；定位器不改变所定位组件的许可。DiscoveryWorld.bbl 是书目记录，不授权所引作品；未保存的五个非文本媒体、外链代码/模型/数据、商标及专利不在本许可包范围。没有删除任何已保存源文字以回避许可条件，不施加额外限制或暗示上游支持。

### LinkML schema-first knowledge modeling (`methodology:linkml-schema-first`)

- Components: `claim:583280271287ef9c`
- Source revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Source version: [pinned upstream version](https://linkml.io/linkml/)
- License: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
- NOTICE: [raw_data/licenses/apache-2.0.md](../../../../raw_data/licenses/apache-2.0.md)
- Attribution: This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. Converted the captured LinkML HTML landing page to Markdown; navigation, headings, hyperlinks, whitespace, and footnote markers were omitted or normalized, while CSS, JavaScript, theme files, and media were not stored; 164 selector excerpts were generated. The upstream copyright and Apache-2.0 statement are restored in this attribution block.
- Scope: 仅覆盖当前 https://linkml.io/linkml/ 单页经转换后、许可附注前的 7,340-byte 既有 Markdown 正文及其 164 个 selector 摘录；不声称存储或覆盖 LinkML 整个文档站、其他页面正文、主题、JavaScript、CSS、媒体、外链作品、商标或权利人无权许可的第三方材料。

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation (`arxiv:2305.14251`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models (`arxiv:2402.14207`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models (`arxiv:2509.23233`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### Kosmos: An AI Scientist for Autonomous Discovery (`arxiv:2511.02824`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### VectifyAI/OpenKB (`github:VectifyAI/OpenKB`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### xoai/sage-wiki (`github:xoai/sage-wiki`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
