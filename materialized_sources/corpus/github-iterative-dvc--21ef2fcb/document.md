# Repository semantic capsule: iterative/dvc

- Commit: `56e59829512ff134aa269099a2099587b810b4dd`
- Default branch: `main`
- Description: DVC
- Selected evidence files: 3 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.rst`

|Banner|

`Website <https://dvc.org>`_
• `Docs <https://dvc.org/doc>`_
• `Blog <http://blog.dataversioncontrol.com>`_
• `Tutorial <https://dvc.org/doc/get-started>`_
• `Related Technologies <https://dvc.org/doc/user-guide/related-technologies>`_
• `How DVC works`_
• `VS Code Extension`_
• `Installation`_
• `Contributing`_
• `Community and Support`_

|CI| |Python Version| |Coverage| |VS Code| |DOI|

|PyPI| |PyPI Downloads| |Packages| |Brew| |Conda| |Choco| |Snap|

|

**Data Version Control** or **DVC** is a command line tool and `VS Code Extension`_ to help you develop reproducible machine learning projects:

#. **Version** your data and models.
   Store them in your cloud storage but keep their version info in your Git repo.

#. **Iterate** fast with lightweight pipelines.
   When you make changes, only run the steps impacted by those changes.

#. **Track** experiments in your local Git repo (no servers needed).

#. **Compare** any data, code, parameters, model, or performance plots.

#. **Share** experiments and automatically reproduce anyone's experiment.

Quick start
===========

    Please read our `Command Reference <https://dvc.org/doc/command-reference>`_ for a complete list.

A common CLI workflow includes:


+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Task                              | Terminal                                                                                           |
+===================================+====================================================================================================+
| Track data                        | | ``$ git add train.py params.yaml``                                                               |
|                                   | | ``$ dvc add images/``                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Connect code and data             | | ``$ dvc stage add -n featurize -d images/ -o features/ python featurize.py``                     |
|                                   | | ``$ dvc stage add -n train -d features/ -d train.py -o model.p -M metrics.json python train.py`` |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Make changes and experiment       | | ``$ dvc exp run -n exp-baseline``                                                                |
|                                   | | ``$ vi train.py``                                                                                |
|                                   | | ``$ dvc exp run -n exp-code-change``                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Compare and select experiments    | | ``$ dvc exp show``                                                                               |
|                                   | | ``$ dvc exp apply exp-baseline``                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share code                        | | ``$ git add .``                                                                                  |
|                                   | | ``$ git commit -m 'The baseline model'``                                                         |
|                                   | | ``$ git push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share data and ML models          | | ``$ dvc remote add myremote -d s3://mybucket/image_cnn``                                         |
|                                   | | ``$ dvc push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+

How DVC works
=============

    We encourage you to read our `Get Started
    <https://dvc.org/doc/get-started>`_ docs to better understand what DVC
    does and how it can fit your scenarios.

The closest *analogies* to describe the main DVC features are these:

#. **Git for data**: Store and share data artifacts (like Git-LFS but without a server) and models, connecting them with a Git repository. Data management meets GitOps!
#. **Makefiles** for ML: Describes how data or model artifacts are built from other data and code in a standard format. Now you can version your data pipelines with Git.
#. Local **experiment tracking**: Turn your machine into an ML experiment management platform, and collaborate with others using existing Git hosting (Github, Gitlab, etc.).

Git is employed as usual to store and version code (including DVC meta-files as placeholders for data).
DVC `stores data and model files <https://dvc.org/doc/start/data-management>`_ seamlessly in a cache outside of Git, while preserving almost the same user experience as if they were in the repo.
To share and back up the *data cache*, DVC supports multiple remote storage platforms - any cloud (S3, Azure, Google Cloud, etc.) or on-premise network storage (via SSH, for example).

|Flowchart|

