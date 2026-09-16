---
phase: "P3-TEX-02"
base_sha: "e36e117a9199f3e57a27f02a5cec93ae61507e92"
status: "local_validation_pass_pending_independent_evaluation"
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
    complete: 10
    metadata_only: 15
    partial: 15
    unknown: 91
  text_extraction_counts:
    complete: 3
    partial: 38
    unavailable: 15
    unknown: 75
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 3
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 76
    ocr_assessment: 5
    open_fulltext_fetch: 13
    public_persistence_decision: 2
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 43
  structure_only_full_text: 50
  locally_persisted_complete: 3
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 128
---

# P3-TEX-02 — Streaming 的保真阅读视图（faithful reading view）

本批为 PR #14，只处理 `arxiv:2606.09877` 的既有固定 v1。PR #13 已在 exact HEAD `ef152d0b6801e64a56d58f72f010ddce94420022`／BASE `f717a9922333c7b7960570dcd2f31fb79bf8e14f`、独立 COMMENT review 5226364239 三维 PASS 与 CI 35130748893 success 后正常合入 work，merge 为本批 base `e36e117a9199f3e57a27f02a5cec93ae61507e92`。父 PR #1 仍 Draft，main 仍 `99ce4670be91637209d67792de0962404fa96488`；不能将 work 内完成当作已入 main。

## 规划与纠偏（planner）

PR13 的逐节核验已证明：本地 v1 root 与旧 normalized TeX 逐字一致、没有实引图／章节缺源，原件完整；默认 TXT 却删除了公式／算法控制符、表中不确定性符号和 Exact Prompts 的占位花括号。72 条 bib 包含全部 54 个实引 key，但默认消费者只留下 bibliography 名称。此次没有必要重新下载，也不能只升级状态标签。

比较三条路径：直接将默认文档切为 raw TeX，会使现有自动摘句漏正文或误取隐藏段；继续增加删宏正则，会继续丢实质表达；全面安装转换器或构建 TeX 引擎，超出必要范围。选择显式 opt-in 的保守阅读视图：仅做可证明的有限静态转换，复杂数学、表格、literal 与未知语法保留原表达并说明限制，不执行 TeX。

曾考虑同批处理八篇 allow 材料的共同 secondary parser 问题；复核 03/06 的“一个主要 action bucket”约束后收缩到唯一 `parser_only` UID，其余七篇留在未来同一 `open_fulltext_fetch` 批中正常预处理、复用已验证能力。`8 parser → 7 fetch` 与 `1 parser → 7 fetch+正常预处理` 都是两个批次，后者无需改规则、改七项主桶或扩大当前生产范围。通用性通过任意宏名和结构的合成测试证明，不以额外生产 UID 回放冒充本批结果。

## 明确边界与责任（executor）

- 唯一 source：`arxiv:2606.09877`／v1，capsule `materialized_sources/corpus/arxiv-2606.09877--80ac4aba/`。
- 保留四个 `source/` 原件、`files.jsonl`、历史 retrieval／revision、旧 `normalized/document.tex`、`normalized/document.txt` 全部字节与旧 98 selectors；不删除、不改版次、不重新执行原论文代码。
- 只新增 `normalized/reading.md` 及其派生定位，将 chosen consumer 明确绑定该 view；保留旧表示作为历史回退。书目只使用本地 references.bib，不递归下载被引用作品。
- 一个代码 executor 独占合同内实现与合成测试；一个 packaging writer 仅同步本 UID 既有许可包的 modifications/scope；main 整合、逐章消费审读、运行限定回放、更新聚合及报告；coverage 最后唯一 writer；最终 evaluator 不参与写入。
- 保留原 CC-BY 允许依据、原作者／模板归属与完整 NOTICE，不重新调查组件、不增加许可结论。旧 TXT 尾注是历史表示，新 view 使用准确的派生与范围声明；不得将旧允许外推到新 PDF、图或其它 UID。
- 非 opt-in 来源的解析／消费行为和其它 214 capsules 不变。本 UID 没有当前 demo claims，不增加知识断言；若完整 index 作为 release 输入改变 build identity，只重放必要生成产物，不改其它 claims/evidence 语义。

