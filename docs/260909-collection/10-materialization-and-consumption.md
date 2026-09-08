# Materialization and Source-Specific Consumption

## Why this layer exists

A source record is not automatically consumable. Different source families expose different units of meaning, version semantics, selectors, rights constraints, and failure modes.

Examples:

- arXiv is best consumed from a versioned TeX source tree;
- a PDF needs page, region, table, and figure selectors;
- a GitHub repository is a mutable software system rather than a linear document;
- a blog needs a time-stamped HTML snapshot and paragraph selectors;
- a standard needs an exact edition and normative-section identity;
- a dataset needs release, split, row/field identity, checksum, and license;
- a retraction is a change event that must propagate through dependencies.

The repository therefore separates four layers:

```text
raw_data/              discovery metadata and provenance
source_registry/       normalized identity and adapter selection
materialized_sources/  frozen source-specific artifacts
knowledge/ and wiki/   future claims, evidence, pages, and consumer views
```

## Source registry

`source_registry/registry.yaml` is generated from every `raw_data/**/metadata.yaml` record. Each entry states:

- stable `uid` and canonical identity;
- verification and collection priority;
- metadata path;
- selected consumption adapter;
- whether semanticization is required;
- current materialization state and manifest path.

`registry.jsonl` provides the same information one source per line.

## Adapter contract

The machine-readable catalog is `raw_data/collections/source_consumption_adapters.yaml`. Every adapter must:

1. freeze a source revision;
2. retain retrieval time, hash, and rights state;
3. produce stable selectors;
4. report extraction loss and omitted content;
5. keep evidence separate from summaries;
6. be idempotent for the same revision and configuration;
7. expose dependency information for update, removal, or retraction propagation.

## arXiv materialization

The `arxiv_latex` adapter downloads a source bundle, records its archive hash, safely extracts text-bearing files, detects a root TeX candidate, and creates:

```text
materialized_sources/arxiv/<id>/
├── manifest.yaml
├── SOURCE_MAP.md
├── files.jsonl
├── selectors.jsonl
├── source/
└── normalized/main.tex
```

The archive is hashed but not retained. Binary figures are omitted from the first text-oriented pass and listed in the manifest. PDF materialization remains the fallback for visual and layout evidence.

## GitHub repository materialization

A mutable repository URL must not be passed directly to a knowledge compiler. The `github_repo_wiki` adapter freezes one commit and constructs:

```text
materialized_sources/github/<owner>--<repo>/
├── manifest.yaml
├── evidence/
│   ├── files.jsonl
│   ├── excerpts.jsonl
│   └── excerpts/
└── wiki/
    ├── index.md
    ├── overview.md
    ├── architecture.md
    └── interfaces-and-operations.md
```

The complete repository is not copied. The file index preserves paths and blob SHAs. Selected documentation and manifest excerpts receive `repo://...#Lx-Ly` selectors. Candidate pages organize the evidence, but remain in review state.

This deterministic capsule does not prove runtime behavior, build success, or agreement between README and implementation. A later repo-wiki pass should add symbol graphs, call relations, tests, releases, issues, paper-to-code mappings, and execution evidence.

## Legacy metadata migration

`scripts/materialize_pipeline.py` first adds missing common-schema fields without overwriting source-specific fields. Structurally migrated records receive `verification.state: pending`, not a false verified state. Unknown values remain unknown.

## Validation boundary

`scripts/validate_materialized.py` checks hashes, selector targets, required capsule files, wiki frontmatter schema, unique registry identities, and local evidence references.

Passing proves structural integrity. It does not prove a scientific claim or repository runtime behavior.

## Initial batch

The first materialization batch covers:

- Gödel Machines, DGM, AI Scientist, STORM, A-MEM, and Zep from arXiv;
- DGM, AI Scientist, Graphiti, sage-wiki, LinkML, and OpenKB from GitHub.

This spans RSI, Auto Research, knowledge evolution, ontology/schema, and compiled-wiki implementations while remaining small enough to inspect.
