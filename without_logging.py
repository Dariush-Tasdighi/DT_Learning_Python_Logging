import os
from rich import print
import learn_0600_module as my_module


def main() -> None:
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")

    print("Hello, World!")

    my_module.do_something()


if __name__ == "__main__":
    main()
