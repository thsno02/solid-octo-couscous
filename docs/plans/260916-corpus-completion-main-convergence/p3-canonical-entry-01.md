---
phase: P3-CANONICAL-ENTRY-01
status: locally_verified_pending_current_head_CI_and_independent_evaluation
base_sha: 506a33dbd92adc5ca11a1402030bbd32ace3b760
execution_branch: codex/p3-canonical-entry-01-260917
adapter_family: generic_web_or_document_v2
action_bucket: canonical_repair
source_uids: ["industry-doc:microsoft-fabric-ontology-preview","doi:10.1038/s41587-021-01054-6","journal-doi-10.1016-0004-3702-79-90032-7","methodology:ontouml-ufo","paper:The-Basic-AI-Drives"]
coverage_summary: {"collection_records":215,"non_repo_total":131,"github_repo_excluded":84,"reported_content_tier_counts":{"excerpt_capsule":23,"full_text":97,"metadata_capsule":11},"source_type_counts":{"arxiv":73,"biorxiv":2,"blog":10,"industry":2,"journal":11,"methodology":7,"paper":2,"standard":24},"original_artifact_counts":{"complete":37,"metadata_only":13,"partial":6,"unknown":75},"text_extraction_counts":{"complete":8,"partial":45,"unavailable":13,"unknown":65},"action_bucket_counts":{"access_restricted":9,"author_manuscript_fetch":2,"complete_verified":8,"html_article_snapshot":11,"identity_or_version_ambiguous":3,"needs_boundary_verification":65,"ocr_assessment":21,"parser_only":6,"public_persistence_decision":4,"standard_spec_fetch":2},"public_redistribution_counts":{"allow":33,"block":65,"unknown":33},"content_inspected_full_text":47,"structure_only_full_text":50,"locally_persisted_complete":8,"knowledge_candidate_sources":30,"knowledge_trusted_sources":0,"knowledge_sources_without_demo_claims":101,"unresolved_sources":123}
---


