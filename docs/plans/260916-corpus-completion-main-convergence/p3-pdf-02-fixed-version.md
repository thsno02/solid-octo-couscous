---
phase: "P3-PDF-02"
base_sha: "3a69c2f2550ed2159d365605b3f4df96cc30dc01"
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
    complete: 17
    metadata_only: 15
    partial: 8
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
    ocr_assessment: 11
    open_fulltext_fetch: 6
    parser_only: 1
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

# P3-PDF-02 — 七篇固定版本官方 PDF 补充

本批为 PR #15，基于已合入 PR #14 的 work `3a69c2f2550ed2159d365605b3f4df96cc30dc01`；最终目的地仍为经 P4/P5 验收的 main。本批内容已实现，当前仍待最终提交的独立审核与远程 CI；本记录不是 main 完成证明。

## 规划（planning）

P3-BOUNDARY-01 已核实七篇已有 TeX 缺失 62 个实际科学图件。比较继续扩写 TeX 解释器、仅保留缺口、补充同版本官方 PDF 三条路径后，采用已有 PDF supplement；不新增解析框架或默认 OCR，不改旧 source、normalized、selectors、NOTICE、files.jsonl、revision 与历史获取记录。

本批唯一 family 为 arxiv_latex_v2，唯一主要动作是 open_fulltext_fetch。明确范围是 WikiChat `2305.14292v2`、Self-RAG `2310.11511v1`、DiscoveryWorld `2406.06769v2`、Language agents `2409.13740v2`、OpenScholar `2411.14199v1`、Self-Evolving Agents Survey `2507.21046v4`、Recursive `2607.07663v2`。没有新 UID、引用网络、实验数据集、模型或仓库下载。

作品级许可已有证据，但旧 TeX 包的 allow 不自动移植到新 PDF：实际固定版 PDF、可见独立信用、表示范围和新归属包须分别核对。DiscoveryWorld 与 Language agents 沿 CC BY-SA 4.0；WikiChat 沿已有作者 camera-ready 映射及 ACL 作品授权，保留 Wikipedia/USGS 独立信用，不把 arXiv nonexclusive 当公开许可。

## 执行与核验（execution and evaluation）

启动时尚未获取七个新 PDF。随后七次固定 PDF 请求均 HTTP 200、application/pdf，最终 URL 与固定请求 URL 相同，无 latest 或其他出版 PDF 回退。批次请求前记录时间为 2026-09-16 19:03:06 UTC，全部成功完成的确认时间为 19:04:05 UTC；以此确认时刻作为 retrieved_at，不编造逐传输结束时刻。

