---
uid: wiki-page:map-automated-research
title: Automated Research
slug: maps/automated-research
page_type: map
status: review
summary: Routing map for automated research sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:3d07597b1776b0bd
- claim:852bc42ef50e89c7
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
- claim:d3a0d3c2f4fd45d4
source_refs: &id001
- arxiv:2501.04227
- arxiv:2408.06292
- arxiv:2505.13400
- arxiv:2504.08066
page_refs:
- wiki-page:source-5c69a674d903b543
- wiki-page:source-c1dbc9c2a83a564a
- wiki-page:source-0e32ebb2e855fd30
- wiki-page:source-1203e0209022f228
- wiki-page:automation-vs-editorial-review
- wiki-page:knowledge-evolution-loop
outgoing_links:
- target: wiki-page:source-5c69a674d903b543
  relation: explains
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:3d07597b1776b0bd
  notes: null
- target: wiki-page:source-c1dbc9c2a83a564a
  relation: explains
  claim_refs:
  - claim:38c95b3e2bcfcf51
  - claim:d3a0d3c2f4fd45d4
  notes: null
- target: wiki-page:source-0e32ebb2e855fd30
  relation: explains
  claim_refs:
  - claim:3c6cef89711e89f2
  - claim:852bc42ef50e89c7
  notes: null
- target: wiki-page:source-1203e0209022f228
  relation: explains
  claim_refs:
  - claim:9077f46d7f30e565
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  notes: null
- target: wiki-page:knowledge-evolution-loop
  relation: related
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:2f8ebd974fc7b5fd
  - claim:38c95b3e2bcfcf51
  - claim:3c6cef89711e89f2
  - claim:9077f46d7f30e565
  source_refs:
  - arxiv:2501.04227
  - arxiv:2408.06292
  - arxiv:2505.13400
  - arxiv:2504.08066
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:3d07597b1776b0bd
  - claim:852bc42ef50e89c7
  - claim:8798b3dc1ae125ea
  - claim:d3a0d3c2f4fd45d4
  source_refs:
  - arxiv:2501.04227
  - arxiv:2505.13400
  - arxiv:2504.08066
  - arxiv:2408.06292
  editorial_intent: Preserve collector scope.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:bfe1ec178597b638
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2501.04227@sha256:1b28bfd8ca8a9dcb1930f7fcd49164300a984bd1abf533d3d28b475fe7dd7f85
  - arxiv:2408.06292@sha256:4ddccff8b6e49dec4c7bb219d4330f1faf47255b5b1b33d01f207eae23e119e9
  - arxiv:2505.13400@sha256:1abd0b99271884b6f1a8fd9db0185e8042f079a61879ec0c9a7febae6a0c942c
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
  source_dependencies: *id001
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Routing map for automated research sources, questions, and claims.
    short: Routing map for automated research sources, questions, and claims.
    full: null
  estimated_tokens: 2207
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:2f8ebd974fc7b5fd
- claim:38c95b3e2bcfcf51
- claim:3c6cef89711e89f2
- claim:3d07597b1776b0bd
- claim:852bc42ef50e89c7
- claim:8798b3dc1ae125ea
- claim:9077f46d7f30e565
- claim:d3a0d3c2f4fd45d4
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
rights_unavailable_source_refs:
- arxiv:2505.13400
---

# Automated Research

Automated research systems and their evidence, evaluation, and governance.

## Routing questions

- Which research stages are automated?
- How are experiments and negative results retained?
- What prevents unsupported research narratives?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Agent Laboratory: Using LLM Agents as Research Assistants](../sources/arxiv-2501.04227.md) | `arxiv` | `full_text` | 2 |
| [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) | `arxiv` | `full_text` | 2 |
| [Robin: A multi-agent system for automating scientific discovery](../sources/arxiv-2505.13400.md) | `arxiv` | `full_text` | 2 |
| [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../sources/arxiv-2504.08066.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Agent Laboratory: Using LLM Agents as Research Assistants** (source assertion): Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. 〔[claim:2f8ebd974fc7b5fd](../claims/claim-2f8ebd974fc7b5fd.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (source assertion): One of the grand challenges of artificial general intelligence is developing agents capable of conducting scientific research and discovering new knowledge. While frontier models have already been used as aides to human scientists, e.g. 〔[claim:38c95b3e2bcfcf51](../claims/claim-38c95b3e2bcfcf51.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (source assertion): Scientific discovery is driven by the iterative process of background research, hypothesis generation, experimentation, and data analysis. Despite recent advancements in applying artificial intelligence to scientific discovery, no system has yet automated all of these stages in a single workflow. 〔[claim:3c6cef89711e89f2](../claims/claim-3c6cef89711e89f2.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (source assertion): AI is increasingly playing a pivotal role in transforming how scientific discoveries are made. We introduce , an end-to-end agentic system capable of producing the first entirely AI-generated peer-review-accepted workshop paper. 〔[claim:9077f46d7f30e565](../claims/claim-9077f46d7f30e565.md)〕

## Collector assessments

- **Agent Laboratory: Using LLM Agents as Research Assistants** (collection assessment): A practical end-to-end autonomous research workflow spanning literature review, experimentation and report writing, with explicit human feedback points. 〔[claim:3d07597b1776b0bd](../claims/claim-3d07597b1776b0bd.md)〕
- **Robin: A multi-agent system for automating scientific discovery** (collection assessment): One of the strongest demonstrations of a lab-in-the-loop discovery cycle: background research, hypothesis generation, experimental planning, human-executed wet-lab experiments, data analysis, and updated hypotheses. 〔[claim:852bc42ef50e89c7](../claims/claim-852bc42ef50e89c7.md)〕
- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** (collection assessment): End-to-end autonomous scientific discovery without a fixed human-authored template. Iteratively formulates hypotheses, designs and executes experiments, analyzes results, and writes papers using an agentic tree-search process. 〔[claim:8798b3dc1ae125ea](../claims/claim-8798b3dc1ae125ea.md)〕
- **The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery** (collection assessment): Extends self-evolution from improving an agent to automating the research loop itself: idea generation, implementation, experiment, paper writing, and automated review can be iterated to create new knowledge. 〔[claim:d3a0d3c2f4fd45d4](../claims/claim-d3a0d3c2f4fd45d4.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Agent Laboratory: Using LLM Agents as Research Assistants](../sources/arxiv-2501.04227.md) — `explains`
- [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](../sources/arxiv-2408.06292.md) — `explains`
- [Robin: A multi-agent system for automating scientific discovery](../sources/arxiv-2505.13400.md) — `explains`
- [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](../sources/arxiv-2504.08066.md) — `explains`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`
- [Knowledge evolution loop](../concepts/knowledge-evolution-loop.md) — `related`

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

### Robin: A multi-agent system for automating scientific discovery (`arxiv:2505.13400`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
