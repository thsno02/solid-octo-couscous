---
phase: "P3-BOUNDARY-01"
base_sha: "f717a9922333c7b7960570dcd2f31fb79bf8e14f"
status: "boundary_inspected_pending_independent_evaluation"
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
    complete: 2
    partial: 39
    unavailable: 15
    unknown: 75
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 2
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 76
    ocr_assessment: 5
    open_fulltext_fetch: 13
    parser_only: 1
    public_persistence_decision: 2
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 43
  structure_only_full_text: 50
  locally_persisted_complete: 2
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 129
---

# P3-BOUNDARY-01 — 十篇既有 TeX 的正文与消费边界核验

本批为 PR #13，仅更新十个已有 UID 的覆盖判断与执行报告；不是下载批次，也不改写来源／派生正文。PR #12 已在精确 HEAD `b06dbf5515b2c23b01031ac163724622a0a4bf66`／BASE `448a0e7a421a2bf1a58c821e07d8673d5c89f09b` 的独立三维 PASS（COMMENT review 5225996674）和 CI 35126963225 success 后正常合入 work，merge 为 `f717a9922333c7b7960570dcd2f31fb79bf8e14f`。父 PR #1 仍 Draft，main 仍为 `99ce4670be91637209d67792de0962404fa96488`。

## 规划判断（planner）

已有 full_text 标签中仍有 59 项仅作结构检查；继续把未知（unknown）当缺失或完成都会误导下一步。比较三个候选：已有版本记录的 RAG／研究代理 TeX、Wikipedia 系列（已知某些本地 input 未展开及附录 PDF 缺失）、模型编辑论文（宏／表较复杂且多未记录 vN）。选择第一类，并从相同 family／action bucket 补足十项，以减少不必要的微型 PR；补入项有实际 metadata／目录证据，不按标题凑数。

全部为 `arxiv_latex_v2 / needs_boundary_verification`。九项无内容审读证据；Zep 有三个局部样本但未逐节比对。下面 vN 是既有 metadata 与所存快照的记录，本批零网络，不冒称已再次向官方确认版本。若本地证据出现不可判定的作品／版本冲突，须停止并报告，不能静默换作品。

| UID | 目标／既有版本 | 实际 root | 原件／文本 before | 公开状态 before | 当前知识 before |
| --- | --- | --- | --- | --- | --- |
| arxiv:2210.08726 | RARR / v3 | `arxiv-2210.08726--8e79abf3/source/main.tex` | unknown / unknown | block | 无当前 demo claim |
| arxiv:2305.14292 | WikiChat / v2 | `arxiv-2305.14292--5b8a65bd/source/main.tex` | unknown / unknown | allow | 无当前 demo claim |
| arxiv:2310.11511 | Self-RAG / v1 | `arxiv-2310.11511--2a23ab40/source/iclr2024_conference.tex` | unknown / unknown | allow | 无当前 demo claim |
| arxiv:2406.06769 | DiscoveryWorld / v2 | `arxiv-2406.06769--d1971e3b/source/DiscoveryWorld.tex` | unknown / unknown | allow | 2 candidate claims |
| arxiv:2409.13740 | Language agents achieve superhuman synthesis / v2 | `arxiv-2409.13740--66861ff1/source/main.tex` | unknown / unknown | allow | 无当前 demo claim |
| arxiv:2411.14199 | OpenScholar / v1 | `arxiv-2411.14199--e07b84a9/source/iclr2025_conference.tex` | unknown / unknown | allow | 无当前 demo claim |
| arxiv:2501.13956 | Zep / v1 | `arxiv-2501.13956--b93a114f/source/main.tex` | unknown / unknown | block | 2 candidate claims |
| arxiv:2507.21046 | Self-Evolving Agents Survey / v4 | `arxiv-2507.21046--f477f5c3/source/main.tex` | unknown / unknown | allow | 2 candidate claims |
| arxiv:2606.09877 | Streaming Knowledge Compilation / v1 | `arxiv-2606.09877--80ac4aba/source/main.tex` | unknown / unknown | allow | 无当前 demo claim |
| arxiv:2607.07663 | Recursive Self-Improvement / v2 | `arxiv-2607.07663--e2b770de/source/main.tex` | unknown / unknown | allow | 无当前 demo claim |

