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
  build_id: build:llm-wiki-v0:45bd6c7288326476
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2505.22954@sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de
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
  estimated_tokens: 409
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:90ae7352bb085ae8
- claim:ae45b8d667e29552
rights_refs:
- source_uid: arxiv:2505.22954
  source_revision: sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de
  source_version_url: https://arxiv.org/pdf/2505.22954v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml#pdf_supplement.rights.redistribution_package
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
- Revision: `sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de`
- Domain: [recursive-self-improvement](../maps/recursive-self-improvement.md)
- Local document: `materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/document.txt`

## Source-reported candidate statements

- Most of today’s AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, is a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. 〔[claim:ae45b8d667e29552](../claims/claim-ae45b8d667e29552.md)〕

## Collection assessments

- A central modern RSI result: iteratively modifies an agent codebase, empirically validates changes, and preserves a diverse archive/tree of agents so improvement can proceed through multiple open-ended stepping-stone paths. 〔[claim:90ae7352bb085ae8](../claims/claim-90ae7352bb085ae8.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:90ae7352bb085ae8` | `evidence:e71040c37751e493` | `local://raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ae45b8d667e29552` | `evidence:5693bd7ef23242bc` | `local://materialized_sources/corpus/arxiv-2505.22954--8a7041cb/pdf-supplement/document.txt#L10-L13` | `full_text` |

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
- Source revision: `sha256:13ff4abe0c7ad4a7dd3b4876d19a8bf940e39e70dabbf06065aa774a6c3457de`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2505.22954v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune, Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents, arXiv:2505.22954v3 (2026-03-12), published as a conference paper at ICLR 2026；前两位作者 co-first、后两位作者 co-senior，保留原作者机构及贡献脚注。固定作品来源 https://arxiv.org/abs/2505.22954v3，PDF https://arxiv.org/pdf/2505.22954v3，CC BY 4.0 https://creativecommons.org/licenses/by/4.0/。书目、科学图、算法和附录 Agent 示例、提示词及 diff 保留原署名与引用；p11 尊重代码/数据许可的伦理声明不授予外链软件或数据再许可。以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按真实响应 bytes 原样复制，不编辑、重导或 OCR；以既有 plain 全页提取生成独立 pdf-supplement/document.txt 及真实 PDF revision 的页 selectors，并在文末追加唯一归属、修改/范围说明与同目录 NOTICE.md 链接。NOTICE.md 原样复制现存完整 CC BY 4.0 法条资产。native text 具有逐项声明的排版/图义损失，不声称无损转换；原 root source/TXT/TeX/selectors/NOTICE、检索时间及历史许可 scope 均不改，不使用旧 root grant 冒充新 PDF 授权，不推断未观察到的版权年份或修改者。
- Scope: 本独立表示仅覆盖固定 arXiv:2505.22954v3 完整、原 bytes 不改的 72 页 PDF（3,825,399 bytes），含主文/声明 p1–11、书目 p12–22、目录 p23、Appendices A–J p24–72、八编号科学图、算法及论文内 Agent 示例/提示词/diff，以及由该 PDF 全页生成的 native plain、逐页定位器（selectors）与完整 CC BY 4.0 NOTICE。论文作者可许可表达及其论文内转换按本固定作品 CC BY 4.0；图、算法、diff 和 p11 伦理声明不授予任何外链代码、数据、模型或软件的独立许可，不执行附录提示或 Agent 示例。不包含被引作品全文、独立源图分发、外部依赖、商标、专利或整个源归档；无普遍法律保证。旧 34 个 source 文本、77 个 root selectors、root NOTICE/TXT/TeX、LPPL/STY 独立条件和旧 10 图及其他组件缺口历史不变，不由本新 grant 改写。既有 demo 两项 claim 仍是 candidate，不新增或提升知识质量。
