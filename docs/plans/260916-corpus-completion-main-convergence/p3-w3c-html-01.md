---
phase: P3-W3C-HTML-01
base_sha: 879596f10f34344337b1be2f05a6ffa347fd9a86
branch: codex/p3-w3c-html-01-260917
status: implementation_complete_pending_final_review_and_ci
pull_request: 17
adapter_family: generic_web_or_document_v2
action_bucket: parser_only
source_acquisition: seven_html_48_figures_one_css_acquired_45_figures_admitted_three_maps_excluded
independent_evaluation: final_exact_pair_review_pending
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts:
    excerpt_capsule: 26
    full_text: 93
    metadata_capsule: 12
  source_type_counts:
    arxiv: 73
    biorxiv: 2
    blog: 10
    industry: 2
    journal: 11
    methodology: 7
    paper: 2
    standard: 24
  original_artifact_counts:
    complete: 29
    metadata_only: 14
    partial: 9
    unknown: 79
  text_extraction_counts:
    complete: 6
    partial: 43
    unavailable: 14
    unknown: 68
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 6
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 69
    ocr_assessment: 17
    parser_only: 4
    public_persistence_decision: 3
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 43
  structure_only_full_text: 50
  locally_persisted_complete: 6
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 125
---

# P3-W3C-HTML-01 — 七份固定 W3C 规范的保全、正文提取与验收记录

## 当前结果（current result）

七份固定规范已完成本批实现与实物内容复核，等待最终提交的独立审核及 CI。下文启动合同与分阶段修订是历史记录，其“尚未获取／未实现”描述不代表当前状态。没有以本报告自评代替最终三维 PASS，没有将 PR #17 或父 PR #1 提前记为已合并。

本批取得 7 HTML、48 正文图、1 CSS，共 56 次列定来源 GET；准入并保留 53 件原件（7 HTML、45 图、1 CSS），共 7,210,546 bytes。三张 DCAT 地图虽然成功取得，但底图许可仍 unknown，未写入公开 repo。七个旧根正文／selector 文件、完整旧 NOTICE 和旧 manifest 历史事实继续保留。固定分母仍为 215 个来源，其中 131 个非 repo、84 个 GitHub repo；不新增 UID。

| 规范（固定版本见合同） | 原件完整性 | 结构文本完整性 | 正文质量已核 | 严格 complete_target | 新 consumer selectors | inventory 文件／bytes |
| --- | --- | --- | --- | --- | --- | --- |
| DCAT 3 | partial | partial | true | false | 180 | 12／1,901,730 |
| DID Core | complete | partial | true | false | 121 | 20／2,840,309 |
| JSON-LD 1.1 | complete | complete | true | true | 132 | 9／2,761,230 |
| ODRL 2.2 | complete | complete | true | true | 56 | 12／1,389,091 |
| OWL Time | complete | partial | true | false | 134 | 13／751,364 |
| RDF 1.2 Concepts | complete | complete | true | true | 64 | 13／1,355,047 |
| VC Data Model 2.0 | complete | partial | true | false | 163 | 23／2,970,462 |

基线七项的原件／文本 `state` 均为 `unknown`，对应 `verification_state` 均为 `partial_check`。新原件保全与正文验证已有上述可核结果；不将四项 partial 包装为 complete。表中严格 `complete_target` 是 coverage 字段 `local_persistence.complete_target_consumable` 的简写。新 sidecar 合计 850 条，旧根 7,712 条保持，总声明 8,562 条；七份 inventory 共 102 件／13,969,233 bytes，不含 manifest 本身。持久化在 repo 的是实物原件与正文，不依赖临时审阅目录或本机缓存；新 checkout 可沿 manifest 的显式 consumer 与 sidecar 消费。

三位非包装作者分别复核 DCAT/ODRL/OWL、JSON-LD/RDF、DID/VC 的全部主章及附录边界，并对原先空定义、表格、代码、引用、图和真实摘句定点核验。可用正文（usable body）、完整提取（complete extraction）、公开准入（publication admission）及知识晋级（knowledge promotion）是四个不同判断；七 UID 没有新增 claim、candidate 或 trusted 判定。

具体剩余边界：DCAT 三张地图缺公开许可且 Fig7 部分图内词未进入线性文本；DID B.1 的 path/query/fragment、alsoKnownAs 与详细回路，OWL Fig5 的地质节点及拓扑，VC 附录 D 第二凭证标签／值尚未全文字化，但后三者的完整图件已保留。后续只有消费者确实需要这些图义时才开展相应图文本处理，不把全图 OCR 当成本批新增门槛。JSON-LD、VC 的原作 alt／图值不一致原样保留；RDF 两个辅助 source-line anchor 重复不影响真实 selector URI／行范围及原生 ID。VC 默认自动摘句落在发布状态段，虽无锚点污染但不等于实质模型摘要，不用于新增知识。

最终代码冻结后主线全套测试 174 项通过，demo／Wiki 构建和验证通过。build ID 为 `build:llm-wiki-v0:97b320a509c00481`；36 个 selected sources、72 条 claims、72 条 evidence 与 BASE 字节一致，生成 diff 仅为必要的全局 build identity 传播。最终离线重放、coverage 与远程 CI 的结果继续记在本报告后部；尚未完成的门控不得由这里的局部成功替代。

