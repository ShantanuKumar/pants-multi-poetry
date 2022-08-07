import pandas as pd

import package_b as pb
import package_a as pa


def main():
    print("inside main")
    print(f"package_a version: {pa.__version__}")
    print(f"package_b version: {pb.__version__}")
    print(f"pandas version: {pd.__version__}")


if __name__ == "__main__":
    main()
