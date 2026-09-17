---
uid: wiki-page:source-81e58c8add4ce203
title: 'AgentRxiv: Towards Collaborative Autonomous Research'
slug: sources/arxiv-2503.18102
page_type: source
status: review
summary: 'Source page for AgentRxiv: Towards Collaborative Autonomous Research with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:07439fdff0cc0aa3
- claim:f5d2f5be4a498ca2
source_refs: &id002
- arxiv:2503.18102
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-1b992220f722d044
- wiki-page:evidence-1e3c274acc6e4c60
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-1b992220f722d044
  relation: evidenced_by
  claim_refs:
  - claim:07439fdff0cc0aa3
  notes: null
- target: wiki-page:evidence-1e3c274acc6e4c60
  relation: evidenced_by
  claim_refs:
  - claim:f5d2f5be4a498ca2
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:07439fdff0cc0aa3
  source_refs:
  - arxiv:2503.18102
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:f5d2f5be4a498ca2
  source_refs:
  - arxiv:2503.18102
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:0175f4c78a0341b7
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2503.18102@sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669
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
    one_line: 'Source page for AgentRxiv: Towards Collaborative Autonomous Research with claim/evidence expansion.'
    short: 'Source page for AgentRxiv: Towards Collaborative Autonomous Research with claim/evidence expansion.'
    full: null
  estimated_tokens: 400
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:07439fdff0cc0aa3
- claim:f5d2f5be4a498ca2
rights_refs:
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
rights_unavailable_source_refs: []
---

# AgentRxiv: Towards Collaborative Autonomous Research

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2503.18102`
- Canonical ID: `2503.18102`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/document.txt`

## Source-reported candidate statements

- Progress in scientific discovery is rarely the result of a single "Eureka" moment, but is rather the product of hundreds of scientists incrementally working together toward a common goal. While existing agent workflows are capable of producing research autonomously, they do so in isolation, without the ability to continuously improve upon prior research results. 〔[claim:07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md)〕

## Collection assessments

- A direct bridge between autonomous research and knowledge self-evolution: agent laboratories upload, retrieve and build on each others research, creating cumulative improvement across generations of work. 〔[claim:f5d2f5be4a498ca2](../claims/claim-f5d2f5be4a498ca2.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:07439fdff0cc0aa3` | `evidence:3eb5d79a34cdce67` | `local://materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/document.txt#L9-L12` | `full_text` |
| `claim:f5d2f5be4a498ca2` | `evidence:4b7e0c84f5a212e4` | `local://raw_data/arxiv/AgentRxiv: Towards Collaborative Autonomous Research/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim 07439fdff0cc0aa3](../claims/claim-07439fdff0cc0aa3.md) — `evidenced_by`
- [Claim f5d2f5be4a498ca2](../claims/claim-f5d2f5be4a498ca2.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### AgentRxiv: Towards Collaborative Autonomous Research (`arxiv:2503.18102`)

- Components: `claim:07439fdff0cc0aa3`
- Source revision: `sha256:762045781a10140f714e0f23388014286a50cce79f385d6b4a1475162cce9669`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2503.18102v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2503.18102--1133e9d5/pdf-supplement/NOTICE.md)
- Attribution: Samuel Schmidgall; Michael Moor, AgentRxiv: Towards Collaborative Autonomous Research, arXiv:2503.18102v1 (2025-03-23), https://arxiv.org/abs/2503.18102v1, PDF https://arxiv.org/pdf/2503.18102v1, CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。实际当前PDF两作者按序Samuel Schmidgall; Michael Moor。1 Department of Electrical & Computer Engineering, Johns Hopkins University；2 Department of Biosystems Science & Engineering, ETH Zurich；Samuel Schmidgall通讯sschmi46@jhu.edu。固定v1侧边日期23 Mar 2025与题名页右上2025-3-25独立保留，不以pagehead或Creation/ModDate覆盖提交事实。p27 National Science Foundation Graduate Research Fellowship, Grant No. DGE 2139757支持信用保留，不暗示NSF/作者/机构背书。p1 Figure1网页列表截图另文Agent Laboratory: Using LLM Agents as Research Assistants，实际九作者按序Samuel Schmidgall、Yusheng Su、Ze Wang、Ximeng Sun、Jialian Wu、Xiaodong Yu、Jiang Liu、Zicheng Liu、Emad Barsoum，不含Michael Moor、不混入当前两作者。图中打印arXiv:2501.04227 [pdf, other]为bare ID、没有vN或完整URL；有限六显示行约52个空白tokens摘要预览起Historically, scientific discovery...，止accepts a human-provide...并有More，是原图已截断预览、非完整摘要/全文。若需定位 https://arxiv.org/abs/2501.04227 只按可见ID生成locator，不称本批核定另文固定版/取得全文；p24书目独立信用、Figures2/3研究上下文按原件保留。当前p1 AgentRxiv.github.io项目链接保留。只保存本PDF中实际有限展示与信用，不单独再许可另篇整文或底层媒体，也不新增抓取/许可函退出条件。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 本次唯一固定版GET的2757188 bytes原PDF按字节原样保留，不编辑/重导/重排/OCR。既有helper以plain全页提取生成独立pdf-supplement/document.txt与实际新PDF revision绑定的逐页selectors；页标题/定位和唯一文末归属/修改/范围footer为collector表示元数据，native不是作者另交原始文本或byte-exact executable prompt/code。NOTICE自包含实际署名/独立信用/来源/范围/损失与既有完整CC BY4法律文本，notice_path自绑定本文件，不新rawlicense资产。本primary_excerpt仅声明同一native Page1实际父摘要L9–23，不修改原文。旧root source/normalized/selectors/NOTICE/README/files及revision/retrieval/rights/gate/source_version键缺省不改，不把新选版回溯为旧bare archive GET的已证版次。
- Scope: 本独立表示只覆盖本UID固定arXiv:2503.18102v1原bytes不改的29页compiled PDF（2757188 bytes）：固定arXiv:2503.18102v1完整29物理页编译论文：p1父摘要/Figure1，p2–17主文、六活动图、单/三实验室结果、Failure/Ethics/Discussion/实际Conclusion，p17–27 References，p27 Acknowledgments，p28 A.Algorithms与B.Agent Laboratory configuration，p29配置表/B.3/真实C.Prompts结尾。末句All prompts are the same as in Schmidgall et al. (2025).是正常引用，原件未列另一论文完整prompt，不递归取另文。 论文作者可许可表达依本固定作品已证CC BY4路径；图表/参考文献/实际有限引述保存其原信用，不外推standalone被引作品/素材/程序/代码/数据/媒体/服务/模型/权重/模板的一般许可。范围含该PDF派生有损native plain、revision-bound逐页selectors及完整NOTICE；不执行被审指令、不重新打包外链、不改变底层许可、不为已许可权利添加下游限制，无普遍权利保证，不授商标/专利。当前原图有限另文列表/截图/摘要预览在此出版表示内原样保留并落实九作者与bareID信用，不扩大为另文独立全文或底层图片/角色/程序/数据的一般许可。旧bib LUMI-lab长摘要和competing-interest/patent声明未在此实际PDF出现；p4简短介绍/p18普通书目不等于旧完整摘要，其NC-ND用途/转换条件与旧GDM BY-SA4、ICLR/LPPL等组件/root block保持，不外推到整个新PDF也不因新BY4放行旧source。
