---
phase: P2
base_sha: 474992c2664fb2af06765abdb4dfb23b6db40fb8
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":27,"full_text":90,"metadata_capsule":14},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":1,"metadata_only":18,"partial":6,"unknown":106},"text_extraction_counts":{"partial":23,"unavailable":18,"unknown":90},"action_bucket_counts":{"access_restricted":7,"author_manuscript_fetch":2,"canonical_repair":8,"html_article_snapshot":14,"identity_or_version_ambiguous":2,"needs_boundary_verification":90,"open_fulltext_fetch":6,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":26,"block":65,"unknown":40},"content_inspected_full_text":26,"structure_only_full_text":64,"locally_persisted_complete":0,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":131}
---

# P2 — 两项已知解析缺口的离线修复

本报告属于 PR #7，基于 PR #6 合入后的 work `474992c2664fb2af06765abdb4dfb23b6db40fb8`。集合仍为 215 条，其中 131 条非 repo、84 条 GitHub repo 排除在正文完成分母外。只改变 `arxiv:2406.04268` 和 `arxiv:2502.18864` 的派生文本及必要聚合；来源网络获取为 0。P1 的 `coverage-baseline.md` 是历史快照，本文件和当前 coverage ledger 承接 P2，不把旧核验冒充本次新核验。

## Before / After

| 来源 | Before | After | 仍未解决 |
| --- | --- | --- | --- |
| arxiv:2406.04268 | `.txt` 实际是 TeX root，但没有 normalized document；32 source selectors | 从原 `main_clean_arxiv.txt` 生成 normalized TeX 和可读正文；60 selectors，原 32 条不变；实际没有 input/include 正文边 | 三幅引用图未保留，`vN` 未固定；纯文本数学表达有损，TeX 原件仍在；保持 partial |
| arxiv:2502.18864 | 固定 v2 PDF 已完整留存，157 页中 155 页可提取文本；4／20 页仅图像 | 原 PDF 保持；另存页 4 图中文字与页 20 八幅图标题／轴名称；155 原生 page selectors 加 4 个派生 line selectors | 不重建版式、箭头、坐标刻度或散点数据；无传统 OCR，不宣称 extraction complete |

2406 的规范化正文为 70,717 bytes／70,713 characters／272 lines。其 normalized TeX 与原 root 字节相同，包含图注、主文与三节附录，但没有获取缺失图资产。增加的派生文本不是新的外部来源。

2502 转录为独立 `derived/image-pages-transcription.md`，不混入原生 PDF 提取层。方法是代理视觉转录（agent visual transcription）；服务端模型版本未暴露，明确记 `not_exposed`。使用本机 Poppler `pdftoppm` 26.05.0 以 240 dpi 检查页 4 分块、180 dpi 检查页 20。临时渲染不作为仓库源文件；原 PDF 是永久依据。独立 evaluator 已逐图核对 101 个列表条目、八个组合标题及轴名称，视觉子范围 PASS。

同步 2502 唯一 metadata 的 `rights.redistribution_package.modifications/scope`，只描述新增派生层；许可、固定版本、revision 和公共发布门控不改判。原生 `document.txt` 仅末尾 attribution footer 随说明更新，notice marker 前 155 页内容逐字节不变。

## 规划—执行—独立评价（planner–executor–evaluator）

1. Planner 从原源文件定位 `.txt` root、实际零 include 边，以及 PDF 两页的图像内容；没有用 full_text 标签代替阅读。
2. TeX executor 只拥有 materializer、对应单元测试及 2406 capsule；主线程拥有 PDF 转录、唯一 metadata 说明、聚合及 demo；coverage executor 只承接读写边界明确的台账和只读 auditor。没有多人同时改同一个 manifest/index。
3. PDF 选择视觉转录而不是安装 OCR 框架：两页边界已知、可逐项核查；不从曲线和散点猜实验数值。为远程继续工作，正文与溯源说明都留在 repo。
4. Independent evaluator 不参与实现，先审核图片与转录，再审核 exact head/base 的诉求满足、代理式执行（agentic execution）、核心质量。其反馈发现辅助 TeX 文档误入 root 候选、偶数反斜杠后的注释处理问题；executor 已据此修订，须再独立复评，不以 CI 绿色替代判断。按明确内容/历史证据排除辅助文件后，仍然存在的真实多稿保持歧义；取得新 payload 后先在内存检查，无法确认唯一 root 时抛出显式错误，保留既有 normalized 胶囊，不由异常兜底清空。注释判断按连续反斜杠奇偶共用，2406 正文经新旧比较不变。导言区语义摘要（preamble abstract）不扩写解析器，明确产生遗漏诊断，而非宣称全格式无损。
5. 本地门控首先拒绝新增的非原生页定位（`ARXIV_PDF_NON_PAGE_SELECTOR`）；这是真实失败记录。修订严格区分 manifest 声明的图像转录定位和原生 page 定位，保留原始页数、missing-page 与所有路径/范围门控，不跳过检查。新校验还要求派生方法、文件、source page、URI 行范围与同段 preview 一致，所有声明转录页必须被有效 selector 覆盖；原生 155 页加合格派生 4 条才等于全部定位。

