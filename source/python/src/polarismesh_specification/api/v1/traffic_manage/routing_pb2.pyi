from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import any_pb2 as _any_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
MetadataPolicy: RoutingPolicy
RulePolicy: RoutingPolicy

class Destination(_message.Message):
    __slots__ = ["isolate", "metadata", "name", "namespace", "priority", "service", "transfer", "weight"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    isolate: _wrappers_pb2.BoolValue
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    priority: _wrappers_pb2.UInt32Value
    service: _wrappers_pb2.StringValue
    transfer: _wrappers_pb2.StringValue
    weight: _wrappers_pb2.UInt32Value
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., weight: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., transfer: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., isolate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class DestinationGroup(_message.Message):
    __slots__ = ["isolate", "labels", "name", "namespace", "priority", "service", "transfer", "weight"]
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    isolate: bool
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    name: str
    namespace: str
    priority: int
    service: str
    transfer: str
    weight: int
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[int] = ..., weight: _Optional[int] = ..., transfer: _Optional[str] = ..., isolate: bool = ..., name: _Optional[str] = ...) -> None: ...

class MetadataFailover(_message.Message):
    __slots__ = ["failover_range", "labels"]
    class FailoverRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ALL: MetadataFailover.FailoverRange
    FAILOVER_RANGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    OTHERS: MetadataFailover.FailoverRange
    OTHER_KEYS: MetadataFailover.FailoverRange
    failover_range: MetadataFailover.FailoverRange
    labels: _containers.ScalarMap[str, str]
    def __init__(self, failover_range: _Optional[_Union[MetadataFailover.FailoverRange, str]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MetadataRoutingConfig(_message.Message):
    __slots__ = ["failover", "labels", "namespace", "service"]
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FAILOVER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    failover: MetadataFailover
    labels: _containers.ScalarMap[str, str]
    namespace: str
    service: str
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., failover: _Optional[_Union[MetadataFailover, _Mapping]] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ["destinations", "extendInfo", "sources"]
    class ExtendInfoEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[Destination]
    extendInfo: _containers.ScalarMap[str, str]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    def __init__(self, sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[Destination, _Mapping]]] = ..., extendInfo: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RouteRule(_message.Message):
    __slots__ = ["ctime", "description", "enable", "etime", "extendInfo", "id", "mtime", "name", "namespace", "priority", "revision", "routing_config", "routing_policy"]
    class ExtendInfoEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ctime: str
    description: str
    enable: bool
    etime: str
    extendInfo: _containers.ScalarMap[str, str]
    id: str
    mtime: str
    name: str
    namespace: str
    priority: int
    revision: str
    routing_config: _any_pb2.Any
    routing_policy: RoutingPolicy
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., enable: bool = ..., routing_policy: _Optional[_Union[RoutingPolicy, str]] = ..., routing_config: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., priority: _Optional[int] = ..., description: _Optional[str] = ..., extendInfo: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Routing(_message.Message):
    __slots__ = ["ctime", "inbounds", "mtime", "namespace", "outbounds", "revision", "rules", "service", "service_token"]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    INBOUNDS_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ctime: _wrappers_pb2.StringValue
    inbounds: _containers.RepeatedCompositeFieldContainer[Route]
    mtime: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    outbounds: _containers.RepeatedCompositeFieldContainer[Route]
    revision: _wrappers_pb2.StringValue
    rules: _containers.RepeatedCompositeFieldContainer[RouteRule]
    service: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., inbounds: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., outbounds: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rules: _Optional[_Iterable[_Union[RouteRule, _Mapping]]] = ...) -> None: ...

class RuleRoutingConfig(_message.Message):
    __slots__ = ["destinations", "rules", "sources"]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationGroup]
    rules: _containers.RepeatedCompositeFieldContainer[SubRuleRouting]
    sources: _containers.RepeatedCompositeFieldContainer[SourceService]
    def __init__(self, sources: _Optional[_Iterable[_Union[SourceService, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationGroup, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[SubRuleRouting, _Mapping]]] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ["metadata", "namespace", "service"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    namespace: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class SourceMatch(_message.Message):
    __slots__ = ["key", "type", "value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CALLER_IP: SourceMatch.Type
    COOKIE: SourceMatch.Type
    CUSTOM: SourceMatch.Type
    HEADER: SourceMatch.Type
    KEY_FIELD_NUMBER: _ClassVar[int]
    METHOD: SourceMatch.Type
    PATH: SourceMatch.Type
    QUERY: SourceMatch.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    type: SourceMatch.Type
    value: _model_pb2.MatchString
    def __init__(self, type: _Optional[_Union[SourceMatch.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...

class SourceService(_message.Message):
    __slots__ = ["arguments", "namespace", "service"]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedCompositeFieldContainer[SourceMatch]
    namespace: str
    service: str
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., arguments: _Optional[_Iterable[_Union[SourceMatch, _Mapping]]] = ...) -> None: ...

class SubRuleRouting(_message.Message):
    __slots__ = ["destinations", "name", "sources"]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationGroup]
    name: str
    sources: _containers.RepeatedCompositeFieldContainer[SourceService]
    def __init__(self, name: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[SourceService, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationGroup, _Mapping]]] = ...) -> None: ...

class RoutingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
