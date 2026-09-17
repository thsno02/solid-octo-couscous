---
uid: wiki-page:evidence-d389535df5553705
title: Claim ad198ecf5d0cad6b
slug: claims/claim-ad198ecf5d0cad6b
page_type: evidence
status: review
summary: While large pre-trained models have enabled impressive results on a variety of downstream tasks, the largest
  existing models still make errors, and even accurate predictions may become outdated over time. Because detecti
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:ad198ecf5d0cad6b
source_refs: &id001
- arxiv-2110.11309
page_refs:
- wiki-page:source-c707950005ce916a
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-c707950005ce916a
  relation: evidenced_by
  claim_refs:
  - claim:ad198ecf5d0cad6b
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:ad198ecf5d0cad6b
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:ad198ecf5d0cad6b
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:ad198ecf5d0cad6b
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:45bd6c7288326476
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv-2110.11309@sha256:16f6480eabfa9f68205b41eb2054e02e1eaa79591d21fa75a998318dcf2c2ab9
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
    one_line: While large pre-trained models have enabled impressive results on a variety of downstream tasks, the
      largest existing models still make errors, and even accurate predictions may become outdated over time. Because
      detecti
    short: While large pre-trained models have enabled impressive results on a variety of downstream tasks, the
      largest existing models still make errors, and even accurate predictions may become outdated over time. Because
      detecti
    full: null
  estimated_tokens: 352
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:ad198ecf5d0cad6b
rights_refs:
- source_uid: arxiv-2110.11309
  source_revision: sha256:16f6480eabfa9f68205b41eb2054e02e1eaa79591d21fa75a998318dcf2c2ab9
  source_version_url: https://arxiv.org/pdf/2110.11309v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2110.11309--d5da3395/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ad198ecf5d0cad6b
rights_unavailable_source_refs: []
---

# Source assertion from Fast Model Editing at Scale

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

While large pre-trained models have enabled impressive results on a variety of downstream tasks, the largest existing models still make errors, and even accurate predictions may become outdated over time. Because detecting all such failures at training time is impossible, enabling both developers and end users of such models to correct inaccurate outputs while leaving the model otherwise intact is desirable.

## Scope

- Claim ID: `claim:ad198ecf5d0cad6b`
- Scope: `source-reported assertion`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:5a459f5951ba3ff8` | `local://materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/document.txt#L9-L13` | `materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Fast Model Editing at Scale (`arxiv-2110.11309`)

- Components: `claim:ad198ecf5d0cad6b`
- Source revision: `sha256:16f6480eabfa9f68205b41eb2054e02e1eaa79591d21fa75a998318dcf2c2ab9`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2110.11309v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2110.11309--d5da3395/pdf-supplement/NOTICE.md)
- Attribution: Eric Mitchell; Charles Lin; Antoine Bosselut; Chelsea Finn; Christopher D. Manning, Fast Model Editing at Scale, arXiv:2110.11309v2 (2022-06-13), https://arxiv.org/abs/2110.11309v2, PDF https://arxiv.org/pdf/2110.11309v2, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整真实顺序 Eric Mitchell／Charles Lin／Antoine Bosselut／Chelsea Finn／Christopher D. Manning，Finn在Manning前（不同于SERAC）；Stanford，ICLR2022 conference页眉与MEND完整展开名保留。p10完整致谢 Angeliki Lazaridou、Spencer Braun、Mitchell Wortsman、Gabriel Ilharco、Stephanie Chan、Archit Sharma、Michael Chang、Michael Janner、Ashwin Paranjape、匿名reviewers及Knight-Hennessy／CIFAR归属保留。FEVER／zsRE／Wikitext、De Cao2021／Thorne2018／Ma2021与模型样例保持研究输入身份；C.4虚构edit labels不是可信事实，dual-use/backdoor风险不是复制限制，不重许可底层数据／模型。 本批正式 https://arxiv.org/abs/2110.11309v2 的作品 view license 正常到BY4，v2日期2022-06-13／完整五作者已核；A报告核实际21页A–G与Caching真结尾，主线全文读并明确准入。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2110.11309v2 原 bytes 不改的21页 PDF（1140371 bytes）：固定 arXiv:2110.11309v2 完整21物理页编译PDF：p1–9主文／Algorithms1–2／Tables1–6／Figure1–3，p10完整Acknowledgements／Ethics／Reproducibility，p11–14References，p15–21正式A–G／Figure4／Tables7–11；p21浮动Table11后完整F qualitative examples、G Editing through Caching至 or the edit success.，不另造SI。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。