```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-CANONICAL-ENTRY-01",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "506a33dbd92adc5ca11a1402030bbd32ace3b760",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "source_uids": [
      "industry-doc:microsoft-fabric-ontology-preview",
      "doi:10.1038/s41587-021-01054-6",
      "journal-doi-10.1016-0004-3702-79-90032-7",
      "methodology:ontouml-ufo",
      "paper:The-Basic-AI-Drives"
    ],
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "canonical_repair",
    "allowed_paths": [
      "docs/plans/260916-corpus-completion-main-convergence/p3-canonical-entry-01.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "raw_data/industry/Microsoft Fabric Ontology Preview/metadata.yaml",
      "raw_data/journal/OBO Foundry in 2021/metadata.yaml",
      "raw_data/journal/A Truth Maintenance System/metadata.yaml",
      "raw_data/methodology/OntoUML and UFO/metadata.yaml",
      "raw_data/paper/The Basic AI Drives/metadata.yaml",
      "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/**",
      "materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/**",
      "materialized_sources/corpus/journal-doi-10.1016-0004-3702-79-90032-7--641228a2/**",
      "materialized_sources/corpus/methodology-ontouml-ufo--a19a68ba/**",
      "materialized_sources/corpus/paper-The-Basic-AI-Drives--03d9a4da/**",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_rights_review.yaml",
      "scripts/materialize_all_sources.py",
      "scripts/validate_materialization_completeness.py",
      "tests/test_materialization_integrity.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py",
      "experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_excerpt.py",
      "materialized_sources/index.yaml",
      "materialized_sources/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "source_registry/README.md",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/{materialization_snapshot,wiki_build_request,page_plan}.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/{05_wiki,06_evaluation,07_review,08_release}/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
    ],
    "generated_paths": [
      "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/{source-metadata.yaml,manifest.yaml,README.md,NOTICE.md}",
      "materialized_sources/corpus/doi-10.1038-s41587-021-01054-6--5fa5a2aa/{source-metadata.yaml,manifest.yaml,README.md,NOTICE.md}",
      "materialized_sources/corpus/journal-doi-10.1016-0004-3702-79-90032-7--641228a2/{source-metadata.yaml,manifest.yaml,README.md,NOTICE.md}",
      "materialized_sources/corpus/methodology-ontouml-ufo--a19a68ba/{source-metadata.yaml,manifest.yaml,README.md,NOTICE.md}",
      "materialized_sources/corpus/paper-The-Basic-AI-Drives--03d9a4da/{source-metadata.yaml,manifest.yaml,README.md,NOTICE.md}",
      "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/normalized/{document.md,selectors.jsonl}",
      "materialized_sources/index.yaml",
      "materialized_sources/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "source_registry/README.md",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/00_inputs/{materialization_snapshot,wiki_build_request,page_plan}.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/01_ontology/meta_kb_ontology.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/02_entities/domains.jsonl",
      "experiments/v0_meta_kb_initialization_demo_260910/{05_wiki,06_evaluation,07_review,08_release}/**",
      "experiments/v0_meta_kb_initialization_demo_260910/README.md"
    ],
    "approved_originals": [
      {
        "uid": "industry-doc:microsoft-fabric-ontology-preview",
        "url": "https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/overview.md",
        "local": "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/source/docs/iq/ontology/overview.md",
        "selected_version": "git:91971feb08d699c09c20125faccae35effd60166"
      },
      {
        "uid": "industry-doc:microsoft-fabric-ontology-preview",
        "url": "https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/includes/feature-preview-note.md",
        "local": "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/source/docs/includes/feature-preview-note.md",
        "selected_version": "git:91971feb08d699c09c20125faccae35effd60166"
      },
      {
        "uid": "industry-doc:microsoft-fabric-ontology-preview",
        "url": "https://raw.githubusercontent.com/MicrosoftDocs/fabric-docs/91971feb08d699c09c20125faccae35effd60166/docs/iq/ontology/includes/refresh-graph-model.md",
        "local": "materialized_sources/corpus/industry-doc-microsoft-fabric-ontology-preview--512d8f84/source/docs/iq/ontology/includes/refresh-graph-model.md",
        "selected_version": "git:91971feb08d699c09c20125faccae35effd60166"
      }
    ],
    "explicitly_out_of_scope": [
      "其他UID/整站/外链参考文献/数据模型下载",
      "UID或source_type迁移；历史原件/diagnostic/selector删除覆盖",
      "其他四UID的新PDF/XML/SI/图片/未知许可全文公开",
      "挑战/TLS/登录/付费绕过；私有MicrosoftDocs发布仓库访问",
      "新framework/依赖/workflow/防御性身份体系",
      "新增demo selection/claim/trusted",
      "main合并/issue关闭/管理员设置/分支清理；自评PASS"
    ]
  }
}
```

# P3-CANONICAL-ENTRY-01：修复五项正式入口并保留 Fabric 原生正文

状态：启动合同（startup contract），尚未正文执行或独立 PASS。已读 Issue #3/#4 与计划 README、02—06、plan.yaml、branch-ledger。2026-09-17 远端仅父 PR #1 open/Draft；work 为上述 base，main 为 99ce4670be91637209d67792de0962404fa96488。PR #20 已正常合入 work，独立 review 5232296216、CI 35172384895、merge 506a33dbd92adc5ca11a1402030bbd32ace3b760；不沿用其 PASS 到本批。

上段为启动时历史；当前实物与验证见文末。Fabric已完成本批正文表示，其他四项有界入口修复与真实未决已落盘；最终head/base独立审核、CI、merge和main尚未完成。

## 判断与路径

目标是同一 collection 的真实文档在 repo 可继续消费。比较只修链接、抓渲染网站、固定官方原生文本三条路径：Fabric 选择已由官方页面 Edit 链接确认的公开原生 Markdown，只保留 overview 与两条实际 include，明确采用 public Git commit，不冒称它与私有部署 commit 或当前 HTML 字节相同。其余四项没有本批可正常取得且准入的完整正文，保留真实未决，不因找到正式记录就宣布获取完成。

planner 独立只读检查最小接口；主线负责入口证据/准入/串行集成；executor 只实现合同；最终另调非作者 evaluator 按精确 HEAD/BASE 审核需求、agentic 判断、核心质量。任何 FAIL 回到修复，不弃置关闭。

## 有界正式入口观察（不是正文完成）

