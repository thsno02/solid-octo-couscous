# Raw data collection

This directory stores source material for the knowledge-base self-evolution research pipeline.

## Research scope

The collection deliberately covers a wider evolutionary background than knowledge systems alone:

1. recursive self-improvement (RSI) and self-modification,
2. open-ended evolution, quality-diversity, stepping stones and co-evolution,
3. meta-learning and learned optimization,
4. self-training, self-reward and evaluator evolution,
5. **automated research / AI scientists / autonomous scientific discovery**,
6. automated agent/workflow design,
7. knowledge/memory/graph self-evolution,
8. governance of evolving agents: objective stability, evaluator reliability, provenance, replication, mesa-optimization, power-seeking and oversight.

### Why auto research is first-class

Auto research is not treated as a downstream application. It is a concrete self-evolution loop in a domain where the evolving object is knowledge itself:

`prior knowledge -> research question -> hypothesis -> critique/selection -> experiment -> evidence -> claim revision -> verified knowledge write-back -> next research question`

The collection therefore tracks both systems that *do research* and systems that make research cumulative across time. In particular, shared research memory, world models, preprint/repository write-back, contradiction detection, replication, provenance, and generation of the next problem are considered core mechanisms of knowledge evolution.

For a cross-source taxonomy and priority list, see `collections/auto_research.yaml`.

## Layout

- `arxiv/<paper-title>/` — arXiv papers. Prefer unpacked TeX source when available; keep source metadata next to it.
- `biorxiv/<paper-title>/` — bioRxiv preprints and provenance metadata.
- `journal/<paper-title>/` — peer-reviewed journal articles that are important primary sources and not primarily represented by arXiv.
- `paper/<paper-title>/` — other foundational papers/book chapters not primarily distributed through arXiv.
- `blog/<article-title>/` — public lab/researcher blog metadata, canonical URL, and research notes/summary.
- `github/<project-or-article-title>/` — source/project metadata for implementations that materially describe evolving AI/knowledge systems.
- `x/<post-or-thread-title>/` — public post/thread metadata and canonical URL when relevant.
- `collections/<topic>.yaml` — cross-source topic maps used for coverage, priority, deduplication and future scheduled collection.

Each item should include a `metadata.yaml` with provenance, dates, authors, source URL, topic tags and (where useful) an explicit link to the knowledge-evolution thesis. For copyrighted web articles, store metadata + canonical URL + structured notes rather than copying the full article body.

For arXiv, `source_archive_url` points to `/src/<id>` and is the preferred acquisition target because it exposes the original TeX bundle. The current GitHub connector writes UTF-8 text but cannot directly ingest gzip/tar binary source archives, so metadata records preserve the exact source archive URL for a downloader/materializer stage.

## Trust policy for evolving research knowledge

A generated paper/report is evidence-bearing research output, **not automatically trusted knowledge**. Promotion into a durable knowledge layer should preserve:

- claim and hypothesis lineage,
- source and experimental provenance,
- contradictory evidence,
- code/data/experiment trace where available,
- replication or independent verification status,
- evaluator/reviewer identity and protocol,
- confidence/status changes over time.

This distinction is critical because recursive research systems consume their own prior outputs; without provenance and verification, the loop can compound error as easily as it compounds capability.
