
# Evaluation and Quality Gates

## Evaluation layers

### 1. Source and parsing

- canonical source resolves;
- selected revision is pinned;
- content hash recorded;
- structure recovered;
- extraction loss reported;
- rights allow the operation.

### 2. Claim extraction

- claim atomicity;
- correct assertion kind;
- exact evidence selector;
- subject/object identity accuracy;
- qualifier and temporal-scope preservation;
- unsupported extraction rate.

### 3. Citation

- citation presence;
- entailment;
- completeness;
- source quality;
- independence;
- selector precision;
- no circular sourcing.

ALCE-style citation metrics are useful here, but they must be evaluated against this repository's source types and high-risk cases.

### 4. Factual precision

Use FActScore-like decomposition:

```text
supported atomic claims / checkable atomic claims
```

Also report:

- disputed;
- unsupported;
- uncheckable;
- inferred;
- predicted.

A single factuality percentage hides these distinctions.

### 5. Contradiction

Evaluate:

- explicit contradictions;
- implicit contradictions;
- incompatible time or population scope;
- cross-page contradictions;
- contradiction explanation quality;
- false-positive conflict detection.

Use WikiContradict and WikiCollide as methodological seeds, then create a repository-specific set.

### 6. Organization

STORM/WikiGenBench-inspired measures:

- outline breadth;
- outline depth;
- perspective coverage;
- section coherence;
- redundancy;
- source diversity;
- missing prerequisite concepts;
- link usefulness.

### 7. Editorial governance

- neutral framing;
- due weight;
- separation of source views and wiki voice;
- no original synthesis presented as cited fact;
- treatment of minority and disputed evidence;
- inclusion relevance;
- reviewer agreement and unresolved dissent.

### 8. Freshness and evolution

- time since dependency check;
- changed-source coverage;
- stale claim rate;
- affected-page detection recall;
- repair latency;
- supersession correctness;
- retraction propagation;
- rollback success.

### 9. Consumer utility

Evaluate fixed tasks:

- answer accuracy;
- citation traceability;
- research orientation time;
- task completion;
- token cost;
- latency;
- number of source opens;
- navigation success;
- human learning and confidence.

Compare:

1. raw source only;
2. vector RAG;
3. wiki only;
4. wiki plus source access;
5. claim graph plus wiki.

## Gate classes

### Blocking

- broken source or claim reference;
- failed schema;
- unsupported high-risk claim;
- unresolved identity collision;
- prohibited rights state;
- policy violation;
- source retraction not propagated;
- no rollback for breaking change.

### Warning

- weak source diversity;
- stale low-risk background;
- orphan page;
- high redundancy;
- missing secondary perspective;
- uncertain automatic evaluation.

### Informational

- possible new link;
- page split suggestion;
- candidate research gap.

## Evaluator policy

- pin evaluator model and prompt versions;
- use more than one evaluator for high-risk content;
- use hidden or held-out checks;
- sample human review;
- monitor evaluator drift;
- retain raw evaluator outputs;
- do not let the same agent generate, grade, and merge without independent controls.

## Initial acceptance thresholds

These are starting points, not permanent truth:

- 100% valid source and claim references;
- 100% factual paragraphs cited;
- 100% high-risk claims linked to atomic evidence;
- zero blocking contradictions hidden from the page;
- zero broken links in published pages;
- zero unreviewed entity merges;
- complete build manifest and rollback plan;
- fixed task suite shows no material regression.

Threshold changes are policy changes and require review.
