from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..service_manage import service_pb2 as _service_pb2
from ..fault_tolerance import circuitbreaker_pb2 as _circuitbreaker_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigRelease(_message.Message):
    __slots__ = ("service", "ctime", "mtime", "circuitBreaker")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    service: _service_pb2.Service
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    def __init__(self, service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ...) -> None: ...

class ConfigWithService(_message.Message):
    __slots__ = ("services", "circuitBreaker")
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    def __init__(self, services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ...) -> None: ...
