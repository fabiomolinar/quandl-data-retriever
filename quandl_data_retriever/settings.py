import os
import logging

FORGEONE_API_KEY = os.environ.get("FORGEONE_KEY", "")
QUANDL_API_KEY = os.environ.get("QUANDL_KEY", "")
# Every how many seconds should we ask for data
FREQUENCY = 10 * 60

LOG_NAME = "qdt"
DEBUG = os.environ.get("DEBUG_MODE", "False") == "True"
LOG_LEVEL = os.environ.get("LOG_LEVEL", 30)
if DEBUG:
    LOG_LEVEL = logging.DEBUG