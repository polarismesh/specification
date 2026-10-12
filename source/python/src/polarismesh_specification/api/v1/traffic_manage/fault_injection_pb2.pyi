from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import any_pb2 as _any_pb2
from ..model import model_pb2 as _model_pb2
from ..traffic_manage import routing_pb2 as _routing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FaultInjection(_message.Message):
    __slots__ = ("service", "namespace", "revision", "enabled", "sources", "delayFault", "abortFault", "ctime", "mtime", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    DELAYFAULT_FIELD_NUMBER: _ClassVar[int]
    ABORTFAULT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    enabled: _wrappers_pb2.BoolValue
    sources: _containers.RepeatedCompositeFieldContainer[_routing_pb2.Source]
    delayFault: DelayFault
    abortFault: AbortFault
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., sources: _Optional[_Iterable[_Union[_routing_pb2.Source, _Mapping]]] = ..., delayFault: _Optional[_Union[DelayFault, _Mapping]] = ..., abortFault: _Optional[_Union[AbortFault, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DelayFault(_message.Message):
    __slots__ = ("delayPercent", "delay")
    DELAYPERCENT_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    delayPercent: int
    delay: int
    def __init__(self, delayPercent: _Optional[int] = ..., delay: _Optional[int] = ...) -> None: ...

class AbortFault(_message.Message):
    __slots__ = ("abortPercent", "abortCode")
    ABORTPERCENT_FIELD_NUMBER: _ClassVar[int]
    ABORTCODE_FIELD_NUMBER: _ClassVar[int]
    abortPercent: int
    abortCode: int
    def __init__(self, abortPercent: _Optional[int] = ..., abortCode: _Optional[int] = ...) -> None: ...
