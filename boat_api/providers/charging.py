from abc import ABC, abstractmethod
import logging
from os import getenv
import gevent
from boat_api.utils.req import api_call
from boat_api.model import ChargingStation

log = logging.getLogger(getenv("APP_NAME"))


class ProviderAPI(ABC):
    """Represents a API from a provider"""

    TIMEOUT = 2

    def __init__(self, name: str, api_url: str):
        self.name = name
        self.api_url = api_url

    @abstractmethod
    def stations(self, longitude: float, latitude: float) -> list[ChargingStation]:
        """Returns nearby charging stations"""


class ProviderA(ProviderAPI):
    def __init__(self, api_url: str):
        super().__init__(self.__class__.__name__, api_url)

    def stations(self, longitude: float, latitude: float) -> list[ChargingStation]:
        stations = [
            ChargingStation(
                name=f"station_{self.name}_{i}", latitude=latitude, longitude=longitude
            )
            for i in range(10)
        ]
        api_call(self.api_url)
        return stations


class ProviderB(ProviderAPI):
    def __init__(self, api_url: str):
        super().__init__(self.__class__.__name__, api_url)

    def stations(self, longitude: float, latitude: float) -> list[ChargingStation]:
        stations = [
            ChargingStation(
                name=f"station_{self.name}_{i}", latitude=latitude, longitude=longitude
            )
            for i in range(10)
        ]
        api_call(self.api_url)
        return stations


def nearby_stations(
    radius: int, longitude: float, latitude: float
) -> list[ChargingStation]:
    """
    Returns charging stations within a radius from a given position
    """
    providers = {
        "ProviderA": ProviderA(
            api_url="https://www.fdic.gov/bank/individual/failed/banklist.csv"
        ),
        "ProviderB": ProviderB(
            api_url="https://www.fdic.gov/bank/individual/failed/banklist.csv"
        ),
    }

    jobs = [gevent.spawn(providers[p].stations, longitude, latitude) for p in providers]
    gevent.joinall(jobs, timeout=ProviderAPI.TIMEOUT)
    stations = []
    for job in jobs:
        stations += job.value
    return stations
