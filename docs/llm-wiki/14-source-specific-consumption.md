# 来源专属消费（Source-Specific Consumption）

## 决策

LLM Wiki compiler 消费统一的物化接口（materialization interface），而不是直接消费 URL，也不会把不同来源强行压平成匿名 chunks。

```text
source metadata
→ adapter selection
→ frozen source revision
→ source-specific parsing / semanticization
→ local evidence + selectors
→ candidate claim
→ wiki compilation
```

这避免把 repository 当成文章、把 PDF 页当成普通段落、把标准当成实现，或把可变网页当成不可变来源版本。

## 消费矩阵（Consumption Matrix）

| 来源 | 首选物化方式 | 主要 selector | 额外语义化 |
|---|---|---|---|
| arXiv | source archive 与 TeX tree | file、line、section | 通常不需要 |
| journal / preprint | 开放结构化 HTML 或 licensed full text；PDF fallback | section/paragraph 或 page/region | 不需要 |
| GitHub repository | frozen commit 与 semantic capsule | commit、file、line | 需要 |
| blog / web | 带时间与 hash 的 HTML/text snapshot | DOM/paragraph | 观点与来源角色分类 |
| standard / ontology | 精确版本或 edition | section、term | normative/informative 分类 |
| dataset / benchmark | versioned release、split 与 evaluator | row/field/item/run/metric | schema 与 protocol 重建 |
| incident / retraction | primary event record | event/time/affected object | dependency impact |

## Repository-to-Wiki 桥接

一个 repository 同时包含目录拓扑、依赖、文档、接口、配置、tests、evaluation、release history 与 paper-code linkage。单一 README 无法代表所有语义表面。

当前 adapter 的目标是建立确定性 baseline：固定 commit，保存预算内的高价值证据，生成 exact local selectors 和候选 mini-wiki。它明确不证明：

- runtime behavior；
- build/test 成功；
- benchmark 数字真实；
- production reliability 或 security；
- README 与实际实现一致。

当 GitHub REST API 不可用时，commit-pinned raw-path fallback 仍会保存 README、架构/接口文档和构建配置等常规路径；manifest 必须标记 tree coverage 不完整。不存在、重命名或无法公开读取的 repository 则诚实降级为 `metadata_capsule`。

## Paper 与 Repository 是独立来源

```text
Paper --describes--> Method
Repository --implements--> Method
Commit --realizes--> Repository state
Benchmark run --evaluates--> Commit
Claim --supported_by--> Paper section / code evidence / benchmark run
```

同一作者维护的 paper 与 repository 也不能自动互相证实；README 更不能作为论文结论的独立 corroboration。

## 准入边界（Admission Boundary）

Repository capsule 和生成页面都处于 candidate/review 状态。晋升需要：

1. pinned revision；
2. 可解析的本地 evidence selectors；
3. 与证据范围一致的措辞；
4. paper、official docs 与 execution evidence 之间的冲突检查；
5. 与风险匹配的 review；
6. rollback path。

诸如 “state of the art”“production ready” 或 benchmark 数字，默认仍是 maintainer assertion，直到获得独立证据。

## 更新、删除与回溯

新 commit 产生新 source revision。旧版本应由 Git history 保留。系统需要根据 source delta 找到受影响的 evidence、claims、wiki sections 和 context packs，再执行 dependency-aware rebuild。

Force-push、相同 reference 下 bytes 改变、source removal 或 retraction 都属于需要传播的完整性事件；不能通过覆盖旧页面抹掉 lineage。

## 当前可执行入口

```text
pipeline/materialization_all_260910.yaml
scripts/materialize_all_sources.py
scripts/validate_materialization_completeness.py
source_registry/registry.yaml
materialized_sources/index.yaml
materialized_sources/corpus/
experiments/v0_meta_kb_initialization_demo_260910/
```

完整运行使用 `make materialize`；只重建某个来源族可使用 `--only-source-type`。所有 consumer 应先读取 manifest 的 `content_tier`、`status`、`rights`、`warnings/errors` 与 selector 清单，再决定允许的下游操作。
