---
phase: P3-SPEC-01
base_sha: d066fd64cb48a92f480a3393dcd055bb6da5f836
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts: {excerpt_capsule: 27, full_text: 91, metadata_capsule: 13}
  source_type_counts: {arxiv: 73, biorxiv: 2, blog: 10, industry: 2, journal: 11, methodology: 7, paper: 2, standard: 24}
  original_artifact_counts: {complete: 6, metadata_only: 17, partial: 7, unknown: 101}
  text_extraction_counts: {complete: 1, partial: 28, unavailable: 17, unknown: 85}
  action_bucket_counts: {access_restricted: 7, author_manuscript_fetch: 2, canonical_repair: 7, complete_verified: 1, html_article_snapshot: 14, identity_or_version_ambiguous: 2, needs_boundary_verification: 86, ocr_assessment: 4, open_fulltext_fetch: 6, standard_spec_fetch: 2}
  public_redistribution_counts: {allow: 27, block: 65, unknown: 39}
  content_inspected_full_text: 32
  structure_only_full_text: 59
  locally_persisted_complete: 1
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 130
---

# P3-SPEC-01 — RO-Crate 1.2 规范正文

本批为 PR #10，唯一 UID `standard:ro-crate-1.2`、`generic_web_or_document_v2` family、`canonical_repair` 行动桶。上一批 #9 已在精确 HEAD/BASE 的独立三维 PASS（review 5224608190）和 CI run 35113677507 success 后正常合入 work `d066fd64cb48a92f480a3393dcd055bb6da5f836`；父 PR #1 仍 Draft 对 main。

## 判断与执行纠偏（agentic decisions）

原记录只有旧入口 404 的 metadata 胶囊，没有正文。比较只改 URL、镜像整站、固定版本有界规范三种路线，选择第三种。只读 planner 在已保留官方 README 找到新的 `specification/1.2/` 路径；实际打开后，官方版本页直接提供完整单页 HTML，release 1.2.0 同时提供完整 Markdown。因此不重新编写通用 HTML 提取器，保留上游已经整理好的正文表示。

原生 Markdown 使用 Setext／ATX、Pandoc raw-HTML fences 和 simple table。为完整章节定位，只给既有 heading helper 增加默认关闭的结构模式，避免把代码块内的 `#` 或 simple table 尾线误认为标题；旧 GitHub 默认处理保持不变。消费者仅调整四处图片本地路径并追加归属，正文、代码和表格不改写。

另外检查了后续执行路径：原 generic adapter 会清空胶囊后重新抓 canonical 首页，可能把完整规范降回目录。新增可选的固定 Markdown 快照重放路径，只从已保存原件派生；身份／版本／revision 或本地图引用不符时先拒绝，不删除原件、不抓 latest。继续复用已有 inventory、retrieval 与许可包装，不建立新物化框架。

## 实际获取与版本（retrieval and identity）

