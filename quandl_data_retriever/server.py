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
from . import resources

API_KEY = settings.QUANDL_API_KEY
logger = logging.getLogger(settings.LOG_NAME + ".server")

def main():
    from .data import data_list
    try:
        resource_name = data_list[0]["resource"]
        resource = resources.__dict__[resource_name]
        key = data_list[0]["api_key"]
        key = settings.__dict__[key]
        resource = resource(key)
    except KeyError as e:
        logger.warning("KeyError while trying to instantiate Resource class with : " + str(e))
    else:        
        # TODO: go to next item
        pass
    
    url = resource.get_url(data_list[0]["url"])
    agent = Agent(reactor)
    d = agent.request(
        str.encode(data_list[0]["method"], "utf-8"),
        str.encode(url, "ascii")
    )
    
    def cbResponse(response):
        if response.code == 200:
            def cbBody(body):
                resource.save(body)
                pass
            d = readBody(response)
            d.addCallback(cbBody)
            return d
    d.addCallback(cbResponse)
    
    def cbShutdown(ignored):
        if not ignored:
            logger.warning("request failed.")
        reactor.stop()
    d.addBoth(cbShutdown)

    reactor.run()

if __name__ == "__main__":
    main()