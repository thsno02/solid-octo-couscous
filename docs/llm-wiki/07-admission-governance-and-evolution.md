
# Admission, Governance, and Evolution

## Separation of powers

Recommended roles:

- **Collector** — discovers and registers sources;
- **Parser** — converts source formats;
- **Extractor** — proposes claims and entities;
- **Librarian** — plans pages and links;
- **Writer** — drafts page changes;
- **Linter** — runs structural and semantic checks;
- **Reviewer** — evaluates evidence and presentation;
- **Owner** — approves high-impact changes;
- **Publisher** — merges approved changes;
- **Auditor** — samples released knowledge and investigates incidents.

One agent may perform several low-risk roles, but high-risk generation, evaluation, and publication should not be controlled by one unobserved process.

## Permission model

Actions should be independently authorized:

```text
read source
propose claim
propose entity merge
propose page edit
approve claim
approve page
merge page
promote claim
supersede claim
retract claim
change ontology
change policy
execute operational action
rollback release
```

## Admission matrix

| Object | Candidate gate | Trusted/published gate |
|---|---|---|
| Source | canonical identity and rights | verified revision and hash |
| Claim | source selector and type | evidence, conflict check, review |
| Mapping | candidate match | scope, confidence, justification, review |
| Page | schema and citations | review, policy, evaluation, freshness |
| Change | reproducible diff | approval, rollout, rollback |
| Context pack | deterministic build | pinned revisions and task evaluation |

## Wikipedia lessons

Transfer these practices:

- inline citations;
- burden on the contributor or agent proposing content;
- reliable sources appropriate to the claim;
- neutral presentation when sources disagree;
- no original research or unsupported synthesis;
- due weight;
- public discussion and review;
- verifiability does not force inclusion;
- revision and rollback history.

Do not copy Wikipedia's exact social process blindly. This repository has a smaller community and must encode roles and risk levels explicitly.

## Wikidata lessons

A claim-like statement benefits from:

- qualifiers;
- references;
- rank or applicability status;
- explicit unknown versus no-value;
- deprecation without deletion;
- collaborative property constraints.

A rank is not a probability. It indicates preferred, normal, or deprecated applicability under a modeling convention.

## Change classes

- editorial-only;
- structural;
- evidence-strengthening;
- claim-changing;
- identity-changing;
- ontology-changing;
- policy-changing;
- action-capability-changing.

Review intensity increases down the list.

## Wiki evolution loop

```text
variation:
  new source, claim, page, link, outline, or schema proposal

evaluation:
  deterministic checks, evidence checks, task tests, reviewers

selection:
  approve, contest, defer, reject, quarantine

retention:
  revisions, claims, sources, discussions, build artifacts

recombination:
  cross-page synthesis, comparison, map, context pack

environment generation:
  new questions, gaps, lint tasks, benchmark cases

meta-evolution:
  improve prompts, schemas, evaluators, routing, and policy
```

Meta-evolution must not bypass governance. A proposed change to the admission policy cannot approve itself.

## Retraction

Retraction is not deletion. It creates a durable state transition, records cause and authority, downgrades dependent claims, rebuilds pages, and retains historical views.

## Consensus and dissent

Review outcomes may be:

- consensus approve;
- consensus reject;
- provisional;
- contested;
- owner decision with recorded dissent;
- unresolved.

A page can represent disagreement even when the merge decision is clear.