路径均相对于 `materialized_sources/corpus/`。公开状态独立于原件／提取覆盖，本批不重审许可；RARR／Zep 的 block 不解释为“没有数据”。当前十项都已有 normalized、selector、manifest 与 Git 内材料，不依赖临时网络下载作为内容起点。

## 执行边界（executor）

五组只读内容执行者各负责两 UID：RARR＋WikiChat；Self-RAG＋OpenScholar；DiscoveryWorld＋Language agents；Zep＋Self-Evolving Survey；Streaming Compilation＋Recursive Self-Improvement。逐节审读实际 root 与引用闭包、正文／附录／表／公式／例子及 citation support，核对 normalized TeX/text 和定位。main 归并判断，单独 writer 更新台账十项及 summary，不并行改聚合文件。最终另由未参与写作的 evaluator 审核。

判据是实质内容和边界，不是标题、文件体积或 selector 数量。需区分：

- 本地 source 已有、只是归一化未消费；
- 本地确实未保留被正文引用的图／章节；
- 身份或覆盖仍未核验；
- 排版依赖、旧稿、引用网络本不属于目标正文。

原件缺图不等于上游没有图；TeX 正文存在不等于数学、表和图都被纯文本完整表达。发现后续 parser、获取或图像消费任务只记录精确文件／章节及动作，本批不偷偷扩成修复批次。

## 实际内容结果

以下定位以各 UID 的 capsule 为根；`source/` 是保留原件，`normalized/document.txt` 简写为 TXT。`verified` 表示该覆盖判断已有实证，`partial / verified` 绝不表示正文完整。原件中存在的矛盾、笔误和缺句保留为来源局限，不由转换器猜测改正。本批没有新 GET，版本沿用既有绑定。

### RARR 与 WikiChat

两篇均 `original=partial / verified`、`text=partial / verified`，已完整审读现存主文、全部活动 include、附录、表／公式及完整提示例子。RARR 的 v3 来自既有 metadata，历史 archive URL 未带 vN，本批不将它改写为固定版本 GET，也未发现作品／版次矛盾；WikiChat 的既有请求／resolved URL 则都明确 v2。

RARR 30 个 TeX、29 次 include、48 个非 include 源片段全部按序进入 document.tex，无活动 include 残留；附录 A–E 与十套完整提示已读。首 abstract:5→TeX:131／TXT:121，方法名／全名却变为 `we propose ( )`；中 tab_main_results:26→TeX:541–542／TXT:490–491，NQ 数字保留而 RARR 行名消失；尾 fig_prompts:508→TeX:2053／TXT:1921，末套 GPT-3 QReCC 提示及图注仍在。`1_task.tex:21/36/52/58` 和 `2_approach.tex:67` 的五式在 TXT:186/201/218/224/343 丢指标宏名与集合／max／分式／求和语义。62 实引 key 均由 main.bbl 支持，缺 custom.bib 不等于缺参考数据；派生仍未拼入书目。

RARR 真正缺图为 `source/figures/` 下 7 件：`fate_api9e.pdf`、`fate_overview9d.pdf`、`fate_plot6tight.pdf`、`fate_e2e_barchart.png`、`human-vs-auto-eval2.png`、`human-eval-attribution.png`、`human-eval-preservation.png`。`tiger_emoji.pdf` 仅在未调用宏定义中，不计正文缺口。既有 block 原因为具体第三方摘录分发依据未闭合，主桶 `public_persistence_decision`；技术次级动作是同 v3 七图或完整表示获取，以及离线宏／数学／表／书目修复。不是访问失败，不开展新许可考古。

