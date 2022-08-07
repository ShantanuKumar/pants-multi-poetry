python_sources(resolve="common_a_b")


python_distribution(
    name="package-b",
    dependencies=[":package_b"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="package_b",
        description="package_b",
        version="0.1.0",
    ),
    generate_setup=True,
)
