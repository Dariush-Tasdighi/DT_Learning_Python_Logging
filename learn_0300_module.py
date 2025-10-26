import logging

logger = logging.getLogger(name=__name__)


def do_something() -> None:
    """Do something function."""

    logger.debug(msg="This is debug.")
    logger.info(msg="This is info.")
    logger.warning(msg="This is warning.")
    logger.error(msg="This is error.")
    logger.critical(msg="This is critical.")

    print()


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!\n")