`DVC pipelines <https://dvc.org/doc/start/data-management/data-pipelines>`_ (computational graphs) connect code and data together.
They specify all steps required to produce a model: input dependencies including code, data, commands to run; and output information to be saved.

Last but not least, `DVC Experiment Versioning <https://dvc.org/doc/start/experiments>`_ lets you prepare and run a large number of experiments.
Their results can be filtered and compared based on hyperparameters and metrics, and visualized with multiple plots.

.. _`VS Code Extension`:

VS Code Extension
=================

|VS Code|

To use DVC as a GUI right from your VS Code IDE, install the `DVC Extension <https://marketplace.visualstudio.com/items?itemName=Iterative.dvc>`_ from the Marketplace.
It currently features experiment tracking and data management, and more features (data pipeline support, etc.) are coming soon!

|VS Code Extension Overview|

    Note: You'll have to install core DVC on your system separately (as detailed
    below). The Extension will guide you if needed.

Installation
============

There are several ways to install DVC: in VS Code; using ``snap``, ``choco``, ``brew``, ``conda``, ``pip``; or with an OS-specific package.
Full instructions are `available here <https://dvc.org/doc/get-started/install>`_.

Snapcraft (Linux)
-----------------

|Snap|

.. code-block:: bash

   snap install dvc --classic

This corresponds to the latest tagged release.
Add ``--beta`` for the latest tagged release candidate, or ``--edge`` for the latest ``main`` version.

Chocolatey (Windows)
--------------------

|Choco|

.. code-block:: bash

   choco install dvc

Brew (mac OS)
-------------

|Brew|

.. code-block:: bash

   brew install dvc

Anaconda (Any platform)
-----------------------

|Conda|

.. code-block:: bash

   conda install -c conda-forge mamba # installs much faster than conda
   mamba install -c conda-forge dvc

Depending on the remote storage type you plan to use to keep and share your data, you might need to install optional dependencies: `dvc-s3`, `dvc-azure`, `dvc-gdrive`, `dvc-gs`, `dvc-oss`, `dvc-ssh`.

PyPI (Python)
-------------

|PyPI|

.. code-block:: bash

   pip install dvc

Depending on the remote storage type you plan to use to keep and share your data, you might need to specify one of the optional dependencies: ``s3``, ``gs``, ``azure``, ``oss``, ``ssh``. Or ``all`` to include them all.
The command should look like this: ``pip install 'dvc[s3]'`` (in this case AWS S3 dependencies such as ``boto3`` will be installed automatically).

To install the development version, run:

.. code-block:: bash

   pip install "dvc @ git+https://github.com/treeverse/dvc"

Package (Platform-specific)
---------------------------

|Packages|

Self-contained packages for Linux, Windows, and Mac are available.
The latest version of the packages can be found on the GitHub `releases page <https://github.com/treeverse/dvc/releases>`_.

Ubuntu / Debian (deb)
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
   wget -qO - https://dvc.org/deb/iterative.asc | sudo apt-key add -
   sudo apt update
   sudo apt install dvc

Fedora / CentOS (rpm)
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   sudo wget https://dvc.org/rpm/dvc.repo -O /etc/yum.repos.d/dvc.repo
   sudo rpm --import https://dvc.org/rpm/iterative.asc
   sudo yum update
   sudo yum install dvc

Contributing
============

Contributions are welcome!
Please see our `Contributing Guide <https://dvc.org/doc/user-guide/contributing/core>`_ for more details.
Thanks to all our contributors!

|Contribs|

Community and Support
=====================

* `Twitter <https://twitter.com/DVCorg>`_
* `Forum <https://discuss.dvc.org/>`_
* `Discord Chat <https://dvc.org/chat>`_
* `Email <mailto:support@dvc.org>`_
* `Mailing List <https://dvc.org/community#subscribe>`_

Copyright
=========

This project is distributed under the Apache license version 2.0 (see the LICENSE file in the project root).


## `CONTRIBUTING.md`

