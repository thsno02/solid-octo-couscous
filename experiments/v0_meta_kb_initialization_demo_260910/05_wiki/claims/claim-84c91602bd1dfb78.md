---
uid: wiki-page:evidence-7251138bb2057919
title: Claim 84c91602bd1dfb78
slug: claims/claim-84c91602bd1dfb78
page_type: evidence
status: review
summary: Automated scientific discovery promises to accelerate progress across scientific domains. However, developing
  and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:84c91602bd1dfb78
source_refs: &id001
- arxiv:2406.06769
page_refs:
- wiki-page:source-18c791741aa4bcd7
- wiki-page:map-governance-evaluation
outgoing_links:
- target: wiki-page:source-18c791741aa4bcd7
  relation: evidenced_by
  claim_refs:
  - claim:84c91602bd1dfb78
  notes: null
- target: wiki-page:map-governance-evaluation
  relation: part_of
  claim_refs:
  - claim:84c91602bd1dfb78
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:84c91602bd1dfb78
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:84c91602bd1dfb78
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:ac56ea43f6b5393c
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
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
    one_line: Automated scientific discovery promises to accelerate progress across scientific domains. However,
      developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running
      real-world
    short: Automated scientific discovery promises to accelerate progress across scientific domains. However, developing
      and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world
    full: null
  estimated_tokens: 646
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:84c91602bd1dfb78
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
rights_unavailable_source_refs: []
---

# Source assertion from DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent's capacity for end-to-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible.

## Scope

- Claim ID: `claim:84c91602bd1dfb78`
- Scope: `source-reported assertion`
- Domain: [governance-evaluation](../maps/governance-evaluation.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:69559f8937311f42` | `local://materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt#L89-L90` | `materialized_sources/corpus/arxiv-2406.06769--d1971e3b/normalized/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](../sources/arxiv-2406.06769.md) — `evidenced_by`
- [Governance Evaluation](../maps/governance-evaluation.md) — `part_of`

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
