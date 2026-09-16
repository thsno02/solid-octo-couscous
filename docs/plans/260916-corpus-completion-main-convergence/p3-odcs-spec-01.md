---
phase: P3-ODCS-SPEC-01
base_sha: 463b848b0b4abef33df6fa51f6fcf9bd7482a922
branch: codex/p3-odcs-spec-01-260917
status: local_validation_passed_exact_pair_review_and_ci_pending
pull_request: 18
source_uid: standard:odcs-3.2.0
source_acquisition: nineteen_fixed_commit_originals_http200_336418_bytes_admitted
independent_evaluation: frontmatter_blocker_resolved_final_exact_pair_pending
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
    complete: 30
    metadata_only: 14
    partial: 9
    unknown: 78
  text_extraction_counts:
    complete: 6
    partial: 44
    unavailable: 14
    unknown: 67
  action_bucket_counts:
    access_restricted: 7
    author_manuscript_fetch: 2
    canonical_repair: 5
    complete_verified: 6
    html_article_snapshot: 14
    identity_or_version_ambiguous: 2
    needs_boundary_verification: 68
    ocr_assessment: 18
    parser_only: 4
    public_persistence_decision: 3
    standard_spec_fetch: 2
  public_redistribution_counts:
    allow: 29
    block: 65
    unknown: 37
  content_inspected_full_text: 43
  structure_only_full_text: 50
  locally_persisted_complete: 6
  knowledge_candidate_sources: 30
  knowledge_trusted_sources: 0
  knowledge_sources_without_demo_claims: 101
  unresolved_sources: 125
---

# P3-ODCS-SPEC-01 — ODCS 3.2.0 规范正文补齐

当前状态：19原件及修后真实正文已完成有界内容验收。独立evaluator确认frontmatter核心质量阻塞已解除；183 tests、真实严格重放、demo/Wiki、全量validate、coverage audit及四阶段169文件repro均通过。原件与旧历史未改，Fig1纯文本图义仍partial。早期状态与首次统计保留为执行历史，不代表当前结果。提交后的准确HEAD/BASE CI/三维审核、merge及main仍未完成。

## 规划与真实起点（planning）

本批目标是补齐已收集的固定 ODCS 3.2.0 正文，不增加 UID、不抓整个 GitHub repo。当前唯一 work 已在 `463b848b0b4abef33df6fa51f6fcf9bd7482a922`：PR #17 正常 merged/closed，非作者三维 PASS 对应 HEAD `1afaf52fd3ba81ec9dba09d733ce4a3a01f19154` / BASE `879596f10f34344337b1be2f05a6ffa347fd9a86`、COMMENT review 5229044802、CI 35157849042 success。PR #1 仍 Draft，head 是该最新 work、base main `99ce4670be91637209d67792de0962404fa96488`。

主线延续已经完整读取的 Issue #3/#4、本目录 README、02/03/04、plan 与 ledger；本次重新核对 06 合同、上一批关闭结果、work 与 PR #1 的准确远端状态。短期分支从该 work 创建，当前仅登记两份启动文档，无正文 GET、代码改动或生成重建。旧分支保留，不删除、不强推，也不把 work 当作最终 main。

工作假设（working hypothesis）：现存 1,454-byte 首页正文只列 15 章标签及 Full example 入口，真正字段定义与完整例子尚未持久化。考虑“只更正台账”“抓渲染站点”“保留固定 commit 原生文档”三条路径，选择第三条；其正文边界、版本和最小离线派生最清晰，复用现有 retained helper，不造新框架。

## 启动合同（execution contract）

先发布本合同，再只取得明确列定 README／LICENSE 及必要固定目录信息。其余章／example 的准确 href 未在旧转换中保留，不能猜文件名；填满有界路径后修订远端合同，才获取对应正文。临时取得不自动授权公开持久化。

