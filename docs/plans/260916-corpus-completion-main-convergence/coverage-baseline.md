---
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":27,"full_text":90,"metadata_capsule":14},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":1,"metadata_only":18,"partial":6,"unknown":106},"text_extraction_counts":{"partial":23,"unavailable":18,"unknown":90},"action_bucket_counts":{"access_restricted":7,"author_manuscript_fetch":2,"canonical_repair":8,"html_article_snapshot":14,"identity_or_version_ambiguous":2,"needs_boundary_verification":88,"ocr_assessment":1,"open_fulltext_fetch":6,"parser_only":1,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":26,"block":65,"unknown":40},"content_inspected_full_text":26,"structure_only_full_text":64,"locally_persisted_complete":0,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":131}
---

# P1 — 非 repo 正文覆盖基线（Coverage baseline）

本报告只回答“当前 repo 对每条目标文档实际保留了什么、哪些结论尚不能成立、下一步做什么”。**这是离线盘点，不是正文补齐，也不是 PR #1 的最终验收。**

## 执行范围与证据

- 计划：`nonrepo-materialization-main-convergence-260916`，阶段 P1，PR #6。
- 执行 base：`work/v0-meta-kb-initialization-demo-260910` @ `5458fbdffc95444cc26d5e9346fc2f9ab96e09c5`；规划 PR #5 已合入该基线。
- 唯一实现分支：`codex/p1-nonrepo-coverage-260916`，目标为 work，最终通过 PR #1 进入 main。
- [逐项机器可读台账](../../../raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml)记录完整 UID、目标/版本/边界、实际路径、六维状态、证据定位、限制与下一步。
- [只读复算器](../../../scripts/audit_non_repo_coverage.py)读取既有 metadata、manifest、index、registry、selectors、既有 rights audit 和 demo claims；不下载来源、不创建新的物化框架、不重新调查许可。
- 来源网络请求为 0。GitHub PR、分支和 CI 管理不是来源正文获取。没有更改 source、manifest、index、registry、selector、Wiki 或原始元数据。


## 复算结果

| 独立维度 | 实际计数 |
| --- | --- |
| 范围 | 215 总记录 − 84 GitHub repo = 131 非 repo |
| 既有内容标签 | 90 full_text / 27 excerpt / 14 metadata-only（不是覆盖结论） |
| 原件覆盖 | complete 1 / partial 6 / metadata_only 18 / unknown 106 |
| 文本提取覆盖 | partial 23 / unavailable 18 / unknown 90 |
| 全文内容检查 | 26 有具体内容/解析检查；64 未作正文开中尾检查 |
| 完整目标可消费已获证明 | 0（不等于没有可消费文本） |
| 既有公开再分发决定 | allow 26 / block 65 / unknown 40（独立于覆盖度） |
| 当前 demo claim 状态 | 30 个来源有 candidate；0 有 trusted；101 无 demo claim |
| 尚未全维完成的来源 | 131 unresolved；不声称 131 没有正文 |

覆盖、权利与准入维度的分母均为131，全文检查行的分母为90；原件 metadata_only 的18项与旧标签 metadata-only 的14项不相同，因为验证页/目录页/迁移页等也未构成目标正文原件。具体判定见每 UID 的证据与 limitation，不能把两列互换。

## 如何作出判断

先比较了三条路径：照抄 `full_text` 标签、继续零散许可审计、按目标正文逐项离线建账。选择第三条，因为前两条都不能回答正文是否完整；已有许可审计只作为独立维度引用，不替代获取结论。

事实探针（structural probe）覆盖全部 131 条；内容检查（content inspection）另有具体文件与行号，不把探针结果当人工通读。26 条现标 `full_text` 有内容/已知解析检查，另 64 条未完成正文开中尾检查、保守保留未核验。独立审核发现错作品后，又补扫全部 73 条 arXiv root 标题；标题对齐只能检查身份候选，不是完整正文验证。27 条 excerpt、14 条 metadata-only 均记录实际文本、错误页、获取错误或缺失证据；两个已知 parser 问题属于 90 条 `full_text` 内部，不另加分母。

`unknown` 表示尚不能证明完整度，不等于无数据。`partial` 需要具体缺口。`complete` 只用于有版本、目标边界及内容证据的单个维度，不自动推导整条来源完成。台账的 unresolved 不能解释为全部来源都没有正文。

## 影响执行顺序的发现

