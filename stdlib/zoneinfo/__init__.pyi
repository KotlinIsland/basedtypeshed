import typing
from _typeshed import Self, StrPath
from datetime import tzinfo
from typing import Any, Iterable, Protocol, Sequence

_T = typing.TypeVar("_T", bound="ZoneInfo")

class _IOBytes(Protocol):
    def read(self, __size: int) -> bytes: ...
    def seek(self, __size: int, __whence: int = ...) -> Any: ...

class ZoneInfo(tzinfo):
    @property
    def key(self) -> str: ...
    def __init__(self, key: str) -> None: ...
    @classmethod
    def no_cache(cls: type[Self], key: str) -> Self: ...
    @classmethod
    def from_file(cls: type[Self], __fobj: _IOBytes, key: str | None = ...) -> Self: ...
    @classmethod
    def clear_cache(cls, *, only_keys: Iterable[str] = ...) -> None: ...

# Note: Both here and in clear_cache, the types allow the use of `str` where
# a sequence of strings is required. This should be remedied if a solution
# to this typing bug is found: https://github.com/python/typing/issues/256
def reset_tzpath(to: Sequence[StrPath] | None = ...) -> None: ...
def available_timezones() -> set[str]: ...

TZPATH: Sequence[str]

class ZoneInfoNotFoundError(KeyError): ...
class InvalidTZPathWarning(RuntimeWarning): ...
