# Raw data collection

This directory stores source material for the knowledge-base self-evolution research pipeline.

## Research scope

The collection deliberately covers a wider evolutionary background than knowledge systems alone:

1. recursive self-improvement (RSI) and self-modification,
2. open-ended evolution, quality-diversity, stepping stones and co-evolution,
3. meta-learning and learned optimization,
4. self-training, self-reward and evaluator evolution,
5. automated agent/workflow design and automated scientific discovery,
6. knowledge/memory/graph self-evolution,
7. governance of evolving agents: objective stability, mesa-optimization, power-seeking, provenance and oversight.

## Layout

- `arxiv/<paper-title>/` — arXiv papers. Prefer unpacked TeX source when available; keep source metadata next to it.
- `paper/<paper-title>/` — foundational or peer-reviewed papers/book chapters not primarily distributed through arXiv.
- `blog/<article-title>/` — public blog/article metadata, canonical URL, and research notes/summary.
- `github/<project-or-article-title>/` — source/project metadata for implementations that materially describe evolving AI/knowledge systems.
- `x/<post-or-thread-title>/` — public post/thread metadata and canonical URL when relevant.

Each item should include a `metadata.yaml` with provenance, dates, authors, source URL, and topic tags. For copyrighted web articles, store metadata + canonical URL + structured notes rather than copying the full article body.

For arXiv, `source_archive_url` points to `/src/<id>` and is the preferred acquisition target because it exposes the original TeX bundle. The current GitHub connector writes UTF-8 text but cannot directly ingest gzip/tar binary source archives, so metadata records preserve the exact source archive URL for a downloader/materializer stage.
