---
uid: wiki-page:source-51388aa8e2e8587f
title: Enabling Large Language Models to Generate Text with Citations
slug: sources/arxiv-2305.14627
page_type: source
status: review
summary: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence expansion.
aliases: []
ontology_refs:
- experiment:meta-kb-v0
claim_refs: &id001
- claim:9a3b21da11a96956
- claim:bed2f056ecd73c69
source_refs: &id002
- arxiv:2305.14627
page_refs:
- wiki-page:map-llm-wiki
- wiki-page:evidence-acf3f9a285c1d147
- wiki-page:evidence-12cbeb94dfbfbe21
outgoing_links:
- target: wiki-page:map-llm-wiki
  relation: part_of
  claim_refs: *id001
  notes: null
- target: wiki-page:evidence-acf3f9a285c1d147
  relation: evidenced_by
  claim_refs:
  - claim:9a3b21da11a96956
  notes: null
- target: wiki-page:evidence-12cbeb94dfbfbe21
  relation: evidenced_by
  claim_refs:
  - claim:bed2f056ecd73c69
  notes: null
sections:
- heading: Source-reported candidate statements
  claim_refs:
  - claim:bed2f056ecd73c69
  source_refs:
  - arxiv:2305.14627
  editorial_intent: Represent source statements.
- heading: Collection assessments
  claim_refs:
  - claim:9a3b21da11a96956
  source_refs:
  - arxiv:2305.14627
  editorial_intent: Keep collector interpretation separate.
temporal:
  created_at: '2026-09-16T04:30:26Z'
  updated_at: '2026-09-16T04:30:26Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-16T04:30:26Z'
provenance:
  build_id: build:llm-wiki-v0:0175f4c78a0341b7
  generated_by_agent: pipeline/build_llm_wiki.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-llm-wiki-v0.2
  compiled_from_revisions:
  - arxiv:2305.14627@sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
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
    one_line: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence
      expansion.
    short: Source page for Enabling Large Language Models to Generate Text with Citations with claim/evidence expansion.
    full: null
  estimated_tokens: 509
  machine_entry_points:
  - ../../04_claims/claims.jsonl
  - ../../03_evidence/evidence.jsonl
  - ../catalog/pages.jsonl
rendered_claim_refs:
- claim:9a3b21da11a96956
- claim:bed2f056ecd73c69
rights_refs:
- source_uid: arxiv:2305.14627
  source_revision: sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1
  source_version_url: https://aclanthology.org/2023.emnlp-main.398.pdf
  license_spdx: CC-BY-4.0
  license_url: https://creativecommons.org/licenses/by/4.0/
  notice_path: materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md
  package_path: materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/manifest.yaml#pdf_supplement.rights.redistribution_package
  usage: rendered_source_claims
  transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page.
  claim_refs:
  - claim:bed2f056ecd73c69
rights_unavailable_source_refs: []
---

# Enabling Large Language Models to Generate Text with Citations

> Source-oriented candidate page. Source statements and collector interpretation remain separate.

## Source identity

- Source UID: `arxiv:2305.14627`
- Canonical ID: `2305.14627`
- Source type: `arxiv`
- Content tier: `full_text`
- Revision: `sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1`
- Domain: [llm-wiki](../maps/llm-wiki.md)
- Local document: `materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/document.txt`

## Source-reported candidate statements

- Large language models (LLMs) have emerged as a widely-used tool for information seeking, but their generated outputs are prone to halluci- nation. In this work, our aim is to allow LLMs to generate text with citations, improving their factual correctness and verifiability. 〔[claim:bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md)〕

## Collection assessments

- ALCE provides reproducible citation-quality metrics across correctness, completeness, and fluency, directly applicable to wiki admission gates. 〔[claim:9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md)〕

## Evidence inventory

| Claim | Evidence | Selector | Tier |
|---|---|---|---|
| `claim:9a3b21da11a96956` | `evidence:cff53a88da30fbec` | `local://raw_data/arxiv/Enabling Large Language Models to Generate Text with Citations/metadata.yaml#collection.inclusion_reason` | `metadata_capsule` |
| `claim:bed2f056ecd73c69` | `evidence:4527dd12000fe21f` | `local://materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/document.txt#L11-L16` | `full_text` |

## Governance boundary

Source statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence.

## Related pages

- [Llm Wiki](../maps/llm-wiki.md) — `part_of`
- [Claim 9a3b21da11a96956](../claims/claim-9a3b21da11a96956.md) — `evidenced_by`
- [Claim bed2f056ecd73c69](../claims/claim-bed2f056ecd73c69.md) — `evidenced_by`

## Source text rights and attribution

The terms below apply only to the listed source-authored claim components. They do not relicense collector assessments, compiler synthesis, other source components, or this repository as a whole.

### Enabling Large Language Models to Generate Text with Citations (`arxiv:2305.14627`)

