from typing import List
from enum import Enum
from pydomain.basecls.aggregate import AggregateRoot
from .booking_id import BookingId
from .itinerary import Itinerary
from .contactinfo import ContactInfo


class BookingState(Enum):
    Editing = 0,
    Established = 1,
    Discord = 2
    PayToFinished = 3


class TripType(Enum):
    """
    旅程類型
    """
    OneWay = "OneWay",
    RoundTrip = "RoundTrip"


class BookingInfo(AggregateRoot):
    def __init__(self,
                 bkid: BookingId,
                 state: BookingState,
                 trip_type: TripType,
                 itineraries: List[Itinerary],
                 contactinfo: ContactInfo) -> None:
        self._booking_id = bkid
        self._state = state
        self._trip_type = trip_type
        self._itineraries = itineraries
        self._contactinfo = contactinfo

    @classmethod
    def create(cls,
               bkid: BookingId,
               trip_type: TripType,
               itineraries: List[Itinerary],
               contact: ContactInfo) -> "BookingInfo":

        return cls(bkid, BookingState.Established, trip_type, itineraries, contact)
