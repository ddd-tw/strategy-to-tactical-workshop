from enum import Enum
from typing import cast
from decimal import Decimal
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject


class Currency(Enum):
    TWD = "TWD"
    USD = "USD"


@dataclass(frozen=True)
class Money(ValueObject):
    amount: Decimal
    curreny: Currency

    # def __eq__(self, other: object) -> bool:
    #     if other is None: return False
    #     if type(self) != type(other): return False
    #     other = cast(Money, other)
    #     return (self.amount, self.curreny) == (other.amount, other.curreny)

    # def __hash__(self) -> int:
    #     return hash((self.amount, self.curreny))
