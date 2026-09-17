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

## Fabric 版本、范围与公开表示

原生overview在固定public commit的contents API已正常读取；两条字面include为 ../../includes/feature-preview-note.md（一次）和 includes/refresh-graph-model.md（两次）。合同只允许以上三原件；include检查如发现新实质依赖，先修订而不递归下载。其他教程/Graph/全产品链接不在目标正文内。

HTML显示Last updated2026-07-21，原生frontmatter ms.date=10/06/2025；各是原作者声明，不伪造新发布日期。来源为Microsoft及贡献者，公开[仓库说明](https://github.com/MicrosoftDocs/fabric-docs/blob/91971feb08d699c09c20125faccae35effd60166/ThirdPartyNotices.md)明确文档适用CC-BY4，代码MIT、商标保留；[完整许可证](https://github.com/MicrosoftDocs/fabric-docs/blob/91971feb08d699c09c20125faccae35effd60166/LICENSE)已读并取得200/18650B，ThirdPartyNotices200/1134B。允许这三个原生文档、忠实结构转换和摘录，保留来源、署名、许可/商标声明、改动说明；不据此将Learn站点skin重新许可。

沿现有git_snapshot retained helper；只补真实metadata-only历史没有root文档/selector时的sidecar消费，以及两条显式DocFX include按原位置展开。原始三文件字节不变，frontmatter不作为正文；无网络离线replay、真实line/section定位。不建立通用DocFX、HTML crawler或新framework。旧有正文历史的严格检查必须保持；缺旧文件不得通过新的metadata-only模式绕过。

## Before / 预期而非结果

五项均 original=metadata_only、text=unavailable、public=unknown、未selected/未trusted；Basic只有旧错误页。Fabric计划变为三原稿可消费，实际complete必须逐项开中末/末尾和全部include验证后填写。其他四项保持无正文并分别记录技术/持久化/身份限制；OBO的文章许可已证，不把下载挑战误写rights unknown。UID/source_type和旧失败历史不改写。

## 验证与明确未完成

执行后逐UID填写六维before/after、实际GET时间/响应/bytes、原件和派生文件、selectors首中末及缺口；更新coverage与必要aggregate。五项未selected，不新生claims；若生成器/aggregate影响global build identity，仅重放现有输出。make test、make validate、materialization completeness、coverage audit、make reproducibility在最终一致树运行；demo/repro不可与coverage读取并行。独立非作者三维PASS及当前head/base CI通过后才正常merge至work。

当前没有正文成功/complete结论、尚未独立审核、未进main；无trusted晋升、历史删除、强推、分支清理或issue关闭。其余126非repo来源不属本批。

