---
uid: wiki-page:source-1203e0209022f228
title: 'The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search'
slug: sources/arxiv-2504.08066
page_type: source
status: review
summary: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
  with claim/evidence expansion.'
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
source_refs: &id002
- arxiv:2504.08066
page_refs:
- wiki-page:map-automated-research
- wiki-page:evidence-638ecd816dce953d
- wiki-page:evidence-caa99c40bb0689a1
outgoing_links:
- target: wiki-page:map-automated-research
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-638ecd816dce953d
  relation: evidenced_by
  claim_refs:
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:evidence-caa99c40bb0689a1
  relation: evidenced_by
  claim_refs:
  - claim:9077f46d7f30e565
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:9077f46d7f30e565
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:8798b3dc1ae125ea
  source_refs:
  - arxiv:2504.08066
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:59348b6351fcf392
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2504.08066@sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
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
    one_line: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    short: 'Source page for The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree
      Search with claim/evidence expansion.'
    full: null
  estimated_tokens: 869
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
rights_refs:
- source_uid: arxiv:2504.08066
  source_revision: sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e
  source_version_url: https://arxiv.org/abs/2504.08066v1
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/ai-scientist-v2-v1-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md
  package_path: materialized_sources/corpus/arxiv-2504.08066--22ed15f2/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:9077f46d7f30e565
rights_unavailable_source_refs: []
---

