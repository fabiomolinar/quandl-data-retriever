import os

QUANDL_API_KEY = os.environ.get("QUANDL_KEY", "")
QUANDL_API_ENDPOINT = {
    "scheme": "https",
    "netloc": "www.quandl.com",
    "path": "/api/v3/"
}
QUANDL_API_DATATYPE = {
    "timeseries": "datasets/",
    "tables": "datatables/"
}
DEBUG = os.environ.get("DEBUG_MODE", "False") == "True"
# Every how many seconds should we ask for data
FREQUENCY = 10 * 60