WikiChat 12 个 TeX／11 次 include、16 个非 include 源片段全部展开；主文、附录 A–F、六段完整对话和八套 listing 已读。首 abstract:1→TeX:146／TXT:101（TXT:99 为摘要标题，100 为空行，已纠正速报定位）；中 analysis:53→TeX:440／TXT:387，97.3 数字仍在但 systemgf 行名和 ± 消失；尾 appendix:539→TeX:1354／TXT:1259 为 Stage 7 最后提示图注。appendix:271–274 的 Jinja for/endfor 在 TXT:993–997 消失，双花括号变量亦被剥，模型宏使说话者／行名为空。64 实引 key 由 main.bbl 支持；anthology.bib.txt 是下载提示，不据此抓取整份文献库。appendix:252 明示原作主动节选 few-shot 示例，不属于缺失代码仓库。

WikiChat 真正缺图为 `source/images/` 的 `pipeline.pdf`、`user_study_ui.png`、`user_ratings.jpg`、`scale.pdf`、`scale2.png`。主桶 `open_fulltext_fetch`，限定同 v2 五图或完整表示；宏、数学、listing 与书目修复为第二动作。两篇 selectors 首中末按文件而非阅读顺序排列，部分只有标题，不是完整段落证据。`missing_sections=[]` 仅代表没有整节文件缺失；图像未取得，未评估 OCR，缺图与 parser_errors 另列。

### Self-RAG 与 OpenScholar

两篇均为 `original=partial / verified`、`text=partial / verified`。Self-RAG 根文件及全部 8 个 input、主文六节、伦理／致谢和完整附录逐段审读；OpenScholar 根与全部 9 个 input、主文、局限、作者贡献及长附录逐段审读。所有活动 input 已保留并进入 document.tex；已有 bbl 支持活跃引用，但尚未合入单一派生消费者，这不是缺少书目原件。

| UID | 开／中／尾证据 | 已确认的消费缺口 |
| --- | --- | --- |
| arxiv:2310.11511 | `source/iclr2024_conference.tex:172`→TXT:620；`source/sections/method_v3.tex:160`→TXT:865；`source/sections/appendix.tex:469`→TXT:1637 | 模型名、四种 reflection token 表头、critic 列名、人工评估行名丢失；加权评分的求和／分式／token 绑定损失；尾部 Tokyo 示例保留但 utility 宏名消失。两个历史题名均被输出，selectors 含模板与 3 个注释假标题。 |
| arxiv:2411.14199 | `source/iclr2025_conference.tex:147`→TXT:133；`source/sections/human_eval.tex:38`→TXT:684；`source/sections/appedix.tex:851`→TXT:1658 | 模型／数据名、12 个主表指标名、人评四项列名和长回答标签丢失；微米的 mu 被删成 m。`human_eval.tex:14–20` 的 if0 旧段落进入正文；selectors 含 5 个注释假标题。末尾多论文问答只有缺失图片的文件名和说明。 |

Self-RAG 的 7 个实质活跃缺图均在 `source/figs/`：`teaser_self_rag_v8.pdf`、`training_examples.pdf`、`soft_alignment.pdf`、`tradeoff_fever.pdf`、`PopQA_scale.pdf`、`med_scale.pdf`、`ASQA_Prec.pdf`。另外 3 个 omitted 未被活动正文引用，不扩大补取范围。

OpenScholar 的 26 个实质活跃缺图均在 `source/figs/`：`open_scholar_teaser_v6.pdf`、`scilit_method_details.pdf`、`scilit_example_figure_v2.pdf`、`top_n_accuracy.pdf`、`top_n_citation.pdf`、`human_eval.pdf`、`subjects.pdf`、`duration.pdf`、`data_distribution.pdf`、`interface_1.png`、`interface_2.png`、`paper_distributions.pdf`、`gpt4_fluency.png`、`llama3_fluency.png`、`gpt4_relevance.png`、`llama3_relevance.png`、`gpt4_prometheous_sufficient.png`、`llama3_prometheous_sufficient.png`、`gpt4_overall_usefuleness.png`、`llama3_overall_usefulness.png`、`scholarbench_single_qa.pdf`、`scholarbench_example_1v2.pdf`、`scholarbench_example_2v2.pdf`、`scholarbench_example_3v2.pdf`、`scholarbench_example_4v2.pdf`、`scholarbench_example_5v2.pdf`。两张活动装饰图标 `source/icons/hf-logo.pdf`、`github-logo.pdf` 单列、不计正文缺失；另 7 个非活动 omitted 不扩取。`appedix.tex`、`usefuleness`、`prometheous` 为真实文件拼写，不自动更正。

