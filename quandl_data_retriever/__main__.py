import settings
import server
import logging
import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    if settings.DEBUG == True:
        loop.set_debug(True)
        logging.getLogger('asyncio').setLevel(logging.DEBUG)
    loop.run_until_complete(server.main())
    loop.close()