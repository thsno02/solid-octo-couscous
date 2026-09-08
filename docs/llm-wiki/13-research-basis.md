
# Research Basis

This design combines several distinct lineages. No single source is treated as a complete architecture.

## Compiled wiki pattern

### Andrej Karpathy — LLM Wiki

Primary contribution:

- immutable raw-source layer;
- LLM-maintained Markdown wiki;
- schema or operating instructions;
- ingest, query, and lint;
- content index and chronological log;
- Git/Obsidian-compatible persistent artifact.

Canonical source: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>

## Research and outline generation

### STORM — arXiv:2402.14207

Contributes:

- perspective discovery;
- simulated multi-perspective questioning;
- trusted-source retrieval;
- outline-first long-form article generation;
- Wikipedia-editor feedback and outline evaluation.

### Co-STORM — arXiv:2408.15232

Contributes:

- human steering of multi-agent research discourse;
- dynamic mind-map construction;
- discovery of unknown unknowns;
- report generation from a collaborative exploration trace.

### WikiGenBench — arXiv:2402.18264

Contributes:

- real-world full-length Wikipedia generation benchmark;
- evaluation of organization, verifiability, and comprehensiveness;
- evidence that strong structure and high verifiability remain separate optimization goals.

### WikiSum — arXiv:1801.10198

Contributes the historical framing of article generation as multi-document selection and synthesis over long inputs.

## Factuality, citation, and repair

### FActScore — arXiv:2305.14251

Contributes atomic-fact decomposition and supported-fact precision for long-form output.

### ALCE — arXiv:2305.14627

Contributes reproducible evaluation of retrieval, correctness, fluency, and citation quality.

### RARR — arXiv:2210.08726

Contributes a research-then-revise repair process for unsupported generated text.

### WikiChat — arXiv:2305.14292

Contributes grounded conversational consumption over a curated wiki corpus.

## Contradiction and maintenance

### WikiContradict — arXiv:2406.13805

Contributes real-world contradictory Wikipedia passages and evaluation of whether models acknowledge conflict.

### CLAIRE / WikiCollide — arXiv:2509.23233

Contributes corpus-level inconsistency detection, evidence presentation, and human-editor review.

### Streaming Knowledge Compilation — arXiv:2606.09877

A watch item for materiality-based retention and evaluation of time-evolving compiled knowledge under a fixed budget. It is not treated as settled methodology.

## Editorial and statement governance

### Wikipedia policies

Transferred concepts:

- verifiability;
- inline citation burden;
- reliable-source appropriateness;
- neutral point of view;
- due weight;
- no original research;
- discussion and consensus;
- verifiability does not force inclusion;
- circular-sourcing prevention.

Primary pages:

- <https://en.wikipedia.org/wiki/Wikipedia:Verifiability>
- <https://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view>
- <https://en.wikipedia.org/wiki/Wikipedia:No_original_research>
- <https://en.wikipedia.org/wiki/Wikipedia:Consensus>

### Wikidata and Wikibase

Transferred concepts:

- statement rather than bare triple;
- qualifiers;
- references;
- normal, preferred, and deprecated ranks;
- unknown value versus no value;
- property constraints;
- collaborative data-model evolution.

Primary pages:

- <https://www.wikidata.org/wiki/Wikidata:Data_model>
- <https://www.mediawiki.org/wiki/Wikibase/DataModel/Primer>

### MediaWiki

Transferred concepts:

- immutable revisions;
- permanent revision links;
- diffs;
- attribution;
- talk/discussion;
- rollback;
- watch and change workflows.

Primary page: <https://www.mediawiki.org/wiki/Help:History>

## Implementation evidence

Representative projects are tracked in `raw_data/collections/llm_wiki.yaml`. They are used to study implementation choices, not to establish scientific truth:

- `ddsyasas/llm-wiki`;
- `nashsu/llm_wiki`;
- `xoai/sage-wiki`;
- `VectifyAI/OpenKB`;
- `stanford-oval/storm`;
- `wikimedia/mediawiki`;
- `wikimedia/mediawiki-extensions-Wikibase`;
- `SemanticMediaWiki/SemanticMediaWiki`;
- `shmsw25/FActScore`;
- `princeton-nlp/ALCE`;
- `anthonywchen/RARR`.

## Synthesis rule

The repository adopts:

```text
Karpathy:
  persistent compiled artifact

STORM:
  research and outline before prose

Wikipedia:
  editorial sourcing and neutral synthesis

Wikidata:
  qualified, referenced and ranked statements

Ontology work:
  identity, semantics, time, policy and change lineage

Repository governance:
  proposal, validation, review, admission and rollback
```

Any future method that contradicts these decisions must be proposed as an architecture change rather than silently introduced by an implementation.
