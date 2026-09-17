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
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:0edb741be0f31f6f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
- claim:17c715b34b0f0c68
source_refs: &id001
- arxiv:2502.14499
- arxiv:2406.06769
- arxiv:2602.06855
- arxiv:2503.18102
- arxiv-1706.08840
- arxiv-2306.15626
- github:getzep/graphiti
- arxiv:2501.13956
- arxiv:2511.02824
- methodology:linkml-schema-first
- github:linkml/linkml
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
  build_id: build:llm-wiki-v0:bdc4c9116985ab25
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2503.18102@sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
  - arxiv-1706.08840@sha256:330858b30f0963297c9d772fc29aabc8dfcff7d687856d91a2f167847d0fca88
  - arxiv-2306.15626@sha256:5893d0b64b077ec01bee907ead6d94ae8c810abf023c2b4f618250c4fb0b7680
  - github:getzep/graphiti@c035afb7990b6077331a81e98b04efcfd9bf8184
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  - arxiv:2511.02824@sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8
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
    one_line: Page, claim, and source revisions evolve separately through dependency-aware rebuilds.
    short: Page, claim, and source revisions evolve separately through dependency-aware rebuilds.
    full: null
  estimated_tokens: 2168
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:4bf5ea8e6b4e37de
- claim:84c91602bd1dfb78
- claim:ecdd2719fa55751c
- claim:07439fdff0cc0aa3
- claim:12237a4df4847d59
- claim:a67432ee7afb1535
- claim:bc85c4d0c6801c3a
- claim:ef04f2ebbd2da425
- claim:0edb741be0f31f6f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
- claim:17c715b34b0f0c68
rights_refs:
- source_uid: arxiv:2406.06769
  source_revision: sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91
  source_version_url: https://arxiv.org/pdf/2406.06769v2
  license_spdx: CC-BY-SA-4.0
  license_url: https://creativecommons.org/licenses/by-sa/4.0/
  notice_path: raw_data/licenses/p3-pdf-02-discoveryworld-v2.md
  package_path: materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:84c91602bd1dfb78
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
- source_uid: arxiv:2511.02824
  source_revision: sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8
  source_version_url: https://arxiv.org/pdf/2511.02824v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2511.02824--1c218a8e/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:0edb741be0f31f6f
- source_uid: methodology:linkml-schema-first
  source_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  source_version_url: https://linkml.io/linkml/
  license_spdx: Apache-2.0 AND MIT
  license_url: https://www.apache.org/licenses/LICENSE-2.0
  notice_path: raw_data/licenses/linkml-page-body-02-260917.md
  package_path: materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:583280271287ef9c
rights_unavailable_source_refs:
- arxiv-1706.08840
- arxiv-2306.15626
- arxiv:2502.14499
- arxiv:2602.06855
- github:getzep/graphiti
- github:linkml/linkml
---

# Freshness, versioning, and rollback

## Purpose

Page, claim, and source revisions evolve separately through dependency-aware rebuilds.

