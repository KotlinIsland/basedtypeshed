from _typeshed import Self
from typing import IO, Pattern

from paramiko.message import Message

OPENSSH_AUTH_MAGIC: bytes = ...

def _unpad_openssh(data: bytes) -> bytes: ...

class PKey:
    public_blob: PublicBlob | None
    BEGIN_TAG: Pattern[str]
    END_TAG: Pattern[str]
    def __init__(self, msg: Message | None = ..., data: str | None = ...) -> None: ...
    def asbytes(self) -> bytes: ...
    def __cmp__(self, other: object) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def get_name(self) -> str: ...
    def get_bits(self) -> int: ...
    def can_sign(self) -> bool: ...
    def get_fingerprint(self) -> bytes: ...
    def get_base64(self) -> str: ...
    def sign_ssh_data(self, data: bytes) -> Message: ...
    def verify_ssh_sig(self, data: bytes, msg: Message) -> bool: ...
    @classmethod
    def from_private_key_file(cls: type[Self], filename: str, password: str | None = ...) -> Self: ...
    @classmethod
    def from_private_key(cls: type[Self], file_obj: IO[str], password: str | None = ...) -> Self: ...
    def write_private_key_file(self, filename: str, password: str | None = ...) -> None: ...
    def write_private_key(self, file_obj: IO[str], password: str | None = ...) -> None: ...
    def load_certificate(self, value: Message | str) -> None: ...

class PublicBlob:
    key_type: str
    key_blob: str
    comment: str
    def __init__(self, type_: str, blob: bytes, comment: str | None = ...) -> None: ...
    @classmethod
    def from_file(cls, filename: str) -> PublicBlob: ...
    @classmethod
    def from_string(cls, string: str) -> PublicBlob: ...
    @classmethod
    def from_message(cls, message: Message) -> PublicBlob: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
