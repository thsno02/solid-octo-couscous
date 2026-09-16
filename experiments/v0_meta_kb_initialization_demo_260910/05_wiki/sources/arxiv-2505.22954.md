---
uid: wiki-page:source-c29f716871f80314
title: 'Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents'
slug: sources/arxiv-2505.22954
page_type: source
status: review
summary: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
  expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:90ae7352bb085ae8
- claim:ae45b8d667e29552
source_refs: &id002
- arxiv:2505.22954
page_refs:
- wiki-page:map-recursive-self-improvement
- wiki-page:evidence-e923ecfc4b63b02d
- wiki-page:evidence-21eaae99382a895a
outgoing_links:
- target: wiki-page:map-recursive-self-improvement
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-e923ecfc4b63b02d
  relation: evidenced_by
  claim_refs:
  - claim:90ae7352bb085ae8
  notes: null
- target: wiki-page:evidence-21eaae99382a895a
  relation: evidenced_by
  claim_refs:
  - claim:ae45b8d667e29552
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ae45b8d667e29552
  source_refs:
  - arxiv:2505.22954
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:90ae7352bb085ae8
  source_refs:
  - arxiv:2505.22954
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
  - arxiv:2505.22954@sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
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
    one_line: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
      expansion.'
    short: 'Source page for Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 427
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:90ae7352bb085ae8
- claim:ae45b8d667e29552
rights_refs:
- source_uid: arxiv:2505.22954
  source_revision: sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed
  source_version_url: https://arxiv.org/abs/2505.22954v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md
  package_path: materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ae45b8d667e29552
rights_unavailable_source_refs: []
---

# Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2505.22954`
- Canonical ID: `2505.22954`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Local document: `materialized_sources/corpus/arxiv-2505.22954--8a7041cb/normalized/document.txt`

## Source-reported candidate statements

- Most of today's AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕

## Collection assessments

- A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths. 〔[claim:90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:90ae7352bb085ae8` | `evidence:e71040c37751e493` | `local://raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ae45b8d667e29552` | `evidence:5693bd7ef23242bc` | `local://materialized_sources/corpus/arxiv-2505.22954--8a7041cb/normalized/document.txt#L88-L88` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Recursive Self Improvement](../maps/recursive-self-improvement.md) — `part_of`
- [Claim 90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md) — `evidenced_by`
- [Claim ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents (`arxiv:2505.22954`)

- Components: `claim:ae45b8d667e29552`
- Source revision: `sha256:9ce27273d9175badbb14d1181bc6166c7afd5e7989ac274d3d5187413e19b9ed`
- Source version: [pinned upstream version](https://arxiv.org/abs/2505.22954v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md](../../../../raw_data/licenses/dgm-v3-cc-by-4.0-iclr-adaptation-lppl-1.3c-natbib-source.md)
- Attribution: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune, Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents, arXiv:2505.22954v3 (2026-03-12), https://arxiv.org/abs/2505.22954v3, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. ICLR, Template for ICLR 2025 Conference Submission, CC BY 4.0, https://www.overleaf.com/latex/templates/template-for-iclr-2025-conference-submission/gqzkdyycxtvt; retain Hugo Larochelle's NIPS-style adaptation credit. Official ICLR2026 copy at https://github.com/ICLR/Master-Template/commit/067b60c3985bd549c8b1afabb426a007905cea46 changes two year labels; local STY additionally centers the author table (l→c), modifier unknown. BST: Copyright 2010 Hal Daum\'e III, J. Fürnkranz label modifications, Copyright 1993-2007 Patrick W Daly; fancyhdr 3.2: Piet van Oostrum; natbib 8.31: Copyright 1993-2009 Patrick W Daly, 2009/07/16 original source. Components retain independent LPPL version 1 or later, selecting LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c.txt. 完整原 natbib.dtx 随 NOTICE.md 及 raw_data/licenses/components/natbib-8.31/natbib.dtx 提供； 00README.json 是 arXiv 自动编译元数据，按 https://info.arxiv.org/help/policies/submission_agreement.html#metadata-license 的CC0范围单列。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 34份源文本及原版权、归属和历史修改不改；复用现有 TeX 合并与纯文本转换， normalized/document.tex 和77个定位器不改，normalized/document.txt 仅在文末追加唯一署名、 修改/范围说明及 NOTICE.md 链接。ICLR模板的两处年份变化和作者表格l→c是已披露既存差异， 不虚构修改者或本仓库实施历史；完整法律文本及原 natbib.dtx 伴随保存，不声称维护者支持本仓库修改。
- Scope: 仅34份实存 source 文本（390140 bytes）、normalized/document.tex（227665 bytes）、 附注前190099-byte normalized/document.txt 正文和77个定位器。论文作者发布的正文、附录、 Agent代码/提示/差异与模型样例及其转换按论文BY4；ICLR模板表达和已披露改编按原2025模板BY4； BST、fancyhdr、natbib与伴随原dtx独立按LPPL条件，选择1.3c；arXiv编译元数据单列CC0。 main.bib只保留书目字段，没有额外abstract/copyright字段，不授权被引作品全文； 不包括原已省略10份PDF图像、未保存的math_commands/gdm_format组件、整个归档、外链代码/数据或外部依赖。
