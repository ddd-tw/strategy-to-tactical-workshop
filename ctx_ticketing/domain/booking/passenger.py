from enum import Enum
from typing import cast
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject


class SalutationType(Enum):
    Mr = 0,
    Miss = 1,
    Ms = 2,
    Mrs = 3
    Dr = 4


class AgeGroupType(Enum):
    Adult = 0,
    Child = 1,
    Baby = 2


@dataclass(frozen=True)
class Passenger(ValueObject):
    family_name: str
    given_name: str
    passport_number: str
    salutation: SalutationType
    age_type: AgeGroupType

    def __eq__(self, other: object) -> bool:
        if other is None: return False
        if type(self) != type(other): return False
        other = cast(Passenger, other)
        return (self.salutation, self.family_name, self.given_name, self.age_type, self.passport_number) \
            == (other.salutation, other.family_name, other.given_name, other.age_type, other.passport_number)

    def __hash__(self) -> int:
        return hash((self.salutation, self.family_name, self.given_name, self.age_type, self.passport_number))