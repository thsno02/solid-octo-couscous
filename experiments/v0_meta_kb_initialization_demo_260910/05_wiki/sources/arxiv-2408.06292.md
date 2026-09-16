---
uid: wiki-page:source-c1dbc9c2a83a564a
title: 'The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery'
slug: sources/arxiv-2408.06292
page_type: source
status: review
summary: 'Source page for The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:38c95b3e2bcfcf51
- claim:d3a0d3c2f4fd45d4
source_refs: &id002
- arxiv:2408.06292
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-9f274d1678d7b92b
- wiki-page:evidence-c7a63ea9f72c6b3c
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-9f274d1678d7b92b
  relation: evidenced_by
  claim_refs:
  - claim:38c95b3e2bcfcf51
  notes: null
- target: wiki-page:evidence-c7a63ea9f72c6b3c
  relation: evidenced_by
  claim_refs:
  - claim:d3a0d3c2f4fd45d4
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:38c95b3e2bcfcf51
  source_refs:
  - arxiv:2408.06292
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:d3a0d3c2f4fd45d4
  source_refs:
  - arxiv:2408.06292
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
  - arxiv:2408.06292@sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507
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
    one_line: 'Source page for The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery with claim/evidence
      expansion.'
    short: 'Source page for The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 387
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:38c95b3e2bcfcf51
- claim:d3a0d3c2f4fd45d4
rights_refs:
- source_uid: arxiv:2408.06292
  source_revision: sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507
  source_version_url: https://arxiv.org/pdf/2408.06292v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2408.06292--522d359c/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:38c95b3e2bcfcf51
rights_unavailable_source_refs: []
---

# The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2408.06292`
- Canonical ID: `2408.06292`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2408.06292--522d359c/pdf-supplement/document.txt`

## Source-reported candidate statements

- One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕

## Collection assessments

- Extends self-evolution from improving an agent to automating the research loop itself: idea generation, implementation, experiment, paper writing, and automated review can be iterated to create new knowledge. 〔[claim:d3a0d3c2f4fd45d4](../claims/claim-d3a0d3c2f4fd45d4.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:38c95b3e2bcfcf51` | `evidence:32355b67bcee3a03` | `local://materialized_sources/corpus/arxiv-2408.06292--522d359c/pdf-supplement/document.txt#L9-L11` | `full_text` |
| `claim:d3a0d3c2f4fd45d4` | `evidence:f82ae22267c5c145` | `local://raw_data/arxiv/The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md) — `evidenced_by`
- [Claim d3a0d3c2f4fd45d4](../claims/claim-d3a0d3c2f4fd45d4.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (`arxiv:2408.06292`)

- Components: `claim:38c95b3e2bcfcf51`
- Source revision: `sha256:e911f90b0114d5e3fc23a0000177ea670fa9ed79d5f9a664efa2980fdb350507`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2408.06292v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. Fixed arXiv 2408.06292v3, https://arxiv.org/abs/2408.06292v3; original PDF https://arxiv.org/pdf/2408.06292v3. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2408.06292v3 取得的固定版本官方 PDF（186页，11731143 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。
