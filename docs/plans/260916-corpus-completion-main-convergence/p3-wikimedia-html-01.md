---
phase: P3-WIKIMEDIA-HTML-01
status: locally_verified_pending_current_head_CI_and_independent_evaluation
base_sha: 0bcc23a5ea8069e1868f4f12610e5ef29375d98f
execution_branch: codex/p3-wikimedia-html-01-260917
adapter_family: generic_web_or_document_v2
action_bucket: html_article_snapshot
source_uids:
  - methodology:mediawiki-revision-discussion
  - methodology:wikidata-statement-model
  - methodology:wikipedia-editorial-governance
startup_source_network_requests: 0
actual_body_html_gets: 8
actual_body_asset_gets: 9
startup_repository_changes: report_and_branch_ledger_only
coverage_summary:
  collection_records: 215
  non_repo_total: 131
  github_repo_excluded: 84
  reported_content_tier_counts:
    excerpt_capsule: 23
    full_text: 96
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
    complete: 36
    metadata_only: 14
    partial: 6
    unknown: 75
  text_extraction_counts:
    complete: 7
    partial: 45
    unavailable: 14
    unknown: 65
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 7
    html_article_snapshot: 11
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 65
    ocr_assessment: 21
    parser_only: 6
    public_persistence_decision: 3
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 32
    block: 65
    unknown: 34
  content_inspected_full_text: 46
  structure_only_full_text: 50
  locally_persisted_complete: 7
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 124
---

# P3-WIKIMEDIA-HTML-01：三个方法文档 UID 的有限八页 HTML 物化

当前实物结果见§12起；下列启动／获取前声明保留为执行历史，不代表当前仍未取得正文。最终独立精确 head/base 审核与 CI 尚待完成。

启动声明（startup contract），不是获取／许可／独立 PASS 或 main 完成证明。2026-09-17 UTC 已按 06 读取 Issue #3/#4、README、02、03、04、plan.yaml、branch-ledger 及 05/06；远端仅父 PR #1 open / Draft，head 为本批精确 base，main 为 `99ce4670be91637209d67792de0962404fa96488`。PR #19 已于 2026-09-17T00:40:42Z 正常合入 work：evaluated head `9e28eacc8503b294b731b39eed3d68d95dba8d1a`、base `512794e2386898aaaac67a8268cc61e0fe8cb594`，完整独立三维 PASS review `5229784430`，CI `35166677599`，merge `0bcc23a5ea8069e1868f4f12610e5ef29375d98f`。本批从该最新、干净 work 创建唯一实现分支；当前仅启动报告／台账修改，尚无元数据或正文请求。先 push 启动提交并开 Draft PR，再执行有限 revision 预检；固定八页版本并修订合同后才获取正文。

## 1. 为什么是一个有限批次

工作假设（working hypothesis）：三个 collection UID 的本体是 metadata 已列定的文档组合，不是三个整站。原 `source_urls` 已足够固定 **2＋2＋4=8 页**，无须扩大到 MediaWiki 全手册、Wikidata 实体数据库、Wikipedia 全部政策或真实用户 talk 内容。Help:Talk_pages 是说明讨论页机制的帮助文档，不是递归获取讨论线程。

同一 `generic_web_or_document_v2`／`html_article_snapshot` 批次；先取精确页面版本的官方 HTML 原件，复用静态结构抽取、独立派生 Markdown／sidecar selectors 与本地 consumer。不创建新 adapter、通用 crawler 或许可考古工作流。

## 2. 三 UID 身份与准确八页

| UID | canonical metadata／capsule（仓库相对路径） | 已声明目标页与拟保留原件 |
| --- | --- | --- |
| `methodology:mediawiki-revision-discussion` | `raw_data/methodology/MediaWiki Revision History and Discussion Model/metadata.yaml`；`materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4` | `https://www.mediawiki.org/wiki/Help:History` → `source/help-history.html`；`https://www.mediawiki.org/wiki/Help:Talk_pages` → `source/help-talk-pages.html` |
| `methodology:wikidata-statement-model` | `raw_data/methodology/Wikidata Statement, Qualifier, Reference and Rank Model/metadata.yaml`；`materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187` | `https://www.wikidata.org/wiki/Wikidata:Data_model` → `source/wikidata-data-model.html`；`https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer` → `source/wikibase-datamodel-primer.html` |
| `methodology:wikipedia-editorial-governance` | `raw_data/methodology/Wikipedia Editorial Governance/metadata.yaml`；`materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93` | `https://en.wikipedia.org/wiki/Wikipedia:Verifiability` → `source/verifiability.html`；`https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view` → `source/neutral-point-of-view.html`；`https://en.wikipedia.org/wiki/Wikipedia:No_original_research` → `source/no-original-research.html`；`https://en.wikipedia.org/wiki/Wikipedia:Consensus` → `source/consensus.html` |

三 canonical identifier 保持 `mediawiki:revision-history-and-talk`、`wikidata:data-model`、`wikipedia:core-content-and-consensus-policies`；题名／UID 不变。`source_urls` 仍是上述八个身份 URL，不静默换成另一种方法文档或教程。若官方同作品页面移动，先记录 alias／正式重定向关系并修订固定响应 URL；真正目标无法判定才提出用户选择，不把常规 revision 选择升级为权限请求。

现证据（不是新 GET）：metadata 第一项 `source_urls` 在 L89–91，第二项 L91–93，第三项 L90–94。三旧 `versioning.source_version=null`，没有上游固定版本；metadata retrieved_at=2026-09-09 不是新快照日期。

| UID | before 原件／文本／公共 gate | 旧 root selectors | 精确缺口 |
| --- | --- | --- | --- |
| revision-discussion | unknown／partial／unknown | 43 | 仅 History；`document.md:90` 到 `cur option li` 截断，Talk 文档未存。 |
| statement-model | unknown／partial／unknown | 20 | `document.md:43` qualifiers 例句截断，Primer 未存。 |
| editorial-governance | unknown／partial／unknown | 120 | 前216行主要语言／政策导航，`:217` 只存 Verifiability 首段并截断，其余三政策未存。 |

