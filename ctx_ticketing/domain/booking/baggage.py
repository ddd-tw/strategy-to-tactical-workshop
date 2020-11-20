from typing import cast
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject


@dataclass(frozen=True)
class AdditionalBaggage(ValueObject):
    weight: int
    unit: str

    def __eq__(self, other: object) -> bool:
        if other is None: return False
        if type(self) != type(other): return False
        other = cast(AdditionalBaggage, other)
        return (self.weight, self.unit, self.flight_number) \
            == (other.weight, other.unit, other.flight_number)

    def __hash__(self) -> int:
        return hash((self.weight, self.unit, self.flight_number))