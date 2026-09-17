---
phase: P3-PDF-01
base_sha: 57793c9eea07316a9715f6599fcbb1a89a999102
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts: {excerpt_capsule: 27, full_text: 90, metadata_capsule: 14}
  source_type_counts: {arxiv: 73, biorxiv: 2, blog: 10, industry: 2, journal: 11, methodology: 7, paper: 2, standard: 24}
  original_artifact_counts: {complete: 5, metadata_only: 18, partial: 7, unknown: 101}
  text_extraction_counts: {partial: 28, unavailable: 18, unknown: 85}
  action_bucket_counts: {access_restricted: 7, author_manuscript_fetch: 2, canonical_repair: 8, html_article_snapshot: 14, identity_or_version_ambiguous: 2, needs_boundary_verification: 86, ocr_assessment: 4, open_fulltext_fetch: 6, standard_spec_fetch: 2}
  public_redistribution_counts: {allow: 26, block: 65, unknown: 40}
  content_inspected_full_text: 31
  structure_only_full_text: 59
  locally_persisted_complete: 0
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 131
---

# P3-PDF-01 — 固定版本论文的补充 PDF 正文

本批为 PR #9，基于上一批 PR #8 三维独立 PASS、当前 CI success 后正常合入的 work `57793c9eea07316a9715f6599fcbb1a89a999102`。只处理四个既有 UID，一个 arXiv family／open_fulltext_fetch 行动桶。不扩大 collection，不覆盖旧 TeX，不获取引用网络或外部实验数据。

## 规划与纠偏（planning and correction）

只读预检确认旧 TeX 具有实质性消费缺口：AI Scientist 的 VerbatimInput/minted 与十篇内嵌论文未展开，Agent Laboratory 的三份内嵌评分调查表未入正文，AI Scientist-v2 有算法名宏丢失、代码/评审文本未展开及三篇内嵌论文。ADAS 作为相对简单的同版表示案例，验证共同路径。

比较继续扩写完整 TeX 解释器、仅记录缺口、获取同版本官方 PDF 三条路径后，选择最后一条：已有作品级 CC BY 4.0 证据与固定 vN 可以支持明确的补充表示；编译后的 PDF 已包含目标正文和实际内嵌附录，不需递归下载被引用论文、数据集或模型。旧 source、normalized、默认 selectors、archive revision、retrieval 与原归属包均原样保留。

执行中发现不能直接复用旧提取策略：pypdf 的 layout 模式对内嵌 PDF 页静默给出空串。实测 AI Scientist 186 页仅 89 页有文本、Agent Laboratory 84 页仅 58 页、AI Scientist-v2 69 页仅 48 页；普通 plain 模式能读出这些页的实质内容，并经视觉核对。故只为新增补充层明确使用 plain，并记录模式；旧默认 layout 行为和旧派生不变。这是解析策略纠偏，不把算法缺陷伪装成原件没有文字，也不默认 OCR。

首次 demo 重放虽结构通过，内容检查又发现默认摘要算法会在全 PDF 搜索 Abstract：AI Scientist 两篇父论文首页没有该题头，误选了内嵌子论文摘要。修复限于新 PDF 表示：默认摘录不得越过第一页；允许 agent 核验后声明同一页连续正文行范围，并校验行界与全局 offset，不按 UID 猜标题或新增复杂摘要算法。四篇父论文摘要范围分别为 ADAS L9–33、AI Scientist L9–29、Agent Laboratory L10–25、AI Scientist-v2 L11–29（均为各自 pdf-supplement/document.txt）。这些范围是消费选择，不改变原文或准入包，旧源格式行为不变。

## 实际获取（retrieval）

四次 PDF 请求在 2026-09-16 14:41:22 UTC 启动，14:42:16 UTC 确认全部传输已完成；manifest 的 retrieved_at 使用这一确认时刻，并保留 request_started_at/completion_observed_at，未编造逐传输结束时刻。四次均 HTTP 200、application/pdf，最终 URL 与以下请求的固定版本 URL 相同，无 latest 回退。官方同版 abs 页面另用于核对题名、完整作者、版本与 CC BY 4.0 链接；本批没有其他 corpus 获取。