来源自身的异常（Self-RAG 数字 `1,2594`、公式／阈值括号；OpenScholar 237M/234M、2.2k/2,967 等不一致）不归因于转换器。Self-RAG 的 MAUVE bib key 大小写差异有现存 bbl 支持，不误报缺参考。下一主动作是固定 v1 的 `open_fulltext_fetch`（目标图件或完整原件表示），随后修复正文边界、宏／数学／表格／书目消费及 selector 语义；不因已经核查便声称修复完成。

### DiscoveryWorld 与 Language agents

两篇活动 root／include 全部逐节审读，去除展开标记／忽略空白后的 source 闭包与 document.tex 相同；原件和文本均为 `partial / partial_check`。这里保守保留 partial_check，因为未见缺失图的视觉内容，不削弱已确认缺口的实证。

DiscoveryWorld 的 root→`abstract/introduction/related_work/experiments/appendix.tex` 均在：任务／三项评测、实验、局限、动作表、八主题、63 属性、代理提示／记忆／评分、人类实验与 checklist 已读。首 `source/abstract.tex:2–14`→TeX:102–114／TXT:89–101，活动摘要为 120 tasks；中 `source/appendix.tex:82`→TeX:891／TXT:750 为 Reactor Lab；尾 appendix:718–747→TeX:1527–1556／TXT:1389–1430 为人类实验／保存失败／GUI，TXT:1432 后为 collector notice。

其 4 个科学图实缺：`source/figures/planetx-1c.pdf`（root:111）、`discovery-figure-1c1.pdf`（introduction:65）、`scenario-unit-tests.pdf`（appendix:99）、`frame_1.png`（appendix:744）。省略的 neurips 模板 PDF 不列目标正文。references.bib 虽不在，`DiscoveryWorld.bbl` 已覆盖全部实引 key，不能称书目原件全缺。派生只有 bibliography 命令／名称（TeX:735–736／TXT:585–586）。

DiscoveryWorld root:49 定义空体 `eat`，root:100–107 隐藏旧摘要却被 TXT:105–110 输出为第二份“24 scientific tasks”摘要；`env` 宏未展开使 TXT:75 题名失名；checklist 的 Yes/N/A 消失（root:533–583→TXT:596–647）；附录 Verbatim JSON 的花括号被删（如 TXT:984–1005、1306–1312）；乘号丢失（appendix:582→TXT:1251）。原稿晶体公式的异常保持为上游内容。74 selectors 中仍有旧稿／模板，不能把数量视为正文质量。

Language agents 的 root→`SI.tex` 全在，主文 LitQA2、工具／消融、WikiCrow、矛盾检测及结论，与 SI 全部配置／工具提示、引用统计／伪代码、人工评价、泛化及两套矛盾指令均已读。首 main:142–144→TXT:103–105；中 SI:165–209→TeX:434–478／TXT:385–427；尾 SI:501–518→TeX:770–787／TXT:724–741，TXT:746 后为 notice。

其 6 个科学 PNG 实缺，均在 `source/Figures/`：`Wikicrow-Schematic.png`（main:162）、`Wikicrow-PaperQA.png`（186）、`Wikicrow-WikiArticle.png`（213）、`Wikicrow-Contradictions.png`（232）、`Wikicrow-Ablations.png`（SI:263）、`Wikicrow-LitQAtest.png`（271）。两张活动背景 PDF 属排版，其余 5 张非活动 JPEG 不列正文缺口。`bu1.bbl`、`main.bbl`、references.bib 支持活跃引用，派生却仅留命令／名称。SI:186 完整分桶 comprehension 在 TXT:406 只剩 `B = ]`；希腊变量、赋值／集合／比较符丢失；SI:149 约定的“粗体为保留值”在 TXT:356–371 失去区别，灰空格变为色码；main:143 的 `2.34 ± 1.99` 在 TXT:105 失去 ±。28 selectors 的文件／标题点位可定位，但不等于正文段落范围。

