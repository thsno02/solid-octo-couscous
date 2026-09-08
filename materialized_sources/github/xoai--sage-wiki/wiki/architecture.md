---
uid: wiki-page:repo-xoai--sage-wiki-architecture-ab36031ace70
title: xoai/sage-wiki — architecture
slug: repos/xoai--sage-wiki/architecture
page_type: system
status: review
summary: Structural view of xoai/sage-wiki.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
page_refs: []
outgoing_links: []
sections: []
temporal:
  created_at: '2026-09-09T00:00:00Z'
  updated_at: '2026-09-09T00:00:00Z'
  valid_from: null
  valid_to: null
  as_of: '2026-09-09T00:00:00Z'
provenance:
  build_id: repo-capsule:xoai--sage-wiki:ab36031ace70
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  created_at: '2026-09-09T00:00:00Z'
  updated_at: '2026-09-09T00:00:00Z'
  manual_edits_preserved: true
review:
  state: automated_checks_only
  reviewers: []
  decision_ref: null
  checked_claim_refs: []
  unresolved_issues:
  - Requires semantic review.
freshness:
  status: fresh
  checked_at: '2026-09-09T00:00:00Z'
  max_age_days: 30
  source_dependencies:
  - github:xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Structural view of xoai/sage-wiki.
    short: Structural view of xoai/sage-wiki.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Architecture

## Top-level paths

- `internal`: 752 paths
- `testdata`: 230 paths
- `cmd`: 49 paths
- `eval`: 48 paths
- `pkg`: 46 paths
- `clients`: 29 paths
- `web`: 28 paths
- `docs`: 27 paths
- `tools`: 21 paths
- `.github`: 12 paths
- `scripts`: 11 paths
- `examples`: 8 paths
- `ci`: 7 paths
- `assets`: 5 paths
- `skills`: 2 paths
- `tests`: 2 paths
- `.dockerignore`: 1 paths
- `.gitattributes`: 1 paths
- `.gitignore`: 1 paths
- `.golangci.yml`: 1 paths
- `CHANGELOG.md`: 1 paths
- `CONTRIBUTING.md`: 1 paths
- `Dockerfile`: 1 paths
- `LICENSE`: 1 paths
- `Makefile`: 1 paths
- `README.md`: 1 paths
- `api`: 1 paths
- `go.mod`: 1 paths
- `go.sum`: 1 paths
- `integration_test.go`: 1 paths

## Extension profile

- `.go`: 769
- `.json`: 236
- `.md`: 100
- `.py`: 43
- `.yaml`: 17
- `.ts`: 17
- `.txt`: 14
- `.yml`: 12
- `.sh`: 11
- `.png`: 6
- `.authz`: 6
- `.creq`: 6
- `.req`: 6
- `.sts`: 6
- `.svg`: 6
- `.tsx`: 6
- `.css`: 4
- `.jsonl`: 3
- `.js`: 2
- `.html`: 2
- `.toml`: 1
- `.typed`: 1
- `.mod`: 1
- `.sum`: 1
- `.tmpl`: 1

Directory structure is not proof of runtime behavior.
