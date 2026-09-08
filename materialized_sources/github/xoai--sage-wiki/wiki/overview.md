---
uid: wiki-page:repo-xoai--sage-wiki-overview-ab36031ace70
title: xoai/sage-wiki — repository overview
slug: repos/xoai--sage-wiki/overview
page_type: system
status: review
summary: '**English** | [中文](docs/translations/README_zh.md) | [日本語](docs/translations/README_ja.md) | [한국어](docs/translations/README_ko.md)
  | [Tiếng Việt](docs/translations/README_vi.md) | [Français](docs/translations/README_fr.md) | [Русский](docs/translations/README_ru.md)'
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
    one_line: '**English** | [中文](docs/translations/README_zh.md) | [日本語](docs/translations/README_ja.md) | [한국어](docs/translations/README_ko.md)
      | [Tiếng Việt](docs/translations/README_vi.md) | [Français](docs/translations/README_fr.md) | [Русский](docs/translations/README_ru.md)'
    short: '**English** | [中文](docs/translations/README_zh.md) | [日本語](docs/translations/README_ja.md) | [한국어](docs/translations/README_ko.md)
      | [Tiếng Việt](docs/translations/README_vi.md) | [Français](docs/translations/README_fr.md) | [Русский](docs/translations/README_ru.md)'
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# xoai/sage-wiki

**English** | [中文](docs/translations/README_zh.md) | [日本語](docs/translations/README_ja.md) | [한국어](docs/translations/README_ko.md) | [Tiếng Việt](docs/translations/README_vi.md) | [Français](docs/translations/README_fr.md) | [Русский](docs/translations/README_ru.md)

- Frozen commit: `ab36031ace701fb1e3c620323d138a90a450f48d`
- Indexed paths: 1291
- Evidence excerpts: 32

## README outline
- sage-wiki — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L3`
- From personal vault to company knowledge graph — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L22`
- Knowledge graph & graph memory — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L28`
- Guides — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L80`
- Install — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L103`
- CLI only (no web UI) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L106`
- With web UI (requires Node.js for building frontend assets) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L109`
- Quickstart — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L115`
- Greenfield (new project) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L119`
- Add sources to raw/ — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L123`
- Edit config.yaml to add api key, and pick LLMs — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L125`
- Vault Overlay (existing Obsidian vault) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L156`
- Edit config.yaml to set source/ignore folders, add api key, pick LLMs — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L161`
- Supported Source Formats — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L168`
- Graph memory — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L189`
- Commands — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L212`
- TUI — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L243`
- Web UI — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L258`
- MCP Integration — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L272`
- Agent skills — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L310`
- Claude Code — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L318`
- Or manually: copy skills/sage-wiki/SKILL.md to .claude/skills/ — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L321`
- Client SDKs — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L340`
- Examples — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L375`
- Embedding in a Go program — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L386`
- Operations — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L429`
- Embedding (Go API) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L458`
- Cost — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L482`
- Resource limits — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L508`
- Scaling to large vaults — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L535`
- Bounded vector memory (opt-in) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L551`
- Multi-workspace serve — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L582`
- Remote mirror (S3 backup) — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L610`
- 1. Configure the mirror: block (below), then: — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L618`
- Ecosystem — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L689`
- Contribution Packs — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L691`
- External Parsers — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L711`
- Teams — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L719`
- Benchmarks — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L724`
- Architecture — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L756`
- License — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L773`
