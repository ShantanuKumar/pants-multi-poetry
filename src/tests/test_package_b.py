# from package_b import __version__
import pandas as pd

import package_b


def test_version():
    assert package_b.__version__ == "0.1.0"
    assert pd.__version__ is not None