三份 manifest 的旧 root revision 已记录首次主页面响应身份，不能用它证明未保留的 HTML 或未获取伴随页；启动时按最新原值完整保留历史，不在这里创造组合 revision。三篇各仅1501字符 excerpt，无保留原 HTML，共12个旧库存文件；183个旧 selectors 结构 resolved、语义 false，均 unresolved／html_article_snapshot。既有 audit 未覆盖三 UID，不能借相邻 WikiChat 许可包放行。三项当前均不在36 selected，无 demo claims，knowledge=null。

## 3. 可接受的快照版本策略（snapshot versioning）

优先选择启动时一次记录的真实 UTC cutoff `T`：每页取该时刻或之前最新 revision，不追求八页同时编辑或历史2026-09-09快照。仅允许官方 API 为八个 title 查询 page id／revision id／timestamp／canonical alias，随后在**正文 GET 前**把八个确定的 `oldid`、精确请求 URL、源路径与 scope 补进 repo 启动报告／合同。三个允许的有限身份查询端点是 `https://www.mediawiki.org/w/api.php`、`https://www.wikidata.org/w/api.php`、`https://en.wikipedia.org/w/api.php`；不查询全站 recentchanges 或所有历史。

固定响应可用各站 `https://<host>/w/index.php?title=<已声明title编码>&oldid=<实际revision_id>`。八页版本是 per-page 向量，不是 Git commit 或共同 release。canonical selected version 可明确写 `Wikimedia page snapshot at <T>`，伴随各页 revision id／timestamp／permalink 与实际 retrieved_at；字段名由启动联调确定，不能沿用 null 或臆造新版号。canonical identity URL 与 `source_urls` 保持稳定，`full_text_url` 为主页面固定 permalink，其他七页用明确源描述绑定。

`oldid` 固定作者页面版本，但模板转入／skin 渲染仍可能随服务状态变化；保存的原件是**该 revision 在真实 GET 时的 HTML 响应**，不宣称完整依赖树历史固定、永久响应 byte identity 或两次 GET 必须相同。不递归抓模板；离线重放使用所存 HTML。

若 API 被限制，不绕过访问控制：可用八个当前页面自身可见的永久链接／revision 元数据固定所存实际响应，并记录每页实际时刻，不伪称共同 cutoff。若无法证 revision，则仅如实记 dated response、版本不足与 next action，不猜 oldid 或提升 complete；改变版本合同前先修订。

## 4. 实际页面取得后即可闭合的最低准入证据

三项 `rights.license_spdx=null`、`access=metadata_only`，旧 notes-only 是收集策略，不是权利人拒绝授权。域名、“Wikidata数据CC0”或 Wikipedia 相邻文章 BY-SA 不能替代八文档自己的许可。

逐页只需有界证据：实际 title／namespace、canonical／永久链接、revision id／timestamp；正文／页脚中具体文字版权／许可链接；页面可见的外部导入／独立版权或信用声明；该页 contributor history 的正式署名链接；必要时跟随页脚所指**一个适用 reuse policy／许可法律文本**。可合理依赖官方页面明示的文档文字授权，不逐句原创证明、不下载全部编辑者历史、不查不存在的历史服务合同。Help 命名空间若明示公有领域条件，则按该实际声明记录；不先假定 Help 一律 PD。非实体库的 Wikidata 文档文字与 CC0 数据授权分开。

来源合并派生须逐页保留 contributor／title／permalink／history／具体 license 与已有信用，记录结构转换和本仓库修改；ShareAlike 若适用则传播到对应派生正文／selector 摘录，不借 repo 整体 MIT 或 metadata CC0 抹去，也不把一页的许可扩大到整个站点／仓库。仅有主页许可不能掩盖其余7页未知。公开 commit 前完成三组合表示的 package 与机器审计；有真实未覆盖表达只阻止该页／UID，记录 `public_persistence_decision`，不伪装网络失败。

原 HTML 保留真实 bytes，不执行其中脚本、表单、示例或提示词；许可范围区分文档文字／已许可改编与可见独立素材，不将页面许可自动转为外链 JS／CSS／媒体再许可。正文有关键截图／模型图时，先用实际 DOM 列精确 src、角色、信用和必须保留的语义，再修订合同和准入后才能 GET 该有限资产；本启动上限**不含任何图片下载**。标识／skin 图标不默认为用户正文；也不能删去核心图后冒充无缺件完整文档。原件完整与原生文本有损独立记录，不要求全图 OCR。

## 5. 可复用能力与真正最小接口缺口

可直接复用：`retained_html_sections` 的 heading／paragraph／dt-dd／table／pre-code／列表／blockquote 结构抽取；`derive_retained_text_sources` 的有序多原件组装、真实源行边界及 sidecar selectors；现有 NOTICE／唯一末注／库存／聚合生成；`build_demo.py`、coverage 的共享 selector router 和原件消费。

**不能宣称零代码直用。** 当前 `retained_text_selector_file`（`materialize_all_sources.py:2167`）把 `dated_html_response` 限成一个 `source/specification.html`；其 validator 还禁止 approved URL query（`validate_materialization_completeness.py:288`），普通多源 retained binding 则要求真实 Git commit。wiki 多页面与 `oldid` 不满足这些条件，不能 fake git、拼接伪原件或覆盖旧 root selectors。

建议仅新增一个有限、显式的 wiki revision-set opt-in（名字／字段启动前联调）：仍用同 adapter、`normalized/document.md`／`normalized/selectors.jsonl`；绑定2／2／4个 declared HTML，每页显式 source、identity URL、fixed oldid URL、revision id／timestamp、retrieval／inventory 和准入范围。主 root revision 可沿主页面真实 HTML hash；其他页面靠逐件强绑定，不冒称一个合成 hash 是上游 release。修改限既有 materializer replay／preflight、validator 和定向 tests，不放宽旧 W3C／Git 分支。

派生 DOM 使用逐页实见正文 container（如页面实际 `#mw-content-text`／parser output）及有限 UI 排除，具体 selector 在取得后补证；原 HTML 不改。保留 policy status／nutshell／争议与编辑警告、必要正文模板、例子、引用、表／代码和正文结尾；排除语言选择、sidebar、edit tools 等界面，不能预写一个全站 CSS 规则把正文一起删掉。新 opt-in 必须将正确 derived pair 接入共享 router；coverage 已用该 router，不预先授权 coverage 重写。未来 selected 的分类如有必要仅补 `build_demo.py` HTML reading-view 条件与现有 `test_excerpt.py` 测试，不新增本三 UID demo 选入。

