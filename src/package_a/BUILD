python_sources(resolve="common_a_b")

python_distribution(
    name="package-a",
    dependencies=[":package_a"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="package_a",
        description="package_a",
        version="0.1.0",
    ),
    generate_setup=True,
)
