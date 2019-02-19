""" Server module

Quandl API limits:
Authenticated users have a limit of 300 calls per 10 seconds, 
2,000 calls per 10 minutes and a limit of 50,000 calls per day.
"""
import urllib
import logging

from twisted.internet import reactor
from twisted.web.client import Agent, readBody

from . import settings

API_KEY = settings.QUANDL_API_KEY
logger = logging.getLogger(settings.LOG_NAME + ".server")

def main():
    agent = Agent(reactor)
    d = agent.request(
        b"GET",
        str.encode(uri, 'ascii')
    )
    
    def cbResponse(response):
        if response.code == 200:
            def cbBody(body):
                # do something with JSON
                pass
            d = readBody(response)
            d.addCallback(cbBody)
            return d
    d.addCallback(cbResponse)
    
    def cbShutdown(ignored):
        logger.warning("request failed.")
        reactor.stop()
    d.addBoth(cbShutdown)

    reactor.run()

if __name__ == "__main__":
    main()