## 六维 before／实际 after

| 维度 | Before | After（逐节内容核验后） |
| --- | --- | --- |
| 身份（identity） | arxiv:2606.09877 v1，既有官方绑定 | 不变；本批零新官方版本请求 |
| 原件（original） | complete / verified；1365 行 main.tex，无 input 或实引图，4 source | complete / verified；原字节不变，不新抓取 |
| 文本（text） | partial / verified；数学／算法／表／listing/bib/标题定位有具体损失 | complete / verified，仅指本固定 v1 的 chosen reading；旧 TXT 损失保留为历史 |
| 本地（persistence） | 已声明文件 present/tracked、98 source selectors 合法，complete_target_consumable=false | true；reading 实际消费、198 个有效定位、双禁网回放一致；不冒充 main fresh checkout |
| 公开（redistribution） | allow；既有 CC-BY-4.0、metadata CC0 分层包 | grant 不变，仅真实 modifications/scope 与四方包装同步 |
| 知识（admission） | 无 demo claim，未 trusted | 不变 |

## 内容验收点

源 main.tex 的八个主节、Proofs／Exact Prompts 两附录、14 对 table/tabular（14 个表及各自内层 tabular）、19 个方程环境、1 算法、5 个 listings 逐项对照。至少检查：

- L66 的 sqrt/log/epsilon；L207–211 的 AVR 分式与 indicator 条件；L238–241 的 regret 差项；L389–393 的 MSE 残差。
- L274–304 的 IF/FOR、阈值、比较、赋值与集合差；L1064 的 `3.87±0.95`。
- L1310–1330 精确 prompt 中 `{ticker}`／`{headline}`，及另外两个完整 prompt；百分号、花括号或假 include 不能被普通注释／展开破坏。
- 主文开头 L63–71、中段 price labels L602–608、尾部 WikiCompilation L1347–1363；三个嵌套 ref 证明标题 L1236/1270/1287。书目名称占位不能冒称本地 bib 已被消费。

通用合成测试覆盖任意名称零参宏／别名、空体单参宏、循环／重定义的保守边界、literal 与注释顺序、数学／表格结构、不从 fenced fallback 摘句、明确派生定位和重复回放不追加重复条目。不能通过硬编码论文 UID 或宏名来凑过。

内容 reader 还单列原稿已有问题（source-native limitations）：L715 的列规格为 8 而实有 7 列，L1021 的列规格为 7 而实有 6 列；保全实际表头／单元，不补造列。L1114 的 `sec:qa_finance` 在本 root 无对应 label；引用 key 原样保留，不伪造定位。L66/202 与 L524 对 epsilon 的表述不同，L555–559 的收敛表述与 L1292–1296 证明条件有张力；L1155 正文与 L1160 表注也不应由转换器统一。该层核验不承担论文科学结论纠错，不能将原文问题混记为提取丢失。

### 全文内容验收结果

独立于代码执行者的内容 reader 完整逐节阅读 source 和实际 chosen reading，并调用真实消费者；main 复核首中尾及消费入口。全文范围如下（不是抽样替代全读）：

| 范围 | source 行 | reading 行 |
| --- | --- | --- |
| Abstract | 63–71 | 6–20 |
| Introduction | 74–114 | 21–105 |
| Related Work | 115–181 | 106–197 |
| Problem | 182–262 | 198–350 |
| Algorithm | 263–515 | 351–740 |
| Theory | 516–581 | 741–840 |
| Experiments | 582–700 | 841–1042 |
| Results | 701–1173 | 1043–1701 |
| Discussion | 1174–1227 | 1702–1795 |
| Proofs | 1233–1299 | 1796–1876 |
| Exact Prompts | 1300–1364 | 1877–1958 |

