# PR #1 Post-Completion Audit — 2026-09-16

## Scope

This audit reviews PR #1 at head commit `97cc3716ce336d46e09c86bc127453554271cd27` as an implementation-complete candidate. At audit time, GitHub still reports PR #1 as open and draft; this document therefore evaluates merge readiness rather than assuming that the change is already part of `main`.

The review covered:

- collection and materialization status;
- source → evidence → claim → page traceability;
- deterministic build and validation entry points;
- GitHub Actions lifecycle behavior;
- publication-rights gating;
- candidate/trusted admission boundaries;
- operational risks that are not represented by schema validation alone.

## Executive assessment

The candidate is structurally strong and substantially improved over the earlier state. It has an explicit source registry, source-specific capsules, evidence selectors, candidate claims, typed Wiki pages, review queues, release manifests, rollback metadata, offline tests and deterministic validators.

It is **not yet a trusted knowledge release**. The correct state remains a validated candidate because:

1. no scientific claim has completed independent admission;
2. full-text redistribution is still blocked for the active corpus;
3. the public branch already contains material whose redistribution decision is unresolved;
4. repository settings do not currently enforce required checks or pull-request-only changes;
5. long-term supply-chain reproducibility remains distinct from same-environment byte replay; dependency versions are now fixed, but runner images and action release tags are not immutable.

## Findings

### A-01 — Committed generated artifacts were not part of the reproducibility comparison

**Severity:** high engineering integrity risk  
**Status:** fixed in the follow-up audit PR

The previous replay script performed a first `make demo`, then captured the generated tree, and only compared later builds against that post-build snapshot. If committed Wiki artifacts were stale but still internally valid, the first rebuild could silently replace them and every later comparison would pass.

This matters because pull-request CI used that replay as evidence that generated outputs matched their declared inputs. Repeated post-build equality proves idempotence, but it does not prove that the checked-in tree is current.

The follow-up changes the sequence to:

```text
snapshot committed generated tree
→ make demo
→ compare rebuilt tree with committed tree
→ repeat full demo
→ repeat compiler-only build
→ run read-only validators
```

Any added, removed or byte-changed generated file now fails at `committed_tree_replay` before later replay checks can mask it.

### A-02 — The Wiki workflow was tied to the temporary work branch and self-committed changes

**Severity:** high lifecycle/governance risk  
**Status:** fixed in the follow-up audit PR

The prior workflow only listened to:

```text
work/v0-meta-kb-initialization-demo-260910
```

After PR #1 eventually lands, equivalent changes on `main` would not receive the same Wiki rebuild check. The workflow also had `contents: write` and committed generated artifacts directly back to its branch. That behavior is inconsistent with the repository's proposal → review → merge governance model and makes CI both evaluator and publisher.

The follow-up workflow:

- runs on pull requests;
- uses a single `CI` / `Quality gate` on all PRs, `main` pushes and `merge_group`, without temporary-branch or PR-path filters;
- uses `contents: read`;
- rebuilds and validates without publishing;
- fails when the rebuilt experiment differs from the committed tree.

Generation remains a developer or proposal-branch responsibility; CI becomes an independent verifier.

### A-03 — Full-text publication rights remain unresolved

**Severity:** merge-blocking governance and legal risk  
**Status:** 全文留存于当前 GitHub repo 的方向已确定；逐项许可履约尚未完成

The rights audit reports an active full-text set for which public redistribution is blocked. The fail-closed validator is correct: it returns failure unless every active full-text capsule has an explicit audited `allow` decision.

用户已明确：正文与预处理产物必须持久保存在当前 GitHub repo，以便远程继续工作（remote continuation）。因此执行路径是为保留的每项全文版本取得并记录适用许可，落实署名、原声明、修改说明及第三方材料条件；不能用删除正文、改写历史、替换为链接或迁移存储作为替代交付。

这些文件已存在公开工作分支，并不意味着许可问题自动消失。尚未核实的项目保持阻塞，在逐项完成许可履约之前不合并 PR #1；也不把用户的存储选择解释为第三方授权。

Relevant records:

