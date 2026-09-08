
# Reference Architecture

## Logical layers

```text
L0  Raw acquisition
    source files, canonical URLs, revisions, checksums, rights

L1  Normalized source registry
    metadata, source selectors, parsing outputs, provenance

L2  Identity and ontology
    entities, concepts, aliases, mappings, types, constraints

L3  Epistemic graph
    claims, observations, evidence, inference, prediction,
    contradiction, uncertainty, time, review state

L4  Wiki compilation
    page plan, outlines, sections, typed links, summaries, diffs

L5  Wiki release
    published Markdown, maps of content, indexes, timelines, logs

L6  Consumption
    human browsing, search, graph traversal, MCP/API, context packs,
    query answers, reusable agent skills

L7  Maintenance and governance
    lint, staleness, source updates, retractions, review, rollback,
    schema and policy evolution
```

## Recommended physical layout

The first implementation should preserve the existing `raw_data/` and add new generated directories rather than mixing layers:

```text
/
├── raw_data/                   # existing source collection
├── knowledge/
│   ├── entities/
│   ├── claims/
│   ├── evidence/
│   ├── contradictions/
│   ├── mappings/
│   └── changes/
├── wiki/
│   ├── maps/
│   ├── concepts/
│   ├── entities/
│   ├── methods/
│   ├── systems/
│   ├── comparisons/
│   ├── timelines/
│   ├── debates/
│   ├── gaps/
│   ├── evaluations/
│   └── sources/
├── builds/
│   └── <build-id>/
│       ├── manifest.yaml
│       ├── dependency-graph.yaml
│       ├── evaluation.yaml
│       └── proposed-changes/
├── context_packs/
├── schemas/
└── logs/
```

`knowledge/`, `wiki/`, `builds/`, and `context_packs/` are future outputs. They are not created as trusted content merely by creating directories.

## Control plane versus data plane

### Data plane

- source snapshots;
- parsed content;
- claims and evidence;
- wiki pages;
- indexes;
- context packs.

### Control plane

- ontology and schemas;
- compilation configuration;
- model and prompt versions;
- permissions;
- admission policies;
- evaluation thresholds;
- reviewer assignments;
- build and rollback manifests.

A model must not be allowed to rewrite its own control-plane rules as part of a normal page compilation job.

## Dependency graph

Every build should record:

```text
source revision
  → parsed segment
  → evidence selector
  → claim
  → page section
  → page
  → index/context pack
  → consuming task or answer
```

This graph enables targeted rebuild, retraction propagation, and impact analysis.

## Build identity

A reproducible build ID should bind:

- selected source revisions and hashes;
- parser versions;
- ontology/schema versions;
- entity registry version;
- model IDs;
- prompts or skills;
- configuration;
- deterministic validator versions;
- build timestamp and code commit.

## Storage choice

Markdown is the human-readable release format. Structured objects may initially be YAML/JSON files committed to Git. Later, an indexed store can be added, but the canonical exported representation must remain deterministic and portable.

## Isolation

Compilation runs should use:

- read-only raw source mounts;
- a temporary candidate workspace;
- no direct write access to published pages;
- restricted network and tool permissions;
- explicit output manifests;
- bounded source and token budgets.
