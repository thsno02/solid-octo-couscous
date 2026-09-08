PYTHON ?= python3
MATERIALIZATION_CONFIG ?= pipeline/materialization.yaml
ARXIV_WORKERS ?= 2
GITHUB_WORKERS ?= 3

.PHONY: materialize validate validate-raw validate-materialized validate-docs

materialize:
	$(PYTHON) scripts/preflight_legacy_metadata.py
	$(PYTHON) scripts/materialize_parallel.py --config $(MATERIALIZATION_CONFIG) --arxiv-workers $(ARXIV_WORKERS) --github-workers $(GITHUB_WORKERS)
	$(PYTHON) scripts/pin_materialized_selectors.py
	$(PYTHON) scripts/register_materialization.py
	$(MAKE) validate

validate: validate-raw validate-materialized validate-docs

validate-raw:
	$(PYTHON) scripts/validate_raw_data.py

validate-materialized:
	$(PYTHON) scripts/validate_materialized.py

validate-docs:
	$(PYTHON) scripts/validate_docs.py
