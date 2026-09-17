---
uid: wiki-page:map-knowledge-editing
title: Knowledge Editing
slug: maps/knowledge-editing
page_type: map
status: review
summary: Routing map for knowledge editing sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:40178c8dde6cbf34
- claim:4715a4ff3b1706fd
- claim:65d2f5de5c0ecdfd
- claim:69e9059578125358
- claim:ad198ecf5d0cad6b
- claim:d6b9ad7b6c2678cc
source_refs: &id001
- arxiv-2110.11309
- arxiv-2104.00405
- arxiv:2310.16218
page_refs:
- wiki-page:source-c707950005ce916a
- wiki-page:source-9923ee576cd59e46
- wiki-page:source-003e063d0c302d83
- wiki-page:knowledge-evolution-loop
- wiki-page:freshness-versioning-and-rollback
outgoing_links:
- target: wiki-page:source-c707950005ce916a
  relation: explains
  claim_refs:
  - claim:ad198ecf5d0cad6b
  - claim:40178c8dde6cbf34
  notes: null
- target: wiki-page:source-9923ee576cd59e46
  relation: explains
  claim_refs:
  - claim:4715a4ff3b1706fd
  - claim:69e9059578125358
  notes: null
- target: wiki-page:source-003e063d0c302d83
  relation: explains
  claim_refs:
  - claim:d6b9ad7b6c2678cc
  - claim:65d2f5de5c0ecdfd
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:4715a4ff3b1706fd
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  notes: null
- target: wiki-page:freshness-versioning-and-rollback
  relation: related
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:4715a4ff3b1706fd
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:4715a4ff3b1706fd
  - claim:ad198ecf5d0cad6b
  - claim:d6b9ad7b6c2678cc
  source_refs:
  - arxiv-2104.00405
  - arxiv-2110.11309
  - arxiv:2310.16218
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:40178c8dde6cbf34
  - claim:65d2f5de5c0ecdfd
  - claim:69e9059578125358
  source_refs:
  - arxiv-2110.11309
  - arxiv:2310.16218
  - arxiv-2104.00405
  editorial_intent: Preserve collector scope.
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
  - arxiv-2110.11309@sha256:16f6480eabfa9f68205b41eb2054e02e1eaa79591d21fa75a998318dcf2c2ab9
  - arxiv-2104.00405@sha256:d9ca19652574908e954b524249d31a8b450830023739ee49797f58d52784dd03
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
    one_line: Routing map for knowledge editing sources, questions, and claims.
    short: Routing map for knowledge editing sources, questions, and claims.
    full: null
  estimated_tokens: 848
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:40178c8dde6cbf34
- claim:4715a4ff3b1706fd
- claim:65d2f5de5c0ecdfd
- claim:69e9059578125358
- claim:ad198ecf5d0cad6b
- claim:d6b9ad7b6c2678cc
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
rights_unavailable_source_refs:
- arxiv-2104.00405
---

# Knowledge Editing

Modification of model or knowledge state with locality and rollback controls.

## Routing questions

