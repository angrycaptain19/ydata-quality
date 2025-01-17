import logging
from typing import TextIO
import sys
import os
from logging import _nameToLevel

# Default vars for the logger
NAME = os.getenv('DQ_LOGGER_NAME', 'DQ_Logger')


def get_logger(name, stream: TextIO = sys.stdout, level: str = logging.INFO):
    acceptable_levels = [None] + list(_nameToLevel.keys())
    assert level in acceptable_levels, f"Valid levels for warning severity are {acceptable_levels}. \
      Defaults to info level."
    if not level:
        level = logging.INFO  # Default threshold

    handler = logging.StreamHandler(stream)
    handler.setFormatter(
        logging.Formatter("%(levelname)s | %(message)s")
    )

    logger = logging.getLogger(name)
    logger.setLevel(level)

    if len(logger.handlers) == 0:
        logger.addHandler(handler)

    logger.propagate = False

    return logger
