
# Source Model and Directory Layout

## Top-level source families

```text
raw_data/
├── arxiv/          # arXiv metadata; TeX source preferred during materialization
├── biorxiv/        # bioRxiv preprints
├── journal/        # peer-reviewed journal sources
├── paper/          # other foundational papers or chapters
├── standard/       # standards, vocabularies, ontologies
├── methodology/    # methods and operating models
├── industry/       # official industry architecture and product methodology
├── blog/           # public researcher or lab articles
├── githubs/        # metadata only; repositories are not vendored
├── dataset/        # planned first-class dataset records
├── benchmark/      # planned benchmark/version records
├── incident/       # planned failures, retractions, postmortems
├── collections/    # topic maps, priorities, and coverage matrices
├── manifests/      # additive batch inventories
├── audits/         # point-in-time integrity and coverage reports
├── schemas/        # validation contracts
├── quarantine/     # unresolved records blocked from trusted promotion
└── index.yaml      # machine-readable root
```

## Item layout

Readable title folders are retained:

```text
raw_data/arxiv/<paper-title>/metadata.yaml
raw_data/githubs/<owner>--<repo>/metadata.yaml
```

Folder names are not identity. `uid` and `canonical_id` are authoritative.

## Why manifests are additive

`raw_data/manifest.yaml` records the original seed. Later work is represented as dated additive manifests rather than rewriting the original batch. This provides:

- auditability;
- reproducibility;
- provenance of collection decisions;
- deterministic deduplication;
- the ability to reconstruct the collection as of a date.

Consumers load the base manifest plus every additive manifest listed in `raw_data/index.yaml`, then deduplicate by canonical identity.

## Raw versus derived

`raw_data/` stores source-level records and eventually source snapshots. It must not contain the future wiki's editorial pages as if they were source evidence.

The intended separation is:

```text
raw source snapshot
→ normalized source record
→ atomic claim/evidence objects
→ compiled wiki pages
→ indexes and consumer context packs
```

A derived page may point to a raw source; it must never masquerade as that source.

## Full-text materialization

For arXiv, the preferred acquisition is `/src/<id>`:

1. resolve canonical identifier and latest selected revision;
2. download the source archive;
3. hash the archive;
4. unpack safely;
5. identify the primary TeX file;
6. retain bibliography and figures;
7. record source revision, retrieval time, content hash, and license;
8. never overwrite older materialized revisions.

Until these steps are complete, the record is metadata-only.
