# Architecture evidence: bluesky/bluesky

- `README.md:6` — Bluesky — An Experiment Specification & Orchestration Engine
- `Dockerfile:1` — The devcontainer should use the developer target and run as root with podman
- `Dockerfile:2` — or docker with user namespaces.
- `Dockerfile:6` — Add any system dependencies for the developer/build environment here
- `Dockerfile:12` — Set up a virtual environment and put it in PATH
- `pyproject.toml:126` — Run pytest with all our checkers, and don't spam us with massive tracebacks on error
- `pyproject.toml:127` — Don't collect the interactive directory which is intended for manual execution
- `pyproject.toml:131` — https://iscinumpy.gitlab.io/post/bound-version-constraints/#watch-for-warnings
- `pyproject.toml:138` — Doctest python code in docs, python code in src docstrings, test functions in tests
- `pyproject.toml:148` — Tests are run from installed location, map back to the src directory
- `pyproject.toml:151` — tox must currently be configured via an embedded ini string
- `pyproject.toml:152` — See: https://github.com/tox-dev/tox/issues/999
- `pyproject.toml:180` — By default, private member access is allowed in tests
- `pyproject.toml:181` — See https://github.com/DiamondLightSource/python-copier-template/issues/154
- `pyproject.toml:182` — Remove this line to forbid private member access in tests
- `pyproject.toml:202` — Don't create a virtualenv for the command, requires tox-direct plugin
