
# Build Pipeline

This is the primary implementation specification.

## Pipeline contract

```text
input:
  selected source revisions
  collection scope
  ontology/schema versions
  identity registry
  compilation policy
  model/prompt versions

output:
  normalized source artifacts
  candidate claim/evidence changes
  candidate wiki page changes
  validation reports
  review queue
  build manifest
  dependency graph
  releasable or rejected change set
```

The pipeline is incremental, idempotent where possible, dependency-aware, and proposal-based.

---

## Stage 0 — trigger and scope

### Triggers

- new source;
- updated source revision;
- source removal or retraction;
- scheduled refresh;
- query answer proposed for filing;
- lint finding;
- ontology/schema change;
- entity merge or split;
- manual editorial request.

### Output

A build request with:

- trigger type and reference;
- source set;
- target collections;
- priority and risk class;
- allowed operations;
- budget;
- required reviewers;
- expected evaluation suite.

### Gate

Reject an unbounded “read everything and improve the wiki” request. Every build must declare scope and maximum affected surface.

---

## Stage 1 — acquire and freeze source

### Actions

1. Resolve canonical identifier.
2. Select a source revision.
3. Download or snapshot legal content.
4. Compute content hash.
5. Store rights and access state.
6. Record retrieval time.
7. Keep the source immutable.

### Output

`SourceRevision` and a build-local read-only copy.

### Failure handling

- unresolved identity → quarantine;
- unknown license → metadata-only unless policy permits processing;
- source unavailable → preserve prior revision and emit freshness warning;
- changed bytes under same revision → integrity incident.

---

## Stage 2 — parse and recover structure

### Actions

- parse TeX, HTML, Markdown, PDF, code, or structured data;
- recover headings, paragraphs, tables, figures, citations, footnotes, and code blocks;
- preserve source selectors;
- identify extraction loss;
- attach parser version and warnings.

### Output

A normalized document tree whose nodes have stable selectors and hashes.

### Gate

No claim extraction from an untraceable flat text dump when the source has recoverable structure.

---

## Stage 3 — source quality, rights, and trust classification

Classify:

- primary versus secondary source;
- peer-reviewed, preprint, official documentation, opinion, or social post;
- independence and conflict of interest;
- recency and revision state;
- domain appropriateness;
- copyright and quotation constraints;
- known retraction or correction status.

This does not decide claim truth. It informs admission and due weight.

---

## Stage 4 — atomic claim and evidence extraction

### Two-pass design

**Pass A: candidate extraction**

Extract:

- entities;
- observations;
- assertions;
- numerical results;
- definitions;
- mechanisms;
- comparisons;
- limitations;
- predictions;
- open questions.

**Pass B: evidence binding**

For every candidate:

- bind exact source selector;
- capture evidence hash;
- preserve qualifiers;
- classify assertion kind;
- record uncertainty and temporal scope;
- reject claims that cannot be linked back to source text.

### Output

Candidate claim/evidence records, never page prose.

### Gate

A claim without a source selector can remain a note or research question; it cannot be promoted as supported knowledge.

---

## Stage 5 — identity and entity resolution

### Actions

- map mentions to canonical entities;
- retain source-local IDs;
- compare aliases and identity criteria;
- create merge or split proposals;
- detect homonyms;
- preserve confidence and justification.

### Policy

High-confidence automatic matching may be allowed only for reversible low-risk aliases. Entity merges with broad downstream impact require review.

### Output

Resolved references plus an identity-change proposal where needed.

---

## Stage 6 — ontology and schema mapping

Map candidate knowledge to:

- entity and relation types;
- page types;
- assertion kinds;
- units and measurement types;
- temporal and contextual properties;
- domain modules.

Unknown concepts create ontology proposals, not ad hoc permanent fields.

### Gate

If a candidate needs a schema change, suspend its promotion until the semantic change process supplies compatibility, migration, impact, and rollback.

---

## Stage 7 — novelty, overlap, and conflict analysis

For each claim:

- find exact duplicates;
- find paraphrases;
- find refinements or narrower scopes;
- find superseding evidence;
- find explicit and implicit contradictions;
- find temporal changes;
- find source dependence or circular citation.

### Output

A relation proposal:

```text
duplicates
supports
refines
contradicts
supersedes
independent_of
derived_from
```

A conflict is not automatically resolved. It may require a debate page or contested claim state.

---

## Stage 8 — page planning and outline generation

Use the current wiki, question frontier, and source bundle to plan:

- pages to create;
- pages to update;
- pages to split or merge;
- section outlines;
- perspectives and comparisons;
- missing evidence;
- navigation links.

For broad topics, use STORM-like perspective discovery:

1. identify distinct stakeholder or research perspectives;
2. generate research questions per perspective;
3. retrieve evidence;
4. build a hierarchical outline;
5. check source and viewpoint coverage;
6. only then draft prose.

### Output

A `PagePlan`, not final Markdown.

