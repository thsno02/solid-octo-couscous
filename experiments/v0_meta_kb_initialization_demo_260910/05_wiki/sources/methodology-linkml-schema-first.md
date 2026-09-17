---
uid: wiki-page:source-93365d53a252ec8d
title: LinkML schema-first knowledge modeling
slug: sources/methodology-linkml-schema-first
page_type: source
status: review
summary: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:27f7e77bbaa0d47f
- claim:583280271287ef9c
source_refs: &id002
- methodology:linkml-schema-first
page_refs:
- wiki-page:map-ontology-semantic-architecture
- wiki-page:evidence-b0da231e5faa8371
- wiki-page:evidence-1e92251bcd39495b
outgoing_links:
- target: wiki-page:map-ontology-semantic-architecture
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-b0da231e5faa8371
  relation: evidenced_by
  claim_refs:
  - claim:27f7e77bbaa0d47f
  notes: null
- target: wiki-page:evidence-1e92251bcd39495b
  relation: evidenced_by
  claim_refs:
  - claim:583280271287ef9c
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:583280271287ef9c
  source_refs:
  - methodology:linkml-schema-first
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:27f7e77bbaa0d47f
  source_refs:
  - methodology:linkml-schema-first
  editorial_intent: Keep collector interpretation separate.
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
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
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
    one_line: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
    short: Source page for LinkML schema-first knowledge modeling with claim/evidence expansion.
    full: null
  estimated_tokens: 292
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:27f7e77bbaa0d47f
- claim:583280271287ef9c
rights_refs:
- source_uid: methodology:linkml-schema-first
  source_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  source_version_url: https://linkml.io/linkml/
  license_spdx: Apache-2.0 AND MIT
  license_url: https://www.apache.org/licenses/LICENSE-2.0
  notice_path: raw_data/licenses/linkml-page-body-02-260917.md
  package_path: materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:583280271287ef9c
rights_unavailable_source_refs: []
---

# LinkML schema-first knowledge modeling

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `methodology:linkml-schema-first`
- Canonical ID: `METHODOLOGY-LINKML`
- Source type: `methodology`
- Content tier: `full_text`
- Revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Domain: [ontology-semantic-architecture](../maps/ontology-semantic-architecture.md)
- Local document: `materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/document.md`

## Source-reported candidate statements

- Everything you need to know about [LinkML](https://linkml.io), the Linked Data Modeling Language. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕

## Collection assessments

- Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts. 〔[claim:27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:27f7e77bbaa0d47f` | `evidence:d3ebb3860ae3f34c` | `local://raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:583280271287ef9c` | `evidence:b0f0f32b0b4cc957` | `local://materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/normalized/document.md#L24-L24` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Ontology Semantic Architecture](../maps/ontology-semantic-architecture.md) — `part_of`
- [Claim 27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md) — `evidenced_by`
- [Claim 583280271287ef9c](../claims/claim-583280271287ef9c.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### LinkML schema-first knowledge modeling (`methodology:linkml-schema-first`)

- Components: `claim:583280271287ef9c`
- Source revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Source version: [pinned upstream version](https://linkml.io/linkml/)
- License: [Apache-2.0 AND MIT](https://www.apache.org/licenses/LICENSE-2.0)
- NOTICE: [raw_data/licenses/linkml-page-body-02-260917.md](../../../../raw_data/licenses/linkml-page-body-02-260917.md)
- Attribution: This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0. 原页脚保留Made with Sphinx and @pradyunsg's Furo署名；本原响应实际嵌入Furo2025.12.19模板另按MIT：Copyright (c) 2020 Pradyun Gedam <mail@pradyunsg.me>。完整MIT随NOTICE；保留上游Adapted from Just the Docs以及Feather/Tabler来源线索，不声称各图标全许可链审核或第三方权利担保，不暗示背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原55141B HTML原字节保存；只在派生DOM消费唯一article#furo-main-content，排除a.headerlink的¶ UI符号，保留作者文字、目录href及URI/CURIE代码词法；li/p/blockquote列表层级在Markdown中部分丢失，原HTML可核。结构Markdown、空白连续化、链接解析、源行锚点/sidecar和边界说明属于collector-derived format conversion，不是raw quotation；保守source bounds可至entity EOF，不证明逐行转换或精确closing-tag，article外nav/footer不混正文。新normalized EOF附唯一归属/范围/修改块和NOTICE；旧root doc/164selectors不改，旧NOTICE复制history/NOTICE-before-page-body-02.md，全旧M/C/R review保全，不执行脚本或补造部署commit。
- Scope: 仅本次https://linkml.io/linkml/单页dated-response-2026-09-17T14:20:17Z完整原HTML内作者内容（Apache-2.0）及实际嵌入Furo2025.12.19模板（MIT），并覆盖声明article的normalized/document.md/新sidecar；AND分范围履约不是OR，具体派生bytes/count以manifest为准。旧7340B pre-notice正文/164root selectors和text-only grant另留完整历史。未保存的其他文档页、logo/媒体、远程CSS/JS/依赖/外链作品/代码/数据、商标或无权许可材料不准入；URI引用不是资源已保存/获许可。原UID多页总体边界仍unresolved，partial/full_text不等于whole-UID complete/trusted或离线站点视觉/功能完整。