```json
{
  "execution_contract": {
    "plan_id": "nonrepo-materialization-main-convergence-260916",
    "phase": "P3-ODCS-SPEC-01",
    "base_branch": "work/v0-meta-kb-initialization-demo-260910",
    "base_sha": "463b848b0b4abef33df6fa51f6fcf9bd7482a922",
    "target_branch": "work/v0-meta-kb-initialization-demo-260910",
    "adapter_family": "generic_web_or_document_v2",
    "action_bucket": "standard_spec_fetch",
    "source_uids": [
      "standard:odcs-3.2.0"
    ],
    "upstream_commit": "f0bdad95346905d500be5ef4b2c2d9b1d95223b7",
    "selected_version": "3.2.0",
    "status": "startup_plan_exact_path_preflight_pending",
    "allowed_paths": [
      "raw_data/standard/Open Data Contract Standard 3.2.0/metadata.yaml",
      "materialized_sources/corpus/standard-odcs-3.2.0--affacf92/**",
      "raw_data/licenses/p3-odcs-spec-01-*.md",
      "raw_data/audits/non_repo_materialization_coverage_2026-09-16.yaml",
      "raw_data/audits/materialization_rights_review.yaml",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "docs/plans/260916-corpus-completion-main-convergence/p3-odcs-spec-01.md",
      "docs/plans/260916-corpus-completion-main-convergence/branch-ledger.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "generated_paths": [
      "materialized_sources/corpus/standard-odcs-3.2.0--affacf92/**",
      "materialized_sources/README.md",
      "materialized_sources/index.yaml",
      "source_registry/README.md",
      "source_registry/registry.yaml",
      "source_registry/registry.jsonl",
      "raw_data/audits/materialization_completeness_2026-09-10.yaml",
      "experiments/v0_meta_kb_initialization_demo_260910/**"
    ],
    "explicitly_out_of_scope": [
      "implementation before PR17 normal merge and latest work base confirmation",
      "chapter or full-example GET before exact fixed-commit path contract amendment",
      "latest or different-version substitution, all-site mirror or recursive external references",
      "JSON Schema as replacement body, full examples directory, ODPS, datasets, weights and runtime dependencies",
      "inheriting old text-only allow as new representation admission",
      "legacy document, selectors, history or shared-license deletion/overwrite",
      "pipeline or consumer edits before an evidenced minimal-change contract amendment",
      "handwritten experiment edits, new selected sources/claims/evidence/collector assessments",
      "perfect conversion/OCR, trusted promotion, administrator settings, history rewrite and branch cleanup"
    ],
    "execution_branch": "codex/p3-odcs-spec-01-260917",
    "initial_source_requests": [
      {
        "path": "docs/README.md",
        "url": "https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/docs/README.md",
        "proposed_local_path": "source/docs/README.md",
        "purpose": "actual fixed-version homepage and 15 chapter plus full-example direct href discovery"
      },
      {
        "path": "LICENSE",
        "url": "https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/LICENSE",
        "proposed_local_path": "source/LICENSE",
        "purpose": "actual fixed-commit work license"
      }
    ],
    "metadata_preflight": "read only fixed-commit tree paths and necessary navigation metadata; no all-file body download",
    "pre_get_gates": {
      "initial_requests": "only after startup PR published; scratch acquisition is not publication admission",
      "chapters_and_example": "all exact fixed-commit source/local paths and formats must be recorded in amended PR contract before GET",
      "publication": "inspect actual selected files credits/exclusions; old homepage allow does not automatically cover new representations",
      "consumer": "confirm strict git binding and explicit sidecar route; authorize exact minimal code paths only if observed necessary"
    }
  }
}
```

## 目标边界与预核（target boundary）

固定上游 commit 为 `f0bdad95346905d500be5ef4b2c2d9b1d95223b7`，canonical version 3.2.0／tag v3.2.0；旧网页的“Since v3.1.0”是分页说明，不换目标版本。以下是已有首页的准确标签／顺序，尚不是已核准的 source 文件名：

1. Fundamentals
2. Schema
3. Context
4. References
5. Data Quality
6. Support & Communication Channels
7. Pricing
8. Team
9. Roles
10. Service-Level Agreement
11. Infrastructures & Servers
12. Custom & Other Properties
13. Authoritative Definitions
14. Tags
15. Variables
16. Full example（直接完整示例，不以 JSON Schema 代替）

只核 fixed README 的直接链接及必要导航声明；不遍历全部 examples，不抓外链定义／其他版本／数据／runtime／模型资产。若原稿不是这些目标或例子来自不同作品，先解决具体身份边界，不下载相似内容凑数。