---

## Stage 9 — candidate page compilation

Compile sections from approved candidate claims.

Rules:

- cite every factual paragraph;
- use atomic claim references for risky statements;
- separate settled, contested, and speculative content;
- retain limitations and negative evidence;
- avoid copied source prose beyond policy;
- do not cite another generated wiki page as external evidence;
- add typed links;
- preserve human-authored protected regions;
- create a proposed patch against the base page revision.

### Output

Candidate Markdown, frontmatter, typed-link sidecar, and semantic diff.

---

## Stage 10 — deterministic validation

Run without an LLM where possible:

- YAML/frontmatter schema;
- unique IDs;
- valid claim and source references;
- no broken or circular page links;
- no orphan required pages;
- every cited source exists;
- every claim selector resolves;
- no deprecated identifier without redirect;
- source-removal dependencies handled;
- deterministic render;
- no prohibited file or secret;
- no unexpected direct edits to raw sources.

Failure blocks review.

---

## Stage 11 — evidence and semantic evaluation

Run:

### Citation checks

- citation present;
- source selector resolves;
- source entails the claim;
- citation scope matches wording;
- citation is sufficiently complete;
- source is appropriate for the claim.

### Factuality checks

- decompose page into atomic claims;
- compare claim set with explicit references;
- calculate supported, unsupported, disputed, and uncheckable rates.

### Contradiction checks

- internal page consistency;
- cross-page consistency;
- conflict with trusted claims;
- temporal and contextual compatibility;
- source independence.

### Editorial checks

- outline breadth and depth;
- redundancy;
- coherent organization;
- neutral representation;
- due weight;
- no novel synthesis presented as sourced fact;
- clear separation of inference and observation.

### Utility checks

- fixed question set;
- answer correctness;
- citation traceability;
- token and latency cost;
- navigation success;
- task completion with and without wiki.

LLM judges may assist, but deterministic tests, source entailment models, multiple evaluators, and sampled human review must constrain them.

---

## Stage 12 — risk-based review

Assign review depth:

| Risk | Example | Required review |
|---|---|---|
| Low | typo, broken link | automated checks plus sampled review |
| Medium | new explanatory section | independent agent or human review |
| High | disputed claim, entity merge, source retraction | domain owner and evidence review |
| Critical | ontology identity change, action permission, safety claim | multi-party approval and canary |

Reviewers see:

- source delta;
- claim delta;
- page diff;
- semantic diff;
- validation results;
- unresolved conflicts;
- downstream impact;
- rollback plan.

---

## Stage 13 — admission and merge

The decision may:

- approve all;
- approve selected claims or sections;
- publish as contested;
- request revision;
- reject;
- quarantine;
- defer pending evidence.

Merge creates:

- immutable page revision;
- updated claim promotion state;
- change decision record;
- dependency graph update;
- index rebuild request;
- release note.

---

## Stage 14 — indexes, maps, and context packs

Build deterministic products:

- root index;
- maps of content;
- page-type indexes;
- entity and method indexes;
- timeline and debate indexes;
- graph neighborhoods;
- full-text and optional vector indexes;
- task-specific context packs;
- machine-readable change feed.

A context pack contains IDs and revisions, not copied mutable truth without references.

---

## Stage 15 — consumption

Humans browse pages and diffs. Agents:

1. route through an index or map;
2. retrieve a bounded page set;
3. expand to claims and source evidence when necessary;
4. answer with page, claim, and source references;
5. mark uncertainty and as-of time;
6. optionally create a candidate filing proposal.

Query answers remain ephemeral unless explicitly filed through the build pipeline.

---

## Stage 16 — monitoring, lint, and repair

Scheduled lint detects:

- stale source dependencies;
- unsupported claims;
- broken citations;
- contradictions;
- orphan pages;
- duplicated pages or entities;
- overgrown pages;
- missing perspectives;
- deprecated terms;
- failed source refresh;
- policy drift;
- pages unused by any consumer;
- context packs pinned to old revisions.

Repairs are new `WikiChange` proposals.

---

## Idempotency and caching

Cache keys include:

- source content hash;
- parser version;
- schema/ontology version;
- identity registry version;
- prompt/model version;
- task configuration.

A cache hit is valid only when all semantic dependencies match.

---

## Incremental rebuild

When a source changes:

```text
source revision diff
→ affected selectors
→ affected claims
→ affected sections
→ affected pages
→ affected indexes/context packs
```

Do not rebuild the entire wiki unless the dependency graph or schema change requires it.

---

## Minimum viable build

The first working version should support:

1. source registry and checksums;
2. parsed Markdown/TeX;
3. candidate claim/evidence YAML;
4. concept, system, method, and comparison pages;
5. page and change schemas;
6. paragraph citations;
7. deterministic reference validation;
8. manual review;
9. Git merge and rollback;
10. five fixed evaluation questions per collection.

Everything else is an extension.
