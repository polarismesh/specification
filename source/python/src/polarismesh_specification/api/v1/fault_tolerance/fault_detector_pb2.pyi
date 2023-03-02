from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaultDetectRule(_message.Message):
    __slots__ = ["ctime", "description", "http_config", "id", "interval", "mtime", "name", "namespace", "port", "protocol", "revision", "target_service", "tcp_config", "timeout", "udp_config"]
    class Protocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DestinationService(_message.Message):
        __slots__ = ["method", "namespace", "service"]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        method: _model_pb2.MatchString
        namespace: str
        service: str
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HTTP: FaultDetectRule.Protocol
    HTTP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    TARGET_SERVICE_FIELD_NUMBER: _ClassVar[int]
    TCP: FaultDetectRule.Protocol
    TCP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UDP: FaultDetectRule.Protocol
    UDP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: FaultDetectRule.Protocol
    ctime: str
    description: str
    http_config: HttpProtocolConfig
    id: str
    interval: int
    mtime: str
    name: str
    namespace: str
    port: int
    protocol: FaultDetectRule.Protocol
    revision: str
    target_service: FaultDetectRule.DestinationService
    tcp_config: TcpProtocolConfig
    timeout: int
    udp_config: UdpProtocolConfig
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., description: _Optional[str] = ..., target_service: _Optional[_Union[FaultDetectRule.DestinationService, _Mapping]] = ..., interval: _Optional[int] = ..., timeout: _Optional[int] = ..., port: _Optional[int] = ..., protocol: _Optional[_Union[FaultDetectRule.Protocol, str]] = ..., http_config: _Optional[_Union[HttpProtocolConfig, _Mapping]] = ..., tcp_config: _Optional[_Union[TcpProtocolConfig, _Mapping]] = ..., udp_config: _Optional[_Union[UdpProtocolConfig, _Mapping]] = ...) -> None: ...

class FaultDetector(_message.Message):
    __slots__ = ["revision", "rules"]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    revision: str
    rules: _containers.RepeatedCompositeFieldContainer[FaultDetectRule]
    def __init__(self, rules: _Optional[_Iterable[_Union[FaultDetectRule, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...

class HttpProtocolConfig(_message.Message):
    __slots__ = ["body", "headers", "method", "url"]
    class MessageHeader(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    body: str
    headers: _containers.RepeatedCompositeFieldContainer[HttpProtocolConfig.MessageHeader]
    method: str
    url: str
    def __init__(self, method: _Optional[str] = ..., url: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[HttpProtocolConfig.MessageHeader, _Mapping]]] = ..., body: _Optional[str] = ...) -> None: ...

class TcpProtocolConfig(_message.Message):
    __slots__ = ["receive", "send"]
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    receive: _containers.RepeatedScalarFieldContainer[str]
    send: str
    def __init__(self, send: _Optional[str] = ..., receive: _Optional[_Iterable[str]] = ...) -> None: ...

class UdpProtocolConfig(_message.Message):
    __slots__ = ["receive", "send"]
    RECEIVE_FIELD_NUMBER: _ClassVar[int]
    SEND_FIELD_NUMBER: _ClassVar[int]
    receive: _containers.RepeatedScalarFieldContainer[str]
    send: str
    def __init__(self, send: _Optional[str] = ..., receive: _Optional[_Iterable[str]] = ...) -> None: ...
