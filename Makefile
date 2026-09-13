PYTHON ?= python3
MATERIALIZATION_CONFIG ?= pipeline/materialization_all_260910.yaml
EXPERIMENT ?= experiments/v0_meta_kb_initialization_demo_260910

.PHONY: materialize materialize-all build-demo validate validate-raw validate-materialized validate-materialization validate-docs validate-demo

materialize: materialize-all build-demo validate

materialize-all:
	$(PYTHON) scripts/materialize_all_sources.py --config $(MATERIALIZATION_CONFIG)

build-demo:
	$(PYTHON) $(EXPERIMENT)/pipeline/build_demo.py

validate: validate-raw validate-materialization validate-docs validate-demo

validate-raw:
	$(PYTHON) scripts/validate_raw_data.py

validate-materialization:
	$(PYTHON) scripts/validate_materialization_completeness.py

validate-materialized: validate-materialization

validate-docs:
	$(PYTHON) scripts/validate_docs.py

validate-demo:
	$(PYTHON) $(EXPERIMENT)/pipeline/validate_demo.py
