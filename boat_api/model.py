from dataclasses import dataclass, field
from marshmallow import Schema, fields
from enum import Enum


class BoatType(Enum):
    C8_DC = "C8 DC"
    C8_CC = "C8 CC"


@dataclass
class Boat:
    name: str
    type: str
    owner: str


class BoatSchema(Schema):
    name = fields.String(required=True)
    type = fields.String(required=True)
    owner = fields.String(required=True)


@dataclass
class BoatPosition:
    boat_id: int
    latitude: float
    longitude: float
    timestamp: str


@dataclass
class ChargingStation:
    name: str
    latitude: float
    longitude: float


class ChargingStationSchema(Schema):
    name = fields.String(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