## Candidate evidence

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent’s capacity for end- to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕
- **AgentRxiv: Towards Collaborative Autonomous Research** (source assertion): Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕
- **Gradient Episodic Memory for Continual Learning** (source assertion): One major obstacle towards AI is the poor ability of models to solve new problems quicker, and without forgetting previously acquired knowledge. To better understand this issue, we study the problem of continual learning, where the model observes, once and one by one, examples concerning a sequence of tasks. 〔[claim:12237a4df4847d59](../claims/claim-12237a4df4847d59.md)〕
- **LeanDojo: Theorem Proving with Retrieval-Augmented Language Models** (source assertion): Large language models (LLMs) have shown promise in proving formal theorems using proof assistants such as Lean. However, existing methods are difficult to reproduce or build on, due to private code, data, and large compute requirements. 〔[claim:a67432ee7afb1535](../claims/claim-a67432ee7afb1535.md)〕
- **getzep/graphiti** (source assertion): ⭐ *Help us reach more developers and grow the Graphiti community. 〔[claim:bc85c4d0c6801c3a](../claims/claim-bc85c4d0c6801c3a.md)〕
- **Zep: A Temporal Knowledge Graph Architecture for Agent Memory** (source assertion): We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depthoftheirfindings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕
- **LinkML schema-first knowledge modeling** (source assertion): Everything you need to know about [LinkML](https://linkml.io), the Linked Data Modeling Language. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (collection assessment): A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕

## Compiled interpretation

This page reorganizes candidate knowledge around a stable reader task. It is not source concatenation and it does not turn retrieval, maintainer claims, preprints, or generated prose into verified truth.

## Review boundary

Check evidence entailment, source independence, contradiction, neutrality, due weight, freshness, and downstream impact before publication.

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/p3-pdf-02-discoveryworld-v2.md](../../../../raw_data/licenses/p3-pdf-02-discoveryworld-v2.md)
- Attribution: Peter Jansen; Marc-Alexandre Côté; Tushar Khot; Erin Bransom; Bhavana Dalvi Mishra; Bodhisattwa Prasad Majumder; Oyvind Tafjord; Peter Clark. "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents". Fixed arXiv 2406.06769v2, https://arxiv.org/abs/2406.06769v2; original PDF https://arxiv.org/pdf/2406.06769v2. Article expression the authors/submitter may license is available under CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/; full legal code https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Fixed article/PDF license checked in this batch on 2026-09-16. PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 No endorsement or additional right to external works/models/trademarks is implied.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按实际下载 bytes 原样保存，不编辑或重导出；复用既有 pypdf plain 提取逐页文字，加入明确页边界并生成独立页定位；在派生 text 末尾附唯一署名、修改、范围声明及完整 NOTICE.md 链接。plain 文字保留原抽取结果，不做 OCR、不运行 TeX、论文代码或提示词，不将图形、数学排版或阅读顺序损失隐藏为完整。旧 source、normalized、default selectors、NOTICE、files、archive revision/retrieval 和旧许可包全部保留，不新增 trusted。 适用论文表达/页文字及后续改编沿 BY-SA4 同方式共享，不重许可整个仓库。
- Scope: 仅本次从 https://arxiv.org/pdf/2406.06769v2 取得的固定 v2 官方完整 PDF（29 页，3054585 bytes）、其 plain 页文字与独立页定位器。范围为完整主文、全部附录、四幅实际科学图（p2/3/18/29），真实末尾 p29 Save failures/Windows autosave 用户数据丢失说明。作者/提交者有权许可的论文表达与本次文字派生沿作品级 CC BY-SA 4.0；PDF p9 致谢与 p13 checklist 的实际信用：作者购买 CuteRPG/PixyMoon 素材并说明 attribution 要求；原论文截图中的 CuteRPG 素材归属 PixyMoon，产品页 https://pixymoon.itch.io/2d-topdown-cute-rpg-world 。本批已核该具体产品页允许 personal/commercial project use、modify/edit，要求 Credit PixyMoon，禁止 resell asset pack。科学主题增改归论文作者及 OpenAI DALL-E。完整论文内已合成截图保留这些实际信用，不提供或授权独立提取、转售或再分发底层 asset pack，不冒称 sprite 素材获得 CC BY-SA 4.0，也不把资产包条款施加到论文作者有权许可的原创 BY-SA 部分。 论文作者有权许可的原创表达/页文字及后续改编继续 BY-SA4；具体资产边界不施于这些原创 BY-SA 部分，不整库重许可。完整 PDF 原有署名、资助、图注、引文、警告和第三方信用原样保留，不授权外部被引作品全文、模型、代码、脚本或数据，不转授商标、专利或许可者无权许可材料。PDF 原字节不编辑/重导出，plain 文字有损、不做 OCR，原件完整不等于 text extraction complete。旧 source/normalized/default selectors/NOTICE/files/archive revision/retrieval/旧组件授权包不变。

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

