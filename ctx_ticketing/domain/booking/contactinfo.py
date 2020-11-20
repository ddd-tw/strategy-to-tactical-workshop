from typing import cast, Optional
from dataclasses import dataclass
from pydomain.basecls.valueobject import ValueObject


@dataclass(frozen=True)
class ContactInfo(ValueObject):
    email: str
    country_code: str
    mobile: str
    telephone: Optional[str]

    def __eq__(self, other: object) -> bool:
        if other is None: return False
        if type(self) != type(other): return False
        other = cast(ContactInfo, other)
        return (self.email, self.country_code, self.mobile, self.telephone) \
            == (other.email, other.country_code, other.mobile, other.telephone)

    def __hash__(self) -> int:
        return hash((self.email, self.country_code, self.mobile, self.telephone))
