---
phase: P3-WIKIMEDIA-HTML-01
status: startup_revision_preflight_pending
base_sha: 0bcc23a5ea8069e1868f4f12610e5ef29375d98f
execution_branch: codex/p3-wikimedia-html-01-260917
adapter_family: generic_web_or_document_v2
action_bucket: html_article_snapshot
source_uids:
  - methodology:mediawiki-revision-discussion
  - methodology:wikidata-statement-model
  - methodology:wikipedia-editorial-governance
source_network_requests: 0
startup_repository_changes: report_and_branch_ledger_only
---

# P3-WIKIMEDIA-HTML-01：三个方法文档 UID 的有限八页 HTML 物化

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
    "status": "startup_revision_preflight_pending",
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "html_article_snapshot",
    "source_uids": ["methodology:mediawiki-revision-discussion", "methodology:wikidata-statement-model", "methodology:wikipedia-editorial-governance"],
    "target_pages": [
      {"uid": "methodology:mediawiki-revision-discussion", "identity_url": "https://www.mediawiki.org/wiki/Help:History", "source": "source/help-history.html"},
      {"uid": "methodology:mediawiki-revision-discussion", "identity_url": "https://www.mediawiki.org/wiki/Help:Talk_pages", "source": "source/help-talk-pages.html"},
      {"uid": "methodology:wikidata-statement-model", "identity_url": "https://www.wikidata.org/wiki/Wikidata:Data_model", "source": "source/wikidata-data-model.html"},
      {"uid": "methodology:wikidata-statement-model", "identity_url": "https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer", "source": "source/wikibase-datamodel-primer.html"},
      {"uid": "methodology:wikipedia-editorial-governance", "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Verifiability", "source": "source/verifiability.html"},
      {"uid": "methodology:wikipedia-editorial-governance", "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view", "source": "source/neutral-point-of-view.html"},
      {"uid": "methodology:wikipedia-editorial-governance", "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:No_original_research", "source": "source/no-original-research.html"},
      {"uid": "methodology:wikipedia-editorial-governance", "identity_url": "https://en.wikipedia.org/wiki/Wikipedia:Consensus", "source": "source/consensus.html"}
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
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
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
      "assets": "no_asset_GET_without_exact_src_role_credit_scope_and_contract_amendment",
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
    ]
  }
}
```

## 7. 验收与收口，不无限扩批

单 writer 写三个 capsule／canonical／rights review／coverage／aggregates；其他 agent 仅并行读八份暂存原件的版本、正文边界和可见信用。每 UID 按2／2／4页逐页核正文开中尾、heading层级、页末、表／例子／代码、必要图／独立声明；不能只核第一主页面便宣称组合完整。每套新增 selectors 首中末语义核查并验证源与derived范围。保留三旧 `document.md` 和183个 root selectors 字节，新增 `historical_acquisition` 保留完整旧 revision／retrievals／rights／materialization／local_files／null版本观察；新根当前表示与历史明确区分。

准入后 root完整package／NOTICE／唯一末注与审计齐备；给三项 before→after，原件、文本、公开、消费与 knowledge 分开。新增 fulltext review 使用既有追加审计机制，不改既有100条审计观测。无法合法公开的实际文档如实 unresolved，保留有限官方尝试与具体决策，不能拿 unknown=无正文或新框架需求做豁免。

三个 UID 未 selected：保留 selected set、claims、evidence、collector assessment 原字节；允许已有全局 build identity 的必要传播，不能提交 stale release。代码只补上述显式 opt-in；fixtures 覆盖2／4多源、wrong oldid／URL、缺页、inventory／snapshot drift、旧root保留、正文container排除与源selector语义，旧W3C／Git测试不变。精确 head 的 `make test`／`make validate`／`make demo`／`make reproducibility`、completeness与coverage校验，加当前CI与独立三维PASS后正常合work。离线双重放不冒充双GET。

真实风险／待核只有：八个实际revision及页面移动；八页实际文字许可／可见导入信用；实际正文DOM和关键图；上述已有helper的小接口联调。初步无删除、用途或管理员权限决定需要用户确认。若观察到真正未授权表达则报告具体页／段／scope最小决定，不追全部版本、模板和编辑历史；P4/P5与PR1main仍按05/06既有条件收口，不追加trusted或全图OCR门槛。