现有机器审阅指向固定 README 的 The Bitol Contributors / Apache-2.0 及同 commit LICENSE；旧 allow 只涵盖旧首页文字。本批审查选定实际文件的信用、另行许可与排除，保留 Apache 完整法条、原署名及修改说明，scope 只列真实原件。复用共享原法条或新增本批累计 NOTICE，不改共享许可、不做无具体反向证据的历史考古；新增公开范围 unknown 时不先提交正文。

## 最小消费与所有权（consumer / ownership）

沿用 `standard-odcs-3.2.0--affacf92` 胶囊。旧根 document／selectors／NOTICE 历史保持；新原稿按真实路径保存，新 consumer 为 `normalized/document.md` 与显式 `normalized/selectors.jsonl`。首页→15章→完整example按声明顺序组装，保留原表格／围栏／版权；使用真实 git commit 严格绑定，不冒充 dated HTML 响应。先核现有 git 分支是否直接支持新 sidecar；若必要，只修订合同加入精准最小 helper／validator／test 路径再改代码。YAML full example 必须是“示例”，不得默认为 schema。

主线负责固定边界／GET／公开准入和最终提交；代码预核只读，包装作者与台账作者串行写各自路径；独立 evaluator 不参与作者实现。仅一个活跃批次，不与后续 PDF／网页工作并行改 index/registry/coverage。先核选集；即使未 selected，global index 改动仍需必要 build identity 传播，不增 claim／evidence／collector assessment。

## 验证与明确非结果（validation / explicit non-results）

最终报告逐 UID 给出 original、text、persistence、selectors、public、knowledge 的实际 before→after；每份真实章节／完整例子核开中末、字段定义和例子，真实 source bounds 与配对 consumer 可回溯。缺口记录具体原因和 next action，不以首页存在推完整。离线 retained replay、对应 tests／validate／coverage／demo／repro须适用当前最终树；独立非作者在最终准确 HEAD／BASE 三维 PASS 且该 pair CI成功后，才能正常 merge 到 work。

目前没有新正文、公开准入、派生／CI／独立 PASS；没有进入 main、没有 trusted 晋级、没有 issue 关闭、分支删除或历史重写。后续仅在本批正常合并后启动下一批。

## 固定路径预核与获取修订（fixed-path acquisition amendment）

PR #18 已在本批 GET 前登记，startup HEAD `4a9161806c13dc961c75352265aeebb3867cf60c`／BASE `463b848b0b4abef33df6fa51f6fcf9bd7482a922`。README／LICENSE 各一次GET，2026-09-16 22:41:13 UTC启动、22:41:36 UTC全部结果完成观察，均HTTP200、text/plain; charset=utf-8、无redirect，分别2,465／11,357 bytes。README实际含15个同目录.md href及 `examples/all/full-example.odcs.yaml`；同commit非截断GitHub tree元数据逐项确认真实blob，例子确在docs/examples/all而不是猜根examples。目录元数据查询与这两正文GET分开计数。

现批准以下16文件各一次有界GET到临时审阅目录，再检查实际内容/信用/结构。完整URL统一为 `https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/` 加下表source path；repo候选保存为 `source/` 加同一path。当前仅获取授权，不是新范围公开准入。

| source path | format | 本地保全路径 |
| --- | --- | --- |
| docs/fundamentals.md | markdown | source/docs/fundamentals.md |
| docs/schema.md | markdown | source/docs/schema.md |
| docs/context.md | markdown | source/docs/context.md |
| docs/references.md | markdown | source/docs/references.md |
| docs/data-quality.md | markdown | source/docs/data-quality.md |
| docs/support-communication-channels.md | markdown | source/docs/support-communication-channels.md |
| docs/pricing.md | markdown | source/docs/pricing.md |
| docs/team.md | markdown | source/docs/team.md |
| docs/roles.md | markdown | source/docs/roles.md |
| docs/service-level-agreement.md | markdown | source/docs/service-level-agreement.md |
| docs/infrastructure-servers.md | markdown | source/docs/infrastructure-servers.md |
| docs/custom-other-properties.md | markdown | source/docs/custom-other-properties.md |
| docs/authoritative-definitions.md | markdown | source/docs/authoritative-definitions.md |
| docs/tags.md | markdown | source/docs/tags.md |
| docs/variables.md | markdown | source/docs/variables.md |
| docs/examples/all/full-example.odcs.yaml | yaml | source/docs/examples/all/full-example.odcs.yaml |

