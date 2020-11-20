from enum import Enum
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject
from .money import Money


class CabinClassType(Enum):
    """
    艙等代號類型
    """
    Economy = "M",
    PremiumEconomy = "P",
    Bussines = "B",
    First = "F"


@dataclass(frozen=True)
class FlightInfo(ValueObject):
    flight_number: str
    aircraft: str
    cabin_class: CabinClassType
    fee: Money
