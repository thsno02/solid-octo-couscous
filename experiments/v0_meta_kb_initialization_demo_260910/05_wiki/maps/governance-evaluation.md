---
uid: wiki-page:map-governance-evaluation
title: Governance Evaluation
slug: maps/governance-evaluation
page_type: map
status: review
summary: Routing map for governance evaluation sources, questions, and claims.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:17c715b34b0f0c68
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
- claim:84c91602bd1dfb78
- claim:bde139a533f9483a
- claim:ecdd2719fa55751c
source_refs: &id001
- arxiv:2602.06855
- arxiv:2502.14499
- arxiv:2406.06769
page_refs:
- wiki-page:source-a264f295a5ce5604
- wiki-page:source-3dda2384308efbda
- wiki-page:source-18c791741aa4bcd7
- wiki-page:v0-quality-gates
- wiki-page:automation-vs-editorial-review
outgoing_links:
- target: wiki-page:source-a264f295a5ce5604
  relation: explains
  claim_refs:
  - claim:ecdd2719fa55751c
  - claim:17c715b34b0f0c68
  notes: null
- target: wiki-page:source-3dda2384308efbda
  relation: explains
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  notes: null
- target: wiki-page:source-18c791741aa4bcd7
  relation: explains
  claim_refs:
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  notes: null
- target: wiki-page:v0-quality-gates
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  - claim:ecdd2719fa55751c
  notes: null
- target: wiki-page:automation-vs-editorial-review
  relation: related
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4bf5ea8e6b4e37de
  - claim:4fd96c70e0c625fd
  - claim:84c91602bd1dfb78
  - claim:bde139a533f9483a
  - claim:ecdd2719fa55751c
  notes: null
sections:
- heading: Source coverage
  claim_refs: []
  source_refs: *id001
  editorial_intent: Route by source family.
- heading: Source-reported signals
  claim_refs:
  - claim:4bf5ea8e6b4e37de
  - claim:84c91602bd1dfb78
  - claim:ecdd2719fa55751c
  source_refs:
  - arxiv:2502.14499
  - arxiv:2406.06769
  - arxiv:2602.06855
  editorial_intent: Preserve source-authored scope.
- heading: Collector assessments
  claim_refs:
  - claim:17c715b34b0f0c68
  - claim:4fd96c70e0c625fd
  - claim:bde139a533f9483a
  source_refs:
  - arxiv:2602.06855
  - arxiv:2502.14499
  - arxiv:2406.06769
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
  - arxiv:2602.06855@sha256:ac1ba940f1bdc54e012cc384c428f78bd01d50d7a947f052117944c03e790d9a
  - arxiv:2502.14499@sha256:de8bc15be762914dd2f056f00efe2b83d51ce852a7035d65e866e6cdecbbb65a
  - arxiv:2406.06769@sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
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
    one_line: Routing map for governance evaluation sources, questions, and claims.
    short: Routing map for governance evaluation sources, questions, and claims.
    full: null
  estimated_tokens: 1071
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:17c715b34b0f0c68
- claim:4bf5ea8e6b4e37de
- claim:4fd96c70e0c625fd
- claim:84c91602bd1dfb78
- claim:bde139a533f9483a
- claim:ecdd2719fa55751c
rights_refs:
- source_uid: arxiv:2406.06769
  source_revision: sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e
  source_version_url: https://arxiv.org/abs/2406.06769v2
  license_spdx: CC-BY-SA-4.0
  license_url: https://creativecommons.org/licenses/by-sa/4.0/
  notice_path: raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml#rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:84c91602bd1dfb78
rights_unavailable_source_refs:
- arxiv:2502.14499
- arxiv:2602.06855
---

# Governance Evaluation

Admission, factuality, review, rollback, and policy controls.

## Routing questions

- What evidence is sufficient for admission?
- How are citation and factual precision measured?
- Which changes require independent review?

## Source coverage

| Source | Type | Tier | Claims |
|---|---|---|---|
| [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) | `arxiv` | `full_text` | 2 |
| [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) | `arxiv` | `full_text` | 2 |
| [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) | `arxiv` | `full_text` | 2 |