## 全局派生与状态边界

全量 215 个 manifest 输入既有 registry/index/audit 生成器，避免仅用两个 UID 重建时截断其他来源。2406 属于现有 36-source demo，所以沿既有构建链重放：新增一个来自真实正文的有界摘录（bounded excerpt）候选，claims/evidence 从 71/71 变为 72/72，Wiki 134 页变 135 页；无 trusted 晋级。2502 不在所选 demo 中，没有人为添加其 claim。

现有构建身份会传播到 release manifest、页面 frontmatter、队列和 context pack，因此大量 Wiki 文件只有必要的 build identity 同步；没有手工改写生成页面来凑通过。其余 129 条非 repo 正文、全部 84 个 repo capsule 都未改动。

## 验证与放行

以下为冻结代码与产物的本地验证；报告不构成 merge 授权。最终 head、CI run、三维独立结论记录在 PR #7 review/body，避免为自指 head 反复提交。命令均用 `PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python`（Python 3.12.13，与 CI 一致）；远程使用仓库锁定的依赖。

- 原件保护：2406 原 7 source 文件及 `files.jsonl`、2502 原 PDF 与 P1 基线逐字节一致。
- 幂等性（idempotence）：两目标 capsule 各两次离线 finalize，结果一致；PDF native text marker 前不变。
- `make test`：67 项 PASS，其中 materialization 42 项。新增正负例包括真实多 root、standalone/模板/历史辅助文件、注释反斜杠奇偶、缺失/循环/深层 include、payload preflight 保留现存文件、preamble abstract 诊断；PDF 转录来源/文件/范围/同段 preview/native coverage，以及“删除某个声明页但调整总数”仍失败。
- `make validate`：PASS；215 metadata／215 manifests、2,849 个既有校验文件、21,499 selectors，43 篇 docs，36 demo sources／72 claims／72 evidence／135 pages，0 warnings／errors。该命令含单独物化完整性校验，不把结构 PASS 当作语义完整。
- `make demo`：PASS；完整重建至 `build:llm-wiki-v0:bfe1ec178597b638`。
- `make reproducibility`：169 个生成文件在提交树重放、完整 demo 重放、仅 compiler 重放均逐字节相同。
- `python -B scripts/audit_non_repo_coverage.py`：PASS。完整 staged `git diff --check` 在两份新增 normalized 文件报告源文本继承的行尾空白；此前工作区检查没有覆盖已暂存的新文件，不能当全量 PASS。为保持 normalized TeX 与 retained root 字节一致、避免为格式清理改动来源表达，本批明确保留这两份派生文本的空白；其余差异执行 `git diff --cached --check -- . ':!materialized_sources/corpus/arxiv-2406.04268--ce5afac4/normalized/document.tex' ':!materialized_sources/corpus/arxiv-2406.04268--ce5afac4/normalized/document.txt'`，PASS。没有关闭 CI 或内容/定位校验，独立 evaluator 需知悉此范围差异。
- 独立审核与最新 CI 全 PASS 之前保持 Draft，不 merge。

## 未完成事项

P2 不是全 corpus 完成。131 条目标的未决项仍按覆盖台账推进 P3；P1 的 unknown 表示尚未证明，不等于没有数据。两个已知解析缺口修复／评估后不自动宣称其来源 complete。许可门控与知识准入各自独立，不借正文修复放宽任一门控。

当前 action bucket 的唯一计数迁移为两例均进入 `needs_boundary_verification`，88→90；原件和文本完整度计数不变，`unresolved=131` 也不变。它们的实际可读性改善由 before/after 和新证据说明，不靠状态升级制造完成感。

阶段约束：当前 auditor 使用 P1 collection anchor 的 Git 历史和 P2 execution base 祖先关系。它验证当前 work 链，不是 squash 到 main 后的吸收证明；P4 必须显式升级该历史依赖，P5 用最终文件树／manifest 与 fresh checkout 验证，不能把祖先检查失败当作数据消失，也不能跳过验证。

本次尚未进入 main；PR #1 及 Issues #3/#4 继续 open。下一批只能在本 PR 合入最新 work 后创建，并沿一个 action bucket／一个 adapter family／最多 10 UID 的边界推进；不再创建第二条长期整合分支。
