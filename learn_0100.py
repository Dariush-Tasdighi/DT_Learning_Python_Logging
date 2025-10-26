import os
from rich import print


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    # روش سنتی
    print("INFO: ...")
    print("DEBUG: ...")
    print()


if __name__ == "__main__":
    main()
