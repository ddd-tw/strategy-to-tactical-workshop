from typing import cast, Optional
from dataclasses import dataclass
from datetime import datetime
from pydomain.basecls.entity import EntityId


class BookingId(EntityId):
    DATE_FORMAT = "%Y%m%d"

    def __init__(self, code: str, serial_no: str, createtd_at: datetime) -> None:
        if len(code) != 3:
            raise ValueError("The length of Code is 3.")
        if len(serial_no) != 4:
            raise ValueError("The length of Serial No is 4.")
        self._code = code
        self._serial_no = serial_no
        self._createtd_at = createtd_at
        super(BookingId, self).__init__(self._make_identifier())

    @classmethod
    def create(cls, serial_no: str) -> "BookingId":
        return cls("BKD", serial_no, datetime.utcnow())

    @classmethod
    def translate(cls, source: str) -> "BookingId":
        if len(source) != 15:
            raise ValueError("The size of Booking Id format not corret.")
        code, created_time, serial_no = source[:3], source[3:11], source[11:]
        try:
            created_at = datetime.strptime(created_time, cls.DATE_FORMAT)
        except Exception:
            raise ValueError("Booking Id format not correct.")

        return cls(code, serial_no, created_at)

    def _make_identifier(self):
        # 取得字串型別的 Entity Id
        createtd_at = self.createtd_at.strftime(self.DATE_FORMAT)
        return "{code}{date}{sn}".format(code=self.code, date=createtd_at, sn=self.serial_no)

    @property
    def code(self) -> str:
        return self._code

    @property
    def serial_no(self) -> str:
        return self._serial_no

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    def __str__(self) -> str:
        return self._make_identifier()

    def __repr__(self) -> str:
        return "<{cls}: code={code}, createtd_at={date}, serial_no={sn}" \
            .format(cls=type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)
