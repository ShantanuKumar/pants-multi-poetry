ARG build_for=linux/x86_64
FROM --platform=$build_for public.ecr.aws/docker/library/python:3.9.13-slim-bullseye as base

RUN apt-get -qq update && \
    apt-get -y install curl && \
    python -m ensurepip

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /build

COPY pants.toml .
COPY pants .

RUN ./pants --version

COPY common_a_b.lock .
COPY multi-poetry.lock .

COPY src/ ./src/

RUN ./pants package src/package_a:pex_package_a

FROM --platform=$build_for public.ecr.aws/docker/library/python:3.9.13-slim-bullseye
COPY --from=base /build/dist/src.package_a/pex_package_a.pex /bin/helloworld
ENTRYPOINT ["/bin/helloworld"]
