---
uid: wiki-page:source-1203e0209022f228
title: 'The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search'
slug: sources/arxiv-2504.08066
page_type: source
status: review
summary: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
  with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
source_refs: &id002
- arxiv:2504.08066
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-638ecd816dce953d
- wiki-page:evidence-caa99c40bb0689a1
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-638ecd816dce953d
  relation: evidenced_by
  claim_refs:
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:evidence-caa99c40bb0689a1
  relation: evidenced_by
  claim_refs:
  - claim:9077f46d7f30e565
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:9077f46d7f30e565
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:8798b3dc1ae125ea
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Keep collector interpretation separate.
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
  - arxiv:2504.08066@sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
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
    one_line: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    short: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    full: null
  estimated_tokens: 491
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
rights_refs:
- source_uid: arxiv:2504.08066
  source_revision: sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2
  source_version_url: https://arxiv.org/pdf/2504.08066v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2504.08066--22ed15f2/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:9077f46d7f30e565
rights_unavailable_source_refs: []
---

# The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2504.08066`
- Canonical ID: `2504.08066`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2504.08066--22ed15f2/pdf-supplement/document.txt`

## Source-reported candidate statements

- AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce Th e A I Sc i e n t i s t - v 2, an end-to-end agentic system capable of producing the first entirely AI- generatedpeer-review-acceptedworkshoppaper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

## Collection assessments

- End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process. 〔[claim:8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:8798b3dc1ae125ea` | `evidence:924a40542eeaca58` | `local://raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:9077f46d7f30e565` | `evidence:85c1017952d003b4` | `local://materialized_sources/corpus/arxiv-2504.08066--22ed15f2/pdf-supplement/document.txt#L11-L13` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md) — `evidenced_by`
- [Claim 9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (`arxiv:2504.08066`)

- Components: `claim:9077f46d7f30e565`
- Source revision: `sha256:53bafd3028e3f8829a3d85220e84dcf0d18934f9b75c092a60de303ff3644bd2`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2504.08066v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search. Fixed arXiv 2504.08066v1, https://arxiv.org/abs/2504.08066v1; original PDF https://arxiv.org/pdf/2504.08066v1. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements. Seven human workshop reviews retain independent anonymous reviewer attribution: compositional regularization Reviewer #1/#2 (source/workshop_papers/compositional_regularization/reviewer_2.txt and reviewer_3.txt); label noise Reviewer #1/#2 (source/workshop_papers/label_noise/reviewer_1.txt and reviewer_3.txt); pest prediction Reviewer #1/#2/#3 (source/workshop_papers/pest_prediction/reviewer_1.txt, reviewer_2.txt, reviewer_3.txt). Their separately established CC BY 4.0 basis is OpenReview Comment/review Terms updated 2024-09-24, https://openreview.net/legal/terms, as documented in the existing source package. Only the two compositional reviews have an explicit inclusion-permission statement; no equivalent consent, reviewer identity or public forum match is invented for the others.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2504.08066v1 取得的固定版本官方 PDF（69页，8923691 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。 七份匿名 workshop review 继续按独立 CC BY 4.0 及逐组 Reviewer 标签归属，不冒称论文作者原创。