## 6. 启动合同

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-WIKIMEDIA-HTML-01",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "0bcc23a5ea8069e1868f4f12610e5ef29375d98f",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "execution_branch": "codex/p3-wikimedia-html-01-260917",
    "status": "actual_body_persisted_content_corrected_pending_final_CI_and_independent_evaluation",
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "html_article_snapshot",
    "source_uids": [
      "methodology:mediawiki-revision-discussion",
      "methodology:wikidata-statement-model",
      "methodology:wikipedia-editorial-governance"
    ],
    "target_pages": [
      {
        "uid": "methodology:mediawiki-revision-discussion",
        "identity_url": "https://www.mediawiki.org/wiki/Help:History",
        "source": "source/help-history.html",
        "page_id": 189572,
        "title": "Help:History",
        "revision_id": 8524540,
        "revision_timestamp": "2026-07-25T03:29:55Z",
        "approved_url": "https://www.mediawiki.org/w/index.php?title=Help%3AHistory&oldid=8524540"
      },
      {
        "uid": "methodology:mediawiki-revision-discussion",
        "identity_url": "https://www.mediawiki.org/wiki/Help:Talk_pages",
        "source": "source/help-talk-pages.html",
        "page_id": 20469,
        "title": "Help:Talk pages",
        "revision_id": 8374334,
        "revision_timestamp": "2026-05-14T21:02:40Z",
        "approved_url": "https://www.mediawiki.org/w/index.php?title=Help%3ATalk_pages&oldid=8374334"
      },
      {
        "uid": "methodology:wikidata-statement-model",
        "identity_url": "https://www.wikidata.org/wiki/Wikidata:Data_model",
        "source": "source/wikidata-data-model.html",
        "page_id": 109922707,
        "title": "Wikidata:Data model",
        "revision_id": 2518329379,
        "revision_timestamp": "2026-07-16T20:34:20Z",
        "approved_url": "https://www.wikidata.org/w/index.php?title=Wikidata%3AData_model&oldid=2518329379"
      },
      {
        "uid": "methodology:wikidata-statement-model",
        "identity_url": "https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer",
        "source": "source/wikibase-datamodel-primer.html",
        "page_id": 210750,
        "title": "Wikibase/DataModel/Primer",
        "revision_id": 8399774,
        "revision_timestamp": "2026-05-31T05:57:04Z",
        "approved_url": "https://www.mediawiki.org/w/index.php?title=Wikibase%2FDataModel%2FPrimer&oldid=8399774"
      },
      {
        "uid": "methodology:wikipedia-editorial-governance",
        "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Verifiability",
        "source": "source/verifiability.html",
        "page_id": 3961892,
        "title": "Wikipedia:Verifiability",
        "revision_id": 1373569010,
        "revision_timestamp": "2026-09-06T17:54:43Z",
        "approved_url": "https://en.wikipedia.org/w/index.php?title=Wikipedia%3AVerifiability&oldid=1373569010"
      },
      {
        "uid": "methodology:wikipedia-editorial-governance",
        "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view",
        "source": "source/neutral-point-of-view.html",
        "page_id": 39805,
        "title": "Wikipedia:Neutral point of view",
        "revision_id": 1370393267,
        "revision_timestamp": "2026-08-20T21:44:45Z",
        "approved_url": "https://en.wikipedia.org/w/index.php?title=Wikipedia%3ANeutral_point_of_view&oldid=1370393267"
      },
      {
        "uid": "methodology:wikipedia-editorial-governance",
        "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:No_original_research",
        "source": "source/no-original-research.html",
        "page_id": 410235,
        "title": "Wikipedia:No original research",
        "revision_id": 1374682589,
        "revision_timestamp": "2026-09-13T14:12:28Z",
        "approved_url": "https://en.wikipedia.org/w/index.php?title=Wikipedia%3ANo_original_research&oldid=1374682589"
      },
      {
        "uid": "methodology:wikipedia-editorial-governance",
        "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Consensus",
        "source": "source/consensus.html",
        "page_id": 805445,
        "title": "Wikipedia:Consensus",
        "revision_id": 1370677546,
        "revision_timestamp": "2026-08-22T13:26:30Z",
        "approved_url": "https://en.wikipedia.org/w/index.php?title=Wikipedia%3AConsensus&oldid=1370677546"
      }
    ],
    "allowed_paths": [
      "docs/plans/260916-corpus-completion-main-convergence/p3-wikimedia-html-01.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "raw_data/methodology/MediaWiki Revision History and Discussion Model/metadata.yaml",
      "raw_data/methodology/Wikidata Statement, Qualifier, Reference and Rank Model/metadata.yaml",
      "raw_data/methodology/Wikipedia Editorial Governance/metadata.yaml",
      "raw_data/licenses/p3-wikimedia-html-01-*.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source/help-history.html",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source/help-talk-pages.html",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/normalized/document.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/manifest.yaml",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source-metadata.yaml",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/NOTICE.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/README.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/source/wikidata-data-model.html",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/source/wikibase-datamodel-primer.html",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/normalized/document.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/manifest.yaml",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/source-metadata.yaml",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/NOTICE.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/README.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/verifiability.html",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/neutral-point-of-view.html",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/no-original-research.html",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/consensus.html",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/normalized/document.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/manifest.yaml",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source-metadata.yaml",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/NOTICE.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/README.md",
      "scripts/materialize_all_sources.py",
      "scripts/validate_materialization_completeness.py",
      "tests/test_materialization_integrity.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_excerpt.py",
      "raw_data/audits/materialization_rights_review.yaml",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**",
      "experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**",
      "experiments/v0_meta_kb_initialization_demo_260910/07_review/**",
      "experiments/v0_meta_kb_initialization_demo_260910/08_release/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source/assets/help-history.png",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source/assets/reply-tool.png",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source/assets/insert-signature.png",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/source/assets/wikidata-datamodel.png",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/assets/consensus-flowchart.png",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/assets/wikipedia-scale-of-justice.png",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/assets/starry-night.jpg",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/assets/jimmy-wales4.jpg",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source/assets/manusingmicroscope.jpg"
    ],
    "generated_paths": [
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/normalized/document.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/manifest.yaml",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/source-metadata.yaml",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/NOTICE.md",
      "materialized_sources/corpus/methodology-mediawiki-revision-discussion--b35a85e4/README.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/normalized/document.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/manifest.yaml",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/source-metadata.yaml",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/NOTICE.md",
      "materialized_sources/corpus/methodology-wikidata-statement-model--ca4d2187/README.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/normalized/document.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/normalized/selectors.jsonl",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/manifest.yaml",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/source-metadata.yaml",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/NOTICE.md",
      "materialized_sources/corpus/methodology-wikipedia-editorial-governance--99973b93/README.md",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/materialization_snapshot.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/wiki_build_request.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/page_plan.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/05_wiki/**",
      "experiments/v0_meta_kb_initialization_demo_260910/06_evaluation/**",
      "experiments/v0_meta_kb_initialization_demo_260910/07_review/**",
      "experiments/v0_meta_kb_initialization_demo_260910/08_release/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
    ],
    "pre_get_gates": {
      "integration": "PDF03_normal_merge_latest_work_exact_base_single_active_writer",
      "identity_and_version": "exact_eight_page_revision_ids_permalinks_cutoff_and_contract_amendment_before_body_GET",
      "assets": "nine_exact_observed_image_srcs_and_per_file_credit_review_recorded_no_other_assets",
      "publication": "per_page_actual_notice_and_combo_representation_review_before_public_commit"
    },
    "explicitly_out_of_scope": [
      "all pages except the eight declared documents, real talk threads, all history revisions, translations, Wikidata entities, whole sites and recursively followed references",
      "images, CSS, JS, template dependencies or any other asset GET before explicit contract amendment",
      "overwriting old document.md or root selectors.jsonl, discarding legacy revision/retrieval/materialization facts or fabricating Git identity",
      "domain-default CC, Wikidata-data-CC0 applied to documentation, immediate public fulltext commit before review",
      "new adapter framework, schema-wide rewrite, dependencies/workflows and blanket weakening of existing W3C/Git validators",
      "demo selected-source changes, new claims/evidence, collector assessment changes, trusted promotion or unrelated generated semantics",
      "main merge, issue closure, branch deletion, administrator settings or history cleanup"
    ],
    "revision_cutoff": "2026-09-17T00:47:39Z",
    "body_assets": [
      {
        "page": "help-history",
        "source": "source/assets/help-history.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/4/46/HelpHistory.png/1280px-HelpHistory.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/4/46/HelpHistory.png/1280px-HelpHistory.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": null,
        "source_line": 811,
        "file_page": "https://www.mediawiki.org/wiki/File:HelpHistory.png",
        "uid": "methodology:mediawiki-revision-discussion",
        "capsule": "methodology-mediawiki-revision-discussion--b35a85e4",
        "attribution": "Network-charles",
        "permission_basis": "CC0-1.0; preserve depicted MediaWiki GPL-2.0-or-later screenshot notice"
      },
      {
        "page": "help-talk-pages",
        "source": "source/assets/reply-tool.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/3/3b/Reply_tool_version_2b_screenshot.png/250px-Reply_tool_version_2b_screenshot.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3b/Reply_tool_version_2b_screenshot.png/250px-Reply_tool_version_2b_screenshot.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": null,
        "source_line": 801,
        "file_page": "https://www.mediawiki.org/wiki/File:Reply_tool_version_2b_screenshot.png",
        "uid": "methodology:mediawiki-revision-discussion",
        "capsule": "methodology-mediawiki-revision-discussion--b35a85e4",
        "attribution": "ESanders (WMF)",
        "permission_basis": "CC-BY-SA-4.0"
      },
      {
        "page": "help-talk-pages",
        "source": "source/assets/insert-signature.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/2/2d/Insert-signature2.svg/40px-Insert-signature2.svg.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/2/2d/Insert-signature2.svg/40px-Insert-signature2.svg.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": "Signature button",
        "source_line": 818,
        "file_page": "https://www.mediawiki.org/wiki/File:Insert-signature2.svg",
        "uid": "methodology:mediawiki-revision-discussion",
        "capsule": "methodology-mediawiki-revision-discussion--b35a85e4",
        "attribution": "I, Perhelion",
        "permission_basis": "CC-BY-SA-4.0 selected from offered alternatives"
      },
      {
        "page": "wikibase-datamodel-primer",
        "source": "source/assets/wikidata-datamodel.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/a/ae/Datamodel_in_Wikidata.svg/960px-Datamodel_in_Wikidata.svg.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ae/Datamodel_in_Wikidata.svg/960px-Datamodel_in_Wikidata.svg.png?utm_source=www.mediawiki.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": null,
        "source_line": 791,
        "file_page": "https://www.mediawiki.org/wiki/File:Datamodel_in_Wikidata.svg",
        "uid": "methodology:wikidata-statement-model",
        "capsule": "methodology-wikidata-statement-model--ca4d2187",
        "attribution": "Charlie Kritschmar (WMDE)",
        "permission_basis": "CC0-1.0"
      },
      {
        "page": "consensus",
        "source": "source/assets/consensus-flowchart.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/en/thumb/5/5f/Consensus_Flowchart.svg/330px-Consensus_Flowchart.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/en/thumb/5/5f/Consensus_Flowchart.svg/330px-Consensus_Flowchart.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": "Make an edit deviating from the previous consensus state of the article, and wait. If the article is not edited further, presumed consensus exists favoring your changes. If the article is edited further, but you agree with the changes, presumed consensus exists in favor of the article's new state. If you disagree with the changes, seek a compromise, implement in another edit, and once again wait for further edits to the article.",
        "source_line": 775,
        "file_page": "https://en.wikipedia.org/wiki/File:Consensus_Flowchart.svg",
        "uid": "methodology:wikipedia-editorial-governance",
        "capsule": "methodology-wikipedia-editorial-governance--99973b93",
        "attribution": "Locke Cole; based upon CCC Flowchart 6.jpg by Kevin Murray",
        "permission_basis": "CC-BY-SA-3.0 selected from dual license"
      },
      {
        "page": "neutral-point-of-view",
        "source": "source/assets/wikipedia-scale-of-justice.png",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/e/ed/Wikipedia_scale_of_justice.svg/250px-Wikipedia_scale_of_justice.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ed/Wikipedia_scale_of_justice.svg/250px-Wikipedia_scale_of_justice.svg.png?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": "A scale of justice with two Wikipedia logos being weighed",
        "source_line": 1017,
        "file_page": "https://en.wikipedia.org/wiki/File:Wikipedia_scale_of_justice.svg",
        "uid": "methodology:wikipedia-editorial-governance",
        "capsule": "methodology-wikipedia-editorial-governance--99973b93",
        "attribution": "Mrmw (vectorization); referenced logo/scale components retained by attribution link",
        "permission_basis": "CC-BY-SA-3.0; Wikimedia trademarks reserved; contextual policy illustration only"
      },
      {
        "page": "neutral-point-of-view",
        "source": "source/assets/starry-night.jpg",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/250px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/250px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": null,
        "source_line": 1184,
        "file_page": "https://en.wikipedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        "uid": "methodology:wikipedia-editorial-governance",
        "capsule": "methodology-wikipedia-editorial-governance--99973b93",
        "attribution": "Vincent van Gogh; Google Arts & Culture reproduction; Museum of Modern Art",
        "permission_basis": "Public domain / PD-Art / PDM1.0; retain jurisdiction caveat"
      },
      {
        "page": "neutral-point-of-view",
        "source": "source/assets/jimmy-wales4.jpg",
        "observed_src": "//thumb.wikimedia.org/wikipedia/commons/thumb/a/a9/WikiConference_India_2011_Jimmy_Wales_4.jpg/250px-WikiConference_India_2011_Jimmy_Wales_4.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "approved_url": "https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a9/WikiConference_India_2011_Jimmy_Wales_4.jpg/250px-WikiConference_India_2011_Jimmy_Wales_4.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "alt": null,
        "source_line": 1206,
        "file_page": "https://en.wikipedia.org/wiki/File:WikiConference_India_2011_Jimmy_Wales_4.jpg",
        "uid": "methodology:wikipedia-editorial-governance",
        "capsule": "methodology-wikipedia-editorial-governance--99973b93",
        "attribution": "Victorgrigas",
        "permission_basis": "CC-BY-SA-3.0"
      },
      {
        "page": "no-original-research",
        "source": "source/assets/manusingmicroscope.jpg",
        "observed_src": "//upload.wikimedia.org/wikipedia/commons/b/b8/Manusingmicroscope.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled",
        "approved_url": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Manusingmicroscope.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail_unscaled",
        "alt": "A microbiologist conducting scientific research using a microscope.",
        "source_line": 875,
        "file_page": "https://en.wikipedia.org/wiki/File:Manusingmicroscope.jpg",
        "uid": "methodology:wikipedia-editorial-governance",
        "capsule": "methodology-wikipedia-editorial-governance--99973b93",
        "attribution": "USDA Agricultural Research Service; photographer not supplied; Quadell original upload / Maksim transfer",
        "permission_basis": "Public domain US federal government work; jurisdiction caveat"
      }
    ]
  }
}
```

## 7. 验收与收口，不无限扩批

单 writer 写三个 capsule／canonical／rights review／coverage／aggregates；其他 agent 仅并行读八份暂存原件的版本、正文边界和可见信用。每 UID 按2／2／4页逐页核正文开中尾、heading层级、页末、表／例子／代码、必要图／独立声明；不能只核第一主页面便宣称组合完整。每套新增 selectors 首中末语义核查并验证源与derived范围。保留三旧 `document.md` 和183个 root selectors 字节，新增 `historical_acquisition` 保留完整旧 revision／retrievals／rights／materialization／local_files／null版本观察；新根当前表示与历史明确区分。

准入后 root完整package／NOTICE／唯一末注与审计齐备；给三项 before→after，原件、文本、公开、消费与 knowledge 分开。新增 fulltext review 使用既有追加审计机制，不改既有100条审计观测。无法合法公开的实际文档如实 unresolved，保留有限官方尝试与具体决策，不能拿 unknown=无正文或新框架需求做豁免。

三个 UID 未 selected：保留 selected set、claims、evidence、collector assessment 原字节；允许已有全局 build identity 的必要传播，不能提交 stale release。代码只补上述显式 opt-in；fixtures 覆盖2／4多源、wrong oldid／URL、缺页、inventory／snapshot drift、旧root保留、正文container排除与源selector语义，旧W3C／Git测试不变。精确 head 的 `make test`／`make validate`／`make demo`／`make reproducibility`、completeness与coverage校验，加当前CI与独立三维PASS后正常合work。离线双重放不冒充双GET。

真实风险／待核只有：八个实际revision及页面移动；八页实际文字许可／可见导入信用；实际正文DOM和关键图；上述已有helper的小接口联调。初步无删除、用途或管理员权限决定需要用户确认。若观察到真正未授权表达则报告具体页／段／scope最小决定，不追全部版本、模板和编辑历史；P4/P5与PR1main仍按05/06既有条件收口，不追加trusted或全图OCR门槛。

## 8. 官方 revision 预检与下载前合同修订

PR #20 已先于请求创建，启动 commit `0ff986198a62f9ec96d56e2226fd95ea354f2598`。统一 cutoff 为 `2026-09-17T00:47:39Z`；实际预检于 `2026-09-17T00:48Z` 完成，至 `00:48:55Z` 已读取八个结果。仅 query/revisions/ids/timestamp/info，没有正文请求，没有追随 API continue。

初次按站点合并的三个 API 请求均 HTTP 200，但 MediaWiki 与 Wikipedia 返回 `invalidparammix`：含 `rvstart`/`rvlimit` 时不能一次查询多个 title；Wikidata 单页成功。按实际错误改为另外七个单页查询，均 HTTP 200、TLS 验证成功、无重定向；不是访问失败或绕过。合计10次 API GET，8次有效单页身份结果。所有 revision timestamp 早于 cutoff；只有下划线到空格的标准 title normalization，无作品身份替换。以下固定 URL 从官方返回的准确 revision id 和既定入口构建；尚未获取正文。

| 源路径 | page id | revision id | revision timestamp | 准确正文请求 URL |
| --- | ---: | ---: | --- | --- |
| source/help-history.html | 189572 | 8524540 | 2026-07-25T03:29:55Z | https://www.mediawiki.org/w/index.php?title=Help%3AHistory&oldid=8524540 |
| source/help-talk-pages.html | 20469 | 8374334 | 2026-05-14T21:02:40Z | https://www.mediawiki.org/w/index.php?title=Help%3ATalk_pages&oldid=8374334 |
| source/wikidata-data-model.html | 109922707 | 2518329379 | 2026-07-16T20:34:20Z | https://www.wikidata.org/w/index.php?title=Wikidata%3AData_model&oldid=2518329379 |
| source/wikibase-datamodel-primer.html | 210750 | 8399774 | 2026-05-31T05:57:04Z | https://www.mediawiki.org/w/index.php?title=Wikibase%2FDataModel%2FPrimer&oldid=8399774 |
| source/verifiability.html | 3961892 | 1373569010 | 2026-09-06T17:54:43Z | https://en.wikipedia.org/w/index.php?title=Wikipedia%3AVerifiability&oldid=1373569010 |
| source/neutral-point-of-view.html | 39805 | 1370393267 | 2026-08-20T21:44:45Z | https://en.wikipedia.org/w/index.php?title=Wikipedia%3ANeutral_point_of_view&oldid=1370393267 |
| source/no-original-research.html | 410235 | 1374682589 | 2026-09-13T14:12:28Z | https://en.wikipedia.org/w/index.php?title=Wikipedia%3ANo_original_research&oldid=1374682589 |
| source/consensus.html | 805445 | 1370677546 | 2026-08-22T13:26:30Z | https://en.wikipedia.org/w/index.php?title=Wikipedia%3AConsensus&oldid=1370677546 |

先把此向量同步 repo／PR 合同，再各 GET 一次上述八个 HTML 到暂存区，逐页核验实际正文、许可及信用后决定可公开表示。无图片、CSS、JS、全历史或模板 GET 授权；原 HTML 不执行。`oldid` 不代表模板依赖完整历史固定。

## 9. 正文 GET 结果、实际图片范围与获取前修订

八份固定 HTML 均为 HTTP200、`text/html; charset=UTF-8`、零重定向、TLS验证成功，共1,862,396 bytes；保存响应Date均 `2026-09-17T00:49:48Z`，客户端全部完成确认上界 `2026-09-17T00:52:08Z`。该上界不是服务器逐请求时间。HTML中的wgRevisionId／articleId／pageName与预检逐项绑定，原件未执行。正文阅读确认Help两页文字CC0，其余六页文字BY-SA4；不是统一“Wikidata数据CC0”。

实际观察才补充上方合同的 **9 个正文 img 原始src**，每个仅一次GET，保留页面显示尺寸的官方PNG/JPG响应，不取其他srcset、巨大艺术品母版、SVG的全翻译或站点素材。图片bytes仍待获取；这些是页面正文的已有组成，不是新增来源。装饰图标、语言栏／编辑按钮排除仅作用派生DOM，保留原HTML与实质状态/警告/正反例语义。

| 精确本地文件名 | 原作信用（credit） | 实见准入依据与边界 |
| --- | --- | --- |
| source/assets/help-history.png | Network-charles | CC0-1.0; preserve depicted MediaWiki GPL-2.0-or-later screenshot notice；[File description](https://www.mediawiki.org/wiki/File:HelpHistory.png) |
| source/assets/reply-tool.png | ESanders (WMF) | CC-BY-SA-4.0；[File description](https://www.mediawiki.org/wiki/File:Reply_tool_version_2b_screenshot.png) |
| source/assets/insert-signature.png | I, Perhelion | CC-BY-SA-4.0 selected from offered alternatives；[File description](https://www.mediawiki.org/wiki/File:Insert-signature2.svg) |
| source/assets/wikidata-datamodel.png | Charlie Kritschmar (WMDE) | CC0-1.0；[File description](https://www.mediawiki.org/wiki/File:Datamodel_in_Wikidata.svg) |
| source/assets/consensus-flowchart.png | Locke Cole; based upon CCC Flowchart 6.jpg by Kevin Murray | CC-BY-SA-3.0 selected from dual license；[File description](https://en.wikipedia.org/wiki/File:Consensus_Flowchart.svg) |
| source/assets/wikipedia-scale-of-justice.png | Mrmw (vectorization); referenced logo/scale components retained by attribution link | CC-BY-SA-3.0; Wikimedia trademarks reserved; contextual policy illustration only；[File description](https://en.wikipedia.org/wiki/File:Wikipedia_scale_of_justice.svg) |
| source/assets/starry-night.jpg | Vincent van Gogh; Google Arts & Culture reproduction; Museum of Modern Art | Public domain / PD-Art / PDM1.0; retain jurisdiction caveat；[File description](https://en.wikipedia.org/wiki/File:Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg) |
| source/assets/jimmy-wales4.jpg | Victorgrigas | CC-BY-SA-3.0；[File description](https://en.wikipedia.org/wiki/File:WikiConference_India_2011_Jimmy_Wales_4.jpg) |
| source/assets/manusingmicroscope.jpg | USDA Agricultural Research Service; photographer not supplied; Quadell original upload / Maksim transfer | Public domain US federal government work; jurisdiction caveat；[File description](https://en.wikipedia.org/wiki/File:Manusingmicroscope.jpg) |

有限版权证据读取为8个新File描述页GET（Help3、Wikipedia5，均200、无重定向），Primer的File页通过web读取，均已有本地或转入Commons的描述，未进一步递归历史/作者。主agent实读CC BY-SA4和CC0法律文本、BY-SA3 §3/4、Wikimedia Terms §7。官网商标policy因scale图可见标记而有限跟随，§3.6.3允许讨论Wikimedia的科学/文学用途；本库仅保存原政策插图作为研究材料，不以logo作品牌/封面、不搭建冒充Wikipedia的镜像、不声称背书或任意商标再授权。保留商标权人/政策链接和无背书声明。两幅公有领域图保留官方范围/辖区提示，不误写CC授权。HelpHistory另保留所示软件GPL2-or-later及无担保提示，不将截图作者CC0外推为软件license。

在各UID的完整NOTICE中提供准确title、原页/固定版本/署名history、逐图归属/适用license、派生变更与无背书/无担保；普通文档派生正文/selector摘录采用BY-SA4，Help文本仍CC0、图片各自许可。该判断只覆盖本批已观察的有界表示，未完成全库公共清关。图片成功取得后仍需内容与派生验收，不能由本节直接宣布complete。

## 10. 实际资产审核与包装交接

本节为当前进度；§8／§9 的“尚未获取”是各次获取前合同的历史状态，不是当前结果。九个列定原始 img src 于 `2026-09-17T00:58:22Z` 至 `00:58:42Z` 完成一次有界 GET：全部 HTTP 200、零重定向、TLS 验证成功，共 **1,303,443 bytes**。八 HTML 与九图合计 **17 个原件、3,165,839 bytes**，不含许可描述页与 API 临时证据。主 agent 已逐一目视九图，确认实际表示、类型、画面与文档用途；没有取 srcset、SVG 母版或 696 MB 绘画母图，没有新来源扩围。

独立读取分工：Help 两页由 help reader 全读；四政策由 policy reader 全读；Data model／Primer 由主 agent 全读。逐页标题数为14、10、21、10、34、35、23、14；不是用标题计数代替阅读。关键判断包括：Talk 教学表中的 `[edit]` 是作者示例而非 UI；嵌套讨论回复与九行 pre 示例必须保留；policy 正反例七个勾／叉按原 alt 与 Y／N 表达，不能作为装饰删掉；状态、警告、引用与页尾仍属正文。

九图中的截图内部像素文字与空间关系、数据模型图内部标签不保证全部变成线性文本，因此先按 honest partial 包装，待实际派生复读再判断；原图完整留存与文本完整是两个结论。图中的 public editor names／署名、人物和 trademark 均按原教学或讨论语境保留，无人物背书、广告或站点仿冒用途。

三份仓库 NOTICE 已写入 `raw_data/licenses/p3-wikimedia-html-01-*.md`，列明逐页版本、贡献历史、逐图作者、混合许可、改编与下游义务。代码 writer 仅改五个获准 code/test 路径，新增显式 `wiki_page_revision_set`，不放宽旧 W3C／Git 分支；82 个 integrity tests 与18个 excerpt tests 已通过。这不是实物派生或最终精确 head/base 的独立 PASS。

当前单一 packaging writer 正在保留旧六个正文／selector 文件与完整 acquisition history、追加三条 rights review，写入本批17原件及 normalized pair。全库生成器尚未运行；随后进行实际 consumer 复读、严格离线双重放、聚合更新及最终 CI／独立三维审核。

## 11. 实物复读的纠偏（evaluation → repair）

首次三套包装与逐套严格离线双重放成功；17原件字节与获取响应一致，旧6个正文/selector文件、完整旧manifest及原100条audit对象/前缀保全。新增169个selectors（26/33/110）、旧183保留；三套定向validator无错误。此次包装成功仍未直接提升正文质量。

Help reader 与主 agent 在真实派生中分别发现相同阻断：原 heading 内的空span锚点把题名挤到 ATX 行之外，造成“有题名文字、没有正确标题层级”；Primer 的多层有序列表另因每级两空格不满足 CommonMark 父序号缩进而展平。已退回 executor，仅修 wiki 的标题锚点与有效嵌套缩进，保留原HTML、source anchors和旧W3C/Git行为，不增加提取框架。

实际共享消费探针另发现 Data 在 `i.e.` 缩写处截句、Policy 选中 `WP:V`／`WP:PROOF` redirect 帽注。三个UID不在selected，这不是已生成claim；但也不能用手造fixture通过替代真实consumer验证。代码 writer 正定点诊断，保留原帽注内容，不把它冒充政策论点。修复与实物复核结束前保持 `body_quality_verified=false`，不宣称text complete或最终独立PASS。

## 12. 修复后实物验收与六维结果

上述四项实际 finding 均已关闭：wiki 标题的空锚点独立前置、真实题名留在同一 ATX 行；嵌套列表采用有效四空格层级；78个原帽注全文保留在明确 collector source-role块，不用于自动论点摘录；wiki仅选取≤700字符完整连续段落，不在缩写处切句，过长则找下一合格段落，无合格段诚实返回空。旧 W3C／Git及其他reading-view输出不变。

Help／Policy内容reader分别完成实物delta；主agent完成Data delta；独立evaluator另用冻结源与真实派生作结构验证（包括Markdown实际解析），161个源标题、Primer28条summary li的0–3层嵌套、169个sidecar preview均对齐。该独立稳定子集检查不是最终全PR PASS，最终仍锁精确head/base。

| 六维状态 | MediaWiki Revision／Discussion | Wikidata Statement／Primer | Wikipedia Editorial Governance |
| --- | --- | --- | --- |
| 身份／版本 | UID/identity稳定；null→cutoff及2个oldid | UID/identity稳定；null→cutoff及2个oldid | UID/identity稳定；null→cutoff及4个oldid |
| 原件覆盖 | unknown→complete（2HTML+3图） | unknown→complete（2HTML+1图） | unknown→complete（4HTML+5图） |
| 文本提取 | partial→partial；截断已补齐，截图内细节仍有边界 | partial→partial；截断已补齐，图内细节仍有边界 | partial→complete；四政策意义与结构已核 |
| 本地持久化 | 旧root保全；新增完整原件及normalized pair | 旧root保全；新增完整原件及normalized pair | 旧root保全；新增完整原件及normalized pair |
| 公开再分发 | unknown→allow，混合CC0/BY-SA4按NOTICE履约 | unknown→allow，文字BY-SA4／图CC0分开 | unknown→allow，文字BY-SA4／独立BY-SA3/PD图分开 |
| 知识准入 | null→null，无新增claim/trusted | null→null，无新增claim/trusted | null→null，无新增claim/trusted |

本批准确UID仍为 `methodology:mediawiki-revision-discussion`、`methodology:wikidata-statement-model`、`methodology:wikipedia-editorial-governance`。三个body_quality_verified均true；严格complete_target_consumable仅Policy为true，Help/Data保留具体text partial和ocr_assessment。此行动桶仅表示未来有纯文本需求时可定向处理截图/图内细节；原图已在repo、正常正文可消费，不新增全图OCR或trusted作为main收口门槛。

| 实物结果 | Help | Data | Policies |
| --- | ---: | ---: | ---: |
| normalized正文行数／bytes | 778／35,317 | 1,231／63,093 | 9,485／301,441 |
| 新sidecar／旧root selectors | 26／43 | 33／20 | 110／120 |
| 全包文件数／bytes（含manifest） | 13／1,417,704 | 11／470,063 | 17／1,999,188 |

总计17原件／3,165,839B；三包41文件／3,886,955B，inventory不含manifest为38文件／3,812,684B。新增正文399,851B、sidecar127,743B。旧6个root正文/selector、完整旧manifest（包括原source_version键缺席）、原100条rights审计对象及原始前缀保全；新增3条审计，总103条，四方包相等。修复后每包两次默认严格重放全包byte_changes=0，fetch/prepare调用均为0，三套定向validator无错误；不是再次网络获取。

### 可复核的内容／定位证据

- Help：History 11步骤、Talk教学 `[edit]`、9行literal pre、Bob→Simon→Bob→Lisa嵌套及页末完整。最终consumer L18的481字符首段含比较及deleted-revision权限条件；source envelope为History L762–797。Talk literal pre为derived492–500，authored edit在505，最后MessageBox在745；新增首中末selectors均真实命中，无跨页/跨末注。
- Data：31章节、两类数据表、qualifier/negation/inheritance/OOP约束、五条references、Primer五表/三例子与末尾ranks完整。L47的219字符property段保留完整 `i.e.` 后relationship及datatype限定；source envelope为Data model826–854。第17个selector为source1048–1052→derived637–648的Format string properties；末条为Primer915–1097→derived1173–1200的Ranks，最后more-values说明在，未吃末注。
- Policies：106章节、政策状态/nutshell、全部限制/正反例、34注释/参考与真实末尾已读；2,641个保留可见文字叶按源序零遗漏。78帽注原文保留；新摘录为derived1515的完整责任句，逐字对应Verifiability源1160，属于Build consensus selector（source1155–1161→derived1458–1520），不摘导航。NOR四标记仍X/N、X/N、check/Y、X/N；Consensus仍Y/Y/N。110条selectors首/中/末及全部bounds/preview复核通过。

上面位置均相对§2列明capsule的source文件或normalized/document.md；末节source EOF包络可含已声明排除的skin/footer，不冒称等长连续raw引文。照片/绘画未OCR不构成政策论证缺口，Policy文本complete不宣称像素、图形几何或原生排版无损。Help两截图及Data图内部字段/空间关系仍按partial明确保留；oldid不锁全模板/skin历史、混合许可与商标/辖区限制未取消。

### 固定集合对账

215＝131非repo＋84GitHub不变；非目标128项的对象和原YAML块均零漂移，全部131项knowledge不变，上一PR19 execution完整进入历史。当前原件complete36／partial6／unknown75／metadata_only14；文本complete7／partial45／unknown65／unavailable14；公开allow32／block65／unknown34；严格locallycomplete7／unresolved124。其余124不是本PR全部完成的暗示，仍按现有逐UID状态继续收敛。当前coverage report-aware默认auditor PASS；详细各桶/类型计数见frontmatter与机器台账。

## 13. 全局生成、实际命令与最终关闭门控

只调用既有 `rebuild_registry`／`write_indexes_and_audit` 刷新215项registry、index与completeness，固定build stamp仍为 `2026-09-16T04:30:26Z`；实际GET时间另外逐件记录，没有倒填获取时间。代码和聚合输入变化需要传播全局build identity，因此执行完整demo/Wiki重建，而非保留stale release。最终本地 build 为 `build:llm-wiki-v0:39419dbd8ad82c9e`：36 selected、72 claims、72 evidence、135 Wiki pages、357 typed links、3 context packs。03_sources、04_claims、02_entities 相对本批基线无内容差异；没有将本三UID选入知识生成。

Python为3.12.13（`/tmp/llm-wiki-ci-312-260916/bin/python`），使用已声明依赖。下列检查均实际执行；代码/正文是同一最终候选树，最终提交后仍以该head对应当前base的远端CI复核，不借启动提交的绿色结果。

| 命令／检查 | 实际结果 |
| --- | --- |
| `make test PYTHON=<Python3.12>` | PASS，190 tests；包括83 integrity、19 excerpt及其余既有回归。 |
| `make demo PYTHON=<Python3.12>` | PASS，上述build identity，135页/72claim/36source，demo及release验证均零错误。 |
| `make validate PYTHON=<Python3.12>` | PASS；248 YAML、215 metadata，215 manifests、3130 inventory hashes、25479 selectors；56 Markdown、80相对链接；demo/release均通过。 |
| 默认 `scripts/audit_non_repo_coverage.py` | PASS；无检查绕过，128非目标对象/原YAML块、131knowledge和前execution保全。运行时仅降噪既有PDF库日志，不改变检查。 |
| `make reproducibility PYTHON=<Python3.12>` | PASS，`committed_tree_replay`、`full_demo_replay`、`compiler_only_replay`、`read_only_validation`四阶段各169生成文件byte-identical。 |
| 三UID默认严格本地重放 | 修复后逐套两次，41包文件全byte-identical，禁止fetch/prepare且调用均0；原17原件与旧6文件不变。 |
| 手写code/test/docs/raw-data的scoped `git diff --check` | PASS；保留的原HTML字节及结构派生中的源生空白不擅自清洗。 |

reproducibility是既有工作树生成物的前置快照与重建比较，不冒称已完成fresh main checkout；后者仍属P5。既有PDF路径可能打印可选fontTools/CFF字体提示，但本轮命令全部exit0，未新增依赖或改变既有PDF正文/提取限制。

手写输入为本报告/台账、五个既有code/test路径、三canonical的版本/准入、三NOTICE及rights/coverage目标行；17原件为未改响应bytes。生成物为三个capsule的normalized pair/库存/快照/README、现有index/registry/completeness以及既有demo/Wiki全局身份传播，不新增选源、claim或框架。完整旧取得历史与非目标128项不变。

最终仍需：提交并push实际候选、核该head/base当前CI、非作者evaluator三维PASS且发布完整COMMENT（不伪造人类APPROVE），再Ready与正常合并work。若出现真实FAIL则回到planner→executor→evaluator，不直接关闭遗弃工作。父PR1、P4/P5、main交接、其余未决UID、全库公共清关、trusted与管理员设置未在本批宣称完成；不删除branch或关闭issue。
