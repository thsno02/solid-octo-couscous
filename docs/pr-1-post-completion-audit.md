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
**Status:** unresolved; requires an explicit repository decision

The rights audit reports an active full-text set for which public redistribution is blocked. The fail-closed validator is correct: it returns failure unless every active full-text capsule has an explicit audited `allow` decision.

However, the affected files already exist on a public GitHub work branch. A later deletion commit does not remove them from Git history. Therefore the safe options must be decided **before merging PR #1**:

1. rewrite the work branch so rights-blocked source bodies never enter the merge history;
2. replace PR #1 with a sanitized branch that keeps metadata, hashes, selectors and permitted excerpts only;
3. obtain and record explicit redistribution permission for each retained full-text revision;
4. move restricted bodies to a controlled object store and keep only stable references in Git.

Merging first and deleting later is not an equivalent remediation.

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
**Status:** automated publication removed; durable private acquisition remains future work

The old scheduled workflow coupled acquisition with a rights gate and an automatic commit. The follow-up replaces it with manual, read-only acquisition: no schedule, commit, push or artifact upload. It only diagnoses acquisition/build/validation in an ephemeral runner. The publication-rights validator is unchanged; there is no longer an automatic publishing path to gate.

The next version should separate two lanes:

```text
acquisition lane
  fetch → freeze → hash → private/quarantined artifact → materialization report

publication lane
  rights decision → evidence policy → candidate diff → PR → review → merge
```

A failed publication gate should not erase the acquisition result, and a successful acquisition should never imply permission to publish.

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

PR #1 is technically suitable as a **candidate pipeline implementation**, subject to the fixes in the follow-up audit PR. It should not be merged with rights-blocked full-text bodies still present in its merge history.

Recommended decision sequence:

1. merge the follow-up audit PR into the PR #1 work branch;
2. confirm the single `CI` / `Quality gate` passes on the new parent PR head, including committed-tree replay;
3. choose and execute the full-text storage/rights remediation;
4. enable branch protection and required checks;
5. obtain a human review of a representative Wiki sample;
6. only then mark PR #1 ready for review and merge.

## Follow-up acceptance criteria

The immediate audit-fix PR is complete when:

- stale committed generated artifacts cause CI failure;
- the Wiki verification workflow runs on pull requests and `main`;
- the verification workflow has read-only repository permissions;
- CI never silently publishes regenerated Wiki artifacts;
- unit tests cover the stale-baseline failure mode;
- the unresolved rights, branch-protection and dependency-lock risks remain visible rather than being hidden by a green structural check.
