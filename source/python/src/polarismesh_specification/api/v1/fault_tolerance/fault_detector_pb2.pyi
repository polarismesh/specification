from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaultDetector(_message.Message):
    __slots__ = ("rules", "revision")
    RULES_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[FaultDetectRule]
    revision: str
    def __init__(self, rules: _Optional[_Iterable[_Union[FaultDetectRule, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...

class FaultDetectRule(_message.Message):
    __slots__ = ("id", "name", "namespace", "revision", "ctime", "mtime", "description", "target_service", "interval", "timeout", "port", "protocol", "http_config", "tcp_config", "udp_config", "priority", "metadata", "extendInfo")
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[FaultDetectRule.Protocol]
        HTTP: _ClassVar[FaultDetectRule.Protocol]
        TCP: _ClassVar[FaultDetectRule.Protocol]
        UDP: _ClassVar[FaultDetectRule.Protocol]
    UNKNOWN: FaultDetectRule.Protocol
    HTTP: FaultDetectRule.Protocol
    TCP: FaultDetectRule.Protocol
    UDP: FaultDetectRule.Protocol
    class DestinationService(_message.Message):
        __slots__ = ("service", "namespace", "method", "api")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        service: str
        namespace: str
        method: _model_pb2.MatchString
        api: _model_pb2.API
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ..., api: _Optional[_Union[_model_pb2.API, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ExtendInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SERVICE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    HTTP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TCP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UDP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    namespace: str
    revision: str
    ctime: str
    mtime: str
    description: str
    target_service: FaultDetectRule.DestinationService
    interval: int
    timeout: int
    port: int
    protocol: FaultDetectRule.Protocol
    http_config: HttpProtocolConfig
    tcp_config: TcpProtocolConfig
    udp_config: UdpProtocolConfig
    priority: int
    metadata: _containers.ScalarMap[str, str]
    extendInfo: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., description: _Optional[str] = ..., target_service: _Optional[_Union[FaultDetectRule.DestinationService, _Mapping]] = ..., interval: _Optional[int] = ..., timeout: _Optional[int] = ..., port: _Optional[int] = ..., protocol: _Optional[_Union[FaultDetectRule.Protocol, str]] = ..., http_config: _Optional[_Union[HttpProtocolConfig, _Mapping]] = ..., tcp_config: _Optional[_Union[TcpProtocolConfig, _Mapping]] = ..., udp_config: _Optional[_Union[UdpProtocolConfig, _Mapping]] = ..., priority: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., extendInfo: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HttpProtocolConfig(_message.Message):
    __slots__ = ("method", "url", "headers", "body")
    class MessageHeader(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    method: str
    url: str
    headers: _containers.RepeatedCompositeFieldContainer[HttpProtocolConfig.MessageHeader]
    body: str
    def __init__(self, method: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[HttpProtocolConfig.MessageHeader, _Mapping]]] = ..., body: _Optional[str] = ...) -> None: ...

class TcpProtocolConfig(_message.Message):
    __slots__ = ("send", "receive")
    SEND_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    send: str
    receive: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, send: _Optional[str] = ..., receive: _Optional[_Iterable[str]] = ...) -> None: ...

class UdpProtocolConfig(_message.Message):
    __slots__ = ("send", "receive")
    SEND_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    send: str
    receive: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, send: _Optional[str] = ..., receive: _Optional[_Iterable[str]] = ...) -> None: ...
