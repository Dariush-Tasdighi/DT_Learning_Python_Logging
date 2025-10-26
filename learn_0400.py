# در روش ذیل، صرفا لاگ‌های این فایل در فایل لاگ ذخیره می‌شود
# و لاگ‌های ماژول‌ها، در فایل لاگ نمی‌شوند

import os
import logging
from rich import print
import learn_0400_module as my_module

LOGGING_ENCODING: str = "utf-8"
LOGGING_FILE_PATH: str = "./app_0400.log"
LOGGING_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
LOGGING_FORMAT: str = (
    "%(asctime)s,%(msecs)03d [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s"
)

logging.basicConfig(
    level=logging.DEBUG,
    format=LOGGING_FORMAT,
    encoding=LOGGING_ENCODING,
    datefmt=LOGGING_DATE_FORMAT,
)

formatter = logging.Formatter(
    fmt=LOGGING_FORMAT,
    datefmt=LOGGING_DATE_FORMAT,
)

file_handler = logging.FileHandler(
    encoding=LOGGING_ENCODING,
    filename=LOGGING_FILE_PATH,
)

file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(fmt=formatter)

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=file_handler)


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
    main()
