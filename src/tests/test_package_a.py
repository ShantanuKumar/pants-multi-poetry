import package_b
from package_a import __version__


def test_version():
    assert __version__ == "0.1.0"
    assert package_b.__version__ == "0.1.0"
