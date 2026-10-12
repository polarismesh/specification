from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ("region", "zone", "campus")
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    region: _wrappers_pb2.StringValue
    zone: _wrappers_pb2.StringValue
    campus: _wrappers_pb2.StringValue
    def __init__(self, region: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., zone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., campus: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class MatchString(_message.Message):
    __slots__ = ("type", "value", "value_type")
    class MatchStringType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXACT: _ClassVar[MatchString.MatchStringType]
        REGEX: _ClassVar[MatchString.MatchStringType]
        NOT_EQUALS: _ClassVar[MatchString.MatchStringType]
        IN: _ClassVar[MatchString.MatchStringType]
        NOT_IN: _ClassVar[MatchString.MatchStringType]
        RANGE: _ClassVar[MatchString.MatchStringType]
    EXACT: MatchString.MatchStringType
    REGEX: MatchString.MatchStringType
    NOT_EQUALS: MatchString.MatchStringType
    IN: MatchString.MatchStringType
    NOT_IN: MatchString.MatchStringType
    RANGE: MatchString.MatchStringType
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEXT: _ClassVar[MatchString.ValueType]
        PARAMETER: _ClassVar[MatchString.ValueType]
        VARIABLE: _ClassVar[MatchString.ValueType]
    TEXT: MatchString.ValueType
    PARAMETER: MatchString.ValueType
    VARIABLE: MatchString.ValueType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: MatchString.MatchStringType
    value: _wrappers_pb2.StringValue
    value_type: MatchString.ValueType
    def __init__(self, type: _Optional[_Union[MatchString.MatchStringType, str]] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., value_type: _Optional[_Union[MatchString.ValueType, str]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Summary(_message.Message):
    __slots__ = ("total_service_count", "total_health_instance_count", "total_instance_count")
    TOTAL_SERVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HEALTH_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_service_count: int
    total_health_instance_count: int
    total_instance_count: int
    def __init__(self, total_service_count: _Optional[int] = ..., total_health_instance_count: _Optional[int] = ..., total_instance_count: _Optional[int] = ...) -> None: ...

class ClientLabel(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: MatchString
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MatchString, _Mapping]] = ...) -> None: ...

class API(_message.Message):
    __slots__ = ("protocol", "method", "path")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    method: str
    path: MatchString
    def __init__(self, protocol: _Optional[str] = ..., method: _Optional[str] = ..., path: _Optional[_Union[MatchString, _Mapping]] = ...) -> None: ...