`docs/resources.md` 虽存在但非首页这15个直接章，不在本批下载列表。README frontmatter 的Bitol logo是品牌图，不当正文图获取；外链issue／引用作品不递归。全部LICENSE已读，Apache文件与现有法条大小一致；同commit tree没有NOTICE命名文件。新的逐文件许可scope、章节内实际依赖、Git sidecar消费支持仍待实物/代码预核，不提前allow、complete、CI或独立PASS。

## 最小 Git sidecar 修订（consumer amendment）

只读代码预核实证：现有 retained_text_selector_file 对 Git 新 sidecar（无binding／git_snapshot）均拒绝，旧Git重放会写根selectors；零代码方案不能满足保全合同。现批准明确opt-in `retained_text_binding: git_snapshot`，沿已有 Git retained helper 增新文档／sidecar配对，旧未opt-in Git行为不变。新document/normalized_document统一normalized/document.md，retained_text_selectors为normalized/selectors.jsonl，manifest同时声明旧根／新sidecar，总count两者相加；历史保存完整旧manifest和旧root bytes。

继续严格校验真实git revision、canonical版本/commit、每个原稿retrieval.commit与inventory及实际派生/selector provenance，正常wrapper失败不能降级或prepare。消费representation为retained_git_text_sources，整fence／collector-anchor排除沿已有reading view，不冒充HTML/TeX。实际已确认full example为source/docs/examples/all/full-example.odcs.yaml；来源项可声明role: example，仅修其展示为完整合同示例，不能再称YAML schema，旧schema默认不变。

仅授权五个现有路径：`scripts/materialize_all_sources.py`、`scripts/validate_materialization_completeness.py`、`tests/test_materialization_integrity.py`、`experiments/v0_meta_kb_initialization_demo_260910/pipeline/build_demo.py`、`experiments/v0_meta_kb_initialization_demo_260910/pipeline/test_excerpt.py`。代码作者不写正文、metadata、rights/coverage或聚合；不新造框架／依赖／workflow／anchor设计，audit已共享selector路由无需编辑。最小回归覆盖两次禁网重放、wrong commit/version、缺原件/sidecar、坏声明保全与旧Git/dated HTML不漂移，实物内容另验。

## 单件正文图修订（body figure amendment）

实际schema.md L21–25以Fig1解释object/property/element，引用 `img/elements-of-schema-odcs-v3.png`；它是正文图而非品牌。固定commit tree确认精确blob为133,050 bytes。仅批准GET `https://raw.githubusercontent.com/bitol-io/open-data-contract-standard/f0bdad95346905d500be5ef4b2c2d9b1d95223b7/docs/img/elements-of-schema-odcs-v3.png`，候选本地路径 `source/docs/img/elements-of-schema-odcs-v3.png`，取得后先核像素/credit/作品许可，再准入。不授权logo或其他外链下载。

context.md L91链接外部RFC-0038以说明完整cascading规范；本批保留该章实际规则和原链接，并准确说明这是外部规范引用，不把链接存在当作已保留RFC全文，也不自动扩展到整套RFC网络。

## 已取得的实物（acquired artifacts，准入/派生另验）

16个准确章节/示例于2026-09-16 22:43:54 UTC批次开始、22:44:29 UTC完成观察，全部HTTP200、text/plain; charset=utf-8、无redirect，共189,546 bytes。单PNG按修订合同于22:46:58 UTC开始、22:47:01 UTC完成观察，HTTP200/image/png、133,050 bytes、无redirect。与先前README及LICENSE合计19件、336,418 bytes；每件有实际URL/HTTP/类型/bytes及观察时间，不把Git tree元数据查询混入正文GET计数，也不编造逐传输时刻。

主线完整阅读末四章/完整362行YAML及LICENSE并目视Fig1；两名独立内容reader分别审其余核心章节/运营与服务器章节。代码作者只改已授权五路径，不参与这些正文判断。Fig1是元素/对象/属性的原作示意图，非品牌logo；有Orders/OrderLines等具体图内标签，不能把保存PNG当作纯文本已经无损。原作custom property的Avis、表格Required与条件required等表述保持原样，不私修样例或执行变量/SQL。正式逐表示准入和真实派生验收尚未结束，本节不是complete/PASS。

