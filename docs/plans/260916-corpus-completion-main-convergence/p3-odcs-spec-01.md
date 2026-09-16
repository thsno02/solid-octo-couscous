---
phase: P3-ODCS-SPEC-01
base_sha: 463b848b0b4abef33df6fa51f6fcf9bd7482a922
branch: codex/p3-odcs-spec-01-260917
status: startup_plan_exact_path_preflight_pending
pull_request: null
source_uid: standard:odcs-3.2.0
source_acquisition: not_started
independent_evaluation: not_requested
---

# P3-ODCS-SPEC-01 — ODCS 3.2.0 规范正文补齐

## 规划与真实起点（planning）

本批目标是补齐已收集的固定 ODCS 3.2.0 正文，不增加 UID、不抓整个 GitHub repo。当前唯一 work 已在 `463b848b0b4abef33df6fa51f6fcf9bd7482a922`：PR #17 正常 merged/closed，非作者三维 PASS 对应 HEAD `1afaf52fd3ba81ec9dba09d733ce4a3a01f19154` / BASE `879596f10f34344337b1be2f05a6ffa347fd9a86`、COMMENT review 5229044802、CI 35157849042 success。PR #1 仍 Draft，head 是该最新 work、base main `99ce4670be91637209d67792de0962404fa96488`。

主线延续已经完整读取的 Issue #3/#4、本目录 README、02/03/04、plan 与 ledger；本次重新核对 06 合同、上一批关闭结果、work 与 PR #1 的准确远端状态。短期分支从该 work 创建，当前仅登记两份启动文档，无正文 GET、代码改动或生成重建。旧分支保留，不删除、不强推，也不把 work 当作最终 main。

工作假设（working hypothesis）：现存 1,454-byte 首页正文只列 15 章标签及 Full example 入口，真正字段定义与完整例子尚未持久化。考虑“只更正台账”“抓渲染站点”“保留固定 commit 原生文档”三条路径，选择第三条；其正文边界、版本和最小离线派生最清晰，复用现有 retained helper，不造新框架。

## 启动合同（execution contract）

