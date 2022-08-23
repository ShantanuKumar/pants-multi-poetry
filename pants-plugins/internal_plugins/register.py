from pants.backend.python.goals.setup_py import SetupKwargs, SetupKwargsRequest
from pants.engine.fs import DigestContents, GlobMatchErrorBehavior, PathGlobs
from pants.engine.rules import Get, collect_rules, rule
from pants.engine.target import Target
from pants.engine.unions import UnionRule


class PyfleetSetupKwargsRequest(SetupKwargsRequest):
    @classmethod
    def is_applicable(cls, _: Target) -> bool:
        # We always use our custom `setup()` kwargs generator for `python_distribution` targets in
        # this repo.
        return True


@rule
async def pyfleet_setup_kwargs_plugin(request: PyfleetSetupKwargsRequest) -> SetupKwargs:
    """Custom setup kwarg for reading version."""

    kwargs = request.explicit_kwargs.copy()

    if request.target.address.path_safe_spec.startswith("tests"):
        return SetupKwargs(kwargs, address=request.target.address)

    # Validate that required fields are set.
    if not kwargs["name"].startswith("pyfleet"):
        raise ValueError(
            f"Invalid `name` kwarg in the `provides` field for {request.target.address}. The name "
            f"must start with 'pyfleet', but was {kwargs['name']}."
        )
    if "description" not in kwargs:
        raise ValueError(
            f"Missing a `description` kwarg in the `provides` field for {request.target.address}."
        )

    if "version" in kwargs:
        raise ValueError(
            "version is only supported to be read from VERSION file, don't provide it manually."
        )

    digest_contents = await Get(
        DigestContents,
        PathGlobs(
            ["**/VERSION"],
            description_of_origin="`setup_py()` plugin",
            glob_match_error_behavior=GlobMatchErrorBehavior.error,
        ),
    )
    version = digest_contents[0].content.decode()
    if not version:
        raise ValueError("version can't be read from VERSION")

    return SetupKwargs(
        {**request.explicit_kwargs, "version": version}, address=request.target.address
    )


def rules():
    return [
        *collect_rules(),
        UnionRule(SetupKwargsRequest, PyfleetSetupKwargsRequest),
    ]
