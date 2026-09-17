---
uid: wiki-page:map-ontology-semantic-architecture
title: Ontology Semantic Architecture
slug: maps/ontology-semantic-architecture
page_type: map
status: review
summary: Routing map for ontology semantic architecture sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:0edb741be0f31f6f
- claim:27f7e77bbaa0d47f
- claim:3adb88340e0eb2b6
- claim:3e6ec7f46b13c44f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
source_refs: &id001
- arxiv:2511.02824
- methodology:linkml-schema-first
- github:linkml/linkml
page_refs:
- wiki-page:source-51ed59b1fc0ecd08
- wiki-page:source-93365d53a252ec8d
- wiki-page:source-8a8c72b9ad5bf51d
- wiki-page:claim-evidence-page-compilation
- wiki-page:llm-wiki-reference-system
outgoing_links:
- target: wiki-page:source-51ed59b1fc0ecd08
  relation: explains
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:3e6ec7f46b13c44f
  notes: null
- target: wiki-page:source-93365d53a252ec8d
  relation: explains
  claim_refs:
  - claim:583280271287ef9c
  - claim:27f7e77bbaa0d47f
  notes: null
- target: wiki-page:source-8a8c72b9ad5bf51d
  relation: explains
  claim_refs:
  - claim:fc57f26307cefee3
  - claim:3adb88340e0eb2b6
  notes: null
- target: wiki-page:claim-evidence-page-compilation
  relation: related
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  notes: null
- target: wiki-page:llm-wiki-reference-system
  relation: related
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  source_refs:
  - arxiv:2511.02824
  - methodology:linkml-schema-first
  - github:linkml/linkml
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  source_refs:
  - methodology:linkml-schema-first
  - github:linkml/linkml
  - arxiv:2511.02824
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
    one_line: Routing map for ontology semantic architecture sources, questions, and claims.
    short: Routing map for ontology semantic architecture sources, questions, and claims.
    full: null
  estimated_tokens: 907
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:0edb741be0f31f6f
- claim:27f7e77bbaa0d47f
- claim:3adb88340e0eb2b6
- claim:3e6ec7f46b13c44f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
rights_refs:
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
- github:linkml/linkml
---

# Ontology Semantic Architecture

Stable identity, schema, typed relations, provenance, and semantic change.

## Routing questions

- Which identifiers remain stable?
- How are schema changes migrated and rolled back?
- How are source, claim, evidence, page, time, and policy separated?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Kosmos: An AI Scientist for Autonomous Discovery](../sources/arxiv-2511.02824.md) | `arxiv` | `full_text` | 2 |
| [LinkML schema-first knowledge modeling](../sources/methodology-linkml-schema-first.md) | `methodology` | `full_text` | 2 |
| [linkml/linkml](../sources/github-linkml-linkml.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depthoftheirfindings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕
- **LinkML schema-first knowledge modeling** (source assertion): Everything you need to know about [LinkML](https://linkml.io), the Linked Data Modeling Language. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Collector assessments

- **LinkML schema-first knowledge modeling** (collection assessment): Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts. 〔[claim:27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md)〕
- **linkml/linkml** (collection assessment): Modern schema-first bridge between developer data models and linked-data/ontology artifacts. 〔[claim:3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (collection assessment): Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts. 〔[claim:3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Kosmos: An AI Scientist for Autonomous Discovery](../sources/arxiv-2511.02824.md) — `explains`
- [LinkML schema-first knowledge modeling](../sources/methodology-linkml-schema-first.md) — `explains`
- [linkml/linkml](../sources/github-linkml-linkml.md) — `explains`
- [Claim–evidence–page compilation](../methods/claim-evidence-page.md) — `related`
- [LLM Wiki reference system](../systems/reference-system.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

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

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
