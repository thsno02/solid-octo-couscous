
# Collection Workflow and CI

## Collector workflow

```text
discover
→ canonicalize
→ deduplicate
→ verify
→ classify
→ link
→ write metadata
→ update additive manifest
→ update topic collection
→ validate
→ review
→ merge
→ schedule refresh
```

## Discovery

Discovery may use:

- arXiv and preprint queries;
- citation and related-work expansion;
- official lab and researcher feeds;
- GitHub organization and repository searches;
- standards bodies;
- benchmark and dataset registries;
- retraction and incident sources.

Discovery sources are leads. Canonical primary sources decide what is written.

## Deduplication keys

- arXiv: normalized work ID;
- journal: DOI when available;
- GitHub: redirect-resolved lower-case owner/repository;
- standard: issuing body plus standard identifier;
- other sources: stable canonical URL plus source-native identifier.

## Write policy

A collector writes:

1. `metadata.yaml`;
2. one additive manifest entry;
3. one or more topic-collection references;
4. quarantine entry when unresolved.

It does not silently rewrite old snapshots.

## Current validation

`./scripts/validate_raw_data.py` checks:

- YAML syntax;
- schema conformance for migrated records;
- duplicate canonical IDs;
- broken references from `raw_data/index.yaml`;
- broken additive-manifest item paths.

`./scripts/validate_docs.py` checks:

- required documentation entry points;
- relative Markdown links;
- required headings and implementation-plan anchors;
- example YAML syntax under `docs/`.

GitHub Actions runs both validators when `raw_data/`, `docs/`, or validator files change.

## Current migration debt

The 2026-09-09 validation snapshot reports a non-blocking legacy backlog. Legacy warnings are temporary. The acceptance target is zero warning-only metadata records.

## Scheduled refresh

Recommended cadence:

- weekly: frontier arXiv, research blogs, LLM Wiki projects;
- monthly: GitHub ownership, archive state, default branch, release, head commit, license;
- quarterly: standards, ontology revisions, coverage audits;
- event-driven: withdrawal, retraction, repository transfer, major benchmark revision.

Every refresh must produce a change report rather than only a new “latest” value.
