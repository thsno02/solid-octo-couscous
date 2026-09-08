---
uid: wiki-page:repo-sakanaai--ai-scientist-interfaces-and-operations-1de1dbc1f4ee
title: SakanaAI/AI-Scientist — interfaces and operations
slug: repos/sakanaai--ai-scientist/interfaces-and-operations
page_type: method
status: review
summary: Candidate operating surface of SakanaAI/AI-Scientist.
aliases: []
ontology_refs:
- github-repository
claim_refs: []
source_refs:
- github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
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
  build_id: repo-capsule:SakanaAI--AI-Scientist:1de1dbc1f4ee
  generated_by_agent: scripts/materialize_pipeline.py
  generated_by_model: null
  prompt_or_skill_version: deterministic-repo-capsule-v1
  compiled_from_revisions:
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
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
  - github:SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
  staleness_reasons: []
consumption:
  audiences:
  - human
  - agent
  summary_tiers:
    one_line: Candidate operating surface of SakanaAI/AI-Scientist.
    short: Candidate operating surface of SakanaAI/AI-Scientist.
    full: null
  estimated_tokens: null
  machine_entry_points:
  - ../manifest.yaml
  - ../evidence/files.jsonl
  - ../evidence/excerpts.jsonl
---

# Interfaces and operations

- `conda create -n ai_scientist python=3.11` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L68`
- `conda activate ai_scientist` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L69`
- `# Install pdflatex` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L70`
- `sudo apt-get install texlive-full` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L71`
- `# Install PyPI requirements` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L73`
- `pip install -r requirements.txt` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L74`
- `pip install anthropic[bedrock]` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L96`
- `pip install google-cloud-aiplatform` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L108`
- `pip install anthropic[vertex]` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L109`
- `export CLOUD_ML_REGION="REGION"           # for Model Garden call` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L115`
- `export ANTHROPIC_VERTEX_PROJECT_ID="PROJECT_ID"  # for Model Garden call` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L116`
- `export VERTEXAI_LOCATION="REGION"         # for Aider/LiteLLM call` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L117`
- `export VERTEXAI_PROJECT="PROJECT_ID"      # for Aider/LiteLLM call` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L118`
- `export GEMINI_API_KEY="YOUR GEMINI API KEY"` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L132`
- `export OPENAI_API_KEY="YOUR KEY HERE"` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L142`
- `export S2_API_KEY="YOUR KEY HERE"` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L143`
- `pip install pyalex` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L152`
- `export OPENALEX_MAIL_ADDRESS="YOUR EMAIL ADDRESS"` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L153`
- `python data/enwik8/prepare.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L173`
- `python data/shakespeare_char/prepare.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L174`
- `python data/text8/prepare.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L175`
- `# Set up NanoGPT baseline run` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L181`
- `# NOTE: YOU MUST FIRST RUN THE PREPARE SCRIPTS ABOVE!` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L182`
- `cd templates/nanoGPT` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L183`
- `python experiment.py --out_dir run_0` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L184`
- `python plot.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L185`
- `# Set up 2D Diffusion` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L197`
- `git clone https://github.com/gregversteeg/NPEET.git` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L198`
- `cd NPEET` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L199`
- `pip install .` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L200`
- `pip install scikit-learn` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L201`
- `# Set up 2D Diffusion baseline run` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L207`
- `cd templates/2d_diffusion` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L208`
- `python experiment.py --out_dir run_0` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L209`
- `python plot.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L210`
- `# Set up Grokking` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L222`
- `pip install einops` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L223`
- `# Set up Grokking baseline run` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L229`
- `cd templates/grokking` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L230`
- `python experiment.py --out_dir run_0` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L231`
- `python plot.py` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L232`
- `conda activate ai_scientist` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L240`
- `# Run the paper generation.` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L241`
- `python launch_scientist.py --model "gpt-4o-2024-05-13" --experiment nanoGPT_lite --num-ideas 2` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L242`
- `python launch_scientist.py --model "claude-3-5-sonnet-20241022" --experiment nanoGPT_lite --num-ideas 2` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L243`
- `import openai` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L251`
- `from ai_scientist.perform_review import load_paper, perform_review` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L252`
- `client = openai.OpenAI()` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L254`
- `model = "gpt-4o-2024-05-13"` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L255`
- `# Load paper from PDF file (raw text)` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L257`
- `paper_txt = load_paper("report.pdf")` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L258`
- `# Get the review dictionary` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L260`
- `review = perform_review(` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L261`
- `paper_txt,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L262`
- `model,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L263`
- `client,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L264`
- `num_reflections=5,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L265`
- `num_fs_examples=1,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L266`
- `num_reviews_ensemble=5,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L267`
- `temperature=0.1,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L268`
- `)` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L269`
- `# Inspect review results` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L271`
- `review["Overall"]    # Overall score (1-10)` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L272`
- `review["Decision"]   # 'Accept' or 'Reject'` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L273`
- `review["Weaknesses"] # List of weaknesses (strings)` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L274`
- `cd review_iclr_bench` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L280`
- `python iclr_analysis.py --num_reviews 500 --batch_size 100 --num_fs_examples 1 --num_reflections 5 --temperature 0.1 --num_reviews_ensemble 5` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L281`
- `@article{lu2024aiscientist,` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L326`
- `title={The {AI} {S}cientist: Towards Fully Automated Open-Ended Scientific Discovery},` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L327`
- `author={Lu, Chris and Lu, Cong and Lange, Robert Tjarko and Foerster, Jakob and Clune, Jeff and Ha, David},` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L328`
- `journal={arXiv preprint arXiv:2408.06292},` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L329`
- `year={2024}` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L330`
- `}` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L331`
- `# Endpoint Script` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L377`
- `docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -v `pwd`/templates:/app/AI-Scientist/templates <AI_SCIENTIST_IMAGE> \` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L378`
- `--model gpt-4o-2024-05-13 \` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L379`
- `--experiment 2d_diffusion \` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L380`
- `--num-ideas 2` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L381`
- `# Interactive` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L385`
- `docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY \` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L386`
- `--entrypoint /bin/bash \` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L387`
- `<AI_SCIENTIST_IMAGE>` — `repo://SakanaAI/AI-Scientist@1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md#L388`

Commands are syntactically extracted and unverified.
