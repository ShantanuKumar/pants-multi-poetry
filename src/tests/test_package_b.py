from package_b import __version__
import pandas as pd


def test_version():
    assert __version__ == '0.1.0'
    assert pd.__version__ is not None