- Components: `claim:bed2f056ecd73c69`
- Source revision: `sha256:ae9868f07f0f7ffaae5346778f79b7827d9ec6b13b1e6aae4dff6b2ffc37a2e1`
- Source version: [pinned upstream version](https://aclanthology.org/2023.emnlp-main.398.pdf)
- License: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- NOTICE: [materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md](../../../../materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/pdf-supplement/NOTICE.md)
- Attribution: Tianyu Gao; Howard Yen; Jiatong Yu; Danqi Chen, Enabling Large Language Models to Generate Text with Citations. Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp.6465–6488, December 6–10, 2023; ©2023 Association for Computational Linguistics。实际四作者顺序、Department of Computer Science & Princeton Language and Intelligence, Princeton University、{tianyug,hyen,jiatongy,danqic}@cs.princeton.edu归属保留。Anthology ID 2023.emnlp-main.398；DOI 10.18653/v1/2023.emnlp-main.398为本批已核正式映射，不称PDF正文印出DOI；作品 https://aclanthology.org/2023.emnlp-main.398/，原PDF https://aclanthology.org/2023.emnlp-main.398.pdf，CC BY4 https://creativecommons.org/licenses/by/4.0/。同一canonical UID arxiv:2305.14627/source_type arxiv不变，不伪造arXiv vN。p10独立致谢Princeton NLP group；Alexander Wettig、Nelson Liu、Tianyi Zhang、Yu Meng、Sadhika Malladi、Yangsibo Huang、Zhiyuan Zeng、Dan Friedman；Surge AI/Anna Folinsky/Edwin Chen的人工评估；Tianyu Gao IBM PhD Fellowship、NSF CAREER IIS-2239290、Sloan Research Fellowship、Microsoft Azure经Accelerate Foundation Models Academic Research Initiative提供credits，独立保留而不混为作者/权利转让或背书。p1 https://github.com/princeton-nlp/ALCE链接与ASQA/QAMPARI/ELI5/Wikipedia/Sphere/Common Crawl及References保留被引对象身份，不下载或再许可其独立代码/数据/被引全文/权重。p23–24 Tables30/31内十段实际有限外部检索文字均为100个空白分隔单元，计数不是token/全文长度/独立作品许可。p23实际标题How to Treat and Prevent Food Poisoning - MsPrepper；FDA Issues Warning About Eating Raw Cookie Dough, But Not For Salmonella Risks；It’s Probably OK to Eat Raw Cookie Dough — As Long As You’re Smart About It - The Crux - Very Top Secret Information；两段How Dangerous Is It to Eat Raw Cookie Dough? | Men’s Health，第四段By Katherine Dempsey，末段说明How Bad Is It To Eat Raw Cookie Dough? originally appeared on Prevention.com。p24实际标题Is Snapchat really worth $19 billion? - CSMonitor.com；What Are Venture Capital Investments? – DollarsAndSense.my；Opinion | What Dara Khosrowshahi Must Do to Save Uber - The New York Times；Snapchat raising funding round at $19 billion valuation: Report；Unicorns And Wall Street | MoneyTips。有限片段/题名/署名/来源提示按原论文学术例示保留，不称四作者原创新闻或ACL拥有外部全文全部权利；PDF未提供全部外部URL，不编造/递归取得原网页，不单独许可新闻整篇，不暗示作者/ACL/机构/资助者背书。
- Excerpt/page transformation: The listed source-authored claim excerpts are rendered inside a mixed, compiler-generated page. 唯一正式GET的481920 bytes/24页原PDF原样保留，不编辑、重导、重排、OCR或修补源作品。现build_pdf_supplement以pypdf plain全页生成独立pdf-supplement/document.txt及新PDF revision绑定的逐页selectors；## Page N边界、定位和唯一归属/修改/范围footer是collector添加的派生表示元数据，不称作者原始文本或无损布局/公式/代码。NOTICE自包含实际四作者/©ACL/会议身份/独立信用/有限外部例示/范围/限制及现存完整CC BY4法条，notice_path自绑定本文件；不新rawlicense。primary_excerpt仅声明native Page1父摘要连续L11–39，不改PDF/native原样层或生产consumer逻辑。旧source/normalized/root selectors/NOTICE/README/files及root revision/retrieval/rights/materialization/generated_at/status/content_tier/source_version键缺省保持，C source_version仍null；正式版不补入旧v2 Open-source Models三段/Stable Beluga2三行，不以新grant整体放行旧包。
- Scope: 本独立新表示仅覆盖固定publisher-vor:doi:10.18653/v1/2023.emnlp-main.398的未改481920 bytes/24页正式EMNLP2023 PDF及同目录有损native plain、revision-bound页selectors和自包含NOTICE；正式DOI 10.18653/v1/2023.emnlp-main.398 / Anthology 2023.emnlp-main.398完整24物理页（印刷页6465–6488）compiled PDF：p1–9主文至Conclusion/四图，p10 Limitations/Acknowledgments及p10–13完整References，p14–17正式A–I附录叙述，p18–20主结果Tables19–21，p21–22 Tables22–29完整prompts，p23–24 Tables30–31两个ELI5 Examples。真尾p24 Table31第三ground-truth claim、表底线/ELI5 example2图注/页码正常结束，不在References/H标题截断。 论文作者/ACL有权许可表达沿已有正式作品BY4路径，原论文已发表的有限图表例示与十段外部passage/题名/署名/来源信用按原件保存，不推导standalone新闻整篇/引用作品/底层素材/代码仓库/数据/权重/模型/商标/专利的一般许可，不另取外链或执行prompt/benchmark，无普遍权利保证，不为已许可权利添加下游限制。新grant不覆盖旧source归档/LaTeX模板/BST/两摘要或旧未对应扩展/normalized/root selectors/历史gate；旧block及对应evidence false保留，C source_version null与root键缺省保留。
