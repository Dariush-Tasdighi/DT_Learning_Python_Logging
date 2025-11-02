import os
import logging
from rich import print
import learn_0300_module as my_module

# Step (1)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

# Step (2)
# logging.basicConfig(
#     level=logging.DEBUG,
#     # NEW
#     datefmt="%Y-%m-%dT%H:%M:%S",
#     format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
# )

# Step (3)
# logging.basicConfig(
#     level=logging.DEBUG,
#     datefmt="%Y-%m-%d %H:%M:%S",
#     format="%(asctime)s,%(msecs) 3d [%(levelname)-8s] [%(filename)s:%(lineno) 4d] - %(message)s",
# )

logger = logging.getLogger(name=__name__)


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

    logger.debug(msg="This is debug.")
    logger.info(msg="This is info.")
    logger.warning(msg="This is warning.")
    logger.error(msg="This is error.")
    logger.critical(msg="This is critical.")


if __name__ == "__main__":
    main()