19 个 equation、14 个 table 及其内部 tabular、1 个 algorithm、5 个 lstlisting 的完整原生块均在 reading 各出现一次并精确吻合。AVR 源207–211→reading251–255、regret238–241→304–307、MSE389–393→534–538；算法274–304→367–397、脚注305→403。五个 listing 对应502–519、663–674、1889–1909、1922–1930、1942–1954，literal 花括号与换行完整。表头／单元、`±`、multirow、校准区间、缺值符号、正负号及 synthetic／judge confound 限定均保留。七个数学宏和 multirow 定义在1963–1970；bib 全652行于1981–2632原样装配，72记录覆盖54个实引 key，明确可能包含未引用记录、不是作者排版 References。

首中尾真实消费为 source63–71→reading6–20、source602–608→863–875、source1347–1365→1935–1958。96个 root heading 全部在原顺序对应独立有界章节。100 个新增 derived selectors 包括文件范围和99个连续章节范围；章节从L6覆盖至L2633，零 gap，footer marker 在2636不冒充正文。94个正文标题带可选 `source_heading_line`；两处重复 Query set decomposition 不猜唯一源行，但各有正确 derived URI/range/preview/root provenance，人工映射 source222→reading279–295、source449→637–652。这是显式源行增强的限制，不是正文缺失。

因此 main 采纳内容 reader 的 `text=complete/verified`、`boundary=verified`、`complete_target_consumable=true`、`known_parser_issue=false`、`action_bucket=complete_verified`／`resolution=resolved`。限定为已逐块核验的固定 v1 prose＋原生 TeX 表达；不是视觉等价排版，不是通用 TeX 支持，也不是所有数学块可自动摘为断言。94 条保守 diagnostics 的实际原表达完整保留，不据其数量制造缺口；旧 TXT 缺陷仍保留在 history。身份、原件、许可、无 demo claim 与不 trusted 状态不变。

## 实际执行与验证

### 独立预审的实质纠偏

非作者 evaluator 在生产回放前通过内存探针发现两类阻断：含条件 `$p>0$` 的句子被拆成 prose／math fence／prose 后，摘句器会选出缺少条件的后半句；未支持宏的多段参数只在首尾 fenced，中间可能隐藏的历史断言却成为可摘正文。这不是格式问题，而是派生消费者引入的语义改变。实现已退回 executor，要求保留完整含数学段落、完整未知宏参数，而不是继续增加 TeX 解释能力。另检查宏星号及引用可选限定语不能被静默删除；未证明的形态应保真回退。修复和复核完成前不生成生产视图、不冻结、不合并。

随后，局部定义／已重定义命令不得绕过静态准入、注释内假环境关闭符、不安全多行标题、引用和 literal URI 参数的同类旁路也经独立探针收口。29 项 reading 测试及既有摘句测试通过后，第一次真实回放仍在 preflight 失败：root 选择前对所有 source 成员做条件遮罩，误将不参与候选的 `.sty` 模板中的条件声明当正文检查。失败发生于写入前；四个原件、files.jsonl、旧两种正文和旧 98 selectors 对 base 仍完全相同，没有生成 reading。继续退回 executor，仅按既有 `.tex/.ltx/.txt` 候选后缀先过滤，不实现模板语义；该场景须通过回归和真实重试后才能记录生产成功。

### 真实回放、消费与聚合

修正经过独立复核和 30 项 reading 回归后，main 实际执行 `replay_arxiv_tex_reading(record, manifest, generated_at=原 manifest 时间)`，再从磁盘载入后第二次回放。`fetch_bytes`、`prepare_capsule` 和旧 `write_arxiv_tex_derivatives` 均被替换为一经调用即失败，证明此次没有联网或清空旧表示。两次所有 13 个胶囊文件逐字节相同；四个 source 合计 146,294 bytes、files.jsonl、旧 TeX/TXT 含历史末注及旧 98 selectors 前缀均与 base 字节一致，revision/retrieval 不变。manifest 的固定时间仍为 `2026-09-13T17:19:33Z`，不是本轮获取时间。