2026-09-17T07:06:31Z 起对五个原 canonical 默认 curl GET、正常 TLS、最多5次重定向；以下均无重定向，TLS verify=0。诊断响应仅私有暂存，不公开挑战页。

| UID（完整列表见合同） | 实际请求与结果 | 已观察正式证据与处理 |
| --- | --- | --- |
| Fabric | https://learn.microsoft.com/en-us/fabric/real-time-intelligence/ontology/overview，404/17593 bytes | 新官方 canonical https://learn.microsoft.com/en-us/fabric/iq/ontology/overview，200/55531 bytes，仍preview；Edit→public MicrosoftDocs/fabric-docs/docs/iq/ontology/overview.md。固定 public commit原稿不是private deployment证明。 |
| OBO | https://doi.org/10.1038/s41587-021-01054-6，404/10616 bytes，DOI not found | 正式 OUP Database 2021 baab069，DOI 10.1093/database/baab069；PMID34697637↔PMC8546234。25作者与作品内容核闭，不是旧DOI注册别名。OUP页面缓存明示文章CC-BY4；raw在07:08:44Z为403/5566B挑战；PMC在07:10:28Z为200/21203B挑战，均不是论文。PDF/XML真实href未观察，不猜址。 |
| Truth Maintenance | https://doi.org/10.1016/0004-3702(79)90032-7，404/10620 bytes | ScienceDirect正式记录 https://www.sciencedirect.com/science/article/pii/0004370279900080：Jon Doyle，Artificial Intelligence12(3)，1979年11月231–272，正确DOI10.1016/0004-3702(79)90008-0；机构正式作品目录 https://groups.csail.mit.edu/medg/ftp/doyle/ 第20项同刊页，无该项PDF链接。出版记录有组织访问/Purchase PDF，不伪称已取全文或公开许可。 |
| OntoUML | https://ontouml.org/，403/402 bytes | 当前响应为本地网络域名策略阻止，不冒充上游403或历史TLS错误。web缓存portal与/ontouml/均只有导航短页，无已证目标完整文档/公开许可，保持未决。 |
| Basic AI Drives | https://dblp.org/rec/conf/agi/Omohundro08，200/7439 bytes | Anubis挑战不是论文。DBLP缓存书目AGI2008pp483–492，CC0仅元数据。作者正式页面 https://selfawaresystems.com/2007/11/30/paper-on-the-basic-ai-drives/ 确认2008会议作品并说明链接稿修订于2008-01-25；未取该PDF，公开再分发许可仍未观察。旧115字符诊断与selectors保留，不作为正文。 |

