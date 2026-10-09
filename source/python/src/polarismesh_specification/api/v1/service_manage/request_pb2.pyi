from ..service_manage import service_pb2 as _service_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoverDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Callee: _ClassVar[DiscoverDirection]
    Caller: _ClassVar[DiscoverDirection]
Callee: DiscoverDirection
Caller: DiscoverDirection

class DiscoverFilter(_message.Message):
    __slots__ = ("OnlyHealthyInstance",)
    ONLYHEALTHYINSTANCE_FIELD_NUMBER: _ClassVar[int]
    OnlyHealthyInstance: bool
    def __init__(self, OnlyHealthyInstance: _Optional[bool] = ...) -> None: ...

class DiscoverRequest(_message.Message):
    __slots__ = ("type", "service", "Filter", "Direction")
    class DiscoverRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DiscoverRequest.DiscoverRequestType]
        INSTANCE: _ClassVar[DiscoverRequest.DiscoverRequestType]
        CLUSTER: _ClassVar[DiscoverRequest.DiscoverRequestType]
        ROUTING: _ClassVar[DiscoverRequest.DiscoverRequestType]
        RATE_LIMIT: _ClassVar[DiscoverRequest.DiscoverRequestType]
        CIRCUIT_BREAKER: _ClassVar[DiscoverRequest.DiscoverRequestType]
        SERVICES: _ClassVar[DiscoverRequest.DiscoverRequestType]
        NAMESPACES: _ClassVar[DiscoverRequest.DiscoverRequestType]
        FAULT_DETECTOR: _ClassVar[DiscoverRequest.DiscoverRequestType]
        LANE: _ClassVar[DiscoverRequest.DiscoverRequestType]
        CUSTOM_ROUTE_RULE: _ClassVar[DiscoverRequest.DiscoverRequestType]
        NEARBY_ROUTE_RULE: _ClassVar[DiscoverRequest.DiscoverRequestType]
        LOSSLESS: _ClassVar[DiscoverRequest.DiscoverRequestType]
        BLOCK_ALLOW_RULE: _ClassVar[DiscoverRequest.DiscoverRequestType]
        TRAFFIC_MIRRORING: _ClassVar[DiscoverRequest.DiscoverRequestType]
        FAULT_INJECTION: _ClassVar[DiscoverRequest.DiscoverRequestType]
    UNKNOWN: DiscoverRequest.DiscoverRequestType
    INSTANCE: DiscoverRequest.DiscoverRequestType
    CLUSTER: DiscoverRequest.DiscoverRequestType
    ROUTING: DiscoverRequest.DiscoverRequestType
    RATE_LIMIT: DiscoverRequest.DiscoverRequestType
    CIRCUIT_BREAKER: DiscoverRequest.DiscoverRequestType
    SERVICES: DiscoverRequest.DiscoverRequestType
    NAMESPACES: DiscoverRequest.DiscoverRequestType
    FAULT_DETECTOR: DiscoverRequest.DiscoverRequestType
    LANE: DiscoverRequest.DiscoverRequestType
    CUSTOM_ROUTE_RULE: DiscoverRequest.DiscoverRequestType
    NEARBY_ROUTE_RULE: DiscoverRequest.DiscoverRequestType
    LOSSLESS: DiscoverRequest.DiscoverRequestType
    BLOCK_ALLOW_RULE: DiscoverRequest.DiscoverRequestType
    TRAFFIC_MIRRORING: DiscoverRequest.DiscoverRequestType
    FAULT_INJECTION: DiscoverRequest.DiscoverRequestType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    type: DiscoverRequest.DiscoverRequestType
    service: _service_pb2.Service
    Filter: DiscoverFilter
    Direction: DiscoverDirection
    def __init__(self, type: _Optional[_Union[DiscoverRequest.DiscoverRequestType, str]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., Filter: _Optional[_Union[DiscoverFilter, _Mapping]] = ..., Direction: _Optional[_Union[DiscoverDirection, str]] = ...) -> None: ...
