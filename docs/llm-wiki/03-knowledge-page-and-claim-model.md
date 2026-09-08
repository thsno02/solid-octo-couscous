
# Knowledge, Page, and Claim Model

## Why three objects are required

The system must not collapse these:

### Source

What an external artifact actually contains.

### Claim

A scoped assertion derived from or made by a source.

### Page

An editorial synthesis that organizes claims for a reader or agent.

Example:

```text
Source S1: DGM paper revision v2
Claim C1: the system preserves a branching archive of agent variants
Page P1: Darwin Gödel Machine
Page P2: Open-ended agent evolution
Page P3: Archive-based selection mechanisms
```

One claim can appear in several pages. One page can contain claims from many sources. Retraction of S1 affects C1 and all dependent sections, not every page indiscriminately.

## Claim structure

A claim should include:

```yaml
uid:
assertion_kind:
subject:
predicate:
object:
qualifiers:
source_ref:
source_selector:
evidence_text_hash:
valid_time:
recorded_time:
confidence:
uncertainty_type:
contradiction_refs:
derivation:
review:
promotion_state:
versioning:
```

`assertion_kind` is one of:

- observation;
- assertion;
- inference;
- prediction;
- decision;
- action.

## Page types

| Type | Purpose |
|---|---|
| `map` | Entry point or map of content |
| `overview` | Broad orientation |
| `concept` | Explain a concept and its boundaries |
| `entity` | Describe a person, lab, project, standard, or artifact |
| `method` | Explain a mechanism or algorithm |
| `system` | Explain an end-to-end architecture |
| `comparison` | Compare alternatives using a declared axis |
| `timeline` | Show changes through time |
| `debate` | Preserve disagreement and evidence |
| `evidence` | Summarize evidence for a narrow question |
| `source` | Human-readable source summary |
| `research_question` | Track an unresolved question |
| `synthesis` | Combine multiple mature pages for a decision |
| `collection` | Explain a corpus or batch |
| `gap` | Identify missing knowledge or evidence |
| `decision` | Record an architecture or governance decision |
| `evaluation` | Report quality and benchmark results |

## Page frontmatter

The page schema requires:

- stable page ID and slug;
- page type and state;
- summary;
- claim and source references;
- typed outgoing links;
- build provenance;
- review state;
- freshness state;
- consumption metadata.

The Markdown body is not parsed as the only source of machine state.

## Typed links

`[[wikilinks]]` are useful for humans but too ambiguous alone. A link should also have a typed representation:

```yaml
- target: wiki-page:belief-revision
  relation: compares_with
  claim_refs:
    - claim:knowledge-editing-vs-belief-revision
```

Useful relations include:

- `explains`;
- `part_of`;
- `depends_on`;
- `extends`;
- `implements`;
- `evaluates`;
- `contradicts`;
- `supersedes`;
- `evidenced_by`;
- `related`.

## Page revision versus claim version

A wording change can create a new page revision without changing knowledge. A new experiment can change a claim without immediately changing every page. These version streams must remain distinct and be linked through a `WikiChange`.

## Citation granularity

Use three tiers:

1. page bibliography for orientation;
2. paragraph citations as the normal minimum;
3. atomic claim/evidence selectors for disputed, numerical, temporal, policy-sensitive, or action-triggering content.

## Editorial content

Pages may include framing, summaries, and navigation that are not factual claims. Such text should be marked or kept distinguishable from evidence-bearing statements.
