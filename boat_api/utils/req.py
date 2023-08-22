import requests
from cachetools import TTLCache, cached
import logging
from os import getenv

log = logging.getLogger(getenv("APP_NAME"))

TIMEOUT = 2


@cached(cache=TTLCache(maxsize=128, ttl=600))
def api_call(url: str, timeout: int = TIMEOUT) -> requests.Response:
    """Makes a call to the API"""
    log.debug("Fetching from %s", url)
    response = requests.get(url, timeout=timeout)
    log.debug("Done fetching from %s", url)
    return response
