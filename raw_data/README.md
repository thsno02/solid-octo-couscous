
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
9. **ontology, schema, mapping, identity and operational semantic layers**,
10. **LLM Wiki, long-form knowledge compilation and collaborative editorial governance**,
11. scientific provenance, reproducibility, experiment orchestration and knowledge promotion,
12. governance of evolving agents: objective stability, evaluator reliability, permissions, rollback, provenance, replication, mesa-optimization, power-seeking and oversight.

### Why auto research is first-class

Auto research is not treated as a downstream application. It is a concrete self-evolution loop in a domain where the evolving object is knowledge itself:

`prior knowledge -> research question -> hypothesis -> critique/selection -> experiment -> evidence -> claim revision -> verified knowledge write-back -> next research question`

The collection therefore tracks both systems that *do research* and systems that make research cumulative across time. Shared research memory, world models, preprint/repository write-back, contradiction detection, replication, provenance, and generation of the next problem are core mechanisms of knowledge evolution.

For a cross-source taxonomy and priority list, see `collections/auto_research.yaml`.

### Why ontology is first-class

Knowledge cannot evolve safely when its organizing model is implicit. The collection therefore separates and tracks:

- terminology, taxonomies and vocabularies,
- formal conceptual ontologies,
- structural schemas and executable constraints,
- mappings and physical source bindings,
- entities, claims, observations, evidence and uncertainty,
- temporal, contextual and causal semantics,
- actions, processes and decisions,
- policy, permissions and privacy,
- semantic versioning, migration, review, impact analysis and rollback.

Palantir Foundry's Ontology is treated as an important **operational ontology** pattern: domain objects and links are connected to live data, actions, functions, applications, security and decision lineage. It is broader than OWL and should not be treated as a replacement name for classical ontology. An open architecture will generally compose several standards and systems rather than depend on one universal format.

See `ontology/README.md`, `collections/ontology_knowledge_architecture.yaml`, and `audits/ontology_knowledge_gap_2026-09-09.yaml`.

### Why LLM Wiki is first-class

LLM Wiki is treated as a distinct knowledge-organization and maintenance paradigm, not as ordinary RAG or automatic Markdown generation.

The intended architecture is:

`immutable source -> normalized source -> atomic claim/evidence -> ontology and identity -> compiled wiki page -> index/context pack -> governed consumption`

The wiki is a persistent, human- and agent-readable **derived projection**. It organizes and synthesizes knowledge, while claim/evidence records retain epistemic authority. Generated page changes are proposals; they require deterministic validation, evidence checks, review, admission, versioning, and rollback.

The collection combines:

- the compiled-wiki pattern: raw sources, wiki, schema, ingest/query/lint;
- STORM/Co-STORM-style perspective discovery and outline-first research;
- Wikipedia-style verifiability, neutrality, no-original-research, due weight, discussion and consensus;
- Wikidata/Wikibase-style statements, qualifiers, references, ranks, unknown/no-value and deprecation;
- factuality, citation and contradiction evaluation;
- representative open implementations and wiki infrastructure.

See `collections/llm_wiki.yaml`, `audits/llm_wiki_gap_2026-09-09.yaml`, `schemas/wiki_page.schema.yaml`, `schemas/wiki_change.schema.yaml`, and the top-level `docs/llm-wiki/` documentation suite.

### Why GitHub implementations are first-class

Papers describe mechanisms; open implementations show which mechanisms survive contact with engineering constraints. The `githubs/` collection tracks implementations that expose at least one meaningful evolution substrate: mutation/optimization, persistent learning, autonomous research, incremental knowledge maintenance, evidence-based evaluation, ontology engineering, wiki compilation, provenance, versioning, experiment orchestration or governance/verification.

Generic agent orchestration alone is not enough for inclusion. Repository source is **not vendored** here; each project is represented by a small metadata YAML containing provenance, license state, related papers, mechanisms, relevance, and governance notes.

For the categorized project maps and priorities, see `collections/github_projects.yaml`, `collections/ontology_projects.yaml`, and `collections/llm_wiki.yaml`.

## Coverage and auditability

Collection volume is not treated as coverage. Coverage is evaluated across:

- the object being evolved: weights, code, prompts, workflows, memory, graphs, claims, hypotheses, experiments, evaluators, schemas, mappings, wiki pages and organizations;
- the evolution loop: variation, evaluation, selection, retention, recombination, environment generation, write-back and rollback;
- the research lifecycle: literature, hypothesis, design, execution, analysis, review, replication, publication, promotion and retraction;
- the semantic lifecycle: terminology, modeling, validation, mapping, binding, migration, deprecation and semantic impact;
- the wiki lifecycle: source acquisition, claim extraction, page planning, compilation, citation, admission, release, consumption, lint and repair;
- source type: primary papers, code, datasets, benchmarks, standards, industry methodology, experiment traces, negative results and incidents;
- governance: provenance, temporal validity, contradiction handling, uncertainty, permissions, evaluator independence, replication and rollback.

