---
uid: wiki-page:source-0e32ebb2e855fd30
title: 'Robin: A multi-agent system for automating scientific discovery'
slug: sources/arxiv-2505.13400
page_type: source
status: review
summary: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:3c6cef89711e89f2
- claim:852bc42ef50e89c7
source_refs: &id002
- arxiv:2505.13400
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-f561a2ece83db79d
- wiki-page:evidence-1f89e493aa80fc8b
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-f561a2ece83db79d
  relation: evidenced_by
  claim_refs:
  - claim:3c6cef89711e89f2
  notes: null
- target: wiki-page:evidence-1f89e493aa80fc8b
  relation: evidenced_by
  claim_refs:
  - claim:852bc42ef50e89c7
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:3c6cef89711e89f2
  source_refs:
  - arxiv:2505.13400
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:852bc42ef50e89c7
  source_refs:
  - arxiv:2505.13400
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:7825e3978fb6a0ee
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2505.13400@sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794
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
    one_line: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence
      expansion.'
    short: 'Source page for Robin: A multi-agent system for automating scientific discovery with claim/evidence
      expansion.'
    full: null
  estimated_tokens: 429
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:3c6cef89711e89f2
- claim:852bc42ef50e89c7
rights_refs:
- source_uid: arxiv:2505.13400
  source_revision: sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794
  source_version_url: https://arxiv.org/pdf/2505.13400v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:3c6cef89711e89f2
rights_unavailable_source_refs: []
---

# Robin: A multi-agent system for automating scientific discovery

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2505.13400`
- Canonical ID: `2505.13400`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/document.txt`

## Source-reported candidate statements

- Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕

## Collection assessments

- One of the strongest demonstrations of a lab-in-the-loop discovery cycle: background research, hypothesis generation, experimental planning, human-executed wet-lab experiments, data analysis, and updated hypotheses. 〔[claim:852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:3c6cef89711e89f2` | `evidence:42eb6cb152f003dc` | `local://materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/document.txt#L10-L12` | `full_text` |
| `claim:852bc42ef50e89c7` | `evidence:876eba3abd8faafc` | `local://raw_data/arxiv/Robin: A multi-agent system for automating scientific discovery/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md) — `evidenced_by`
- [Claim 852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Robin: A multi-agent system for automating scientific discovery (`arxiv:2505.13400`)

- Components: `claim:3c6cef89711e89f2`
- Source revision: `sha256:336d4e3f9065f42918cec8053e020d12c8d8c8031eb4c180764a349d1efa1794`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2505.13400v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/pdf-supplement/NOTICE.md)
- Attribution: Ali Essam Ghareeb; Benjamin Chang; Ludovico Mitchener; Angela Yiu; Caralyn J. Szostkiewicz; Jon M. Laurent; Muhammed T. Razzak; Andrew D. White; Michaela M. Hinks; Samuel G. Rodriques, Robin: A multi-agent system for automating scientific discovery, arXiv:2505.13400v1 (2025-05-19), https://arxiv.org/abs/2505.13400v1, PDF https://arxiv.org/pdf/2505.13400v1, CC BY4 https://creativecommons.org/licenses/by/4.0/。完整十作者 Ali Essam Ghareeb／Benjamin Chang／Ludovico Mitchener／Angela Yiu／Caralyn J. Szostkiewicz／Jon M. Laurent／Muhammed T. Razzak／Andrew D. White／Michaela M. Hinks／Samuel G. Rodriques；Ghareeb/Chang等贡献，White/Rodriques共同监督FutureHouse，Hinks/Rodriques共同监督本工作，FutureHouse／Oxford机构原样，未造逐作者贡献表。p11 Michael Skarlinski／Mayk Caldas／Tyler Nadolski／James Braza／Siddharth Narayanan与FutureHouse致谢保留。p4 Fig2/p6 Fig3明示部分分析由human为publication readability格式化，不改为无人工。p9 Table1供应商catalog引用与Rapamycin Gift from RetroBio（非Rebio）保留。微镜／flow／RNA-seq在原研究表示内保留，不独立重许可底层数据。S10两处重复原样，不补源88bibabstract或其15copyright旧未决。 既有 R 已核固定v1源payload/保留表达与作品BY4；本次PDF可见v1页标、embedded arXivID与License BY4，C核十作者／30页／全部Supplementary Material至S25，主线明确准入。不发明旧固定archive URL。 以上归属不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 固定版本 PDF 按本次真实响应 bytes 原样保留，不编辑、重导或 OCR；以既有 helper 的 plain 全页提取生成独立 pdf-supplement/document.txt 和真实 PDF revision 的页定位器（page selectors），在文末追加唯一归属、修改／范围附注与同目录 NOTICE.md 链接。NOTICE 自包含本项实际归属、精确范围及现存完整 CC BY 4.0 法条；native text 的逐项损失见 limitations，不声称无损转换或可直接执行的源代码／prompt。旧 root source、normalized TXT／TeX、selectors、NOTICE／README、revision、retrieval 和历史 gate 不改，不将新固定版选择冒称旧 source payload 已被追溯核定。
- Scope: 本独立表示仅覆盖固定 arXiv:2505.13400v1 原 bytes 不改的30页 PDF（33781795 bytes）：固定 arXiv:2505.13400v1 完整30物理页编译PDF：p1–7主文Results／Discussion及四科学图，p8–11 Methods4.1–4.5.5／Acknowledgements／Data and Code Availability，p12–15 References[1]–[69]，p16 Supplementary Material／S1，p17–24完整实验assay／therapeutic候选／judge prompts（p22/p24实际重复S10保留），p25–28 S11–S15 human评估／microscopy／flow／RNA-seq，p29–30 S16–S25十类候选至Chronic Kidney Disease十项INF4E。未取外部RNA-seq/.fcs/code/trajectories。 论文作者可许可表达按本固定作品已证 CC BY4 路径；实际有界引用／图板按原件精确信用与身份保留，不改变底层许可、不独立重许被引全文／数据／代码／模型／媒体／商标／源模板或整个source归档。 此范围也包含该PDF native plain、页selectors及完整BY4 NOTICE；旧 root rights／block／retrieval／revision／source_version键缺省和历史原件／文字缺失不改；无普遍权利保证。
