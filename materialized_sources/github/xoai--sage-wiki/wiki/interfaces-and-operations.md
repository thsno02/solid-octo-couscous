---
uid: wiki-page:repo-xoai--sage-wiki-interfaces-and-operations-ab36031ace70
title: xoai/sage-wiki — interfaces and operations
slug: repos/xoai--sage-wiki/interfaces-and-operations
page_type: method
status: review
summary: Candidate operating surface of xoai/sage-wiki.
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
    one_line: Candidate operating surface of xoai/sage-wiki.
    short: Candidate operating surface of xoai/sage-wiki.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Interfaces and operations

- `sage-wiki ontology query --entity kubernetes --depth 3 --direction both` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L67`
- `sage-wiki provenance "service mesh"    # which sources produced this concept` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L68`
- `# CLI only (no web UI)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L106`
- `go install github.com/xoai/sage-wiki/cmd/sage-wiki@latest` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L107`
- `# With web UI (requires Node.js for building frontend assets)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L109`
- `git clone https://github.com/xoai/sage-wiki.git && cd sage-wiki` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L110`
- `cd web && npm install && npm run build && cd ..` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L111`
- `go build -tags webui -o sage-wiki ./cmd/sage-wiki/` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L112`
- `sage-wiki init my-wiki && cd my-wiki` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L122`
- `# Add sources to raw/` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L123`
- `cp ~/papers/*.pdf raw/` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L124`
- `# Edit config.yaml to add api key, and pick LLMs` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L125`
- `sage-wiki compile                                  # first compile` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L126`
- `sage-wiki compile                                  # second: zero LLM calls — unchanged docs are skipped` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L127`
- `sage-wiki compile --explain raw/paper.pdf          # why a doc compiles or skips` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L128`
- `sage-wiki compile --force                          # recompile everything regardless` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L129`
- `sage-wiki search "attention mechanism"             # hybrid search` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L130`
- `sage-wiki query "How does flash attention work?"   # cited Q&A` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L131`
- `sage-wiki tui                                      # terminal dashboard` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L132`
- `sage-wiki serve --ui                               # browser (webui build)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L133`
- `sage-wiki compile --watch                          # watch folder` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L134`
- `my-wiki/` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L142`
- `├── config.yaml           # providers, models, compiler, search, ontology` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L143`
- `├── raw/                  # drop sources here (articles, papers, code, images)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L144`
- `├── wiki/                 # compiled output — Obsidian-compatible markdown` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L145`
- `│   ├── summaries/        # per-source LLM summaries` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L146`
- `│   ├── concepts/         # concept articles (the knowledge graph)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L147`
- `│   ├── images/           # vision-captioned image descriptions` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L148`
- `│   ├── outputs/          # filed query answers (trust.include_outputs: "true")` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L149`
- `│   ├── under_review/     # filed answers awaiting trust review (default)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L150`
- `│   └── archive/          # pruned articles` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L151`
- `├── .sage/wiki.db         # one SQLite file: FTS index, vectors, ontology, queue` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L152`
- `└── .manifest.json        # source↔article mapping + compile state` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L153`
- `cd ~/Documents/MyVault` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L159`
- `sage-wiki init --vault` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L160`
- `# Edit config.yaml to set source/ignore folders, add api key, pick LLMs` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L161`
- `sage-wiki compile --watch` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L162`
- `sage-wiki tui` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L246`
- `sage-wiki serve --ui        # http://127.0.0.1:3333, requires -tags webui build` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L261`
- `{` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L279`
- `"mcpServers": {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L280`
- `"sage-wiki": {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L281`
- `"command": "sage-wiki",` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L282`
- `"args": ["serve", "--transport", "stdio", "--project", "/path/to/wiki"]` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L283`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L284`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L285`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L286`
- `# Claude Code` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L318`
- `npx skills add https://github.com/xoai/sage-wiki --skill sage-wiki` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L319`
- `# Or manually: copy skills/sage-wiki/SKILL.md to .claude/skills/` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L321`
- `npx skills add https://github.com/xoai/sage-wiki --skill sage-wiki-integrate` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L329`
- `from sagewiki import SageWiki` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L347`
- `c = SageWiki()  # SAGE_WIKI_URL / SAGE_WIKI_TOKEN from env` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L349`
- `for r in c.search("attention", limit=5).results:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L350`
- `print(r.final_score, r.content[:80])` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L351`
- `job = c.compile(topic="attention")` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L352`
- `job.wait(timeout=600)  # explicit timeout required` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L353`
- `import { SageWikiClient } from "sagewiki";` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L360`
- `const c = new SageWikiClient();` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L362`
- `const results = await c.search("attention", { limit: 5 });` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L363`
- `const job = await c.compile({ topic: "attention" });` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L364`
- `await job.waitUntilDone({ timeoutMs: 600_000 });` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L365`
- `srv, err := sagewiki.NewServer("/path/to/wiki")  // project must already exist` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L392`
- `if err != nil {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L393`
- `return err` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L394`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L395`
- `defer srv.Close()  // the caller owns the DB handle here` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L396`
- `cli, err := client.NewInProcessClient(srv.MCPServer())` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L398`
- `if err != nil {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L399`
- `return err` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L400`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L401`
- `defer cli.Close()` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L402`
- `if err := cli.Start(ctx); err != nil {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L404`
- `return err` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L405`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L406`
- `if _, err := cli.Initialize(ctx, mcp.InitializeRequest{}); err != nil {` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L407`
- `return err` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L408`
- `}` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L409`
- `res, err := cli.CallTool(ctx, mcp.CallToolRequest{` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L411`
- `Params: mcp.CallToolParams{` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L412`
- `Name:      "wiki_search",` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L413`
- `Arguments: map[string]any{"query": "attention", "limit": 5},` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L414`
- `},` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L415`
- `})` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L416`
- `w, err := engine.Open(ctx, dir)          // one Workspace per directory` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L464`
- `defer w.Close()` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L465`
- `id, _ := w.Capture(ctx, engine.Source{Path: "doc.md"})` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L466`
- `res, _ := w.Compile(ctx, engine.CompileRequest{Selector: "pending", Tier: 3})` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L467`
- `hits, _ := w.Search(ctx, engine.SearchRequest{Query: "attention", Limit: 5})` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L468`
- `sage-wiki compile --batch       # submit batch, checkpoint, exit` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L491`
- `sage-wiki compile               # poll status, retrieve when done` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L492`
- `sage-wiki cost models     # which price produced a number, and its source` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L502`
- `sage-wiki cost report     # recorded spend by model and pass/tier` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L503`
- `limits:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L517`
- `max_doc_bytes: 10485760                  # 10 MiB — max size of one ingested doc` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L518`
- `max_docs_per_capture_batch: 10           # max docs per capture batch` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L519`
- `max_compile_batch: 1000                  # max docs per compile run` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L520`
- `max_query_bytes: 32768                   # 32 KiB — max question length` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L521`
- `max_graph_traversal_nodes: 10000         # max nodes per graph traversal` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L522`
- `max_concurrent_provider_calls: 20        # concurrent LLM/embed calls in a compile` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L523`
- `max_concurrent_requests_per_conn: 8      # serve per-connection in-flight cap` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L524`
- `provider_timeout: 120s                   # per-call LLM/embed deadline` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L525`
- `compile_doc_timeout: 15m                 # per-doc compile budget` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L526`
- `vectors:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L559`
- `backend: mmap        # memory (default) | mmap` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L560`
- `quantization: none   # none (default, fp32 exact) | int8 (4x smaller)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L561`
- `sage-wiki index rebuild-vectors` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L569`
- `sage-wiki serve --workspace-root /path/to/vaults --addr 127.0.0.1:8484` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L589`
- `# 1. Configure the mirror: block (below), then:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L618`
- `sage-wiki mirror enable        # validates creds, writes manifest, bootstraps generation 1` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L619`
- `sage-wiki mirror status        # local + remote state, pending changes, lag` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L620`
- `sage-wiki mirror snapshot      # force a new generation` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L621`
- `sage-wiki mirror verify        # full re-hash invariant check (--fast for HEAD-only)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L622`
- `sage-wiki hydrate s3://bucket/prefix /path/to/empty-dir` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L623`
- `mirror:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L651`
- `enabled: false              # `mirror enable` sets this` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L652`
- `endpoint: ""                # e.g. https://<acct>.r2.cloudflarestorage.com or http://localhost:9000` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L653`
- `addressing: "auto"          # auto = virtual-host for amazonaws.com, path-style otherwise; "path"/"virtual" force` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L654`
- `bucket: ""` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L655`
- `prefix: ""                  # default: workspace directory name` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L656`
- `region: "auto"              # SigV4 region; "auto" works for R2/MinIO` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L657`
- `access_key_env: "AWS_ACCESS_KEY_ID"    # NAME of env var, never the value` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L658`
- `secret_key_env: "AWS_SECRET_ACCESS_KEY"` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L659`
- `session_token_env: "AWS_SESSION_TOKEN" # STS session token env var NAME (empty = absent)` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L660`
- `credentials_file: ""        # optional JSON {"access_key","secret_key","session_token"} outside the workspace` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L661`
- `ship_interval: "1s"         # WAL seal cadence while active` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L662`
- `snapshot_interval: "1h"     # scheduled generation cadence` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L663`
- `min_rotation_interval: "60s" # debounce for fold-forced rotations` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L664`
- `ship_lock_timeout: "5s"     # ship-mutex wait for CLI passes` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L665`
- `drain_timeout: "10s"        # serve shutdown budget for the final ship pass` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L666`
- `retain_generations: 2       # PITR depth in ROTATION COUNT, not time — raise for PITR-heavy use` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L667`
- `max_consecutive_defers: 10  # busy-writer deferrals before status surfaces rotation_deferred` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L668`
- `encryption:` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L669`
- `enabled: false            # AES-256-GCM client-side encryption` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L670`
- `key_file: ""              # 32-byte key file — MUST live outside the workspace` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L671`
- `python3 eval/eval.py .                      # quality + perf on your wiki` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L752`
- `python3 -m pytest eval/eval_test.py -q      # harness self-tests` — `repo://xoai/sage-wiki@ab36031ace701fb1e3c620323d138a90a450f48d/README.md#L753`

Commands are syntactically extracted and unverified.
