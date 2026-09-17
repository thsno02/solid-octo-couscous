# MediaWiki Revision History and Discussion Model — 来源归属与再利用说明（NOTICE）

## 有界表示（bounded representation）

本说明仅覆盖 capsule 的下列原始 HTML、列明的正文图片、由它们形成的 `normalized/document.md` 与 `normalized/selectors.jsonl`；不是整个 Wikimedia 站点、相关作品、外部程序／实体数据库的授权。旧 root 摘录与 selector 的历史获取事实另存 `historical_acquisition`，不以本说明改写历史。

选定版本（selected version）：**Wikimedia page snapshot at 2026-09-17T00:47:39Z**。每页选该 cutoff 前最新 revision；表中 fixed oldid 固定页面编辑版本，但模板、skin 与图片可随服务变化。本库保存的是该 revision 的实际 HTML 响应与实际图片响应，不宣称完整模板依赖历史固定。

原 HTML 响应 Date 为 2026-09-17T00:49:48Z，客户端批次完成确认上界为 00:52:08Z；图片实际获取于 00:58:22Z–00:58:42Z。批次确认时间不是每个请求的独立服务器时间。完整原件字节、实际 URL 与库存信息见 manifest。

## 文档归属与版本（attribution and revision）

作者／贡献者：MediaWiki contributors。依照 Wikimedia Terms of Use §7，以下原页、固定版本与历史页面提供全部贡献者的署名入口；不把最后一次编辑者称为唯一作者。

