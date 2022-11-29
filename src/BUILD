python_requirements(
    resolve="common_a_b",
    module_mapping={
        "python-gdcm": ["gdcm"],
    },
)

docker_image(
    name="pants-base",
    repository="pyfleet",
    registries=["panion"],
    image_tags=["dev"],
    skip_push=True,
    instructions=[
        "ARG build_for=linux/x86_64",
        "FROM --platform=$build_for public.ecr.aws/docker/library/python:3.9.13-slim-bullseye",
        "RUN apt-get -qq update && apt-get -y install curl && python -m ensurepip",
        "COPY pants.toml .",
        "COPY pants .",
        "RUN ./pants --version",
    ],
)
