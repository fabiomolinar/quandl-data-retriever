""" Server module

Quandl API limits:
Authenticated users have a limit of 300 calls per 10 seconds, 
2,000 calls per 10 minutes and a limit of 50,000 calls per day.
"""
import settings
import quandl
import asyncio
import pandas as pd
import numpy as np

API_KEY = settings.QUANDL_API_KEY

async def main():
    print("My first async def")
