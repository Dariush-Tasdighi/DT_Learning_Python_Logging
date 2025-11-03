# **************************************************
# Default: Console
# Default: Warning
# **************************************************
# نیازی به نصب هیچ پکیجی نیست
# **************************************************
import logging

logging.log(level=logging.DEBUG, msg="Debug...")
logging.log(level=logging.INFO, msg="Info...")
logging.log(level=logging.WARNING, msg="Warning...")  # Default
logging.log(level=logging.ERROR, msg="Error...")
logging.log(level=logging.CRITICAL, msg="Critical...")
# **************************************************


# **************************************************
# import logging

# logging.debug(msg="Debug...")
# logging.info(msg="Info...")
# logging.warning(msg="Warning...")  # Default
# logging.error(msg="Error...")
# logging.critical(msg="Critical...")
# **************************************************


# **************************************************
# Error Handling
# **************************************************
# try:
#     result = 1 / 0

# except Exception as e:
#     print(f"Error! {e}")
# **************************************************


# **************************************************
# try:
#     result = 1 / 0

# except Exception as e:
#     print(f"Error: {e}!")
# **************************************************


# **************************************************
# try:
#     result = 1 / 0

# except Exception as e:
#     print(f"[-] {e}!\n")
# **************************************************


# **************************************************
# import logging

# try:
#     result = 1 / 0

# except Exception as e:
#     logging.error(msg=e)
# **************************************************


# **************************************************
# import logging

# try:
#     result = 1 / 0

# except Exception as e:
#     logging.error(msg=e, exc_info=True)
# **************************************************


# **************************************************
# import logging

# try:
#     result = 1 / 0

# except Exception as e:
#     logging.exception(msg=e)
# **************************************************


# **************************************************
# Change Default of Log Level
# **************************************************
# import logging

# # NEW
# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(level=logging.WARNING)  # Default
# # logging.basicConfig(level=logging.ERROR)
# # logging.basicConfig(level=logging.CRITICAL)

# logging.debug(msg="Debug...")
# logging.info(msg="Info...")
# logging.warning(msg="Warning...")  # Default
# logging.error(msg="Error...")
# logging.critical(msg="Critical...")
# **************************************************


# **************************************************
# Log to (JUST) File
# **************************************************
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     # NEW
#     encoding="utf-8",
#     filename="./app_0200.log",
#     filemode="wt",  # Default: "at"
# )

# logging.debug(msg="Debug...")
# logging.info(msg="Info...")
# logging.warning(msg="Warning...")
# logging.error(msg="Error...")
# logging.critical(msg="Critical...")
# **************************************************


# **************************************************
# Change the Format
#
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# **************************************************
# import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     # NEW
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     # format="%(asctime)s - [%(levelname)-8s] - %(message)s",
#     # format="%(asctime)s - [%(levelname)-8s] - %(name)s - %(message)s",
# )

# logging.debug(msg="Debug...")
# logging.info(msg="Info...")
# logging.warning(msg="Warning...")
# logging.error(msg="Error...")
# logging.critical(msg="Critical...")
# **************************************************


# **************************************************
# root -> Resevered
#   Magooli
#   Googooli
#   ...
# **************************************************


# **************************************************
# Custom Logger
# **************************************************
# import logging

# # NEW: root -> Googooli
# logger = logging.getLogger(name="Googooli")

# # NEW: logging -> logger
# logger.debug(msg="Debug...")
# logger.info(msg="Info...")
# logger.warning(msg="Warning...")  # Default
# logger.error(msg="Error...")
# logger.critical(msg="Critical...")
# **************************************************


# **************************************************
# import logging

# logging.basicConfig(
#     # NEW
#     level=logging.NOTSET,
#     # NEW: %(name)s
#     format="%(asctime)s - [%(levelname)-8s] - %(name)s - %(message)s",
# )

# # NEW: root -> Googooli
# logger_googooli = logging.getLogger(name="Googooli")

# # NEW: root -> Magooli
# logger_magooli = logging.getLogger(name="Magooli")

# logger_googooli.debug(msg="Debug...")  # Default
# logger_googooli.info(msg="Info...")
# logger_googooli.warning(msg="Warning...")
# logger_googooli.error(msg="Error...")
# logger_googooli.critical(msg="Critical...")

# print("-" * 50)

# logger_magooli.debug(msg="Debug...")  # Default
# logger_magooli.info(msg="Info...")
# logger_magooli.warning(msg="Warning...")
# logger_magooli.error(msg="Error...")
# logger_magooli.critical(msg="Critical...")
# **************************************************


# **************************************************
# import logging

# # NEW
# root = logging.getLogger()

# # NEW
# # Let handlers decide what to emit
# # keep root at lowest useful level
# root.setLevel(level=logging.DEBUG)

# # NEW
# # از بین بردن تمام پیش‌فرض‌ها
# # Remove existing handlers for
# # avoiding duplicate logs on reconfigure!
# for handler in root.handlers:
#     root.removeHandler(hdlr=handler)

# # NEW: Best Practice: Googooli -> __name__
# logger = logging.getLogger(name=__name__)

# logger.debug(msg="Debug...")
# logger.info(msg="Info...")
# logger.warning(msg="Warning...")  # Default
# logger.error(msg="Error...")
# logger.critical(msg="Critical...")
# **************************************************


# **************************************************
# StreamHandler: Console Handler
# **************************************************
# import logging

# root = logging.getLogger()
# root.setLevel(level=logging.DEBUG)
# for handler in root.handlers:
#     root.removeHandler(hdlr=handler)

# # NEW
# formatter = logging.Formatter(
#     fmt="%(asctime)s - [%(levelname)-8s] - %(name)s - %(message)s",
# )

# # NEW
# console_handler = logging.StreamHandler()

# # NEW
# console_handler.setFormatter(fmt=formatter)
# console_handler.setLevel(level=logging.DEBUG)

# logger = logging.getLogger(name=__name__)

# # NEW
# logger.addHandler(hdlr=console_handler)

# logger.debug(msg="Debug...")
# logger.info(msg="Info...")
# logger.warning(msg="Warning...")
# logger.error(msg="Error...")
# logger.critical(msg="Critical...")
# **************************************************


# **************************************************
# FileHandler
# **************************************************
# import logging

# root = logging.getLogger()
# root.setLevel(level=logging.DEBUG)
# for handler in root.handlers:
#     root.removeHandler(hdlr=handler)

# formatter = logging.Formatter(
#     fmt="%(asctime)s - [%(levelname)-8s] - %(name)s - %(message)s",
# )

# console_handler = logging.StreamHandler()

# console_handler.setFormatter(fmt=formatter)
# console_handler.setLevel(level=logging.DEBUG)

# # NEW
# file_handler = logging.FileHandler(
#     mode="at",
#     encoding="utf-8",
#     filename="./app_0200.log",
# )

# # NEW
# file_handler.setFormatter(fmt=formatter)
# file_handler.setLevel(level=logging.WARNING)

# logger = logging.getLogger(name=__name__)

# # NEW
# logger.addHandler(hdlr=file_handler)
# logger.addHandler(hdlr=console_handler)

# logger.debug(msg="Debug...")
# logger.info(msg="Info...")
# logger.warning(msg="Warning...")
# logger.error(msg="Error...")
# logger.critical(msg="Critical...")
# **************************************************
