---
uid: wiki-page:map-knowledge-memory
title: Knowledge Memory
slug: maps/knowledge-memory
page_type: map
status: review
summary: Routing map for knowledge memory sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:419c77c89a471f8e
- claim:633b28ce5aca37bd
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:d13d2fd07c92af58
- claim:d6556415105fc41e
- claim:ef04f2ebbd2da425
- claim:f5d2f5be4a498ca2
source_refs: &id001
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv:2501.13956
- arxiv-2306.15626
- github:getzep/graphiti
page_refs:
- wiki-page:source-81e58c8add4ce203
- wiki-page:source-644f51e7e354fe05
- wiki-page:source-f4f68942b55357ed
- wiki-page:source-5be112b896547169
- wiki-page:source-2672a50bc210b0f4
- wiki-page:context-pack-routing
- wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
outgoing_links:
- target: wiki-page:source-81e58c8add4ce203
  relation: explains
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:f5d2f5be4a498ca2
  notes: null
- target: wiki-page:source-644f51e7e354fe05
  relation: explains
  claim_refs:
  - claim:12237a4df4847d59
  - claim:633b28ce5aca37bd
  notes: null
- target: wiki-page:source-f4f68942b55357ed
  relation: explains
  claim_refs:
  - claim:ef04f2ebbd2da425
  - claim:419c77c89a471f8e
  notes: null
- target: wiki-page:source-5be112b896547169
  relation: explains
  claim_refs:
  - claim:a67432ee7afb1535
  - claim:d13d2fd07c92af58
  notes: null
- target: wiki-page:source-2672a50bc210b0f4
  relation: explains
  claim_refs:
  - claim:bc85c4d0c6801c3a
  - claim:d6556415105fc41e
  notes: null
- target: wiki-page:context-pack-routing
  relation: related
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  notes: null
- target: wiki-page:llm-wiki-vs-rag-vs-knowledge-graph
  relation: related
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:07439fdff0cc0aa3
  - claim:12237a4df4847d59
  - claim:a67432ee7afb1535
  - claim:bc85c4d0c6801c3a
  - claim:ef04f2ebbd2da425
  source_refs:
  - arxiv:2503.18102
  - arxiv-1706.08840
  - arxiv-2306.15626
  - github:getzep/graphiti
  - arxiv:2501.13956
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:419c77c89a471f8e
  - claim:633b28ce5aca37bd
  - claim:d13d2fd07c92af58
  - claim:d6556415105fc41e
  - claim:f5d2f5be4a498ca2
  source_refs:
  - arxiv:2501.13956
  - arxiv-1706.08840
  - arxiv-2306.15626
  - github:getzep/graphiti
  - arxiv:2503.18102
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:f3fea76ebc259510
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2503.18102@sha256:f26720fb630b99a1ee6534baf2f49b4d8a89bdde3f6f4542b0d0c5ade40f67c0
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
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
    one_line: Routing map for knowledge memory sources, questions, and claims.
    short: Routing map for knowledge memory sources, questions, and claims.
    full: null
  estimated_tokens: 1134
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:419c77c89a471f8e
- claim:633b28ce5aca37bd
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:d13d2fd07c92af58
- claim:d6556415105fc41e
- claim:ef04f2ebbd2da425
- claim:f5d2f5be4a498ca2
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
- arxiv:2503.18102
- github:getzep/graphiti
---

# Knowledge Memory

Persistent memory, retrieval, graph organization, and temporal context.

## Routing questions

- What is stored and versioned?
- How are lexical, graph, and vector retrieval combined?
- How are freshness and provenance exposed?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) | `arxiv` | `full_text` | 2 |
| [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) | `arxiv` | `full_text` | 2 |
| [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) | `arxiv` | `full_text` | 2 |
| [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) | `arxiv` | `full_text` | 2 |
| [getzep/graphiti](../sources/github-getzep-graphiti.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕

## Collector assessments

- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (collection assessment): A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships. 〔[claim:419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md)〕
- **Gradient Episodic Memory for Continual Learning** (collection assessment): Connects memory retention to constrained updates and positive backward transfer, directly informing governed knowledge updates. 〔[claim:633b28ce5aca37bd](../claims/claim-633b28ce5aca37bd.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (collection assessment): Introduces machine-verifiable research output and retrieval over formal libraries, balancing less-verifiable natural-language research agents. 〔[claim:d13d2fd07c92af58](../claims/claim-d13d2fd07c92af58.md)〕
- **getzep/graphiti** (collection assessment): Direct engineering implementation of an agent knowledge graph that changes over time while preserving temporal history. 〔[claim:d6556415105fc41e](../claims/claim-d6556415105fc41e.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (collection assessment): A direct bridge between autonomous research and knowledge self-evolution: agent laboratories upload, retrieve and build on each others research, creating cumulative improvement across generations of work. 〔[claim:f5d2f5be4a498ca2](../claims/claim-f5d2f5be4a498ca2.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [AgentRxiv: Towards Collaborative Autonomous Research](../sources/arxiv-2503.18102.md) — `explains`
- [Gradient Episodic Memory for Continual Learning](../sources/arxiv-1706.08840.md) — `explains`
- [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](../sources/arxiv-2501.13956.md) — `explains`
- [LeanDojo: Theorem Proving with Retrieval-Augmented Language Models](../sources/arxiv-2306.15626.md) — `explains`
- [getzep/graphiti](../sources/github-getzep-graphiti.md) — `explains`
- [Context-pack routing](../methods/context-pack-routing.md) — `related`
- [LLM Wiki versus vector RAG versus knowledge graph](../comparisons/wiki-rag-kg.md) — `related`

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

### AgentRxiv: Towards Collaborative Autonomous Research (`arxiv:2503.18102`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
