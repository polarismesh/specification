from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ["ctime", "host", "id", "location", "mtime", "stat", "type", "version"]
    class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AGENT: Client.ClientType
    CTIME_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    SDK: Client.ClientType
    STAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Client.ClientType
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ctime: _wrappers_pb2.StringValue
    host: _wrappers_pb2.StringValue
    id: _wrappers_pb2.StringValue
    location: _model_pb2.Location
    mtime: _wrappers_pb2.StringValue
    stat: _containers.RepeatedCompositeFieldContainer[StatInfo]
    type: Client.ClientType
    version: _wrappers_pb2.StringValue
    def __init__(self, host: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[Client.ClientType, str]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., location: _Optional[_Union[_model_pb2.Location, _Mapping]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stat: _Optional[_Iterable[_Union[StatInfo, _Mapping]]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class StatInfo(_message.Message):
    __slots__ = ["path", "port", "protocol", "target"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    path: _wrappers_pb2.StringValue
    port: _wrappers_pb2.UInt32Value
    protocol: _wrappers_pb2.StringValue
    target: _wrappers_pb2.StringValue
    def __init__(self, target: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., path: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., protocol: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
