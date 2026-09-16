---
uid: wiki-page:source-c9890d5668d1c1b3
title: Automated Design of Agentic Systems
slug: sources/arxiv-2408.08435
page_type: source
status: review
summary: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:00e6310ce97dc279
- claim:0d2b54965305cf83
source_refs: &id002
- arxiv:2408.08435
page_refs:
- wiki-page:map-cross-cutting
- wiki-page:evidence-1726c87cfdd2429b
- wiki-page:evidence-cff7f8af0fb78c76
outgoing_links:
- target: wiki-page:map-cross-cutting
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-1726c87cfdd2429b
  relation: evidenced_by
  claim_refs:
  - claim:00e6310ce97dc279
  notes: null
- target: wiki-page:evidence-cff7f8af0fb78c76
  relation: evidenced_by
  claim_refs:
  - claim:0d2b54965305cf83
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:0d2b54965305cf83
  source_refs:
  - arxiv:2408.08435
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:00e6310ce97dc279
  source_refs:
  - arxiv:2408.08435
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:640f5f05531b8dbe
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2408.08435@sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
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
    one_line: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
    short: Source page for Automated Design of Agentic Systems with claim/evidence expansion.
    full: null
  estimated_tokens: 399
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:00e6310ce97dc279
- claim:0d2b54965305cf83
rights_refs:
- source_uid: arxiv:2408.08435
  source_revision: sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
  source_version_url: https://arxiv.org/abs/2408.08435v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md
  package_path: materialized_sources/corpus/arxiv-2408.08435--dc6e6730/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:0d2b54965305cf83
rights_unavailable_source_refs: []
---

# Automated Design of Agentic Systems

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2408.08435`
- Canonical ID: `2408.08435`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2`
- Domain: [cross-cutting](../maps/cross-cutting.md)
- Local document: `materialized_sources/corpus/arxiv-2408.08435--dc6e6730/normalized/document.txt`

## Source-reported candidate statements

- Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within agentic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). 〔[claim:0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md)〕

## Collection assessments

- Defines Automated Design of Agentic Systems (ADAS): agents are represented in code and a meta-agent iteratively programs better agents using an ever-growing archive of prior discoveries. 〔[claim:00e6310ce97dc279](../claims/claim-00e6310ce97dc279.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:00e6310ce97dc279` | `evidence:4c23103dc864786c` | `local://raw_data/arxiv/Automated Design of Agentic Systems/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:0d2b54965305cf83` | `evidence:33d6742cf3d38320` | `local://materialized_sources/corpus/arxiv-2408.08435--dc6e6730/normalized/document.txt#L115-L115` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Cross Cutting](../maps/cross-cutting.md) — `part_of`
- [Claim 00e6310ce97dc279](../claims/claim-00e6310ce97dc279.md) — `evidenced_by`
- [Claim 0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Automated Design of Agentic Systems (`arxiv:2408.08435`)

- Components: `claim:0d2b54965305cf83`
- Source revision: `sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2`
- Source version: [pinned upstream version](https://arxiv.org/abs/2408.08435v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md](../../../../raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md)
- Attribution: Shengran Hu, Cong Lu, Jeff Clune, Automated Design of Agentic Systems, arXiv:2408.08435v2 (2025-03-02), https://arxiv.org/abs/2408.08435v2, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. ICLR, Template for ICLR 2025 Conference Submission, CC BY 4.0, https://www.overleaf.com/latex/templates/template-for-iclr-2025-conference-submission/gqzkdyycxtvt; ICLR STY retains Hugo Larochelle's NIPS-style adaptation credit and matches https://github.com/ICLR/Master-Template/blob/05833d63fe48bbf250b144741ea77691018bb328/iclr2025/iclr2025_conference.sty. Deep Learning notation retains goodfeli/dlbook_notation attribution and the original authors' free-use statement at https://github.com/goodfeli/dlbook_notation/blob/master/README.md. BST: Copyright 2010 Hal Daum\'e III, J. Fürnkranz label modifications, Copyright 1993-2007 Patrick W Daly; fancyhdr 3.2: Piet van Oostrum; natbib 8.31: Copyright 1993-2009 Patrick W Daly, original 2009/07/16 source. These components retain independent LPPL version 1 or later; packaging selects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c.txt. 完整原始 natbib.dtx 随 NOTICE.md 及 raw_data/licenses/components/natbib-8.31/natbib.dtx 提供。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 9份原源文本及其版权、归属、历史修改说明不改；复用现有 TeX 合并与纯文本转换， normalized/document.tex 和33个定位器不改，在 normalized/document.txt 末尾追加唯一署名、 修改/范围说明及 NOTICE.md 链接。附注保存完整 CC BY 4.0、LPPL 1.3c 和未修改的原 natbib.dtx； 未新增或转换原已省略的5份PDF图像，不声称原作者/维护者支持本仓库修改。
- Scope: 仅实存9份 source 文本（304218 bytes）、normalized/document.tex（109460 bytes）、 附注前93591-byte normalized/document.txt 正文及33个定位器。论文作者材料及其转换按论文 CC BY 4.0； ICLR2025 STY按官方模板 CC BY 4.0，notation保留goodfeli/dlbook_notation原作者自由使用说明和来源； iclr2025_conference.bst、fancyhdr.sty、natbib.sty及随包原 natbib.dtx独立按LPPL条件，选用1.3c。 两份书目文件仅保留引用字段/排版记录，不外推被引用作品全文；不包括原已省略5份PDF图像、 整个归档、外链代码/数据、外部依赖或其他作品。