两篇下一主桶为固定 v2 的 `open_fulltext_fetch`，仅补实际科学媒体或完整同版表示；随后修复已有书目、数学／算法／Verbatim／宏和正文边界。不递归获取外链评测数据、代码或引用论文。

### Zep 与 Self-Evolving Agents Survey

Zep v1 的 600 行 root、三结果表、五个完整附录提示逐段读完。无活动 input／include／import 或 includegraphics；`graphicspath{media/}` 不构成缺图。4 个源文件中 root 与 document.tex 逐字一致，28 个实引 key 都在本地 bib/bbl。因此原件为 `complete / verified`，文本为 `partial / partial_check`，不是 locally complete。首 source:83–92→TXT:71–75；中 source:270–328→TXT:274–318；尾 source:513–592 的 Temporal Extraction 九条规则→TXT:511–590，source:596–600 对应 TXT:592–595 的书目／结尾；notice 从 TXT:598 起。

Zep TXT 前 68 行是导言污染；source:104、106–108 的图结构符号在 TXT:89–93 丢失；source:154–161 的检索组合亦有损；source:302/308/315 的下降箭头与其他上升箭头在 TXT:297/303/310 被抹成无方向百分数。bbl 28 项存在但未内联。29 selectors 全为 source 文件／标题，非派生段落。source:124 的 `ntity`、133 的 `or each fact...`、383 的半句是原件本身缺陷，不补写或归因于 parser。

Survey v4 的 root、9 章、3 外置表与 math_commands 全部实读；13 条 input 边均展开，document.tex 与字面闭包相同，无遗漏 TeX、无 appendix 声明。12 表均在；183 行 TikZ/forest 路线图是内联代码，不误报外置图缺失。原件／文本保持 `partial / partial_check`。首 main:94–102→TeX:563–571／TXT:546 起；中 `source/tables/what_to_evolve_table.tex:17–20` 的实心／空心圆分类在 TXT:1003–1006 变空；`source/sections/evaluation.tex:36–37` 的 FGT/BWT→TeX:1806–1807／TXT:1685–1686，FGT 核心 max 差项被删除；尾 conclusion:1–4→TeX:2590–2593／TXT:2435–2438，TXT:2446 后为 notice。

Survey 8 个活动 PDF 实缺，均在 `source/Figures/`：`develop.pdf`（main:100）、`overview.pdf`（intro:44）、`timeline.pdf`（intro:62）、`when.pdf`（when:16）、`how_reward.pdf`（how:115）、`how_cross_dim.pdf`（how:263）、`where.pdf`（where:26）、`eval.pdf`（evaluation:7）。图注不能替代未见的关系与标签。TXT 导言和宏定义污染到 Abstract:546；比较表勾叉成为 mygreen/myred55，分类矩阵圆点消失，数学与内联关系树不可完整消费。135 selectors 仍只指原文件／标题。382 个实引 key 在 bib 中，但没有本地 bbl，派生也未装配书目。原 bib 的 `ma2025agentic` 在 L103/L2983 重复：同题名／标识、作者字段冲突；该 key 未被当前 root 活跃引用，不是 Survey UID 冲突，不选作者、不自行纠正。

Survey 下一主桶 `open_fulltext_fetch`（固定 v4 的 8 图或同版完整表示），parser 修复为第二动作。Zep 的技术路径无需重新抓正文，但既有 NC 用途事实未确认而 public=block；主桶选择 `public_persistence_decision`，离线 parser-only 是技术第二动作，未授权新公开派生。许可对象不修改，不把 block 说成获取失败。

### Streaming Knowledge Compilation 与 Recursive Self-Improvement

两篇 source/main.tex 与 document.tex 分别逐字一致；00README 均指定 main.tex 为 top-level，无 input／include／import 缺源。主文与全部 TXT 逐行对照；本轮只沿用固定 v1/v2 的既有来源绑定，不把文章日期当版次证明。

