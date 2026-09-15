# Repository semantic capsule: materialsproject/atomate2

- Commit: `b7eadba7b937f0116cfc6b2f2ed92a0d2968c310`
- Default branch: `main`
- Description: atomate2
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# atomate2

[![tests](https://img.shields.io/github/actions/workflow/status/materialsproject/atomate2/testing.yml?branch=main&label=tests)](https://github.com/materialsproject/atomate2/actions?query=workflow%3Atesting)
[![code coverage](https://img.shields.io/codecov/c/gh/materialsproject/atomate2)](https://codecov.io/gh/materialsproject/atomate2)
[![pypi version](https://img.shields.io/pypi/v/atomate2?color=blue)](https://pypi.org/project/atomate2)
![supported python versions](https://img.shields.io/pypi/pyversions/atomate2)
[![Zenodo](https://img.shields.io/badge/DOI-10.5281/zenodo.10677080-blue?logo=Zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.15603088)
[![This project supports Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org/downloads)
[![PyPI](https://img.shields.io/pypi/dm/atomate2.svg?maxAge=2592000)](https://pypi.python.org/pypi/atomate2)

[Documentation][docs] | [PyPI][pypi] | [GitHub][github]

Atomate2 is a free, open-source software for performing complex materials science
workflows using simple Python functions. Features of atomate2 include

- It is built on open-source libraries: [pymatgen], [custodian], [jobflow], and
  [jobflow-remote] or [FireWorks].
- A library of "standard" workflows to compute a wide variety of desired materials
  properties.
- The ability scale from a single material, to 100 materials, or 100,000 materials.
- Easy routes to modifying and chaining workflows together.
- It can build large databases of output properties that you can query, analyze, and
  share in a systematic way.
- It automatically keeps meticulous records of jobs, their directories, runtime
  parameters, and more.

## Workflows

Some of the workflows available in atomate2 are:

- electronic band structures
- elastic, dielectric, and piezoelectric tensors
- one-shot electron-phonon interactions
- electronic transport using [AMSET]
- phonons using [phonopy]
- defect formation energy diagrams
- [Lobster] bonding analysis with [lobsterpy]

It is easy to customise and compose any of the above workflows.

## Quick start

Workflows in atomate2 are written using the [jobflow] library. Workflows are generated using
`Maker` objects which have a consistent API for modifying input settings and chaining
workflows together. Below, we demonstrate how to run a band structure workflow
(see the [documentation][RelaxBandStructure] for more details). In total, 4 VASP
calculations will be performed:

1. A structural optimisation.
2. A self-consistent static calculation on the relaxed geometry.
3. A non-self-consistent calculation on a uniform k-point mesh (for the density of
   states).
4. A non-self-consistent calculation on a high symmetry k-point path (for the line mode
   band structure).

```py
from atomate2.vasp.flows.core import RelaxBandStructureMaker
from jobflow import run_locally
from pymatgen.core import Structure

# construct a rock salt MgO structure
mgo_structure = Structure(
    lattice=[[0, 2.13, 2.13], [2.13, 0, 2.13], [2.13, 2.13, 0]],
    species=["Mg", "O"],
    coords=[[0, 0, 0], [0.5, 0.5, 0.5]],
)

# make a band structure flow to optimise the structure and obtain the band structure
bandstructure_flow = RelaxBandStructureMaker().make(mgo_structure)

# run the flow
run_locally(bandstructure_flow, create_folders=True)
```

Before the above code can run successfully, you'll need to

- tell pymatgen where to [find your pseudopotential files](https://pymatgen.org/installation.html#potcar-setup)
- tell atomate2 where to find your VASP binary
- (optionally) prepare an external database to store the job output

See the [installation] steps for details how to set all of this up.

In this example, we execute the workflow immediately. In many cases, you might want
to perform calculations on several materials simultaneously. To achieve this, all
atomate2 workflows can be run using the [jobflow-remote] or [FireWorks] software. See the
[jobflow-remote-specific documentation][atomate2-jobflow-remote] or [fireworks-specific documentation][atomate2_fireworks] for more details.

## Installation

Atomate2 is a Python 3.10+ library and can be installed using pip. Full installation
and configuration instructions are provided in the [installation tutorial][installation].

## Tutorials

The documentation includes comprehensive tutorials and reference information to get you
started:

- [Introduction to running workflows][running-workflows]
- [Using atomate2 with FireWorks][atomate2_fireworks]
- [Overview of key concepts][key-concepts]
- [List of VASP workflows][vasp_workflows]
- [Executable tutorials for different workflows][tutorials]

In March 2025, the first dedicated school on atomate2 (including the workflow language jobflow and the workflow manager jobflow-remote) took place, and one can access the video material here:

- [Jobflow and Jobflow-remote][videotutorial1]
- [atomate2][videotutorial2]
- [Advanced Workflows in atomate2: Part 1][videotutorial3]
- [Advanced Workflows in atomate2: Part 2][videotutorial4]

## Need help?

Ask questions about atomate2 on the [atomate2 support forum][help-forum].
If you've found an issue with atomate2, please submit a bug report on [GitHub Issues][issues].

## What’s new?

Track changes to atomate2 through the [changelog][changelog].

## Contributing

We greatly appreciate any contributions in the form of a pull request.
Additional information on contributing to atomate2 can be found [here][contributing].
We maintain a list of all contributors [here][contributors].

## License

Atomate2 is released under a modified BSD license; the full text can be found [here][license].

## Acknowledgements

The development of atomate2 has benefited from many people across several research groups.
A full list of contributors can be found [here][contributors].

## Citing atomate2

If you use atomate2, please cite the [following article](https://doi.org/10.1039/D5DD00019J):

```bib
@article{ganose2025_atomate2,
	title = {Atomate2: modular workflows for materials science},
	author = {Ganose, Alex M. and Sahasrabuddhe, Hrushikesh and Asta, Mark and Beck, Kevin and Biswas, Tathagata and Bonkowski, Alexander and Bustamante, Joana and Chen, Xin and Chiang, Yuan and Chrzan, Daryl C. and Clary, Jacob and Cohen, Orion A. and Ertural, Christina and Gallant, Max C. and George, Janine and Gerits, Sophie and Goodall, Rhys E. A. and Guha, Rishabh D. and Hautier, Geoffroy and Horton, Matthew and Inizan, T. J. and Kaplan, Aaron D. and Kingsbury, Ryan S. and Kuner, Matthew C. and Li, Bryant and Linn, Xavier and McDermott, Matthew J. and Mohanakrishnan, Rohith Srinivaas and Naik, Aakash A. and Neaton, Jeffrey B. and Parmar, Shehan M. and Persson, Kristin A. and Petretto, Guido and Purcell, Thomas A. R. and Ricci, Francesco and Rich, Benjamin and Riebesell, Janosh and Rignanese, Gian-Marco and Rosen, Andrew S. and Scheffler, Matthias and Schmidt, Jonathan and Shen, Jimmy-Xuan and Sobolev, Andrei and Sundararaman, Ravishankar and Tezak, Cooper and Trinquet, Victor and Varley, Joel B. and Vigil-Fowler, Derek and Wang, Duo and Waroquiers, David and Wen, Mingjian and Yang, Han and Zheng, Hui and Zheng, Jiongzhi and Zhu, Zhuoying and Jain, Anubhav},
	year = {2025},
	journal = {Digital Discovery},
	doi = {10.1039/D5DD00019J},
	url = {https://doi.org/10.1039/D5DD00019J},
	urldate = {2025-07-01},
}
```
## Journal publications for new contributions to atomate2?
We have published the initial publication on atomate2 in Digital Discovery. New additions to atomate2 can be published within a [https://pubs.rsc.org/dd/article/4/2/301/846290/Commit-Mini-article-for-dynamic-reporting-of](Commit) independent of the previous authors.

We are of course happy to mention and link such Commits in our Readme, the documentation or at relevant parts in the code.

[pymatgen]: https://pymatgen.org
[fireworks]: https://materialsproject.github.io/fireworks/
[jobflow]: https://materialsproject.github.io/jobflow/
[jobflow-remote]: https://github.com/Matgenix/jobflow-remote
[custodian]: https://materialsproject.github.io/custodian/
[VASP]: https://www.vasp.at
[AMSET]: https://hackingmaterials.lbl.gov/amset/
[help-forum]: https://matsci.org/c/atomate
[issues]: https://github.com/materialsproject/atomate2/issues
[changelog]: https://materialsproject.github.io/atomate2/about/changelog.html
[installation]: https://materialsproject.github.io/atomate2/user/install.html
[contributing]: https://materialsproject.github.io/atomate2/about/contributing.html
[contributors]: https://materialsproject.github.io/atomate2/about/contributors.html
[license]: https://raw.githubusercontent.com/materialsproject/atomate2/main/LICENSE
[running-workflows]: https://materialsproject.github.io/atomate2/user/running-workflows.html
[key-concepts]: https://materialsproject.github.io/atomate2/user/key_concepts_overview.html#key-concepts-in-atomate2-job-flow-makers-inputset-taskdocument-and-builder
[atomate2_fireworks]: https://materialsproject.github.io/atomate2/user/fireworks.html
[atomate2-jobflow-remote]: https://materialsproject.github.io/atomate2/user/jobflow-remote.html
[vasp_workflows]: https://materialsproject.github.io/atomate2/user/codes/vasp.html
[tutorials]: https://materialsproject.github.io/atomate2/tutorials/tutorials.html
[RelaxBandStructure]: https://materialsproject.github.io/atomate2/user/codes/vasp.html#relax-and-band-structure
[Lobster]: http://www.cohp.de
[lobsterpy]: https://github.com/JaGeo/LobsterPy
[phonopy]: https://github.com/phonopy/phonopy
[docs]: https://materialsproject.github.io/atomate2/
[github]: https://github.com/materialsproject/atomate2
[pypi]: https://pypi.org/project/atomate2
[videotutorial1]: https://lhumos.org/collection/0/680bb4d7e4b0f0d2028027ce
[videotutorial2]: https://lhumos.org/collection/0/680bb4d3e4b0f0d2028027c9
[videotutorial3]: https://lhumos.org/collection/0/680bb4d0e4b0f0d2028027c5
[videotutorial4]: https://lhumos.org/collection/0/680bb4c7e4b0f0d2028027c1

## `CONTRIBUTING.md`

# Contributing to atomate2

We love your input! We want to make contributing as easy and
transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing or implementing new features
- Becoming a maintainer

## Reporting bugs, getting help, and discussion

atomate2 is still in development, so at the moment we
do not have a dedicated help forum. For the time being, please
submit questions and bugs to the
[GitHub issues page](https://github.com/materialsproject/atomate2/issues).

If you are making a bug report, incorporate as many elements of the
following as possible to ensure a timely response and avoid the
need for followups:

- A quick summary and/or background.
- Steps to reproduce - be specific! **Provide sample code.**
- What you expected would happen, compared to what actually happens.
- The full stack trace of any errors you encounter.
- Notes (possibly including why you think this might be happening,
  or steps you tried that didn't work).

We love thorough bug reports as this means the development team can
make quick and meaningful fixes. When we confirm your bug report,
we'll move it to the GitHub issues where its progress can be
further tracked.

## Contributing code modifications or additions through GitHub

We use GitHub to host code, to track issues and feature requests,
as well as accept pull requests. We maintain a list of all
contributors [here](https://materialsproject.github.io/atomate2/contributors.html).

Pull requests are the best way to propose changes to the codebase.
Follow the [GitHub flow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
for more information on this procedure.

The basic procedure for making a PR is:

- Fork the repo and create your branch from master.
- Commit your improvements to your branch and push to your GitHub fork (repo).
- When you're finished, go to your fork and make a Pull Request. It will
  automatically update if you need to make further changes.

## How to Make a Great Pull Request

We have a few tips for writing good PRs that are accepted into the main repo:

- Use the Numpy Code style for all of your code. Find an example [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy).
- Your code should have (4) spaces instead of tabs.
- If needed, update the documentation.
- **Write tests** for new features! Good tests are 100%, absolutely necessary
  for good code. We use the python `pytest` framework -- see some of the
  other tests in this repo for examples, or review the [Hitchhiker's guide
  to python](https://docs.python-guide.org/writing/tests) for some good
  resources on writing good tests.
- Understand your contributions will fall under the same license as this repo.

When you submit your PR, our CI service will automatically run your tests.
We welcome good discussion on the best ways to write your code, and the comments
on your PR are an excellent area for discussion.

## `pyproject.toml`

[build-system]
requires = ["setuptools >= 42, < 85", "versioningit >= 1,< 4", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "atomate2"
description = "atomate2 is a library of materials science workflows"
readme = "README.md"
keywords = ["automated", "dft", "high-throughput", "vasp", "workflow"]
license = "BSD-3-Clause-LBNL"
authors = [{ name = "Alex Ganose", email = "alexganose@gmail.com" }]
dynamic = ["version"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "Intended Audience :: System Administrators",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Other/Nonlisted Topic",
    "Topic :: Scientific/Engineering",
]
requires-python = ">=3.11"
dependencies = [
    "PyYAML",
    "click",
    "custodian>=2024.4.18",
    "emmet-core>=0.86.1",
    "jobflow>=0.1.11",
    "monty>=2024.12.10",
    "numpy",
    "pydantic-settings>=2.0.3",
    "pydantic>=2.0.1",
    "pymatgen>=2024.11.13",
    "pymatgen-core>=2026.5.18",
    "pymongo<=4.18.0",
]

[project.optional-dependencies]
abinit = [
    "abipy>=0.9.3",
    "netCDF4<1.7.5", # TODO: latest NetCDF missing 3.12 support: https://github.com/Unidata/netcdf4-python/issues/1461
]
aims = ["pymatgen-io-aims>=0.0.5", "pymatgen>=2025.10.7"]
amset = ["amset>=0.4.15", "pydash"]
cclib = ["cclib>=1.8.1"]
mp = ["mp-api>=0.37.5"]
# phonopy 4.x changed force-constants/primitive-axis handling, breaking the
# phonon.save -> phonopy.load round-trip used by the Grüneisen workflow
# ("Force constants shape disagrees with crystal structure setting").
phonons = ["phonopy>=2.43.6,<5", "seekpath>=2.0.0"]
lobster = ["ijson>=3.2.2", "lobsterpy>=0.6.0"]
defects = [
    "dscribe>=1.2.0",
    "pymatgen-analysis-defects>=2024.5.11",
    "python-ulid>=2.7",
]

ase = ["ase>=3.26.0"]
ase-ext = ["tblite>=0.3.0; platform_system=='Linux'"]
forcefields-demo = ["chgnet>=0.3.8","atomate2[ase]"]

torchsim = [
    "torch-sim-atomistic[symmetry]==0.6.0; python_version >= '3.12'"
]
jdftx = ["pymatgen==2026.5.4"]
approxneb = ["pymatgen-analysis-diffusion>=2024.7.15"]
openmm = [
    "mdanalysis>=2.8.0",
    "openmm-mdanalysis-reporter>=0.1.0",
    "openmm>=8.1.0",
]
fireworks = ["fireworks==2.1.4"]
strict-openff = [
    "mdanalysis==2.10.0",
    "monty==2026.7.16",
    "openmm-mdanalysis-reporter==0.1.0",
    "openmm==8.6.0",
    "pymatgen==2026.5.4", # EXERCISE CAUTION WHEN UPDATING - open ff is extremely sensitive to pymatgen version
]

# Forcefields have separate strict groupings because of conflicting dependencies.
# The labels below should not be taken as fixed in time.
# They are meant to be instructive as to why certain forcefields are grouped together.
# Ex: `strict-forcefields-torch-limited` might indicate that these require a lower version of `pytorch`
# Whereas `strict-forcefields-generic` might indicate that no dependency conflicts are known for the group

# ALWAYS REMEMBER to update `.github/workflows/testing.yml` to reflect the current set of
# forcefield dependency groups.
strict-forcefields-generic = [
    "calorine==3.5; python_version >= '3.12'",
    "calorine==3.1; python_version < '3.12'",
    "chgnet==0.4.2",
    "quippy-ase==0.10.3",
    "sevenn==0.13.0",
    "deepmd-kit==3.2.0",
    "tensorflow-cpu==2.21.0; sys_platform == 'linux'",
    "tensorflow==2.21.0; sys_platform == 'darwin' or sys_platform == 'win32'",
#     "mattersim>=1.2.3", # need to be activated again
    "wandb==0.29.0", # required for mattersim
    "upet==0.2.5",
]
strict-forcefields-torch-limited = [
    "matgl==4.0.3",
    "nequip==0.19.1", # requires numpy<2 because of matscipy
]

strict-forcefields-e3nn-limited = [
    "mace-torch==0.3.16",
    "torch-dftd==0.5.3",
]
strict-forcefields-numpy-limited = [
    "nequip-allegro==0.8.3",
]

strict = [
    "atomate2[cclib, phonons, lobster, openmm, mp, defects, ase, ase-ext]",
    "numpy<3.0",
    "numba>=0.60.0", # needed to get numpy >2,<3 installed
    "pymatgen==2026.5.4",
    "pymatgen-core==2026.8.30",
]

[project.scripts]
atm = "atomate2.cli:cli"

[project.urls]
homepage = "https://materialsproject.github.io/atomate2/"
repository = "https://github.com/materialsproject/atomate2"
documentation = "https://materialsproject.github.io/atomate2/"
changelog = "https://github.com/materialsproject/atomate2/blob/main/CHANGELOG.md"

[dependency-groups]
dev = ["pre-commit>=4.5.1"]
tests = [
    "fireworks==2.1.4",
    "nbmake==1.5.5",
    "pytest-cov==7.1.0",
    "pytest-mock==3.15.1",
    "pytest-split==0.11.0",
    "pytest-xdist==3.8.0",
    "pytest==9.1.1",
]
docs = [
    "fireworks==2.1.4",
    "autodoc_pydantic==2.2.0",
    "furo==2025.12.19",
    "ipython==9.17.1",
    "jsonschema[format]",
    "myst_parser==5.1.0",
    "numpydoc==1.10.0",
    "sphinx-copybutton==0.5.2",
    "sphinx==9.0.4",
    "sphinx_design==0.7.0",
    "jupyterlab==4.6.3",
]

[tool.setuptools.package-data]
atomate2 = ["py.typed"]
"atomate2.vasp.sets" = ["*.yaml"]
"atomate2.cp2k.sets" = ["*.yaml"]
"atomate2.cp2k.schemas.calc_types" = ["*.yaml"]
"atomate2.jdftx.sets" = ["*.yaml"]

[tool.versioningit.vcs]
method = "git"
default-tag = "0.0.1"

[tool.mypy]
ignore_missing_imports = true
no_strict_optional = true

[tool.pytest.ini_options]
addopts = "-p no:warnings --import-mode=importlib --cov-config=pyproject.toml"
filterwarnings = [
    "ignore:.*POTCAR.*:UserWarning",
    "ignore:.*input structure.*:UserWarning",
    "ignore:.*is not gzipped.*:UserWarning",
    "ignore:.*magmom.*:UserWarning",
    "ignore::DeprecationWarning",
]

[tool.coverage.run]
include = ["src/*"]
parallel = true
branch = true

[tool.coverage.paths]
source = ["src/"]

[tool.coverage.report]
skip_covered = true
show_missing = true
exclude_lines = [
    '^\s*@overload( |$)',
    '^\s*assert False(,|$)',
    'if typing.TYPE_CHECKING:',
    'if TYPE_CHECKING:',
]

[tool.ruff]
target-version = "py310"
output-format = "concise"

[tool.ruff.lint]
select = ["ALL"]
ignore = [
    "ANN002",  # Missing type annotation for *arg
    "ANN003",  # Missing type annotation for **kwargs
    "ANN401",  # typing.Any disallowed
    "ARG002",  # unused method argument
    "C408",    # Unnecessary (dict/list/tuple) call - remove call
    "C901",    # function too complex
    "COM812",  # trailing comma missing
    "CPY001",  # copyright notice at top of file
    "EM",      # exception message must not use f-string literal
    "ERA001",  # found commented out code

## `docs/index.md`

```{toctree}
:caption: User Guide
:hidden:
user/index
user/install
user/running-workflows
user/key_concepts_overview
user/docs-schemas-emmet
user/jobflow-remote
user/fireworks
user/atomate-1-vs-2
user/codes/index
user/addons
tutorials/tutorials
```

```{toctree}
:caption: Reference
:hidden:
reference/index
```

```{toctree}
:caption: Developer Guide
:hidden:
dev/dev_install
dev/workflow_tutorial
dev/vasp_tests
dev/abinit_tests
dev/forcefields
```

```{toctree}
:caption: About
:hidden:
about/changelog
about/contributors
about/contributing
about/license
```

# atomate2 documentation

**Date**: {sub-ref}`today`

**Useful links**:
[Source Repository](https://github.com/materialsproject/atomate2) |
[Issues & Ideas](https://github.com/materialsproject/atomate2/issues) |
[Q&A Support](https://matsci.org/c/atomate)

Atomate2 is an open-source library providing computational workflows for
automating first-principles calculations.

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: user/index
:link-type: doc
:class-header: bg-light
**User Guide** 🚀
^^^
The user guide provides in-depth information and tutorials for using *atomate2*.
:::

:::{grid-item-card}
:link: https://matsci.org/c/atomate
:class-header: bg-light
**Support forum** ✨
^^^
You've read the user guide but still need help? Ask questions on the atomate2
support forum.
:::

:::{grid-item-card}
:link: reference/index
:link-type: doc
:class-header: bg-light
**API reference** 📖
^^^
The reference guide contains a detailed description of the *atomate2* API. It
assumes that you have an understanding of the key concepts.
:::

:::{grid-item-card}
:link: dev/dev_install
:link-type: doc
:class-header: bg-light
**Developer guide** 👩‍💻
^^^
Do you want to develop your own workflows or improve existing functionalities?
Check out the developer guide.
:::
::::