## 新表示公开准入（publication admission）

主线汇总两位内容reader完整原稿检查、自己的末四章/完整YAML/完整LICENSE阅读和Fig1实际像素检查，准入列定19原件（336,418 bytes）及其文本/selector派生。README、15章、完整YAML共17正文文件均实有The Bitol Contributors / Apache-2.0署名，固定LICENSE全文已核；所选文件无具体相反许可/第三方排除，Fig1无新信用标记，fixed tree无NOTICE文件。不把产品例子/外链RFC/品牌商标推为本包授权。

条件：原件逐字节保留；完整旧NOTICE及旧六字段许可包作为历史前缀/记录累积，原Apache法条不缩成链接；新package准确列19件及有限派生、原署名/许可证/修改说明。source_revision使用真实git commit；source_version_url为固定commit tree，仅身份载体、不是整repo授权；专用新NOTICE资产为raw_data/licenses/p3-odcs-spec-01-3.2.0.md。

旧metadata中未限定的content_sha256只指旧63,735-byte网站首页，不得当作新Git原稿摘要。将这条既有事实移入versioning.historical_html_response，明确旧source_url、bytes及原content_sha256，其他source_version/tag/snapshot_commit/previous_versions保持；full_text_url仍是固定v3.2.0文档身份入口，不冒充本轮实际GET。manifest历史保留完整旧字典（原本没有source_version键，不补null），root document/selectors不写。

本次准入不代表派生已完成或文本全线性化。PNG中的具体标签/关系、Context的外部normative RFC指向，以及References/Quality/Team/SLA/Server原生差异应真实保留；不得运行示例、擅修源稿、增加trusted或把后续缺口压成complete。现授权后续代码冻结后的唯一包装writer；正文质量与最终独立门控另验。

## 实物审核发现与纠偏（frontmatter）

首次实物为19原件336,418 bytes、派生3691行/202,924 bytes、新181定位加历史27；两次禁fetch/prepare严格磁盘重放均稳定。主线实际阅读发现README前置YAML中插入README-L4锚点，独立evaluator确认README与15章共16个frontmatter闭合`---`被误认成Setext标题。例如源README L4–5的image字段、fundamentals L3–4的description字段被标为H2；定位范围可解析不代表结构语义正确。原稿/root历史未改，既有自动excerpt仍是正文L33，但这不是放行理由。

该项作为核心质量阻塞退回executor。仅在明确git_snapshot opt-in中识别有界leading frontmatter，排除内部伪heading/anchor，保持原稿bytes、正文真实Setext/ATX/围栏和旧未opt-in派生行为。修正范围仅既有scripts/materialize_all_sources.py与tests/test_materialization_integrity.py，不新增框架/依赖/源GET。随后由已有严格重放更新本UID的派生pair，内容reader复核改变的边界，独立evaluator重新审查。上述首次统计仅历史观察，不是最终交付统计；最终准确HEAD/BASE门控仍待完成。

独立复核补充：插入anchor已使派生中的原本有效YAML不再连续有效；仅过滤sidecar也不能阻止普通Markdown renderer将闭合横线当标题。故同一git_snapshot修正中，将有界leading frontmatter明确作为collector metadata的literal围栏展示，保持原始内容与source行可追踪，原件仍逐字节不变。正文真实标题和原围栏不因此重写。

修后主线实际调用默认严格materialize_generic→materialize_one（固定2026-09-16T22:58:20Z；fetch/prepare均禁止），第二次27个胶囊文件逐字节稳定。修正只改变manifest、新document和新sidecar，19原件、旧根document/selectors、历史字典与完整旧NOTICE前缀不变。新document为3739行/204,495 bytes，新定位仍181（加旧27共208）；数量未下降，因为16个伪section变为无heading的真实file-prefix，而非删除前置内容。全部16个metadata block在literal围栏内连续原样显示，真正first heading从自身source行开始。

主线修后再次完整核对末四章的metadata边界和完整362行YAML原文。最终source→consumer首/中/末范围如下（source均相对本胶囊source/docs；数字不是质量代理）：