# The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2504.08066`
- Canonical ID: `2504.08066`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e`
- Domain: [automated-research](../maps/automated-research.md)
- Local document: `materialized_sources/corpus/arxiv-2504.08066--22ed15f2/normalized/document.txt`

## Source-reported candidate statements

- AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

## Collection assessments

- End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process. 〔[claim:8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:8798b3dc1ae125ea` | `evidence:924a40542eeaca58` | `local://raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:9077f46d7f30e565` | `evidence:85c1017952d003b4` | `local://materialized_sources/corpus/arxiv-2504.08066--22ed15f2/normalized/document.txt#L598-L599` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Automated Research](../maps/automated-research.md) — `part_of`
- [Claim 8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md) — `evidenced_by`
- [Claim 9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search (`arxiv:2504.08066`)

- Components: `claim:9077f46d7f30e565`
- Source revision: `sha256:ea458b4c4212b9e61d909193504485986780026a962727da8669877f6f76740e`
- Source version: [pinned upstream version](https://arxiv.org/abs/2504.08066v1)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/ai-scientist-v2-v1-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md](../../../../raw_data/licenses/ai-scientist-v2-v1-cc-by-4.0-gdm-cc-by-sa-4.0-lppl-1.3c-natbib-source.md)
- Attribution: Paper attribution: copied/derived text from "The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search", fixed arXiv 2504.08066v1, by Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune, David Ha. Source and article license record: https://arxiv.org/abs/2504.08066v1. The authors' and submitter's licensable paper expression is under Creative Commons Attribution 4.0 International (CC BY 4.0): https://creativecommons.org/licenses/by/4.0/; full legal code: https://creativecommons.org/licenses/by/4.0/legalcode.en. This article-level license does not replace any separately stated third-party component or review-text license.

Google DeepMind template attribution: source/include/gdm_format.cls is copied unchanged, Google DeepMind paper template v0.4 (September 2023), with the original "DeepMind, London, 2019" attribution and shakir@ review-contact notice retained. Its own Attribution-ShareAlike 4.0 International grant remains separate: https://creativecommons.org/licenses/by-sa/4.0/; full legal code: https://creativecommons.org/licenses/by-sa/4.0/legalcode.en. Original retained member source: https://arxiv.org/src/2504.08066v1. Any reuse or adaptation of this template remains under that component's CC BY-SA 4.0 conditions; including it in this collection does not extend ShareAlike to the independent paper or the entire repository.

Natbib attribution and source accompaniment: source/natbib.sty is copied unchanged, version 2009/07/16 8.31 (PWD, AO), Copyright 1993-2009 Patrick W Daly; the original source credits Arthur Ogawa's contribution. Its own LPPL version 1-or-later grant is retained, and this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. The original generated-file notice requiring accompaniment by natbib.dtx is preserved, not waived. The complete original 248383-byte natbib.dtx is included, without code changes, as the explicitly named source block in this capsule's NOTICE.md; the repository also retains the exact original at raw_data/licenses/components/natbib-8.31/natbib.dtx. Original historical source URL: https://sources.debian.org/data/main/t/texlive-base/2009-11%2Bsqueeze1/texmf-dist/source/latex/natbib/natbib.dtx. This source and its notices are not relicensed under the paper's Creative Commons license.

Fancyhdr attribution: source/fancyhdr.sty is copied unchanged, version 3.2, by Piet van Oostrum, Department of Computer and Information Sciences, University of Utrecht, with the original contact and modification history retained. Its independent LPPL version 1-or-later grant is preserved; this package elects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c/. Historical component source: https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2009/tlnet/archive/fancyhdr.tar.xz. No additional natbib-specific source accompaniment condition is inferred for fancyhdr.

Independent human-review attributions: the following seven retained review texts are attributed separately to their anonymous reviewer labels and original paths, with source report https://arxiv.org/abs/2504.08066v1. The applicable Comment/review license is CC BY 4.0, https://creativecommons.org/licenses/by/4.0/, under OpenReview Terms updated 2024-09-24: https://openreview.net/legal/terms.
- source/workshop_papers/compositional_regularization/reviewer_2.txt: anonymous Reviewer #1 in the fixed report.
- source/workshop_papers/compositional_regularization/reviewer_3.txt: anonymous Reviewer #2 in the fixed report.
- source/workshop_papers/label_noise/reviewer_1.txt: anonymous Reviewer #1 in the fixed report.
- source/workshop_papers/label_noise/reviewer_3.txt: anonymous Reviewer #2 in the fixed report.
- source/workshop_papers/pest_prediction/reviewer_1.txt: anonymous Reviewer #1 in the fixed report.
- source/workshop_papers/pest_prediction/reviewer_2.txt: anonymous Reviewer #2 in the fixed report.
- source/workshop_papers/pest_prediction/reviewer_3.txt: anonymous Reviewer #3 in the fixed report.
The two compositional_regularization reviews alone have an explicit inclusion-permission statement in the report. No equivalent consent is asserted for the other five reviews; their license basis is the review/Comment terms, not public API readability. No real-world identity or public-forum match is inferred; the submissions were withdrawn. The original anonymous texts and paths are retained unchanged.

- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. The existing retained TeX source files and normalized/document.tex are preserved byte-for-byte. The existing text body is the materializer's TeX-to-plain-text conversion with flattened input/include files, removed comments, simplified commands and citation syntax, and omitted non-text archive members; those transformations predate this notice. This packaging adds only one attribution/redistribution footer to normalized/document.txt and a capsule-root NOTICE.md, including the unchanged original natbib.dtx source block. Component code, filenames, runtime identities and existing selector content are not changed.
- Scope: 仅覆盖固定 arXiv 2504.08066v1 当前保留的 source 文字成员、正文转换与 selector；作者/提交者有权许可的论文表达适用 CC BY 4.0。source/include/gdm_format.cls 单独保留 Google DeepMind 的 CC BY-SA 4.0，SA 不外推独立论文或整仓库。source/natbib.sty 及完整原 natbib.dtx 单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c，并履行该 natbib 生成件的原源码随附条件。source/fancyhdr.sty 单独按原 LPPL 1-or-later、本包选用 LPPL 1.3c。七份匿名 human-review 文本按逐路径/Reviewer 编号独立署名并适用 OpenReview Comment 的 CC BY 4.0，不虚构全体同意、去匿名身份或公开 forum 匹配。不覆盖未保存的图像/PDF、外链媒体、模型、程序或数据包、商标、专利及权利人无权许可的材料；没有删除已存文字以回避独立许可条件，不添加限制或暗示上游支持。