- 官方入口：[RO-Crate specification 1.2](https://www.researchobject.org/ro-crate/specification/1.2/)，永久 URI 为 `https://w3id.org/ro/crate/1.2`。身份仍是规范 edition 1.2；release tag 为 1.2.0，不把两个版本字段混同。
- 原 Markdown：[1.2.0 Markdown](https://github.com/ResearchObject/ro-crate/releases/download/1.2.0/ro-crate-1.2.0.md)，302,360 bytes、5,572 行。
- 原 HTML：[1.2.0 单页 HTML](https://github.com/ResearchObject/ro-crate/releases/download/1.2.0/ro-crate-1.2.0.html)，746,231 bytes、4,794 行。
- 两件 GET 在 2026-09-16T15:19:37Z 启动，15:20:12Z 确认均完成，HTTP 200，传输类型 application/octet-stream，内容分别是 Markdown／HTML。经 GitHub 官方 release-assets 重定向；manifest 保留最终 host/path、移除短期签名查询串，不把带时限的访问参数作为远程消费依赖。Web reader 不能打开 release asset 的工具错误不冒称站点拒绝访问；正常公开 GET 成功。
- 官方 release 的 published_at 为 2025-04-28T17:52:41Z；两件 asset 创建于 2025-06-04，而规范自身 Published 为 2025-06-04。分开记录，不把 release 外壳创建时间冒充规范发布日期。
- 四个正文实际引用图像从 tag 1.2.0 指向的 `dc42c230937b872710bae187b1b5bf51a3b494d2` 的 `docs/assets/img/` 获取：`crate1-folders.svg` 27,486 bytes、`introduction-figure-1.png` 48,548 bytes、`introduction-figure-2.png` 49,838 bytes、`ro-crate-preview-example.png` 98,264 bytes。15:22:10Z 开始，15:22:28Z 确认完成，均 HTTP 200，SVG／PNG 类型正确。
- 旧 `assets/img` API 路径查询得到404，查看固定树后确认真实仓库路径是 `docs/assets/img`。没有将这一次目录定位错误写成规范缺图。

除了该版身份／release／许可信息、两件正文和四张实际图，没有抓其他规范版本、教程、外部数据或引用网络。原404诊断保留于 manifest.historical_acquisition；旧尝试没有记录时间，不补造时间。

## 正文边界与实质核验

原 Markdown 的主章节行：Introduction 52、Terminology 313、Structure 388、Metadata 602、Root Data Entity 805、Data Entities 1003、Contextual Entities 1577、Focus 2172、Provenance 2384、Profiles 2681、Workflows and Scripts 3306。Appendixes 3662；四个实际展开附录为 Implementation notes 3692、JSON-LD 3918、relative URI 4305、Changelog 4990；References 5108，最后脚注在5572。

开头核对规范定义与 JSON-LD running example；中段核对 Profile Crate 的 resource／role 与长示例，L3033–3055 的 schema-language 表有4列、10条数据行；尾部核对绝对 URI relativization、L4967 边界警告、完整 changelog／references／末脚注。不是首页摘要或截断页。

内容 agent 的只读跨表示比较显示155个标题的级别／顺序相同，119个实质 fenced code 块逐块对应，另12个 HTML pre 对应 Markdown 缩进代码／目录树；131个 pre 均有正文。641个较长 HTML 正文段落在去 Markdown 格式后匹配。HTML 内部 fragment 无缺锚点或重复 id，没有额外 script/link/iframe/object/embed 加载依赖。上述统计支持忠实度，仍以实际内容检查而非数量单独判定完整。

四图全部原样保留，原件目录层级使 `../../assets/img/` 自然解析；消费者只改为 `../source/assets/img/`。三个 PNG 经实际视觉检查，SVG 的 title/description、creator/contributor、CC0 元数据直接检查。不得把代码中的 `workflow/workflow.svg`、CSV、BagIt 或外部 context URL 当成该规范页面还要获取的资产。

真实原作限制：图1 PNG 仍显示 `/crate/1.1`，但附近规范正文与 alt 为1.2；原件照存并注明，不改图。原稿 Web pages 链接是旧入口，PDF 标签误指 HTML。部分 JSON 是片段或有原作者额外逗号，不宣称可直接执行。Pandoc 文本完整可读，不宣称任何 GFM 渲染器都能保持排版；完整 HTML 和图像可供视觉检查。

## 六维结果与公开表示

| 维度 | before → after |
| --- | --- |
| 身份／版本 | RO-Crate 1.2、旧失效入口 → 同一规范 edition 1.2、已核验官方入口及 release1.2.0 |
| 原件 | metadata_only → 完整官方单页 HTML／Markdown＋四张实际引用图；最终覆盖判断记录于台账 |
| 文本 | unavailable → 原生完整 Markdown 的最小派生，定义表／代码／附录均保留 |
| 持久化 | 仅metadata/README → 原件、派生、图片、章节定位、NOTICE、manifest及registry入repo |
| 公开表示 | unknown → 明确固定范围的 allow，Apache-2.0正文与CC0示例/SVG分开，完整许可和署名随包 |
| 知识 | 未进入demo、无claim → 不改变，不新增trusted |

新全文审阅不追溯改写历史91条 rights baseline。以可选 `additional_full_text_review_count: 1` 明示新增审阅，92条当前审计总数中原91条对象不变；旧65个block不被稀释。四方包绑定原 Markdown revision及固定 HTML/四图范围，完整作者（84名）、原版权、修改说明和许可链接在原件／消费者／NOTICE保留。

全库公开包装检查（publication rights check）同时暴露两个继承问题：`arxiv:2404.16130` 和 `arxiv:2502.18864` 的 canonical／capsule／manifest 修改说明与范围已在先前正文修复中更新，但 rights audit 仍是旧包。逐文件与逐审阅对象比对证明它们在 BASE d066fd6 已存在，本批未改这两个 UID。当前检查为 active91／audited92、64个既有活跃block、上述2个包不一致错误；RO-Crate 自身无block/error。不能把专项通过写成全库公开门控通过；P4必须修复这两项真实包对账，不沿用先前CI绿灯或重新泛化组件许可审计。

## 生成依赖与验证

主线程实测所选36个demo来源未变且没有 RO-Crate；但现有 build_demo 的输入包含全量 index 与 rights audit，materialization_snapshot 记录 corpus_summary。因此启动合同在重建前已细化：允许由既有生成器传播必要的全库计数与build身份，禁止改pipeline手写代码、selected内容、claim/evidence内容。不能为了小diff留下不可重放的旧构建身份。

使用与CI一致的Python 3.12.13／pypdf 6.18.1运行 `make demo && make test && make validate && make reproducibility`：106项测试通过；215份manifest、2,874个文件、22,069个selector检查无错误；46篇文档、80个相对链接检查通过。最终build为 `build:llm-wiki-v0:6b16cc1e2adf538b`；committed-tree、full-demo、compiler-only、read-only-validation四轮的169个生成文件均字节一致。

RO-Crate胶囊共12文件；inventory计11件非manifest文件，`local_bytes=1,681,687`，含manifest的12件实际合计1,692,854 bytes。派生正文5,584行／303,853字符、155个章节selector。固定原件离线重放不重新获取、不清空目录；原件和四图保持下载字节。36个selected、72条claim、72条evidence的各自文件与BASE字节一致，既有91条rights对象不变。

隔离Git候选索引导出（candidate index export）检验在禁用网络获取与目录清空的条件下重放同一胶囊，并逐字节比较12个文件；原Markdown、原HTML、派生Markdown的四张本地图均可解析。这个检查只证明候选Git树具备离线消费能力，不冒称remote clone或main fresh checkout；P5仍待执行。

保留原作字节也保留其行尾空格：完整 `git diff --check` 会报告原Markdown、原HTML、SVG及忠实派生Markdown中的上游空白；排除这四件的实现／元数据／文档／许可／生成产物检查通过，不为获得空白绿灯改写原件。当前HEAD的覆盖检查、独立审核和远端CI记录于PR #10，不以启动提交CI或上一批PASS冒充完成。

## 独立关闭门控与未完成边界

独立 evaluator `/root/pr10_independent_evaluator` 不参与实现或数据写入，最终针对精确HEAD和BASE d066fd6判断诉求、agentic过程、核心质量。三维PASS和当前CI成功后才Ready／正常merge回work，使用agent COMMENT而非人类APPROVE。

本批不代表其余130个非repo完成，不改84repo原件，不关闭Issues #3/#4，不删除分支、不强推、不改workflow/保护、不晋升trusted，尚未进入main。父PR #1仍需剩余P3、P4对账及P5 main新检出验收。
