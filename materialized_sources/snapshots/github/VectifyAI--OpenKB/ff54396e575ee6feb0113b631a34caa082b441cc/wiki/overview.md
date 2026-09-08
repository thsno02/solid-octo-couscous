---
uid: wiki-page:repo-vectifyai--openkb-overview-ff54396e575e
title: VectifyAI/OpenKB — repository overview
slug: repos/vectifyai--openkb/overview
page_type: system
status: review
summary: '- *Google Open Knowledge Format (OKF)*: Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
  specification for knowledge sharing.'
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
    one_line: '- *Google Open Knowledge Format (OKF)*: Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
      specification for knowledge sharing.'
    short: '- *Google Open Knowledge Format (OKF)*: Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
      specification for knowledge sharing.'
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# VectifyAI/OpenKB

- *Google Open Knowledge Format (OKF)*: Wiki pages follow the [Google OKF](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) specification for knowledge sharing.

- Frozen commit: `ff54396e575ee6feb0113b631a34caa082b441cc`
- Indexed paths: 293
- Evidence excerpts: 6

## README outline
- OpenKB: Open LLM Knowledge Base — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L14`
- 📑 What is OpenKB — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L30`
- Why not traditional RAG? — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L36`
- Features — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L42`
- 🚀 Getting Started — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L54`
- Install — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L56`
- Quick Start — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L81`
- 1. Create a directory for your knowledge base — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L84`
- 2. Initialize the knowledge base — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L87`
- 3. Add documents — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L90`
- 4. Ask a question — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L95`
- 5. Or chat interactively — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L98`
- (Optional) Turn the wiki into other outputs — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L101`
- Set up your LLM — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L107`
- Knowledge Workbench (Web UI) — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L121`
- 🧩 How OpenKB Works — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L134`
- Architecture — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L136`
- Short vs Long Document Handling — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L142`
- Knowledge Compilation — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L153`
- ⚙️ Usage — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L165`
- Layer 1: 🧱 Wiki Foundation — compile and maintain — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L169`
- Layer 2: 💡 Generators — turn the wiki into output — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L194`
- (i) 💬 Query & Chat — *ask the wiki* — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L206`
- (ii) 🛠 Skill Factory — *drop in a book; out comes a digital expert.* — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L232`
- 🔧 Configuration — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L248`
- Settings — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L250`
- PageIndex Setup — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L262`
- AGENTS.md — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L284`
- 🔌 Integrations — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L290`
- Using with Obsidian — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L292`
- Using with Claude Code / Codex / Gemini CLI — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L301`
- REST API — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L342`
- 🧭 Learn More — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L348`
- Compared to Karpathy's Approach — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L350`
- The Stack — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L362`
- Roadmap — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L371`
- Contributing — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L379`
- License — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L383`
- 🌐 Open-Source Ecosystem — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L387`
- Support Us — `repo://VectifyAI/OpenKB@ff54396e575ee6feb0113b631a34caa082b441cc/README.md#L396`
