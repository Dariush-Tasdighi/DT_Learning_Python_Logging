import os
import logging
from rich import print
from dt_logging import setup_logging
import learn_0500_module as my_module


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    logger.debug(msg="This is debug.")
    logger.info(msg="This is info.")
    logger.warning(msg="This is warning.")
    logger.error(msg="This is error.")
    logger.critical(msg="This is critical.")

    print()

    logger.debug(msg="سلام")
    logger.info(msg="سلام")
    logger.warning(msg="سلام")
    logger.error(msg="سلام")
    logger.critical(msg="سلام")

    print()

    my_module.do_something()


if __name__ == "__main__":
    setup_logging(file_path="./app_0600.log")
    logger = logging.getLogger(name=__name__)

    main()
