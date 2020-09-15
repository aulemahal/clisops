# -*- coding: utf-8 -*-
"""Top-level package for clisops."""

import logging
import logging.config
import os

import dask
from roocs_utils.config import get_config

import clisops

from .__version__ import __author__, __email__, __version__

logging.config.fileConfig(
    os.path.join(os.path.dirname(__file__), "etc", "logging.conf")
)
CONFIG = get_config(clisops)


# Set the memory limit for each dask chunk
def get_chunk_mem_limit():
    chunk_memory_limit = CONFIG["clisops:read"].get("chunk_memory_limit", None)
    return chunk_memory_limit


# if chunk_memory_limit:
#     dask.config.set({"array.chunk-size": get_chunk_mem_limit()})


for key, value in CONFIG["environment"].items():
    os.environ[key.upper()] = value
