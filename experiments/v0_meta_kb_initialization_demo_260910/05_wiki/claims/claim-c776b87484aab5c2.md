---
uid: wiki-page:evidence-1d4cfb868e3ee45c
title: Claim c776b87484aab5c2
slug: claims/claim-c776b87484aab5c2
page_type: evidence
status: review
summary: Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain
  fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or
  dynami
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs:
- claim:c776b87484aab5c2
source_refs: &id001
- arxiv:2507.21046
page_refs:
- wiki-page:source-68be106d4fc61e3b
- wiki-page:map-open-ended-evolution
outgoing_links:
- target: wiki-page:source-68be106d4fc61e3b
  relation: evidenced_by
  claim_refs:
  - claim:c776b87484aab5c2
  notes: null
- target: wiki-page:map-open-ended-evolution
  relation: part_of
  claim_refs:
  - claim:c776b87484aab5c2
  notes: null
sections:
- heading: Candidate statement
  claim_refs:
  - claim:c776b87484aab5c2
  source_refs: *id001
  editorial_intent: Expose the exact candidate statement.
- heading: Evidence bindings
  claim_refs:
  - claim:c776b87484aab5c2
  source_refs: *id001
  editorial_intent: Resolve to local selectors.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:052e92babb00da4b
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2507.21046@sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602
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
    one_line: Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain
      fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains,
      or dynami
    short: Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain
      fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains,
      or dynami
    full: null
  estimated_tokens: 464
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:c776b87484aab5c2
rights_refs:
- source_uid: arxiv:2507.21046
  source_revision: sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602
  source_version_url: https://arxiv.org/pdf/2507.21046v4
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: raw_data/licenses/cc-by-4.0.md
  package_path: materialized_sources/corpus/arxiv-2507.21046--f477f5c3/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:c776b87484aab5c2
rights_unavailable_source_refs: []
---

# Source assertion from A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence

> **Candidate only.** This page exposes one atomic claim and its evidence bindings.

## Candidate statement

Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse tasks but remain fundamentally static, unable to adapt their internal parameters to novel tasks, evolving knowledge domains, or dynamic interaction contexts. As LLMs are increas- ingly deployed in open-ended, interactive environments, this static nature has become a critical bottleneck, necessitating agents that can adaptively reason, act, and evolve in real time.

## Scope

- Claim ID: `claim:c776b87484aab5c2`
- Scope: `source-reported assertion`
- Domain: [open-ended-evolution](../maps/open-ended-evolution.md)
- Promotion state: `candidate`

## Evidence bindings

| Evidence | Selector | Local artifact | Tier |
|---|---|---|---|
| `evidence:ed04910f7e6cc17e` | `local://materialized_sources/corpus/arxiv-2507.21046--f477f5c3/pdf-supplement/document.txt#L20-L25` | `materialized_sources/corpus/arxiv-2507.21046--f477f5c3/pdf-supplement/document.txt` | `full_text` |

## Review requirements

Check entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion.

## Related pages

- [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](../sources/arxiv-2507.21046.md) — `evidenced_by`
- [Open Ended Evolution](../maps/open-ended-evolution.md) — `part_of`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence (`arxiv:2507.21046`)

- Components: `claim:c776b87484aab5c2`
- Source revision: `sha256:0b39df03feea2f4d8ac41e35a9247889978a53cb1e7b7d3eafaae76ad97b5602`
- Source version: [pinned upstream version](https://arxiv.org/pdf/2507.21046v4)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [raw_data/licenses/cc-by-4.0.md](../../../../raw_data/licenses/cc-by-4.0.md)
- Attribution: Huan-ang Gao; Jiayi Geng; Wenyue Hua; Mengkang Hu; Xinzhe Juan; Hongzhang Liu; Shilong Liu; Jiahao Qiu; Xuan Qi; Yiran Wu; Hongru Wang; Han Xiao; Yuhang Zhou; Shaokun Zhang; Jiayi Zhang; Jinyu Xiang; Yixiong Fang; Qiwen Zhao; Dongrui Liu; Qihan Ren; Cheng Qian; Zhenhailong Wang; Minda Hu; Huazheng Wang; Qingyun Wu; Heng Ji; Mengdi Wang. "A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence". Fixed arXiv 2507.21046v4, https://arxiv.org/abs/2507.21046v4; original PDF https://arxiv.org/pdf/2507.21046v4. Article expression the authors/submitter may license is available under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/; full legal code https://creativecommons.org/licenses/by/4.0/legalcode.en. Fixed article/PDF license checked in this batch on 2026-09-16. Original figure, citation, author and funding credits inside the PDF are retained; no endorsement or right to external works, model logos or trademarks is implied.
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 原官方 PDF 按实际下载 bytes 原样保存，不编辑或重导出；复用既有 pypdf plain 提取逐页文字，加入明确页边界并生成独立页定位；在派生 text 末尾附唯一署名、修改、范围声明及完整 NOTICE.md 链接。plain 文字保留原抽取结果，不做 OCR、不运行 TeX、论文代码或提示词，不将图形、数学排版或阅读顺序损失隐藏为完整。旧 source、normalized、default selectors、NOTICE、files、archive revision/retrieval 和旧许可包全部保留，不新增 trusted。
- Scope: 仅本次从 https://arxiv.org/pdf/2507.21046v4 取得的固定 v4 官方完整 PDF（77 页，5726709 bytes）、其 plain 页文字与页级定位器。范围为编译后九章、12 个表、真实科学图与 inline taxonomy、以及 p53–77 参考文献；作品无 appendix。 作者/提交者有权许可的论文表达及本次文字派生沿作品级 CC BY 4.0；完整 PDF 原有图注、引用、署名、资助与警告保留，不授权被引用作品全文、外部实验数据集、模型、代码或脚本，也不转授 logo/商标、专利或权利人无权许可的材料。原 PDF 保留下载原字节，文字层有损且不做 OCR，原件完整不等于 text extraction complete。既有 TeX/source/normalized/default selectors/NOTICE/files 与旧包各组件授权范围不变。
