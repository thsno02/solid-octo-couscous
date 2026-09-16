---
uid: wiki-page:map-ontology-semantic-architecture
title: Ontology Semantic Architecture
slug: maps/ontology-semantic-architecture
page_type: map
status: review
summary: Routing map for ontology semantic architecture sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:0edb741be0f31f6f
- claim:27f7e77bbaa0d47f
- claim:3adb88340e0eb2b6
- claim:3e6ec7f46b13c44f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
source_refs: &id001
- arxiv:2511.02824
- methodology:linkml-schema-first
- github:linkml/linkml
page_refs:
- wiki-page:source-51ed59b1fc0ecd08
- wiki-page:source-93365d53a252ec8d
- wiki-page:source-8a8c72b9ad5bf51d
- wiki-page:claim-evidence-page-compilation
- wiki-page:llm-wiki-reference-system
outgoing_links:
- target: wiki-page:source-51ed59b1fc0ecd08
  relation: explains
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:3e6ec7f46b13c44f
  notes: null
- target: wiki-page:source-93365d53a252ec8d
  relation: explains
  claim_refs:
  - claim:583280271287ef9c
  - claim:27f7e77bbaa0d47f
  notes: null
- target: wiki-page:source-8a8c72b9ad5bf51d
  relation: explains
  claim_refs:
  - claim:fc57f26307cefee3
  - claim:3adb88340e0eb2b6
  notes: null
- target: wiki-page:claim-evidence-page-compilation
  relation: related
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  notes: null
- target: wiki-page:llm-wiki-reference-system
  relation: related
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:0edb741be0f31f6f
  - claim:583280271287ef9c
  - claim:fc57f26307cefee3
  source_refs:
  - arxiv:2511.02824
  - methodology:linkml-schema-first
  - github:linkml/linkml
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:27f7e77bbaa0d47f
  - claim:3adb88340e0eb2b6
  - claim:3e6ec7f46b13c44f
  source_refs:
  - methodology:linkml-schema-first
  - github:linkml/linkml
  - arxiv:2511.02824
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:699e317011de119b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2511.02824@sha256:6c71312f8e88b313baf4eeb44a39fefa9f09ad5bd247e176e49824310cf5fb5e
  - methodology:linkml-schema-first@sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  - github:linkml/linkml@0e401cef2711b0f12f5a1870805c5cfa999b0858
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
    one_line: Routing map for ontology semantic architecture sources, questions, and claims.
    short: Routing map for ontology semantic architecture sources, questions, and claims.
    full: null
  estimated_tokens: 600
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:0edb741be0f31f6f
- claim:27f7e77bbaa0d47f
- claim:3adb88340e0eb2b6
- claim:3e6ec7f46b13c44f
- claim:583280271287ef9c
- claim:fc57f26307cefee3
rights_refs:
- source_uid: methodology:linkml-schema-first
  source_revision: sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c
  source_version_url: https://linkml.io/linkml/
  license_spdx: Apache-2.0
  license_url: https://www.apache.org/licenses/LICENSE-2.0
  notice_path: raw_data/licenses/apache-2.0.md
  package_path: materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:583280271287ef9c
rights_unavailable_source_refs:
- arxiv:2511.02824
- github:linkml/linkml
---

# Ontology Semantic Architecture

Stable identity, schema, typed relations, provenance, and semantic change.

## Routing questions

- Which identifiers remain stable?
- How are schema changes migrated and rolled back?
- How are source, claim, evidence, page, time, and policy separated?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Kosmos: An AI Scientist for Autonomous Discovery](../sources/arxiv-2511.02824.md) | `arxiv` | `full_text` | 2 |
| [LinkML schema-first knowledge modeling](../sources/methodology-linkml-schema-first.md) | `methodology` | `full_text` | 2 |
| [linkml/linkml](../sources/github-linkml-linkml.md) | `github` | `semantic_capsule` | 2 |

## Source-reported signals

- **Kosmos: An AI Scientist for Autonomous Discovery** (source assertion): Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depth of their findings. 〔[claim:0edb741be0f31f6f](../claims/claim-0edb741be0f31f6f.md)〕
- **LinkML schema-first knowledge modeling** (source assertion): LinkML is a flexible modeling language that allows you to author schemas in YAML that describe the structure of your data. 〔[claim:583280271287ef9c](../claims/claim-583280271287ef9c.md)〕
- **linkml/linkml** (source assertion): LinkML is a linked data modeling language following object-oriented and ontological principles. 〔[claim:fc57f26307cefee3](../claims/claim-fc57f26307cefee3.md)〕

## Collector assessments

- **LinkML schema-first knowledge modeling** (collection assessment): Modern developer-friendly source model that generates JSON Schema, OWL, SHACL, code, SQL and other artifacts. 〔[claim:27f7e77bbaa0d47f](../claims/claim-27f7e77bbaa0d47f.md)〕
- **linkml/linkml** (collection assessment): Modern schema-first bridge between developer data models and linked-data/ontology artifacts. 〔[claim:3adb88340e0eb2b6](../claims/claim-3adb88340e0eb2b6.md)〕
- **Kosmos: An AI Scientist for Autonomous Discovery** (collection assessment): Long-horizon autonomous data-driven discovery. Kosmos repeatedly interleaves literature search, data analysis and hypothesis generation while maintaining a structured world model across hundreds of agent rollouts. 〔[claim:3e6ec7f46b13c44f](../claims/claim-3e6ec7f46b13c44f.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Kosmos: An AI Scientist for Autonomous Discovery](../sources/arxiv-2511.02824.md) — `explains`
- [LinkML schema-first knowledge modeling](../sources/methodology-linkml-schema-first.md) — `explains`
- [linkml/linkml](../sources/github-linkml-linkml.md) — `explains`
- [Claim–evidence–page compilation](../methods/claim-evidence-page.md) — `related`
- [LLM Wiki reference system](../systems/reference-system.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### LinkML schema-first knowledge modeling (`methodology:linkml-schema-first`)

- Components: `claim:583280271287ef9c`
- Source revision: `sha256:93a9f00b0006695dab8f1bde801a40e36eed8c236c4c839aff645bec38b5dc6c`
- Source version: [pinned upstream version](https://linkml.io/linkml/)
- License: [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0)
- NOTICE: [raw_data/licenses/apache-2.0.md](../../../../raw_data/licenses/apache-2.0.md)
- Attribution: This document includes material copied from or derived from "LinkML Documentation", https://linkml.io/linkml/. Copyright 2021-2026 LinkML Authors. SPDX-License-Identifier: Apache-2.0. Licensed under the Apache License, Version 2.0, https://www.apache.org/licenses/LICENSE-2.0.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. Converted the captured LinkML HTML landing page to Markdown; navigation, headings, hyperlinks, whitespace, and footnote markers were omitted or normalized, while CSS, JavaScript, theme files, and media were not stored; 164 selector excerpts were generated. The upstream copyright and Apache-2.0 statement are restored in this attribution block.
- Scope: 仅覆盖当前 https://linkml.io/linkml/ 单页经转换后、许可附注前的 7,340-byte 既有 Markdown 正文及其 164 个 selector 摘录；不声称存储或覆盖 LinkML 整个文档站、其他页面正文、主题、JavaScript、CSS、媒体、外链作品、商标或权利人无权许可的第三方材料。

### Kosmos: An AI Scientist for Autonomous Discovery (`arxiv:2511.02824`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### linkml/linkml (`github:linkml/linkml`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
