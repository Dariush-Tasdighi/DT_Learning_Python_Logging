import os
import logging
from rich import print
import learn_0500_module as my_module

FILE_MODE: str = "at"
FILE_ENCODING: str = "utf-8"
DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
FORMAT: str = (
    "%(asctime)s,%(msecs)3d [%(levelname)-8s] [%(filename)s:%(lineno) 3d] - %(message)s"
)


# NEW
def setup_logging(
    console_level=logging.DEBUG,
    file_level=logging.WARNING,
    file_path: str = "./app.log",
) -> None:
    """Setup Logging"""

    root = logging.getLogger()

    # Let handlers decide what to emit
    # keep root at lowest useful level
    root.setLevel(level=logging.DEBUG)

    # از بین بردن تمام پیش‌فرض‌ها
    # Remove existing handlers for
    # avoiding duplicate logs on reconfigure!
    for handler in root.handlers:
        root.removeHandler(hdlr=handler)

    formatter = logging.Formatter(
        fmt=FORMAT,
        datefmt=DATE_FORMAT,
    )

    # Console Handler:

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(fmt=formatter)
    console_handler.setLevel(level=console_level)

    root.addHandler(hdlr=console_handler)

    # File Handler:

    file_handler = logging.FileHandler(
        mode=FILE_MODE,
        filename=file_path,
        encoding=FILE_ENCODING,
    )

    file_handler.setFormatter(fmt=formatter)
    file_handler.setLevel(level=file_level)

    root.addHandler(hdlr=file_handler)


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
    # NEW
    setup_logging(file_path="./app_0500.log")
    logger = logging.getLogger(name=__name__)

    main()
