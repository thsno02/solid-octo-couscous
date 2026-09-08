# Source-Specific Consumption

## Decision

The LLM Wiki compiler consumes a normalized materialization interface, not raw URLs and not every source in the same way.

```text
source metadata
→ adapter selection
→ frozen source revision
→ source-specific parsing or semanticization
→ selectors and evidence map
→ claim extraction
→ wiki compilation
```

This prevents the compiler from confusing a repository with an article, a PDF page with a paragraph, a standard with an implementation, or a mutable current page with an immutable source revision.

## Consumption matrix

| Source | Preferred materialization | Primary selector | Extra semanticization |
|---|---|---|---|
| arXiv | source bundle and TeX tree | file and line/section | usually no |
| journal/preprint | structured HTML or licensed full text; PDF fallback | section/paragraph or page/region | no |
| GitHub repository | frozen commit and semantic repo capsule | file, blob, line, symbol | yes |
| blog | time-stamped HTML/Markdown snapshot | DOM/paragraph | viewpoint classification |
| X/thread | immutable post/thread capture | post ID and segment | context and deletion state |
| standard/ontology | exact active edition | section and term | normative/informative classification |
| dataset | versioned release and split | row/record/field | data dictionary and quality profile |
| benchmark | task and evaluator version | item/run/metric | protocol reconstruction |
| incident/retraction | primary event record | event/time/affected object | dependency impact |

## Repository-to-wiki bridge

A repository has several semantic surfaces:

```text
repository identity and commit
├── directory and module topology
├── package/dependency manifests
├── documentation
├── public interfaces and commands
├── configuration and deployment
├── tests and evaluation
├── runtime behavior
├── issue/release history
└── relationship to papers and datasets
```

No single README captures all of them. The initial deterministic capsule creates an evidence-backed baseline, but it is not a complete repo wiki.

A mature repo-wiki pass should add:

1. symbol and module extraction;
2. imports, calls, data-flow, and configuration relationships;
3. test-to-feature and benchmark-to-claim mappings;
4. public API, CLI, service, and file-format contracts;
5. architecture decisions and release evolution;
6. paper-to-code and dataset-to-code linkage;
7. exact file/line evidence for every generated statement;
8. staleness detection when the repository head changes.

## Admission boundary

Repository capsule pages have status `review`. They may guide navigation and source selection, but cannot independently corroborate a scientific claim.

Promotion requires:

- a pinned commit;
- resolvable evidence selectors;
- wording supported by source or execution evidence;
- conflict checks against papers and official documentation;
- risk-appropriate review;
- a rollback path.

README claims such as “state of the art,” “production ready,” or benchmark results remain assertions by the project until independently verified.

## Paper and repository linking

A paper and codebase are separate sources even when maintained by the same authors:

```text
Paper --describes--> Method
Repository --implements--> Method
Commit --realizes--> Repository state
Benchmark run --evaluates--> Commit
Claim --supported_by--> Paper section or benchmark run
```

Do not use an associated repository README as independent confirmation of the paper.

## Update and deletion behavior

A new commit creates a new capsule. The old capsule remains historical. The system compares file/blob and semantic deltas, finds affected claims and wiki sections, rebuilds the dependency closure, and reruns fixed evaluations.

A force-push or changed bytes under the same recorded reference is an integrity incident. An archived or deleted repository does not erase its frozen historical capsule.

## Compiler input contract

```yaml
source_uid: github:owner/repo
source_revision: <commit>
adapter: github_repo_wiki
manifest_ref: materialized_sources/github/owner--repo/manifest.yaml
evidence_index_ref: materialized_sources/github/owner--repo/evidence/excerpts.jsonl
allowed_selectors:
  - repo://owner/repo@commit/path#Lx-Ly
semantic_pages_ref: materialized_sources/github/owner--repo/wiki/
trust:
  semantic_pages: candidate
  evidence_excerpts: source-derived
  runtime_behavior: unverified
```

## Anti-patterns

- placing a GitHub URL in a RAG corpus and calling the repository ingested;
- summarizing the default branch without recording a commit;
- copying the entire repository into `raw_data`;
- citing generated repo-wiki prose instead of file evidence;
- inferring runtime behavior from directory names;
- mixing README marketing, code, tests, and issues into one trust level;
- overwriting pages when HEAD changes without preserving the old capsule;
- treating paper and repository statements as independent sources when they share the same origin.

## Current executable path

```text
pipeline/materialization.yaml
scripts/materialize_pipeline.py
scripts/validate_materialized.py
source_registry/
materialized_sources/
```
