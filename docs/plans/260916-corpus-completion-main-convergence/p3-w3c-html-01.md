---
phase: P3-W3C-HTML-01
base_sha: 879596f10f34344337b1be2f05a6ffa347fd9a86
branch: codex/p3-w3c-html-01-260917
status: startup_plan_pending_joint_preflight
pull_request: null
adapter_family: generic_web_or_document_v2
action_bucket: parser_only
source_acquisition: not_started
independent_evaluation: not_requested
---

# P3-W3C-HTML-01 — 七份固定 W3C 规范的保全与正文提取启动合同

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
| `standard:w3c-owl-time`；Candidate Recommendation Draft 2022-11-15 | `raw_data/standard/Time Ontology in OWL/metadata.yaml`；`materialized_sources/corpus/standard-w3c-owl-time--446fcf02` | 旧 `document.md:377,601,1081,1185`：§4.1 Duration、§4.2 定义、A.2 汇总与 G 书目；保留联合 W3C–OGC／非背书／草案状态。旧 scope 排除了未保存 geologic-timescale 图，不等于新图已获准；既有 2015 法条载体。 |
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

同一批次只有一个 writer；只读 agent 可分别核正文／信用／消费者，但不同时写 canonical、capsule、machine audit 或全局生成物。身份歧义、base 冲突或 scope 变更停止整个 PR；单 UID 的访问／公开准入失败记录具体 unresolved 后可完成其他独立项。不预设它们都成功，也不把失败默默排出台账。

## 明确非结果（explicit non-results）

当前仅完成两份启动文档。无新增 HTML／正文资产 GET，无 parser／validator／消费者实现，无生成物重建，无本批内容／法律／独立 PASS 或 CI 结果；PR 尚未创建。消费路径、dated-response/history schema 及正文资产清单尚待联调／预核修订。PR #16 已在 work，但本批及 PR #1 尚未进入 main；无 trusted 晋级、删除正文、清理分支、改写历史、管理员设置或关闭 Issue #3/#4。
