
# Metadata Schemas and Identifiers

## Source schema

`raw_data/schemas/item.schema.yaml` governs migrated source records.

Required fields:

```yaml
uid:
source_type:
title:
canonical_url:
verification:
classification:
collection:
```

Important optional groups include:

- `canonical_id` and `aliases`;
- `dates`;
- `versioning`;
- `rights`;
- `model_characteristics`;
- `linkage`;
- `evidence`;
- `governance`.

Legacy records are temporarily warning-only. New records must use the migrated schema.

## Knowledge object schema

`raw_data/schemas/knowledge_model.schema.yaml` covers future semantic, epistemic, operational, and lifecycle objects:

- concepts, entity types, properties, constraints, mappings, source bindings;
- entities, claims, observations, evidence, inference, prediction, contradiction;
- actions, processes, decisions, policies, permissions;
- change sets, semantic diffs, migrations, reviews, supersessions, retractions, rollbacks.

## Wiki schemas

This batch adds:

- `raw_data/schemas/wiki_page.schema.yaml`
- `raw_data/schemas/wiki_change.schema.yaml`

A page schema describes a compiled view. A change schema describes a proposed modification and its validation, review, rollout, and rollback.

## Identifier policy

### Internal identity

`uid` is stable inside this repository and includes the source family:

```text
arxiv:2402.14207
github:xoai/sage-wiki
methodology:andrej-karpathy-llm-wiki
wiki-page:open-ended-evolution
wiki-change:2026-09-09T120000Z-abc123
```

### Canonical source identity

Examples:

- arXiv ID without a version suffix as work identity;
- DOI;
- canonical `owner/repository`;
- standard identifier;
- dataset or benchmark ID.

Version belongs in `versioning.source_version`, not in the identity field.

### Alias and redirect policy

Repository transfers, renamed terms, and entity aliases must be retained as lineage. They must not be counted as independent records after canonical resolution.

### Identity versus label

Two labels that look alike are not automatically the same entity. Two differently named entities may be identical. Entity merges and splits require evidence, review, and reversibility.

## Unknown values

Use `null`, `unknown`, `pending`, or `undeclared`. Never invent:

- author names;
- licenses;
- dates;
- versions;
- confidence;
- replication status;
- canonical repository ownership.
