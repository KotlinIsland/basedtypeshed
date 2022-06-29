import datetime
from typing import Any, ClassVar, Protocol, TypeVar
from typing_extensions import Literal

from ..relativedelta import relativedelta
from ._common import _tzinfo as _tzinfo, enfold as enfold, tzname_in_python2 as tzname_in_python2, tzrangebase as tzrangebase

_DT = TypeVar("_DT", bound=datetime.datetime)

ZERO: datetime.timedelta
EPOCH: datetime.datetime
EPOCHORDINAL: int

class tzutc(datetime.tzinfo):
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def is_ambiguous(self, dt: datetime.datetime | None) -> bool: ...
    def fromutc(self, dt: _DT) -> _DT: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__

class tzoffset(datetime.tzinfo):
    def __init__(self, name, offset) -> None: ...
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def is_ambiguous(self, dt: datetime.datetime | None) -> bool: ...
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def fromutc(self, dt: _DT) -> _DT: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__
    @classmethod
    def instance(cls, name, offset) -> tzoffset: ...

class tzlocal(_tzinfo):
    def __init__(self) -> None: ...
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def is_ambiguous(self, dt: datetime.datetime | None) -> bool: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    __reduce__ = object.__reduce__

class _ttinfo:
    def __init__(self) -> None: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...

class _TZFileReader(Protocol):
    # optional attribute:
    # name: str
    def read(self, __size: int) -> bytes: ...
    def seek(self, __target: int, __whence: Literal[1]) -> object: ...

class tzfile(_tzinfo):
    def __init__(self, fileobj: str | _TZFileReader, filename: str | None = ...) -> None: ...
    def is_ambiguous(self, dt: datetime.datetime | None, idx: int | None = ...) -> bool: ...
    def utcoffset(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def dst(self, dt: datetime.datetime | None) -> datetime.timedelta | None: ...
    def tzname(self, dt: datetime.datetime | None) -> str: ...
    def __eq__(self, other): ...
    __hash__: ClassVar[None]  # type: ignore[assignment]
    def __ne__(self, other): ...
    def __reduce__(self): ...
    def __reduce_ex__(self, protocol): ...

class tzrange(tzrangebase):
    hasdst: bool
    def __init__(
        self,
        stdabbr: str,
        stdoffset: int | datetime.timedelta | None = ...,
        dstabbr: str | None = ...,
        dstoffset: int | datetime.timedelta | None = ...,
        start: relativedelta | None = ...,
        end: relativedelta | None = ...,
    ) -> None: ...
    def transitions(self, year: int) -> tuple[datetime.datetime, datetime.datetime]: ...
    def __eq__(self, other): ...

class tzstr(tzrange):
    hasdst: bool
    def __init__(self, s: str, posix_offset: bool = ...) -> None: ...
    @classmethod
    def instance(cls, name, offset) -> tzoffset: ...

class _ICalReader(Protocol):
    # optional attribute:
    # name: str
    def read(self) -> str: ...

class tzical:
    def __init__(self, fileobj: str | _ICalReader) -> None: ...
    def keys(self): ...
    def get(self, tzid: Any | None = ...): ...

TZFILES: list[str]
TZPATHS: list[str]

def datetime_exists(dt: datetime.datetime, tz: datetime.tzinfo | None = ...) -> bool: ...
def datetime_ambiguous(dt: datetime.datetime, tz: datetime.tzinfo | None = ...) -> bool: ...
def resolve_imaginary(dt: datetime.datetime) -> datetime.datetime: ...

class _GetTZ:
    def __call__(self, name: str | None = ...) -> datetime.tzinfo | None: ...
    def nocache(self, name: str | None) -> datetime.tzinfo | None: ...

gettz: _GetTZ
