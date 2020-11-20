from enum import Enum
from typing import cast, List
from datetime import datetime
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject
from .passenger import Passenger
from .baggage import AdditionalBaggage
from .flightinfo import FlightInfo


class PassengerReservation(ValueObject):
    passenger: Passenger
    extra_baggage: AdditionalBaggage


@dataclass(frozen=True)
class Itinerary(ValueObject):
    departing_at: datetime
    arriving_at: datetime
    departure: str
    destiation: str
    flight: FlightInfo
    passengers_resv: List[PassengerReservation]
