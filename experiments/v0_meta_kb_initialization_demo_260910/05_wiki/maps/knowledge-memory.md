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
  build_id: build:llm-wiki-v0:7825e3978fb6a0ee
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2503.18102@sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
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
  estimated_tokens: 1240
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
- source_uid: arxiv:2503.18102
  source_revision: sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
  source_version_url: https://arxiv.org/pdf/2503.18102v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2503.18102--1133e9d5/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:07439fdff0cc0aa3
rights_unavailable_source_refs:
- arxiv-1706.08840
- arxiv-2306.15626
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

### AgentRxiv: Towards Collaborative Autonomous Research (`arxiv:2503.18102`)

- Components: `claim:07439fdff0cc0aa3`
- Source revision: `sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2503.18102v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md)
- Attribution: Samuel Schmidgall; Michael Moor, AgentRxiv: Towards Collaborative Autonomous Research, arXiv:2503.18102v1 (2025-03-23), https://arxiv.org/abs/2503.18102v1, PDF https://arxiv.org/pdf/2503.18102v1, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。实际当前PDF两作者按序Samuel Schmidgall; Michael Moor。1 Department of Electrical & Computer Engineering, Johns Hopkins University；2 Department of Biosystems Science & Engineering, ETH Zurich；Samuel Schmidgall通讯sschmi46@jhu.edu。固定v1侧边日期23 Mar 2025与题名页右上2025-3-25独立保留，不以pagehead或Creation/ModDate覆盖提交事实。p27 National Science Foundation Graduate Research Fellowship, Grant No. DGE 2139757支持信用保留，不暗示NSF/作者/机构背书。p1 Figure1网页列表截图另文Agent Laboratory: Using LLM Agents as Research Assistants，实际九作者按序Samuel Schmidgall、Yusheng Su、Ze Wang、Ximeng Sun、Jialian Wu、Xiaodong Yu、Jiang Liu、Zicheng Liu、Emad Barsoum，不含Michael Moor、不混入当前两作者。图中打印arXiv:2501.04227 [pdf, other]为bare ID、没有vN或完整URL；有限六显示行约52个空白tokens摘要预览起Historically, scientific discovery...，止accepts a human-provide...并有More，是原图已截断预览、非完整摘要/全文。若需定位 https://arxiv.org/abs/2501.04227 只按可见ID生成locator，不称本批核定另文固定版/取得全文；p24书目独立信用、Figures2/3研究上下文按原件保留。当前p1 AgentRxiv.github.io项目链接保留。只保存本PDF中实际有限展示与信用，不单独再许可另篇整文或底层媒体，也不新增抓取/许可函退出条件。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 本次唯一固定版GET的2757188 bytes原PDF按字节原样保留，不编辑/重导/重排/OCR。既有helper以plain全页提取生成独立pdf-supplement/document.txt与实际新PDF revision绑定的逐页selectors；页标题/定位和唯一文末归属/修改/范围footer为collector表示元数据，native不是作者另交原始文本或byte-exact executable prompt/code。NOTICE自包含实际署名/独立信用/来源/范围/损失与既有完整CC BY4法律文本，notice_path自绑定本文件，不新rawlicense资产。本primary_excerpt仅声明同一native Page1实际父摘要L9–23，不修改原文。旧root source/normalized/selectors/NOTICE/README/files及revision/retrieval/rights/gate/source_version键缺省不改，不把新选版回溯为旧bare archive GET的已证版次。
- Scope: 本独立表示只覆盖本UID固定arXiv:2503.18102v1原bytes不改的29页compiled PDF（2757188 bytes）：固定arXiv:2503.18102v1完整29物理页编译论文：p1父摘要/Figure1，p2–17主文、六活动图、单/三实验室结果、Failure/Ethics/Discussion/实际Conclusion，p17–27 References，p27 Acknowledgments，p28 A.Algorithms与B.Agent Laboratory configuration，p29配置表/B.3/真实C.Prompts结尾。末句All prompts are the same as in Schmidgall et al. (2025).是正常引用，原件未列另一论文完整prompt，不递归取另文。 论文作者可许可表达依本固定作品已证CC BY4路径；图表/参考文献/实际有限引述保存其原信用，不外推standalone被引作品/素材/程序/代码/数据/媒体/服务/模型/权重/模板的一般许可。范围含该PDF派生有损native plain、revision-bound逐页selectors及完整NOTICE；不执行被审指令、不重新打包外链、不改变底层许可、不为已许可权利添加下游限制，无普遍权利保证，不授商标/专利。当前原图有限另文列表/截图/摘要预览在此出版表示内原样保留并落实九作者与bareID信用，不扩大为另文独立全文或底层图片/角色/程序/数据的一般许可。旧bib LUMI-lab长摘要和competing-interest/patent声明未在此实际PDF出现；p4简短介绍/p18普通书目不等于旧完整摘要，其NC-ND用途/转换条件与旧GDM BY-SA4、ICLR/LPPL等组件/root block保持，不外推到整个新PDF也不因新BY4放行旧source。

### Gradient Episodic Memory for Continual Learning (`arxiv-1706.08840`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (`arxiv-2306.15626`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
