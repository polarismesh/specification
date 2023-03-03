from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ["campus", "region", "zone"]
    CAMPUS_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    campus: _wrappers_pb2.StringValue
    region: _wrappers_pb2.StringValue
    zone: _wrappers_pb2.StringValue
    def __init__(self, region: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., zone: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., campus: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class MatchString(_message.Message):
    __slots__ = ["type", "value", "value_type"]
    class MatchStringType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EXACT: MatchString.MatchStringType
    IN: MatchString.MatchStringType
    NOT_EQUALS: MatchString.MatchStringType
    NOT_IN: MatchString.MatchStringType
    PARAMETER: MatchString.ValueType
    RANGE: MatchString.MatchStringType
    REGEX: MatchString.MatchStringType
    TEXT: MatchString.ValueType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIABLE: MatchString.ValueType
    type: MatchString.MatchStringType
    value: _wrappers_pb2.StringValue
    value_type: MatchString.ValueType
    def __init__(self, type: _Optional[_Union[MatchString.MatchStringType, str]] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., value_type: _Optional[_Union[MatchString.ValueType, str]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