## Source-reported signals

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (source assertion): We introduce Meta and -Bench, a new framework and benchmark for evaluating and developing LLM agents on AI research tasks. This is the first Gym environment for machine learning (ML) tasks, enabling research on reinforcement learning (RL) algorithms for training such agents. 〔[claim:4bf5ea8e6b4e37de](../claims/claim-4bf5ea8e6b4e37de.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (source assertion): Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. 〔[claim:84c91602bd1dfb78](../claims/claim-84c91602bd1dfb78.md)〕
- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (source assertion): LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce ~(the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. 〔[claim:ecdd2719fa55751c](../claims/claim-ecdd2719fa55751c.md)〕

## Collector assessments

- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** (collection assessment): A 2026 benchmark explicitly targeting frontier AI research-science agents across the research lifecycle, including idea generation, experimentation, analysis and iterative refinement. 〔[claim:17c715b34b0f0c68](../claims/claim-17c715b34b0f0c68.md)〕
- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** (collection assessment): A Gym-style environment and benchmark for training/evaluating agents on open-ended ML research tasks requiring ideation, implementation, experimentation, analysis and iterative improvement. 〔[claim:4fd96c70e0c625fd](../claims/claim-4fd96c70e0c625fd.md)〕
- **DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents** (collection assessment): A benchmark environment for complete novel scientific discovery cycles where agents must form hypotheses, run experiments, analyze results and discover explanatory knowledge. 〔[claim:bde139a533f9483a](../claims/claim-bde139a533f9483a.md)〕

## Current synthesis boundary

The map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically.

## Related pages

- [AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents](../sources/arxiv-2602.06855.md) — `explains`
- [MLGym: A New Framework and Benchmark for Advancing AI Research Agents](../sources/arxiv-2502.14499.md) — `explains`
- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `explains`
- [v0 LLM Wiki quality gates](../evaluations/v0-quality-gates.md) — `related`
- [Automation versus editorial review](../debates/automation-editorial-review.md) — `related`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents (`arxiv:2406.06769`)

- Components: `claim:84c91602bd1dfb78`
- Source revision: `sha256:cb1d6ccc88eb66af69e71730a5c488234ff4fe8af04ba04081b5a445f4d39b3e`
- Source version: [pinned upstream version](https://arxiv.org/abs/2406.06769v2)
- License: [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- NOTICE: [raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md](../../../../raw_data/licenses/discoveryworld-v2-cc-by-sa-4.0-neurips-corresponding-expression-cc-by-4.0.md)
- Attribution: "DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents", arXiv:2406.06769v2, by Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra, Bodhisattwa Prasad Majumder, Oyvind Tafjord and Peter Clark, https://arxiv.org/abs/2406.06769v2, licensed under CC BY-SA 4.0: https://creativecommons.org/licenses/by-sa/4.0/. source/neurips_data_2024.sty is an independent NeurIPS Data 2024 template component with its original Lora Aroyo credit and attribution to Roman Garnett and the many authors of nips15submit_e.sty, including MK and drstrip@sandia, retained. Its corresponding licensed original template expression is identified in the NeurIPS 2026 Program Chairs' official "Formatting Instructions For NeurIPS 2026", https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc, explicitly declared CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. The corresponding official current source is https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip, checked on 2026-09-16. The retained 2024 Data variant is packaged using this corresponding-expression/adaptation path, not a claim that the historical 2024 ZIP declared an overall CC BY 4.0 license. The retained member is also identified by the official 2024 Data bundle, https://media.neurips.cc/Conferences/NeurIPS2024/NeurIPS-Dataset-Styles.zip, linked from https://neurips.cc/Conferences/2024/CallForDatasetsBenchmarks. None of these attributions implies endorsement of this repository.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. All nine text source members of the fixed v2 archive are retained unchanged, including related_work-v1-old.tex. The existing normalized/document.tex and all 74 selectors are preserved byte-for-byte. The original 94,506-byte normalized/document.txt is preserved as an exact prefix; only the complete attribution, changes, scope and NOTICE link are appended to its end. Compared with the currently reviewed official NeurIPS 2026 style, the retained Data 2024 style has the Lora Aroyo header, its 2024/04/30 package identifier, the anonymous default/option and @submission boolean mapping, and the @submission test in the title block; its meeting identifiers are 38th/2024 and its existing location string is "Vancouver, USA". It retains "Preprint. Under review." and the Datasets and Benchmarks track footer. The lineno/amsmath compatibility block appears earlier in the retained style rather than at the current style's end; its closing-brace layout differs. The retained style uses the 2024 package warning identifier and a space between each checklist answer label and its argument. It lacks the current multi-track, position/eandd/creativeai/education/workshop/nonanonymous options, minimum font-size overrides, acknowledgement-hiding block and justificationTODO command. Long formatting and compatibility expressions correspond to the currently licensed original; version labels, short footer text and routine functional adaptations are separately disclosed. These differences are pre-existing and are not introduced, repaired or attributed to a newly asserted modifier by this repository. No historical template download identity, historical 2024 BY4 declaration or byte-identical correspondence to the complete current style is claimed.
- Scope: 本包仅覆盖固定 arXiv 2406.06769v2 的九个 source 文字成员、normalized/document.tex、normalized/document.txt 与 74 个定位器（selectors）。作者/提交者有权许可的论文源表达及其文本转换，包括保留的旧稿，按 CC BY-SA 4.0 共享；改编材料继续按该许可同方式共享。source/neurips_data_2024.sty 是独立第三方模板，按当前官方模板的对应授权表达及 CC BY 4.0 复制/改编路径分别署名，保留其既存短常规功能适配，不将历史 2024 ZIP 宣称为整体 BY4，也不将模板著作权归论文作者。两许可按组件分别适用，不将整仓库重新许可为 BY-SA4 或 BY4；定位器不改变所定位组件的许可。DiscoveryWorld.bbl 是书目记录，不授权所引作品；未保存的五个非文本媒体、外链代码/模型/数据、商标及专利不在本许可包范围。没有删除任何已保存源文字以回避许可条件，不施加额外限制或暗示上游支持。

### MLGym: A New Framework and Benchmark for Advancing AI Research Agents (`arxiv:2502.14499`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.

### AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents (`arxiv:2602.06855`)

- Rights status: No complete redistribution package is recorded for this source. No license or permission is inferred by this compiler.
- Excerpt note: The page identifies the component as a source-reported candidate and preserves its pinned source reference; downstream reuse must resolve rights separately.
