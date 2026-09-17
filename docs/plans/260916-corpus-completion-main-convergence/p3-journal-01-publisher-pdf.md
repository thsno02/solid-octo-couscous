---
phase: "P3-JOURNAL-01"
base_sha: "8d954a2f969475bb606229d5eae57427f47030a9"
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
    complete: 23
    metadata_only: 14
    partial: 8
    unknown: 86
  text_extraction_counts:
    complete: 3
    partial: 39
    unavailable: 14
    unknown: 75
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 3
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 76
    ocr_assessment: 16
    parser_only: 2
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


# P3-JOURNAL-01 — 六篇期刊论文的出版社正文表示

本批为 PR #16，基于 work `8d954a2f969475bb606229d5eae57427f47030a9`，最终目的地仍为经验收的 main。六篇的十一份表示已完成获取、内容审读与独立表示包装，旧摘录未获重新授权。当前仍待最终提交的独立验收与远程 CI；本记录不表示 PR 已完成或 main 已完成。

## 规划与边界（planning and boundary）

对比扩写网页提取器、仅保留旧摘录、取得出版社正式版本（Version of Record，VoR）三条路径，本批沿已有 PDF supplement 扩展期刊身份与离线重放。保持六个 UID、旧摘录、默认 selectors、NOTICE、原 revision 与历史获取记录；不伪造 arXiv 版本或 Git 提交，不新增解析框架、OCR、依赖或 workflow。

六个 UID 均不在当前 demo 的 36 个选中来源中。独立预核纠正了原先“更新六个已选摘录”的规划假设：本批只补材料，不新增选源，不改 72 条主张（claims）、证据（evidence）及 collector-assessment；消费者的正反向定向验证与生产选源分开。

官方页面核对发现，五篇 Nature 论文各有一份属于论文方法／结果边界的补充信息（Supplementary Information，SI）。在获取这些文件前，PR 合同已明确列出六个主 PDF 和五个 SI 的准确 URL 与单独保存路径。各文件独立保留原件、页文本、selectors 和授权，不拼接 PDF，不借主文许可自动放行 SI。数据 ZIP、代码包、视频、审稿文件、独立更正附件和站点镜像不在本批范围内。