- [`materialization-rights-audit.md`](materialization-rights-audit.md)
- `raw_data/audits/materialization_rights_review.yaml`
- `scripts/validate_publication_rights.py`

### A-04 — `main` does not enforce the checks represented by this repository

**Severity:** high governance risk  
**Status:** unresolved; repository-setting change required

At audit time, `main` is not protected and required status checks are disabled. This means:

- a failing rights check does not technically prevent a merge;
- deterministic validation is advisory rather than enforced;
- direct pushes can bypass the proposal/review path;
- self-committing workflows can modify the branch without an independent approval boundary.

Recommended repository settings:

```text
require pull request before merging
require Quality gate (workflow: CI; select the actual emitted check)
require branch to be up to date
block force pushes
block direct pushes except narrowly scoped automation
require review for workflow and governance changes
```

This cannot be fully solved by a repository file alone.

### A-05 — Scheduled acquisition and public publication are still coupled

**Severity:** medium/high operational risk  
**Status:** acquisition now proposes a repository update; direct-to-base publication remains removed

The old scheduled workflow coupled acquisition with a rights gate and a direct commit to its base branch. The first CI repair temporarily reduced it to ephemeral diagnostics. The owner subsequently clarified that full text must persist in this GitHub repository for remote continuation. The manual producer therefore validates the generated candidate and its exact-revision rights before pushing a new proposal branch and opening a Draft PR. It never pushes directly to base/main or merges itself; the independent CI remains read-only.

The two lanes are now:

```text
acquisition lane
  rights preflight → fetch → preprocess → validate/replay → exact-revision rights gate

publication lane
  repository proposal branch (text + manifests + derived artifacts) → PR → independent CI → review → merge
```

剩余 85 项受阻的全文使生产流程无法上传新批次；四项固定版本 W3C 文字包与一项 arXiv PDF 包已完成声明与署名条件，但不代表端到端上传成功。许可失败不会退回 artifact 发布或直接推送分支。已提交正文留存在 GitHub，远程任务检出相应 commit 继续工作，无需依赖上一个 runner。默认分支启用、Actions 创建 PR 权限及自动化 PR 的 CI 批准要求见[当前操作说明](ci-workflow.md)。

### A-06 — Reproducibility is same-environment, not yet supply-chain reproducibility

**Severity:** medium  
**Status:** dependency drift reduced; immutable supply-chain reproduction not claimed

The follow-up fixes Python to 3.12.13, runner family to ubuntu-24.04, Actions to explicit release tags, and the complete resolved Python dependency set to exact versions in the existing requirements file. Byte-identical replay still does not prove an immutable runner or supply chain.

Optional future high-assurance measures (not required for this minimal CI repair):

- add a fully resolved lock file with hashes;
- record Python implementation/version and installed package versions in the build manifest;
- pin GitHub Actions by immutable commit SHA for high-assurance workflows;
- add a periodic clean-room replay against the recorded environment fingerprint.

### A-07 — Scientific and editorial admission is still intentionally empty

**Severity:** expected candidate limitation  
**Status:** correctly represented

The release preserves `trusted_claims: 0`, and the review queue requires evidence entailment, citation scope, identity, contradiction, neutrality, due weight and freshness checks. This is correct. Structural validation must not be reworded as factual validation.

The first admission batch should remain small and should use independent reviewers or at least reviewer agents that do not share the generator's context and prompts.

**准入范围澄清（Admission scope）：** 原始[准入矩阵](llm-wiki/07-admission-governance-and-evolution.md)将 Page 的 schema/citations 列为 candidate gate，将 review/policy/evaluation/freshness 列为 trusted/published gate。因此，人工编辑审核是可信晋升或正式发布前的门槛，不应被本审计扩大为候选 pipeline 代码 PR 的必需人工批准。当前 review/not_started、candidate、trusted=0 与 rollout=none 均保持不变。Source 的 rights 本来就属于 candidate gate，不能用候选状态豁免公开全文许可。

### A-08 — arXiv 的 PDF 响应被当成 TeX（已修复）

