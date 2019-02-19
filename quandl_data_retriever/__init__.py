"""
quandl_data_retriever
"""
import logging

from . import settings

__version__ = "0.1"
__author__ = "Fabio Molinar"

# Logging
logger = logging.getLogger(settings.LOG_NAME)

ch = logging.StreamHandler()
fh = logging.FileHandler('logs.log')
ch.setLevel(settings.LOG_LEVEL)
fh.setLevel(logging.INFO)

cf = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
ff = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(cf)
fh.setFormatter(ff)

logger.addHandler(ch)
logger.addHandler(fh)