A-Lab 选择当前更正版本：正式题名已由 novel materials 改为 inorganic materials；官方 2026-01-19 更正同时影响成功数、图 2 与 SI。只选择原论文当前主 PDF 与当前 SI，不选择更正页的 annotated uncorrected article。旧摘录与历史身份记录保留，不能静默改写为当前结果。[官方更正](https://www.nature.com/articles/s41586-025-09992-y)

## 获取证据（acquisition evidence）

本批 11 次列定 PDF GET 均一次成功：HTTP 200、application/pdf。请求启动前记录为 2026-09-16 19:58:09 UTC；全部结果成功完成的观察时刻为 20:03:25 UTC。使用观察完成时刻作 retrieved_at，不编造逐个传输结束时间。六个主 PDF 自然重定向至同一官方 host/path，附加 cookies_not_supported 与 code 查询参数；五个 SI 的最终 URL 等于合同 URL。须如实保留 requested 与 resolved URL，不将重定向伪写为无变化。

此前另有六次出版社 HTML 预核 GET，均 HTTP 200；HTML 仅供临时审阅身份、作者、许可和 SI 链接，没有将网页全文纳入 repo。本段 11 次只统计列定的本地 PDF 获取，不冒充此前浏览器工具访问、许可页与 GitHub 查询总量。

| 作品 | 选定版本 | 主 PDF bytes／页 | SI bytes／页 |
| --- | --- | ---: | ---: |
| FAIR | publisher-vor:2016-03-15;amended:addendum-2019-03-19 | 254,899／9 | 无列定 SI |
| AlphaTensor | publisher-vor:2022-10-05 | 15,314,954／17 | 1,037,875／30 |
| AlphaDev | publisher-vor:2023-06-07 | 3,077,082／17 | 2,404,602／28 |
| A-Lab | publisher-vor:2023-11-29;corrected:2026-01-19 | 10,411,037／12 | 7,477,648／44 |
| FunSearch | publisher-vor:2024-01-11 | 2,034,181／14 | 1,725,197／39 |
| Coscientist | publisher-vor:2023-12-20 | 8,869,905／13 | 3,183,870／52 |

FunSearch 的 online 日期 2023-12-14、VoR 日期 2024-01-11 和期刊期次日期 2024-01-18 是同一作品的不同出版节点，不据此另建 UID。FAIR 当前 PDF 首页明确 Amended: Addendum，故根据实物在公开持久化前细化选定版本；2016 是原出版日期，不声称取得未修订初版。其后续独立 Addendum 仅记关系，不扩展本批获取边界。

11 个已获取 PDF 合计 55,791,250 bytes、275 页。此处是原 PDF 合计，不混用未来 inventory／manifest／NOTICE／派生文本的总大小。FunSearch 的 VoR 日期另由官方页面 About this article 的 Version of record 字段确认，不单凭 PDF CreationDate 推断。

## 补充信息的许可边界（SI licensing boundary）

SI 未重复印刷 CC 段落，不自动等于必须重新获取五份许可文书。独立 evaluator 复核后认可有界证据链：各实际论文页面的 BY4 声明、该页面准确链接的正式 SI、附件同 DOI／题名／作者，以及每份附件的具体信用检查。每份表示仍须独立绑定 URL、实际版本、四方授权包与 NOTICE；不能机械复制主 PDF 的 allow。

当前[官方许可指南](https://www.springernature.com/gp/open-science/policies/journal-policies/licensing-and-copyright)提供所用示例；其[OA CC BY 4.0 示例 §1(a)](https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/27848838/data/v1)把 SI 纳入 Article 定义。这只支持出版社的公开范围释义，不声称六篇作者签署该 2026 示例，也不把模板当作品授权。预核期间曾查到的 Springer Healthcare CC BY-NC 表单不适用于此批，2012 Nature 表单也不作为六作品 CC BY4 的授权依据。

AlphaDev SI 第 19 页（印刷页 18）附录 G 代码实际包含 DeepMind 2022 版权与 Apache 2.0 **and** CC BY4 条件；该代码范围保留两套条件，不改成任选 OR，不外推其他 SI。完整原文 header 与 Apache 法条已随本表示保留。SI 范围预核不是最终发布验收；实际信用检查与包装已完成，独立最终审核仍是另一步门控。

## 内容审读（content review）

### FAIR

九页主 PDF 的全部 native 页与全部渲染页已由内容执行者审读。首页带 Comment 文体前缀，正文同 DOI；原出版日 2016-03-15、当前 Amended 标记分别记录。p8 的 53 位作者与官方 HTML 对齐，p8–9 的 47 是机构编号而非作者数。主线程另目视首页确认该修订标记与摘要。独立 Addendum 未获取，不能声称其全文已包含。

主文起于 p1 Supporting discovery through good data management；p2/4/6 的三个 Box 分别是术语、FAIR 全部 F/A/I/R 原则、示例项目，正文与框均有实质文字。p7 FAIRness 结论后接 References，p8 续最后两条，再接致谢、贡献、CC 声明、全作者；p9 正常结束机构列表，没有丢失的编号附录。外部 living document／项目是引用，不扩大为整站目标。

全部九页非空、没有提取异常，但仍为 partial：fi/fl 字形、异常词内空格、断行 URL、上标与页首 Box 的线性顺序有损。不能用九页非空宣称可直接解析全部 URL 或无损排版。p8 BY4 声明与官方作品页一致，全部九页未见相反材料排除；原作者、Lorentz／Dutch Techcenter／Netherlands eScience Center／Force11／BD2K／ELIXIR／BioHackathon 致谢与利益声明保留。页面 metadata 的 CC0 不外推论文正文。

### AlphaTensor

17 页主 PDF 加 30 页必要 SI 的全部 native 页已审读。主文首页与 SI 作者页同 13 位作者、同 DOI；online 2022-10-05 与 issue 2022-10-06 不混淆。主件 p1–7 为主文／五幅图／References，p8–10 Methods，p11 续书目与信用，p12–15 Extended Data Figures 1–4，p16–17 Extended Data Tables 1–2；不是到印刷正文末页 p7 就算全文。

SI 的 publisher 封面之后，作者正文依次覆盖 A 网络组件及 Algorithms A.1–A.13、B 分解等价与定理、C 卷积／DFT、D 实际运行时间评测、E border rank、F 消融、G 超参数、H 分治、I 证明；p29–30 为参考文献。主文明确依赖 SI 的具体算法与证明，因此五幅 SI 科学图及这份完整附件属于本次正文边界；外部 factorizations、notebook、GitHub 软件不属于这两份 PDF。

两份均无空页或提取异常，仍有明确科学内容损失。主件 p12–17 图内 47／76 条乘法、网络架构与结果／DFT 系数表没有进入 plain，只留下图注／表注；其他页的矩阵、颜色、求和和上下标也不保真。SI 多页正常数学括号变控制字形，求和变 P/X，p16 代码失去词内空格与缩进，p19/21–22/27 的矩阵／分块／高亮关系不能按线性文字重建。不执行或猜写这些算法，原件保留而文字保持 partial。

主件 p7 有 BY4 与 Authors 2022 声明，p11 指向此 DOI 的 SI；附件封面 DOI、完整作者与官方精确链接闭合。SI 自身不另印 CC 段，准入依据按前述作品／附件有界链记录，不伪称其首页印有许可。原 Strassen／Python Cookbook／timeit 与全部参考信用保留；p11 的 DeepMind 专利申请意向保留，版权许可不扩成专利授权。实际文字与图像信用核查不授予被引作品、外部代码或数据的许可。

### AlphaDev

主件 17 页与 SI 28 页的全部 native 页已审读；两份 SI（本作和 FunSearch）全部 67 页另完成逐页视觉信用核查。主件首页／SI 封面 DOI 与 30 作者一致；online 2023-06-07 和 issue 2023-06-08 分开。主件 p1–7 主文、图、表、书目及 BY4 声明之后，还有 p8–11 完整 Methods、后续书目、信用，以及 p12–17 三幅扩展图和三张扩展表。

SI 附录 A 超参数、B 长度／时延、C 大规模排序／GNN、D 其他任务、E LLVM patch 的三种架构性能表、F Assembly Zero-One Principle 的反例／受限条件／两项证明、G 十二个 assembly 程序均存在，最后 p28 为真实书目结尾。F 的结论有条件，不能简写成任意 assembly 只需二值测试；E 的回退和噪声说明保留，不只摘进步数值。

native 的具体缺陷包括主件 p2/p4 图内 mov／cmp／Memory 等变成乱码，p15–17 扩展表只留下图注，p8 数学结构错序；SI p4 Table B.5 列头倒序，p12 连线／wire grouping 丢失，数学上下标和程序跨页格式仍部分丢失。SI p13 Table F.10 的列头与 caption 差异是原作品问题，不静默纠正。所有页非空且无异常，但不能据此宣称代码可运行或文本完整。

主件 Authors 2023／BY4、指定 SI 关联、原参考信用与 p11 专利申请意向均保留。SI 附录 G 的 DeepMind 2022／Apache2.0 AND BY4 是实物中的额外条件，按上节独立包装；其余 SI 全页视觉检查未发现新的具体许可排除。这个结论不外推 libc++、被引书籍或外部软件。

### FunSearch

14 页主件和 39 页 SI 全部 native 已审读；SI 全部逐页视觉核查信用。12 位作者、DOI、作品题名吻合。主件 p1–8 包含方法概览、cap sets／admissible sets／bin packing、局限和书目；p9–11 Methods 说明异步组件、程序库、island／cluster 选择及信用，p12–14 三幅扩展图实际存在。主件版权为 Authors 2023，不因 2024 卷期改写。

SI 的 A 消融与成本、B Shannon capacity／corners、C skeletons 和展示程序、D 对称／预 admissible 集合及证明、E 更多细节、F 十六个实现伪代码均存在，p37–39 为完整书目尾段。作者自己披露了展示函数删 unused lines／rename／加注释，不能算作采集器的修改。原 Algorithm F.14 的 header／implementation 字样差异保留，不执行或擅改伪代码。

主件 p5 Fig.4 表值在线性提取中黏连，p12 prompt 图内代码没有提取；公式 glyph／分数顺序、图的系列／箭头、Python 缩进有损。SI p13–15 嵌套 Python 的 block scope 丢失，p22–23 集合／张量符号和分段定义错译，p30／36 系统图与采样公式的关系不能按 native 重建。没有空页或异常，但四种实际缺陷足以要求 partial，不声称 runnable software fidelity。

实际 BY4 作品声明、指定作者 SI、Hill 构造及引用说明、作者原程序编辑说明、专利申请意向全部保留。SI 全页视觉检查未见另行版权／许可排除，不授权被引材料全文或外部模型。官方另列 Supplementary Data 1 ZIP，内容为实际程序与输出；合同已明确排除，故本批 complete 只指文章主文＋列定 SI PDF，不指全部补充附件或软件复现包。

### A-Lab

12 页主件与 44 页 SI 共 56 页全部 native 和逐页视觉已读。两份题名均为 inorganic materials，同 16 作者与 DOI；主件 p1 当前结果为 36/57，p3 明示四项不确定、Fig.2 为 36／4／17，p6 为 Authors 2023, modified publication 2026。旧 40/57 只在更正历史说明中出现；不是取得 annotated old revision。主线程另目视首页核对当前题名和结果。PDF 制作日 2026-01-06 与正式更正日 2026-01-19 分开；HTML SEO 的残留旧数字不替代实际正文。

主件 p1–6 主文与书目、p7–9 Methods／Data/Code availability／信用、p10–12 三幅 Extended Data 均完整。SI 封面后有 Notes 1–11（p3–16）、七幅图（p17–23）、五张表（p24–42，含更正后的长篇文献核验 Table3）、p43 参考文献和 p44 视频说明。这里只保存视频说明，不宣称外链视频、XRD/CIF 数据 ZIP 已取得。

native 没有空页或异常，但主件扩展照片／通信网络主要仅有图注，SI p4 的数学参数编码错误，图内周期表频次、凸包、分布、SEM/EDS 与标尺不完整进入文字，表格合并单元格／上下标有损。曾因低分辨率怀疑 SI Table2 漏行，后以高分辨率与原生提取复核撤回；88 行实际存在，不把审读误差写成解析缺口。

主件 p6 BY4、指定官方 SI、全页具体信用形成表示准入依据。Labman Automation 硬件、Berkeley Lab 的 M. Sargent 摄影、Materials Project 标记、SI 引文和视频来源均保留。SI 不另印 CC 段，全部 44 页未见具体版权排除；不把品牌、引文或数据链接许可化为外部作品全文授权。

### Coscientist

13 页主件与 52 页 SI 共 65 页全部原生提取、逐页视觉与信用检查。非敏感内容逐页阅读；SI 敏感案例只核对存档结构、警示／拒绝文字、可读性与来源标记，不推演、执行或补全其流程。正式主文／SI publisher 封面同题名、DOI 与四作者；SI 内部旧工作题名保留，不误换另一作品。

主件 p1–9 覆盖论文各节、技术使用披露、书目和 CC，p10 数据／代码边界与信用，p11–13 三幅 Extended Data。SI 包含术语与两幅 Scheme、实现与安全说明、实验档案、代码、三幅科学图、行为／人类基线和复杂设计截图，p52 optimization procedure 为真实结尾。原文明确部分数据、代码、prompts 因安全原因未完整公开，SI p5 也有 reviewer-only 移除标记；这是出版边界而非下载失败，不尝试恢复。

全部页非空且没有异常，仍保持 partial：主件 μl、对话／JSON 字形与数学结构有损，扩展页大多只有图注；SI p47–51 实际密集截图仅提取 203／10／82／6／11 字符。不能将剩下的页码当整页正文已文字化。其他代码缩进、角色色彩、曲线与化学结构仍需要回看原件；不执行论文程序、不做 OCR 或额外实验。

主件 p9 BY4、官方精确 SI 关联与全 52 页视觉信用检查支持独立绑定。保留实际 ScienceDirect Source、浏览来源域名和搜索截图的来源／URL，不把这些归属标记解释成外站的独立许可；技术使用披露和原安全警示也保留。无另行明确排除行，但 SI 自己未印 CC 段的事实照实记录。

### 审读覆盖与字段语义

内容执行者共审查全部 275 页原生提取／页面边界，实际目视 257 页，其中五份 SI 的 193 页全部逐页核查信用。主线程另目视 FAIR 首页、A-Lab 首页和 AlphaDev SI 第19页，后者确认真实 AND 许可 header。未声称主线程自己逐页读完全部原件。11 份各建议 body_quality_verified=true，指作品身份、实际 PDF 正文边界与可读性成立，不指无损文本、科学正确、专利实施权、软件可执行或 trusted；所有新 native 表示均为 partial。

## 真实联调与纠偏（integration findings）

首次生产包装时，FAIR 与 AlphaTensor 完成预检及断网双重放；AlphaDev 随后触发 `PDF_SUPPLEMENT_NATIVE_TEXT_DRIFT`，因此暂停后续构建。只读比对确认：其主件第 2 页的字体提取含两个单独 U+000D 控制字形，保存文本按 UTF-8 原字节解码并去除明确末注后，与原生提取完全相等；校验器的 `Path.read_text()` 通用换行转换把它们改成 LF，造成误报。其余十份 PDF 无此 CR／CRLF。

处理原则是修正校验器的无损读取与回归测试，而不是改写原始字形、重建以掩盖漂移或绕过完整性门控。已生成的 AlphaDev 保存层须先通过修正后的校验才继续重放；真正的文本漂移仍必须拒绝。最终修复结果及验证数值在下面验收节记录。

实际最小修复为 `read_bytes().decode("utf-8")`。新增主文及 SI 的 CR 回归在旧代码上明确失败，修正后 PDF supplement 32 项、publication-rights 13 项定向测试通过；测试同时证明改写 CR 为 LF 即使刷新 inventory 仍被拒绝。执行者随后只读核验真实 AlphaDev 17＋28 页和 45 个 selectors，零 validation errors，检查前后整胶囊字节完全相同。JSON 转义预览保留 CR，页行定位继续使用一致的 splitlines 语义；没有扩大到生产消费者或把归一化文本当原件字节。

在提交前的独立审查中，非作者 evaluator 另发现真实的 fail-closed 漏洞：`versioning=7` 这一损坏声明在保护块之外抛 TypeError，可能进入通用 fallback 的 `finalize_capsule`，覆盖已保留包。以隔离 journal fixture 复现了旧实现调用 finalize 的失败；执行者将类型检查与 retained manifest／PDF replay 纳入同一保护块，已保存 PDF 存在时统一转为 `RedistributionPackageError`，不修改无 PDF 的历史 fallback。新增 wrapper＋executor 回归通过，独立 evaluator 随后用自己的临时副本复验：fetch／prepare／finalize 均为 0 次，完整胶囊字节及 inventory 不变。此修复未改六项生产材料，也不代替最终精确提交审核。

## 六维结果（six-dimensional results）

| UID | 原件 before→after | 提取 before→after | 本地持久化 before→after | selectors before→after | 公开再分发 before→after | 知识状态 before→after |
| --- | --- | --- | --- | --- | --- | --- |
| `doi:10.1038/sdata.2016.18` (FAIR) | metadata_only→complete（主文） | unavailable→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧47保留＋9个新页定位 | root unknown保留；新增一表示 allow | null→null，无 demo claim |
| `journal-doi-10.1038-s41586-022-05172-4` (AlphaTensor) | unknown→complete（主文＋列定 SI） | partial→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧29保留＋47个新页定位 | root unknown保留；新增两表示 allow | null→null，无 demo claim |
| `journal-doi-10.1038-s41586-023-06004-9` (AlphaDev) | unknown→complete（主文＋列定 SI） | partial→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧47保留＋45个新页定位 | root unknown保留；新增两表示 allow | null→null，无 demo claim |
| `journal-doi-10.1038-s41586-023-06734-w` (A-Lab) | unknown→complete（主文＋列定 SI） | partial→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧35保留＋56个新页定位 | root unknown保留；新增两表示 allow | null→null，无 demo claim |
| `journal-doi-10.1038-s41586-023-06924-6` (FunSearch) | unknown→complete（主文＋列定 SI） | partial→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧32保留＋53个新页定位 | root unknown保留；新增两表示 allow | null→null，无 demo claim |
| `journal:10.1038/s41586-023-06792-0` (Coscientist) | unknown→complete（主文＋列定 SI） | partial→partial | 仅旧摘录→旧材料＋原 PDF／页文本／NOTICE | 旧24保留＋65个新页定位 | root unknown保留；新增两表示 allow | null→null，无 demo claim |

六项全部仍为 unresolved：FAIR 的字形／词间距／阅读顺序待 parser-only 评估；其余五项保留逐页列定的公式、图内代码、表格或截图损失，进入 OCR assessment，而非承诺 OCR 能还原科学语义。完整原 PDF 已可回看，未凭文件齐全将 native text 或 complete_target_consumable 改为 true。selected_version 只绑定显式新表示，旧顶层 null 版本与旧 coverage 事实保留为历史。

## 保存、消费与验证（persistence and verification）

包装执行者实际保存了 11 份原 PDF、11 份原生页文本、11 份页 selectors 和各自 NOTICE，并核对与取得原件逐字节相等。275 个页 selectors 对应 275 页，empty／failed 均为 0；这些计数不替代前面的内容判断。六个目标各进行两次离线重放，明确禁止 `fetch_bytes`／`prepare_capsule`，完整胶囊字节稳定；真实消费者均选中主 PDF 文本与其页 selectors。五份 SI 仍以独立目录可消费，不被主文摘录选取器当成父摘要。

六个 inventory 合计 68 件、57,098,202 bytes；包括六份 manifest 的全部胶囊为 74 件、57,180,298 bytes。这两个口径包含既有材料及新元数据，不与 11 份原 PDF 的 55,791,250 bytes 混写。

逐项完整性与表示级权利检查均无 errors／blocks。11 份 NOTICE 的完整 BY4 法条与既有官方法条资产一致，AlphaDev SI 另完整保留实际 AND 声明与 Apache 2.0 法条。六个审阅根对象仍为旧 excerpt 的 unknown；新增的六 main 与五 SI 各有独立 allow，不把表示级放行合并到根 gate。

已复核六来源的 18 份既有 README／document／默认 selectors 字节不变；12 份 canonical／snapshot 除新增 publisher_pdf 及表示权利外，历史对象不变；六 manifest 原根字段不变。旧 94 条 rights 审阅对象及原 items 字节保留，其他 209 胶囊未改。主线程独立比对了旧正文文件、其他 209 个 index／registry 对象和原 94 个 rights 对象，不只采用执行者声明。

只调用既有 registry／index／audit 生成器读取全部已保存 manifest，沿用既有 generated_at，不重新全库获取。因完整 index 是构建输入，执行 `make demo` 传播新的全局构建身份 `build:llm-wiki-v0:699e317011de119b`。36 selected、72 claims、72 evidence 与 BASE 字节一致，135 篇 Wiki 不引入六篇的新知识内容，collector assessment 不改变。

最终代码冻结后主线程实跑 `make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python`：163 项通过，包括 33 个 PDF supplement 回归。环境固定 Python 3.12.13／pypdf 6.18.1，没有新增依赖。pypdf 的可选 fontTools 编码警告如实保留；未安装新库以改变原生提取结果，已知编码损失继续记为 partial。

完整 `git diff --check` 返回 2，8,853 个诊断仅在八份忠实 native TXT（6,641）及 A-Lab 原 PDF（2,212）。Git 将该 PDF 自动判为文本进行空白诊断，不表示重写过原件；初次汇总工具按 UTF-8 解码整段 Git 输出因此失败，改为只解析诊断路径后确认范围。排除新表示 PDF／TXT 的其余路径 scoped 检查返回 0；不删原生空白、不改 PDF、不宣称全量空白检查通过。

主线程实际 `make validate` 通过：215 manifests、3,004 个 inventory 文件、24,167 selectors、52 篇文档与 80 个相对链接，校验器零 warnings／errors。`make reproducibility` 的 committed-tree／full-demo／compiler-only／read-only 四阶段各 169 个生成物逐字节相等。上述重放使用本批真实材料；最后的 malformed-versioning 修复只改变坏输入异常路径，不修改材料或 Wiki 输入，远端仍须用最终提交重新验证。

coverage 执行者实际运行默认 report-aware auditor 通过，其他 125 个原始 YAML 块与 observed 对象不变，PR15 execution 完整保留于历史，六条 knowledge 状态不变。当前 131 条非 repo 原件 complete 23／metadata_only 14／partial 8／unknown 86；文本 complete 3／partial 39／unavailable 14／unknown 75。完整本地消费仍仅证明 3 条、unresolved 128、trusted 0；旧 full_text 标签仍 93，不能当完成数。摘要与本报告 frontmatter 完全一致。

全库 publication 检查**没有通过**：99 个保留全文／补充表示的 UID、100 条审阅根行，仍有 64 个既有活跃 block，以及 GraphRAG `arxiv:2404.16130`／CoScientist `arxiv:2502.18864` 两条继承授权包不一致。六个新包没有新增错误或 block。这些事项保留给 P4／父 PR #1，不由本批 PASS 豁免；不能把结构／CI 通过表述为全库公开再分发已获准。

## 独立关闭门控（independent closure gate）

最终需精确 head/base 的独立 evaluator 分别对需求（requirements）、判断链条（agentic process）和核心质量（core quality）给出 PASS，并验证同一提交的 CI，之后才正常合入 work。本批不关闭 Issues #3/#4，不宣称完成 main 交接。
