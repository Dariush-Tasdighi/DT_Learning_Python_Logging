"""
Lightweight logging configuration helpers - Version 1.0

This module provides a small, dependency-free helper for configuring Python's
standard logging module with sane defaults for both console and file output.
It is intended for small scripts, applications, and learning purposes where a
simple, consistent logging setup is desired without repeating boilerplate in
multiple modules.

Features
- Configure a root logger with a console (stream) handler and a file handler.
- Uses a readable, timestamped formatter with millisecond precision.
- Keeps the root logger at DEBUG and lets handlers filter messages by level.

Public API
- setup_logging(console_level=logging.DEBUG,
                file_level=logging.WARNING,
                file_path: str = "./app.log") -> None
    Configure the root logger with a console and file handler.

Usage example
    import logging
    from dt_logging import setup_logging

    setup_logging(console_level=logging.INFO, file_level=logging.DEBUG, file_path="./myapp.log")

Notes
- Call `setup_logging` early in your application's startup (before emitting
  many log messages) to avoid reconfiguration races.
- The root logger is set to DEBUG to allow handlers to perform level filtering.
"""

import logging

ENCODING: str = "utf-8"
DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
FORMAT: str = (
    "%(asctime)s,%(msecs)03d [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s"
)


def setup_logging(
    console_level=logging.DEBUG,
    file_level=logging.WARNING,
    file_path: str = "./app.log",
) -> None:
    """Setup Logging"""

    root = logging.getLogger()

    # Note: Remove existing handlers
    # for avoiding duplicate logs on reconfigure!
    for handler in root.handlers[:]:
        root.removeHandler(hdlr=handler)

    # Note: let handlers decide what to emit
    # keep root at lowest useful level
    root.setLevel(level=logging.DEBUG)

    formatter = logging.Formatter(
        fmt=FORMAT,
        datefmt=DATE_FORMAT,
    )

    # File Handler:

    file_handler = logging.FileHandler(
        encoding=ENCODING,
        filename=file_path,
    )

    file_handler.setFormatter(fmt=formatter)
    file_handler.setLevel(level=file_level)

    root.addHandler(hdlr=file_handler)

    # Console Handler:

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(fmt=formatter)
    console_handler.setLevel(level=console_level)

    root.addHandler(hdlr=console_handler)


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!\n")
