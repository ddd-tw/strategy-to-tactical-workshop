from enum import Enum
from typing import cast, List
from datetime import datetime
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject
from .passenger import Passenger
from .baggage import AdditionalBaggage
from .flightinfo import FlightInfo


class PassengerResvDemand(ValueObject):
    """
    每位顧客對於該旅程航班預定的需求：包含行李，座位，配餐等
    """
    passenger: Passenger
    extra_baggage: AdditionalBaggage


@dataclass(frozen=True)
class Itinerary(ValueObject):
    """
    旅程資訊：每趟旅程的此次航班資訊與出發抵達時間，以及每位乘客對於該旅行及航班的預定需求
    """
    departing_at: datetime
    arriving_at: datetime
    departure: str
    destiation: str
    flight: FlightInfo
    passengers_demand: List[PassengerResvDemand]

    # def __eq__(self, other: object) -> bool:
    #     if other is None: return False
    #     if type(self) != type(other): return False
    #     other = cast(Itinerary, other)
    #     return (self.departing_at, self.arriving_at, self.departure, self.destiation, self.flight, self.passengers_demand) \
    #         == (other.departing_at, other.arriving_at, other.departure, other.destiation, other.flight, other.passengers_demand)

    # def __hash__(self) -> int:
    #     return hash((self.departing_at, self.arriving_at, self.departure, self.destiation, self.flight, self.passengers_demand))