Streaming v1 原件 `complete / verified`，文本 `partial / verified`：1365 行 root 含八大节、Proofs 与 Exact Prompts 两附录、14 表、19 方程、1 算法和 5 listings，无外置实引图，4 个源文件已在库。首 raw:63–71↔TXT:63–71；中 raw:602–608↔TXT:632–638；尾 WikiCompilation raw:1347–1363↔TXT:1398–1414，raw:1365↔TXT:1416 为结尾，TXT:1419 后是 notice。

其原件齐全不代表 TXT 保真：raw:66→TXT:67 的 sqrt/log/epsilon 丢失；raw:207–211→TXT:215–219 的 AVR 分式及 indicator 条件消失；raw:238–241→TXT:249–252 的 regret 两组差项消失；raw:389–393→TXT:408–412 的 MSE 残差仅余 `^2`；算法 raw:274–304→TXT:286–316 丢 FOR/IF、比较和集合符号。raw:1064→TXT:1111 丢 ±；raw:1310–1330→TXT:1361–1381 的原样提示丢 `{ticker}`／`{headline}` 花括号，另外两提示同类。54 实引 key 在 72 条 bib 中，但派生只剩 plainnat/references。98 selectors 都在 source，93 个 root 标题点位缺三处嵌套 ref 证明标题，且包含 sty 模板 Acknowledgments。主桶 `parser_only`：仅从既有源修复保真消费、书目和正文定位，不需新获取。

Recursive v2 原件／文本均 `partial / verified`：2022 行 root 的九节、Data availability 与 References 齐全，无附录声明。首 raw:99–132↔TXT:96–129；中 SelfEval raw:1143–1205↔TXT:1158–1222；尾 Conclusion raw:1970–2008↔TXT:2000–2039，raw:2022↔TXT:2055 结尾，TXT:2058 后为 notice。

其 6 个活动 PNG 实缺，均在 `source/figures/`：`Figure1.png`（raw:419）、`map_landscape_v2.png`（484）、`deployment_self_evolve.png`（519）、`train_time_self_iteraction.png`（910）、`verification_hierarchy.png`（1232）、`growth_timeline_v2.png`（1822）。拼写按原件保留；未见图原件，不声称已读其像素或完成 OCR。唯一 longtable 的五类数字／百分比仍在，但有 minipage／列宽噪声；此篇没有实际 equation/align/algorithm/listing，不虚报不存在的数学块损失。raw:1165→TXT:1182 的约 80% 丢近似号，raw:1515→TXT:1539 的约 $15 丢近似与货币符号。196 实引 key 在 bib/bbl 中，但默认 References 只有占位名称。17 selectors 合法，却仅覆盖 36 个标题中的 13 个 root 点位；23 个换行标题没专用 selector，不等于原文缺章节。主桶 `open_fulltext_fetch`：固定 v2 六图及其图像消费／公开表示核验；随后整理书目、层级、符号，不自动将现存四文字成员许可范围外推到新 PNG。外链 1250-paper corpus 和绘图脚本属于研究数据，不获取或执行。

### 六维变更与下一步

本地持久化栏的 present/tracked/resolved 表示所有**已声明文件**存在、入 Git、定位范围合法，不代表未获取的图已在库或 selector 语义完整。fresh-checkout 本批仍 false；`complete_target_consumable` 从未判定 null 改为 false。身份栏的 vN 均保持既有绑定，original complete 仅对已审读的本地目标边界成立。十篇已确认 parser issue，全部仍 unresolved。

