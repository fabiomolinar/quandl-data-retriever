import settings
import quandl
import pandas as pd
import numpy as np

def main():
    api_key = settings.QUANDL_API_KEY
    quandl.ApiConfig.api_key = api_key
    data = quandl.get("EIA/PET_RWTC_D")
    print(data)
