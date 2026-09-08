---
uid: wiki-page:repo-getzep--graphiti-overview-3ff5c160c57c
title: getzep/graphiti — repository overview
slug: repos/getzep--graphiti/overview
page_type: system
status: review
summary: Graphiti
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
    one_line: Graphiti
    short: Graphiti
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# getzep/graphiti

Graphiti

- Frozen commit: `3ff5c160c57c6790aeb148e7388bf380ed351c7b`
- Indexed paths: 363
- Evidence excerpts: 14

## README outline
- What is a Context Graph? — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L60`
- Graphiti and Zep — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L79`
- Zep vs Graphiti — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L95`
- When to choose which — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L108`
- Why Graphiti? — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L114`
- Graphiti vs. GraphRAG — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L136`
- Installation — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L154`
- Installing with FalkorDB Support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L190`
- or with uv — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L197`
- or embedded version (requires Python 3.12+) — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L200`
- or with uv — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L202`
- Installing with Kuzu Support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L206`
- or with uv — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L218`
- Installing with Amazon Neptune Support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L222`
- or with uv — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L229`
- You can also install optional LLM providers as extras: — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L233`
- Install with Anthropic support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L236`
- Install with Groq support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L239`
- Install with Google Gemini support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L242`
- Install with multiple providers — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L245`
- Install with FalkorDB and LLM providers — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L248`
- Install with Amazon Neptune — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L251`
- Default to Low Concurrency; LLM Provider 429 Rate Limit Errors — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L255`
- Quick Start — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L267`
- Running with Docker Compose — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L290`
- MCP Server — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L310`
- REST Service — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L328`
- Optional Environment Variables — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L334`
- Database Configuration — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L340`
- Neo4j with Custom Database Name — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L350`
- Create a Neo4j driver with custom database name — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L356`
- Pass the driver to Graphiti — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L364`
- FalkorDB with Custom Database Name — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L368`
- Create a FalkorDB driver with custom database name — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L374`
- Or use embedded FalkorDB Lite (requires Python 3.12+) — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L383`
- from redislite.async_falkordb_client import AsyncFalkorDB — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L384`
- falkordb_client = AsyncFalkorDB(dbfilename='/path/to/database.db') — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L385`
- driver = FalkorDriver(falkor_db=falkordb_client) — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L386`
- Pass the driver to Graphiti — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L388`
- Kuzu — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L392`
- Create a Kuzu driver — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L402`
- Pass the driver to Graphiti — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L405`
- Amazon Neptune — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L409`
- Create a Neptune driver — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L415`
- Pass the driver to Graphiti — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L423`
- Using Graphiti with Azure OpenAI — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L429`
- Quick Start — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L433`
- Initialize Azure OpenAI client using the standard OpenAI client — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L442`
- with Azure's v1 API endpoint — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L443`
- Create LLM and Embedder clients — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L449`
- Initialize Graphiti with Azure OpenAI clients — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L459`
- Now you can use Graphiti with Azure OpenAI — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L468`
- Using Graphiti with Google Gemini — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L480`
- or — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L490`
- Google API key configuration — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L501`
- Initialize Graphiti with Gemini clients — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L504`
- Now you can use Graphiti with Google Gemini for all components — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L529`
- Using Graphiti with OpenAI-compatible providers and local LLMs — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L536`
- Configure Ollama LLM client — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L560`
- Initialize Graphiti with Ollama clients — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L570`
- Now you can use Graphiti with local Ollama models — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L587`
- Structured output and small models — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L592`
- Documentation — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L612`
- Telemetry — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L618`
- What We Collect — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L623`
- What We Don't Collect — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L635`
- Why We Collect This Data — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L646`
- View the Telemetry Code — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L657`
- How to Disable Telemetry — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L661`
- For bash users (~/.bashrc or ~/.bash_profile) — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L674`
- For zsh users (~/.zshrc) — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L677`
- Then initialize Graphiti as usual — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L688`
- Technical Details — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L696`
- Contributing — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L703`
- Support — `repo://getzep/graphiti@3ff5c160c57c6790aeb148e7388bf380ed351c7b/README.md#L709`
