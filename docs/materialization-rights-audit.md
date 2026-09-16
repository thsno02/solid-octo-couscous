# 物化全文权利审计（Materialization Rights Audit）

## 结论

本审计逐条覆盖基线提交 <code>ee43cb37856bd40274bedda289a70dab03aaf3cc</code> 中 91 个 full_text 胶囊：73 篇 arXiv、17 份标准/词汇表、1 份方法文档。证据审计（evidence review）已完成，但权利清理（rights clearance）未完成。

- 51 条找到明确公众复制/再分发许可，分类为 <code>documented_permission</code>；这不表示当前胶囊已经履约。
- 40 条未找到面向公众/本仓库的适用许可，分类为 <code>permission_unverified</code>；不应公开再分发全文。
- 基线审计的 91 项中，七项 W3C、ODCS 3.2.0 定义首页、五项 arXiv、LinkML 文档首页及 Schema.org 文档快照已完成当前内容版本的许可包装，15 项为 <code>allow</code>；其余 76 项仍为 <code>block</code>。
- Apache Ossie 基线胶囊只有 7 bytes（# Home），不是实质标准全文；后续降级不删除其基线审计行。

当前 `full_text` 为 90 条，公开发布门检查结果为 `active_full_text=90 audited=91 blocked=75 errors=0`；整体仍未放行。75 项分为 40 项尚无适用公众许可证据、35 项已有许可证据但尚待履约，不应统称为缺少授权。审计覆盖数 91 与当前全文数 90 使用不同基线，不应混用。全文继续保存在本 GitHub repo；本次保留既有正文与快照，只补齐许可条件和传播信息，未移除作品、迁移存储或改写 Git 历史。

机器可读逐条记录：<code>raw_data/audits/materialization_rights_review.yaml</code>。本报告记录许可证据与已落实的包装条件，不是法律意见或人工批准。

## 判定模型（Decision Model）

只有权利人、发布机构、作品许可链接，或与确切版本对应的 LICENSE/NOTICE 明确覆盖复制与再分发时，才记为 documented_permission。HTTP 200、公开 URL、可下载、域名 allowlist、open/source_available 标签和 full_text_redistribution_assumed 均不足。

许可范围必须对象匹配：代码/模型/数据/模板/参考文献许可不能覆盖论文；平台获授分发权不能转授公众；CC/W3C/Apache 的署名、NOTICE、修改、NC、ND、SA 条件必须落实。

审查以实际保存的表达与具体权利声明为边界，不要求证明每句话原创。在作品版本对应、发布机构/作者明确许可且没有相反声明或具体风险迹象时，可以合理依赖该许可；纯书目事实、名称、URL、未保存的外链作品不要求另行授权。不能仅因论文含用户研究或模型样例，就要求调取参与者同意书、作者历史服务合同；正式论文之外已明确识别的第三方长摘录、软件或模板则分别履约。完整法条副本、四方包校验和双次重建是当前实现的校验办法，不是额外的人类批准或所有许可证一概要求的法律条件。

替代出版路径的版本对应（Version correspondence）也可以通过实际保存的表达与获许可出版内容的实质比对建立，不普遍要求作者另写精确 arXiv vN 确认信，更不要求 TeX 源包与出版 PDF 字节相同。相同题名或作者本身仍不足；发现正文、附录或第三方组件差异时须明确差异及其许可范围。旧审计中的“人工核对”“机器证明”描述待办或实现状态，不新增人类审批条件；尚未找到许可也不等于已经证明不存在任何其他授权。

论文正文完整保存，与源包中每个附带组件必须字节不变，是两个不同要求。当前尚未获得整理非正文组件的范围确认，因此没有删除参考文献里的第三方完整摘要，也没有改名或改写 LaTeX 模板来越过问题。若后续允许此类整理，仍须保留论文实际表达、说明转换、重建受影响的定位器，并通过相同许可门；不能只手工改当前胶囊而让下一次物化恢复旧问题。

### 知识编辑综述：已修改模板不能按未修改原版放行