| UID | 固定版本官方 PDF | 原件 bytes／页数 | 前态 → 本批原件／文本 |
| --- | --- | --- | --- |
| arxiv:2408.08435 | [ADAS v2](https://arxiv.org/pdf/2408.08435v2) | 801,981／34 | 未核验旧 TeX → 完整同版渲染 PDF／有损页文本 |
| arxiv:2408.06292 | [AI Scientist v3](https://arxiv.org/pdf/2408.06292v3) | 11,731,143／186 | 未核验旧 TeX → 完整同版渲染 PDF／有损页文本 |
| arxiv:2501.04227 | [Agent Laboratory v2](https://arxiv.org/pdf/2501.04227v2) | 3,644,380／84 | 未核验旧 TeX → 完整同版渲染 PDF／有损页文本 |
| arxiv:2504.08066 | [AI Scientist-v2 v1](https://arxiv.org/pdf/2504.08066v1) | 8,923,691／69 | 未核验旧 TeX → 完整同版渲染 PDF／有损页文本 |

Original complete 指固定版本目标渲染作品的全页，不指整个原始 TeX 归档已完整；text partial 反映下述具体缺失，不否认正文已经可读取。现存源包的 omitted 列表与旧状态保留历史含义。四项身份／版本不变；持久化新增独立 PDF、页文本、页定位及 NOTICE；公开表示单独批准；知识准入仍 candidate，不晋升 trusted。

四项旧账本行动桶都是 needs_boundary_verification。本批在只读核验后选择 open_fulltext_fetch 作为执行动作，不把旧桶冒写成 open_fulltext_fetch；新 PDF 获得后，剩余工作转为限定图像文字／代码／表格和字形阅读顺序的 ocr_assessment，而不是继续泛泛声称边界未知，也不是保证 OCR 能恢复图形关系。

## 正文与边界的内容核验

- **ADAS v2**：34 页。首页题名、三位作者与边栏 v2 对齐；主文 p1–11、致谢/参考文献 p12–18、p19 附录目录，A–J 到 p34。实际视觉检查 p1/2/3/5/17/23/26/34；p23 Framework Code 的 1–39 行代码可读，p34 Table 6 与 J 成本说明为真实结尾。五个实际图文件对应四个编号图，均在 PDF；p26 Figure 4 的 ARC 彩色矩阵、p5 曲线/置信域、流程箭头及空间关系未文本化，文字抽取不能宣称无损。
- **AI Scientist v3**：186 页。首页题名、六位作者与 v3 边栏对齐；p30 实际目录列 A Prompts、B Hyperparameters、C Progression of Generated Ideas、D 十篇生成论文。p8–9 minted diff 已是实际代码，p31–36 prompt 与 p38–60 idea 文字可读；p93 表4有 Circle/Dino/Line/Moons 的实验数值及图1，p186 是最后生成论文的 review/limitations/decision，不是下载截断。图形、截图、字体字距、数学与代码缩进仍有损，PDF 原件为核查依据。
- **Agent Laboratory v2**：84 页。首页和 PDF 元数据均固定 v2，十位作者对齐；主文 p1–22、参考文献 p22–30、A 配置 p31、B 提示词 p32–56、C 调查表 p56–84。实际视觉检查 p1/5/17/31/42/57/64/66/74/76/84；三份 includepdf 实页为 p57–64、p66–74、p76–84，确是研究报告评分调查表，不是表内链接的研究论文全文。p42 的 scoring/code repair/initial generation 提示框和 p84 Confidence/Decision/Optional feedback 可读。p17 Figure 8 的三块图像表格单元格没有进入 native text；p57/66/76 各有 1/2/1 个未映射 NUL 字形，问卷空间绑定有损。
- **AI Scientist-v2 v1**：69 页。首页八位作者、v1 边栏对齐，算法名在编译文本中存在而非空宏；p20 目录包含 A 参数、B 提示词、C 三篇生成论文及团队/代码/匿名 workshop reviews。三篇论文实页在 p33–40、p46–52、p59–64；实际视觉看 p1/35/56/69。p35 边注会插入 native 段落阅读顺序，p55–56 Figures 8–10 和 p66–67 Figures 11–13 的代码截图未被原生提取。p69 保留 Reviewer #3 的完整末段、Rating/Confidence；七份匿名评审继续保留独立归属，不推断真实身份或全部同意。

AI Scientist 的进一步逐项核验确认：十篇内嵌论文实页为 p62–72、75–84、88–96、100–110、114–124、128–134、138–147、151–159、163–172、176–184，共 97 页；每篇实际摘要／中段／尾部都可读。20/20 份已有 TXT 在去页眉页码、折叠空白后与 plain 文字完整匹配。另发现原 PDF 自身 p171（MDL 内嵌论文第9页）Figure 5 是仅显示 `mdl_transition_rate_vs_grokking_speed.png` 的空白占位框，Figure 6 则有真实图。这是原作品内容缺陷（source content defect），不是本批漏下载，也不授权从外部仓库替换/补造原件；完整保存官方 PDF 不等于作者预期的每张图均存在。

## 表示、归属与消费

新增 `pdf_supplement` 仅服务这一类“已有 TeX＋同版官方 PDF 补充”，不是重建通用 pipeline。原件为 `pdf-supplement/document.pdf`，页文本、独立页 selectors 与完整许可 NOTICE 同目录；旧默认表示全部保留。新层的原件 revision、真实获取记录、页数与提取模式、内容质量核验、具体损失、独立归属包分别记录。

已有文字包 allow 不自动外推新 PDF。四方 canonical metadata／capsule metadata／manifest／rights audit 的新 PDF 表示对象明确绑定实际 PDF revision；同版官方作品 CC BY 4.0、完整作者和可见独立信用保留，六字段归属包及完整 CC BY 4.0 NOTICE 随文本。AI Scientist-v2 的七份 review 沿已有独立 OpenReview Comment 许可证据与 Reviewer 标签，既不冒称论文作者原创，也不重新开展无边界模板审计。旧包、旧 gate 与既有 65 block 原样保留。

消费端只有在新增表示准入、正文质量核验通过后才选择新页文本，并将权益引用绑定到 PDF revision 和 PDF 归属包；不能读新 PDF 却继续引用旧 TeX 的许可范围。`body_quality_verified=true` 表示已执行可消费质量核验，不等于 `text_extraction=complete`。不把保存原件、文本提取、公开存储与知识可信晋升合为一个布尔值。

## 验证与独立关闭门控

最终数据已明确采用 plain，旧 layout 中间结果不作为提交产物。四个胶囊都经过两次离线提取／包装的全文件字节幂等比较，旧 base 的 source／normalized／默认 selectors／NOTICE／files.jsonl 逐字节不变。

| UID | 新 PDF 页定位 | 页文本存储字符（含唯一归属附注） | 新胶囊总 bytes |
| --- | --- | --- | --- |
| arxiv:2408.08435 | 34 | 119,255 | 1,781,191 |
| arxiv:2408.06292 | 186 | 506,208 | 13,351,232 |
| arxiv:2501.04227 | 84 | 170,597 | 4,877,341 |
| arxiv:2504.08066 | 69 | 197,328 | 9,983,477 |

373 个新页定位全部存在，无空文本页或提取异常；这些是结构结果，不取消图文 partial。手写变更为最小可选接口／校验／消费权益分支、定向测试、四项新归属对象与审阅台账/报告；原件是上述四次 PDF GET；生成物为四胶囊页文本/页定位/manifest/metadata镜像、215-entry聚合及受影响 demo/Wiki/release。

实际重建仍为 36 sources／72 claims／72 evidence／135 Wiki pages，build=`build:llm-wiki-v0:8d5202830938fe6b`。与本批 base 比较，只有本批四 UID 的四条 excerpt claim 与四条 evidence 内容改变，其余 claims/evidence 记录完全一致；selected sources 对这四项明确选择 PDF 文本和 PDF revision，权益引用绑定新 PDF 包，其余来源不切换表示。Wiki 必须传播新的输入、权益与构建身份，而非人工改页来减小 diff。

最终实际 evidence 定位为 ADAS L9–11、AI Scientist L9–11、Agent Laboratory L10–13、AI Scientist-v2 L11–13，均来自父论文首页。既有两句摘录启发式仍会把 AI Scientist 的 `e.g.` 误判为句末，因而包含完整首句和截短的第二句；这是有界摘录的已知限制，不是完整摘要或可信知识声明，本批不扩写通用句法解析器。原 PDF 与完整页文本保留后文，可供远程继续阅读。

已实际运行（Python 3.12.13、pypdf 6.18.1）：

- `make demo`、`make test`：PASS，94 tests；含 Form XObject 的真实内嵌文字、plain/layout 选择、父首页摘要与准确行定位、旧 NON_PAGE_SELECTOR 约束，以及错版本、缺页、跨页 preview、未准入/包漂移/NOTICE/footer/revision 的负测。
- `make validate`：PASS，215 manifests、2,865 个校验文件、21,914 selectors、45 篇 docs／80 相对链接，0 warnings／errors。专项新 PDF gate 验证不把旧 65 block 改为 allow 或变成新全库门槛。
- `make reproducibility`：PASS，committed_tree、full_demo、compiler_only、read_only_validation 四种重放各 169 个生成文件字节一致；不能用旧 head 绿色 CI 替代。
- 全量 staged `git diff --check` 退出 2，仅 ADAS 和 Agent Laboratory 的新 `pdf-supplement/document.txt` 保留了 pypdf 原生行尾空白；不做 cosmetic trim 或冒称全量 PASS。明确排除这两个生成文本后的 staged scoped `git diff --check` PASS，未关闭 CI 或内容校验。
- 默认 `scripts/audit_non_repo_coverage.py` 实际运行 PASS，131 项 observed 和本报告 summary 一致；台账只有四个本批 UID 改变，其他 127 逐对象不变。完整原件 5，文本 partial 28／unavailable 18／unknown 85，候选来源 30、trusted 0；unresolved 131 如实保留，不靠总数美化完成度。

独立 evaluator 不参与上述实现或内容写作；最终锁定精确 HEAD 与 BASE，分别判断诉求、agentic 判断链、核心质量。当前 CI success 和独立三维 PASS 前保持 Draft；精确提交、CI run 与独立 agent COMMENT 保留在 PR #9，不伪装人类 APPROVE。

本批不表示 131 来源完成，不进入 main，不关闭 Issues #3/#4，不删除分支，不改历史、保护或 workflow。其他 127 个非 repo 与 84 个 repo 原件不动；P4 对账和 P5 main fresh checkout 仍未完成。
