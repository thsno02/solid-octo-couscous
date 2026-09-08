---
uid: wiki-page:repo-getzep--graphiti-architecture-3ff5c160c57c
title: getzep/graphiti — architecture
slug: repos/getzep--graphiti/architecture
page_type: system
status: review
summary: Structural view of getzep/graphiti.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
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
  build_id: repo-capsule:getzep--graphiti:3ff5c160c57c
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
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
  - github:getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Structural view of getzep/graphiti.
    short: Structural view of getzep/graphiti.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Architecture

## Top-level paths

- `graphiti_core`: 159 paths
- `mcp_server`: 59 paths
- `tests`: 53 paths
- `examples`: 28 paths
- `.github`: 19 paths
- `server`: 17 paths
- `images`: 4 paths
- `.env.example`: 1 paths
- `.gitignore`: 1 paths
- `AGENTS.md`: 1 paths
- `CLAUDE.md`: 1 paths
- `CODE_OF_CONDUCT.md`: 1 paths
- `CONTRIBUTING.md`: 1 paths
- `Dockerfile`: 1 paths
- `LICENSE`: 1 paths
- `Makefile`: 1 paths
- `OTEL_TRACING.md`: 1 paths
- `README.md`: 1 paths
- `SECURITY.md`: 1 paths
- `Zep-CLA.md`: 1 paths
- `conftest.py`: 1 paths
- `depot.json`: 1 paths
- `docker-compose.test.yml`: 1 paths
- `docker-compose.yml`: 1 paths
- `ellipsis.yaml`: 1 paths
- `py.typed`: 1 paths
- `pyproject.toml`: 1 paths
- `pytest.ini`: 1 paths
- `signatures`: 1 paths
- `spec`: 1 paths
- `uv.lock`: 1 paths

## Extension profile

- `.py`: 268
- `.md`: 23
- `.yml`: 21
- `.example`: 6
- `.json`: 5
- `.yaml`: 5
- `.toml`: 4
- `.lock`: 4
- `.ini`: 4
- `.sh`: 3
- `.txt`: 3
- `.ipynb`: 2
- `.png`: 2
- `.typed`: 2
- `.gif`: 2
- `.svg`: 1
- `.standalone`: 1

Directory structure is not proof of runtime behavior.
