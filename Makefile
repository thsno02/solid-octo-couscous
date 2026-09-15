PYTHON ?= python3
MATERIALIZATION_CONFIG ?= pipeline/materialization_all_260910.yaml
EXPERIMENT ?= experiments/v0_meta_kb_initialization_demo_260910
TEST_SCRIPTS := $(sort $(wildcard tests/test_*.py) $(wildcard scripts/test_*.py) $(wildcard $(EXPERIMENT)/pipeline/test_*.py))

.PHONY: materialize materialize-all demo build-demo validate-demo build-wiki validate-wiki validate validate-raw validate-materialized validate-materialization validate-docs test reproducibility

# Recursive sub-makes preserve this destructive pipeline order even with `make -j`.
materialize:
	$(MAKE) materialize-all
	$(MAKE) demo
	$(MAKE) validate

materialize-all:
	$(PYTHON) scripts/materialize_all_sources.py --config $(MATERIALIZATION_CONFIG)

build-demo:
	$(PYTHON) $(EXPERIMENT)/pipeline/build_demo.py

validate-demo:
	$(PYTHON) $(EXPERIMENT)/pipeline/validate_demo.py

build-wiki:
	$(PYTHON) $(EXPERIMENT)/pipeline/build_llm_wiki.py

validate-wiki: validate-demo
	$(PYTHON) $(EXPERIMENT)/pipeline/validate_llm_wiki.py

demo:
	$(MAKE) build-demo
	$(MAKE) validate-demo
	$(MAKE) build-wiki
	$(MAKE) validate-wiki

validate: validate-raw validate-materialization validate-docs validate-wiki

validate-raw:
	$(PYTHON) scripts/validate_raw_data.py

validate-materialization:
	$(PYTHON) scripts/validate_materialization_completeness.py

validate-materialized: validate-materialization

validate-docs:
	$(PYTHON) scripts/validate_docs.py

test:
	@set -e; for test_file in $(TEST_SCRIPTS); do $(PYTHON) "$$test_file"; done

reproducibility:
	$(PYTHON) scripts/verify_demo_reproducibility.py