### See our contribution guide at [dvc.org](https://dvc.org/doc/user-guide/contributing/core).

## `pyproject.toml`

[build-system]
build-backend = "setuptools.build_meta"
requires = ["setuptools>=77", "setuptools_scm[toml]>=8"]

[project]
name = "dvc"
description = "Git for data scientists - manage your code and data together"
readme = "README.rst"
keywords = [
    "ai",
    "collaboration",
    "data-science",
    "data-version-control",
    "developer-tools",
    "git",
    "machine-learning",
    "reproducibility",
]
license = "Apache-2.0"
license-files = ["LICENSE"]
maintainers = [{ name = "Treeverse", email = "support@dvc.org" }]
authors = [{ name = "Dmitry Petrov", email = "dmitry@dvc.org" }]
requires-python = ">=3.9"
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
]
dynamic = ["version"]

dependencies = [
    "attrs>=22.2.0",
    "celery",
    "colorama>=0.3.9",
    "configobj>=5.0.9",
    "distro>=1.3",
    "dpath<3,>=2.1.0",
    "dulwich",
    "dvc-data>=3.18.2,<3.19.0",
    "dvc-http>=2.29.0",
    "dvc-objects",
    "dvc-render>=1.0.1,<2",
    "dvc-studio-client>=0.21,<1",
    "dvc-task>=0.3.0,<1",
    "flatten-dict<1,>=0.4.1",
    "flufl.lock>=8.1.0,<10",
    "fsspec>=2024.2.0",
    "funcy>=1.14",
    "grandalf<1,>=0.7",
    "gto>=1.6.0,<2",
    "hydra-core>=1.1",
    "iterative-telemetry>=0.0.7",
    "kombu",
    "networkx>=2.5",
    "omegaconf",
    "packaging>=19",
    "pathspec>=0.10.3,<2",
    "platformdirs<5,>=3.1.1",
    "psutil>=5.8",
    "pydot>=1.2.4",
    "pygtrie>=2.3.2",
    "pyparsing>=3.0.0",
    "requests>=2.22",
    "rich>=12",
    "ruamel.yaml>=0.17.11",
    "scmrepo>=3.5.2,<4",
    "shortuuid>=0.5",
    "shtab<2,>=1.3.4",
    "tabulate>=0.8.7",
    "tomlkit>=0.11.1",
    "tqdm<5,>=4.63.1",
    "voluptuous>=0.11.7",
    "zc.lockfile>=1.2.1",
]

[project.optional-dependencies]
all = ["dvc[azure,gdrive,gs,hdfs,oss,s3,ssh,webdav,webhdfs]"]
azure = ["dvc-azure>=3.1.0,<4"]
dev = ["dvc[azure,gdrive,gs,hdfs,lint,oss,s3,ssh,tests,webdav,webhdfs]"]
gdrive = ["dvc-gdrive>=3,<4"]
gs = ["dvc-gs>=3.0.2,<4"]
hdfs = ["dvc-hdfs>=3,<4"]
lint = [
    "mypy==1.19.1",
    "pandas-stubs",
    "types-colorama",
    "types-psutil",
    "types-pyinstaller",
    "types-requests",
    "types-tabulate",
    "types-toml",
    "types-tqdm",
    "typing-extensions",
]
oss = ["dvc-oss>=3,<4"]
s3 = ["dvc-s3>=3.2.1,<4"]
ssh = ["dvc-ssh>=4,<5"]
ssh_gssapi = ["dvc-ssh[gssapi]>=4,<5"]
testing = [
  "pytest-benchmark[histogram]>=5,<6",
  "uv",
]
tests = [
    "dvc[testing]",
    "beautifulsoup4>=4.4",
    "dvc-ssh",
    "filelock",
    "pytest>=7,<10",
    "pytest-rerunfailures<17.0",
    "pytest-cov>=4.1.0",
    "pytest-docker>=1,<4",
    "pytest-mock",
    "pytest-timeout>=2",
    "pytest-xdist>=3.2",
    'pywin32>=225; sys_platform == "win32"', # optional test dependency
    'tzdata; sys_platform == "win32"',  # for testing with celery
    "sqlalchemy>=1,<3", # optional dependency for `import-db`
    "pandas>=1", # optional dependency for `import-db`
]
webdav = ["dvc-webdav>=3.0.1,<4"]
webhdfs = ["dvc-webhdfs>=3.1,<4"]
webhdfs_kerberos = ["dvc-webhdfs[kerberos]>=3.1,<4"]