| UID | repo 中实际观察 | 结论与后续动作 |
| --- | --- | --- |
| `arxiv-1809.10697` | 元数据标题为 DyRep，实际 root 和 normalized 是关于深度非弹性散射的物理论文 | 明确记录作品身份错配并先修身份；当前 demo 没有引用该 UID，不能据此声称71条现有claim均受影响 |
| `paper:The-Basic-AI-Drives` | `document.md` 是防机器人验证页，不是论文 | 修正合法入口；不得把验证页算摘录正文，不绕过访问控制 |
| `standard:w3c-community-dpv` | 正文仅迁移提示 | 核对新官方入口与同一版本，再获取规范 |
| `standard:etsi-ngsi-ld` | 现存文本是目录列表 | 固定目标规范版本，不把目录页当标准全文 |
| `standard:odcs-3.2.0` | 文本明确自 v3.1 起各章节分别在独立页面，当前只保留定义首页 | 按 3.2.0 目标规范核对章节范围；不是全站镜像，也不能把定义首页当整份规范 |
| `methodology:linkml-schema-first` | 文档首页介绍和教程索引 | 明确目标文档边界，不把单页概览外推为完整文档站 |
| `vocabulary:schema.org` | Schemas 组织说明和类型入口 | 核对现有目标边界，不能以许可包装证明整个 vocabulary 已保存 |
| `standard:w3c-owl2` | 本地标题明确为 Document Overview (Second Edition) | 保留 Overview 与整个 OWL 2 文档集的差别，不静默扩展或缩小范围 |
| `arxiv:2406.04268` | `main_clean_arxiv.txt` 是正文 TeX，但原适配器未识别 root，normalized 文件不存在 | P2 识别正文结构并预处理；保留版本/图资产缺口 |
| `arxiv:2502.18864` | 原 PDF 已在 repo，157 页；文本仅覆盖 155 页，第 4、20 页无原生可提取文字 | 原件和提取分开；P2 判断图内文字与 OCR/转录需要，不伪造恢复结果 |

所有上述发现都在逐项台账中附本地定位。W3C 样本也记录了正文与规范版本、部分 References 空 heading、尾部引用导航污染及转换限制，不能只看文本长度。现有 HTML 提取器只选择部分元素，且没有原 HTML 快照可供本阶段重放对照；此处记录验证缺口，不在 P1 修改 parser。

TeX 中已确认正文引用但未保留的图资产属于原件覆盖缺口；排版模板、旧稿、第三方附带组件不被自动升级为正文需求，也不在本阶段删除。

## 六个维度的 before / after

| 维度 | Before | P1 After |
| --- | --- | --- |
| 身份与版本（identity/version） | 元数据、canonical URL 和本地 revision 分散 | 每 UID 显式记录；未记录的上游版本为 null 并附限制，不用 payload revision 冒充 vN |
| 原件覆盖（original artifact） | 容易由 full_text 标签推断 | 保留实际路径、缺失与核验状态；没有改任何原件 |
| 文本提取（text extraction） | excerpt/full_text 标签与 parser 状态混用 | 单列缺页、章节、错误及 OCR 状态；没有新增或修复正文 |
| 本地持久化（local persistence） | “有 capsule”常被解释为全部可消费 | 分别记录已跟踪文件、正文路径、selector 可解析性和完整目标可消费状态；结构可用不等于目标完整 |
| 公开再分发（public redistribution） | 容易用 block 数量代表数据缺口 | 引用既有 audit 与 revision 对应，不新增许可调查，不改 allow/block |
| 知识准入（knowledge admission） | 容易把 metadata verified 当 trusted | 只按实际 demo claims 汇总；没有 claim 的来源明确未生成，不编造 candidate/trusted |

## 验证与后续路由

执行命令（只读，不运行 materialize）：

```bash
python scripts/audit_non_repo_coverage.py --probe
python scripts/audit_non_repo_coverage.py
make validate
git diff --check
```

复算器检查 131/84 分母、逐 UID 与 repo 事实相符、证据路径/行范围、受控状态、人工检查最低覆盖及本报告 frontmatter 计数一致性。已有 materialization validator 检查当前 215 manifest、2,846 个清单文件和 21,467 个 selector；这些结构结果不是正文完整性证明。PR 的最新执行记录与精确 head/base 独立评估以 PR #6 为准，不能引用旧 SHA 的 CI 代替最新验证。

P1 合入后才启动 P2 两个已知解析项；然后按 action bucket 串行执行 P3，每批最多 10 个明确 UID、一个 adapter family、一个主要 bucket，从最新 work head 出发并回流 work。对身份/版本不清、访问限制或公开持久化未决的来源保留具体待办，不让它们吞掉其他来源的进展。

## Explicit non-results

- 未取得新的来源正文，未修复 parser，未进行 OCR，未重建 Wiki。
- 未更改公开再分发条件，未晋升任何 trusted claim。
- 未将 PR #1 标为 Ready，未进入 main，Issues #3/#4 仍 open。
- 未删除内容或分支、未改写历史、未修改保护。
- 全 corpus 完成度仍须由 P2/P3/P4 的具体结果核验；P1 或其 CI 通过不能关闭父 PR 的需求。
