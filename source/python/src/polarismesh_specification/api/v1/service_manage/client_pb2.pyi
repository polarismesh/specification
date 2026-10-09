from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ("host", "type", "version", "location", "id", "stat", "ctime", "mtime", "config_enabled", "config_metadata", "server_host")
    class ClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Client.ClientType]
        SDK: _ClassVar[Client.ClientType]
        AGENT: _ClassVar[Client.ClientType]
    UNKNOWN: Client.ClientType
    SDK: Client.ClientType
    AGENT: Client.ClientType
    HOST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STAT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONFIG_METADATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_HOST_FIELD_NUMBER: _ClassVar[int]
    host: _wrappers_pb2.StringValue
    type: Client.ClientType
    version: _wrappers_pb2.StringValue
    location: _model_pb2.Location
    id: _wrappers_pb2.StringValue
    stat: _containers.RepeatedCompositeFieldContainer[StatInfo]
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    config_enabled: _wrappers_pb2.BoolValue
    config_metadata: _wrappers_pb2.StringValue
    server_host: _wrappers_pb2.StringValue
    def __init__(self, host: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[Client.ClientType, str]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., location: _Optional[_Union[_model_pb2.Location, _Mapping]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., stat: _Optional[_Iterable[_Union[StatInfo, _Mapping]]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., config_enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., config_metadata: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., server_host: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class StatInfo(_message.Message):
    __slots__ = ("target", "port", "path", "protocol")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    target: _wrappers_pb2.StringValue
    port: _wrappers_pb2.UInt32Value
    path: _wrappers_pb2.StringValue
    protocol: _wrappers_pb2.StringValue
    def __init__(self, target: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., path: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., protocol: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ClientEvent(_message.Message):
    __slots__ = ("type", "client_id", "index", "content")
    class ClientEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ClientEvent.ClientEventType]
        WATCH: _ClassVar[ClientEvent.ClientEventType]
        PUSH: _ClassVar[ClientEvent.ClientEventType]
        ACK: _ClassVar[ClientEvent.ClientEventType]
    UNKNOWN: ClientEvent.ClientEventType
    WATCH: ClientEvent.ClientEventType
    PUSH: ClientEvent.ClientEventType
    ACK: ClientEvent.ClientEventType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: ClientEvent.ClientEventType
    client_id: str
    index: int
    content: str
    def __init__(self, type: _Optional[_Union[ClientEvent.ClientEventType, str]] = ..., client_id: _Optional[str] = ..., index: _Optional[int] = ..., content: _Optional[str] = ...) -> None: ...
