# Documentation

This directory explains how the repository was collected, materialized, governed, audited, and converted into durable knowledge.

## Entry points

- [`260909-collection/`](260909-collection/README.md) — the 2026-09-09 collection snapshot: scope, coverage, omissions, schemas, source-specific materialization, validation, and handoff rules.
- [`llm-wiki/`](llm-wiki/README.md) — how frozen source revisions become claims, pages, indexes, context packs, and governed wiki releases.
- [`pr-1-post-completion-audit.md`](pr-1-post-completion-audit.md) — post-completion audit of the v0 materialization/meta-KB/LLM Wiki pull request, including fixed defects and remaining merge gates.
- [`materialization-rights-audit.md`](materialization-rights-audit.md) — item-level publication-rights review for locally stored full-text material.
- [`pr-1-wiki-review.md`](pr-1-wiki-review.md) — representative agent editorial review of the candidate Wiki; this is not a human admission decision.

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
