# Repository semantic capsule: INCATools/ontology-development-kit

- Commit: `a17e75015ec935d5f42e41f458c25efcd9a3c48f`
- Default branch: `master`
- Description: INCATools/ontology-development-kit
- Selected evidence files: 5 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

[![Build the ODK images and run the tests](https://github.com/INCATools/ontology-development-kit/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/INCATools/ontology-development-kit/actions/workflows/build-and-test.yml)
[![DOI](https://zenodo.org/badge/48047921.svg)](https://zenodo.org/badge/latestdoi/48047921)
[![DOI](https://img.shields.io/docker/pulls/obolibrary/odkfull.svg)](https://hub.docker.com/r/obolibrary/odkfull)


https://www.wikidata.org/wiki/Q112336713

# The Ontology Development Kit (ODK)

<img src="https://github.com/jmcmurry/closed-illustrations/raw/master/logos/odk-logos/odk-logo_black-banner.png" />

Manage your ontology's life cycle with the Ontology Development Kit (ODK)! The ODK is
- a toolbox of various ontology related tools such as ROBOT, owltools, dosdp-tools and many more, bundled as a docker image
- a set of executable workflows for managing your ontology's continuous integration, quality control, releases and dynamic imports

For more details, see

 * [2022 Paper](https://doi.org/10.1093/database/baac087)
 * [2018 Article](https://douroucouli.wordpress.com/2018/08/06/new-version-of-ontology-development-kit-now-with-docker-support/)
 * [ICBO Workshop Slides 2018](https://docs.google.com/presentation/d/1nIybviEEJiRKHO2rkBMZsQ0QjtsHyU01_-9beZqD_Z4/edit?usp=sharing)
 * [ICBO Workshop Slides 2017](https://docs.google.com/presentation/d/1JPAaDl6Nitxet9NVqWI30eIygcerYAjdMIGmxbRtIn0/edit?usp=sharing)
 * [Docker image on Docker Hub](https://hub.docker.com/r/obolibrary/odkfull)

# Where to get help

- _How-to guides_:
  - How to [create your first repository](https://oboacademy.github.io/obook/howto/odk-create-repo/) with the ODK
  - How to [add license, title and description to your ontology](https://oboacademy.github.io/obook/reference/formatting-license/)
  - How to [import large ontologies efficiently](https://oboacademy.github.io/obook/howto/deal-with-large-ontologies/)
- Reference:
  - Learn about the [different kinds of release artefacts](https://oboacademy.github.io/obook/reference/release-artefacts/)
  - Learn about the [ODK Project Configuration Schema](https://github.com/INCATools/ontology-development-kit/blob/master/docs/project-schema.md) for allowed parameters in your `[project]-odk.yaml`
- Community:
  -  If you have issues, file them here: https://github.com/INCATools/ontology-development-kit/issues
  -  We also have an active community on Slack; you can request access by making a ticket [here](https://github.com/INCATools/ontology-development-kit/issues) as well

# Steering Committee

* @gouttegd Damien Goutte-Gattat (ODK Lead, German BioImaging e.V.)
* @matentzn Nicolas Matentzoglu (ODK Deputy, Semanticly)
* @cmungall Chris Mungall (ODK Founder, LBNL)

# Core team

* @anitacaron Anita Caron (Novo Nordisk)
* @balhoff Jim Balhoff (RENCI)
* @dosumis David Osumi-Sutherland (Sanger)
* @ehartley Emily Hartley (Critical Path Institute)
* @hkir-dev Huseyin Kir (EMBL-EBI)
* @shawntanzk Shawn Tan (Novo Nordisk)
* @ubyndr Ismail Ugur Bayindir (EMBL-EBI)

Full list of contributors:
https://github.com/INCATools/ontology-development-kit/graphs/contributors

# Cite

https://doi.org/10.1093/database/baac087

# Outstanding contributions
Outstanding contributors are groups and institutions that have helped with organising the ODK development, providing funding,
advice and infrastructure. We are very grateful for all your contributions - the project would not exist without you!

## Monarch Initiative
<img src="https://user-images.githubusercontent.com/7070631/121600493-72ee4b00-ca3c-11eb-87c3-57742fca7af5.png" data-canonical-src="https://user-images.githubusercontent.com/7070631/121600493-72ee4b00-ca3c-11eb-87c3-57742fca7af5.png" width="300" />

The Monarch Initiative is a consortium of medical, biological and computational experts that provide major ontology services such as the Human Phenotype Ontology, [Mondo](https://mondo.monarchinitiative.org/) and an integrative data and [analytic platform](https://monarchinitiative.org/) connecting phenotypes to genotypes across species, bridging basic and applied research with semantics-based analysis.

https://monarchinitiative.org/

## European Bioinformatics Institute
<img src="https://user-images.githubusercontent.com/7070631/121600529-813c6700-ca3c-11eb-8590-871a963a3cfd.png" data-canonical-src="https://user-images.githubusercontent.com/7070631/121600529-813c6700-ca3c-11eb-8590-871a963a3cfd.png" width="300" />

The Samples, Phenotypes and Ontologies (SPOT) team, led by Helen Parkinson, is concerned with high throughput mammalian phenotyping, Semantics as a Service and human genetics resources. Members of the SPOT team including David Osumi-Sutherland have made major contributions to ODK, and provided advice, use cases and funding.

https://www.ebi.ac.uk/spot/

## University of Florida Biomedical Informatics Program
<img src="https://user-images.githubusercontent.com/7070631/121600373-46d2ca00-ca3c-11eb-8899-c814c4041d54.png" data-canonical-src="https://user-images.githubusercontent.com/7070631/121600373-46d2ca00-ca3c-11eb-8899-c814c4041d54.png" width="300" />

https://hobi.med.ufl.edu/research-2/biomedical-informatics-3/

## Knocean Inc.
<img src="https://user-images.githubusercontent.com/7070631/121600426-56eaa980-ca3c-11eb-9315-b03234bb6b06.png" data-canonical-src="https://user-images.githubusercontent.com/7070631/121600426-56eaa980-ca3c-11eb-9315-b03234bb6b06.png" width="300" />

Knocean Inc. offers consulting and development services for science informatics, in particular in the area of biomedical ontologies and ontology tooling.

http://knocean.com/

## Critical Path Institute
<img src="https://user-images.githubusercontent.com/7070631/122019745-049ee500-cdbc-11eb-9ed0-3ac3ca717d9b.png" data-canonical-src="https://user-images.githubusercontent.com/7070631/122019745-049ee500-cdbc-11eb-9ed0-3ac3ca717d9b.png" width="300" />

The Critical Path For Alzheimer’s Disease (CPAD) is a public-private partnership aimed at creating new tools and methods that can be applied to increase the efficiency of the development process of new treatments for Alzheimer disease (AD) and related neurodegenerative disorders with impaired cognition and function.

https://c-path.org/

# Requirements

## Docker

Using the ODK docker image requires Docker Engine version 20.10.8 or greater for v1.3.1.

# Tips and Tricks

## Customizing your ODK installation

You will likely want to customize the build process, and of course to edit the ontology.

We recommend that you do not edit the main Makefile, but instead the supplemental one (e.g. myont.Makefile) is src/ontology

An example of how you can customise your imports for example is documented [here](http://pato-ontology.github.io/pato/odk-workflows/RepoManagement/)

## Migrating an existing ontology repo to the ODK

The ODK is designed for creating a new repo for a new ontology. It can also be used to help figure out how to migrate an existing git repository to the ODK structure. There are different ways to do this.

 * Manually compare your ontology against the [templates](https://github.com/INCATools/odkcore/tree/main/src/incatools/odk/templates) folder and make necessary adjustments
 * Run the seed script as if creating a new repo. Manually compare this with your existing repo and use `git mv` to rearrange, and adding any missing files by copying them across and doing a `git add`
 * Create a new repo de novo and abandon your existing one, using, for example, github issue mover to move tickets across.

Obviously the second method is not ideal as you lose your git history. Note even with `git mv` history tracking becomes harder.

If you have built your ontology using a previous version of ODK,
migration of your setup is unfortunately a manual process. In general
you do not absolutely *need* to upgrade your setup, but doing so will
bring advantages in terms of aligning with emerging standards ways of
doing things. The less customization you do on your repo the easier it
should be to migrate.

Consult the [CHANGELOG.md](CHANGELOG.md) file for changes made between
releases to assist in upgrading.

## More documentation

You will find additional documentation in the src/ontology/README-editors.md file in your repo.

The ODK also comes with built in options to generate your own shiny documentation; see for example the [PATO documentation here](http://pato-ontology.github.io/pato/) which is almost entirely autogenerated from the ODK.

## Alternative to Docker

You can use the `odk install` command of the [ODK
Core](https://github.com/INCATools/odkcore) module to install a “native
ODK environment” that allows using the ODK without using Docker. See the
documentation of ODK Core for more details.

Of note, native ODK environments are only supported for GNU/Linux and
macOS. To use the ODK on Windows, Docker is mandatory.

## `CONTRIBUTING.md`

# Instructions for DEVELOPERs of ODK

This is intended for developers only, see [README](README.md) for the
main docs.

## Development principles

### Project’s aims

The primary aim of the ODK (its mission statement, if you will) is to
make it possible for any ontology project to benefit from thoroughly
designed, well tested ontology engineering workflows, even if the
project does not have the luxury of a full-time ontology pipeline
engineer always available to fix snafus and keep things running.

From this aim, we derive the following guidelines that developers should
keep in mind whenever working on the ODK (especially when adding new
features):

(1) No feature should require from the user to install anything on their
machine beyond Docker (required to run the ODK images) and Git (needed
to work on ODK repositories).

(2) As much as possible, features should not require any specialised
configuration beyond what can be configured in the `*-odk.yaml` ODK
configuration file.

(3) All standard workflows should be usable by people that do not have
engineering or programming skills beyond the ability of running simple
commands on the command line.

(4) Point (3) applies to updating an existing ODK-managed project to a
newer version of the ODK, which should not require the intervention of an
engineer.

### Custom/advanced workflows

For the projects that do have the luxury of an ontology pipeline
engineer, the ODK must not stand in the way of any custom or advanced
workflow that might be necessary.

An ontology pipeline engineer must always be able to customise any
standard ODK workflow and to add specialised workflows as needed.

However, whenever custom workflows are used, the promise of smooth
updates (point 4 in the previous section) no longer holds — it is
explicitly acceptable for ODK developers to introduce changes that may
break custom workflows.

### Technological stack and dependencies

#### Docker

Currently, the ODK is provided as a Docker image. However, at least on
GNU/Linux and macOS, it should be possible to seed/update a repository
and run any workflow within it _without_ Docker, provided all the
required tools (e.g. ROBOT, dosdp-tools, etc.) are available on the
system. The role of the Docker image is merely to provide a convenient
way of ensuring that all the tools are readily available.

Therefore, developers must refrain from assuming that the Docker image
will always be used. For example, workflows must not invoke a tool by
hardcoding its path within the Docker image, but instead assume the
tools is available in the _PATH_ (so, for example, ROBOT should be
invoked simply as `robot`, _not_ as `/odk/bin/robot`).

Likewise, all resource files provided by the ODK must be accessed only
through the `ODK_RESOURCES_DIR` environment variable (defaulting to
`/odk/resources` – the directory for resources within the Docker image –
only when that variable does not exist).

#### Git

Currently, the ODK assumes that an ontology project will be
version-controlled using Git.

There is no plan to support other version control systems (such as
Mercurial, Subversion, etc.), and it is fine for developers to continue
assuming the use of Git.

#### GitHub

Several features in the ODK assumes that an ontology project is or will
be hosted on GitHub.

This is only fine as long as those features are not *required*. It
must *always* be possible to host a ODK-managed ontology on any other
Git hosting service (including self-hosting).

#### POSIX compatibility and “GNU-isms”

The ODK image is built on top of a GNU/Linux system, and there is no
plan to change that anytime soon. However, as much as possible, even for
processes that are intended to run within a ODK container it is best to
avoid relying on GNU-specific behaviours or options (so-called
“GNU-isms”), unless doing so provides a clear benefit (e.g. in
performance or readability) over a strictly POSIX-compliant alternative.

That rule applies more strongly to wrapper scripts that are intended to
be run from the host’s shell rather than from within the ODK container
(e.g. `run.sh`, `seed-via-docker.sh`): those scripts *must* avoid any
features specific to one particular flavour of the Bourne shell (be it
`bash`, `dash`, `zsh`, etc.).

The exception to that rule is for the standard ODK-generated Makefile:
it is explicitly fine for that Makefile to depend on features that are
specific to GNU Make.

#### Operating systems and architectures.

The ODK should be usable at least on:

* GNU/Linux (any distribution, x86\_64 only);
* macOS X (any version >= 10.12, x86\_64 and arm64);
* Windows (versions 10 and 11, 86\_64 only).

Running on other systems, versions, or architectures may be possible but
is not officially supported.

## Templating system

Creating (“seeding”) a ODK-managed repository is done with the `odk`
command from the [ODK Core](https://github.com/INCATools/odkcore). The
`seed` subcommand instantiates the Jinja2 templates found in the
[templates/](https://github.com/INCATools/odkcore/tree/main/src/incatools/odk/templates)
directory of that project.

For example, the file
[Makefile.jinja2](https://github.com/INCATools/odkcore/tree/main/src/incatools/odk/templates/src/ontology/Makefile.jinja2)
will compile to a file `src/ontology/Makefile` in the target/output
directory.

Jinja2 templates should be fairly easy to grok for anyone familiar with
templating systems. We feed the template engine with a project object
that is passed in by the user (see below).

Logic in the templates should be kept to a minimum (though the
aforementioned `Makefile.jinja2` template is a great offender of this
principle). Whenever possible, complex logic should reside in the
`odk.py` script, which should provide ready-to-use variables and lists
for the templates to exploit.

Templates may contain Jinja2 comments (`{# .. #}`) which are intended
for ODK *developers* only (as those comments will not appear in the
produced files). Templates may also contain comments intended for the
*users*, using whatever comment syntax is appropriate for the kind of
produced file (e.g. a Makefile template may contain comments as lines
starting with `#`, a RDF/XML template may contain comments as
`<!-- ... -->` blocks, etc).

### Dynamic File Names

Sometimes the odk needs to create a file whose name is based on an
input setting or configuration; sometimes lists of such files need to
be created.

For example, if the user specifies 3 external ontology dependencies,
then we want to see the repo with 3 files `imports/{{ont.id}}_import.owl`

Rather than embed this logic in code, we can use special “dynamic”
templates (identified by a name starting with `_dynamic`). A dynamic
template is a “tar-like” bundle containing an arbitrary number of files,
each file starting with a line of the form:

```
^^^ path/to/file
```

where `path/to/file` is the complete pathname of the file to create. All
subsequent lines in the bundle, up to the next `^^^` line, will end up
in that file.

Because the entire bundle is itself a Jinja2 template, and the bundle is
extracted _after_ template expansion, this system allows us to have

(1) dynamic file names:

```
^^^ src/ontology/{{ project.id }}-idranges.owl
# ID ranges file
@Prefix: rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
...
```

(2) files that are created or not depending on the value of a
configuration option:

```
{% if project.use_templates %}
^^^ src/templates/README.md
# ROBOT templates
...
{%- endif %}
```

(3) and files that are created serially in a Jinja2 loop:

```
{% for imp in project.import_group.products %}
^^^ src/ontology/imports/{{ imp.id }}_import.owl
...
```

## The Project object

Currently the datamodel is specified as python dataclasses, for now
the best way to see the complete spec is to look at the classes
annotated with `@dataclass` in the code.

An auto-generated documentation is available in
[docs/project-schema.md](docs/project-schema.md), however that
documentation is outdated and currently cannot be refreshed.

At some point, a complete (and up-to-date) documentation for the schema
should be found in the [ODK Core](https://github.com/INCATools/odkcore)
project. Until then, the
[examples](https://github.com/INCATools/odkcore/tree/main/examples) and
[tests/configs](https://github.com/INCATools/odkcore/tree/main/tests/configs)
directories in that project provide some examples of ODK configuration
files.

## `Dockerfile`

# Final ODK image
# (built upon the odklite image)
ARG ODKLITE_TAG=latest
FROM obolibrary/odklite:${ODKLITE_TAG}
LABEL maintainer="obo-tools@googlegroups.com"

WORKDIR /odk

ARG ODK_VERSION 0.0.0
ENV ODK_VERSION=$ODK_VERSION

# Software versions
ENV JENA_VERSION=6.1.0
ENV KGCL_JAVA_VERSION=0.6.1
ENV SCALA_CLI_VERSION=1.8.0
ENV OWLTOOLS_VERSION=2020-04-06
ENV YQ_VERSION=4.53.2

# Avoid repeated downloads of script dependencies by mounting the local coursier cache:
# docker run -v $HOME/.coursier/cache/v1:/odk/tools/.coursier-cache ...
ENV COURSIER_CACHE="/odk/tools/.coursier-cache"

# Install tools provided by Ubuntu.
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends  \
    build-essential \
    openssh-client \
    openjdk-21-jdk-headless \
    maven \
    python3-dev \
    subversion \
    automake \
    aha \
    dos2unix \
    libjson-perl \
    libbusiness-isbn-perl \
    pkg-config \
    xlsx2csv \
    nodejs \
    npm \
    graphviz \
    python3-psycopg2

# Install run-time dependencies for Soufflé.
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
        g++ \
        libffi-dev \
        libncurses5-dev \
        libsqlite3-dev \
        mcpp \
        zlib1g-dev

# Copy everything that we have prepared in the builder image.
COPY --from=obolibrary/odkbuild:latest /staging/full /

# Install Konclude.
# On x86_64, we get it from a pre-built release from upstream; on arm64,
# we use a custom pre-built binary to which we just need to add the
# run-time dependencies (the binary is not statically linked).
ARG TARGETARCH
RUN test "x$TARGETARCH" = xamd64 && ( \
        wget -nv https://github.com/konclude/Konclude/releases/download/v0.7.0-1138/Konclude-v0.7.0-1138-Linux-Docker-Compiled-x64-GCC4.8.4-Static-Qt5.12.10.zip \
            -O /odk/Konclude.zip && \
        unzip Konclude.zip && \
        mv Konclude-v0.7.0-1138-Linux-Docker-Compiled-x64-GCC4.8.4-Static-Qt5.12.10/Binaries/Konclude /odk/bin/Konclude && \
        rm -rf Konclude-v0.7.0-1138-Linux-Docker-Compiled-x64-GCC4.8.4-Static-Qt5.12.10 && \
        rm Konclude.zip \
    ) || ( \
        DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
            libqt5xml5 libqt5network5 libqt5concurrent5 && \
        wget -nv https://incenp.org/files/softs/konclude/0.7/Konclude-v0.7.0-1138-Linux-arm64-GCC.zip \
            -O /odk/Konclude.zip && \
        unzip Konclude.zip && \
        mv Konclude-v0.7.0-1138-Linux-arm64-GCC/Binaries/Konclude /odk/bin/Konclude && \
        rm -rf Konclude-v0.7.0-1138-Linux-arm64-GCC && \
        rm Konclude.zip \
    )

# Install OWLTOOLS.
RUN wget -nv https://github.com/owlcollab/owltools/releases/download/$OWLTOOLS_VERSION/owltools \
        -O /odk/tools/owltools.jar && \
    echo "#!/bin/sh" > /odk/bin/owltools && \
    echo "exec java \$JAVA_OPTS -DentityExpansionLimit=4086000 -Djava.awt.headless=true -jar /odk/tools/owltools.jar \"\$@\"" >> /odk/bin/owltools && \
    echo "#!/bin/sh" > /odk/bin/ontology-release-runner && \
    echo "exec java \$JAVA_OPTS -cp /odk/tools/owltools.jar owltools.ontologyrelease.OboOntologyReleaseRunner \"\$@\"" >> /odk/bin/ontology-release-runner && \
    chmod 755 /odk/bin/owltools && \
    chmod 755 /odk/bin/ontology-release-runner

# Install Jena.
RUN wget -nv http://archive.apache.org/dist/jena/binaries/apache-jena-$JENA_VERSION.tar.gz -O- | tar xzC /odk/tools && \
    mv /odk/tools/apache-jena-$JENA_VERSION /odk/tools/apache-jena && \
    find /odk/tools/apache-jena/bin -type f -executable -exec ln -s {} /odk/bin \;

# Install Scala-CLI
RUN wget -nv https://github.com/VirtusLab/scala-cli/releases/download/v$SCALA_CLI_VERSION/scala-cli.jar \
        -O /odk/tools/scala-cli.jar && \
    echo "#!/bin/sh" > /odk/bin/scala-cli && \
    echo "exec java \$JAVA_OPTS -jar /odk/tools/scala-cli.jar \"\$@\"" >> /odk/bin/scala-cli && \
    chmod 0755 /odk/bin/scala-cli

# Install obographviz
RUN npm install -g obographviz && \
    chown -R root:root /usr/local/lib/node_modules

# Install KGCL ROBOT plugin
RUN wget -nv -O /odk/resources/robot/plugins/kgcl.jar https://github.com/gouttegd/kgcl-java/releases/download/kgcl-java-$KGCL_JAVA_VERSION/kgcl-robot-plugin-$KGCL_JAVA_VERSION.jar

# Install Mike Farah's (mf) YQ command-line YAML, JSON and XML processor
RUN if [ "$TARGETARCH" = "amd64" ]; then \
        wget -nv https://github.com/mikefarah/yq/releases/download/v$YQ_VERSION/yq_linux_amd64 -O /odk/bin/yq-mf && \
        chmod 0755 /odk/bin/yq-mf ; \
    elif [ "$TARGETARCH" = "arm64" ]; then \
        wget -nv https://github.com/mikefarah/yq/releases/download/v$YQ_VERSION/yq_linux_arm64 -O /odk/bin/yq-mf && \
        chmod 0755 /odk/bin/yq-mf ; \
    else \
        echo "Unsupported TARGETARCH: $TARGETARCH" && exit 1 ; \
    fi


## `Makefile`

# This makefile is purely for running tests on the complete ontology-development-kit package on travis;
# users should not need to use this

# command used in make test.
# this can be changed to seed-via-docker.sh;
# but this should NOT be the default for environments like travis which
# run in a docker container anyway
CMD = odk seed

EMAIL_ARGS=

CACHE=

ARCH=linux/$(shell uname -m | sed 's/x86_64/amd64/')
PLATFORMS=linux/amd64,linux/arm64

.PHONY: .FORCE

test_odklite_programs:
	@./tests/test-program.sh ROBOT robot --version
	@./tests/test-program.sh DOSDP-TOOLS dosdp-tools --version
	@./tests/test-program.sh DICER-CLI dicer-cli --version
	@./tests/test-program.sh SSSOM-CLI sssom-cli --version
	@./tests/test-program.sh ODK odk --help

test_odkfull_programs: test_odklite_programs
	@./tests/test-program.sh KONCLUDE Konclude -h
	@./tests/test-program.sh SOUFFLE souffle --version
	@./tests/test-program.sh JENA jena
	@./tests/test-program.sh OWLTOOLS owltools --version
	@./tests/test-program.sh OORT ontology-release-runner --help
	@./tests/test-program.sh JINJANATOR jinjanate --version
	@./tests/test-program.sh SCALA-CLI scala-cli --version
	@./tests/test-program.sh SPARQL sparql --version
	@./tests/test-program.sh RELATION-GRAPH relation-graph --version
	@./tests/test-program.sh OAKLIB runoak --help
	@./tests/test-program.sh SSSOM-PY sssom --version
	@./tests/test-program.sh YQ-MF yq-mf --version

test_odkdev_programs: test_odkfull_programs

# Subset of ODK Core tests to run
TESTS = minimal module-star release
TEST_FILES = $(foreach t, $(TESTS), core/tests/configs/test-$(t).yaml)
test: $(TEST_FILES)
	echo "All tests passed successfully!"

core/tests/configs/*.yaml: .FORCE
	$(CMD) -c -C $@


# Building docker image
VERSION = "v1.7"
IM=obolibrary/odkfull
IMLITE=obolibrary/odklite
ROB=obolibrary/robot
#ROBOT_JAR="https://github.com/monarch-ebi-dev/odk_utils/raw/master/robot_maven_test.jar"
ROBOT_JAR_ARGS=#--build-arg ROBOT_JAR=$(ROBOT_JAR)
TAGS_OPTION=-t $(IM):$(VERSION) -t $(IM):latest

build: build-odklite
	docker build $(CACHE) --platform $(ARCH) \
	    --build-arg ODK_VERSION=$(VERSION) $(ROBOT_JAR_ARGS) \
	    $(TAGS_OPTION) \
	    .

build-odklite: build-builder
	$(MAKE) -C docker/odklite ARCH=$(ARCH) CACHE=$(CACHE) \
		IM=$(IMLITE) VERSION=$(VERSION) build

build-robot:
	$(MAKE) -C docker/robot ARCH=$(ARCH) CACHE=$(CACHE) build

build-builder:
	$(MAKE) -C docker/builder ARCH=$(ARCH) CACHE=$(CACHE) build

build-no-cache:
	$(MAKE) build CACHE=--no-cache

build-odklite-dev: build-builder
	$(MAKE) TAGS_OPTION="-t $(IMLITE):dev" VERSION=$(VERSION)-dev build-odklite

build-dev: build-odklite-dev
	docker build $(CACHE) --platform $(ARCH) \
		--build-arg ODK_VERSION=$(VERSION)-dev \
		--build-arg ODKLITE_TAG=dev \
		$(ROBOT_JAR_ARGS) \
		-t $(IM):dev \
		.

clean:
	docker kill $(IM) || echo not running
	docker rm $(IM) || echo not made


#### TESTING #####

test-flavor:
	@if docker images | grep -q odk$(FLAVOR) ; then \
		$(MAKE) test_odk$(FLAVOR)_programs ODK_IMAGE=odk$(FLAVOR) ; \
		$(MAKE) test CMD=./seed-via-docker.sh ODK_IMAGE=odk$(FLAVOR) ; \
	else \
		echo "Image obolibrary/odk$(FLAVOR) not locally available" ; \
	fi

test-full: build
	$(MAKE) test-flavor FLAVOR=full

test-lite: build-odklite
	$(MAKE) test-flavor FLAVOR=lite

tests: test-full

test-no-build:
	$(MAKE) test-flavor FLAVOR=full

test-lite-no-build:
	$(MAKE) test-flavor FLAVOR=lite


#### Publishing #####

publish-no-build:
	docker push $(DEV):$(VERSION)
	docker push $(IM):latest
	docker push $(IM):$(VERSION)
	$(MAKE) -C docker/odklite publish-no-build

publish: build
	$(MAKE) publish-no-build

publish-multiarch:
	$(MAKE) -C docker/robot CACHE=$(CACHE) PLATFORMS=$(PLATFORMS) \
		publish-multiarch
	$(MAKE) -C docker/builder CACHE=$(CACHE) PLATFORMS=$(PLATFORMS) \
		publish-multiarch
	$(MAKE) -C docker/odklite IM=$(IMLITE) VERSION=$(VERSION) \
	    CACHE=$(CACHE) PLATFORMS=$(PLATFORMS) \
	    publish-multiarch
	docker buildx build $(CACHE) --push --platform $(PLATFORMS) \
	    --build-arg ODK_VERSION=$(VERSION) \
	    $(TAGS_OPTION) \
	    .

publish-multiarch-dev:
	$(MAKE) -C docker/builder CACHE=$(CACHE) PLATFORMS=$(PLATFORMS) \
		publish-multiarch
	$(MAKE) -C docker/odklite IM=$(IMLITE) VERSION=$(VERSION)-dev \
		CACHE=$(CACHE) PLATFORMS=$(PLATFORMS) \
		TAGS_OPTION="-t $(IMLITE):dev" \
		publish-multiarch
	docker buildx build $(CACHE) --push --platform $(PLATFORMS) \
		--build-arg ODK_VERSION=$(VERSION)-dev \
		--build-arg ODKLITE_TAG=dev \
		-t $(IM):dev \
		.

# This should use the same base image as the one used to build the ODK itself.
constraints.txt: python-requirements.txt
	docker run -v $$PWD:/work -w /work --rm -ti ubuntu:26.04 /work/scripts/update-constraints.sh --in-docker

clean-tests:
	rm -rf target/*

dev-test-publish:
	git pull
	docker buildx rm multiarch
	docker buildx create --name multiarch --driver docker-container --use
	$(MAKE) tests publish-multiarch-dev

dev-test-publish-no-rm:
	git pull
	docker buildx create --name multiarch --driver docker-container --use
	$(MAKE) tests publish-multiarch-dev

## `docs/index.md`

# The Ontology Development Kit (ODK) - Documentation

<img src="https://github.com/jmcmurry/closed-illustrations/raw/master/logos/odk-logos/odk-logo_black-banner.png" />

Manage your ontology's life cycle with the Ontology Development Kit (ODK)! 

The ODK is
- a toolbox of various ontology related tools such as ROBOT, owltools, dosdp-tools and many more, bundled as a docker image
- a set of executable workflows for managing your ontology's continuous integration, quality control, releases and dynamic imports

For more details, see

 * [2022 Paper](https://doi.org/10.1093/database/baac087) 
 * [2018 Article](https://douroucouli.wordpress.com/2018/08/06/new-version-of-ontology-development-kit-now-with-docker-support/)
 * [ICBO Workshop Slides 2018](https://docs.google.com/presentation/d/1nIybviEEJiRKHO2rkBMZsQ0QjtsHyU01_-9beZqD_Z4/edit?usp=sharing)
 * [ICBO Workshop Slides 2017](https://docs.google.com/presentation/d/1JPAaDl6Nitxet9NVqWI30eIygcerYAjdMIGmxbRtIn0/edit?usp=sharing)

# Where to get help

- _How-to guides_:
  - How to [create your first repository](https://oboacademy.github.io/obook/tutorial/setting-up-project-odk/) with the ODK
  - [ODK in 20 minutes](https://oboacademy.github.io/obook/tutorial/odk-tutorial-2/)
  - [ODK adding custom QC checks](https://oboacademy.github.io/obook/tutorial/custom-qc/)
  - How to [import large ontologies efficiently](https://oboacademy.github.io/obook/howto/deal-with-large-ontologies/)
- Reference:
  - Learn about the [different kinds of release artefacts](https://oboacademy.github.io/obook/reference/release-artefacts/)
  - Learn about the [ODK Project Configuration Schema](project-schema.md) for allowed parameters in your `[project]-odk.yaml` 
- Community:
  -  If you have issues, file them on [our issue tracker](https://github.com/INCATools/ontology-development-kit/issues)
  -  We also have an active community on Slack; you can request access by making a ticket [here](https://github.com/INCATools/ontology-development-kit/issues)
