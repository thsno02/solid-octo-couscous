
# Agent Handoff and Operating Rules

This file is a compact operating contract for future collection agents.

## Before collecting

1. Read `raw_data/index.yaml`.
2. Read the relevant topic collection and latest audit.
3. Search the existing canonical IDs and aliases.
4. Resolve the current primary source.
5. Confirm the current date and record `retrieved_at`.

## While collecting

- Prefer primary sources and official repositories.
- Store metadata, not copied copyrighted bodies, unless reuse rights and acquisition policy permit it.
- Preserve exact source URLs.
- Mark unknown fields as unknown.
- Record why the item matters to knowledge evolution.
- Link the item to papers, code, datasets, benchmarks, standards, and predecessors when verified.
- Do not label a public repository “open source” without license evidence.
- Put unresolved identity, title, date, license, or withdrawal questions in quarantine.
- Treat current popularity as discovery evidence, not scientific evidence.

## Before writing

Check:

```text
canonical identity
duplicate/alias
source type
version
rights
verification state
classification
evolution object
loop role
evidence level
governance risks
collection rationale
```

## Before merging

Run:

```bash
python scripts/validate_raw_data.py
python scripts/validate_docs.py
```

Then inspect the additive manifest and diff.

## Forbidden shortcuts

- no fabricated authors, dates, versions, or licenses;
- no title-based identity;
- no replacing old versions without lineage;
- no page-level citation as a substitute for atomic support where scope is ambiguous;
- no self-citation or derivative-mirror corroboration;
- no direct promotion of generated summaries;
- no destructive deletion of deprecated or retracted records;
- no direct ontology or wiki overwrite by an unreviewed agent.

## Handoff record

A completed batch should state:

- date and collector;
- search scope and seeds;
- items added, updated, quarantined, or rejected;
- exact validation commit and result;
- unresolved questions;
- next recommended batch.
