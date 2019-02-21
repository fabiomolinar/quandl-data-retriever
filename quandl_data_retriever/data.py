import datetime

data_list = [
    {
        "url": "https://www.quandl.com/api/v3/datasets/AAII/AAII_SENTIMENT?start_date=" + datetime.datetime.now().date().strftime("%Y-%m-%d"),
        "method": "GET",
        "api_key": "QUANDL_API_KEY",
        "resource": "Quandl"
    }
]