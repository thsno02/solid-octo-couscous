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
  build_id: build:llm-wiki-v0:b04c61704bd4b7be
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
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
  estimated_tokens: 574
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:38c95b3e2bcfcf51
rights_refs:
- source_uid: arxiv:2408.06292
  source_revision: sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
  source_version_url: https://arxiv.org/abs/2408.06292v3
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/ai-scientist-v3-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md
  package_path: materialized_sources/corpus/arxiv-2408.06292--522d359c/manifest.yaml#rights.redistribution_package
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
| `evidence:32355b67bcee3a03` | `local://materialized_sources/corpus/arxiv-2408.06292--522d359c/normalized/document.txt#L573-L574` | `materialized_sources/corpus/arxiv-2408.06292--522d359c/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) — `evidenced_by`
- [Automated Research](../maps/automated-research.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery (`arxiv:2408.06292`)

- Components: `claim:38c95b3e2bcfcf51`
- Source revision: `sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9`
- Source version: [pinned upstream version](https://arxiv.org/abs/2408.06292v3)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/ai-scientist-v3-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md](../../../../raw_data/licenses/ai-scientist-v3-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md)
- Attribution: Paper attribution: copied/derived text from "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery", fixed arXiv 2408.06292v3, by Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, David Ha. Source and article license record: https://arxiv.org/abs/2408.06292v3. The authors' and submitter's licensable paper expression is under Creative Commons Attribution 4.0 International (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/; full legal code: https://creativecommons.org/licenses/by/4.0/legalcode.en. This article-level license does not replace any separately stated third-party component or review-text license.

Google DeepMind template attribution: source/include/gdm_format.cls is copied unchanged, Google DeepMind paper template v0.4 (September 2023), with the original "DeepMind, London, 2019" attribution and shakir@ review-contact notice retained. Its own Attribution-ShareAlike 4.0 International grant remains separate: https://creativecommons.org/licenses/by-sa/4.0/; full legal code: https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Original retained member source: https://arxiv.org/src/2408.06292v3. Any reuse or adaptation of this template remains under that component's CC BY-SA 4.0 conditions; including it in this collection does not extend ShareAlike to the independent paper or the entire repository.

Natbib attribution and source accompaniment: source/natbib.sty is copied unchanged, version 2009/07/16 8.31 (PWD, AO), Copyright 1993-2009 Patrick W Daly; the original source credits Arthur Ogawa's contribution. Its own LPPL version 1-or-later grant is retained, and this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. The original generated-file notice requiring accompaniment by natbib.dtx is preserved, not waived. The complete original 248383-byte natbib.dtx is included, without code changes, as the explicitly named source block in this capsule's NOTICE.md; the repository also retains the exact original at raw_data/licenses/components/natbib-8.31/natbib.dtx. Original historical source URL: https://sources.debian.org/data/main/t/texlive-base/2009-11%2Bsqueeze1/texmf-dist/source/latex/natbib/natbib.dtx. This source and its notices are not relicensed under the paper's Creative Commons license.

- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The existing retained TeX source files and normalized/document.tex are preserved byte-for-byte. The existing text body is the materializer's TeX-to-plain-text conversion with flattened input/include files, removed comments, simplified commands and citation syntax, and omitted non-text archive members; those transformations predate this notice. This packaging adds only one attribution/redistribution footer to normalized/document.txt and a capsule-root NOTICE.md, including the unchanged original natbib.dtx source block. Component code, filenames, runtime identities and existing selector content are not changed.
- Scope: 仅覆盖固定 arXiv 2408.06292v3 当前保留的 source 文字成员、正文转换与 selector；作者/提交者有权许可的论文表达适用 CC BY 4.0。source/include/gdm_format.cls 单独保留 Google DeepMind 的 CC BY-SA 4.0，SA 不外推独立论文或整仓库。source/natbib.sty 及完整原 natbib.dtx 单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c，并履行该 natbib 生成件的原源码随附条件。不覆盖未保存的图像/PDF、外链媒体、模型、程序或数据包、商标、专利及权利人无权许可的材料；没有删除已存文字以回避独立许可条件，不添加限制或暗示上游支持。