[arXiv:2310.16218v4](https://arxiv.org/abs/2310.16218v4) 的 1,823,714-byte 固定源响应与现存 revision 和五个 source 成员对应，主论文 CC BY 4.0 明确；十个图像/PDF 成员原已省略，书目文件没有摘要字段。真正未满足的条件在 `acmart.cls`：从[官方 v1.90a Work](https://github.com/borisveytsman/acmart/tree/c7f908da9118fd3040fdadc998258af9dc992f0b)执行 `tex -no-shell-escape acmart.ins` 后对比，现存文件包含两处 Keywords 修改、五处页脚禁用，却继续使用原文件名和运行时身份。

因此不采用未修改编译产物的 LPPL §3 路径，也不把添加全局 NOTICE 当作全部履约。[LPPL 1.3c §6](https://www.latex-project.org/lppl/lppl-1-3c/)要求修改版身份、组件内变更说明或明确指向随包日志，以及原 Work 的取得信息。可行的最小修复是给修改版独立身份、保留原版权和七处变更日志、只重绑主 TeX 的类引用并重新生成受影响定位器；不必额外取得 ACM 授权或引入新的模板管理框架。当前未自行改源，仍保持 `block`。

| 维度 | 结果 |
|---|---:|
| 基线 full_text | 91 |
| documented_permission | 51 |
| permission_unverified | 40 |
| allow_after_conditions_met | 36 |
| allow_with_packaged_notice | 15 |
| do_not_redistribute_full_text | 40 |
| publication gate: allow | 15 |
| publication gate: block（基线项） | 76 |

### Robin / Kosmos：论文正文与额外收录的摘要分别判断

Robin 的固定 v1（13,149,222 bytes）与 Kosmos 的固定 v2（7,605,232 bytes）均对应既有源响应及全部保留的文字成员，主论文 CC BY 4.0 已核实。问题不是版本不明，而是 `references.bib` 额外收录了分别 88 和 80 个 `abstract` 字段，其中包含已识别的第三方完整摘要；不能把这些表达都当作纯书目事实，也不把网站短描述一律认定为完整摘要。

Robin 已定位两项公众许可依据缺口：[Dabrafenib 2013](https://link.springer.com/article/10.1007/s40265-013-0095-2) 与 [Aulakh 2018](https://academic.oup.com/jleukbio/article-abstract/104/1/147/6935662)。此判断不把付费墙本身当作再分发禁令，也不声称全部 88 项都禁止复制。另有明确 CC BY-NC 摘要，仍需确认实际用途。George Kour 模板存在官方 MIT 许可，可独立包装，不用论文许可代替。

Kosmos 的 `yan_systemic_2024` 保存旧预印本完整摘要及禁止未经许可再分发的明确声明，[官方 v1 记录](https://api.biorxiv.org/details/biorxiv/10.1101/2024.06.17.599454)为 `cc_no`；[后续期刊 BY4 版本](https://www.thno.org/v15p4016.htm)的摘要已重写，不能追溯覆盖旧表达。另有 BY-NC 摘要。文中“reproduced with permission”对应的图像原已省略，不把未保存媒体作为当前包的障碍。

这些是附带源文件的具体条件，并不推翻主论文的 BY4。两项继续保留全文、保持 `block`；在用户确认整理非正文组件的边界前，不删除摘要、不换成不同版本，也不把补充 NOTICE 冒充摘要授权。

### 三篇 AI 研究论文：共享旧组件的具体分发条件

AI Scientist v3、Agent Laboratory v2、AI Scientist-v2 v1 的固定源响应已分别对应既有 revision，论文均为 CC BY4；GDM 模板头明确 BY-SA4，范围独立。保留的 `natbib.sty` 8.31 在三包中一致，并与 [ICLR 官方固定副本](https://github.com/ICLR/Master-Template/blob/09727556f8eb5183f03d427d2a285711cc554888/natbib.sty)同字节；[CTAN 发布公告](https://ctan.org/ctan-ann/id/alpine.DEB.2.00.0907222144050.25678@wintermute.proteosys)确认其版本及 LPPL。并非这些论文没有许可或组件身份不明。

尚未闭合的是该文件头额外写明分发时须附原 `natbib.dtx`。LPPL 1.3c §3 本身不普遍要求未修改编译产物随附源码，但当前没有明确依据认定选择后续许可证版本就撤销这一具体声明。实际取得的历史小包为 8.31a，不能冒充 8.31；本轮有界查找到此停止，不下载整个 TeX 发行版，也不新增生产脚本。三项保持原文和 `block`，待对应原源码或明确公开解释后再包装。`fancyhdr` 没有同一声明，不把此条件扩张为全部 LPPL 组件的门槛。

AI Scientist-v2 七份匿名评审意见已独立核对：[OpenReview 条款](https://openreview.net/legal/terms)将受邀评审归入 CC BY4 评论，并区分许可与 API 可读性。仅两份有报告中明确的纳入同意说明，不虚称七份均获同样同意，也不虚构已匹配公开论坛。按原 Reviewer 编号、来源、路径和转换说明分别署名即可；不要求私密同意书或去匿名。这部分不是当前阻塞原因。

## 已落实的六项 W3C 许可包装（Packaged clearance）

- [DCAT 3 固定 Recommendation](https://www.w3.org/TR/2024/REC-vocab-dcat-3-20240822/) 与 [VC Data Model 2.0 固定 Recommendation](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) 的官方 HTML 响应均与现存 source revision 对齐；canonical metadata 的 `full_text_url` 固定到相应版本。
- 两者明确使用 [W3C Software and Document License 2023](https://www.w3.org/copyright/software-license-2023/)。完整 NOTICE 随胶囊入库，恢复原权利链接；原文保持不变，仅在末尾补充署名、转换说明与 NOTICE 链接，不移动既有 selector 行位置。
- [ODRL 2.2 固定 Recommendation](https://www.w3.org/TR/2018/REC-odrl-model-20180215/) 与 [JSON-LD 1.1 固定 Recommendation](https://www.w3.org/TR/2020/REC-json-ld11-20200716/) 使用 [2015 版许可](https://www.w3.org/copyright/software-license-2015/)，分别保留原 ©2018 和 ©2010–2020 W3C（MIT、ERCIM、Keio、Beihang）署名；共享完整 2015 NOTICE，不以新版版权主体替换旧版。两次从固定 HTML 输入重新物化的文件逐字节相同。
- [DID Core 1.0 固定 Recommendation](https://www.w3.org/TR/2022/REC-did-core-20220719/) 与 [OWL-Time 固定 Candidate Recommendation Draft](https://www.w3.org/TR/2022/CRD-owl-time-20221115/) 同样使用 2015 版许可，保留原 ©2022 W3C 版权。各自固定 HTML 与现存 revision 一致，完整重新物化两次逐字节一致，既有正文仅在文末补署名、来源和转换说明。`full_text_url` 与实际 requested/resolved URL 均为固定版本，不依赖 latest；selectors 的 URL 派生前缀随之重新绑定，数量、段落、行号与 preview 保持不变，派生索引同步重建。
- DID Core 的语法主体是其自身 DID 规则，RFC 规则名/语法引用与短归因引述不等同于另行保存整个 RFC 代码附件。OWL-Time 保留 W3C/OGC 联合项目、候选推荐草案及非背书声明；许可依据是固定 W3C 发布页的明确许可，不宣称另有 OGC 授权。实际包未保存独立 ISO/OGC 文档、图像或外链 ontology/RDF 文件。
- `W3C-20150513` 标识不是误用旧许可：[SPDX 官方说明](https://spdx.org/licenses/W3C-20150513.html)确认 2023 年的小幅修改继续使用该标识；具体许可 URL 仍记录为 2023 版。
- 清关只覆盖当前包内的规范文字及 selector 摘录，不扩展到外链作品、媒体、商标或专利。源版权头保留，未向包内加入外链媒体。
- 生成器每次从 canonical metadata 与共享 NOTICE 重新组装，不依赖手工补丁。声明的包与新全文 revision 不符会终止物化，而不会被降级为 metadata-only 后误过门控。
- 对这六项 `allow`，门控检查 canonical metadata、审计、胶囊 metadata、manifest 四方一致，并验证完整 NOTICE 和唯一的文末署名块；丢失声明、漏写审计包或替换 NOTICE 均失败。未将 Agent 核验写作 human approval。

### RDF 1.2：主文档与附录 RFC 代码分别履约

[RDF 1.2 Concepts and Abstract Data Model 固定 Candidate Recommendation Snapshot](https://www.w3.org/TR/2026/CR-rdf12-concepts-20260407/) 的附录 F 实际保存了 RFC3986、RFC3987、RFC6874 的合成 IRI ABNF，不是可以通过 scope 排除的外链。主文档按 W3C 2023 Software and Document License 包装，附录代码另按各自出版时的适用许可履约。

2005 年 1 月的 RFC3986/3987 适用 [RFC3667 §3.3(a)(E)](https://www.rfc-editor.org/rfc/rfc3667.html#section-3.3) 和 §5 通知条件；[IETF Trust 官方 FAQ](https://trustee.ietf.org/about/faq/)同时明确说明 2005 年 3 月以前代码的复用和修改路径。两篇原文未列禁止衍生声明，因此不需要新增作者授权，也不把后来的 BSD 追溯套给旧代码。两份 RFC 的作者、来源及原 Full Copyright Statement（含免责）在正文末注和组合 NOTICE 中保留。

RFC6874 的三条规则 `IP-literal`、`ZoneID`、`IPv6addrz` 按出版时生效的 [TLP4](https://trustee.ietf.org/wp-content/uploads/IETF-TLP-4.pdf) 履约。原声明中的 Simplified BSD 是历史误名：[IETF 官方更正](https://trustee.ietf.org/documents/trust-legal-provisions/tlp-5/)确认原文一直为三条款 Revised BSD，未修改许可文本。本包在实际包含代码的 `document.md` 末注内保存完整三条款、版权和免责，不只是外置 NOTICE，也不将代码许可套给 W3C 整文。

原正文和既有合成语法说明保持不变；固定 URL 重新绑定定位器的 URL 前缀，不改变定位顺序、行号或摘录内容。该项成为第七份已包装 W3C 文字包，仅覆盖当前实存文字和代码，不代表外链资源或其他 RFC 全文获得授权。

## 已落实的 PDF 版本许可与物化修复

[arXiv:2502.18864v2](https://arxiv.org/abs/2502.18864v2) 的标题为 *Accelerating scientific discovery with Co-Scientist*，官方固定版本标注 CC BY 4.0。固定 PDF 与 e-print 响应均为原 manifest 对应的 5,885,207 bytes、157 页 PDF；51 位作者按官方顺序完整署名。完整 [CC BY 4.0 法律文本](https://creativecommons.org/licenses/by/4.0/legalcode.txt)、来源链接和转换说明随包入库，原始 PDF 保持不变。v1 的 CC BY-NC-ND 4.0 不被替换或追溯豁免，本项 `allow` 仅绑定已验证的 v2。

旧管线误把 PDF 解码为 TeX，现以 `source/document.pdf` 和 `document.txt` 替换损坏的衍生文件。155 页有可提取文本；第 4、20 页的图示仍完整保留在 PDF 中，没有冒充 OCR 文本或生成虚假页定位器。因此保留 `full_text` 原件，状态为 `partial`、证据角色为 `bounded-excerpt`。许可核验覆盖实际保留的整个 PDF 与文本衍生物，而不是用抽取缺页缩小许可范围。全文扫描及代表页图像复核未发现另列第三方权利声明；外链数据未被复制入包。

门控对包含 `source_pdf` 的胶囊始终检查完整原件许可，即使文本提取失败导致其文本层级降为 metadata/excerpt，也不能绕过检查。版本、NOTICE、署名及审计与其他已许可包采用同一套一致性验证，不新增针对该 UID 的例外。

## 已落实的 ODCS 固定定义页许可包装

[ODCS v3.2.0 定义页](https://bitol-io.github.io/open-data-contract-standard/v3.2.0/) 的 63,735-byte HTML 与现存 revision 一致。官方 tag 对应 commit `f0bdad95346905d500be5ef4b2c2d9b1d95223b7`；[该版本的文档源文件](https://github.com/bitol-io/open-data-contract-standard/blob/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/docs/README.md) 自身标注 Bitol Contributors 版权和 `SPDX-License-Identifier: Apache-2.0`，不只是仓库根目录有许可证。完整 Apache-2.0 文本随包保存，恢复版权/SPDX、来源及修改说明；上游 tag 没有 NOTICE，本地 `NOTICE.md` 是本仓库的许可载体，不冒充上游文件。

本项只清理实际保存的定义首页文字（包装前 1,454 bytes）及 27 个 selectors，不宣称已物化或许可审核了整套多页标准。15 个外链章节、完整示例、JSON Schema、Bitol logo、Material 主题、Font Awesome 图标/字体均未进入当前包；原商标提示保留。`full_text` 表示当前单页来源的文字层级，不等同于整个网站的覆盖率。

顶层 `full_text_url`、许可包版本 URL 与 manifest requested/resolved URL 均固定到 `/v3.2.0/`。两次真实固定 URL 重新物化逐字节一致；原正文保留，仅追加许可块，selectors 除 URL 派生前缀外的定位字段不变。复用现有包装机制，没有新增 pipeline 代码或 workflow。

## 已落实的 TeX 文本与组件许可包装

[arXiv:2607.07663v2](https://arxiv.org/abs/2607.07663v2) 的固定 source archive 为 5,313,742 bytes，与现存 revision 一致；官方页面列出 Mingguang Chen、Licheng Wang、Bo Qu 三位作者及 CC BY 4.0 许可。版本固定到 v2，不把该结论追溯至 v1。实际胶囊保存四个 source 文字成员、两个 normalized 文件及 17 个 selectors；六张 PNG 原本就未保存，不能称为完整图文 archive。

独立复核识别出 `main.tex` 导言中的 Pandoc 默认模板片段。因此组合 NOTICE 分别保存论文的完整 CC BY 4.0 法律文本，以及 [Pandoc 官方模板 BSD 3-Clause 声明](https://github.com/jgm/pandoc-templates/blob/c27ad9128fa744fd6fe301416d274db9c1dea2a4/README.markdown)中的原版权、三项条件与免责声明。固定官方模板中的显著片段与本地导言对应，但没有据此虚构作者实际使用的 Pandoc 版本。不能仅用论文许可或 scope 排除语跳过实际保存的第三方模板。

`00README.json` 是 [arXiv 自动生成的编译元数据](https://info.arxiv.org/help/00README.html)，依据[提交协议的 metadata CC0 条款](https://info.arxiv.org/help/policies/submission_agreement.html#metadata-license)单独标记，不归因为论文作者原创。`references.bib` 的 1,274 条书目与 `main.bbl` 的 196 条排版记录不包含所引作品正文，也不授权那些作品。

通用包装器现在显式识别 `normalized/document.txt` 为正文，并从正文所在目录生成 `../NOTICE.md` 链接。校验器使用同一相对路径规则，拒绝错误链接；重复包装保持唯一附注。两次真实固定 v2 物化结果逐字节一致，四个 source 文件、`normalized/document.tex` 和 17 个 selectors 相对原包保持不变，预处理正文只追加组合署名块。此前八个根目录正文包的附注格式不变；没有新增独立脚本、UID 特例或 workflow。

## PaperQA2 的分层组件许可与派生传播

[PaperQA2 arXiv:2409.13740v2](https://arxiv.org/abs/2409.13740v2) 的固定源包为 4,646,196 bytes，与既有 revision 一致。当前保留七个 source 文字成员、28 个 selectors，13 个图片/PDF 成员原已省略；不宣称包含完整图文 archive。论文九位作者完整署名，作者材料与其文本转换按 CC BY-SA 4.0 分发。

实际独立组件分别履约：Moulay A. Akhloufi 的 PRIME 模板改编依据[作者 Overleaf 模板页](https://www.overleaf.com/latex/templates/arxiv-and-prime-ai-style-template/qdnhqytdqzsc)使用 CC BY 4.0；George Kour 基础模板保留原版权与 MIT。`references.bib` 唯一的摘要字段对应 [PubMedQA](https://aclanthology.org/D19-1259/)，与固定 ACL XML 的摘要规范化后对应，按 [ACL 2019 材料适用的 CC BY 4.0](https://aclanthology.org/faq/copyright/)保留五作者、来源及许可。没有假定 ACL metadata 为 CC0，也没有把论文许可外推到 PubMedQA 数据集、底层 PubMed 摘要或所引作品。

三份完整许可文本随 NOTICE 保存；四个权利范围独立标明。两次真实固定 v2 重建的 15 个胶囊文件一致，source、规范化 TeX 与 selectors 保持，正文仅追加许可附注。此项成为第十二项 `allow`，仅限所记录版本与实际保留内容。

派生管线复用通用许可传播模块（Rights propagation），将来源的声明包与版本化引用传递到 evidence、claim、Wiki 页面及机器视图。来源表达与收集者评述分开，缺包显式 `unavailable`，混合页面不把某一组件的许可套到整库独立作品。结构校验不代替此处逐来源的使用与发布判断。

## 自演化 Agent 综述：论文、模板与三份摘要分别履约

[arXiv:2507.21046v4](https://arxiv.org/abs/2507.21046v4) 的固定源响应为 3,856,523 bytes，与既有 revision 一致；canonical 更新为该版本的完整题名及 27 位作者。当前保存 19 个 source 文字成员、135 个定位器，八个非文本成员原已省略。论文作者材料按 CC BY4，不能据此覆盖附带模板或第三方摘要。

[TMLR 官方作者指南](https://jmlr.org/tmlr/author-guide.html)链接的[固定模板仓库](https://github.com/JmlrOrg/tmlr-style-file/tree/7bf90efe3a0debbba703c05c43f3ff7e4d4a2992)与实存三个组件逐字对应：`tmlr.sty` 依 Apache 2.0，`tmlr.bst` 和 `fancyhdr.sty` 各保留原 LPPL 授予、署名与身份，本包选择 LPPL 1.3c。仓库 Apache 不覆盖组件内另列的 LPPL；本包没有保存 `natbib.sty`，外部依赖声明不构成复制该组件。完整三份法条随组合 NOTICE 保存，不暗示上游为此胶囊提供支持。

`main.bib` 实际有三份额外摘要。[AppBench](https://aclanthology.org/2024.emnlp-main.856/) 与 [ARIA](https://aclanthology.org/2025.emnlp-industry.115/)对应 ACL 官方摘要，按其 BY4 分别署名；[ACM tool-learning tutorial](https://doi.org/10.1145/3626772.3661381)的 DOI、题名、五作者和页码对应 [ACM 提交的 Crossref 作品记录](https://api.crossref.org/works/10.1145/3626772.3661381)，该记录明确 VOR 的 CC BY4，自 2024-07-10 起生效。它不是 metadata CC0 或“可免费阅读”推断；记录没有摘要正文，未声称完成 ACM PDF/摘要逐字核验。在确切作品对应且无相反声明的情况下，可合理依赖正式许可记录，不额外要求取得 PDF 页眉。

全部 source、规范化 TeX 和定位器保持，正文只增加署名附注。集成时发现修改说明中的相对 Markdown 链接传播到 Wiki 后失效；将该描述改为纯文本后，胶囊生成器仍产生正确的真实 NOTICE 链接，无需新增链接重写器或放宽校验。

## Streaming Knowledge Compilation：正文与官方模板分别署名

[arXiv:2606.09877v1](https://arxiv.org/abs/2606.09877v1) 的固定 48,158-byte 源响应与既有 revision 和全部四个 source 成员对应。Juan M. Huerta 的论文采用 CC BY4；没有省略成员，72 条书目无额外摘要字段。正文的新闻提示为占位符，具体新闻标题明确标为合成示例；没有保存底层新闻或 Wikipedia 长篇文本。

模板另有独立依据：[NeurIPS 2026 Program Chairs 官方模板页](https://www.overleaf.com/latex/templates/formatting-instructions-for-neurips-2026/bjdwqfdkyftc)明确 CC BY4。对比[会议官网模板 ZIP](https://media.neurips.cc/Conferences/NeurIPS2026/Formatting_Instructions_For_NeurIPS_2026.zip)，现存 `neurips_2026.sty` 仅少六行 education-option 块，其他表达和版本标识对应。包装保留 Program Chairs、Roman Garnett 及原作者线索，披露这一既存差异，不虚构修改者或历史下载版本；当前许可不自动外推其他年份模板。

本项复用已有完整 CC BY4 NOTICE，主文和模板分别归属，arXiv 事实编译元数据单列 CC0。独立复核发现 canonical metadata 的重复旧 URL 会覆盖新固定 URL，删除重复项后重新执行两次真实 v1 物化，12 个胶囊文件一致。原四份 source、规范化 TeX 和 98 个定位器不变，正文精确为原内容加唯一末尾许可附注；本仓库未改模板或论文表达。

## 已包装但未放行：Zep 的非商业用途条件

[Zep arXiv:2501.13956v1](https://arxiv.org/abs/2501.13956v1) 的 22,911-byte 固定源包已与现存 revision 对应。论文的 CC BY-NC-SA 4.0、Moulay PRIME 改编的 CC BY 4.0 与 George Kour 基础模板的 MIT 分别保存。Zep 与 PaperQA2 模板仅页码开关一行不同，未将该变体归为 Zep 作者原创；五位论文作者、来源及修改说明已补齐。两次固定 v1 物化一致，四个 source 文件、规范化 TeX 与 29 个 selectors 不变，规范化正文仅追加许可附注。

这项仍为 `block`，不计入已放行来源：实际使用是否满足非商业（NonCommercial）条件尚待确认。其判断标准是该使用是否主要旨在或指向商业利益或金钱报酬，不是简单判断仓库是否公开、使用者是否营利或是否标成研究项目。派生内容保留归属、许可与适用的相同方式共享（ShareAlike）条件；通用传播已实现，但不替代实际用途的确认，也不把某一来源的 SA 条件自动套到整个仓库的独立作品。

## LinkML 单页许可包装与必要证据边界

[LinkML 文档首页](https://linkml.io/linkml/) 的实际 55,141-byte HTML 与既有 revision 一致。同部署的 [View source](https://linkml.io/linkml/_sources/index.rst.txt) 为 2,493-byte RST，与[固定官方源码](https://github.com/linkml/linkml/blob/2ed83cabd15294ef1fa406007ce12e850a151b81/docs/index.rst)逐字节相同。页面自身的 Apache-2.0 声明、官方仓库对应的文档源与根 LICENSE 无文档例外，共同构成当前已存文字的许可证据；`docs/conf.py` 的 ©2021–2026 LinkML Authors 与页面版权对应。

这里证明的是源内容对应（source-content correspondence），不是整个站点的精确部署 commit，也不是 HTML、RST、Markdown 三者字节相同。之前将整个 deployment commit 的证明列为必要清权条件，超出了当前许可所需证据；本次纠正这个额外条件，不降低实际 payload revision 的绑定要求。

完整 Apache-2.0、原版权、来源与转换说明已随包保存；上游证据 commit 没有 NOTICE，本地文件仅作为许可载体。两次真实重建一致，附注前 7,340-byte Markdown 正文保持完整前缀，164 个 selectors 未变。范围仅限这份单页转换文本，不宣称其他文档页、主题、JS/CSS、媒体或外链已获授权。未来页面 revision 改变会继续触发重新核验。

## Schema.org 已存快照与同许可共享（ShareAlike）

当前包保留的是物化清单标记为 2026-09-13 的 [Schemas 文档页](https://schema.org/docs/schemas.html)内容快照，所记录的原 HTML 响应为 12,007 bytes、revision 为 `f62a658dd54f9185572242dd6e97df94b201c73132e744d4f078c66b2f51e0d3`。这不是 metadata 的 2026-09-09 收集日期，也不把 `generated_at` 冒充独立的网络获取日志。该 URL 可变；当前线上页面已变化，不能把旧快照命名为新的 release，也不能借重新抓取覆盖既有正文。

官方 [Terms](https://schema.org/docs/terms.html)与 [FAQ](https://schema.org/docs/faq.html#18)明确将 supporting documentation 纳入 CC BY-SA 3.0；历史官方 FAQ 与 Terms 已包含同一授权，许可不因后续网页更新而自动消失。完整 CC BY-SA 3.0 法律文本、Schema.org/Sponsors 归属、来源和转换说明随包入库，并明确本 Markdown 适配物与同源 selector 摘录按 CC BY-SA 3.0 分发。未据此重新许可 collection 中的独立作品；后续引用或派生仍须分别满足适用条件。

本项只对现存 2,982-byte 正文和 34 个 selectors 进行离线许可包装，保留旧 revision、retrieval 和正文前缀。原页面仅提及 GS1、Croissant 等外部资源，未保存那些网站的正文、媒体或软件；商标和专利不在此文本许可范围。重复 finalize 幂等，不宣称进行了两次旧 URL 网络重建；新响应若与该包 revision 不同，现有生产管线会拒绝复用旧许可包。

## 本轮未放行的具体边界

- ICML 家族的 2022/2024/2025 官方 author kit 已做有界检查：主 `.sty` 尚未见明确公众再分发授权，独立 `.bst` 和 `fancyhdr` 的 LPPL 不能覆盖它。`algorithm/algorithmic` 的官方当前包是 LGPL 2.1，不是 LPPL，旧件仍须对应后分别履约。投稿模式的“Do not distribute”是条件输出，不被当作模板禁令；PaperBench 的同名 `arxiv.sty` 是 ICML 派生件，不能误套 George Kour 模板的 MIT。这四项没有据此放行，也没有删减正文。
- OWL 2、R2RML 与 SHACL 的 dated TR HTML 已与现存 revision 对齐。W3C [2015 General Document License](https://www.w3.org/copyright/document-license-2015/)及[FAQ](https://www.w3.org/Consortium/Legal/IPR-FAQ-20000620-new.html#2015published)提供旧 TR 的有限派生使用路径，但没有普遍开放重格式化。当前知识消化语料是否符合软件实现支持用途，以及表格/链接结构丢失是否保留含义，仍缺充分依据；不能靠附上“非规范”标签或给代码示例套软件许可来放行整个规范主体。这三项保持 `block`，不删除正文。
- GraphRAG 的固定 arXiv v2 与现存包已对齐，但实际保存的 `neurips_2024.sty` 尚缺明确再分发依据。匿名投稿页脚中的 “Do not distribute” 不是样式文件自身的禁止分发条款；我们既不错误认定它禁止，也不把可下载当作授权。
- Robin 与 Kosmos 的 `references.bib` 分别含 88、80 个摘要字段及 15、31 个版权字段，不是纯书目。需按实际保存的第三方摘要逐项核清许可，不能只用论文作者的 CC BY 覆盖；这不表示所有摘要都不可分发，当前证据仍不足。

WikiChat 新找到[作者官方公告](https://github.com/stanford-oval/WikiChat)与 [arXiv v2](https://arxiv.org/abs/2305.14292v2)的同日 camera-ready 版本绑定，连同 [ACL 出版记录](https://aclanthology.org/2023.findings-emnlp.157/)和[版权政策](https://aclanthology.org/faq/copyright/)，支持将作者论文正文记为 `documented_permission / CC-BY-4.0`。这不是整个 archive 的放行：`emnlp2023.sty`、`acl_natbib.bst` 等第三方组件及 NOTICE 仍需核清，门控保持 `block`。FActScore、ALCE、RAGTruth、STORM 与 WikiContradict 的替代出版路径尚未形成适用于现存版本的充分公众许可链；相似文本、相同标题或代码/数据许可证都不单独补足这个缺口。

本次对上述待办作了进一步有界核验和纠错：

- ALCE 的[正式 ACL 出版内容](https://aclanthology.org/2023.emnlp-main.398/)有 BY4 路径，主体及附录主干与本地对应；阻碍不再笼统表述为缺少作者精确版本声明。本地附录额外三段 Open-source Models 及 Stable Beluga 2 结果行，未出现在正式出版 PDF 或作者仓库论文副本中，需继续核对这些具体表达的适用许可。两份额外摘要分别有 ACL 作品级许可入口，模板也有官方 Overleaf BY4 线索，但实际组件对应与包装未完成；整包仍为 block。
- Progressive Neural Networks 实存 March 2016 模板尚缺覆盖实际版本的公众许可依据；Darwin Gödel Machine 包含 ICLR2026 模板及有原源码随附条件的 natbib 8.31。这些是有界组件发现，未冒称已经核对整包固定版本，也不将投稿页脚的 Do not distribute 当作模板禁令。
- GEM 的一条替代出版商证据曾错配另一篇作品。已在机器审计中明确排除该条对 GEM 的证明作用并保留纠错历史；官方 GEM 题名、作者、NIPS2017 出版信息和版本史与原错配记录不同。此次纠错不新增或否定 GEM 的公众许可，不改变其门控。

## 来源族发现（Source-family Findings）

- arXiv：32 篇官方文章页链接 CC；WikiChat 另由作者的确切 camera-ready 版本声明与 ACL 出版许可形成正文授权链。其余 40 篇仍缺适用公众许可证据；arXiv non-exclusive/历史 assumed license 本身不授予公众再分发权。
- W3C：7 份页面采用可修改的 Software and Document License；7 份旧页面采用限制一般衍生的 Document License。
- Apache/LinkML/ODCS：ODCS 固定定义首页与 LinkML 当前文档首页已分别完成 Apache-2.0 包装；范围不扩展到各自整个站点。
- Schema.org：已为当前 supporting-documentation 快照恢复 Terms、来源、署名、修改说明和 CC BY-SA 3.0 适配物许可；未来新版本仍需重新核验。

## 人工审核与权利确认（Human Review and Clearance）

逐条证据审核已经完成，许可履约仍未全量完成。已完成包装、待履约与尚缺适用许可的数量，以本文开头的结论及机器审计汇总为准，避免在此重复维护计数。未核实记录仍需适用授权或与确切作品版本绑定的新权威许可证据。客观许可履约不默认要求另行人工批准，但 Agent 也不能代替权利人授予新许可；整体自动上传继续失败关闭（fail closed）。

## 逐条审计（91 items）

| # | UID | 路径 | 已见证据 | 缺失项 | 分类 | 公开再分发建议 |
|---:|---|---|---|---|---|---|
| 1 | <code>arxiv-1606.04671</code> | <code>materialized_sources/corpus/arxiv-1606.04671--2b4672cf/manifest.yaml</code><br><code>raw_data/arxiv/Progressive Neural Networks/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>metadata_only</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 2 | <code>arxiv-1705.05742</code> | <code>materialized_sources/corpus/arxiv-1705.05742--6e18ab25/manifest.yaml</code><br><code>raw_data/arxiv/Know-Evolve Deep Temporal Reasoning for Dynamic Knowledge Graphs/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 3 | <code>arxiv-1706.08840</code> | <code>materialized_sources/corpus/arxiv-1706.08840--acb7e7ed/manifest.yaml</code><br><code>raw_data/arxiv/Gradient Episodic Memory for Continual Learning/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 4 | <code>arxiv-1809.10697</code> | <code>materialized_sources/corpus/arxiv-1809.10697--798152f6/manifest.yaml</code><br><code>raw_data/arxiv/DyRep Learning Representations over Dynamic Graphs/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 5 | <code>arxiv-1904.05530</code> | <code>materialized_sources/corpus/arxiv-1904.05530--cddfa770/manifest.yaml</code><br><code>raw_data/arxiv/Recurrent Event Network for Reasoning over Temporal Knowledge Graphs/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 6 | <code>arxiv-2104.00405</code> | <code>materialized_sources/corpus/arxiv-2104.00405--93b3bffb/manifest.yaml</code><br><code>raw_data/arxiv/Avalanche an End-to-End Library for Continual Learning/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 7 | <code>arxiv-2110.11309</code> | <code>materialized_sources/corpus/arxiv-2110.11309--d5da3395/manifest.yaml</code><br><code>raw_data/arxiv/Fast Model Editing at Scale/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>metadata_only</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 8 | <code>arxiv-2202.05262</code> | <code>materialized_sources/corpus/arxiv-2202.05262--f62c1586/manifest.yaml</code><br><code>raw_data/arxiv/Locating and Editing Factual Associations in GPT/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 9 | <code>arxiv-2206.06520</code> | <code>materialized_sources/corpus/arxiv-2206.06520--f7ce3f6e/manifest.yaml</code><br><code>raw_data/arxiv/Memory-Based Model Editing at Scale/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>metadata_only</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 10 | <code>arxiv-2210.07229</code> | <code>materialized_sources/corpus/arxiv-2210.07229--06f64fc5/manifest.yaml</code><br><code>raw_data/arxiv/Mass-Editing Memory in a Transformer/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 11 | <code>arxiv-2306.15626</code> | <code>materialized_sources/corpus/arxiv-2306.15626--438dfbd9/manifest.yaml</code><br><code>raw_data/arxiv/LeanDojo Theorem Proving with Retrieval-Augmented Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 12 | <code>arxiv:1112.5309</code> | <code>materialized_sources/corpus/arxiv-1112.5309--a2413513/manifest.yaml</code><br><code>raw_data/arxiv/POWERPLAY: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 13 | <code>arxiv:1504.04909</code> | <code>materialized_sources/corpus/arxiv-1504.04909--f3bc15fa/manifest.yaml</code><br><code>raw_data/arxiv/Illuminating search spaces by mapping elites/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 14 | <code>arxiv:1605.03142</code> | <code>materialized_sources/corpus/arxiv-1605.03142--8845b857/manifest.yaml</code><br><code>raw_data/arxiv/Self-Modification of Policy and Utility Function in Rational Agents/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 15 | <code>arxiv:1606.04474</code> | <code>materialized_sources/corpus/arxiv-1606.04474--7003a57b/manifest.yaml</code><br><code>raw_data/arxiv/Learning to learn by gradient descent by gradient descent/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 16 | <code>arxiv:1711.09846</code> | <code>materialized_sources/corpus/arxiv-1711.09846--c863a793/manifest.yaml</code><br><code>raw_data/arxiv/Population Based Training of Neural Networks/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 17 | <code>arxiv:1801.10198</code> | <code>materialized_sources/corpus/arxiv-1801.10198--71f31d71/manifest.yaml</code><br><code>raw_data/arxiv/Generating Wikipedia by Summarizing Long Sequences/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 18 | <code>arxiv:1901.01753</code> | <code>materialized_sources/corpus/arxiv-1901.01753--774aac9a/manifest.yaml</code><br><code>raw_data/arxiv/Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 19 | <code>arxiv:1905.10985</code> | <code>materialized_sources/corpus/arxiv-1905.10985--50978b7d/manifest.yaml</code><br><code>raw_data/arxiv/AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 20 | <code>arxiv:1906.01820</code> | <code>materialized_sources/corpus/arxiv-1906.01820--d2306d3e/manifest.yaml</code><br><code>raw_data/arxiv/Risks from Learned Optimization in Advanced Machine Learning Systems/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 21 | <code>arxiv:1912.01683</code> | <code>materialized_sources/corpus/arxiv-1912.01683--074c13b2/manifest.yaml</code><br><code>raw_data/arxiv/Optimal Policies Tend to Seek Power/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 22 | <code>arxiv:2206.08896</code> | <code>materialized_sources/corpus/arxiv-2206.08896--d2b63071/manifest.yaml</code><br><code>raw_data/arxiv/Evolution through Large Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 23 | <code>arxiv:2210.08726</code> | <code>materialized_sources/corpus/arxiv-2210.08726--8e79abf3/manifest.yaml</code><br><code>raw_data/arxiv/RARR: Researching and Revising What Language Models Say, Using Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 24 | <code>arxiv:2210.11610</code> | <code>materialized_sources/corpus/arxiv-2210.11610--122d6152/manifest.yaml</code><br><code>raw_data/arxiv/Large Language Models Can Self-Improve/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 25 | <code>arxiv:2304.05376</code> | <code>materialized_sources/corpus/arxiv-2304.05376--4e0dcba3/manifest.yaml</code><br><code>raw_data/arxiv/ChemCrow: Augmenting large-language models with chemistry tools/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 26 | <code>arxiv:2305.14251</code> | <code>materialized_sources/corpus/arxiv-2305.14251--582edc7d/manifest.yaml</code><br><code>raw_data/arxiv/FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 27 | <code>arxiv:2305.14292</code> | <code>materialized_sources/corpus/arxiv-2305.14292--5b8a65bd/manifest.yaml</code><br><code>raw_data/arxiv/WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia/metadata.yaml</code> | CC-BY-4.0；作者2023-10-27 camera-ready公告、固定arXiv v2与ACL DOI/许可对应；仅作者论文表达 | 第三方TeX组件范围及NOTICE履约尚未完成 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 28 | <code>arxiv:2305.14627</code> | <code>materialized_sources/corpus/arxiv-2305.14627--6d5b37c6/manifest.yaml</code><br><code>raw_data/arxiv/Enabling Large Language Models to Generate Text with Citations/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 29 | <code>arxiv:2310.02304</code> | <code>materialized_sources/corpus/arxiv-2310.02304--0938f3f9/manifest.yaml</code><br><code>raw_data/arxiv/Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 30 | <code>arxiv:2310.11511</code> | <code>materialized_sources/corpus/arxiv-2310.11511--2a23ab40/manifest.yaml</code><br><code>raw_data/arxiv/Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 31 | <code>arxiv:2310.16218</code> | <code>materialized_sources/corpus/arxiv-2310.16218--21c4a191/manifest.yaml</code><br><code>raw_data/arxiv/Knowledge Editing for Large Language Models: A Survey/metadata.yaml</code> | 固定 v4 与既有源成员对应；主论文 BY4，acmart 明确 LPPL | 现存 acmart 有七处修改却沿用原版身份；需依 LPPL §6 整理组件 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 32 | <code>arxiv:2401.00396</code> | <code>materialized_sources/corpus/arxiv-2401.00396--5292590c/manifest.yaml</code><br><code>raw_data/arxiv/RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 33 | <code>arxiv:2401.10020</code> | <code>materialized_sources/corpus/arxiv-2401.10020--9bd6f28f/manifest.yaml</code><br><code>raw_data/arxiv/Self-Rewarding Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 34 | <code>arxiv:2402.04624</code> | <code>materialized_sources/corpus/arxiv-2402.04624--c3e9e366/manifest.yaml</code><br><code>raw_data/arxiv/MEMORYLLM: Towards Self-Updatable Large Language Models/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 35 | <code>arxiv:2402.14207</code> | <code>materialized_sources/corpus/arxiv-2402.14207--b99559f4/manifest.yaml</code><br><code>raw_data/arxiv/Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 36 | <code>arxiv:2402.18264</code> | <code>materialized_sources/corpus/arxiv-2402.18264--ebc0e524/manifest.yaml</code><br><code>raw_data/arxiv/WIKIGENBENCH: Exploring Full-length Wikipedia Generation under Real-World Scenario/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>metadata_only</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 37 | <code>arxiv:2404.07738</code> | <code>materialized_sources/corpus/arxiv-2404.07738--3e68f613/manifest.yaml</code><br><code>raw_data/arxiv/ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 38 | <code>arxiv:2404.14387</code> | <code>materialized_sources/corpus/arxiv-2404.14387--a0c7dbc0/manifest.yaml</code><br><code>raw_data/arxiv/A Survey on Self-Evolution of Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 39 | <code>arxiv:2404.16130</code> | <code>materialized_sources/corpus/arxiv-2404.16130--fe9ed9e5/manifest.yaml</code><br><code>raw_data/arxiv/From Local to Global: A Graph RAG Approach to Query-Focused Summarization/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 40 | <code>arxiv:2405.14768</code> | <code>materialized_sources/corpus/arxiv-2405.14768--80dba2af/manifest.yaml</code><br><code>raw_data/arxiv/WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 41 | <code>arxiv:2405.14831</code> | <code>materialized_sources/corpus/arxiv-2405.14831--e17ccf48/manifest.yaml</code><br><code>raw_data/arxiv/HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 42 | <code>arxiv:2406.04268</code> | <code>materialized_sources/corpus/arxiv-2406.04268--ce5afac4/manifest.yaml</code><br><code>raw_data/arxiv/Position: Open-Endedness is Essential for Artificial Superhuman Intelligence/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 43 | <code>arxiv:2406.06769</code> | <code>materialized_sources/corpus/arxiv-2406.06769--d1971e3b/manifest.yaml</code><br><code>raw_data/arxiv/DISCOVERYWORLD: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents/metadata.yaml</code> | <code>CC-BY-SA-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-SA-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 44 | <code>arxiv:2406.13805</code> | <code>materialized_sources/corpus/arxiv-2406.13805--21c7c163/manifest.yaml</code><br><code>raw_data/arxiv/WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 45 | <code>arxiv:2408.06292</code> | <code>materialized_sources/corpus/arxiv-2408.06292--522d359c/manifest.yaml</code><br><code>raw_data/arxiv/The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery/metadata.yaml</code> | 固定 v3 与既有源包对应；论文 BY4、GDM BY-SA4、natbib LPPL 分别识别 | natbib 8.31 头的原源码条件待闭合；不以 8.31a 代替，不删正文 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 46 | <code>arxiv:2408.08435</code> | <code>materialized_sources/corpus/arxiv-2408.08435--dc6e6730/manifest.yaml</code><br><code>raw_data/arxiv/Automated Design of Agentic Systems/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 47 | <code>arxiv:2408.15232</code> | <code>materialized_sources/corpus/arxiv-2408.15232--a890ae4f/manifest.yaml</code><br><code>raw_data/arxiv/Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 48 | <code>arxiv:2409.13740</code> | <code>materialized_sources/corpus/arxiv-2409.13740--66861ff1/manifest.yaml</code><br><code>raw_data/arxiv/Language agents achieve superhuman synthesis of scientific knowledge/metadata.yaml</code> | 固定v2论文CC BY-SA4、PRIME改编BY4、基础MIT与PubMedQA摘要BY4分别履约；access=open，assumed=false | 当前实际包已完成版本、署名、NOTICE和转换声明 | <code>documented_permission</code> | 已包装放行；当前 gate=allow |
| 49 | <code>arxiv:2410.04444</code> | <code>materialized_sources/corpus/arxiv-2410.04444--2b1bb2d2/manifest.yaml</code><br><code>raw_data/arxiv/Goedel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 50 | <code>arxiv:2410.05779</code> | <code>materialized_sources/corpus/arxiv-2410.05779--5b53b22b/manifest.yaml</code><br><code>raw_data/arxiv/LightRAG: Simple and Fast Retrieval-Augmented Generation/metadata.yaml</code> | <code>CC-BY-NC-SA-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-NC-SA-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 51 | <code>arxiv:2410.07095</code> | <code>materialized_sources/corpus/arxiv-2410.07095--b72cdb8f/manifest.yaml</code><br><code>raw_data/arxiv/MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 52 | <code>arxiv:2410.10762</code> | <code>materialized_sources/corpus/arxiv-2410.10762--72c09413/manifest.yaml</code><br><code>raw_data/arxiv/AFlow: Automating Agentic Workflow Generation/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 53 | <code>arxiv:2411.14199</code> | <code>materialized_sources/corpus/arxiv-2411.14199--e07b84a9/manifest.yaml</code><br><code>raw_data/arxiv/OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 54 | <code>arxiv:2501.04227</code> | <code>materialized_sources/corpus/arxiv-2501.04227--a0515b2c/manifest.yaml</code><br><code>raw_data/arxiv/Agent Laboratory: Using LLM Agents as Research Assistants/metadata.yaml</code> | 固定 v2 与既有源包对应；论文 BY4、GDM BY-SA4、natbib LPPL 分别识别 | natbib 8.31 头的原源码条件待闭合；不以 8.31a 代替，不删正文 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 55 | <code>arxiv:2501.13956</code> | <code>materialized_sources/corpus/arxiv-2501.13956--b93a114f/manifest.yaml</code><br><code>raw_data/arxiv/Zep: A Temporal Knowledge Graph Architecture for Agent Memory/metadata.yaml</code> | 固定v1论文CC BY-NC-SA4、PRIME改编BY4与基础MIT分别完成NOTICE；access=restricted，assumed=false | 实际NC用途尚待确认；许可传递不替代用途判断 | <code>documented_permission</code> | 源包已包装但不等于发布批准；当前 gate=block |
| 56 | <code>arxiv:2502.12110</code> | <code>materialized_sources/corpus/arxiv-2502.12110--d27d79d8/manifest.yaml</code><br><code>raw_data/arxiv/A-MEM: Agentic Memory for LLM Agents/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 57 | <code>arxiv:2502.14499</code> | <code>materialized_sources/corpus/arxiv-2502.14499--a7f1a2e8/manifest.yaml</code><br><code>raw_data/arxiv/MLGym: A New Framework and Benchmark for Advancing AI Research Agents/metadata.yaml</code> | <code>CC-BY-NC-SA-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-NC-SA-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 58 | <code>arxiv:2502.18864</code> | <code>materialized_sources/corpus/arxiv-2502.18864--014b4710/manifest.yaml</code><br><code>raw_data/arxiv/Towards an AI co-scientist/metadata.yaml</code> | 固定 v2 的 <code>CC-BY-4.0</code>；原始 PDF、51 作者、完整 NOTICE 与文本转换说明均已绑定 | 无；抽取缺页 4/20 如实标记 partial，不影响 PDF 原件留存 | <code>documented_permission</code> | 仅当前已验证 v2 包 gate=allow；不覆盖 v1 或未来版本 |
| 59 | <code>arxiv:2503.18102</code> | <code>materialized_sources/corpus/arxiv-2503.18102--1133e9d5/manifest.yaml</code><br><code>raw_data/arxiv/AgentRxiv: Towards Collaborative Autonomous Research/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 60 | <code>arxiv:2504.01848</code> | <code>materialized_sources/corpus/arxiv-2504.01848--006ccffe/manifest.yaml</code><br><code>raw_data/arxiv/PaperBench: Evaluating AI's Ability to Replicate AI Research/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 61 | <code>arxiv:2504.03160</code> | <code>materialized_sources/corpus/arxiv-2504.03160--0f30d3ca/manifest.yaml</code><br><code>raw_data/arxiv/DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 62 | <code>arxiv:2504.08066</code> | <code>materialized_sources/corpus/arxiv-2504.08066--22ed15f2/manifest.yaml</code><br><code>raw_data/arxiv/The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search/metadata.yaml</code> | 固定 v1 与既有源包对应；论文 BY4、GDM BY-SA4、natbib LPPL 分别识别 | natbib 8.31 头的原源码条件待闭合；不以 8.31a 代替，不删正文 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 63 | <code>arxiv:2505.13400</code> | <code>materialized_sources/corpus/arxiv-2505.13400--6cb0cfb6/manifest.yaml</code><br><code>raw_data/arxiv/Robin: A multi-agent system for automating scientific discovery/metadata.yaml</code> | 固定 v1 与既有源成员对应；主论文 BY4、基础模板 MIT | 附带完整摘要存在具体许可依据缺口及 NC 条件；正文不删 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 64 | <code>arxiv:2505.22954</code> | <code>materialized_sources/corpus/arxiv-2505.22954--8a7041cb/manifest.yaml</code><br><code>raw_data/arxiv/Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents/metadata.yaml</code> | <code>CC-BY-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 65 | <code>arxiv:2506.13131</code> | <code>materialized_sources/corpus/arxiv-2506.13131--83bbeb67/manifest.yaml</code><br><code>raw_data/arxiv/AlphaEvolve: A coding agent for scientific and algorithmic discovery/metadata.yaml</code> | <code>CC-BY-NC-ND-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-NC-ND-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 66 | <code>arxiv:2507.21046</code> | <code>materialized_sources/corpus/arxiv-2507.21046--f477f5c3/manifest.yaml</code><br><code>raw_data/arxiv/A Survey of Self-Evolving Agents: On Path to Artificial Super Intelligence/metadata.yaml</code> | 固定 v4、27 作者与源包对应；主文 BY4、模板 Apache/LPPL、三摘要 BY4 分别完成包装 | 无；限当前19个source文字成员，不覆盖八个省略媒体 | <code>documented_permission</code> | 当前固定文本包 gate=allow；不等于人工批准或整体 PR 完成 |
| 67 | <code>arxiv:2509.23233</code> | <code>materialized_sources/corpus/arxiv-2509.23233--b148460b/manifest.yaml</code><br><code>raw_data/arxiv/Detecting Corpus-Level Knowledge Inconsistencies in Wikipedia with Large Language Models/metadata.yaml</code> | 官方许可只授予 arXiv.org 非独占分发权，不授予公众或本仓库。；本地 access=<code>metadata_only</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 68 | <code>arxiv:2509.25651</code> | <code>materialized_sources/corpus/arxiv-2509.25651--2ba7699b/manifest.yaml</code><br><code>raw_data/arxiv/AutoLabs: Cognitive Multi-Agent Systems with Self-Correction for Autonomous Chemical Experimentation/metadata.yaml</code> | <code>CC-BY-NC-ND-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-NC-ND-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 69 | <code>arxiv:2511.02824</code> | <code>materialized_sources/corpus/arxiv-2511.02824--1c218a8e/manifest.yaml</code><br><code>raw_data/arxiv/Kosmos: An AI Scientist for Autonomous Discovery/metadata.yaml</code> | 固定 v2 与既有源成员对应；主论文 BY4 | 附带摘要有明确无再分发许可与 NC 条件；未保存图像不是障碍 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 70 | <code>arxiv:2602.06855</code> | <code>materialized_sources/corpus/arxiv-2602.06855--0b517136/manifest.yaml</code><br><code>raw_data/arxiv/AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents/metadata.yaml</code> | <code>CC-BY-NC-SA-4.0</code>；arXiv 官方文章页的 Rights to this article 链接指向 CC-BY-NC-SA-4.0。；本地 access=<code>unknown</code>，assumed=true | 本地三处 rights 未记录该文章许可及核验日期。；retrieval hash 尚未与确切 arXiv vN 建立可审计映射。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 71 | <code>arxiv:2606.09877</code> | <code>materialized_sources/corpus/arxiv-2606.09877--80ac4aba/manifest.yaml</code><br><code>raw_data/arxiv/Streaming Knowledge Compilation: Proactive Materiality-Scored Pinning for Time-Evolving LLM Wikis/metadata.yaml</code> | 固定 v1；主文与官方 NeurIPS2026 模板各 BY4，既存六行差异披露；完整 NOTICE 入库 | 无；四个source/98selectors保留，不虚构模板历史版本 | <code>documented_permission</code> | 当前固定文本包 gate=allow；不等于人工批准或整体 PR 完成 |
| 72 | <code>arxiv:2607.07663</code> | <code>materialized_sources/corpus/arxiv-2607.07663--e2b770de/manifest.yaml</code><br><code>raw_data/arxiv/Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops/metadata.yaml</code> | 固定 v2 archive 与 revision 一致；论文 CC BY、Pandoc 模板 BSD 及 arXiv 编译元数据 CC0 分别标记；完整组合 NOTICE 入库 | 无；仅覆盖当前保存的文本成员与派生物，六张 PNG 未保存 | <code>documented_permission</code> | 当前固定版本文本包 gate=allow；不等于整个 archive 或人工批准 |
| 73 | <code>arxiv:cs/0309048</code> | <code>materialized_sources/corpus/arxiv-cs-0309048--34c0ca59/manifest.yaml</code><br><code>raw_data/arxiv/Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements/metadata.yaml</code> | 官方记录仅假定 arXiv 自己具有历史非独占分发权；没有面向公众的明示许可。；本地 access=<code>unknown</code>，assumed=true | 面向公众的论文全文复制/再分发许可。；许可版本、权利人和精确作品版本绑定。 | <code>permission_unverified</code> | 不公开全文，仅元数据/链接；当前 gate=block |
| 74 | <code>methodology:linkml-schema-first</code> | <code>materialized_sources/corpus/methodology-linkml-schema-first--182a2b38/manifest.yaml</code><br><code>raw_data/methodology/LinkML Schema First Knowledge Modeling/metadata.yaml</code> | Apache-2.0；部署source-view与固定官方docs源对应，原版权与完整许可已包装 | 无（仅当前单页revision；不声称exact deployment commit） | <code>documented_permission</code> | 已完成当前revision许可包装；当前 gate=allow |
| 75 | <code>standard-w3c-prov-o</code> | <code>materialized_sources/corpus/standard-w3c-prov-o--6f83f2d8/manifest.yaml</code><br><code>raw_data/standard/PROV-O The PROV Ontology/metadata.yaml</code> | <code>W3C-Document-License-2002</code>；允许复制和分发，但一般不授予修改/衍生权。；本地 access=<code>open</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 76 | <code>standard:apache-ossie</code> | <code>materialized_sources/corpus/standard-apache-ossie--ae9e548a/manifest.yaml</code><br><code>raw_data/standard/Apache Ossie Open Semantic Interchange/metadata.yaml</code> | <code>Apache-2.0</code>；官网页脚和 ossie-website README/首页源明确 Apache-2.0，NOTICE 标注 ASF。；本地 access=<code>open</code>，assumed=true | document.md 只有 7 bytes 且没有权利文本。；retrieval hash 未映射网站 commit。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 77 | <code>standard:odcs-3.2.0</code> | <code>materialized_sources/corpus/standard-odcs-3.2.0--affacf92/manifest.yaml</code><br><code>raw_data/standard/Open Data Contract Standard 3.2.0/metadata.yaml</code> | 固定v3.2.0目标文档源直接声明Apache-2.0；完整许可、版权/SPDX与转换说明已包装，实际获取URL固定 | 无；仅当前定义首页，不代表多页标准或站点资产已清权 | <code>documented_permission</code> | 当前固定单页包 gate=allow；不扩展到外链章节或资产 |
| 78 | <code>standard:w3c-dcat-3</code> | <code>materialized_sources/corpus/standard-w3c-dcat-3--fe7850d7/manifest.yaml</code><br><code>raw_data/standard/Data Catalog Vocabulary DCAT 3/metadata.yaml</code> | <code>W3C-Software-and-Document-License-2023</code>；固定版本响应与source revision匹配；完整NOTICE及署名/修改声明已随文本入库 | 当前文字包条件已落实；不覆盖外链作品、商标或专利 | <code>documented_permission</code> | 当前固定版本与包装条件下 gate=allow；丢失NOTICE或署名仍失败 |
| 79 | <code>standard:w3c-did-core</code> | <code>materialized_sources/corpus/standard-w3c-did-core--0d0c2de8/manifest.yaml</code><br><code>raw_data/standard/Decentralized Identifiers DID Core/metadata.yaml</code> | 固定 DID Core 1.0 Recommendation；2015 NOTICE、原版权、来源和转换声明已完整包装 | 无；仅覆盖已核验的固定版本文字包 | <code>documented_permission</code> | 当前固定版本 gate=allow；不外推未来版本或外链资产 |
| 80 | <code>standard:w3c-json-ld-1.1</code> | <code>materialized_sources/corpus/standard-w3c-json-ld-1.1--673c0833/manifest.yaml</code><br><code>raw_data/standard/JSON-LD 1.1/metadata.yaml</code> | <code>W3C-Software-and-Document-License-2015</code>；固定Recommendation响应与revision一致；完整NOTICE、署名与修改说明已入库；原Community Group来源保留为沿革证据 | 当前文字包条件已落实；外链媒体未保存，不扩展商标或专利 | <code>documented_permission</code> | 当前固定版本许可包 gate=allow；不等于人工批准 |
| 81 | <code>standard:w3c-odrl-2.2</code> | <code>materialized_sources/corpus/standard-w3c-odrl-2.2--df9e3701/manifest.yaml</code><br><code>raw_data/standard/ODRL Information Model 2.2/metadata.yaml</code> | <code>W3C-Software-and-Document-License-2015</code>；固定Recommendation响应与revision一致；完整NOTICE、署名与修改说明已入库；原Community Group来源保留为沿革证据 | 当前文字包条件已落实；外链媒体未保存，不扩展商标或专利 | <code>documented_permission</code> | 当前固定版本许可包 gate=allow；不等于人工批准 |
| 82 | <code>standard:w3c-owl-time</code> | <code>materialized_sources/corpus/standard-w3c-owl-time--446fcf02/manifest.yaml</code><br><code>raw_data/standard/Time Ontology in OWL/metadata.yaml</code> | 固定 OWL-Time CRD；2015 NOTICE、2022 W3C版权、联合项目及非背书状态已保留 | 无；仅覆盖已核验的固定版本文字包 | <code>documented_permission</code> | 当前固定版本 gate=allow；不外推未来版本或外链资产 |
| 83 | <code>standard:w3c-owl2</code> | <code>materialized_sources/corpus/standard-w3c-owl2--602129ed/manifest.yaml</code><br><code>raw_data/standard/OWL 2 Web Ontology Language/metadata.yaml</code> | <code>W3C-Document-License-2002</code>；允许复制和分发，但一般不授予修改/衍生权。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 84 | <code>standard:w3c-r2rml</code> | <code>materialized_sources/corpus/standard-w3c-r2rml--b9b6cc67/manifest.yaml</code><br><code>raw_data/standard/R2RML RDB to RDF Mapping Language/metadata.yaml</code> | <code>W3C-Document-License-2002</code>；允许复制和分发，但一般不授予修改/衍生权。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 85 | <code>standard:w3c-rdf-1.2-concepts</code> | <code>materialized_sources/corpus/standard-w3c-rdf-1.2-concepts--02058aec/manifest.yaml</code><br><code>raw_data/standard/RDF 1.2 Concepts and Abstract Syntax/metadata.yaml</code> | 固定 2026-04-07 CR Snapshot；W3C 2023 与附录 RFC 代码分别履约，原通知和完整三条款 BSD 随正文保存 | 无；仅限当前保存文字与合成 ABNF，不含外链资源 | <code>documented_permission</code> | 当前固定文字包 gate=allow；不等于人工批准或整体 PR 完成 |
| 86 | <code>standard:w3c-shacl</code> | <code>materialized_sources/corpus/standard-w3c-shacl--63e18f6d/manifest.yaml</code><br><code>raw_data/standard/Shapes Constraint Language SHACL/metadata.yaml</code> | <code>W3C-Document-License-2015</code>；允许复制和分发；修改/衍生仅有有限实现例外。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 87 | <code>standard:w3c-skos</code> | <code>materialized_sources/corpus/standard-w3c-skos--02ed3abb/manifest.yaml</code><br><code>raw_data/standard/SKOS Simple Knowledge Organization System/metadata.yaml</code> | <code>W3C-Document-License-2002</code>；允许复制和分发，但一般不授予修改/衍生权。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 88 | <code>standard:w3c-sosa-ssn</code> | <code>materialized_sources/corpus/standard-w3c-sosa-ssn--33efc488/manifest.yaml</code><br><code>raw_data/standard/SOSA SSN Ontology/metadata.yaml</code> | <code>W3C-Document-License-2015</code>；允许复制和分发；修改/衍生仅有有限实现例外。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 89 | <code>standard:w3c-vc-data-model-2.0</code> | <code>materialized_sources/corpus/standard-w3c-vc-data-model-2.0--af7d4a38/manifest.yaml</code><br><code>raw_data/standard/Verifiable Credentials Data Model 2.0/metadata.yaml</code> | <code>W3C-Software-and-Document-License-2023</code>；固定版本响应与source revision匹配；完整NOTICE及署名/修改声明已随文本入库 | 当前文字包条件已落实；不覆盖外链作品、商标或专利 | <code>documented_permission</code> | 当前固定版本与包装条件下 gate=allow；丢失NOTICE或署名仍失败 |
| 90 | <code>standard:w3c-web-annotation</code> | <code>materialized_sources/corpus/standard-w3c-web-annotation--3f6ab1c4/manifest.yaml</code><br><code>raw_data/standard/Web Annotation Data Model/metadata.yaml</code> | <code>W3C-Document-License-2015</code>；允许复制和分发；修改/衍生仅有有限实现例外。；本地 access=<code>unknown</code>，assumed=true | metadata 未记录确切 W3C 许可版本。；Markdown 未附完整许可/NOTICE，原许可链接已丢失。 | <code>documented_permission</code> | 满足条件后才可考虑发布；当前 gate=block |
| 91 | <code>vocabulary:schema.org</code> | <code>materialized_sources/corpus/vocabulary-schema.org--c8b3dc95/manifest.yaml</code><br><code>raw_data/standard/Schema.org Vocabulary/metadata.yaml</code> | CC-BY-SA-3.0；官方历史FAQ/Terms覆盖文档，既有快照离线附完整许可、署名及SA声明 | 无（moving URL未来变化不继承旧包allow） | <code>documented_permission</code> | 已完成当前revision许可包装；当前 gate=allow |

## 主要官方依据（Authoritative Sources）

- [arXiv 许可说明](https://info.arxiv.org/help/license/index.html)
- [arXiv 非独占许可](https://arxiv.org/licenses/nonexclusive-distrib/1.0/)
- [arXiv 历史推定许可](https://arxiv.org/licenses/assumed-1991-2003/)
- [Creative Commons 许可概览](https://creativecommons.org/share-your-work/cclicenses/)
- W3C Document License：[2002](https://www.w3.org/copyright/document-license-2002/)、[2015](https://www.w3.org/copyright/document-license-2015/)
- W3C Software and Document License：[2015](https://www.w3.org/copyright/software-license-2015/)、[2023](https://www.w3.org/copyright/software-license-2023/)
- [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
- Schema.org：[Terms](https://schema.org/docs/terms.html)、[FAQ](https://schema.org/docs/faq.html#18)
- [LinkML 固定版本许可](https://raw.githubusercontent.com/linkml/linkml/0e401cef2711b0f12f5a1870805c5cfa999b0858/LICENSE)
- [ODCS v3.2.0](https://github.com/bitol-io/open-data-contract-standard/tree/v3.2.0)

审计日期：2026-09-16。官方证据仅作短概述，完整条款以链接页面为准。