OBO身份/许可出处：[OUP正式作品页](https://academic.oup.com/database/article/doi/10.1093/database/baab069/6410158)、[PubMed正式记录](https://pubmed.ncbi.nlm.nih.gov/34697637/)。网页工具的可读缓存不等于本机raw200。没有执行挑战、浏览器脚本或来源代码；没有取得新PDF/XML/SI/图片。

TMS 的 DOI／期号／月份来自上述 ScienceDirect 正式出版页面的可读搜索缓存（本轮正常限定查询再次观察，缓存标注约三周前抓取），不是成功 raw GET，也不是正文取得。MIT 官方作者目录独立核对题名、作者、刊名、卷／年／页码，但没有明示 DOI。独立 evaluator 此轮 direct open 受阻，与先前可读缓存的证据性质分别记录；未访问搜索返回的第三方论文或镜像。

## Fabric 版本、范围与公开表示

原生overview在固定public commit的contents API已正常读取；两条字面include为 ../../includes/feature-preview-note.md（一次）和 includes/refresh-graph-model.md（两次）。合同只允许以上三原件；include检查如发现新实质依赖，先修订而不递归下载。其他教程/Graph/全产品链接不在目标正文内。

HTML显示Last updated2026-07-21，原生frontmatter ms.date=10/06/2025；各是原作者声明，不伪造新发布日期。来源为Microsoft及贡献者，公开[仓库说明](https://github.com/MicrosoftDocs/fabric-docs/blob/91971feb08d699c09c20125faccae35effd60166/ThirdPartyNotices.md)明确文档适用CC-BY4，代码MIT、商标保留；[完整许可证](https://github.com/MicrosoftDocs/fabric-docs/blob/91971feb08d699c09c20125faccae35effd60166/LICENSE)已读并取得200/18650B，ThirdPartyNotices200/1134B。允许这三个原生文档、忠实结构转换和摘录，保留来源、署名、许可/商标声明、改动说明；不据此将Learn站点skin重新许可。

沿现有git_snapshot retained helper；只补真实metadata-only历史没有root文档/selector时的sidecar消费，以及两条显式DocFX include按原位置展开。原始三文件字节不变，frontmatter不作为正文；无网络离线replay、真实line/section定位。不建立通用DocFX、HTML crawler或新framework。旧有正文历史的严格检查必须保持；缺旧文件不得通过新的metadata-only模式绕过。

## Before / 预期而非结果

五项均 original=metadata_only、text=unavailable、public=unknown、未selected/未trusted；Basic只有旧错误页。Fabric计划变为三原稿可消费，实际complete必须逐项开中末/末尾和全部include验证后填写。其他四项保持无正文并分别记录技术/持久化/身份限制；OBO的文章许可已证，不把下载挑战误写rights unknown。UID/source_type和旧失败历史不改写。

## 验证与明确未完成

执行后逐UID填写六维before/after、实际GET时间/响应/bytes、原件和派生文件、selectors首中末及缺口；更新coverage与必要aggregate。五项未selected，不新生claims；若生成器/aggregate影响global build identity，仅重放现有输出。make test、make validate、materialization completeness、coverage audit、make reproducibility在最终一致树运行；demo/repro不可与coverage读取并行。独立非作者三维PASS及当前head/base CI通过后才正常merge至work。

当前没有正文成功/complete结论、尚未独立审核、未进main；无trusted晋升、历史删除、强推、分支清理或issue关闭。其余126非repo来源不属本批。

## 合同后的实际取得与初步内容核查

上述启动提交 c91afd55c510ccf0a5e9a9a3dbd1e12da2f72396 已 push，并创建 [Draft PR #21](https://github.com/thsno02/solid-octo-couscous/pull/21)。之后才按合同取得三个原生正文文件；默认 curl、正常 TLS、无重定向，Content-Type 均为 text/plain; charset=utf-8。

| 固定 public commit 下的原稿 | HTTP Date（UTC） | 实际响应 |
| --- | --- | --- |
| docs/iq/ontology/overview.md | 2026-09-17T07:18:58Z | HTTP200，7686 bytes |
| docs/includes/feature-preview-note.md | 2026-09-17T07:19:00Z | HTTP200，403 bytes |
| docs/iq/ontology/includes/refresh-graph-model.md | 2026-09-17T07:19:02Z | HTTP200，447 bytes |

主线已逐字读三个原稿：overview 起于 ontology(preview) 定义，经四类模型概念与data binding／ontology graph／querying，结束为三条 Next steps；两种include实际出现1＋2次。第一段为 IMPORTANT 预览状态，第二段为 NOTE 上游数据须手动刷新；没有新增 nested include 或正文图片。不获取 include 内普通说明链接或三个 Next steps 指向的教程。两段各自frontmatter完整留在原件，但不是展示正文。

这证明三个已声明原生原件正常取得，不等于派生文本、可消费定位、机器包装或最终独立审核已经通过。独立内容 evaluator 只读检查稳定输入；代码与包装由不同 executor 按文件所有权实施；最终仍审核准确提交对。

## 最小接口与状态语义澄清

planner 实读发现既有 router、replay、history validator 和 completeness 主循环均假定旧 root 文档与 selectors 存在。本批只兼容有真实 metadata-only 历史、旧两文件在历史库存及当前磁盘均不存在的单 sidecar；既有 paired 模式继续严格保全旧文件，不把缺失 fallback 成 metadata-only。DocFX 只展开主文件显式列出的两种 include，保留三份原件，按每次调用位置记录来源行与派生行；未声明或嵌套 include 不静默抓取。

现 coverage 的 public_redistribution.state 与**已保留表示的 publication gate**一致，不是作品是否有公众许可的完整替代指标。Fabric 三文件实际准入后可记该表示 allow，具体署名/改动说明条件保留在 package。OBO 文章级 CC BY 4.0 已证，另记 document_permission=allow_with_conditions；目前尚无取得的正文载荷可绑定公开表示，root gate 仍 unknown。它的获取缺口是实际挑战及未观察到可正常取得的精确 PDF/XML 地址，不能称为“论文许可未知”、不能因此重复索取作者授权。本批不为这个说明扩写审计框架。

## 实施与内容验收（尚非最终关闭门控）

代码实现限四个既有文件：materializer、completeness validator、materialization integrity tests 和既有 consumer tests。无新adapter/依赖/workflow；build_demo.py未改。定点14项正负测试与consumer20项通过，覆盖新single-sidecar、两种include/重复调用、未声明/嵌套/未使用映射拒绝及旧paired Git/dated HTML/wiki行为。主线完整make test（Python3.12.13）196项通过；最终CI另记，不借用PR20结果。

主线首次离线调用既有replay，仅在明确首次派生时check_derived=False；没有重抓原稿或清空capsule。实际产物是12,743字符的normalized/document.md、16条normalized/selectors.jsonl和8项当前inventory；不存在伪造的旧root文档/selector。原稿三份总8,536 bytes，NOTICE保留完整原Legal Notices及CC BY4法条。

主线与包装executor完整读派生全文/16定位器：12个原生正文heading保持，overview源L15预览提示一次，L56/L64刷新提示分别在上下文中展开；两次include有不同派生范围与锚点，来源指同一真实原件，源行不跨其他文件。overview前置元数据沿既有helper作为明确的collector literal fenced metadata展示（第1个selector），不是源正文；两份include的frontmatter不混入正文。其余15个selector对应12个正文段及3次include，不以locator数量代替正文验收。

真实consumer路径验证：choose_local_document与choose_local_selectors都选择normalized pair，source_excerpt(reading_view=True)取派生L29的真实ontology定义，未引用frontmatter、collector标签或NOTICE。没有因此增加该UID的demo选入或claim。

独立非作者canonical21_content_evaluator已核稳定原稿、许可和四项未决的证据，readiness PASS；其建议明确TMS搜索缓存性质已落实。本结论不覆盖尚未完成的最终聚合、精确提交、CI或最终三维审核，不能单独用于merge。

集成纠偏：首遍aggregate使用新构建时刻，虽demo验证通过，但差异核对发现36个source及72个evidence/claim的provenance/temporal出现无关时间波动。主线据实撤回这一生成策略，用已有函数按原确定性aggregate时间2026-09-16T04:30:26Z重建；该字段不是本轮墙钟时间，三份原稿真实GET的HTTP Date仍逐件保存，不改写。重建后必须核source/evidence/claim保持原字节，仅允许必要global build identity变化；不放宽合同范围容纳无关diff。

## 最终一致树的本地验证记录

| 实际执行 | 结果 |
| --- | --- |
| make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python | 196 tests通过；完整集合包含88 materialization与20consumer tests |
| 实际Fabric generic→materialize_one严格离线重放各一次 | 整capsule含manifest共9文件逐字节不变；fetch/prepare调用0，不用首次生成豁免绕过正常重放 |
| existing aggregate helpers＋make demo | NOTICE纠偏后build3c4b53aa61004c0b（此前5a51e430f7ed833a为修正前历史结果）；36selected/72claims/72evidence/135pages/357typed links/3context packs；source、claim、evidence三个JSONL与BASE逐字节相同 |
| make validate（含completeness） | raw248YAML/215metadata；215manifest、3136受检hash、25495selectors、0errors；57docs/80相对链接；demo/Wiki 0errors |
| NOTICE修正后make reproducibility | exit0；committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四轮均169文件byte-identical，最终完整性/文档/demo/Wiki校验0errors |
| /tmp/llm-wiki-ci-312-260916/bin/python scripts/audit_non_repo_coverage.py | exit0 PASS；131非repo完整复算，summary与本报告frontmatter相等，严格完整8/未决123 |
| 全局公开表示审计只读复算 | active103/audited108，64blocks及2个既有包不一致；本批5UID无新增block/error。两不一致仍为arxiv:2404.16130和arxiv:2502.18864，按既有P4对账，不称全库公开门控已通过 |

PDF检查仍有既有fontTools缺失的CFF编码提示；未新增依赖、未修改旧PDF文本、不把无损文本提取当已证。completeness的正式统计warnings=0并不抹去该库级提示。全部本地检查针对当前工作树，不能替代提交后当前head/base CI和独立审核，也不是fresh main checkout。

## 五项实际 Before → After

| UID | 身份/选版 | 原件覆盖 | 文本提取 | 正文本地持久化 | 当前表示公开门控 | Knowledge / 未决 |
| --- | --- | --- | --- | --- | --- | --- |
| industry-doc:microsoft-fabric-ontology-preview | 旧失效Learn入口→Fabric IQ preview；旧日期seed→明确public git91971feb快照 | metadata_only→complete | unavailable→complete | 否→三原稿及normalized pair，全部库存tracked/可消费 | unknown→allow，CCBY4条件完整包装 | null→null；本选定目标resolved |
| doi:10.1038/s41587-021-01054-6 | 误DOI/Nature→正确DOI/OUP Database；null→2021-10-26 VOR选择 | metadata_only→metadata_only | unavailable→unavailable | 否→否，只有修复后metadata与历史 | unknown→unknown仅无载荷表示；article permission另明确CCBY4条件许可 | null→null；raw挑战、精确PDF/XML href仍未观察 |
| journal-doi-10.1016-0004-3702-79-90032-7 | DOI末尾90032-7→90008-0；null→1979刊载版选择 | metadata_only→metadata_only | unavailable→unavailable | 否→否，正式记录不是正文 | unknown→unknown，未观察正文public grant | null→null；出版访问与公众许可分别未决 |
| methodology:ontouml-ufo | 门户不变；selected_version仍null，目标具体边界未核闭 | metadata_only→metadata_only | unavailable→unavailable | 否→否，保留历史TLS及本轮本地策略诊断 | unknown→unknown | null→null；精确文档边界/版本及正常访问未决 |
| paper:The-Basic-AI-Drives | DBLP书目→作者正式作品页；null→作者明示2008-01-25修订稿选择 | metadata_only→metadata_only | unavailable→unavailable | 否→否，旧115字符诊断/3selectors不变，不是论文 | unknown→unknown，作者链接非public grant | null→null；未取得链接稿/未证正文再分发许可 |

每项完整BASE的身份/observed及六维before随coverage保留，五份historical_acquisition与BASE旧manifest全等；其余126个coverage对象及旧103个rights对象未改。current observed逐项与实际files/index/registry核对，28条证据路径/行范围有效；没有因身份或许可已证就推论原件完整。

全库重新汇总仍是215=131非repo＋84排除：原件complete37/partial6/metadata_only13/unknown75；文本complete8/partial45/unavailable13/unknown65；严格locally persisted complete8、unresolved123；public gate allow33/block65/unknown33；knowledge candidate30/trusted0/无demo claim101。本批增加的是一个严格完整目标，不是宣布131项全部完成。

## 独立审查纠偏（independent review correction）

非作者 evaluator 在逐字核查实现时发现：上游两段法律声明末尾无换行，collector 拼接的 closing fence 与原文末句同行，影响 CommonMark 展示。主线仅补两处分隔换行，不改三个正文原件或法律声明原文；NOTICE 实际24038 bytes，更新库存后整个capsule的local_bytes为62963。evaluator随后独立复读确认两个fence均正确闭合，全部16条定位器与原件/派生行匹配，四项未决保留真实限制，实现前核PASS。本次PASS不是最终提交对的关闭审核。

四项已修复或澄清入口不再停在canonical_repair：OBO/TMS转access_restricted，OntoUML转identity_or_version_ambiguous，Basic转public_persistence_decision；历史before仍保留原bucket。本批执行合同的primary bucket仍是canonical_repair，不因此扩大实施范围或宣布四项正文完成。新增分流只是让下一步对准实际阻碍。

验证环境纠偏：包装复核误用缺少pypdf的默认Python，曾得到20项既有PDF的stale observed；具体差异为PDF_SUPPLEMENT_PARSE / No module named pypdf，并非这些正文发生变化。未据此重写其余126条账本；改用与CI一致的指定Python3.12.13后，全131项coverage复算exit0 PASS。本批五项实际facts全等，其余126对象仍与BASE相同。
