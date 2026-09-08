---
uid: wiki-page:repo-vectifyai--openkb-interfaces-and-operations-ff54396e575e
title: VectifyAI/OpenKB — interfaces and operations
slug: repos/vectifyai--openkb/interfaces-and-operations
page_type: method
status: review
summary: Candidate operating surface of VectifyAI/OpenKB.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
  build_id: repo-capsule:VectifyAI--OpenKB:ff54396e575e
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
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
  - github:VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Candidate operating surface of VectifyAI/OpenKB.
    short: Candidate operating surface of VectifyAI/OpenKB.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Interfaces and operations

- `pip install openkb` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L59`
- `pip install git+https://github.com/VectifyAI/OpenKB.git` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L68`
- `git clone https://github.com/VectifyAI/OpenKB.git` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L74`
- `cd OpenKB` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L75`
- `pip install -e .` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L76`
- `# 1. Create a directory for your knowledge base` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L84`
- `mkdir my-kb && cd my-kb` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L85`
- `# 2. Initialize the knowledge base` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L87`
- `openkb init` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L88`
- `# 3. Add documents` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L90`
- `openkb add paper.pdf` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L91`
- `openkb add ~/papers/                            # Add a whole directory` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L92`
- `openkb add https://arxiv.org/pdf/2509.11420     # Or fetch from a URL` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L93`
- `# 4. Ask a question` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L95`
- `openkb query "What are the main findings?"` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L96`
- `# 5. Or chat interactively` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L98`
- `openkb chat` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L99`
- `# (Optional) Turn the wiki into other outputs` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L101`
- `openkb skill new my-expert "Reason like an expert on <your-topic>"   # a portable agent skill` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L102`
- `openkb visualize                                                     # an interactive knowledge graph` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L103`
- `openkb deck new my-deck "An intro deck on <your-topic>"              # slides — a single-file HTML deck` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L104`
- `LLM_API_KEY=your_llm_api_key` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L116`
- `pip install "openkb[web]"` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L126`
- `openkb-web                       # serves the API + Workbench at http://127.0.0.1:7566/` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L127`
- `model: gpt-5.4                   # LLM model (any LiteLLM-supported provider)` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L255`
- `language: en                     # Wiki output language` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L256`
- `pageindex_threshold: 20          # PDF pages threshold for PageIndex` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L257`
- `PAGEINDEX_API_KEY=your_pageindex_api_key` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L279`
- `/plugin marketplace add VectifyAI/OpenKB` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L310`
- `/plugin install openkb@vectify` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L311`
- `git clone https://github.com/VectifyAI/OpenKB.git ~/openkb-src` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L323`
- `mkdir -p ~/.agents/skills` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L324`
- `ln -s ~/openkb-src/skills/openkb ~/.agents/skills/openkb` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L325`
- `gemini skills install https://github.com/VectifyAI/OpenKB.git --path skills/openkb --consent` — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L335`

Commands are syntactically extracted and unverified.
