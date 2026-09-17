---
uid: wiki-page:source-51ed59b1fc0ecd08
title: 'Kosmos: An AI Scientist for Autonomous Discovery'
slug: sources/arxiv-2511.02824
page_type: source
status: review
summary: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:0edb741be0f31f6f
- claim:3e6ec7f46b13c44f
source_refs: &id002
- arxiv:2511.02824
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-a7da1a63a4c9d723
- wiki-page:evidence-51f99c8c1993ed75
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-a7da1a63a4c9d723
  relation: evidenced_by
  claim_refs:
  - claim:0edb741be0f31f6f
  notes: null
- target: wiki-page:evidence-51f99c8c1993ed75
  relation: evidenced_by
  claim_refs:
  - claim:3e6ec7f46b13c44f
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:0edb741be0f31f6f
  source_refs:
  - arxiv:2511.02824
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:3e6ec7f46b13c44f
  source_refs:
  - arxiv:2511.02824
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:e55e8d731fd60066
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2511.02824@sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8
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
  source_dependencies: *id002
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
    short: 'Source page for Kosmos: An AI Scientist for Autonomous Discovery with claim/evidence expansion.'
    full: null
  estimated_tokens: 640
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:0edb741be0f31f6f
- claim:3e6ec7f46b13c44f
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
rights_unavailable_source_refs: []
---

# Kosmos: An AI Scientist for Autonomous Discovery

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2511.02824`
- Canonical ID: `2511.02824`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:bc1d107627c3f81bd551a6180f1d5739db46b2b3902dc2349a382de500f6b0a8`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/document.txt`

## Source-reported candidate statements

- Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depthoftheirfindings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕

## Collection assessments

- Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts. 〔[claim:3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:0edb741be0f31f6f` | `evidence:a685b3f37385c089` | `local://materialized_sources/corpus/arxiv-2511.02824--1c218a8e/pdf-supplement/document.txt#L13-L16` | `full_text` |
| `claim:3e6ec7f46b13c44f` | `evidence:a566d8629070c224` | `local://raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md) — `evidenced_by`
- [Claim 3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md) — `evidenced_by`

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
