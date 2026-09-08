# Documentation

This directory explains how the repository was collected, materialized, governed, and converted into durable knowledge.

## Entry points

- [`260909-collection/`](260909-collection/README.md) — the 2026-09-09 collection snapshot: scope, coverage, omissions, schemas, source-specific materialization, validation, and handoff rules.
- [`llm-wiki/`](llm-wiki/README.md) — how frozen source revisions become claims, pages, indexes, context packs, and governed wiki releases.

## Layer model

```text
raw_data/              source metadata and provenance
source_registry/       normalized source identity and adapter selection
materialized_sources/  frozen, addressable source artifacts
knowledge/             future atomic claims, evidence, identity and contradictions
wiki/                  future reviewed knowledge views
```

These layers must not be silently collapsed. A URL is not materialization, a semantic capsule is not independent evidence, and a wiki page is not the sole truth record.

## Naming

`260909` means the snapshot date **2026-09-09**. It is not a claim that the collection is complete or permanently current. Later batches should preserve this snapshot and add new dated documentation rather than rewriting history.
