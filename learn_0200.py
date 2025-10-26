import os
import logging
from rich import print


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    # **************************************************
    # logging.debug(msg="This is debug.")
    # logging.info(msg="This is info.")
    # logging.warning(msg="This is warning.")
    # logging.error(msg="This is error.")
    # logging.critical(msg="This is critical.")

    # # logging.exception(msg="This is exception.")

    # print()
    # **************************************************

    # **************************************************
    # مهم
    # Default: 'warning'
    logging.basicConfig(level=logging.DEBUG)

    logging.debug(msg="This is debug.")
    logging.info(msg="This is info.")
    logging.warning(msg="This is warning.")
    logging.error(msg="This is error.")
    logging.critical(msg="This is critical.")

    print()
    # **************************************************


if __name__ == "__main__":
    main()
