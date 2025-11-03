# **************************************************
# Enable Logging in 7 Steps!
# **************************************************

import os
# Step (1)
import logging
from rich import print
# Step (2)
from dtx_logging import setup_logging
import learn_0600_module as my_module


def main() -> None:
    """Main of program."""

    os.system(command="cls" if os.name == "nt" else "clear")

    logger.debug(msg="This is debug.")
    logger.info(msg="This is info.")
    logger.warning(msg="This is warning.")
    logger.error(msg="This is error.")
    logger.critical(msg="This is critical.")

    print()

    my_module.do_something()

    print()

    logger.debug(msg="سلام")
    logger.info(msg="سلام")
    logger.warning(msg="سلام")
    logger.error(msg="سلام")
    logger.critical(msg="سلام")


if __name__ == "__main__":
    # Step (3)
    setup_logging(file_path="./app_0600.log")

    # Step (4)
    logger = logging.getLogger(name=__name__)

    main()
