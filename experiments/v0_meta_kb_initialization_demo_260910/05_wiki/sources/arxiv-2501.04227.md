---
uid: wiki-page:source-5c69a674d903b543
title: 'Agent Laboratory: Using LLM Agents as Research Assistants'
slug: sources/arxiv-2501.04227
page_type: source
status: review
summary: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:2f8ebd974fc7b5fd
- claim:3d07597b1776b0bd
source_refs: &id002
- arxiv:2501.04227
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-42304939383189ab
- wiki-page:evidence-37d06da8881dd925
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-42304939383189ab
  relation: evidenced_by
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  notes: null
- target: wiki-page:evidence-37d06da8881dd925
  relation: evidenced_by
  claim_refs:
  - claim:3d07597b1776b0bd
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  source_refs:
  - arxiv:2501.04227
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:3d07597b1776b0bd
  source_refs:
  - arxiv:2501.04227
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:3de65e2db5aac4d8
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
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
    one_line: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
    short: 'Source page for Agent Laboratory: Using LLM Agents as Research Assistants with claim/evidence expansion.'
    full: null
  estimated_tokens: 755
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:3d07597b1776b0bd
rights_refs:
- source_uid: arxiv:2501.04227
  source_revision: sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
  source_version_url: https://arxiv.org/abs/2501.04227v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/agent-laboratory-v2-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md
  package_path: materialized_sources/corpus/arxiv-2501.04227--a0515b2c/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:2f8ebd974fc7b5fd
rights_unavailable_source_refs: []
---

# Agent Laboratory: Using LLM Agents as Research Assistants

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2501.04227`
- Canonical ID: `2501.04227`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2501.04227--a0515b2c/normalized/document.txt`

## Source-reported candidate statements

- Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕

## Collection assessments

- A practical end-to-end autonomous research workflow spanning literature review, experimentation and report writing, with explicit human feedback points. 〔[claim:3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:2f8ebd974fc7b5fd` | `evidence:b085c8ded21a947a` | `local://materialized_sources/corpus/arxiv-2501.04227--a0515b2c/normalized/document.txt#L133-L133` | `full_text` |
| `claim:3d07597b1776b0bd` | `evidence:64bae7b35d03441f` | `local://raw_data/arxiv/Agent Laboratory: Using LLM Agents as Research Assistants/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md) — `evidenced_by`
- [Claim 3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Agent Laboratory: Using LLM Agents as Research Assistants (`arxiv:2501.04227`)

- Components: `claim:2f8ebd974fc7b5fd`
- Source revision: `sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85`
- Source version: [pinned upstream version](https://arxiv.org/abs/2501.04227v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/agent-laboratory-v2-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md](../../../../raw_data/licenses/agent-laboratory-v2-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md)
- Attribution: Paper attribution: copied/derived text from "Agent Laboratory: Using LLM Agents as Research Assistants", fixed arXiv 2501.04227v2, by Samuel Schmidgall, Yusheng Su, Ze Wang, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Michael Moor, Zicheng Liu, Emad Barsoum. Source and article license record: https://arxiv.org/abs/2501.04227v2. The authors' and submitter's licensable paper expression is under Creative Commons Attribution 4.0 International (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/; full legal code: https://creativecommons.org/licenses/by/4.0/legalcode.en. This article-level license does not replace any separately stated third-party component or review-text license.

Google DeepMind template attribution: source/gdm_format.cls is copied unchanged, Google DeepMind paper template v0.4 (September 2023), with the original "DeepMind, London, 2019" attribution and shakir@ review-contact notice retained. Its own Attribution-ShareAlike 4.0 International grant remains separate: https://creativecommons.org/licenses/by-sa/4.0/; full legal code: https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Original retained member source: https://arxiv.org/src/2501.04227v2. Any reuse or adaptation of this template remains under that component's CC BY-SA 4.0 conditions; including it in this collection does not extend ShareAlike to the independent paper or the entire repository.

Natbib attribution and source accompaniment: source/natbib.sty is copied unchanged, version 2009/07/16 8.31 (PWD, AO), Copyright 1993-2009 Patrick W Daly; the original source credits Arthur Ogawa's contribution. Its own LPPL version 1-or-later grant is retained, and this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. The original generated-file notice requiring accompaniment by natbib.dtx is preserved, not waived. The complete original 248383-byte natbib.dtx is included, without code changes, as the explicitly named source block in this capsule's NOTICE.md; the repository also retains the exact original at raw_data/licenses/components/natbib-8.31/natbib.dtx. Original historical source URL: https://sources.debian.org/data/main/t/texlive-base/2009-11%2Bsqueeze1/texmf-dist/source/latex/natbib/natbib.dtx. This source and its notices are not relicensed under the paper's Creative Commons license.

Fancyhdr attribution: source/fancyhdr.sty is copied unchanged, version 3.2, by Piet van Oostrum, Department of Computer and Information Sciences, University of Utrecht, with the original contact and modification history retained. Its independent LPPL version 1-or-later grant is preserved; this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. Historical component source: https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2009/tlnet/archive/fancyhdr.tar.xz. No additional natbib-specific source accompaniment condition is inferred for fancyhdr.

BST attribution: source/iclr2021_conference.bst retains its original iclr2017.bst/icml2010.bst/plainnl.bst lineage and notices: Copyright 2010 Hal Daume III (original spelling Hal Daum\'e III), Copyright 1993-2007 Patrick W Daly, and the label-format modifications by J. Fuernkranz (original spelling J. Fürnkranz). Its own LPPL version 1-or-later grant is preserved; this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. Fixed official component reference: https://github.com/ICLR/Master-Template/blob/09727556f8eb5183f03d427d2a285711cc554888/iclr2021/iclr2021_conference.bst. The retained file preserves the original header and program identity; the known Latin-1-to-UTF-8 encoding difference is not a new program-logic modification.

- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The existing retained TeX source files and normalized/document.tex are preserved byte-for-byte. The existing text body is the materializer's TeX-to-plain-text conversion with flattened input/include files, removed comments, simplified commands and citation syntax, and omitted non-text archive members; those transformations predate this notice. This packaging adds only one attribution/redistribution footer to normalized/document.txt and a capsule-root NOTICE.md, including the unchanged original natbib.dtx source block. Component code, filenames, runtime identities and existing selector content are not changed.
- Scope: 仅覆盖固定 arXiv 2501.04227v2 当前保留的 source 文字成员、正文转换与 selector；作者/提交者有权许可的论文表达适用 CC BY 4.0。source/gdm_format.cls 单独保留 Google DeepMind 的 CC BY-SA 4.0，SA 不外推独立论文或整仓库。source/natbib.sty 及完整原 natbib.dtx 单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c，并履行该 natbib 生成件的原源码随附条件。source/fancyhdr.sty 单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c。source/iclr2021_conference.bst 及原上游归属单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c。不覆盖未保存的图像/PDF、外链媒体、模型、程序或数据包、商标、专利及权利人无权许可的材料；没有删除已存文字以回避独立许可条件，不添加限制或暗示上游支持。