- What object is edited?
- How are locality and generalization measured?
- How do edits propagate to dependent pages?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) | `arxiv` | `full_text` | 2 |
| [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) | `arxiv` | `full_text` | 2 |
| [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Avalanche: an End-to-End Library for Continual Learning** (source assertion): Learning continually from non-stationary data streams is a long-standing goal and a challenging problem in machine learning. Recently, we have witnessed a renewed and fast-growing interest in continual learning, especially within the deep learning community. 〔[claim:4715a4ff3b1706fd](../claims/claim-4715a4ff3b1706fd.md)〕
- **Fast Model Editing at Scale** (source assertion): While large pre-trained models have enabled impressive results on a variety of downstream tasks, the largest existing models still make errors, and even accurate predictions may become outdated over time. Because detecting all such failures at training time is impossible, enabling both developers and end users of such models to correct inaccurate outputs while leaving the model otherwise intact is desirable. 〔[claim:ad198ecf5d0cad6b](../claims/claim-ad198ecf5d0cad6b.md)〕
- **Knowledge Editing for Large Language Models: A Survey** (source assertion): Large Language Models (LLMs) have recently transformed both the academic and industrial landscapes due to their remarkable capacity to understand, analyze, and generate texts based on their vast knowledge and reasoning ability. Nevertheless, one major drawback of LLMs is their substantial computational cost for pre-training due to their unprecedented amounts of parameters. 〔[claim:d6b9ad7b6c2678cc](../claims/claim-d6b9ad7b6c2678cc.md)〕

## Collector assessments

- **Fast Model Editing at Scale** (collection assessment): MEND makes the update mechanism itself learnable and exposes generalization/locality requirements for governed knowledge editing. 〔[claim:40178c8dde6cbf34](../claims/claim-40178c8dde6cbf34.md)〕
- **Knowledge Editing for Large Language Models: A Survey** (collection assessment): Provides the taxonomy, evaluation metrics, datasets, locality/generalization criteria, and open problems needed to govern knowledge updates rather than treating updates as an unconstrained write operation. 〔[claim:65d2f5de5c0ecdfd](../claims/claim-65d2f5de5c0ecdfd.md)〕
- **Avalanche: an End-to-End Library for Continual Learning** (collection assessment): Provides an implementation and benchmark substrate for comparing retention, transfer and forgetting across continual-learning strategies. 〔[claim:69e9059578125358](../claims/claim-69e9059578125358.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Fast Model Editing at Scale](../sources/arxiv-2110.11309.md) — `explains`
- [Avalanche: an End-to-End Library for Continual Learning](../sources/arxiv-2104.00405.md) — `explains`
- [Knowledge Editing for Large Language Models: A Survey](../sources/arxiv-2310.16218.md) — `explains`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`
- [Freshness, versioning, and rollback](../concepts/freshness-versioning-rollback.md) — `related`

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

### Knowledge Editing for Large Language Models: A Survey (`arxiv:2310.16218`)

- Components: `claim:d6b9ad7b6c2678cc`
- Source revision: `sha256:77d3c50e6184b5fbe01b2797d4d8fbeb885df049bf2f35e1adf3deee677d8098`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2310.16218v4)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2310.16218--21c4a191/pdf-supplement/NOTICE.md)
- Attribution: Song Wang; Yaochen Zhu; Haochen Liu; Zaiyi Zheng; Chen Chen; Jundong Li, Knowledge Editing for Large Language Models: A Survey, arXiv:2310.16218v4 (2024-09-19), https://arxiv.org/abs/2310.16218v4, PDF https://arxiv.org/pdf/2310.16218v4, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整六作者 Song Wang／Yaochen Zhu／Haochen Liu／Zaiyi Zheng／Chen Chen／Jundong Li，University of Virginia USA及各address/email保留。ACM Reference Format中的10.1145/nnnnnnn.nnnnnnn是placeholder，不作为真实DOI或ACM正式出版证据。p29完整资助 NSF IIS-2006844/IIS-2144209/IIS-2223769/CNS2154962/BCS-2228534，CCI VV-1Q23-007/HV-2Q23-003/VV-1Q24-011、JP Morgan Chase／Cisco Faculty Research Award、Jefferson Lab subcontract、UVA4-VA原样。p2 OpenAI/ChatGPT样式图标与GPT3.5研究表示、179参考作品不授予底层商标／模型／被引全文一般BY4。native p2存在不可见banking query text object，不猜制作原因／不作可见父摘要。 既有 R fixed-article-version证据已核v4 2024-09-19及作品BY4／保留payload身份；A核本次35页主文／179书目／四编号图／真结尾，主线全文读并准入；不借acmart或placeholder DOI授予。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2310.16218v4 原 bytes 不改的35页 PDF（1768864 bytes）：固定 arXiv:2310.16218v4 完整35物理页编译PDF：p1–28主文／taxonomy／数学／datasets／applications／challenges，p29真正Conclusions末尾／完整funding／References开始，p30–35书目至[179] Fine-tuning language models from human preferences；Figure1–4／Tables1–3齐，无独立Appendix/SI，不把模板源码注释发明为SI。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。

### Avalanche: an End-to-End Library for Continual Learning (`arxiv-2104.00405`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
