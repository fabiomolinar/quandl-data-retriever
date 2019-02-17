""" Server module

Quandl API limits:
Authenticated users have a limit of 300 calls per 10 seconds, 
2,000 calls per 10 minutes and a limit of 50,000 calls per day.
"""
import urllib
from twisted.internet import reactor
from twisted.web.client import Agent

import settings

API_KEY = settings.QUANDL_API_KEY

def main():
    uri = urllib.parse.urlunparse((
        settings.QUANDL_API_ENDPOINT["scheme"],
        settings.QUANDL_API_ENDPOINT["netloc"],
        settings.QUANDL_API_ENDPOINT["path"] + 
            settings.QUANDL_API_DATATYPE["timeseries"] + 
            "WIKI/FB/data.json",
        "",
        "api_key=" + API_KEY,
        ""
    ))
    agent = Agent(reactor)
    d = agent.request(
        "GET",
        str.encode(uri)
    )
    
    def cbResponse(response):
        print("called")
    d.addCallback(cbResponse)
    
    def cbShutdown(ignored):
        reactor.stop()
    d.addBoth(cbShutdown)

    reactor.run()
