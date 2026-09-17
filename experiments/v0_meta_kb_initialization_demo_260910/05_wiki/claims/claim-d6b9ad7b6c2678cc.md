---
uid: wiki-page:evidence-82279bc33118e4a9
title: Claim d6b9ad7b6c2678cc
slug: claims/claim-d6b9ad7b6c2678cc
page_type: evidence
status: review
summary: Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due
  to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and reasoning
  a
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:d6b9ad7b6c2678cc
source_refs: &id001
- arxiv:2310.16218
page_refs:
- wiki-page:source-003e063d0c302d83
- wiki-page:map-knowledge-editing
outgoing_links:
- target: wiki-page:source-003e063d0c302d83
  relation: evidenced_by
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  notes: null
- target: wiki-page:map-knowledge-editing
  relation: part_of
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:4e541384e82b1271
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2310.16218@sha256:77d3c50e6184b5fbe01b2797d4d8fbeb885df049bf2f35e1adf3deee677d8098
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
    one_line: Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes
      due to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge
      and reasoning a
    short: Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due
      to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and
      reasoning a
    full: null
  estimated_tokens: 359
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:d6b9ad7b6c2678cc
rights_refs:
- source_uid: arxiv:2310.16218
  source_revision: sha256:77d3c50e6184b5fbe01b2797d4d8fbeb885df049bf2f35e1adf3deee677d8098
  source_version_url: https://arxiv.org/pdf/2310.16218v4
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2310.16218--21c4a191/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:d6b9ad7b6c2678cc
rights_unavailable_source_refs: []
---

# Source assertion from Knowledge Editing for Large Language Models: A Survey

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and reasoning ability. Nevertheless, one major drawback of LLMs is their substantial computational cost for pre-training due to their unprecedented amounts of parameters.

## Scope

- Claim ID: `claim:d6b9ad7b6c2678cc`
- Scope: `source-reported assertion`
- Domain: [knowledge-editing](../maps/knowledge-editing.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:c5cfc0bf91f61fb4` | `local://materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/document.txt#L10-L13` | `materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) — `evidenced_by`
- [Knowledge Editing](../maps/knowledge-editing.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Knowledge Editing for Large Language Models: A Survey (`arxiv:2310.16218`)

- Components: `claim:d6b9ad7b6c2678cc`
- Source revision: `sha256:77d3c50e6184b5fbe01b2797d4d8fbeb885df049bf2f35e1adf3deee677d8098`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2310.16218v4)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md)
- Attribution: Song Wang; Yaochen Zhu; Haochen Liu; Zaiyi Zheng; Chen Chen; Jundong Li, Knowledge Editing for Large Language Models: A Survey, arXiv:2310.16218v4 (2024-09-19), https://arxiv.org/abs/2310.16218v4, PDF https://arxiv.org/pdf/2310.16218v4, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整六作者 Song Wang／Yaochen Zhu／Haochen Liu／Zaiyi Zheng／Chen Chen／Jundong Li，University of Virginia USA及各address/email保留。ACM Reference Format中的10.1145/nnnnnnn.nnnnnnn是placeholder，不作为真实DOI或ACM正式出版证据。p29完整资助 NSF IIS-2006844/IIS-2144209/IIS-2223769/CNS2154962/BCS-2228534，CCI VV-1Q23-007/HV-2Q23-003/VV-1Q24-011、JP Morgan Chase／Cisco Faculty Research Award、Jefferson Lab subcontract、UVA4-VA原样。p2 OpenAI/ChatGPT样式图标与GPT3.5研究表示、179参考作品不授予底层商标／模型／被引全文一般BY4。native p2存在不可见banking query text object，不猜制作原因／不作可见父摘要。 既有 R fixed-article-version证据已核v4 2024-09-19及作品BY4／保留payload身份；A核本次35页主文／179书目／四编号图／真结尾，主线全文读并准入；不借acmart或placeholder DOI授予。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2310.16218v4 原 bytes 不改的35页 PDF（1768864 bytes）：固定 arXiv:2310.16218v4 完整35物理页编译PDF：p1–28主文／taxonomy／数学／datasets／applications／challenges，p29真正Conclusions末尾／完整funding／References开始，p30–35书目至[179] Fine-tuning language models from human preferences；Figure1–4／Tables1–3齐，无独立Appendix/SI，不把模板源码注释发明为SI。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。
