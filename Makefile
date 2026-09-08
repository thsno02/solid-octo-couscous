PYTHON ?= python3
MATERIALIZATION_CONFIG ?= pipeline/materialization.yaml

.PHONY: materialize validate validate-raw validate-materialized validate-docs

materialize:
	$(PYTHON) scripts/preflight_legacy_metadata.py
	$(PYTHON) scripts/materialize_resilient_runner.py --config $(MATERIALIZATION_CONFIG)
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
