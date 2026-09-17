# Architecture evidence: protegeproject/webprotege

- `Dockerfile:3` — MongoDB is needed to run the test suite during the Maven build. Ubuntu no
- `Dockerfile:4` — longer ships a mongodb package, so it comes from MongoDB's official repo.
- `Dockerfile:20` — The runtime image has no unzip, but this stage has a full JDK, so the war
- `Dockerfile:21` — is exploded here and copied into the runtime image as a directory.
- `Dockerfile:27` — Tomcat 9, not 10+: WebProtégé uses the javax.servlet API, which Tomcat 10
- `Dockerfile:28` — replaced with jakarta.servlet.
- `Dockerfile:34` — Here WEBPROTEGE_VERSION is coming from the custom build args WEBPROTEGE_VERSION=$DOCKER_TAG hooks/build script.
- `Dockerfile:35` — Ref: https://docs.docker.com/docker-hub/builds/advanced/
