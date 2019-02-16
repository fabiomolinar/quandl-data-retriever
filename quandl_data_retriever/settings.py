import os

QUANDL_API_KEY = os.environ.get('QUANDL_KEY', '')
DEBUG = os.environ.get('DEBUG_MODE', 'False') == 'True'
# Every how many seconds should we ask for data
FREQUENCY = 10 * 60