实际新增 `normalized/reading.md`：133,557 bytes／132,540 characters／2,645 lines；其中派生正文与辅助层 2,633 lines，随后是唯一当前末注。100 条新派生定位使总数为 198；清单库存 12 个文件，另有 manifest，共 13 个胶囊文件，库存 local_bytes 为 638,317。source_paths 明确为 `source/main.tex` 和 `source/references.bib`；原文正文边界为 L59–1365。94 条保守回退／未展开定义诊断不被清零，也不等同于丢了 94 段文字；实际完整性由内容对照判断。

main 实际调用 `choose_local_document` 返回新 reading，并用 `source_excerpt(..., reading_view=True)` 读出 L24 Introduction 首句。整个 Abstract 因含数学限定关系被原样 fenced，自动摘句未拆取其残句。本 UID 不在 selected demo，该直接消费检查与“未改 demo claim”是两份不同证据；没有新增 claim 或 trusted。

既有许可 grant/gate 不变；canonical、capsule snapshot、manifest、rights audit 顶层包及其 observed 缓存共五份包装对象相等。只补当前 UID 的真实派生证据／stored paths，历史网络物化证据保持并明确与本次离线回放区分。该 UID 发布校验为 0 errors／0 blocks；全局仍有两项继承的包不一致（GraphRAG `arxiv:2404.16130`、CoScientist `arxiv:2502.18864`）和其它公开限制，不能称全语料公开门控已通过。其余 93 条 rights 对象不变。

沿既有聚合函数更新 index/registry/completeness，保持聚合固定时间 `2026-09-16T04:30:26Z`。215 manifests／2,932 个库存文件／23,607 selectors 全部通过；其它 214 capsules 无差异。全 index 是 release 输入，因此实际执行 `make demo`，新 build identity 为 `build:llm-wiki-v0:c186e07607708b1c`。selected_sources、72 claims、72 evidence 与 base 全文件逐字节不变；135 个 Wiki Markdown 与 base 的唯一差异为 build identity，绝非新增 135 页知识内容。

初轮工作树实际命令：`make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python` 共 147 项 PASS；`make validate` 全 PASS（215 metadata/manifests、50 文档、80 相对链接、Wiki 135 页，0 warnings/errors）；`make demo` PASS；全量 `git diff --check <base>` PASS。`make reproducibility` 也已完成：committed-tree、full-demo、compiler-only、read-only 四种回放均为 169 个生成文件逐字节一致。rights 审计头部和其它 93 个原始 YAML 条目块也逐字节相同。内容 reader、coverage 及最终 exact HEAD 复验分别记录后再进入关闭门控。

独立非作者 evaluator 对 final HEAD/BASE 的 requirements、agentic、core quality 全 PASS，且当前 pair CI success 后才 Ready／normal merge；预审通过和上述工作树验证均不提前替代最终审核。

覆盖台账（coverage ledger）只更新本 UID，保留 PR13 execution 及旧 TXT/parser 判断完整历史；其它130个对象及原始 YAML 块逐字节不变。默认 report-aware auditor 通过。实际总计仍为131非 repo／84排除；text complete 从2到3、partial从39到38，locally complete从2到3、unresolved从129到128，parser_only主桶清空为0。original complete10/partial15/metadata15/unknown91、content inspected43/structure-only50、public allow29/block65/unknown37、candidate30/trusted0/no-demo101不变。唯一完整性晋级来自本条真实内容验收，不外推到其它材料。最终差异170个路径全部在启动合同内，原件和旧 normalized 无差异。

## 明确未完成（non-results）

本批零下载／OCR／新许可调查，未修复其它七篇或 RARR/Zep，未新增 TeX 执行引擎、依赖或通用脚本框架；不改 workflow／保护，不删文件／分支，不强推或改写历史，不关闭 Issues #3/#4，不合 main、不晋级 trusted。text 状态由真实消费证据决定，整个 corpus 与父 PR #1 仍需后续完成。
