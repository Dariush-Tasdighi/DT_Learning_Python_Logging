import os
import logging
from rich import print
import learn_0500_module as my_module

LOGGING_ENCODING: str = "utf-8"
LOGGING_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
LOGGING_FORMAT: str = (
    "%(asctime)s,%(msecs)03d [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s"
)


def setup_logging(
    console_level=logging.DEBUG,
    file_level=logging.WARNING,
    file_path: str = "./app.log",
) -> None:
    """Setup Logging"""

    root = logging.getLogger()

    # remove existing handlers (avoid duplicate logs on reconfigure)
    for handler in root.handlers[:]:
        root.removeHandler(hdlr=handler)

    # let handlers decide what to emit; keep root at lowest useful level
    root.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter(
        fmt=LOGGING_FORMAT,
        datefmt=LOGGING_DATE_FORMAT,
    )

    # File Handler:

    file_handler = logging.FileHandler(
        filename=file_path,
        encoding=LOGGING_ENCODING,
    )

    file_handler.setFormatter(fmt=formatter)
    file_handler.setLevel(level=file_level)

    root.addHandler(hdlr=file_handler)

    # Console Handler:

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(fmt=formatter)
    console_handler.setLevel(level=console_level)

    root.addHandler(hdlr=console_handler)


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
    setup_logging(file_path="./app_0500.log")
    logger = logging.getLogger(name=__name__)

    main()