[project.urls]
Documentation = "https://dvc.org/doc"
Issues = "https://github.com/treeverse/dvc/issues"
Source = "https://github.com/treeverse/dvc"

[project.scripts]
dvc = "dvc.cli:main"

[project.entry-points."fsspec.specs"]
dvc = "dvc.api:DVCFileSystem"

[project.entry-points."universal_pathlib.implementations"]
dvc = "dvc.fs.dvc_path:DVCPath"
# universal_pathlib does not support fsspec url chaining yet.
# see https://github.com/fsspec/universal_pathlib/issues/28.
"dvc+http" = "dvc.fs.dvc_path:DVCPath"
"dvc+https" = "dvc.fs.dvc_path:DVCPath"
"dvc+ssh" = "dvc.fs.dvc_path:DVCPath"

[project.entry-points."pyinstaller40"]
hook-dirs = "dvc.__pyinstaller:get_hook_dirs"
tests = "dvc.__pyinstaller:get_PyInstaller_tests"

[tool.setuptools.packages.find]
exclude = ["tests", "tests.*"]
namespaces = false

[tool.setuptools_scm]
write_to = "dvc/_version.py"

[tool.pytest.ini_options]
addopts = "-ra --cov-config pyproject.toml"
filterwarnings = [
    "error::ResourceWarning",
    "error::pytest.PytestUnraisableExceptionWarning",
    "error::pytest_mock.PytestMockWarning",
    # https://github.com/boto/botocore/issues/2744
    "ignore:'urllib3.contrib.pyopenssl' module is deprecated:DeprecationWarning",
    # google.cloud: https://github.com/googleapis/python-storage/issues/1000
    # google.logging: https://github.com/googleapis/python-logging/issues/730
    # Also happens with `zc.lockfile`.
    "ignore:Deprecated call to `pkg_resources.declare_namespace:DeprecationWarning",
    # see https://github.com/networkx/networkx/issues/5723.
    "ignore:nx.nx_pydot.* depends on the pydot package, which has.*known issues and is not actively maintained:DeprecationWarning",
    # TODO: investigate where we are not closing sqlite3.Connection
    "ignore:unclosed database.*sqlite3.Connection:ResourceWarning",
    "ignore:unclosed.*<socket.socket:ResourceWarning",
]
markers = [
    "needs_internet: Might need network access for the tests",
    "studio: Tests verifying contract between DVC and Studio",
    "vscode: Tests verifying contract between DVC and VSCode plugin",
]
testpaths = ["tests"]
xfail_strict = true

[tool.coverage.run]
branch = true
source = ["dvc", "tests"]

[tool.coverage.paths]
source = ["dvc"]

[tool.coverage.report]
exclude_lines = [
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "if typing.TYPE_CHECKING:",
    "@overload",
    "pragma: no cover",
    "raise AssertionError",
    "raise NotImplementedError",
]
show_missing = true

[tool.mypy]
check_untyped_defs = true
files = ["dvc"]
no_implicit_optional = true
pretty = true
show_column_numbers = true
show_error_codes = true
show_error_context = true
show_traceback = true
strict_equality = true
extra_checks = true
warn_no_return = true
warn_redundant_casts = true
warn_unreachable = true
warn_unused_configs = true

[[tool.mypy.overrides]]
