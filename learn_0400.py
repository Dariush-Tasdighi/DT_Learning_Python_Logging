# در روش ذیل، صرفا لاگ‌های
# این فایل، در فایل لاگ ذخیره می‌گردد
# و لاگ‌های ماژول‌ها، در فایل، لاگ نمی‌شوند

import os
import logging
from rich import print
import learn_0400_module as my_module

FILE_MODE: str = "at"
ENCODING: str = "utf-8"
FILE_PATH: str = "./app_0400.log"
DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
FORMAT: str = (
    "%(asctime)s,%(msecs)3d [%(levelname)-8s] [%(filename)s:%(lineno) 3d] - %(message)s"
)

logging.basicConfig(
    level=logging.DEBUG,
    format=FORMAT,
    encoding=ENCODING,
    datefmt=DATE_FORMAT,
)

formatter = logging.Formatter(
    fmt=FORMAT,
    datefmt=DATE_FORMAT,
)

file_handler = logging.FileHandler(
    mode=FILE_MODE,
    encoding=ENCODING,
    filename=FILE_PATH,
)

file_handler.setFormatter(fmt=formatter)
file_handler.setLevel(level=logging.WARNING)

logger = logging.getLogger(name=__name__)
logger.addHandler(hdlr=file_handler)


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
    main()
