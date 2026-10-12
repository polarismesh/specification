from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IstioCertificateRequest(_message.Message):
    __slots__ = ("csr", "subject_id", "validity_duration")
    CSR_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_DURATION_FIELD_NUMBER: _ClassVar[int]
    csr: str
    subject_id: str
    validity_duration: int
    def __init__(self, csr: _Optional[str] = ..., subject_id: _Optional[str] = ..., validity_duration: _Optional[int] = ...) -> None: ...

class IstioCertificateResponse(_message.Message):
    __slots__ = ("cert_chain",)
    CERT_CHAIN_FIELD_NUMBER: _ClassVar[int]
    cert_chain: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cert_chain: _Optional[_Iterable[str]] = ...) -> None: ...
