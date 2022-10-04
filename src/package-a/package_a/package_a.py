import pandas as pd

import package_b as pb


def print_version() -> None:
    print(pb.__version__)
    print(pd.__version__)