| 文档与本地原件 | 固定 revision／时间 | 原页与署名历史 |
| --- | --- | --- |
| Help:History — `source/help-history.html` | [8524540](https://www.mediawiki.org/w/index.php?title=Help%3AHistory&oldid=8524540)；2026-07-25T03:29:55Z | [原页](https://www.mediawiki.org/wiki/Help:History)；[贡献历史](https://www.mediawiki.org/w/index.php?title=Help%3AHistory&action=history) |
| Help:Talk pages — `source/help-talk-pages.html` | [8374334](https://www.mediawiki.org/w/index.php?title=Help%3ATalk_pages&oldid=8374334)；2026-05-14T21:02:40Z | [原页](https://www.mediawiki.org/wiki/Help:Talk_pages)；[贡献历史](https://www.mediawiki.org/w/index.php?title=Help%3ATalk_pages&action=history) |

帮助正文贡献及本仓库对此文字的派生贡献采用 CC0-1.0；独立图片分别按下表许可，不把组合整体或软件代码宣称为 CC0。

逐页许可依据来自保存原 HTML 的可见正文 notice／footer，而不是域名推断。Help 两页各自明确帮助贡献 CC0；其他页各自 footer 明确文档文字 CC BY-SA4。原页保留的可见声明、引用、来源链接与作者信用继续保留；参考链接不表示其所指作品已另行复制。

## 正文图片（separate media attribution）

下列文件是该页面原始 `img src` 显示表示的未改字节副本，可能是上游生成的 PNG/JPG 缩略表示；不是 SVG 母版、不是独立的原始高分辨率摄影／绘画扫描。我们不裁剪、不重绘，也不将 PNG 标为 SVG。

| 本地文件／原作标题 | 作者／指定归属 | 许可与文件说明 |
| --- | --- | --- |
| `source/assets/help-history.png` — HelpHistory.png | Network-charles | CC0-1.0; preserve depicted MediaWiki GPL-2.0-or-later screenshot notice；[具体文件说明](https://www.mediawiki.org/wiki/File:HelpHistory.png)；[实际图片响应](https://thumb.wikimedia.org/wikipedia/commons/thumb/4/46/HelpHistory.png/1280px-HelpHistory.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail) |
| `source/assets/reply-tool.png` — Reply tool version 2b screenshot.png | ESanders (WMF) | CC-BY-SA-4.0；[具体文件说明](https://www.mediawiki.org/wiki/File:Reply_tool_version_2b_screenshot.png)；[实际图片响应](https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3b/Reply_tool_version_2b_screenshot.png/250px-Reply_tool_version_2b_screenshot.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail) |
| `source/assets/insert-signature.png` — Insert-signature2.svg | I, Perhelion | CC-BY-SA-4.0 selected from offered alternatives；[具体文件说明](https://www.mediawiki.org/wiki/File:Insert-signature2.svg)；[实际图片响应](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2d/Insert-signature2.svg/40px-Insert-signature2.svg.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail) |

## 修改与下游义务（modifications and reuse）

- 原 HTML 与图片不改字节，仅为离线保全保存；本次采集与派生未执行其中脚本、表单或代码示例。这是处理过程说明，不对相应许可证允许的再利用额外设限。
- 派生层选择实际正文容器，移除经逐页核验的语言／导航／交互装饰；保留实质状态、警告、表、例子、引用和结尾。HTML 结构转为 Markdown，链接重写到已保留本地图片，增加来源定位 anchor 与 collector 标记。每页具体规则见 manifest；未将改编伪装成原作者新内容。
- 原件中的 authored alt／caption 保留；不存在的 alt 不臆造。图片内文字、空间关系或缩略图细节未完全进入线性文本时明确记为 extraction partial；原图可继续消费，不把本说明当 OCR 结果。
- 任何 BY-SA 文字改编与 selector 摘录均保留相应署名、作品链接、许可和修改说明，并按上文指定的 ShareAlike 许可提供。独立 BY-SA3 图片保持 BY-SA3，本库未另行修改；Help CC0 文字与独立图片条件分开。
- 不增加限制上述许可权利的条款或技术措施。仓库内其他代码／元数据许可不覆盖这些文档或媒体。不能从本批有界使用推断商标、专利、人格、隐私或第三方作品的无限授权。

## 许可链接与免责声明（licenses and disclaimers）

- [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)／[完整法律文本](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en)。
- [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)／[完整法律文本](https://creativecommons.org/licenses/by-sa/3.0/legalcode.en)；仅在上表标明时适用。
- [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/)／[完整法律文本](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en)；仅在上表或正文标明时适用。
- [Wikimedia Terms of Use §7](https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use#7._Licensing_of_Content)。

许可人按相应许可证以原样（as-is）、现有状态提供材料，不担保准确性、适用性、完整性或不侵权，责任限制依各许可证。引用本说明不建立法律顾问关系，也不表示内容已通过知识可信晋升。

Wikipedia／Wikimedia 及相关标志的商标权属于 Wikimedia Foundation。此处仅在研究、解释原文的语境保留已有页面表示与插图，不用作本仓库品牌、封面或宣传，不构成 Wikimedia Foundation 或各作者的赞助、认可、关联或背书。此处商标使用依 [Trademark Policy §3.6](https://foundation.wikimedia.org/wiki/Trademark_policy) 的相关讨论语境；不得从版权许可推断任意商标用途。不搭建仿冒 Wikimedia 的页面或品牌镜像。

### HelpHistory 截图的原始附加提示

Network-charles 对标注截图声明 CC0；文件说明同时保留：画面涉及的自由软件按 GNU GPL version 2 or later 提供，附无担保及无适销／特定目的适用性担保；参见 [GPL2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html) 和 [GPL3](https://www.gnu.org/licenses/gpl-3.0.html)。如果截图显示非程序代码直接产物的文字或图形，其许可需独立考虑。该提示不被截图作者的 CC0 抹去；本库只保留已有帮助页面界面标注截图，不分发软件可执行程序。Reply 截图仍为 ESanders (WMF) 的 BY-SA4，Signature 图按明确选项选择 BY-SA4，保留指定归属 **I, Perhelion** 及其来源 [Insert-signature.png](https://commons.wikimedia.org/wiki/File:Insert-signature.png)。
