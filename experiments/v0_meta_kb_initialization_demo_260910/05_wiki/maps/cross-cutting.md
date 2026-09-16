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
  build_id: build:llm-wiki-v0:6b16cc1e2adf538b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2408.08435@sha256:32eb1c1a6888e35fae0f618e33c58698b54d9c49bc063fef91ee591719fca376
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
  estimated_tokens: 857
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
  source_revision: sha256:32eb1c1a6888e35fae0f618e33c58698b54d9c49bc063fef91ee591719fca376
  source_version_url: https://arxiv.org/pdf/2408.08435v2
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2408.08435--dc6e6730/manifest.yaml#pdf_supplement.rights.redistribution_package
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

- **Automated Design of Agentic Systems** (source assertion): Researchers are investing substantial effort in developing powerful general- purpose agents, wherein Foundation Models are used as modules within agen- tic systems (e.g. Chain-of-Thought, Self-Reflection, Toolformer). 〔[claim:0d2b54965305cf83](../claims/claim-0d2b54965305cf83.md)〕
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
- Source revision: `sha256:32eb1c1a6888e35fae0f618e33c58698b54d9c49bc063fef91ee591719fca376`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2408.08435v2)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Shengran Hu, Cong Lu, Jeff Clune. Automated Design of Agentic Systems. Fixed arXiv 2408.08435v2, https://arxiv.org/abs/2408.08435v2; original PDF https://arxiv.org/pdf/2408.08435v2. CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Title, complete author list, fixed version and article license link checked on the official version page on 2026-09-16. Original credits, notices and AI-generated-paper warnings inside the PDF are retained, not converted into repository endorsements.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按下载 bytes 原样保存；使用 pypdf 6.18.1 提取逐页文字，加入明确页边界并生成本地页定位；在派生 text 末尾附唯一署名、修改与范围声明及 NOTICE.md 链接。不编辑原 PDF、不执行其中代码或提示词，不把原生文本当 OCR。既有 source、normalized、selectors、archive revision 和旧归属包均保留。本层是有损预处理，不自动晋升 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2408.08435v2 取得的固定版本官方 PDF（34页，801981 bytes）、其页级提取文本与定位器。覆盖论文编译后主文、参考文献和 PDF 实际内嵌附录/图表，不包含外链论文、数据集、模型、代码仓库或新增源模板。作者/提交者可许可的作品表达沿官方固定版本 CC BY 4.0；保留 PDF 内独立署名、图注和警告，不暗示原作者支持本仓库。旧 TeX 包及其独立组件许可原样保留，本附加包不改其授权范围。原 PDF 完整保存不等于原生文本无损，图内文字、数学、图形与阅读顺序损失另列 coverage。

### AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence (`arxiv:1905.10985`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation (`arxiv:2509.25651`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### SakanaAI/AI-Scientist (`github:SakanaAI/AI-Scientist`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
