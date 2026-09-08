
# Aggregation, Linking, and Navigation

## Aggregation is not concatenation

A page should not append one summary per source. It should reorganize knowledge around stable questions, concepts, entities, mechanisms, evidence, and disagreements.

## Aggregation primitives

### Deduplicate

Merge only when claims have equivalent meaning and compatible scope.

### Refine

A new claim may add qualifiers, narrow the population, improve temporal precision, or supply stronger evidence.

### Contrast

Create explicit comparison axes:

- evolving object;
- variation operator;
- evaluator;
- selection rule;
- retention mechanism;
- governance;
- evidence level;
- failure mode.

### Preserve conflict

Conflicting claims remain separate and linked. A debate page can explain the conflict without inventing resolution.

### Abstract

Create higher-level concepts only when the abstraction can point to supporting claims and exceptions.

### Decompose

Split pages that mix unrelated questions, have incompatible review owners, or exceed navigation and context budgets.

## Navigation hierarchy

Use several complementary structures:

1. root index;
2. maps of content;
3. typed page folders;
4. typed links;
5. full-text search;
6. optional embeddings;
7. claim/evidence graph;
8. timelines and change feed;
9. task-oriented context packs.

No single structure should carry all retrieval responsibility.

## Maps of content

Suggested top-level maps for this repository:

- Knowledge Self-Evolution
- Recursive Self-Improvement
- Open-Ended Evolution
- Automated Research
- Agent Memory
- Knowledge Editing
- Ontology and Semantic Architecture
- LLM Wiki
- Governance and Evaluation
- Standards and Infrastructure
- Open Implementations
- Research Gaps

A map is curated routing, not a second copy of page content.

## Page splitting and merging

Split when:

- sections have different concepts or owners;
- the page mixes settled and disputed questions;
- evidence refresh cadences differ;
- context cost is too high;
- the page becomes a chronological dump.

Merge when:

- two pages are true duplicates;
- identity resolution confirms equivalence;
- links and claims can be migrated without losing scope.

Both operations require a change proposal and redirect lineage.

## Typed links and backlinks

Every typed link should be invertible for navigation:

```text
implements ↔ implemented_by
evaluates ↔ evaluated_by
extends ↔ extended_by
contradicts ↔ contradicted_by
supersedes ↔ superseded_by
part_of ↔ has_part
```

Backlinks are useful but do not define semantic relation type.

## Retrieval strategy

A recommended agent router:

```text
query
→ classify task and freshness need
→ retrieve map/index candidates
→ lexical search
→ graph expansion
→ optional vector recall
→ rerank by claim support, freshness, authority, and task fit
→ assemble bounded context pack
```

Vector similarity is a recall signal, not an admission or truth signal.

## Summary tiers

Every important page should support:

- one-line routing summary;
- short agent context summary;
- full human page;
- source and claim expansion on demand.

Summaries are generated artifacts with their own build and freshness metadata.

## Orphans and bridges

Lint should identify:

- orphan pages;
- pages with only generic `related` links;
- high-degree hubs that became vague dumping grounds;
- fragile bridge pages connecting otherwise disconnected clusters;
- missing comparison or debate pages.
