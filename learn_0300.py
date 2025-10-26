import os
import logging
from rich import print
import learn_0300_module as my_module

# Step (1)
# logging.basicConfig(level=logging.DEBUG)

# Step (2)
# logging.basicConfig(level=logging.ERROR)

# Step (3)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
# )

# Step (4)
# logging.basicConfig(
#     level=logging.DEBUG,
#     datefmt="%Y-%m-%dT%H:%M:%S",
#     format="%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
# )

# Step (5)
logging.basicConfig(
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s,%(msecs)03d [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s",
)

logger = logging.getLogger(name=__name__)
# logger = logging.getLogger(name="Googooli")


def main() -> None:
    """Main function."""

    os.system(command="cls" if os.name == "nt" else "clear")

    logger.debug(msg="This is debug.")
    logger.info(msg="This is info.")
    logger.warning(msg="This is warning.")
    logger.error(msg="This is error.")
    logger.critical(msg="This is critical.")

    print()

    my_module.do_something()


if __name__ == "__main__":
    main()
