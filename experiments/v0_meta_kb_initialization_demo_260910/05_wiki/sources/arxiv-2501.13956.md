---
uid: wiki-page:source-f4f68942b55357ed
title: 'Zep: A Temporal Knowledge Graph Architecture for Agent Memory'
slug: sources/arxiv-2501.13956
page_type: source
status: review
summary: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:419c77c89a471f8e
- claim:ef04f2ebbd2da425
source_refs: &id002
- arxiv:2501.13956
page_refs:
- wiki-page:map-knowledge-memory
- wiki-page:evidence-7781d7df52d59b86
- wiki-page:evidence-410ef6d7fb5163de
outgoing_links:
- target: wiki-page:map-knowledge-memory
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-7781d7df52d59b86
  relation: evidenced_by
  claim_refs:
  - claim:419c77c89a471f8e
  notes: null
- target: wiki-page:evidence-410ef6d7fb5163de
  relation: evidenced_by
  claim_refs:
  - claim:ef04f2ebbd2da425
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:ef04f2ebbd2da425
  source_refs:
  - arxiv:2501.13956
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:419c77c89a471f8e
  source_refs:
  - arxiv:2501.13956
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:aad2073b7a3459ff
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.13956@sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
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
    one_line: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence
      expansion.'
    short: 'Source page for Zep: A Temporal Knowledge Graph Architecture for Agent Memory with claim/evidence expansion.'
    full: null
  estimated_tokens: 541
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:419c77c89a471f8e
- claim:ef04f2ebbd2da425
rights_refs:
- source_uid: arxiv:2501.13956
  source_revision: sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51
  source_version_url: https://arxiv.org/abs/2501.13956v1
  license_spdx: CC-BY-NC-SA-4.0
  license_url: https://creativecommons.org/licenses/by-nc-sa/4.0/
  notice_path: raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md
  package_path: materialized_sources/corpus/arxiv-2501.13956--b93a114f/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:ef04f2ebbd2da425
rights_unavailable_source_refs: []
---

# Zep: A Temporal Knowledge Graph Architecture for Agent Memory

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2501.13956`
- Canonical ID: `2501.13956`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51`
- Domain: [knowledge-memory](../maps/knowledge-memory.md)
- Local document: `materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt`

## Source-reported candidate statements

- We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT, in the Deep Memory Retrieval (DMR) benchmark. Additionally, Zep excels in more comprehensive and challenging evaluations than DMR that better reflect real-world enterprise use cases. 〔[claim:ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md)〕

## Collection assessments

- A directly relevant architecture for continuously integrating conversational and business data into a temporally-aware knowledge graph while preserving historical relationships. 〔[claim:419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:419c77c89a471f8e` | `evidence:82efa10dc6344376` | `local://raw_data/arxiv/Zep: A Temporal Knowledge Graph Architecture for Agent Memory/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:ef04f2ebbd2da425` | `evidence:420fd60b33cee2a7` | `local://materialized_sources/corpus/arxiv-2501.13956--b93a114f/normalized/document.txt#L73-L73` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Knowledge Memory](../maps/knowledge-memory.md) — `part_of`
- [Claim 419c77c89a471f8e](../claims/claim-419c77c89a471f8e.md) — `evidenced_by`
- [Claim ef04f2ebbd2da425](../claims/claim-ef04f2ebbd2da425.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Zep: A Temporal Knowledge Graph Architecture for Agent Memory (`arxiv:2501.13956`)

- Components: `claim:ef04f2ebbd2da425`
- Source revision: `sha256:d98c3a619caf66173e92e9a21829b32312db83156e30ede9e6bb45c1c6016d51`
- Source version: [pinned upstream version](https://arxiv.org/abs/2501.13956v1)
- License: [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- NOTICE: [raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md](../../../../raw_data/licenses/arxiv-cc-by-nc-sa-4.0-prime-cc-by-4.0-george-kour-mit.md)
- Attribution: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory", arXiv:2501.13956v1, by Preston Rasmussen; Pavlo Paliychuk; Travis Beauvais; Jack Ryan; and Daniel Chalef. Source: https://arxiv.org/abs/2501.13956v1. The article-author material is licensed under CC BY-NC-SA 4.0: https://creativecommons.org/licenses/by-nc-sa/4.0/. This repository has not yet verified that its intended publication is NonCommercial; this package is not a publication approval. source/PRIMEarxiv.sty corresponds to the Arxiv & PRIME AI Style Template adapted by Moulay A. Akhloufi, https://www.overleaf.com/latex/templates/arxiv-and-prime-ai-style-template/qdnhqytdqzsc, licensed under CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. That adaptation is based on George Kour's arxiv-style, https://github.com/kourgeorge/arxiv-style; its base portions retain Copyright (c) 2020 George Kour and the MIT License. The retained Zep style enables the page footer that the otherwise matching PaperQA2 copy comments out; the modifier of this one-line variant is unknown and is not attributed to the paper authors.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The fixed v1 source archive is unpacked and its four text members—source/main.tex, source/main.bbl, source/references.bib, and source/PRIMEarxiv.sty—are retained without modification. main.tex is copied to normalized/document.tex and converted to normalized/document.txt; 29 selectors are generated; the article attribution, Moulay A. Akhloufi template attribution, George Kour MIT notice, modification statement, and NOTICE link are appended to normalized/document.txt. For provenance, the retained Zep PRIMEarxiv.sty is recorded as differing from the otherwise matching PaperQA2 copy only at line 35 by enabling the page footer; this packaging does not identify the author of that pre-existing variant.
- Scope: 本组合包仅覆盖固定 arXiv v1 胶囊实际保存的四个 source 文字成员、normalized/document.tex、normalized/document.txt 与 29 个 selector。论文作者材料及其文本转换和 selector 派生物按 CC BY-NC-SA 4.0 履约，任何共享仅限非商业用途，派生输出须采用同一或兼容许可；当前仓库用途尚未完成非商业核实，故本包不表示发布已获准，未来商业用途须另行取得授权。source/PRIMEarxiv.sty 作为 Moulay A. Akhloufi 改编的 PRIME 模板按 CC BY 4.0 履约，并对其所基于的 George Kour arxiv-style 保留 MIT 版权和许可；Zep 所存版本相对 PaperQA2 对应副本仅启用第 35 行页脚，本包记录该差异但不把修改归给论文作者。main.bbl 与 references.bib 作为排版记录和引用元数据保留，不授权其所引用作品。许可不外推到外链论文、代码、数据或权利人无权许可的第三方材料。