Current audit artifacts:

- `audits/coverage_audit_2026-09-09.yaml` — general findings, scorecard, risks and acceptance metrics;
- `audits/ontology_knowledge_gap_2026-09-09.yaml` — ontology and knowledge-architecture audit;
- `audits/llm_wiki_gap_2026-09-09.yaml` — LLM Wiki coverage and construction audit;
- `collections/coverage_matrix.yaml` — general cross-domain coverage matrix;
- `collections/ontology_coverage_matrix.yaml` — ontology-specific coverage matrix;
- `collections/llm_wiki.yaml` — LLM Wiki taxonomy, lifecycle, quality dimensions and implementation map;
- `collections/backfill_plan.yaml` — staged execution plan and collection cadence;
- `schemas/item.schema.yaml` — common source metadata contract;
- `schemas/knowledge_model.schema.yaml` — proposed executable knowledge-object contract;
- `schemas/wiki_page.schema.yaml` — compiled wiki page contract;
- `schemas/wiki_change.schema.yaml` — proposed wiki change, review and rollback contract;
- `quarantine/unverified_items.yaml` — records retained for lineage but blocked from trusted promotion;
- `manifests/*.yaml` — additive manifests preserving execution history.

A topic is not considered fully covered by a paper alone. Engineering-relevant topics should have conceptual primary sources plus implementations and evaluation artifacts. Generated research output or wiki prose is never automatically promoted to trusted knowledge.

## Layout

- `arxiv/<paper-title>/` — arXiv papers. Prefer unpacked TeX source when available; keep source metadata next to it.
- `biorxiv/<paper-title>/` — bioRxiv preprints and provenance metadata.
- `journal/<paper-title>/` — peer-reviewed journal articles that are important primary sources and not primarily represented by arXiv.
- `paper/<paper-title>/` — other foundational papers/book chapters not primarily distributed through arXiv.
- `standard/<standard-title>/` — standards, vocabularies and ontologies relevant to semantics, identity, mapping, provenance and governance.
- `methodology/<method-title>/` — modeling, editorial and knowledge-engineering methodologies.
- `industry/<method-or-product-title>/` — industry operational patterns and official documentation.
- `ontology/` — collection-level architecture and modeling guidance.
- `blog/<article-title>/` — public blog/article metadata, canonical URL, and research notes/summary.
- `githubs/<owner>--<repo>/metadata.yaml` — open-source/source-available implementation metadata only; repository contents are not copied.
- `dataset/<dataset-title>/` — versioned dataset metadata; planned as a first-class source type.
- `benchmark/<benchmark-title>/` — benchmark definition, task/version and evaluation protocol; planned as a first-class source type.
- `incident/<incident-title>/` — failures, unsafe behavior, failed replications and postmortems; planned as a first-class source type.
- `x/<post-or-thread-title>/` — public post/thread metadata and canonical URL when relevant.
- `collections/<topic>.yaml` — cross-source topic maps used for coverage, priority, deduplication and scheduled collection.
- `manifests/<batch>.yaml` — additive collection batches that preserve execution history.
- `audits/<audit>.yaml` — point-in-time integrity and coverage reviews.
- `schemas/<schema>.yaml` — validation contracts for metadata and knowledge objects.
- `quarantine/<list>.yaml` — unresolved records retained for provenance but excluded from trusted promotion.

Each item should include a `metadata.yaml` with stable `uid`, canonical identifier, verification state, dates, authors/maintainers, source URL, version/snapshot fields, rights, topic classification, linkages and collection rationale. Ontology/schema records should additionally declare model kind, world assumption, constraint/inference capabilities, mappings and migration status where known. Unknown values must remain `null` or explicitly pending; they must never be invented.

For arXiv, `source_archive_url` points to `/src/<id>` and is the preferred acquisition target because it exposes the original TeX bundle. The current GitHub connector writes UTF-8 text but cannot directly ingest gzip/tar binary source archives, so metadata records preserve the exact source archive URL for a downloader/materializer stage.

## Trust policy for evolving research knowledge

A generated paper, report, answer or wiki page is evidence-bearing output, **not automatically trusted knowledge**. Promotion into a durable knowledge layer must preserve:

- stable identity and entity merge/split lineage,
- ontology/schema/mapping version and semantic change lineage,
- claim and hypothesis lineage,
- source and experimental provenance,
- assertion kind: observation, assertion, inference, prediction, decision or action,
- contradictory evidence, uncertainty and negative results,
- code/data/environment/experiment traces where available,
- replication or independent verification status,
- evaluator/reviewer identity, independence and protocol,
- confidence, temporal validity and status changes over time,
- page and claim dependency lineage,
- authorization for write, merge, supersede, retract and rollback.

Schema or SHACL conformance, cryptographic authenticity, verifiability, editorial inclusion and factual truth are separate checks. This distinction is critical because recursive research and wiki systems consume their own prior outputs; without explicit semantics, provenance, independent verification and rollback, the loop can compound conceptual error as easily as it compounds capability.
