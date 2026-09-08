# Raw data collection

This directory stores source material for the knowledge-base self-evolution research pipeline.

## Research scope

The collection deliberately covers a wider evolutionary background than knowledge systems alone:

1. recursive self-improvement (RSI) and self-modification,
2. open-ended evolution, quality-diversity, stepping stones and co-evolution,
3. continual/lifelong learning and the stability-plasticity problem,
4. model editing, belief revision, truth maintenance and temporal knowledge,
5. meta-learning, self-training, self-reward and evaluator evolution,
6. **automated research / AI scientists / autonomous scientific discovery**,
7. automated agent/workflow design and algorithm discovery,
8. knowledge/memory/graph self-evolution,
9. scientific provenance, reproducibility, experiment orchestration and knowledge promotion,
10. governance of evolving agents: objective stability, evaluator reliability, permissions, rollback, provenance, replication, mesa-optimization, power-seeking and oversight.

### Why auto research is first-class

Auto research is not treated as a downstream application. It is a concrete self-evolution loop in a domain where the evolving object is knowledge itself:

`prior knowledge -> research question -> hypothesis -> critique/selection -> experiment -> evidence -> claim revision -> verified knowledge write-back -> next research question`

The collection therefore tracks both systems that *do research* and systems that make research cumulative across time. Shared research memory, world models, preprint/repository write-back, contradiction detection, replication, provenance, and generation of the next problem are core mechanisms of knowledge evolution.

For a cross-source taxonomy and priority list, see `collections/auto_research.yaml`.

### Why GitHub implementations are first-class

Papers describe mechanisms; open implementations show which mechanisms survive contact with engineering constraints. The `githubs/` collection tracks implementations that expose at least one meaningful evolution substrate: mutation/optimization, persistent learning, autonomous research, incremental knowledge maintenance, evidence-based evaluation, provenance, versioning, experiment orchestration or governance/verification.

Generic agent orchestration alone is not enough for inclusion. Repository source is **not vendored** here; each project is represented by a small metadata YAML containing provenance, license state, related papers, mechanisms, relevance, and governance notes.

For the categorized project map and priorities, see `collections/github_projects.yaml`.

## Coverage and auditability

Collection volume is not treated as coverage. Coverage is evaluated across:

- the object being evolved: weights, code, prompts, workflows, memory, graphs, claims, hypotheses, experiments, evaluators and organizations;
- the evolution loop: variation, evaluation, selection, retention, recombination, environment generation, write-back and rollback;
- the research lifecycle: literature, hypothesis, design, execution, analysis, review, replication, publication, promotion and retraction;
- source type: primary papers, code, datasets, benchmarks, standards, experiment traces, negative results and incidents;
- governance: provenance, temporal validity, contradiction handling, uncertainty, permissions, evaluator independence, replication and rollback.

Current audit artifacts:

- `audits/coverage_audit_2026-09-09.yaml` — findings, scorecard, risks, executed remediation and acceptance metrics;
- `collections/coverage_matrix.yaml` — machine-readable cross-domain coverage matrix;
- `collections/backfill_plan.yaml` — staged execution plan and collection cadence;
- `schemas/item.schema.yaml` — common metadata contract;
- `quarantine/unverified_items.yaml` — records retained for lineage but blocked from trusted promotion;
- `manifests/coverage_backfill_2026-09-09.yaml` — additive manifest for the current remediation batch.

A topic is not considered fully covered by a paper alone. Engineering-relevant topics should have conceptual primary sources plus implementations and evaluation artifacts. Generated research output is never automatically promoted to trusted knowledge.

## Layout

- `arxiv/<paper-title>/` — arXiv papers. Prefer unpacked TeX source when available; keep source metadata next to it.
- `biorxiv/<paper-title>/` — bioRxiv preprints and provenance metadata.
- `journal/<paper-title>/` — peer-reviewed journal articles that are important primary sources and not primarily represented by arXiv.
- `paper/<paper-title>/` — other foundational papers/book chapters not primarily distributed through arXiv.
- `standard/<standard-title>/` — official standards and ontologies relevant to provenance, identity, interoperability and governance.
- `blog/<article-title>/` — public blog/article metadata, canonical URL, and research notes/summary.
- `githubs/<owner>--<repo>/metadata.yaml` — open-source/source-available implementation metadata only; repository contents are not copied.
- `dataset/<dataset-title>/` — versioned dataset metadata; planned as a first-class source type.
- `benchmark/<benchmark-title>/` — benchmark definition, task/version and evaluation protocol; planned as a first-class source type.
- `incident/<incident-title>/` — failures, unsafe behavior, failed replications and postmortems; planned as a first-class source type.
- `x/<post-or-thread-title>/` — public post/thread metadata and canonical URL when relevant.
- `collections/<topic>.yaml` — cross-source topic maps used for coverage, priority, deduplication and scheduled collection.
- `manifests/<batch>.yaml` — additive collection batches that preserve execution history.
- `audits/<audit>.yaml` — point-in-time integrity and coverage reviews.
- `schemas/<schema>.yaml` — validation contracts for metadata migration.
- `quarantine/<list>.yaml` — unresolved records retained for provenance but excluded from trusted promotion.

Each item should include a `metadata.yaml` with stable `uid`, canonical identifier, verification state, dates, authors/maintainers, source URL, version/snapshot fields, rights, topic classification, linkages and collection rationale. Unknown values must remain `null` or explicitly pending; they must never be invented.

For arXiv, `source_archive_url` points to `/src/<id>` and is the preferred acquisition target because it exposes the original TeX bundle. The current GitHub connector writes UTF-8 text but cannot directly ingest gzip/tar binary source archives, so metadata records preserve the exact source archive URL for a downloader/materializer stage.

## Trust policy for evolving research knowledge

A generated paper/report is evidence-bearing research output, **not automatically trusted knowledge**. Promotion into a durable knowledge layer must preserve:

- claim and hypothesis lineage,
- source and experimental provenance,
- contradictory evidence and negative results,
- code/data/environment/experiment traces where available,
- replication or independent verification status,
- evaluator/reviewer identity, independence and protocol,
- confidence, temporal validity and status changes over time,
- authorization for write, merge, supersede, retract and rollback.

This distinction is critical because recursive research systems consume their own prior outputs; without provenance, independent verification and rollback, the loop can compound error as easily as it compounds capability.
