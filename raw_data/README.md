# Raw data collection

This directory stores source material for the knowledge-base self-evolution research pipeline.

## Layout

- `arxiv/<paper-title>/` — arXiv papers. Prefer unpacked TeX source when available; keep source metadata next to it.
- `blog/<article-title>/` — public blog/article metadata, canonical URL, and research notes/summary.
- `github/<project-or-article-title>/` — source/project metadata for implementations that materially describe dynamic knowledge or agent-memory systems.
- `x/<post-or-thread-title>/` — public post/thread metadata and canonical URL when relevant.

Each item should include a `metadata.yaml` with provenance, dates, authors, source URL, and topic tags. For copyrighted web articles, store metadata + canonical URL + structured notes rather than copying the full article body.
