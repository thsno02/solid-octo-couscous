---
uid: wiki-page:map-cross-cutting
title: Cross Cutting
slug: maps/cross-cutting
page_type: map
status: review
summary: Routing map for cross cutting sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:00e6310ce97dc279
- claim:0d2b54965305cf83
- claim:21bdaa7b130a7cc4
- claim:32d4ab82e7394fa1
- claim:334565c7ebb30cb5
- claim:34aa536e34afa87c
- claim:87456c04d2f50e30
- claim:a7845ddab7913b4f
source_refs: &id001
- arxiv:2408.08435
- github:SakanaAI/AI-Scientist
- arxiv:2509.25651
- arxiv:1905.10985
page_refs:
- wiki-page:source-c9890d5668d1c1b3
- wiki-page:source-11d8f2a43bca42c2
- wiki-page:source-5b06dbb06d02d1f5
- wiki-page:source-089142f7297bed41
- wiki-page:llm-wiki-reference-system
- wiki-page:knowledge-frontier
outgoing_links:
- target: wiki-page:source-c9890d5668d1c1b3
  relation: explains
  claim_refs:
  - claim:0d2b54965305cf83
  - claim:00e6310ce97dc279
  notes: null
- target: wiki-page:source-11d8f2a43bca42c2
  relation: explains
  claim_refs:
  - claim:334565c7ebb30cb5
  - claim:21bdaa7b130a7cc4
  notes: null
- target: wiki-page:source-5b06dbb06d02d1f5
  relation: explains
  claim_refs:
  - claim:32d4ab82e7394fa1
  - claim:34aa536e34afa87c
  notes: null
- target: wiki-page:source-089142f7297bed41
  relation: explains
  claim_refs:
  - claim:a7845ddab7913b4f
  - claim:87456c04d2f50e30
  notes: null
- target: wiki-page:llm-wiki-reference-system
  relation: related
  claim_refs:
  - claim:00e6310ce97dc279
  - claim:0d2b54965305cf83
  - claim:21bdaa7b130a7cc4
  - claim:32d4ab82e7394fa1
  - claim:334565c7ebb30cb5
  - claim:34aa536e34afa87c
  notes: null
- target: wiki-page:knowledge-frontier
  relation: related
  claim_refs:
  - claim:00e6310ce97dc279
  - claim:0d2b54965305cf83
  - claim:21bdaa7b130a7cc4
  - claim:32d4ab82e7394fa1
  - claim:334565c7ebb30cb5
  - claim:34aa536e34afa87c
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:0d2b54965305cf83
  - claim:32d4ab82e7394fa1
  - claim:334565c7ebb30cb5
  - claim:a7845ddab7913b4f
  source_refs:
  - arxiv:2408.08435
  - arxiv:2509.25651
  - github:SakanaAI/AI-Scientist
  - arxiv:1905.10985
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:00e6310ce97dc279
  - claim:21bdaa7b130a7cc4
  - claim:34aa536e34afa87c
  - claim:87456c04d2f50e30
  source_refs:
  - arxiv:2408.08435
  - github:SakanaAI/AI-Scientist
  - arxiv:2509.25651
  - arxiv:1905.10985
  editorial_intent: Preserve collector scope.
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
  - arxiv:2408.08435@sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  - arxiv:2509.25651@sha256:14424738e0ad14b8fd5891102b89d9a3e4888beb22605f723e1cc044231eb803
  - arxiv:1905.10985@sha256:6afa7771c29f7a9a5659d73e62b83cfefb39516d30ae99172e2ad373dafd45e5
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
    one_line: Routing map for cross cutting sources, questions, and claims.
    short: Routing map for cross cutting sources, questions, and claims.
    full: null
  estimated_tokens: 902
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:00e6310ce97dc279
- claim:0d2b54965305cf83
- claim:21bdaa7b130a7cc4
- claim:32d4ab82e7394fa1
- claim:334565c7ebb30cb5
- claim:34aa536e34afa87c
- claim:87456c04d2f50e30
- claim:a7845ddab7913b4f
rights_refs:
- source_uid: arxiv:2408.08435
  source_revision: sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2
  source_version_url: https://arxiv.org/abs/2408.08435v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md
  package_path: materialized_sources/corpus/arxiv-2408.08435--dc6e6730/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:0d2b54965305cf83
rights_unavailable_source_refs:
- arxiv:1905.10985
- arxiv:2509.25651
- github:SakanaAI/AI-Scientist
---

# Cross Cutting

Infrastructure and evidence that spans several knowledge modules.

## Routing questions

- Which interfaces connect the modules?
- Which sources are true bridges rather than weakly classified?
- Where are shared dependencies fragile?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [Automated Design of Agentic Systems](../sources/arxiv-2408.08435.md) | `arxiv` | `full_text` | 2 |
| [SakanaAI/AI-Scientist](../sources/github-sakanaai-ai-scientist.md) | `github` | `semantic_capsule` | 2 |
| [AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation](../sources/arxiv-2509.25651.md) | `arxiv` | `full_text` | 2 |
| [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](../sources/arxiv-1905.10985.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **Automated Design of Agentic Systems** (source assertion): Researchers are investing substantial effort in developing powerful general-purpose agents, wherein Foundation Models are used as modules within agentic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). 〔[claim:0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md)〕
- **AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation** (source assertion): The automation of chemical research through self-driving laboratories (SDLs) promises to accelerate scientific discovery, yet the reliability and granular performance of the underlying AI agents remain critical, under-examined challenges. In this work, we introduce AutoLabs, a self-correcting, multi-agent architecture designed to autonomously translate natural-language instructions into executable protocols for a hig 〔[claim:32d4ab82e7394fa1](../claims/claim-32d4ab82e7394fa1.md)〕
- **SakanaAI/AI-Scientist** (source assertion): One of the grand challenges of artificial intelligence is developing agents capable of conducting scientific research and discovering new knowledge. 〔[claim:334565c7ebb30cb5](../claims/claim-334565c7ebb30cb5.md)〕
- **AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence** (source assertion): Perhaps the most ambitious scientific quest in human history is the creation of general artificial intelligence, which roughly means AI that is as smart or smarter than humans. The dominant approach in the machine learning community is to attempt to discover each of the pieces that might be required for intelligence, with the implicit assumption that at some point in the future some group will complete the Herculean  〔[claim:a7845ddab7913b4f](../claims/claim-a7845ddab7913b4f.md)〕

