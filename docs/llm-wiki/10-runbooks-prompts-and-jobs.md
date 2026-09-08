
# Runbooks, Prompts, and Jobs

## Job: ingest source

Inputs:

- canonical source ID or URL;
- selected revision;
- target collection;
- risk class.

Steps:

1. canonicalize;
2. acquire and hash;
3. parse;
4. classify source;
5. extract claims;
6. resolve identities;
7. map ontology;
8. analyze novelty/conflict;
9. plan pages;
10. emit change proposal;
11. validate;
12. route to review.

The job is successful only when its build manifest and candidate artifacts exist. A model response alone is not success.

## Job: update source

1. fetch selected new revision;
2. compute source diff;
3. locate affected selectors and claims;
4. classify semantic versus editorial change;
5. regenerate affected sections;
6. run regression questions;
7. publish only approved changes.

## Job: retract or remove source

1. mark source state;
2. freeze retraction evidence;
3. find dependent claims;
4. downgrade or contest them;
5. identify dependent page sections and context packs;
6. propose repairs;
7. review;
8. release and test rollback.

## Job: lint wiki

Deterministic pass:

- schemas;
- links;
- IDs;
- citations;
- dependency graph;
- orphan pages;
- deprecated IDs;
- source availability.

Semantic pass:

- unsupported claims;
- contradictions;
- stale scopes;
- missing perspectives;
- over-association;
- duplicated pages;
- excessive summary compression;
- source bias.

## Job: file query answer

1. classify candidate page type;
2. decompose answer into claims;
3. discard self-citations;
4. resolve external evidence;
5. compare with existing claims/pages;
6. produce a `WikiChange`;
7. apply normal gates.

## Prompt: source analyst

Required output:

```text
source identity
source type and quality
main concepts and entities
atomic claims with selectors
limitations and negative evidence
temporal scope
relationships to existing knowledge
contradictions or refinements
questions raised
```

Do not write final wiki prose.

## Prompt: librarian

Required output:

```text
existing pages to update
new pages to create
page type
outline
claim bundle per section
typed links
missing evidence
split/merge suggestions
risk and review class
```

Do not invent sources.

## Prompt: writer

Constraints:

- use only supplied claim bundles;
- preserve qualifiers and uncertainty;
- cite factual paragraphs;
- distinguish assertion, inference, prediction, and editorial explanation;
- represent conflicts;
- avoid repetitive source-by-source summaries;
- output frontmatter and patch, not direct write.

## Prompt: reviewer

Review:

- claim support;
- scope;
- source appropriateness;
- identity;
- neutrality;
- missing dissent;
- original synthesis;
- stale knowledge;
- downstream impact;
- rollback adequacy.

Return a decision with reasons and unresolved issues.

## Job manifests

Every job records:

- code commit;
- model and prompt version;
- input IDs and revisions;
- configuration;
- outputs;
- validation results;
- cost and latency;
- reviewer;
- final state.
