
# Principles and Boundaries

## Principle 1 — compile knowledge, do not repeatedly improvise it

A normal chat-with-documents system retrieves passages and improvises an answer for each query. An LLM Wiki performs deliberate work ahead of the query:

- identify concepts and entities;
- connect sources;
- reconcile or expose disagreements;
- create readable pages;
- maintain indexes;
- record what changed.

This creates a persistent artifact that can be inspected and improved.

## Principle 2 — raw sources remain immutable

The wiki may summarize and reorganize source material, but source snapshots remain separately versioned. A wiki rebuild must be possible from selected source revisions and build configuration.

## Principle 3 — page is not fact

A page is a narrative and navigational projection. It can contain:

- multiple claims;
- opposing claims;
- background explanation;
- editorial organization;
- open questions.

The claim layer retains atomic evidence, uncertainty, and temporal scope.

## Principle 4 — generated change is a proposal

LLM output never directly becomes a trusted page or claim. It creates a `WikiChange` with:

- base revision;
- source delta;
- affected claims and pages;
- semantic diff;
- validations;
- review decision;
- rollout and rollback.

## Principle 5 — organize before writing

For broad topics, compilation follows an outline-first process:

1. discover perspectives;
2. identify questions;
3. retrieve and inspect evidence;
4. create an outline;
5. identify missing evidence;
6. write sections;
7. validate each section.

This is more reliable than asking one model to read everything and write a page in one pass.

## Principle 6 — citations are scoped

A page-level bibliography is insufficient. At minimum, every factual paragraph has citations. High-impact, disputed, temporal, quantitative, or action-triggering statements reference atomic claims and exact source selectors.

## Principle 7 — disagreement is data

Conflicting sources are not silently averaged. The wiki can publish a `DebatePage` or a disputed section containing:

- each claim;
- its source and scope;
- why they conflict;
- available resolution;
- current review state.

## Principle 8 — verifiability, truth, and inclusion differ

A claim may be:

- authentic but false;
- supported by a source but poorly scoped;
- verifiable but not important enough for a page;
- true but not publishable because evidence is unavailable;
- publishable as a disputed view rather than as settled fact.

Admission logic must represent these cases.

## Principle 9 — human and agent views share IDs

Humans browse Markdown. Agents consume structured frontmatter, typed links, claim IDs, source IDs, indexes, and context packs. Both views point to the same identities and revisions.

## Principle 10 — the wiki is replaceable

The source, claim, schema, and change records must survive replacement of the Markdown renderer or wiki application. Obsidian, MediaWiki, a web UI, and an agent API are interfaces, not the knowledge substrate.

## Boundaries

LLM Wiki is not:

- a vector database;
- a conventional ontology;
- a replacement for source verification;
- a guarantee of factual correctness;
- an unrestricted autonomous editor;
- a dump of all generated answers;
- one giant summary file;
- a single-model memory.