先发布本合同，再只取得明确列定 README／LICENSE 及必要固定目录信息。其余章／example 的准确 href 未在旧转换中保留，不能猜文件名；填满有界路径后修订远端合同，才获取对应正文。临时取得不自动授权公开持久化。

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-ODCS-SPEC-01",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "463b848b0b4abef33df6fa51f6fcf9bd7482a922",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "standard_spec_fetch",
    "source_uids": [
      "standard:odcs-3.2.0"
    ],
    "upstream_commit": "f0bdad95346905d500be5ef4b2c2d9b1d95223b7",
    "selected_version": "3.2.0",
    "status": "startup_plan_exact_path_preflight_pending",
    "allowed_paths": [
      "raw_data/standard/Open Data Contract Standard 3.2.0/metadata.yaml",
      "materialized_sources/corpus/standard-odcs-3.2.0--affacf92/**",
      "raw_data/licenses/p3-odcs-spec-01-*.md",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_rights_review.yaml",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "docs/plans/260916-corpus-completion-main-convergence/p3-odcs-spec-01.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "generated_paths": [
      "materialized_sources/corpus/standard-odcs-3.2.0--affacf92/**",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "explicitly_out_of_scope": [
      "implementation before PR17 normal merge and latest work base confirmation",
      "chapter or full-example GET before exact fixed-commit path contract amendment",
      "latest or different-version substitution, all-site mirror or recursive external references",
      "JSON Schema as replacement body, full examples directory, ODPS, datasets, weights and runtime dependencies",
      "inheriting old text-only allow as new representation admission",
      "legacy document, selectors, history or shared-license deletion/overwrite",
      "pipeline or consumer edits before an evidenced minimal-change contract amendment",
      "handwritten experiment edits, new selected sources/claims/evidence/collector assessments",
      "perfect conversion/OCR, trusted promotion, administrator settings, history rewrite and branch cleanup"
    ],
    "execution_branch": "codex/p3-odcs-spec-01-260917",
    "initial_source_requests": [
      {
        "path": "docs/README.md",
        "url": "https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/docs/README.md",
        "proposed_local_path": "source/docs/README.md",
        "purpose": "actual fixed-version homepage and 15 chapter plus full-example direct href discovery"
      },
      {
        "path": "LICENSE",
        "url": "https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/LICENSE",
        "proposed_local_path": "source/LICENSE",
        "purpose": "actual fixed-commit work license"
      }
    ],
    "metadata_preflight": "read only fixed-commit tree paths and necessary navigation metadata; no all-file body download",
    "pre_get_gates": {
      "initial_requests": "only after startup PR published; scratch acquisition is not publication admission",
      "chapters_and_example": "all exact fixed-commit source/local paths and formats must be recorded in amended PR contract before GET",
      "publication": "inspect actual selected files credits/exclusions; old homepage allow does not automatically cover new representations",
      "consumer": "confirm strict git binding and explicit sidecar route; authorize exact minimal code paths only if observed necessary"
    }
  }
}
```

## 目标边界与预核（target boundary）

固定上游 commit 为 `f0bdad95346905d500be5ef4b2c2d9b1d95223b7`，canonical version 3.2.0／tag v3.2.0；旧网页的“Since v3.1.0”是分页说明，不换目标版本。以下是已有首页的准确标签／顺序，尚不是已核准的 source 文件名：

1. Fundamentals
2. Schema
3. Context
4. References
5. Data Quality
6. Support & Communication Channels
7. Pricing
8. Team
9. Roles
10. Service-Level Agreement
11. Infrastructures & Servers
12. Custom & Other Properties
13. Authoritative Definitions
14. Tags
15. Variables
16. Full example（直接完整示例，不以 JSON Schema 代替）

只核 fixed README 的直接链接及必要导航声明；不遍历全部 examples，不抓外链定义／其他版本／数据／runtime／模型资产。若原稿不是这些目标或例子来自不同作品，先解决具体身份边界，不下载相似内容凑数。

现有机器审阅指向固定 README 的 The Bitol Contributors / Apache-2.0 及同 commit LICENSE；旧 allow 只涵盖旧首页文字。本批审查选定实际文件的信用、另行许可与排除，保留 Apache 完整法条、原署名及修改说明，scope 只列真实原件。复用共享原法条或新增本批累计 NOTICE，不改共享许可、不做无具体反向证据的历史考古；新增公开范围 unknown 时不先提交正文。

## 最小消费与所有权（consumer / ownership）

沿用 `standard-odcs-3.2.0--affacf92` 胶囊。旧根 document／selectors／NOTICE 历史保持；新原稿按真实路径保存，新 consumer 为 `normalized/document.md` 与显式 `normalized/selectors.jsonl`。首页→15章→完整example按声明顺序组装，保留原表格／围栏／版权；使用真实 git commit 严格绑定，不冒充 dated HTML 响应。先核现有 git 分支是否直接支持新 sidecar；若必要，只修订合同加入精准最小 helper／validator／test 路径再改代码。YAML full example 必须是“示例”，不得默认为 schema。

主线负责固定边界／GET／公开准入和最终提交；代码预核只读，包装作者与台账作者串行写各自路径；独立 evaluator 不参与作者实现。仅一个活跃批次，不与后续 PDF／网页工作并行改 index/registry/coverage。先核选集；即使未 selected，global index 改动仍需必要 build identity 传播，不增 claim／evidence／collector assessment。

## 验证与明确非结果（validation / explicit non-results）

最终报告逐 UID 给出 original、text、persistence、selectors、public、knowledge 的实际 before→after；每份真实章节／完整例子核开中末、字段定义和例子，真实 source bounds 与配对 consumer 可回溯。缺口记录具体原因和 next action，不以首页存在推完整。离线 retained replay、对应 tests／validate／coverage／demo／repro须适用当前最终树；独立非作者在最终准确 HEAD／BASE 三维 PASS 且该 pair CI成功后，才能正常 merge 到 work。

目前没有新正文、公开准入、派生／CI／独立 PASS；没有进入 main、没有 trusted 晋级、没有 issue 关闭、分支删除或历史重写。后续仅在本批正常合并后启动下一批。

