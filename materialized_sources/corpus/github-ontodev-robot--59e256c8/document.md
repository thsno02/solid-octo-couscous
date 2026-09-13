# Repository semantic capsule: ontodev/robot

- Commit: `a67eed4823af7f5b7bb33ddd12f662adc4303cad`
- Default branch: `master`
- Description: ontodev/robot
- Selected evidence files: 4 of 21 files observed
- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.


## `README.md`

# ROBOT is an OBO Tool

[![Java CI](https://github.com/ontodev/robot/actions/workflows/java-ci.yml/badge.svg)](https://github.com/ontodev/robot/actions/workflows/java-ci.yml)
[![Maven Central](https://img.shields.io/maven-central/v/org.obolibrary.robot/robot.svg?label=Maven%20Central)](https://central.sonatype.com/artifact/org.obolibrary.robot/robot)
[![Javadocs](https://www.javadoc.io/badge/org.obolibrary.robot/robot-core.svg)](https://www.javadoc.io/doc/org.obolibrary.robot/robot-core)

ROBOT is a command-line tool and library for automating ontology development tasks, with a focus on [Open Biological and Biomedical Ontologies (OBO)](http://obofoundry.org).

### Cite ROBOT

R.C. Jackson, J.P. Balhoff, E. Douglass, N.L. Harris, C.J. Mungall, and J.A. Overton. [ROBOT: A tool for automating ontology workflows](https://rdcu.be/bMnHT). BMC Bioinformatics, vol. 20, July 2019.


### Installation and Usage

Please see <http://robot.obolibrary.org>.


## Build

We use [Maven](http://maven.apache.org) as our build tool. Make sure it's [installed](http://maven.apache.org/download.cgi), then run:

    mvn clean package

This will create a self-contained Jar file in `bin/robot.jar`.

Other build options:

- `mvn clean test` runs JUnit tests with reports in `[module]/target/surefire-reports`
- `mvn clean verify` rebuilds the package and runs integration tests against it, with reports in `[module]/target/failsafe-reports`
- `mvn site` generates Javadoc in `target/site` and `[module]/target/site`

Alternatively, you can use [Docker](https://www.docker.com) with the provided [Dockerfile](Dockerfile) to build and run ROBOT from within a container. First build an image with `docker build --tag robot:latest .` then run ROBOT from the container with the usual command-line arguments: `docker run --rm robot --help`.


## Code Style

We use [Google Java Style](https://google.github.io/styleguide/javaguide.html), automatically enforced with [google-java-format](https://github.com/google/google-java-format) and [fmt-maven-plugin](https://github.com/coveo/fmt-maven-plugin). You may want to use the [styleguide configuration file](https://github.com/google/styleguide) for [Eclipse](https://github.com/google/styleguide/blob/gh-pages/eclipse-java-google-style.xml) or [IntelliJ](https://github.com/google/styleguide/blob/gh-pages/intellij-java-google-style.xml).


## Design

The library provides a set of Operations and a set of Commands. Commands handle the command-line interface and IO tasks, while Operations focus on manipulating ontologies. Sometimes you will have the pair of an Operation and a Command, but there's no necessity for a one-to-one correspondence between them.

Commands implement the Command interface, which requires a `main(String[] args)` method. Each command can be called via `main`, but the CommandLineInterface class provides a single entry point for selecting between all the available commands. While each Command can run independently, there are shared conventions for command-line options such as `--input`, `--prefix`, `--output`, etc. These shared conventions are implemented in the CommandLineHelper utility class. There is also an IOHelper class providing convenient methods for loading and saving ontologies and lists of terms. A simple Command will consist of a few CommandLineHelper calls to determine arguments, a few IOHelper calls to load or save files, and one call to the appropriate Operation.

Operations are currently implemented with static methods and no shared interface. They should not contain IO or CLI code.

The current implementation is modular but not pluggable. In particular, the CommandLineInterface class depends on a hard-coded list of Commands.


## Term Lists

Many Operations require lists of terms. The IOHelper class defines methods for collecting lists of terms from strings and files, and returning a `Set<IRI>`. Our convention is that a term list is a space-separated list of IRIs or CURIEs with optional comments. The "#" character and everything to the end of the line is ignored. Note that a "#" must start the line or be preceded by whitespace -- a "#" inside an IRI does not start a comment.


## Acknowledgments

The initial version of ROBOT was developed by James A. Overton, based on requirements and designs given by Chris Mungall, Heiko Dietze and David Osumi-Sutherland. This initial version was funded by P41 grant 5P41HG002273-09 to the Gene Ontology Consortium. Current support is from NIH grant 1 R24 HG010032-01, “Services to support the OBO foundry standards” to C. Mungall and B. Peters.


## Copyright

The copyright for ROBOT code and documentation belongs to the respective authors. ROBOT code is distributed under a [BSD3 license](https://github.com/ontodev/robot/blob/master/LICENSE.txt). Our `pom.xml` files list a number of software dependencies, each with its own license.

## `CONTRIBUTING.md`

## Contributing

ROBOT is fully open to contributions from anyone! To get started, check the [issues](https://github.com/ontodev/robot/issues) and look for `good first issue`.

### Contents

1. [Getting Started](#getting-started)
2. [Making Changes](#making-changes)
3. [Writing Code](#writing-code)
4. [Writing Unit Tests](#writing-unit-tests)
5. [Writing Integration Tests](#writing-integration-tests)
6. [Documenting Errors](#documenting-errors)

### Getting Started

[Fork](https://help.github.com/articles/fork-a-repo/) the ROBOT repo, and then [clone](https://help.github.com/articles/cloning-a-repository/) it to create a local copy for development. If your desired changes aren't already in the tracker, [create a new issue](https://github.com/ontodev/robot/issues/new).

Before changing anything, make sure the tests pass:

    $ mvn test

### Making Changes

* [Create a new branch](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) with your topic name (e.g. `extract-bug-fix`)
* Make your changes and write any corresponding tests
* Test your changes (`$ mvn test -Dtest=TestName`; make sure you are in the `robot-core` sub-directory before running tests)
* Ensure ROBOT builds correctly (`$ mvn clean package`)
* Commit and push changes to your fork, then create a [pull request](https://help.github.com/articles/about-pull-requests/)

### Writing Code

The source code consists of two main directories: `robot-command` and `robot-core`. The core files contain code for the bulk of the operation, while the command files add command line functionality. When implementing a new feature, make sure the operation has both `*Operation.java` and `*Command.java` files. The operation methods should not be dependent on the command methods.

ROBOT follows the [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html), which is auto-enforced by [google java format](https://github.com/google/google-java-format) during builds. Make sure to add doc comments for any new methods - for specifications see [JavaDocs](http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html).

Each new operation must have a corresponding unit test file (see [Writing Unit Tests](#writing-unit-tests)). Each new command must have a corresponding Markdown documentation file with embedded examples (see [Writing Integration Tests](#writing-integration-tests)).

### Writing Unit Tests

Each operation has a set of unit tests built with [JUnit](https://junit.org/junit5/) that are executed when Maven builds the project. These are located in [`robot-core/src/main/test/java/org/obolibrary/robot/`](https://github.com/ontodev/robot/tree/master/robot-core/src/test/java/org/obolibrary/robot). The test file name corresponds to the operation name, e.g. `ExtractOperationTest.java`. Each test class extends the `CoreTest` class:

```
public class ExtractOperationTest extends CoreTest {
  ...
}
```

[`CoreTest.java`](https://github.com/ontodev/robot/blob/master/robot-core/src/test/java/org/obolibrary/robot/CoreTest.java) provides ontology loading and comparison methods for the tests. Each test within a test class is a public method annotated with `@Test` (from JUnit):

```
@Test
public void testExtractStar() {
  ...
}
```

Tests can be structured in different ways as long as there is a [JUnit assertion](http://junit.sourceforge.net/javadoc/org/junit/Assert.html) in tests in the method. We recommend the following - the test loads an ontology, runs an operation, and then compares to a known-good output (the expected output):

```
OWLOntology input = loadOntology("/resource.owl");
OWLOntology output = MyOperation.operation(input);
assertIdentical("/known-good.owl", output);
```

This method uses [`DiffOperation.compare(...)`](https://github.com/ontodev/robot/blob/master/robot-core/src/main/java/org/obolibrary/robot/DiffOperation.java#L74) functionality to ensure ontologies are identical. If the assertion fails, the test fails. Make sure your output ontology IRI is the same as the known-good ontology's IRI, otherwise the test will fail.

Resource files (e.g., `resource.owl` and `known-good.owl`) are stored in `robot-core/src/test/resources/`. When using the `loadOntology(...)` and `assertIdentical(...)` methods, do not use the full path. Use the name of the file prefixed by a forward slash, as shown above.

### Writing Integration Tests

Each command is documented in its own Markdown file in [`docs/`](https://github.com/ontodev/robot/tree/master/docs). These files are used to generate the [documentation](http://robot.obolibrary.org/). The embedded examples in these Markdown files are parsed and executed as part of our integration tests, with the results compared against a known-good set of outputs. The [`diff`](http://robot.obolibrary.org/diff) functionality is used when comparing ontology files, and a standard `diff` is used for all other file types. This "executable documentation" serves as end-to-end tests of the `robot.jar` file against a number of examples, and also tests that our documented examples do what they should.

The integration tests are executed with `mvn verify`, which is run on all pull requests via Travis CI.

Embedded examples for testing must use Markdown [indented code blocks](https://github.github.com/gfm/#indented-code-blocks), where each line begins with four spaces. To provide code examples that *will not* be tested, use [fenced code blocks](https://github.github.com/gfm/#fenced-code-blocks) instead, beginning and ending with three backticks (\`\`\`).

Each integration test should have at least two corresponding files in the [`docs/examples/`](https://github.com/ontodev/robot/tree/master/docs/examples) directory: one or more input files and a known-good output file. When writing the example in the documentation, the inputs must be just the file names (no directories) and the output should be the known-good file name prefixed by `results/`:

```
robot my-command --input my-file.owl --output results/known-good.owl
```

The `results/known-good.owl` file will be compared to the file with the same name in the `docs/examples/` directory.

### Documenting Errors

ROBOT implements a custom error-handling system that wraps any Java `Exception`. Each `*Operation.java` and the matching `*Command.java` share a namespace that points to the documentation URL. For example in [`ExtractOperation.java`, line 34](https://github.com/ontodev/robot/blob/master/robot-core/src/main/java/org/obolibrary/robot/ExtractOperation.java#L34):

```
/** Namespace for errors. */
private static final String NS = "extract#";
```

If the `NS` class variable is not defined, add that variable to match the name of the command or operation followed by `#` (see `extract` example above). Some files may point to the `global#` namespace if they are not connected to a specific ROBOT command, such as `CommandLineHelper.java` and `IOHelper.java`.

Each specific error message is a class variable formatted as a concatenation of `NS` plus the name of the error in all uppercase letters, followed by a brief description:

```
private static final String nameOfError = NS + "NAME OF ERROR description of error";
```

This class variable should be passed when throwing an `Exception`. For example, the following error in [`ExtractOperation.java`, line 121](https://github.com/ontodev/robot/blob/master/robot-core/src/main/java/org/obolibrary/robot/ExtractOperation.java#L121) corresponds with [Extract - Unknown Individuals Error](http://robot.obolibrary.org/extract#unknown-individuals-error):

```
throw new IllegalArgumentException(String.format(unknownIndividualsError, individuals));
```

When writing the documentation for the error in `docs/*.md`, the `NAME OF ERROR` portion should exactly match the header of the error on the command's documentation page. ROBOT uses the `NS` and the `NAME OF ERROR` to create a link to the error documentation that will be printed on the command line, along with the error message itself. For example, the `UNKNOWN INDIVIDUALS ERROR` above displays:

```
UNKNOWN INDIVIDUALS ERROR 'x' is not a valid --individuals argument
For details see: http://robot.obolibrary.org/extract#unknown-individuals-error
Use the -vvv option to show the stack trace.
Use the --help option to see usage information.
```

The text below the header in the documentation should be an extended description of what causes the error and how the user can fix it.

If the documentation page does not yet have an error section, place one at the bottom of the page using the 'Error Messages' header (see [Extract - Error Messages](http://robot.obolibrary.org/extract#error-messages) for an example):

```
---

## Error Messages
```

## `Dockerfile`

# Stage 1: Build the application using Maven
FROM maven:3-openjdk-11-slim AS build

# Create a working directory and set permissions
RUN useradd -m robot
RUN mkdir -p /usr/src/app
RUN chown robot /usr/src/app

WORKDIR /usr/src/app

# Copy the POM and source code to the working directory
COPY pom.xml /usr/src/app
COPY robot-command /usr/src/app/robot-command
COPY robot-core /usr/src/app/robot-core
COPY robot-maven-plugin /usr/src/app/robot-maven-plugin
COPY robot-mock-plugin /usr/src/app/robot-mock-plugin

# Change ownership to robot user
RUN chown -R robot:robot /usr/src/app

# Use the robot user to run Maven
USER robot

# Run the Maven build, skipping tests to speed up the process
RUN mvn install -DskipTests

# Stage 2: Create a smaller runtime container
FROM openjdk:11-jre-slim AS runtime

# Create a non-root user and set up a working directory
RUN useradd -m robot
RUN mkdir -p /usr/src/app/bin
RUN chown robot /usr/src/app/bin

# Copy the compiled JAR file from the build stage to the runtime stage
COPY --from=build /usr/src/app/bin/robot.jar /usr/src/app/bin/robot.jar

# Set robot as the user
USER robot

# Set the entrypoint to run the robot.jar
ENTRYPOINT ["java", "-jar", "/usr/src/app/bin/robot.jar"]

## `docs/index.md`

---
layout: default
title: ROBOT is an OBO Tool
---

# ROBOT is an OBO Tool

ROBOT is a tool for working with [Open Biomedical Ontologies](http://obofoundry.org). It can be used as a command-line tool or as a library for any language on the Java Virtual Machine.

Click on the command names in the sidebar for documentation and examples, and visit our JavaDocs for [`robot-core`](http://www.javadoc.io/doc/org.obolibrary.robot/robot-core/) and [`robot-command`](http://www.javadoc.io/doc/org.obolibrary.robot/robot-command/) for technical details.

For a "how-to" covering the major commands and features of ROBOT, visit our tutorial [located here](https://github.com/rctauber/robot-tutorial).

### Cite ROBOT

R.C. Jackson, J.P. Balhoff, E. Douglass, N.L. Harris, C.J. Mungall, and J.A. Overton. [ROBOT: A tool for automating ontology workflows](https://rdcu.be/bMnHT). BMC Bioinformatics, vol. 20, July 2019.


## 1. Getting Started

The command-line tool is packaged a Java JAR file and can be run via the `robot` shell script. Before getting started, make sure you have [Java 11 or later](https://www.oracle.com/java/technologies/javase/jdk11-archive-downloads.html) installed. Check by entering `java -version` on the command line.

### Mac & Linux

1. Download the `robot.jar` file from the [latest release](https://github.com/ontodev/robot/releases/latest).
2. Save the [ROBOT shell script](https://github.com/ontodev/robot/raw/master/bin/robot).
    - OR enter `curl https://raw.githubusercontent.com/ontodev/robot/master/bin/robot > robot` in the same directory as `robot.jar` to download it from the terminal.
    - Then, make sure the script is executable: `sudo chmod u+x [path-to-robot-script]` (replace `[path-to-robot-script]` with your location)
3. Put both files on your [system PATH](https://en.wikipedia.org/wiki/PATH_(variable)) in the same directory.
    - this could be `/usr/local/bin/`
    - OR [update your PATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html) to include the new directory. Follow the Solaris/Linux directions for Mac OS, except instead of updating `.bashrc`, you will need to update your `.bash_profile`.
4. Make sure `robot` is executable by running `sudo chmod +x robot` from the terminal in the same directory. This will require you to enter you password.
5. Now you should be able to run ROBOT from a command line:

        robot help

### Windows

1. Download the `robot.jar` file from the [latest release](https://github.com/ontodev/robot/releases/latest).
2. Save the [ROBOT batch script](https://github.com/ontodev/robot/raw/master/bin/robot.bat).
    - Make sure this is saved as `.bat` and not `.bat.txt`
    - OR in [PowerShell](https://learn.microsoft.com/powershell/), run `"java %ROBOT_JAVA_ARGS% -jar %~dp0robot.jar %*" | out-file robot.bat -encoding utf8` in the same directory as `robot.jar` to create the batch script.
    - Note that the above command requires PowerShell version 6 or later: previous versions will write a Unicode byte order mark (BOM) to the file, which breaks the command.
3. Put both files on your [system PATH](https://en.wikipedia.org/wiki/PATH_(variable)) in the same directory.
    - this could be `C:\Windows\`
    - OR [update your PATH](https://docs.oracle.com/javase/tutorial/essential/environment/paths.html) to include the new directory.
4. Make sure `robot.bat` is executable by running `icacls robot.bat /grant Users:RX /T` from the command prompt in the same directory.
5. Now you should be able to run ROBOT from a command line:

        robot help

### Docker

ROBOT is part of the [Ontology Development Kit](https://github.com/INCATools/ontology-development-kit) Docker image, and as a [stand-alone Docker image](https://hub.docker.com/r/obolibrary/robot/tags).

To use the Docker image, you can install it like this:

```
docker pull obolibrary/robot
```

To use the Docker image, you can run:

```
docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot --version
```

Or, on Windows:

```
docker run -v D:/ontology:/work --rm -ti obolibrary/robot robot --version
```

Where `D:/ontology` is the directory that contains the ontology or ontologies you want to work on (there is no equivalent for $PWD on Windows when running a command on the command line directly).

## 2. Using the Library

ROBOT is written in Java, and can be used from any language that runs on the Java Virtual Machine. It's available on [Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.obolibrary.robot%22%20a%3A%22robot%22) and [javadoc.io](http://www.javadoc.io/doc/org.obolibrary.robot/robot/). The code is divided into two parts:

1. [`robot-core`](https://github.com/ontodev/robot/tree/master/robot-core/src/main/java/org/obolibrary/robot) is a library of operations for working with ontologies ([Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.obolibrary.robot%22%20a%3A%22robot-core%22), [javadoc.io](http://www.javadoc.io/doc/org.obolibrary.robot/robot-core/))
2. [`robot-command`](https://github.com/ontodev/robot/tree/master/robot-command/src/main/java/org/obolibrary/robot) is a command-line interface for using those operations ([Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.obolibrary.robot%22%20a%3A%22robot-command%22), [javadoc.io](http://www.javadoc.io/doc/org.obolibrary.robot/robot-command/))

You can also download the standalone `robot.jar` file from the [latest release](https://github.com/ontodev/robot/releases/latest) to include in your projects.

The `robot-core` library provides a number of Operation classes for working with ontologies. The `IOHelper` class contains convenient methods for loading and saving ontologies, and for loading sets of term IRIs. Here's an example of extracting a "core" subset from an ontology:

    IOHelper ioHelper = new IOHelper();
    OWLOntology full = ioHelper.loadOntology("ontology.owl");
    Set<IRI> coreTerms = ioHelper.loadTerms("coreTerms.txt");
    OWLOntology core = ExtractOperation.extract(full, coreTerms);
    ioHelper.saveOntology(core, "core.owl");

Alternatively:

    IOHelper ioHelper = new IOHelper();
    ioHelper.saveOntology(
      ExtractOperation.extract(
        ioHelper.loadOntology("ontology.owl"),
        ioHelper.loadTerms("coreTerms.txt"),
        IRI.create("http://example.com")
      ),
      'core.owl'
    );