| source | 首／中／末 source 行 | 对应 consumer 行 | 核心保全 |
| --- | --- | --- | --- |
| custom-other-properties.md | 1–10 / 38–50 / 67–73 | 2998–3012 / 3052–3064 / 3093–3099 | 六字段、vendor MUST、原Avis差异、两个完整例子及contractCreatedTs |
| authoritative-definitions.md | 1–10 / 17–32 / 43–61 | 3106–3120 / 3133–3148 / 3165–3183 | 五字段、九个建议type、Root-only canonicalUrl、自定义type规则 |
| tags.md | 1–10 / 29–38 / 53–61 | 3190–3204 / 3232–3241 / 3262–3270 | array-of-strings、七合法位置、五项建议及真实章间链接 |
| variables.md | 1–10 / 40–46 / 54–60 | 3277–3291 / 3330–3336 / 3350–3356 | literal变量、缺值MUST NOT空串、round-trip token、port例外；不执行样例 |
| examples/all/full-example.odcs.yaml | 1–362（完整单份原文） | 3365–3726 | 完整示例连续未变，明确example而非schema，标准版本与合同版本分开 |

本次修后完整make test（Python3.12.13）183 tests通过，五代码路径与计划文档diff --check通过。内容reader和非作者evaluator的修后定点复审、全量聚合/台账/CI及最终准确提交门控仍待完成。

## 修后内容验收与表示结果（content acceptance）

上述待审已完成：两组reader分别核README/前五章及六个运营章，主线核末四章/完整YAML；所有17正文原稿和真实派生均有实物检查。前六稿49个正文围栏/189表行未丢，运营六章48表/225行/8正文围栏及41个server完整保留；metadata新增围栏不混算正文示例。Source-native差异（References的string表与array例、Quality的缩进/占位符、Team的current/deprecated规则、SLA cron、服务器enum与Custom字段并集）均未私修。

独立evaluator在自有临时拷贝上核全部17source连续范围/181preview、16literal prefix及两次默认严格离线重放，27文件字节稳定；另用精确BASE实现与当前未opt-in实现组装真实17原稿，document bytes/selector objects相同。原P2因此关闭，不用“测试绿”掩盖实物语义错误。修后实际consumer为normalized/document.md+normalized/selectors.jsonl，自动excerpt来自L36 Executive Summary正文，不来自metadata、代码或NOTICE。主线将body_quality_verified置true并再次严格重放稳定；此flag只表示已实读验收，不等于text complete、标准样例可执行或trusted。

关键最终实物位置：README正文L29–73；Schema完整到L792、Fig1图片L192；Context的外部RFC-0038原引用L909；References完整综合例L1315–1401；Quality尾operators L1786–1823；Team新/旧username规则L2065/L2114；SLA条件必需L2291/L2293；41server实际节L2406–2991；最后四章与完整YAML见前表。Fig1的Orders/OrderLines列、四组logicalType/physicalType/name/physicalName配对及分类/包含连线需打开保留PNG消费，不能用caption冒充已完整线性化；不新造外键箭头或修图中OrdersLines拼写。

| UID：standard:odcs-3.2.0／维度 | Before | After |
| --- | --- | --- |
| 目标身份与原件（original） | 固定3.2.0，但只有旧首页派生；original unknown/partial_check | 同commit README+15章+完整例子+LICENSE+Fig1共19原件336,418 bytes；original complete/verified |
| 文本提取（text） | unknown/partial_check；根文档2536 bytes不足以代表规范 | 新collector Markdown3739行/204,495 bytes；text partial/verified，具体图义限制仍在 |
| 持久化（persistence） | 5件inventory/25,850 bytes；无目标原稿集合 | 26件inventory/696,674 bytes，已纳入Git索引；旧根文档、旧27定位、完整历史字典/NOTICE前缀保全；严格全目标线性文本完整标志仍false |
| 定位与消费（selectors） | 27个旧首页定位；未核规范语义 | 新181定位连续覆盖17原稿、preview和实际正文/metadata语义已核；加旧27共208，真实consumer显式用新pair |
| 公开再分发（public） | 旧首页范围allow，不能移作新全文许可 | 仅19列定原件与有限派生的新package allow；四方一致、完整Apache与原署名/修改说明保留；外链和商标不扩大 |
| 知识准入（knowledge） | null，无本UID demo claims | 不变；未新增选集/claims/evidence/collector assessment，未晋升trusted |

