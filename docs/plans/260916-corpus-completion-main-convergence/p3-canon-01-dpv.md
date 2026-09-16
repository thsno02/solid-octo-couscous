---
phase: P3-CANON-01
base_sha: 448a0e7a421a2bf1a58c821e07d8673d5c89f09b
status: local_validation_pass_pending_independent_evaluation
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
    complete: 8
    metadata_only: 15
    partial: 7
    unknown: 101
  text_extraction_counts:
    complete: 2
    partial: 29
    unavailable: 15
    unknown: 85
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 2
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 86
    ocr_assessment: 5
    open_fulltext_fetch: 6
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 34
  structure_only_full_text: 59
  locally_persisted_complete: 2
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 129
---

# P3-CANON-01 — DPV 2.3 核心规范入口与正文消费

本批 PR #12 仅处理 `standard:w3c-community-dpv`，为 generic family 的入口修复（canonical repair）。PR #11 已在最终 `bfff2d6`／BASE `ca5d6e1` 的独立三维 PASS（review 5225466531）与 CI 35121900670 success 后正常合入 work `448a0e7a421a2bf1a58c821e07d8673d5c89f09b`；父 PR #1 仍 Draft 对 main。本批不是全库完成声明。

## 规划与有界调整（planner）

旧 `w3c.github.io/dpv/` 仅有 334-byte 移动页的检索记录，本地正文是 39-byte excerpt；当时未保留原 HTTP 响应。旧记录和 excerpt 保留为历史，不改写成当前版本的成功获取。