| UID | 固定版官方原件 | bytes | 页数 |
| --- | --- | ---: | ---: |
| arxiv:2305.14292 | [WikiChat v2](https://arxiv.org/pdf/2305.14292v2) | 1,147,873 | 27 |
| arxiv:2310.11511 | [Self-RAG v1](https://arxiv.org/pdf/2310.11511v1) | 1,405,127 | 30 |
| arxiv:2406.06769 | [DiscoveryWorld v2](https://arxiv.org/pdf/2406.06769v2) | 3,054,585 | 29 |
| arxiv:2409.13740 | [Language agents v2](https://arxiv.org/pdf/2409.13740v2) | 1,784,943 | 25 |
| arxiv:2411.14199 | [OpenScholar v1](https://arxiv.org/pdf/2411.14199v1) | 3,888,524 | 53 |
| arxiv:2507.21046 | [Survey v4](https://arxiv.org/pdf/2507.21046v4) | 5,726,709 | 77 |
| arxiv:2607.07663 | [Recursive v2](https://arxiv.org/pdf/2607.07663v2) | 5,049,523 | 44 |

七个官方固定版本 abs 页面在本批另行实时核对了题名、作者与版本，点击许可链接确认：Self-RAG/OpenScholar/Survey/Recursive 为 BY 4.0，DiscoveryWorld/Language agents 为 BY-SA 4.0；WikiChat 为 arXiv nonexclusive，其公开再分发依据仍是既有作者 camera-ready 映射与 ACL 作品许可，而不是该 arXiv 授权。[ACL 作品记录](https://aclanthology.org/2023.findings-emnlp.157/)及[版权说明](https://aclanthology.org/faq/copyright/)亦在本批复核。没有新增引用作品或数据集获取；以上请求计数不冒充所有 GitHub 状态、许可页查询和工具调用总数。

执行期据 DiscoveryWorld 实物发现具体素材信用后，只追加查看权利人 PixyMoon 的入口及 [Cute RPG World 产品许可页](https://pixymoon.itch.io/2d-topdown-cute-rpg-world)：允许个人／商业项目使用和修改，要求署名，不允许转售素材包。论文明确声明已购买素材；本批保存的是作品整体中已合成的场景截图，不是提取、购买或公开底层素材包。不把该素材改称 BY-SA，不给被引程序／图形资产作无限授权。具体第三方信用连同作品 BY-SA 的适用范围分别记录；这是 agent 基于证据的表示准入决定，不是人类批准或法律保证。

取得原件后，各内容执行者已核验首中尾、62 个科学图的实际页映射、全文与附录边界和具体提取损失，见下文。主线程另实际渲染查看了两项 selected 来源（DiscoveryWorld／Survey）的首页，确认其摘要、版本边栏与所给连续行范围。完整原件（original artifact）不等于无损文本（text extraction）；上述内容审读不是最终精确提交的独立评价。原件缺陷、文本损失、访问失败与公开持久化未知分别记录。

只允许既有 DiscoveryWorld 与 Survey 的所选摘录切换到经过正文质量审核的父论文首页 PDF 表示；不新增知识主张或 trusted 晋升。最终重放、当前 CI 与精确 HEAD/BASE 的独立 evaluator 三维 PASS 后才正常合入 work；本批不宣称 main 完成，不关闭 Issues #3/#4。

## 本批内容审读证据（content evidence）

### WikiChat v2

27 页全文审读，实际查看渲染页 1、2、7、14、15、16、17、20、21、22、23、25、27，p21 另用高分辨率。首页四作者、题名与 v2／2023-10-27 边栏对齐旧 TeX。主文 pp1–9；限制、伦理、致谢 p10；参考文献 pp10–14；附录 A–F 延伸到 p27。六段对话为 Tables 4–9（p15/16/17）；八套 listing 为 Tables 16–23（p22–27），最后 Table 23／Stage 7 在 refinement 提示反馈引导句后结束。论文主动节选 few-shot 示例，不是授权补抓外部完整代码仓库的缺口。

五项科学媒体映射：`images/pipeline.pdf` → Figure 1／p2；`user_study_ui.png` → Figure 2／p20；`user_ratings.jpg` → Figure 3／p20；`scale.pdf` → Figure 4／p21；`scale2.png` → Figure 5／p21。图中箭头、七阶段流程、UI、箱线图和判断示例真实可见，不是只有图注。Figure 4 原有 literal HTML 标签、Figure 5 截取的部分证据界面原样保留，不修图、不追抓图外段落。

PDF 恢复旧 TXT 丢失的系统名、p7 表格行名与 ±、p19 κ、对话说话者、Jinja 语法。新 plain 仍有实质损失：p21 仅有 243 字符的两段图注，Summary／Workflow／规则／Ronaldo 段落全未进入文本；p20 UI 及箱线图分布、pp16–17 高亮范围、p2 箭头颜色关系仍丢失；p22 变量被插空格，不能把 listing 当精确可运行模板。

新 PDF 保存了旧六页 Wikipedia 表达之外的四项实际引用：p2 Figure 1 的 Christopher Nolan、Oppenheimer (film)、Cillian Murphy，以及 p21 Figure 5 的 Cristiano Ronaldo。新包必须为十页表达保留 Wikipedia contributors／页面和 history URL／BY-SA 4.0；既有 USGS credit 保留，但不声称该 PDF 本身已显示 Wikipedia 许可或 USGS 声明（并未显示）。论文 BY4、独立表达 BYSA、USGS 自有公有领域材料分开，不重许可整篇论文或整库。p10 LLaMA 原模型许可提示不外推到本 PDF，也不获取模型。

### Self-RAG v1

30 页，同版首页五作者、活动标题和 v1／2023-10-17 边栏匹配。实际查看 1、2、4、5、6、8、9、10、11、16、17、18、19、22、24、30。主文 pp1–10，伦理／致谢 p11，References pp11–15；p16 附录目录 A–D，完整到 p30 Table 12 Tokyo utility=3 示例及解释。PDF 恢复 reflection tokens、critic 指标、模型名与书目；p4 Table1／Algorithm1、p6 评分分式、p18 Fig5、p19 阈值及末例均实读。

七项 `source/figs/` 科学媒体映射：`teaser_self_rag_v8.pdf` → Fig1／p2；`training_examples.pdf` → Fig2／p5；`soft_alignment.pdf` → Fig3(b)／p9；`tradeoff_fever.pdf` → Fig3(c)／p9（图实际 PubHealth／PopQA）；`PopQA_scale.pdf` → Fig4(a)／p10；`med_scale.pdf` → Fig4(b)／p10（实际 PubHealth）；`ASQA_Prec.pdf` → Fig4(c)／p10。以实际图义为准，不拿文件名推断数据集身份。

新 plain 的分式仍扁平化，训练示例阅读次序交错；箭头、颜色、候选绑定和曲线点位并未等价文本化。原稿 s(ISREL) 用于 ISSUP、额外括号、p17 的 `1,2594` 均忠实保留而不静默纠正。p11 IBM／Stability AI／Microsoft／DARPA／NSF／AI2 资助信用保留。全部页文字信用扫描及全部科学图视觉未见相反许可声明；BY4 正证为既有固定版本许可及本批官方 abs 链接，不声称 PDF 印了 BY4 声明。

### OpenScholar v1

53 页，首页25作者逐名匹配 metadata，v1／2024-11-21 边栏明确。实际查看 1、2、4、9、11–14、18、25、27、32、37–53；p37/38/40 另高分辨率复核。七节主文、局限、贡献／致谢至 p18；References pp19–24；p25 附录 A–E 目录，训练／rubrics／UI／长回答及 QA 示例完整到 p53 Figure20。p18 Joseph Chee Cheng 与首页 Chang 差异是上游笔误，不改作者身份记录。

26 项 `source/figs/` 科学媒体映射：

| 文件 | PDF 实际图／页 |
| --- | --- |
| open_scholar_teaser_v6.pdf | Fig1／p2 |
| scilit_method_details.pdf | Fig2／p4 |
| scilit_example_figure_v2.pdf | Fig3／p9 |
| top_n_accuracy.pdf；top_n_citation.pdf | Fig4(b)/(c)／p12 |
| human_eval.pdf | Fig5／p14 |
| subjects.pdf；duration.pdf | Fig6(a)/(b)／p27 |
| data_distribution.pdf | Fig7／p32 |
| interface_1.png；interface_2.png | Fig8／p37；Fig9／p38 |
| paper_distributions.pdf | Fig10／p38 |
| gpt4_fluency.png；llama3_fluency.png | Fig11(a)/(b)／p39 |
| gpt4_relevance.png；llama3_relevance.png | Fig12(a)/(b)／p40 |
| gpt4_prometheous_sufficient.png；llama3_prometheous_sufficient.png | Fig13(a)/(b)／p40 |
| gpt4_overall_usefuleness.png；llama3_overall_usefulness.png | Fig14(a)/(b)／p40 |
| scholarbench_single_qa.pdf | Fig15／p46 |
| scholarbench_example_1v2.pdf 至 scholarbench_example_5v2.pdf | Fig16–20／p49–53，一一对应 |

p1 两装饰图标另列而不虚增科学图数。p11 Table2、p14 Table4 的完整指标与 p42/p45 µm 已恢复；p13 不含旧 if0 隐藏块。p46 三例、p47 supporting quotes、p48 Bio query／Inspiring Paper、p49–53 完整例图均实读。新 plain 仍有具体缺口：p37 UI 仅提取 70 字符的页眉／图注／页码；p39–40 八个 raster 矩阵坐标、格值与色阶未提取；p53 Input→Answer→Citations 的视觉阅读次序被打乱。42 条 CFF 字体警告单独记录，不将警告计数当缺页证据。

Figure10／p38 原图 v2 October2024／v3 January2023 图例与更新叙述相反，属于原作品内容不一致，而非本批 v1 身份冲突；保留，不改图。例图主动省略更多引用，不授权补抓外部论文。p18 贡献／资助、p31 Table9 adapted from Yue 等、p47–53 引用／Inspiring Paper 信用保留；p17 版权保护讨论不是该 PDF 的反向许可。全文信用扫描和26图视觉未见独立许可例外；作品 BY4 不外推被引全文、模型、数据或组件。

### DiscoveryWorld v2

29 页，八作者、v2／2024-10-07 边栏与旧源匹配。实际看渲染页 1、2、3、9、13、15、18、23、26、29；逐页正文和全部附录核验。主文 pp1–9、36 条 References pp9–12、完整 Checklist p13、附录 A–F pp14–29。活动摘要为120 tasks，p5 的 8×3×5=120 与之相符，正文24是任务模板数，不能误判为旧隐藏摘要。行动表14动作加两种 teleport、单位任务及对象属性、ReAct／Plan／Hypothesizer JSON／记忆／成本／评分案例和人类实验边界完整。末页 Save failures 明示 Windows 自动保存未解决、少量参与者数据丢失未纳入分析，不补造数据。

四项科学媒体：`figures/planetx-1c.pdf` → Fig1／p2；`discovery-figure-1c1.pdf` → Fig2／p3；`scenario-unit-tests.pdf` → Fig3／p18；`frame_1.png` → Fig4／p29。环境地图、发现流程、十任务场景及 RocketScience GUI 均看见真实图面。旧宏导致的环境名、Checklist Yes／N/A、JSON 花括号、乘号和金额恢复；但 p29 GUI 的 Arg1/Arg2、物品栏、Turn2 等没有原生文字，箭头、颜色与空间关系也有损。JSON 跨页有页眉页脚，排版反引号不等于可直接解析执行的代码。

现有 plain 得1569行，父首页摘要连续 L11–31，L10为标题、L32起 Introduction；L44 Apache-2.0 脚注仅指代码，不当论文许可。最后实质行 L1566–1568，L1569为页脚。p9 CuteRPG/PixyMoon 购买与署名要求、作者／OpenAI DALL-E 科学主题增改均保留，p13指向资产许可；PDF 未独立声明底层素材再许可授权。按上文具体权利人页面核验，仅把原作品中的合成截图保存在完整 PDF，不把底层素材包另存或改称 BY-SA。

### Language agents v2

25 页，九作者与 v2／2024-09-26 边栏匹配。实际查看渲染页 1、2、4、6、8、13、15、16、18、25，逐页正文与全部 SI 核验。主文 pp1–9含 Conclusions／Data Availability／作者贡献／致谢／competing interests，43条主参考文献至 p12；完整 SI/Methods pp12–25，包括参数与提示词、p15比较表、p16的15步 Algorithm1、p18泛化表、WikiCrow/ContraCrow方法、两套人类指导及20条SI参考文献。末条是 GPT-4 technical report，新 plain L1238–1240，L1241为页脚。

六项科学媒体：`Figures/Wikicrow-Schematic.png` → Fig1／p2；`Wikicrow-PaperQA.png` → Fig2／p4；`Wikicrow-WikiArticle.png` → Fig3／p6；`Wikicrow-Contradictions.png` → Fig4／p8；`Wikicrow-Ablations.png` → Fig5／p18；`Wikicrow-LitQAtest.png` → Fig6／p18。六个实际图面完整，包括工具流／问答与证据／FAM83H文章／Likert及ROC／消融／解析器和块长度比较；不把装饰背景和非活跃JPEG算入目标。

新文本恢复 ±、希腊变量及大部分算法符号，p18三模型表数值可读；仍缺数学和图形结构：p16 Algorithm1第7步有 U+0000–U+0003 字形控制字符，Σ→P、括号与行结构失真；p15粗体、灰空格和列位置未保留；六PNG图内文字不完整，p4的CD8a及DOI、p6 keratinization、p8 Nuanced Agreement、p18的89.1/47.8均不在对应页原生文本。主文／Figure4 11点Likert与两指南仅10标签之间是原作不一致，保留不补造。作品BY-SA仅按许可范围处理，不外推 PubMedQA 数据集／底层摘要或代码授权。

### Self-Evolving Agents Survey v4

77 页全部渲染，实际查看 29 页：1、2、4、5、6、9、10、16、17、19、20、21、28、31、32、35、36、37、38、40、41、42、43、45、47、48、52、53、77。新完整题名、27 作者、v4／2026-01-16 页边版本与旧 TeX 相符。九章起页为 2、5、9、16、19、31、35、48、53；p53 Conclusion 后接 References，书目至 p77，末条为 Zweiger 等 Self-adapting language models；没有 Appendix。

八项外置科学媒体：`Figures/develop.pdf` → Figure 1／p2；`overview.pdf` → Figure 3／p5；`timeline.pdf` → Figure 4／p6；`when.pdf` → Figure 5／p17；`how_reward.pdf` → Figure 6／p21；`how_cross_dim.pdf` → Figure 7／p28；`where.pdf` → Figure 8／p32；`eval.pdf` → Figure 9／p36。Figure 2／p4 是已有内联 TikZ 分类树，不虚增外置缺图数。全部图非空、框和箭头可见；Tables 1–12 页码为 9、10、20、28、38、40、41、42、43、45、47、52。

现有 plain 提取得 4502 行，77 页 preview 非空且零失败，只是结构结果。父首页连续摘要为 L20–41（排除 L19 标题、L42 页码、L43 版本）。PDF／新 plain 恢复勾叉、实空圆及 FGT/BWT 核心；公式分数、上下标和求和仍碎裂。Figure 4 图内年、月、方法框未被提取；分类树父子关系、执行循环、分组和多轴关联不是线性文本可替代。原件 complete 与 text partial 分开。实际可见图表、首尾及全文可搜索信用检查未见新增许可例外；第三方模型 logo／名称不外推商标或被引作品授权，p2 Darwin 句归属纠正保留。

### Recursive v2

实际查看 PDF 1、3、6、7、8、13、17、18、22、27、30、44。首页三作者与 v2／2026-09-06 边栏对齐；内文 July 2026 是作品日期，不误报版本冲突。九节起页为 1、3、6、13、17、21、24、26、29；Conclusion／Data availability 到 p30，References pp30–44，[1]–[196] 连续，最后是 Paskov 等 Measuring biological capabilities and risks of AI agents，没有 Appendix。重复 References 标题原样保留。

六项科学媒体：`figures/Figure1.png` → Figure 1／p6；`map_landscape_v2.png` → Figure 2／p7；`deployment_self_evolve.png` → Figure 3／p8；`train_time_self_iteraction.png` → Figure 4／p13；`verification_hierarchy.png` → Figure 5／p18；`growth_timeline_v2.png` → Figure 6／p27。六图 raster 图内格子、坐标／legend、箭头和图例真实可见，非空无明显截断；这不宣称保存了独立 PNG 原文件的字节和 metadata。

现有 plain 产生 1936 行／144781 字符，44 页且零提取失败。p3 Table 1 四列五类数值恢复；p17 `~80%` 与 p22 `~$15` 在新文本保留，而旧 TXT 缺符号。但六图内部语义仍全部未提取，p27 图6只剩图注（图内 `501 in 2026Q2`、季度轴、双 panel、legend 全缺）；表格二维结构、断词／粘连、参考 URL 换行仍有损。作品自身 p26 把 share panel 误称 Figure 3，实际是 Figure 6／p27；旧 TeX 同样如此，是上游交叉引用问题，不修原件。官方 PDF metadata 直接声明 BY4，实际六图与首中末未见独立许可例外，不授权196篇引用作品、1250-paper 数据集或绘图脚本。

## 实现与回归边界（implementation and regression boundary）

新增七份官方 PDF 合计 22,057,284 bytes／285 页，分别伴随原生提取 TXT、285 个逐页定位器与作品级 NOTICE。保留原 87 份 source 文件、492 个旧定位器；执行者与主线程交叉检查七包共129份旧库存文件字节不变。七份 canonical metadata 与七份 snapshot 仅追加 `rights.pdf_supplement`；旧 manifest 除新 supplement 与相应库存／大小外逐字段不变，旧94项权利审计仅七项追加对应 supplement 对象，未重新授权旧源包。其他208个 capsule 未变；没有生产代码、测试、依赖或 workflow 修改。

复用既有 PDF helper；执行者禁用网络连接后两次重放七包均字节一致，七包表示与许可验证分别零错误、零阻断。新原件已实核62项科学媒体的作品内呈现，但不声称补回了原 TeX 所缺独立图文件。七项原件为完整、文本仍部分（partial）；Self-RAG 后续归入 parser_only，其他六项按实见缺图内文字进入有限 OCR 评估，而非承诺全部图义可无损线性化。

现有 demo 重建为 `build:llm-wiki-v0:052e92babb00da4b`，仍36来源、72主张、72证据、135 Wiki 页。`selected_sources.yaml` 仅 DiscoveryWorld 与 Survey 的表示、字节、版本及权利传播改变。源摘要范围分别 L11–31 与 L20–41；当前短摘录消费者实际选择 L11–14 与 L20–25，引用可回到父作品 PDF。72主张／72证据中各仅两条 source-excerpt 更新，其余70条（包括 collector-assessment）逐对象相同；135页中113页仅 build identity 改变，22页存在上述两源的内容、权利、版本或索引传播。短摘录沿用现有空白合并规则，仍保留 `end- to-end`／`increas- ingly` 的换行连字符损失，不宣称无损排版或另加修文算法。

本地 `make test` 的147项测试通过；`make validate` 全部通过：215 manifests、2960库存文件、23892定位器，文档51项，demo及release各零验证错误。OpenScholar 原生提取仍报告 CFF／可选 fontTools 警告，警告与上述文本损失如实保留，不声称原生提取无警告。完整可复现性重放、精确 HEAD/BASE 的独立三维审核与同提交远程 CI 另在 PR 留存，三者满足前不合并。

全量 `git diff --check` 实际退出2：四份新 PDF 原生 TXT（WikiChat／Self-RAG／OpenScholar／Survey）各有33／36／337／32处行尾空白，WikiChat attribution 多段字符串由现有 YAML 序列化器产生的空白行在 canonical／snapshot／audit 各13处。没有修剪源派生字节或改变既有序列化器以制造全绿；排除这七件已解释文件后 scoped diff check 为0，正文／结构验证不受此格式例外豁免。
