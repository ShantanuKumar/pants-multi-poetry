import package_b as pb
import pandas as pd


def print_version() -> None:
    print(pb.__version__)
    print(pd.__version__)