| UID | 身份 before→after | 原件 before→after | 文本 before→after | 本地 before→after | 公开 before→after | 知识 before→after | 主动作 after |
| --- | --- | --- | --- | --- | --- | --- | --- |
| arxiv:2210.08726 | 同 UID/v3→不变 | unknown→partial | unknown→partial | present/tracked/resolved；complete null→false | block→block | 无 demo claim→不变 | public_persistence_decision |
| arxiv:2305.14292 | 同 UID/v2→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | open_fulltext_fetch |
| arxiv:2310.11511 | 同 UID/v1→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | open_fulltext_fetch |
| arxiv:2406.06769 | 同 UID/v2→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | candidate 2→不变 | open_fulltext_fetch |
| arxiv:2409.13740 | 同 UID/v2→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | open_fulltext_fetch |
| arxiv:2411.14199 | 同 UID/v1→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | open_fulltext_fetch |
| arxiv:2501.13956 | 同 UID/v1→不变 | unknown→complete | unknown→partial | 同上 | block→block | candidate 2→不变 | public_persistence_decision |
| arxiv:2507.21046 | 同 UID/v4→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | candidate 2→不变 | open_fulltext_fetch |
| arxiv:2606.09877 | 同 UID/v1→不变 | unknown→complete | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | parser_only |
| arxiv:2607.07663 | 同 UID/v2→不变 | unknown→partial | unknown→partial | 同上 | allow→allow | 无 demo claim→不变 | open_fulltext_fetch |

实际下一决策优先于技术动作排队：两个 block 来源用公开持久化决策（public persistence decision）为主桶，但数据与 parser 问题仍实列；其它七个确证缺图来源用获取，Streaming 用 parser-only。不再把已定位的问题留在 needs_boundary_verification。本批没有依据或权限改动已有公开 gate。

## 文件、验证及关闭门控

唯一允许改动为本报告、branch ledger 和 `raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml`。其它 121 个非 repo coverage 对象／原始块以及全部 metadata、source、normalized、selectors、manifests、rights、index／registry、demo／Wiki 必须保持不变。没有正文获取请求，不把历史 retrieval 冒称本次 GET。

主线程在本批候选执行树实际运行 `make test validate reproducibility PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python`：114 tests 全 PASS；215 manifests、2931 inventory files、23507 selectors，零 warnings/errors；49 篇 docs／80 个链接；169 产物在 committed-tree/full-demo/compiler-only/read-only 四重放逐字节一致，build 保持 `ac56ea43f6b5393c`。这是本次实际执行，不借用 PR12 的测试。冻结提交后仍须在该精确 HEAD 复验并核对 CI；记录不提前宣称远端 success。

sole writer 在最终台账／frontmatter接入后实际运行默认 `scripts/audit_non_repo_coverage.py` PASS：215 总数、131 非 repo／84 排除；原件 complete 10／partial 15／metadata_only 15／unknown 91，文本 complete 2／partial 39／unavailable 15／unknown 75。内容检查 43、结构检查 50（Zep 本来已有局部证据，所以本批是增加 9 而非 10）；locally complete 2、unresolved 129、公开 allow/block/unknown 29/65/37、candidate 来源 30／trusted 0 均未变化。主动作 needs_boundary 76／open_fulltext_fetch 13／parser_only 1／public_persistence_decision 2，其它桶不变。

已核对其余 121 项逐对象及原始 YAML 块字节不变；十项 observed、身份／版次、public／knowledge 字段不变；PR12 execution 原对象完整入历史。writer 另核实 30 个首中尾范围、69 个实引缺图均未在本地，不把图注当图件；主线程修正 WikiChat 摘要空行定位。无 sources、metadata、rights、manifest、index／registry、代码、tests、workflow 或 demo/Wiki 差异。当前全部手写 diff 空白检查通过，没有 PR12 的原 HTML 空白例外。以上结构验证仍不替代本批逐篇正文审读。

最终精确 HEAD／BASE 的需求满足、agentic 判断过程与核心质量须经独立非作者 evaluator 三维 PASS，且同 pair 的 CI 成功，才 Ready 并 normal merge 到 work。GitHub 审核为 COMMENT，不伪造人类 APPROVE；任何 head／base 变化需重审。

## 明确未完成

本批不是十篇全文获取或预处理修复，不新增 parser／脚本框架，不修改记录版本／许可，也不开展组件考古。未知不自动降为 unavailable；缺口不被台账更新消除。不扩张引用网络、数据集、模型或 repo 执行。不合 main、不关闭 Issues #3/#4、不删文件／分支、不强推或改保护、不新增 trusted。父 PR #1、其他来源及 P4/P5 仍需后续完成。