### Kosmos: An AI Scientist for Autonomous Discovery (`arxiv:2511.02824`)

- Components: `claim:0edb741be0f31f6f`
- Source revision: `sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2511.02824v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/NOTICE.md)
- Attribution: Ludovico Mitchener; Angela Yiu; Benjamin Chang; Mathieu Bourdenx; Tyler Nadolski; Arvis Sulovari; Eric C. Landsness; Dániel L. Barabási; Siddharth Narayanan; Nicky Evans; Shriya Reddy; Martha Foiani; Aizad Kamal; Leah P. Shriver; Fang Cao; Asmamaw T. Wassie; Jon M. Laurent; Edwin Melville-Green; Mayk Caldas; Albert Bou; Kaleigh F. Roberts; Sladjana Zagorac; Timothy C. Orr; Miranda E. Orr; Kevin J. Zwezdaryk; Ali E. Ghareeb; Laurie McCoy; Bruna Gomes; Euan A. Ashley; Karen E. Duff; Tonio Buonassisi; Tom Rainforth; Randall J. Bateman; Michael Skarlinski; Samuel G. Rodriques; Michaela M. Hinks; Andrew D. White, Kosmos: An AI Scientist for Autonomous Discovery, arXiv:2511.02824v2 (2025-11-05), https://arxiv.org/abs/2511.02824v2, PDF https://arxiv.org/pdf/2511.02824v2, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整37作者：Ludovico Mitchener; Angela Yiu; Benjamin Chang; Mathieu Bourdenx; Tyler Nadolski; Arvis Sulovari; Eric C. Landsness; Dániel L. Barabási; Siddharth Narayanan; Nicky Evans; Shriya Reddy; Martha Foiani; Aizad Kamal; Leah P. Shriver; Fang Cao; Asmamaw T. Wassie; Jon M. Laurent; Edwin Melville-Green; Mayk Caldas; Albert Bou; Kaleigh F. Roberts; Sladjana Zagorac; Timothy C. Orr; Miranda E. Orr; Kevin J. Zwezdaryk; Ali E. Ghareeb; Laurie McCoy; Bruna Gomes; Euan A. Ashley; Karen E. Duff; Tonio Buonassisi; Tom Rainforth; Randall J. Bateman; Michael Skarlinski; Samuel G. Rodriques; Michaela M. Hinks; Andrew D. White。前三Mitchener/Yiu/Chang等贡献；Mitchener/Hinks共同监督本工作，Rodriques/White共同监督Edison；20机构及p26完整贡献／funding保留（NIH R01NS133365、UK DRI/MRC/Cure Alzheimer’s Fund、CIFAR/Toyota SARC、EPSRC EP/Y037200/1等）。p5 Fig2真实credit为 a and b reproduced with permission from [9]，不是旧bc，也不含c／Trajectory r2。p27 [9]原印13作者出处：Aizad Kamal; Juan Liu; Ernesto R. Gonzales; Khairunisa Mohamad Ibrahim; Fan Zhang; Hannah E. Skelton; Javier Kelly Cuenca; Carla Yuede; Gary J. Patti; Leah P. Shriver; Jin-Moo Lee; Aaron J. Norris; Eric C. Landsness, Preoptic activation induces a torpor-like hypothermic and hypometabolic state that is cerebroprotective, October 2025; ISSN:2692-8205; Pages:2025.10.24.684192; Section:New Results；未印URL或DOI且Annots无externalURI，不猜其bioRxiv链接／DOI，不GET原作，不给底层图板或全文一般BY4。BioRender独立credit精确保留：https://BioRender.com 的 Fig5a/c、Fig6a、Fig7a、Fig8a/f/g；Fig6g原E2G http://e2g.stanford.edu/variant/6_7231610_G_A 与Fig6h http://twas-hub.org 保留，未访问／重许全站。Fig4与[15]有限比较及p24外部SupplementaryData1–7 availability保持出处身份，不冒称已取得。SI1自身Discovery1 connectome／Discovery3 hypothermia顺序按原件，不手改，p41/42 REFUTED批评与±数据不润色为支持。 既有 R 已核固定v2源payload／保留表达与作品BY4；本次可见v2侧边、embedded arXivID/License BY4，C核实际37作者／42页内嵌SI1–4／Fig2a/b permission与BioRender精确credit，主线明确准入，不搬旧80bibabstract/31copyright gate入新PDF。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2511.02824v2 原 bytes 不改的42页 PDF（8162544 bytes）：固定 arXiv:2511.02824v2 完整42物理页编译PDF：p1–20主文七discoveries／Discussion，p20–24 Methods及p24 Data availability，p26 contributions／funding，p27–33 References[1]–[58]，p34 Supplementary Table1，p35–37内嵌SI1七输入，p38 SI2，p39–40 SI3 rubric，p41–42 SI4 supported/refuted评价至 We just don’t have enough information.；Figure1–8完整，外部SupplementaryData1–7／reports／trajectory／datasets／code未取得且不在合同target。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。Fig2仅a/b的原permission与[9]印刷出处、BioRender Fig5a/c/6a/7a/8a/f/g准确保留；外部SD1–7与data/code/trajectory排除。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。

### LinkML schema-first knowledge modeling (`methodology:linkml-schema-first`)

- Components: `claim:583280271287ef9c`
- Source revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Source version: [pinned upstream version](https://linkml.io/linkml/)
- License: [Apache-2.0 AND MIT](https://www.apache.org/licenses/LICENSE-2.0)
- NOTICE: [raw_data/licenses/linkml-page-body-02-260917.md](../../../../raw_data/licenses/linkml-page-body-02-260917.md)
- Attribution: This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0. 原页脚保留Made with Sphinx and @pradyunsg's Furo署名；本原响应实际嵌入Furo2025.12.19模板另按MIT：Copyright (c) 2020 Pradyun Gedam <mail@pradyunsg.me>。完整MIT随NOTICE；保留上游Adapted from Just the Docs以及Feather/Tabler来源线索，不声称各图标全许可链审核或第三方权利担保，不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原55141B HTML原字节保存；只在派生DOM消费唯一article#furo-main-content，排除a.headerlink的¶ UI符号，保留作者文字、目录href及URI/CURIE代码词法；li/p/blockquote列表层级在Markdown中部分丢失，原HTML可核。结构Markdown、空白连续化、链接解析、源行锚点/sidecar和边界说明属于collector-derived format conversion，不是raw quotation；保守source bounds可至entity EOF，不证明逐行转换或精确closing-tag，article外nav/footer不混正文。新normalized EOF附唯一归属/范围/修改块和NOTICE；旧root doc/164selectors不改，旧NOTICE复制history/NOTICE-before-page-body-02.md，全旧M/C/R review保全，不执行脚本或补造部署commit。
- Scope: 仅本次https://linkml.io/linkml/单页dated-response-2026-09-17T14:20:17Z完整原HTML内作者内容（Apache-2.0）及实际嵌入Furo2025.12.19模板（MIT），并覆盖声明article的normalized/document.md/新sidecar；AND分范围履约不是OR，具体派生bytes/count以manifest为准。旧7340B pre-notice正文/164root selectors和text-only grant另留完整历史。未保存的其他文档页、logo/媒体、远程CSS/JS/依赖/外链作品/代码/数据、商标或无权许可材料不准入；URI引用不是资源已保存/获许可。原UID多页总体边界仍unresolved，partial/full_text不等于whole-UID complete/trusted或离线站点视觉/功能完整。

### Gradient Episodic Memory for Continual Learning (`arxiv-1706.08840`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### LeanDojo: Theorem Proving with Retrieval-Augmented Language Models (`arxiv-2306.15626`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### getzep/graphiti (`github:getzep/graphiti`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
