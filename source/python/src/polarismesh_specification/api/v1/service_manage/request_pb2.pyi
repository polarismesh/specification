from ..service_manage import service_pb2 as _service_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoverRequest(_message.Message):
    __slots__ = ["service", "type"]
    class DiscoverRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CIRCUIT_BREAKER: DiscoverRequest.DiscoverRequestType
    CLUSTER: DiscoverRequest.DiscoverRequestType
    FAULT_DETECTOR: DiscoverRequest.DiscoverRequestType
    INSTANCE: DiscoverRequest.DiscoverRequestType
    NAMESPACES: DiscoverRequest.DiscoverRequestType
    RATE_LIMIT: DiscoverRequest.DiscoverRequestType
    ROUTING: DiscoverRequest.DiscoverRequestType
    SERVICES: DiscoverRequest.DiscoverRequestType
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: DiscoverRequest.DiscoverRequestType
    service: _service_pb2.Service
    type: DiscoverRequest.DiscoverRequestType
    def __init__(self, type: _Optional[_Union[DiscoverRequest.DiscoverRequestType, str]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ...) -> None: ...
