from package_a import __version__
from tests.fake.resource import PANTS_VERSION
import importlib


def test_version():
    assert __version__ == "0.1.0"
    assert PANTS_VERSION == "2.14.0rc1"

    gdcm_loaded = importlib.import_module("gdcm")
    assert "ASN1_ParseDump" in dir(gdcm_loaded)