这是启动计划（startup plan），不是获取、实现或验收结果。PR #16 已正常合入 work：merge `879596f10f34344337b1be2f05a6ffa347fd9a86`；独立三维 PASS 对应 HEAD `380db0c8a712526d6545882ee5b0ecc18e80df1e` / BASE `8d954a2f969475bb606229d5eae57427f47030a9`、review `5228329208`，CI `35149634883` success。本批唯一短期分支基于该最新 work；新 PR 尚未创建，PR #1 仍为 Draft，最终目的地为经 P4/P5 验收的 main。

已按 `06-codex-execution-contract.md` 读取 Issue #3/#4、本目录 README、02/03/04、plan 与 ledger，并核对当前 work、PR #1 和上一批状态。本轮只写本报告与 branch ledger，不执行下面的实现合同。

## 可发布的执行合同（execution contract）

以下 JSON 可放入新 PR body 第一段；它明确保留待联调门槛，不构成现在获取正文图或实现的授权。`allowed_paths` 是后续批次的受控上限；原件和旧材料保留约束优先于路径通配。

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-W3C-HTML-01",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "879596f10f34344337b1be2f05a6ffa347fd9a86",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "execution_branch": "codex/p3-w3c-html-01-260917",
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "parser_only",
    "status": "startup_plan_pending_joint_preflight",
    "source_uids": [
      "standard:w3c-dcat-3",
      "standard:w3c-did-core",
      "standard:w3c-json-ld-1.1",
      "standard:w3c-odrl-2.2",
      "standard:w3c-owl-time",
      "standard:w3c-rdf-1.2-concepts",
      "standard:w3c-vc-data-model-2.0"
    ],
    "canonical_source_versions": {
      "standard:w3c-dcat-3": "DCAT 3",
      "standard:w3c-did-core": "DID Core 1.0 Recommendation, 19 July 2022",
      "standard:w3c-json-ld-1.1": "1.1",
      "standard:w3c-odrl-2.2": "2.2",
      "standard:w3c-owl-time": "Candidate Recommendation Draft, 15 November 2022",
      "standard:w3c-rdf-1.2-concepts": "W3C Candidate Recommendation Snapshot 07 April 2026",
      "standard:w3c-vc-data-model-2.0": "Recommendation 2025-05-15"
    },
    "fixed_html_urls": {
      "standard:w3c-dcat-3": "https://www.w3.org/TR/2024/REC-vocab-dcat-3-20240822/",
      "standard:w3c-did-core": "https://www.w3.org/TR/2022/REC-did-core-20220719/",
      "standard:w3c-json-ld-1.1": "https://www.w3.org/TR/2020/REC-json-ld11-20200716/",
      "standard:w3c-odrl-2.2": "https://www.w3.org/TR/2018/REC-odrl-model-20180215/",
      "standard:w3c-owl-time": "https://www.w3.org/TR/2022/CRD-owl-time-20221115/",
      "standard:w3c-rdf-1.2-concepts": "https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/",
      "standard:w3c-vc-data-model-2.0": "https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/"
    },
    "allowed_paths": [
      "docs/plans/260916-corpus-completion-main-convergence/p3-w3c-html-01.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "raw_data/standard/Data Catalog Vocabulary DCAT 3/metadata.yaml",
      "raw_data/standard/Decentralized Identifiers DID Core/metadata.yaml",
      "raw_data/standard/JSON-LD 1.1/metadata.yaml",
      "raw_data/standard/ODRL Information Model 2.2/metadata.yaml",
      "raw_data/standard/Time Ontology in OWL/metadata.yaml",
      "raw_data/standard/RDF 1.2 Concepts and Abstract Syntax/metadata.yaml",
      "raw_data/standard/Verifiable Credentials Data Model 2.0/metadata.yaml",
      "raw_data/licenses/p3-w3c-html-01-*.md",
      "materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/**",
      "materialized_sources/corpus/standard-w3c-did-core--0d0c2de8/**",
      "materialized_sources/corpus/standard-w3c-json-ld-1.1--673c0833/**",
      "materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/**",
      "materialized_sources/corpus/standard-w3c-owl-time--446fcf02/**",
      "materialized_sources/corpus/standard-w3c-rdf-1.2-concepts--02058aec/**",
      "materialized_sources/corpus/standard-w3c-vc-data-model-2.0--af7d4a38/**",
      "scripts/materialize_all_sources.py",
      "scripts/validate_materialization_completeness.py",
      "scripts/audit_non_repo_coverage.py",
      "tests/test_materialization_integrity.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_excerpt.py",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_rights_review.yaml",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "generated_paths": [
      "materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/**",
      "materialized_sources/corpus/standard-w3c-did-core--0d0c2de8/**",
      "materialized_sources/corpus/standard-w3c-json-ld-1.1--673c0833/**",
      "materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/**",
      "materialized_sources/corpus/standard-w3c-owl-time--446fcf02/**",
      "materialized_sources/corpus/standard-w3c-rdf-1.2-concepts--02058aec/**",
      "materialized_sources/corpus/standard-w3c-vc-data-model-2.0--af7d4a38/**",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "pre_get_gates": {
      "consumer_and_response_version_binding": "joint_preflight_required_before_implementation",
      "scientific_assets": "exact_src_role_credit_scope_and_contract_revision_required_before_asset_get",
      "new_representation_publication": "per_uid_admission_required_before_public_persistence"
    },
    "explicitly_out_of_scope": [
      "ODCS pagination and every source UID outside these seven",
      "new collection identities, whole-site mirroring, recursive references, ontologies, datasets, weights and external code",
      "scientific asset GET before exact-src and scope contract amendment",
      "overwriting legacy root document.md or selectors.jsonl, deleting old materials, or fabricating old retrieval history",
      "fabricated Git revisions or silently replacing the selected dated version with latest",
      "automatic application of the old text-only package to new HTML or figures",
      "new generic pipeline, production-wide rewrite, dependencies or workflow changes",
      "demo selection changes, new claims or evidence, collector-assessment changes, or unrelated handwritten experiment changes",
      "OCR of every figure, perfect linear conversion, or automatic trusted promotion",
      "main merge, branch cleanup, history rewrite, administrator settings and issue closure"
    ]
  }
}
```

## 七项目标与既有缺口

以下路径均相对 repo root；允许的原件获取仅为 JSON 中七个 dated HTML 及预核后追加的准确正文资产。canonical metadata 的 `full_text_url` 与许可包 `source_version_url` 已固定；七个旧 manifest 的 `source_version` 仍为 null，不能回写为旧抓取已经核实此语义版本。没有可靠部署 commit，不引入虚构 `git:` revision。

启动前状态（before）来自当前 coverage／manifest 核对：七项的原件／提取状态均为 `unknown`、验证为 `partial_check`，每项 5 个既有 inventory 文件、共 35 个，无原 HTML。按本合同 UID 顺序的旧 selector 数为 1,095／1,256／1,410／484／345／1,349／1,773，共 7,712；结构记录为 resolved，语义核验仍 false。旧 root 公开 gate 均 allow 且 review revision match，但新表示未准入；knowledge 为 null。七条覆盖记录仍是 `needs_boundary_verification`／unresolved，本批的主要行动分类为 `parser_only`，不在启动时改写覆盖状态。JSON 的 `canonical_source_versions` 原样采用 canonical 字符串，旧 manifest null 是未填的保存层字段，不据此发明新版本或否定已有身份依据。

| UID／选定版本 | canonical metadata／capsule | 本地观察与后续重点 |
| --- | --- | --- |
| `standard:w3c-dcat-3`；DCAT 3，Recommendation 2024-08-22 | `raw_data/standard/Data Catalog Vocabulary DCAT 3/metadata.yaml`；`materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7` | 旧 `document.md:143,670,1693,3680`：§3.1/3.2 命名空间、§6.3 定义、§7 逆属性表及书目缺表达；§1–18／A–K 存在。既有法条载体 `w3c-software-document-2023.md`。 |
| `standard:w3c-did-core`；DID Core 1.0，Recommendation 2022-07-19 | `raw_data/standard/Decentralized Identifiers DID Core/metadata.yaml`；`materialized_sources/corpus/standard-w3c-did-core--0d0c2de8` | 旧 `document.md:523,2038,2458,2864,4083`：§5 三张值型／必选性表，B.1 架构图与书目须恢复／核对；§1–10／A–F 存在。既有法条载体 `w3c-software-document-2015.md`。 |
| `standard:w3c-json-ld-1.1`；1.1，Recommendation 2020-07-16 | `raw_data/standard/JSON-LD 1.1/metadata.yaml`；`materialized_sources/corpus/standard-w3c-json-ld-1.1--673c0833` | 旧 `document.md:214,3858,7724`：§1.4 术语、J 书目与代码注释伪标题；§1–13／A–J 及 JSON 例子存在。排除独立 Processing/API 和 Framing；既有 2015 法条载体。 |
| `standard:w3c-odrl-2.2`；Information Model 2.2，Recommendation 2018-02-15 | `raw_data/standard/ODRL Information Model 2.2/metadata.yaml`；`materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701` | 旧 `document.md:79,593,1172`：§1.3 术语、E 书目与所指图；模型及 Agreement 例子存在，整体完整性未证。排除独立 Vocabulary；既有 2015 法条载体。 |
| `standard:w3c-owl-time`；Candidate Recommendation Draft 2022-11-15 | `raw_data/standard/Time Ontology in OWL/metadata.yaml`；`materialized_sources/corpus/standard-w3c-owl-time--446fcf02` | 实物校正旧 `document.md:256,400,544,1081,1185`：§4.1.4 Duration、§4.2.7 hasBeginning、§4.2.53 unitType、A.2 汇总与 G 书目；保留联合 W3C–OGC／非背书／草案状态。旧 scope 排除了未保存 geologic-timescale 图，不等于新图已获准；既有 2015 法条载体。 |
| `standard:w3c-rdf-1.2-concepts`；Candidate Recommendation Snapshot 2026-04-07 | `raw_data/standard/RDF 1.2 Concepts and Abstract Syntax/metadata.yaml`；`materialized_sources/corpus/standard-w3c-rdf-1.2-concepts--02058aec` | 旧 `document.md:1091,2194,3490`：§5.1 XSD 类型表、J 书目与 backlink 噪声；保留附录实际 RFC 表达／独立许可，不向 RFC 全文扩张。复用已存 `w3c-rdf12-concepts-20260407-combined-notice.md`，但新增 HTML 范围仍须审查。 |
| `standard:w3c-vc-data-model-2.0`；Recommendation 2025-05-15 | `raw_data/standard/Verifiable Credentials Data Model 2.0/metadata.yaml`；`materialized_sources/corpus/standard-w3c-vc-data-model-2.0--af7d4a38` | 旧 `document.md:205,3665,5708,6141,7291`：§2 术语、G 书目／backlink、D 图；主体／A–G 存在。既有 2023 法条载体。 |

法条载体均位于 `raw_data/licenses/`，本批启动合同不允许改写这些共享资产。上述是既有观察，不是本轮 fixed GET／视觉核验结果；不把 unknown 改成不存在，也不预填 complete 或 allow。

允许新增 `raw_data/licenses/p3-w3c-html-01-*.md`，仅作为这七 UID 当前表示的累积 NOTICE 载体，保留原完整法条与署名、准确追加获准新范围；不用于改写旧共享资产或给其他来源扩授权。`materialized_sources/README.md` 与 `source_registry/README.md` 只由既有聚合生成器同步；P1 的 `coverage-baseline.md` 不在本批允许范围内。

## 最小实现与待联调决定

1. **先定消费与版本合同。** 新原件统一固定为各 capsule `source/specification.html`；候选阅读路径为 `normalized/document.md`，新 selector sidecar 为 `normalized/selectors.jsonl`。消费和绑定字段须与现有 retained-HTML helper、validator、审计及消费者联调后在本报告固定，才开始实现。最小 opt-in 为 `materialization.retained_text_binding=dated_html_response` 与 `retained_text_selectors=normalized/selectors.jsonl`；`manifest.selectors` 同时声明旧根和新 sidecar。新主 HTML revision 使用真实响应的既有 `sha256:` 模型；Git 固定 source 路径仍沿用原 strict 分支，不能为通过 replay 假造 commit。
2. **保全而非覆盖历史。** 七个旧根 `document.md`、`selectors.jsonl` 与旧文件内容保持原字节。旧 revision、null version、retrieval、版权包作为明确历史快照保留；如 root revision 改为新主 HTML revision，必须先固定相应历史 schema／校验接口。旧浮动或 dated GET 仍是旧事实，不改写为本轮固定成功响应。旧 NOTICE 可累积新范围，但旧完整法条与署名不删除。
3. **有限复用现有能力。** 在 `scripts/materialize_all_sources.py` 复用 `retained_html_sections`／`derive_retained_text_sources`，保留原 HTML 字节与源边界，恢复 table／pre／code／裸文本。只补实际必要的 dt/dd 结构和 dated-response binding、sidecar 输出；在 `scripts/validate_materialization_completeness.py` 接入对应严格验证，不能降低已有 Git 分支。不得建立新 adapter 框架。
4. **消费者用同一显式路由。** `scripts/audit_non_repo_coverage.py` 的 `collect_facts` 当前硬读根 selectors；只为该 opt-in 路由 sidecar，既有 document 路由已尊重 `materialization.document`。`experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py` 的 `choose_local_selectors` 需要最小显式分支，并由同目录 `test_excerpt.py` 验证文档／selector 配对与声明缺失 fail-closed；未 opt-in 来源保持原行为。正常 demo 选源不变。
5. **正文资产先预核再修合同。** 由实际选定 HTML 列出每张正文图的原始 `src`、resolved URL、本地路径、角色、出处／信用和许可范围，区别科学表达与 logo／导航／样式。精确列表与新表示准入方案先修订本合同，再 GET 对应资产；路径必须保持相对资源可离线解析，不直接泛抓 `source/assets/**`。含远程链接的 HTML 不等于正文图已本地保全。
6. **新表示单独准入。** 原有七项 allow 只对应既有文字包。逐项检查实际固定 HTML 的版权／文档状态／图 credit，更新对应六字段 package、manifest／NOTICE 与机器 audit；旧 allow 不直接复制给新增 HTML／图。已有 W3C 和 RDF 组合授权可作为依据，不新增逐组件历史考古；真正新限制仅阻塞该 UID，公开持久化未知时不提交新增原件。

## 生成物与验收边界

七 UID 均不在当前 36 selected 来源。保持 selected set、72 claims、72 evidence 和 collector-assessment 原字节；不新增这些规范的知识内容。整个 `materialized_sources/index.yaml` 是 build identity 输入，local_bytes／revision 变化仍需 registry、snapshot、release／review 等必要全局身份传播；135 Wiki Markdown 只允许必要 build ID 同步，不能以未 selected 为由提交 stale release。JSON 中 experiment 通配仅允许这些既有生成物传播，以及列定的 build_demo／test_excerpt 最小路由，不许可其他手工改写。

后续报告须按 UID 给真实 before→after，分别记录原件、提取、持久化、selectors、再分发与 candidate/trusted；至少完成：

- 固定 dated 请求、真实 requested/resolved URL／HTTP／媒体类型／观察时间与主 HTML 字节绑定；title／版本日期／文档状态与 canonical 一致，拒绝错误页／移动最新版／悄然版本更换。
- HTML 与列定正文资产原字节保留，所有声明本地文件可在新 checkout 使用；旧文件／历史记录保持，不能依赖 tmp 或本机缓存。
- 用规范开／中／末、全部主章／附录边界及上表已证空定义／表／引用检验正文；table 单元格、dt/dd 配对、代码原结构和 source bounds 可核对。原 HTML 离线可读是保全证据，不替代派生文本质量判断；存在具体损失则如实 partial，不要求所有图完全 OCR 或排版线性无损。
- 首／中／末及缺口位置的 selectors 解析到新 consumer；旧根 selectors 仍可解析旧文档。缺 sidecar／损坏绑定／wrong version／缺列定资产时不能回退旧文档然后声称新表示通过。
- 定向 retained HTML／binding／sidecar／消费者正反向测试，再运行适用 tests、raw-data／materialization／rights／coverage／demo 验证与 reproducibility；只读全库生成器不能重抓其他 source。
- 按 `05` 在实际最终 HEAD／BASE 取得非作者独立三维 PASS 和该 HEAD CI success，才正常 merge 到 work。变更后重评，不复用 PR #16 的 PASS／CI。

同一输入集合只有一个 writer；代码与只读内容审阅可在文件所有权不重叠时协作，但不同时写 canonical、capsule、machine audit 或全局生成物。身份歧义、base 冲突或 scope 变更停止整个 PR；单 UID 的访问／公开准入失败记录具体 unresolved 后可完成其他独立项。不预设它们都成功，也不把失败默默排出台账。

## 明确非结果（explicit non-results）

当前仅完成两份启动文档。无新增 HTML／正文资产 GET，无 parser／validator／消费者实现，无生成物重建，无本批内容／法律／独立 PASS 或 CI 结果；PR 尚未创建。消费路径、dated-response/history schema 及正文资产清单尚待联调／预核修订。PR #16 已在 work，但本批及 PR #1 尚未进入 main；无 trusted 晋级、删除正文、清理分支、改写历史、管理员设置或关闭 Issue #3/#4。

## 联合预核与合同修订（joint preflight，2026-09-17）

历史字段校正：以上启动叙述的旧 `source_version: null` 是读取缺省字段得到 None 的简写；七个旧 manifest 实际没有该键。历史快照保留原字典，不补造显式 null，也不声称旧抓取已经核实本轮 semantic version。

以上启动状态保留为历史。PR #17 已在任何本批来源 GET 前登记，初始 HEAD 为 `da9fa55bf16176854e3a1857ade39bc447285e93`、BASE 为 `879596f10f34344337b1be2f05a6ffa347fd9a86`。七个列定 HTML 各一次真实 GET，批次启动观察为 2026-09-16 21:16:09 UTC，完成观察为 21:16:28 UTC；均 HTTP 200、`text/html; charset=utf-8`，resolved URL 与列定 dated URL 相等。按合同顺序字节数为 664822／730300／1021461／181875／265548／577086／1023165。它们与旧 retrieval 已记录的响应摘要分别相同，但旧胶囊没有保存原 HTML；本次不能改写为旧时已有原件。尚未取得任何图资产、尚未将新正文放进 repo。

主线与代码 planner 已读现有 helper／validator／实际消费者并固定最小接口：`retained_text_binding: dated_html_response`；单一 `source/specification.html`；`normalized/document.md`；`retained_text_selectors: normalized/selectors.jsonl`；manifest 同时保留根及 sidecar selector 声明、总数按两文件相加。新 current version 采用上列 canonical 原字符串，主响应沿用实际 `sha256:` revision；`historical_acquisition` 复用既有 manifest 历史快照方式，保留旧 null source_version、retrieval、rights、materialization 与旧 inventory 事实。旧正文与根 selector 不写，metadata／manifest／README／NOTICE 仅按本合同维护当前表示与历史。无 opt-in 的 Git 绑定继续严格；失败必须穿透到现有保全异常而非清空或降级。

七响应实际均没有单一 `<main>`，正文包含 `.head` 身份／版权、abstract、sotd、多个主章／附录，不能一律删 header 或仅取一个 section。新表示允许显式列定的 HTML 排除选择器（exclude selectors），仅移除实见导航 `nav#toc`、`p#back-to-top`、DID／RDF／VC 的 `.dfn-panel`、页首 `.head img` 商标图和 `.head a.orcid svg` 图标；身份、作者、版权、文档状态、正文 notes 和引用保留。原 HTML 不作任何排除或改写。每源只声明实际存在的排除项，不设全站 DOM 框架；JSON-LD 示例切换按钮携带输入／结果标签，不能统一删除 button。

实际预核还发现 JSON-LD 的一幅和 RDF 的四幅正文图使用 `object[data]`，不是 img。现有 retained renderer 在本批 opt-in 下需保留列定本地图路由、aria-label 与 fallback 正文，不执行 object；不得只检查 img 后宣称图完整。dt/dd 仅分隔原始定义块、保持多 term／多 definition 顺序，不猜配对。新消费者复用已有整围栏屏蔽并标明 `retained_html_response`，避免从示例代码内部摘出假正文；旧 Git／legacy 消费不变。该最小实现限于原已列定六个代码／测试路径，图的具体 URL／credit／公开准入仍待三位只读 reader 预核、合同追加后才 GET。

当前仅批准上述有界实现接口；没有新的正文图获取授权列表，没有声明新表示公开 allow、文本 complete、独立 PASS、最终 CI 或 main 落地。

## 正文图获取边界（asset acquisition amendment）

本次仅追加下表实际由七份固定 HTML 引用的 48 件正文图，先取得原件以核图内信用、内容与边界；这不是公开再分发批准。身份为对应原规范的图，不新增 source UID。W3C 作品许可、实际图注与信用是预核依据，DCAT 三张地图的底图信用仍须取得像素后核实；OWL 的论文／地层表参考链接不是对图版权归属的推断。原件仅临时审阅，逐项公开准入完成前不复制入 repo。排除 W3C／OGC logo、ORCID 图标、ODRL 可选 SVG 替代、CSS／JS／字体／EPUB 与全部外部参考资料。

每个下列路径的请求 URL 严格为该 UID 已列定 dated HTML URL 加相对路径（去掉 `./`）；保留位置为该 capsule 的 `source/` 加同一相对路径。完整请求是已有七个固定前缀与下表有限精确路径的组合，不使用目录抓取。

| UID | 正文图相对路径（exact paths） |
| --- | --- |
| `standard:w3c-dcat-3` | `./images/dcat-all-attributes.svg`；`./images/ex-spatial-coverage-geometry-anne-frank-house.png`；`./images/ex-spatial-coverage-centroid-anne-frank-house.png`；`./images/ex-spatial-coverage-bbox-netherlands.png`；`./images/version-chain-and-hierarchy.svg`；`images/dcat-relationships.svg`；`images/schema.org-dataset.svg` |
| `standard:w3c-did-core` | `diagrams/parts-of-a-did.svg`；`diagrams/did_brief_architecture_overview.svg`；`diagrams/diagram-did-document-entries.svg`；`diagrams/diagram-production-consumption.svg`；`diagrams/diagram-resolve-resolverepresentation.svg`；`diagrams/did_url_dereference_overview.svg`；`diagrams/did_detailed_architecture_overview.svg`；`diagrams/figure-a.1-did-and-did-document-graph.svg`；`diagrams/figure-a.2-also-known-as-graph.svg`；`diagrams/figure-b.1-controller-and-subject-equivalence.svg`；`diagrams/figure-c.1-independent-did-controllers.svg`；`diagrams/figure-c.2-group-did-controllers.svg` |
| `standard:w3c-json-ld-1.1` | `linked-data-graph.svg` |
| `standard:w3c-odrl-2.2` | `00Model.png`；`01Constraint.png`；`02Rule.png`；`03Shared.png` |
| `standard:w3c-owl-time` | `./images/TemporalEntity.png`；`./images/IntervalRelations.png`；`./images/TemporalPosition.png`；`./images/TemporalDuration.png`；`images/GeologicTimescale.png` |
| `standard:w3c-rdf-1.2-concepts` | `rdf-graph.svg`；`rdf-graph-arcs.svg`；`triple-term.svg`；`asserted-triple-term.svg` |
| `standard:w3c-vc-data-model-2.0` | `diagrams/ecosystem.svg`；`diagrams/claim.svg`；`diagrams/claim-example.svg`；`diagrams/claim-extended.svg`；`diagrams/vc.svg`；`diagrams/vc-graph.svg`；`diagrams/vc-jwt.svg`；`diagrams/presentation.svg`；`diagrams/vp-graph.svg`；`diagrams/vp-jwt.svg`；`diagrams/claim-example-2.svg`；`diagrams/zkp-cred-pres.svg`；`diagrams/privacy-spectrum.svg`；`diagrams/vp-graph-mult-creds.svg`；`diagrams/vp-jwt-mult-creds.svg` |

所有取得响应逐件记录状态、URL、字节与观测时刻。图内出现新的第三方信用或排除时先暂停该资产公开包装，保留实际未决；不得将获取成功自动写为 allow。源图不修改、链接转换只在派生层，图义无法完整线性表达则 text 保持 partial。

职责分配（ownership）：代码执行者只写合同列定六个代码／测试路径；三位内容 reader 只写临时审阅报告；主线负责获取和合同，后续包装与覆盖更新按明确文件所有权串行进行，不并行写同一 capsule／metadata／audit／聚合输入。

## 有界修订：三张地图不公开、RDF 图形样式依赖

三张 DCAT 地图已 HTTP 200 取得，但实际像素、PNG 元数据、作品正文和有界官方历史均未给底图提供者/许可，故新公开范围 unknown。三 PNG 不写 repo；原 HTML 字节、原 caption、WKT 正文保留。仅准确声明的 source_options.unretained_assets 转为普通发布方绝对链接并明确未保留原因，不远程嵌图，不冒充离线完整；其他 45 件正文图仍须本地原件/inventory/retrieval。Git 绑定逻辑不变。

RDF 四 SVG 的实际 XML 均在第 3 行引用 figure.css，决定箭头、虚线和节点外观。现仅批准获取及审阅 https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/figure.css，目标 source/figure.css；审阅实际内容/依赖/作品许可后才决定公开。非泛化网站 CSS 抓取，不加载脚本。


## 新表示的逐作品公开准入（publication admission，派生质量另验）

主线结合实际固定作品版权/许可段、全部源 DOM 的正文边界、三位内容 reader 对 48 件实物的 XML／像素／信用审阅，批准在完整 NOTICE、原署名、修改说明及非背书条件下，持久化七个列定 HTML 原响应、45 件列定非地图正文图、RDF 单件 figure.css，以及对应文字/selector 派生。许可判断不继承旧 text-only allow；不宣称后续正文、CI 或独立审核已 PASS。

| UID | 本次新增准入范围 | 适用作品许可与保留条件 |
| --- | --- | --- |
| standard:w3c-dcat-3 | fixed HTML、4 SVG、文字/selector；三地图仅原图普通链接与缺口说明，PNG 不提交 | 2023 W3C 完整 NOTICE；三地图底图许可 unknown，不扩大整件公开范围 |
| standard:w3c-did-core | fixed HTML、12 SVG、文字/selector | 2015 W3C 完整 NOTICE；作者、DHS/EU 资助及不背书原文保留 |
| standard:w3c-json-ld-1.1 | fixed HTML、1 SVG、文字/selector | 2015 W3C 完整 NOTICE；附录图名源生不一致不私修 |
| standard:w3c-odrl-2.2 | fixed HTML、4 PNG、文字/selector | 2015 W3C 完整 NOTICE；不含独立 Vocabulary 或四个可选 SVG |
| standard:w3c-owl-time | fixed HTML、5 PNG、文字/selector | 2015 W3C 完整 NOTICE；联合 W3C–OGC / CRD / 不背书状态与科学引用保留；地质图是原作区间关系例示，不是外部 chart 截图 |
| standard:w3c-rdf-1.2-concepts | fixed HTML、4 SVG、figure.css、文字/selector | 2023 W3C 完整 NOTICE；原组合 RFC3986/3987/RFC6874 声明/许可原样累积，范围仅对应附录代码；不将 CR Snapshot 改称 Recommendation |
| standard:w3c-vc-data-model-2.0 | fixed HTML、15 SVG、文字/selector | 2023 W3C 完整 NOTICE；资助/不背书、regex 来源、原作 alt 与图值差异原样保留 |

RDF figure.css 仅一次 GET：2026-09-16 21:33:05 UTC 开始、21:33:21 UTC 完成观察，HTTP 200，text/css，891 bytes，无跳转。实际 16 行只有图形填充、箭头和虚实线规则及本地 fragment 引用，无新外部依赖或单独信用；内容 reader 把四 SVG 原字节与 CSS 同层复制后，实际确认箭头与 asserted/unasserted 差异显示恢复。不是递归网站样式镜像。

图形原件保留不代表图義全部转为线性文字：DID B.1 细化连线、VC 附录 D 第二凭证具体标签，以及原作 alt 与图值差异须在新提取验收后准确记录。完整原件、文字可用性、提取完整性、公开范围和知识门控分别判断。七 UID 未进入 demo 选集，selected 36 / claims 72 / evidence 72 与 collector assessment 不应改变。

## 实现冻结与包装交接（implementation freeze）

代码执行者 `/root/p2_parser_planner` 已冻结六个授权路径。实际运行 67 个 materialization、15 个 excerpt、30 个 TeX reading、33 个 PDF supplement 定向测试及六文件 AST 解析，均通过；这是隔离代码测试，不是七个真实胶囊或本 PR 的最终验收。新增保真行为限显式 dated-HTML opt-in：dt/dd 边界、object/ARIA/fallback、pre 的 br/NBSP、原 cell span 注记、多行 alt 全词、显式缺图普通链接；旧 Git/未 opt-in HTML 继续原语义。

`/root/journal01_packaging_executor` 在代码冻结和逐作品准入后负责七 canonical metadata／七胶囊／新 cumulative NOTICE／rights 对应七行，不写 coverage、聚合、代码、Git。主线持有合同、最终聚合和提交；三位内容 reader 等真实派生后逐篇复核；最终 evaluator 不参与这些实现。首次派生仅用既有 replay 的 `check_derived=False`（两派生文件均不存在才允许），正常 wrapper 缺失新正文或 sidecar 必须报错。RDF `figure.css` 显式 local rewrite 将其纳入既有原件核验，未另造资源依赖框架。

主线已独立核对53件新增原件（7 HTML＋45正文图＋1 CSS）共7,210,546 bytes，与真实获取原件逐字节一致；三张未准入地图不存在，source目录没有清单外文件。七份累计 NOTICE 均以基线完整旧 NOTICE 字节为前缀；旧 W3C 根 document/selectors 对基线仍无 diff。这些仅是已完成的保全检查，不提前代替真实新正文验收或最终独立 PASS。

## 审阅发现与执行闭环（review → execution loop）

1. 独立 evaluator `/root/pr17_independent_evaluator` 在纯临时 fixture 发现 P2：显式新 sidecar 声明仍在、materialization 损坏且新 HTML/sidecar 缺失时，generic 分派可能误入 destructive prepare。作者将显式声明纳入保全识别；独立复核标量／空映射／缺键三变体及两个入口均失败关闭，prepare/fetch/finalize 为零、剩余字节不变。保留原失败记录，不以初次绿色测试掩盖此发现。
2. 实物 reader 发现 DID 两段 ABNF、OWL 三段正则位于 table cell，旧行拼接使 opening fence 不在独立行。作者仅对 dated 模式中含真实 pre 的行输出有序 cell 块，保留空列和 span 注记、原代码字符及独立开闭围栏；未重写一般表格引擎。代码 fixture 与独立定点复核通过，真实两胶囊须重放后再由 reader 定点关闭。
3. 实际自动摘句发现内联 collector anchor 混入候选块。reading view 现跳过整块，不清洗／拼接后冒充连续引用；HTML 表示的 limitations 不再误称 TeX。16 excerpt 回归通过，JSON-LD／RDF／既有 Streaming TeX 摘句保持不变。VC 默认候选可落入真实发布状态段，这是自动摘句的具体质量限制，不等同实质知识；七 UID 不加入现有 demo 选集，不新增 claim 或 trusted 判定。

最新代码定向结果为70 materialization／16 excerpt／30 TeX reading通过；早前主线170项全测是修复前快照，最终提交仍需重新全测、重放、CI及三维独立审核。初次实物 sidecar 合计850条（180/121/132/56/134/64/163），旧7712条保持，总声明8562；不能误用先前执行消息的950心算。

## 最终实物复核与本地验证（final local verification）

上述代码修复已应用到实际 DID／OWL 派生并由原 reader 定点关闭：DID source L1547／L1594 的代码围栏分别在新正文 L1371–1378／L1431–1433；OWL source L3346／L3377／L3407 分别在新正文 L2298–2305／L2332–2339／L2366–2373。五段原代码字符均保留，开闭围栏独占行、周围有段落边界；其他五胶囊正文未因此改写。真实 selector 的行范围／preview 在重放后重新核对，不沿用修复前定位。

内容复核还覆盖 JSON-LD 358 段 pre／88 个表、RDF 6 段 pre（含高亮 ABNF）／6 表、DID 50 段 pre／10 表／33 术语、VC 112 段 pre／7 表／22 术语，以及各规范参考文献和全部章／附录结尾。旧空定义／表格／引用缺口已恢复；三位 reader 的判断是实物边界审阅，不是仅以字数或 selector 数量代替内容质量。

主线在最后代码与正文冻结后实际执行：

| 命令／检查 | 实际结果 |
| --- | --- |
| `make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | 174 tests PASS：4 evidence、16 excerpt、6 rights propagation、13 publication rights、70 materialization、33 PDF、2 reproducibility guard、30 TeX |
| `make demo PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | PASS；36 sources、72 claims、72 evidence、135 Wiki pages、357 typed links、3 context packs，验证 warnings=0／errors=0 |
| `make reproducibility PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` | PASS；当前落盘树、重复完整构建、仅 Wiki 编译、只读验证四阶段均为 169 generated files byte-identical |
| 上述重放内 `make validate`／`scripts/validate_materialization_completeness.py` | PASS；215 metadata／215 manifests、3,071 inventory entries、25,017 declared selectors，warnings=0／errors=0；文档校验 53 Markdown／80 relative links／errors=0 |
| `scripts/audit_non_repo_coverage.py`（同一锁定 Python） | PASS；131 非 repo／84 repo 排除、summary 与本报告一致；strict complete 6、unresolved 125。只更新七 UID；其他 124 对象和原始块、全部 131 knowledge 保持，旧 execution 完整嵌入历史 |
| 既有 publication-rights validator 的只读函数 | 本批七 UID errors=0／blocked=0；全库仍为 2 项历史 package mismatch（arxiv:2404.16130、arxiv:2502.18864）及 64 项历史 blocked，明确不是全库公开门控 PASS，保留 P4 调和工作 |
| 原件／历史／范围核对 | 53 原件与真实响应逐字节一致；7 old NOTICE 完整前缀、14 old document/selectors 字节、7 historical manifest 字典、93 个非目标 rights 对象保持；三张 DCAT 地图没有入库 |

环境使用已锁定 Python 3.12.13。既有 PDF 解析的可选 fontTools/CFF 提示仍存在；没有以安装新依赖改变既有提取结果。原件以及结构保真派生保留源空白，通用 `git diff --check` 对这些新增保全文本会报告源生行尾空白；不为消除格式提示修改原件或代码字符。代码、手写文档、metadata／audit 和既有生成物的定向 whitespace 检查另行执行，不混称全树 whitespace 无告警。

以上是本地结果，不是最终 SHA 的远程 CI 或非作者独立三维结论。最终审核与合并记录保存在 PR #17；本文件在提交时保留 pending，避免为了写入自身 HEAD 而制造无限的审核失效循环。

独立实物重放补充发现：首个实现提交的 RDF manifest 新增辅助锚点说明被手工写为单行；既有 YAML 写出器在首次 replay 时将其折为两行。语义、正文、原件和 selectors 未变，但首次全包字节一致不成立，不能借第二轮稳定掩盖。主线仅按既有序列化结果修正这一折行；报告记下该发现，提交更新后重新锁定最终 HEAD／BASE，独立 reviewer 对修正后副本再验，远程 CI 也必须对应新 HEAD。
