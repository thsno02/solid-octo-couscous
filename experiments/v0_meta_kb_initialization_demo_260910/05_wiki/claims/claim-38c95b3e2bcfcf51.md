---
uid: wiki-page:evidence-9f274d1678d7b92b
title: Claim 38c95b3e2bcfcf51
slug: claims/claim-38c95b3e2bcfcf51
page_type: evidence
status: review
summary: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
  scientific research and discovering new knowledge. While frontier models have already been used as aides to human '
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:38c95b3e2bcfcf51
source_refs: &id001
- arxiv:2408.06292
page_refs:
- wiki-page:source-c1dbc9c2a83a564a
- wiki-page:map-automated-research
outgoing_links:
- target: wiki-page:source-c1dbc9c2a83a564a
  relation: evidenced_by
  claim_refs:
  - claim:38c95b3e2bcfcf51
  notes: null
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs:
  - claim:38c95b3e2bcfcf51
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:38c95b3e2bcfcf51
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:38c95b3e2bcfcf51
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:f3fea76ebc259510
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
      scientific research and discovering new knowledge. While frontier models have already been used as aides to
      human '
    short: 'One of the grand challenges of artificial general intelligence is developing agents capable of conducting
      scientific research and discovering new knowledge. While frontier models have already been used as aides to
      human '
    full: null
  estimated_tokens: 329
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:38c95b3e2bcfcf51
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

# Source assertion from The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g.

## Scope

- Claim ID: `claim:38c95b3e2bcfcf51`
- Scope: `source-reported assertion`
- Domain: [automated-research](../maps/automated-research.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:32355b67bcee3a03` | `local://materialized_sources/corpus/arxiv-2408.06292--522d359c/pdf-supplement/document.txt#L9-L11` | `materialized_sources/corpus/arxiv-2408.06292--522d359c/pdf-supplement/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) — `evidenced_by`
- [Automated Research](../maps/automated-research.md) — `part_of`

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