剩余状态：本UID保持unresolved/text partial；下一步只在纯文本图义查询确需时作定向ocr_assessment，不把完美OCR新增为本批门槛。外部normative RFC链接不是本批目标缺页；它的全文并未获取或保留。旧来源被full_text标记不代表原先就完整，新原件与消费验收也不关闭其他UID缺口。

## 文件与生成影响（files / generated impact）

- 手写输入：本UID canonical metadata及当前rights行、专用累计NOTICE、覆盖台账和本批计划/ledger；代码仅已授权五路径，frontmatter追加修复只占其中materializer与integrity tests。
- 原件：source目录19件，不编辑任何源字节；source/LICENSE和PNG也有同commit retrieval。源原生空白/缩进保留，不能用全目录whitespace清洗改变文献。
- 胶囊派生：新document/sidecar、必要manifest/snapshot/README与累计NOTICE。旧root document/selectors和完整历史保持；manifest不计入自己的inventory字节。
- 聚合与演示：调用现有registry/index/audit helper，保持原aggregate timestamp；ODCS未在36 selected里，但index是build输入，故必要重建demo/Wiki身份。最终36 sources、72 claims、72 evidence、135 pages；选集及claims/evidence内容没有变化，151个生成文件是必要快照/build身份/manifest传播（另有2个pipeline源码文件）。无手写Wiki或新增知识。

独立evaluator与内容reader记录的是本阶段有界事实，最终三维审核仍须锁定提交后HEAD/BASE及其当前CI，不能用上述局部P2复审代替。未进入main、未关闭Issue #3/#4、未删除分支或原文、未改保护/权限/历史；其他UID与全库收口继续由唯一work→PR #1→main路径完成。

## 最终验证记录（verification）

统一使用既有Python3.12.13（与CI匹配）；不安装新依赖。

| 实际检查 | 当前结果 |
| --- | --- |
| make test PYTHON=/tmp/llm-wiki-ci-312-260916/bin/python | 183 tests PASS；包括78 materialization与17excerpt tests |
| 默认strict真实ODCS replay | 修正后generic→one全27文件稳定；body质量接受并规范序列化后再重放仍稳定；fetch/prepare调用0 |
| make demo（同PYTHON） | PASS，36来源/72claims/72evidence/135pages；无新选集或知识内容 |
| make validate（同PYTHON） | raw 248 YAML/215metadata、215manifest、docs54、demo/Wiki全部errors0 |
| scripts/validate_materialization_completeness.py | 215metadata/215manifest、3092库存文件、25198 selectors，warnings0/errors0 |
| 本UID公开包和保全 | 独立目标errors0/blocks0；19原件、完整oldmanifest、rootdoc/27selectors及旧NOTICE前缀不变；其余99rights行不变 |
| 全库公开权利复算 | 仍有2个旧package错误（arxiv:2404.16130、arxiv:2502.18864）与64个既有blocks，active99/audited100；不是全库publication PASS，本批未越界改其他UID |
| make reproducibility（同PYTHON） | committed_tree_replay、full_demo_replay、compiler_only_replay、read_only_validation四阶段各169文件逐字节一致 |
| scripts/audit_non_repo_coverage.py | PASS；215=131+84，frontmatter与实际summary一致；original complete30/text complete6/partial44/unresolved125，不将本批结论升级为全库完成 |
| 准确HEAD/BASE CI与独立三维审核 | 提交后单独验证并在PR记录；当前不预写PASS或merge |

既有PDF检查仍提示可选fontTools的CFF编码warning；未因此改依赖、原稿或提取结果。完整验证保留所有错误与退出码；显示层只过滤重复的该条warning前缀，并启用pipefail，不把过滤当作修复或略过门控。原件及其派生保留上游空白，diff --check仅对手写代码/计划等可控文本执行，不对原稿做格式清洗。

台账机械比较确认其余130项原始块/对象、131知识状态与完整旧execution不变。主线另将顶层scope/interpretation中PR17专属说明显式保留为historical_p3_w3c_html_01字段，并补当前ODCS说明，避免旧“本批七W3C”被误当作当前范围；未改其他UID判断或历史字符串。最终review/CI/merge事实由PR记录锚定准确提交，不能为把结果写进本提交而预填自指SHA或伪造完成。