比较只改 URL、整个网站镜像、固定发布核心正文三条路径，选第三条。[官方 dpv-2.3 release](https://github.com/w3c-cg/dpv/releases/tag/dpv-2.3) 对应 `w3c-cg/dpv` 提交 `cbcd21567808812677eeb3bb0f05b2ff2c2211a5`，发布时间 2026-02-28T19:46:53Z；原稿 ReSpec 配置为 version 2.3、publishDate 2026-02-25、CG-FINAL。规范入口按官方发布固定为 `https://w3id.org/dpv/2.3/dpv`；入口身份依据不冒称已对该 URL 取得正文响应，也不把 Community Group 文档称作 W3C Recommendation。

启动合同先于正文获取。实际主页面第 713 行明确十一模块提供 full definition，因此只留主页面仍缺核心规范。主代理、内容执行核查及独立 evaluator 的只读边界预审后，在下载模块前更新 PR 边界说明：增加同一固定提交的十一份核心模块及真实引用图，不扩张到扩展站点。预审仅认可范围细化，不是最终质量 PASS。

## 实际获取（executor）

全部 39 个源文件用公开 GitHub contents raw API 实际 GET：`https://api.github.com/repos/w3c-cg/dpv/contents/<path>?ref=cbcd21567808812677eeb3bb0f05b2ff2c2211a5`，请求 Accept `application/vnd.github.raw+json`，返回 HTTP 200、`application/vnd.github.raw+json; charset=utf-8`。该 MIME 下响应是原 HTML／SVG／LICENSE 字节，不是 JSON 包装。

| 范围 | 实际源文件 | UTC 观察时间 |
| --- | --- | --- |
| 核心入口 | `2.3/dpv/dpv.html`，550,050 bytes | 2026-09-16T16:37:17Z 确认完成；无精确请求开始时间 |
| 许可证 | `LICENSE.md`，2,489 bytes | 16:38:44Z 确认完成；无精确开始时间 |
| 核心定义 | `2.3/dpv/modules/` 下 TOM、context、entities、legal_basis、personal_data、process、processing、purposes、rights、risk、rules，共十一 HTML | 批次开始 16:38:58Z、16:39:15Z 确认全部完成 |
| 核心总览图 | `2.3/diagrams/overview-dpv-2.0.svg`，1,240,043 bytes | 16:39:15Z 开始，不晚于 16:41:07Z 确认完成 |
| 其余正文图 | 二十五张实际 img 引用 SVG，逐件名称／bytes 见 manifest | 批次开始 16:41:07Z、16:41:32Z 确认全部完成 |

之前 raw.githubusercontent.com 的 core／LICENSE 请求在 16:35:05Z 开始、16:35:42Z 确认连接超时，curl exit 28、HTTP 000、0 bytes；core 的 IPv4 重试同样超时，16:36:41Z 确认完成，没有精确开始时间。失败保留为尝试记录；不解释成来源不存在、拒绝授权或 HTTP 404。改用官方公开 API 是另一实际获取路径，不绕过访问控制。另一次 connector 读回 core 内容只作核查，落库使用实际 curl 下载的字节。

为正确处理未保留相对引用，另作两个实际 HEAD（不下载替换原稿）：响应 Date 为 16:55:50–51Z 的 `w3id.org/dpv/2.3/dpv` 经 302、301 到 `https://w3c-cg.github.io/dpv/2.3/dpv/`，最终 200；16:55:52–53Z 的 `w3id.org/dpv/2.3/modules/purposes` 经 302 到 `https://w3c-cg.github.io/dpv/2.3/dpv/modules/purposes.html`，最终 200。HEAD 声明长度分别 1,319,610／608,205 bytes，是发布表示，不冒充已取得该 GET 或与固定 tag 源码同字节。派生链接以官方展示位置 `document_url` 为相对路径基准，不错误地把 GitHub raw API endpoint 当成文档地址；其他模块沿同目录布局记录基准，不宣称逐一 HEAD 成功。

## 内容审读与范围证据

主页面及十一模块均有静态叙述、定义和示例，不是需执行 JS 才能加载正文的空壳。主索引实际有 1,116 个唯一 dpv 词条／full-definition 链接；全部链接在指定模块的原生 id 找到。模块合计 1,122 个 native dpv 定义表，唯一 IRI 为 1,116，双向集合一致。六个重复是 rights 复用的属性，不当成额外新词条。rights 另有七个外部复用定义表，同样保留。主页面自报 1,259 concepts、changelog 又报 1,165 terms，不能据此虚构“缺失 143／49 条”，也不静默修正文案。

内容任务独立于解析实现，逐模块检查开／中／尾正文、定义表、完整 pre 和实际图片。主要定位如下（行号指保留的原 HTML）：

| 模块 | 关键内容及边界 |
| --- | --- |
| TOM | L665 四组措施；L10914 HumanOversight；L21422 supportsComplianceWith；L20732–20738 hasNoticeLayer 的 domain/range，通知与同意记录实例完整。 |
| context | L833 时间／次数／事件实例；L7259 Location；L15695 isOutsideOfLocation；L1561 区分主观屋外与法律辖区外。 |
| entities | L799 控制者和代表示例；L5708 LegalAgent；L11379 isSubsidiaryOf 方向；L1237–1238 HumanSubject 版本兼容说明。 |
| legal_basis | L761 三种建模模式；L7546 合同履行状态；L14606 isIndicatedBy；L14252 原 range 为 ContractStatus，不擅自收窄。 |
| personal_data | L668 core 与 PD 扩展边界；L913、924 类别／实例；L1034、1107 匿名／未知区别；L3961 hasPersonalData。L3974 不规整 HTML Examples 单元格仍是实质内容。 |
| process | L664–665 整体信息与操作的区分；L717 嵌套实例及多目的交叉适用；L752 不强制 Process；L1141 Service 父类为 Process；保留 L695、930 兼容／弃用说明。 |
| processing | L665 操作层次；L1552 起处理／存储／来源／自动化上下文；L1735、1884 规模为语境定性而非通用阈值；L16600 isImplementedByEntity 的 range。 |
| purposes | L665–680 Purpose／Sector 及有效目的限制；L1515 v2.3 breaking change；L1759、1774 KYC／NACE 实例；L8084 目的覆盖 data 或 technology；L11640 hasSector。 |
| rights | L663 active/passive；L1303–1387 RightExerciseRecord；L2720–2776 foaf:page 外部复用；L2788–2797 资助；L1948／1951 重复 Usage Note 不能覆盖。 |
| risk | L663–664 轻量 core 与 RISK 扩展区分；L1811–1914 Impact；L4140–4206 mitigatesRisk；L4229–4238 资助。 |
| rules | 简单 deontic rules，不提供完整执行引擎；保留 Permission／Recommendation／Obligation／Prohibition／Deterrence／NotProvided 六类 keyword 表、三段原生示例和默认语义、触发时机尚未定义的说明。 |

定义中的 `Domain/Range includes` 不是采集者新增的严格 OWL 约束。多条父链、Subject/Object of relation、重复 Usage Note、Examples、Source 及 funding／贡献者说明属于正文。引用宏 `[[…]]`、`[=…=]` 保留，不运行 ReSpec 猜测其生成结果；原始配置可追溯，不抓 common.js、CSS、favicon 或递归参考文献。

### 上游差异不由采集者纠正

保留而非“修复”：rights E0061 三个左方括号而只有两个右方括号；rights isAfter 注释却说 before；context／risk 例子 `a dpv:hasProcess`；processing E0075 `a dpv:hasProcessing`、E0049 以 hasDataSubject 表达 scale；entities/TOM 的 BetaInc／Beta；TOM StaffCredentialsTraining／StaffCredentialTraining；legal_basis 一年写成 `P1Y` 的 xsd:date、RefuseConsent 注释说 reaffirm；context NotApplicable 注释谈 Stop/Halt；rules 的 RFC2199 标题与 RFC2119 表内容不一致。

purposes L1511 说 Service 扩展 Purpose，反于 process L1141；ServiceOptimisation 的 L10453 旧 note 指 ServiceProvision、L10431 父类已为 ServiceManagement；RightsFulfilment L9565–9572 又列 LegalObligation→LegalBasis。不能把模块中所有词条自动改造成 Purpose。

### 图片和文本提取不是同一维度

二十六张 SVG 原件完整保留。二十五张具有原生文字；总览图虽无 SVG text，却含路径及嵌入 PNG，并非空图。图片箭头、分组、状态颜色、多个起点具有语义，没有等价 alt／desc；只提取标签不能证明完整文本化。本批保留图的本地消费路径，文本状态明确 partial，不做无边界 OCR／图语义重建。

原图也有上游版本差异：overview_Storage 标 hasStorage 而正文 hasStorageCondition；两个 involvement overview 标 hasNonInvolvementEntity 而当前定义 hasNonInvolvedEntity；purpose-2 仍画 ServiceProvision 而未画 ServiceManagement。文件名 overview-dpv-2.0.svg 是 2.3 页面实际引用，不是采集者下载错版本，不据图补造当前词表。

## 持久化和公开边界

固定提交 LICENSE 明确 covers documents/resources，采用 W3C Software and Document License 2023。实际保留完整通知、原作者／贡献者／资助、变更说明和 W3C 短通知，具体包装见 `raw_data/licenses/dpv-2.3-w3c-2023.md`；SPDX 沿用 W3C-20150513 的理由在其中引用官方条目。原文件不改字节。许可核查限于这次实际表示，不恢复逐组件考古。

“原件已取得”“派生文本完整”“可以公开持久化”“知识 trusted”四者分开。预期本批 original complete、text partial；知识不新增 selected／claim／trusted。全部成果必须进入 Git 候选树并经远程 PR 持久化，临时下载目录不是交付。

## 验证与独立门控

解析执行者仅扩展已有 retained_text_sources 的 html opt-in，不引入额外依赖或全站转换框架；主代理在真实接入时发现 API endpoint 不能充当相对文档基址，返回 executor 最小修复并增加回归用例，再次冻结后执行实际预处理。表格按行／单元格顺序表示，保留重复键及不规整 orphan td；pre、code 保留真实 TAB／换行，body 文本逐节点一次；原生 id 按源文件 stem 分隔，标题定位使用真实源行。配置只提供原稿行定位而不复制／执行脚本。

39 份原件与实际临时下载副本逐字节相等，共 6,646,341 bytes，26 SVG 均成功作 XML 解析。胶囊实际 47 文件、9,738,847 bytes；非 manifest 的 inventory 为 46 件、`local_bytes=9690759`。单一消费者 43,115 行、2,187,629 字符；1,372 selectors 分为 12 源前言、1,348 章节、12 原始配置定位。全部来源范围和 source_heading_line 都指向真实原稿；3,832 个锚点唯一，7,002 个本地 fragment 引用没有悬空；26 个图引用全部是实际存在的独立本地原件。

内容执行核查对比实际派生而不是只看实现：core 1,116 个索引锚点顺序和名称／短定义／模块链接逐项一致，49 个非表格段落与语义对照表保留；rights 25 表、258 非空行、566 cells，risk 38 表、402 非空行、880 cells 均按原序匹配，rights 重复 Usage Note 未覆盖；六段 rights／risk pre 内容一致。主代理对 rules 的 31 表、732 cells 作顺序核对，三段 pre 全文精确且在该模块恰出现一次，并人工读解释／混合规则／trigger／funding 的实际消费者内容。

personal_data／process／processing／purposes 四模块 authored body 在仅归一化空白、Unicode 和 Markdown 包装后，全部可见文字顺序匹配；另作二十个 pre 的全文／顺序／缩进精确比较。processing 示例的十六个真实 TAB 保留在消费者 L13982 起代码块；personal_data 原 L3974 的 orphan Examples 在消费者 L12629–12630 保留；purposes ServiceManagement／ServiceProvision 原矛盾、process 全部组合适用条件、父链／Range includes、多行 Usage Note 及尾部资助均在。四模块十二个直接图引用顺序、本地路径和文件存在性全部匹配。

entities 的 110 表／2,658 cells／9 pre、legal_basis 的 158 表／3,520 cells／16 pre、TOM 的 237 表／5,560 cells／11 pre、context 的 174 表／4,042 cells／11 pre 同样逐表／逐块对照，不以数量代替内容判断；全部作者正文的展示格式归一化文字顺序一致，pre 则逐字符相等。ManageConsent 五条父链（D25835–25839）、ContractStatus 宽 range（D26726–26730）、hasNoticeLayer domain→range（D35013–35015）、裸 Examples 多链接（D30910–30911、D38877–38882）均保留，十个本地实引图路径按原序存在。四页完整 Contributions／Funding 及上游异常未静默纠正。这些是执行者的转换质量现证据，不是最终独立 evaluator PASS。

同一真实入口在 fetch_bytes 与 prepare_capsule 被替换为立即报错的条件下连续两次重放，47 文件逐字节不变；这证明所声明本批来源无需重新联网或清空原件才能预处理，不等于完整 ReSpec 离线运行时。

另从暂存 Git 候选树导出 `/tmp/llm-wiki-pr12-index.KDtw5O`，在隔离副本上同样禁网／禁止清空，重复两次入口重放，47 文件都逐字节一致。原件／许可／代码均来自索引导出，不依赖本机原下载目录；这是候选导出验证，不冒充远程 clone 或 main fresh checkout。

Python 3.12.13／pypdf 6.18.1 下实际运行 `make demo`、`make test`、`make validate`、`make reproducibility`：114 测试通过；215 manifests、2,931 inventory 文件、23,507 selectors 无错误／警告；48 篇文档、80 相对链接通过。许可台账最终履约状态冻结后重新运行 demo 及完整四阶段重放，最终 build 为 `build:llm-wiki-v0:ac56ea43f6b5393c`；committed-tree、full-demo、compiler-only、read-only-validation 四阶段各 169 生成文件均 byte-identical，不使用之前的中间 build。

默认 report-aware coverage auditor 实际 PASS。其他 130 项对象及原始 YAML 块、旧 93 条 rights 对象和原始文本保持不变，PR11 执行历史完整保留。当前 131 非 repo 的原件 complete 8、文本 complete 2／partial 29；本地完整可消费仍 2、unresolved 129、trusted 0。DPV 的下一步为有界图像语义消费评估，action bucket 为 ocr_assessment，但不要求安装 OCR，也不在本批假装已解决。精确汇总见本报告 frontmatter，与台账一致。

完整 `git diff --check` 实际 exit 2，共 34,825 处诊断，限十二原 HTML 与忠实派生 document 的上游空白／代码缩进等十三文件；不改原件来获取格式绿灯。排除这十三文件的 scoped 检查实际通过。index、两种 registry 的其他 214 UID 对象与 BASE 完全不变，selected／claims／evidence 无改动。

全库 publication 函数实际返回 active 93／audited 94、64 继承 blocks、2 继承 package 不一致错误（GraphRAG／CoScientist）；DPV 自身无 error／block。该结果与全库公开放行不同，不隐去历史待办。

独立 evaluator 必须在最终精确 HEAD／BASE 上分别判断需求满足、agentic 执行和核心质量；COMMENT 审核不冒充人类 APPROVE。三维 PASS 加同一 HEAD／BASE 的 CI success 后才正常 merge。任何 HEAD／BASE 改动使先前最终结论失效。

## 明确未完成

不修改其他 130 个非 repo／84 个 repo 对象，不扩大到扩展、primer、RDF／CSV、数据集、模型或整个引用网络；Issues #3／#4 不关闭，父 #1 仍待整合/main fresh checkout。P4 的 GraphRAG／CoScientist 两项历史 rights 包不一致及 coverage 历史依赖仍在后续范围，本批不声称全库 publication gate 通过。不强推、不删分支、不绕门控、不改保护。
