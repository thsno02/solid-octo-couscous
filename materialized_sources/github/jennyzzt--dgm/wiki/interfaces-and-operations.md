---
uid: wiki-page:repo-jennyzzt--dgm-interfaces-and-operations-a565fd2d1dca
title: jennyzzt/dgm — interfaces and operations
slug: repos/jennyzzt--dgm/interfaces-and-operations
page_type: method
status: review
summary: Candidate operating surface of jennyzzt/dgm.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
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
  build_id: repo-capsule:jennyzzt--dgm:a565fd2d1dca
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
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
  - github:jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Candidate operating surface of jennyzzt/dgm.
    short: Candidate operating surface of jennyzzt/dgm.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Interfaces and operations

- `# API keys, add to ~/.bashrc` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L26`
- `export OPENAI_API_KEY='...'` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L27`
- `export ANTHROPIC_API_KEY='...'` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L28`
- `# Verify that Docker is properly configured in your environment.` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L32`
- `docker run hello-world` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L33`
- `# If a permission error occurs, add the user to the Docker group` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L35`
- `sudo usermod -aG docker $USER` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L36`
- `newgrp docker` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L37`
- `# Install dependencies` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L41`
- `python3 -m venv venv` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L42`
- `source venv/bin/activate` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L43`
- `pip install -r requirements.txt` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L44`
- `# Optional: for running analysis` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L46`
- `sudo apt-get install graphviz graphviz-dev` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L47`
- `pip install -r requirements_dev.txt` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L48`
- `# Clone SWE-bench` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L52`
- `cd swe_bench` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L53`
- `git clone https://github.com/princeton-nlp/SWE-bench.git` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L54`
- `cd SWE-bench` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L55`
- `git checkout dc4c087c2b9e4cefebf2e3d201d27e36` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L56`
- `pip install -e .` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L57`
- `cd ../../` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L58`
- `# Prepare Polyglot` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L60`
- `# Make sure git is properly configured in your environment with username and email` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L61`
- `python -m polyglot.prepare_polyglot_dataset` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L62`
- `python DGM_outer.py` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L67`
- `@article{zhang2025darwin,` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L97`
- `title={Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents},` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L98`
- `author={Zhang, Jenny and Hu, Shengran and Lu, Cong and Lange, Robert and Clune, Jeff},` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L99`
- `journal={arXiv preprint arXiv:2505.22954},` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L100`
- `year={2025}` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L101`
- `}` — `repo://jennyzzt/dgm@a565fd2d1dca504ef5104a7cc0f3bdc4ab9b4fd2/README.md#L102`

Commands are syntactically extracted and unverified.