## Collector assessments

- **Automated Design of Agentic Systems** (collection assessment): Defines Automated Design of Agentic Systems (ADAS): agents are represented in code and a meta-agent iteratively programs better agents using an ever-growing archive of prior discoveries. 〔[claim:00e6310ce97dc279](../claims/claim-00e6310ce97dc279.md)〕
- **SakanaAI/AI-Scientist** (collection assessment): Canonical open implementation of an end-to-end automated research loop where research artifacts become inputs to subsequent iterations. 〔[claim:21bdaa7b130a7cc4](../claims/claim-21bdaa7b130a7cc4.md)〕
- **AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation** (collection assessment): A self-correcting multi-agent architecture that converts scientific instructions into executable experimental protocols and validates/corrects them before hardware execution. 〔[claim:34aa536e34afa87c](../claims/claim-34aa536e34afa87c.md)〕
- **AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence** (collection assessment): Explicitly proposes replacing manual AI engineering with systems that automatically generate increasingly capable AI, spanning architectures, learning algorithms, and environments. 〔[claim:87456c04d2f50e30](../claims/claim-87456c04d2f50e30.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [Automated Design of Agentic Systems](../sources/arxiv-2408.08435.md) — `explains`
- [SakanaAI/AI-Scientist](../sources/github-sakanaai-ai-scientist.md) — `explains`
- [AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation](../sources/arxiv-2509.25651.md) — `explains`
- [AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](../sources/arxiv-1905.10985.md) — `explains`
- [LLM Wiki reference system](../systems/reference-system.md) — `related`
- [Knowledge frontier](../research_questions/knowledge-frontier.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Automated Design of Agentic Systems (`arxiv:2408.08435`)

- Components: `claim:0d2b54965305cf83`
- Source revision: `sha256:9e5b2a49f62b2d5218e018666a195c85fc5d186d3939e0070303fab4fb7622e2`
- Source version: [pinned upstream version](https://arxiv.org/abs/2408.08435v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md](../../../../raw_data/licenses/adas-v2-cc-by-4.0-iclr2025-lppl-1.3c-natbib-8.31.md)
- Attribution: Shengran Hu, Cong Lu, Jeff Clune, Automated Design of Agentic Systems, arXiv:2408.08435v2 (2025-03-02), https://arxiv.org/abs/2408.08435v2, CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. ICLR, Template for ICLR 2025 Conference Submission, CC BY 4.0, https://www.overleaf.com/latex/templates/template-for-iclr-2025-conference-submission/gqzkdyycxtvt; ICLR STY retains Hugo Larochelle's NIPS-style adaptation credit and matches https://github.com/ICLR/Master-Template/blob/05833d63fe48bbf250b144741ea77691018bb328/iclr2025/iclr2025_conference.sty. Deep Learning notation retains goodfeli/dlbook_notation attribution and the original authors' free-use statement at https://github.com/goodfeli/dlbook_notation/blob/master/README.md. BST: Copyright 2010 Hal Daum\'e III, J. Fürnkranz label modifications, Copyright 1993-2007 Patrick W Daly; fancyhdr 3.2: Piet van Oostrum; natbib 8.31: Copyright 1993-2009 Patrick W Daly, original 2009/07/16 source. These components retain independent LPPL version 1 or later; packaging selects LPPL 1.3c: https://www.latex-project.org/lppl/lppl-1-3c.txt. 完整原始 natbib.dtx 随 NOTICE.md 及 raw_data/licenses/components/natbib-8.31/natbib.dtx 提供。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 9份原源文本及其版权、归属、历史修改说明不改；复用现有 TeX 合并与纯文本转换， normalized/document.tex 和33个定位器不改，在 normalized/document.txt 末尾追加唯一署名、 修改/范围说明及 NOTICE.md 链接。附注保存完整 CC BY 4.0、LPPL 1.3c 和未修改的原 natbib.dtx； 未新增或转换原已省略的5份PDF图像，不声称原作者/维护者支持本仓库修改。
- Scope: 仅实存9份 source 文本（304218 bytes）、normalized/document.tex（109460 bytes）、 附注前93591-byte normalized/document.txt 正文及33个定位器。论文作者材料及其转换按论文 CC BY 4.0； ICLR2025 STY按官方模板 CC BY 4.0，notation保留goodfeli/dlbook_notation原作者自由使用说明和来源； iclr2025_conference.bst、fancyhdr.sty、natbib.sty及随包原 natbib.dtx独立按LPPL条件，选用1.3c。 两份书目文件仅保留引用字段/排版记录，不外推被引用作品全文；不包括原已省略5份PDF图像、 整个归档、外链代码/数据、外部依赖或其他作品。

### AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence (`arxiv:1905.10985`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation (`arxiv:2509.25651`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### SakanaAI/AI-Scientist (`github:SakanaAI/AI-Scientist`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