**严重性：** 物化内容完整性缺陷，不能由结构 CI 绿灯豁免
**状态：** 2026-09-16 发现并修复；实际原件与衍生产物已恢复，新增页级回归检查

`arxiv:2502.18864` 的 manifest 记录响应为 `application/pdf`、5,885,207 bytes，却由 `arxiv_latex_v2` 标为 `archive_container: single`、`materialized/full_text`。保存的 `source/main.tex` 被本机 `file` 识别为 PDF 1.4，文件大小已变成 10,164,708 bytes；它不是可信的 TeX 原稿。`unpack_arxiv` 的单文件回退与后续文本解码没有区分 PDF，现有清单/重放检查也不验证这种媒体类型错配。

修复前，新增验证器已在实际坏胶囊上报出 `ARXIV_PDF_AS_TEX`。现有生产入口按实际内容区分 PDF、TeX、tar 与 HTML/XML/JSON 错误页，兼容 gzip；首个 e-print 入口返回错误页时继续尝试备用入口，不再将任意响应当成单文件 TeX。

固定 v2 的原始 PDF 与先前 manifest 的响应 revision 一致，157 页原件逐字节保留；用可读文本替换损坏的 TeX/文本衍生文件，生成 155 个页定位器。第 4、20 页为图示页，无可提取文本，明确记录为 `partial/full_text`、`bounded-excerpt`，不虚构 OCR。连续两次用同一真实响应物化，胶囊全部文件字节一致。

校验器核对实际 PDF 页数、页 URI 与页字段、页内 preview，以及文本/无文本/失败三类页的互斥完整覆盖；回归覆盖错误页夹带 TeX 标记、错页定位器、跨页 preview、漏页和 PDF 伪装为 TeX。保留原始 PDF 时，不允许利用文本提取失败或 metadata/excerpt 降级绕过全文许可门。固定 v2 的 CC BY 4.0、51 位作者及完整 NOTICE 已绑定到原件与衍生包；不覆盖使用另一许可的 v1。

范围限于当前 Makefile/workflow 调用的 `materialize_all_sources.py`，不宣称历史脚本全部修复。旧损坏产物可从 Git 历史恢复；未删除作品或改写历史。

## Positive controls confirmed

The audit found the following controls to be materially useful:

- every collected record has a local capsule, even when only metadata is available;
- metadata-only and partial states are represented explicitly;
- source-reported assertions and collector assessments are separated;
- claim and source references are machine-validated;
- pages remain derived views rather than the sole truth record;
- no automatic trusted-claim promotion occurs;
- evidence selectors, hashes and local-file inventories are validated;
- review and release objects are retained separately from Wiki prose;
- rollback is modeled as an explicit release concern rather than an implicit Git assumption.

## Merge recommendation

PR #1 的候选 pipeline 已有结构验证基础，A-08 的物化类型缺陷已修复，但仍须完成许可履约；不能以 CI 绿灯证明全部正文具有公开再分发许可。存在许可阻塞时，不合并 main。

Recommended decision sequence:

1. merge the follow-up audit PR into the PR #1 work branch;
2. confirm the single `CI` / `Quality gate` passes on the new parent PR head, including committed-tree replay;
3. 按已确定的 repo 全文留存要求逐项完成许可履约（rights clearance）；
4. enable branch protection and required checks;
5. review the candidate implementation as a code PR without claiming editorial admission, then mark ready and merge only after its applicable gates are met.

在候选代码合并之后、任何可信晋升或正式知识发布之前，仍须完成相应的独立证据/编辑审核并记录准入决定。此前把 representative human review 放入候选 PR 必需合并顺序，是本审计的过度归类，不是原始仓库规则；此处仅纠正说明，不授予批准，也不更改准入策略或产物状态。

## Follow-up acceptance criteria

The immediate audit-fix PR is complete when:

- stale committed generated artifacts cause CI failure;
- the Wiki verification workflow runs on pull requests and `main`;
- the verification workflow has read-only repository permissions;
- CI never silently publishes regenerated Wiki artifacts;
- unit tests cover the stale-baseline failure mode;
- the unresolved rights, branch-protection and dependency-lock risks remain visible rather than being hidden by a green structural check.
