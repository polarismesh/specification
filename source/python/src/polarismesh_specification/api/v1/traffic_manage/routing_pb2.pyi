from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import any_pb2 as _any_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RulePolicy: _ClassVar[RoutingPolicy]
    MetadataPolicy: _ClassVar[RoutingPolicy]
    NearbyPolicy: _ClassVar[RoutingPolicy]
RulePolicy: RoutingPolicy
MetadataPolicy: RoutingPolicy
NearbyPolicy: RoutingPolicy

class Routing(_message.Message):
    __slots__ = ("service", "namespace", "inbounds", "outbounds", "ctime", "mtime", "revision", "service_token", "rules")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    INBOUNDS_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    inbounds: _containers.RepeatedCompositeFieldContainer[Route]
    outbounds: _containers.RepeatedCompositeFieldContainer[Route]
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    rules: _containers.RepeatedCompositeFieldContainer[RouteRule]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., inbounds: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., outbounds: _Optional[_Iterable[_Union[Route, _Mapping]]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rules: _Optional[_Iterable[_Union[RouteRule, _Mapping]]] = ...) -> None: ...

class Route(_message.Message):
    __slots__ = ("sources", "destinations", "extendInfo", "metadata")
    class ExtendInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[Source]
    destinations: _containers.RepeatedCompositeFieldContainer[Destination]
    extendInfo: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, sources: _Optional[_Iterable[_Union[Source, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[Destination, _Mapping]]] = ..., extendInfo: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ("service", "namespace", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class Destination(_message.Message):
    __slots__ = ("service", "namespace", "metadata", "priority", "weight", "transfer", "isolate", "name")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    priority: _wrappers_pb2.UInt32Value
    weight: _wrappers_pb2.UInt32Value
    transfer: _wrappers_pb2.StringValue
    isolate: _wrappers_pb2.BoolValue
    name: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., weight: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., transfer: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., isolate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RouteRule(_message.Message):
    __slots__ = ("id", "name", "namespace", "enable", "routing_policy", "routing_config", "revision", "ctime", "mtime", "etime", "priority", "description", "extendInfo", "metadata")
    class ExtendInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    ROUTING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTENDINFO_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    namespace: str
    enable: bool
    routing_policy: RoutingPolicy
    routing_config: _any_pb2.Any
    revision: str
    ctime: str
    mtime: str
    etime: str
    priority: int
    description: str
    extendInfo: _containers.ScalarMap[str, str]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., enable: _Optional[bool] = ..., routing_policy: _Optional[_Union[RoutingPolicy, str]] = ..., routing_config: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., priority: _Optional[int] = ..., description: _Optional[str] = ..., extendInfo: _Optional[_Mapping[str, str]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MetadataFailover(_message.Message):
    __slots__ = ("failover_range", "labels")
    class FailoverRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[MetadataFailover.FailoverRange]
        OTHERS: _ClassVar[MetadataFailover.FailoverRange]
        OTHER_KEYS: _ClassVar[MetadataFailover.FailoverRange]
    ALL: MetadataFailover.FailoverRange
    OTHERS: MetadataFailover.FailoverRange
    OTHER_KEYS: MetadataFailover.FailoverRange
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FAILOVER_RANGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    failover_range: MetadataFailover.FailoverRange
    labels: _containers.ScalarMap[str, str]
    def __init__(self, failover_range: _Optional[_Union[MetadataFailover.FailoverRange, str]] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MetadataRoutingConfig(_message.Message):
    __slots__ = ("service", "namespace", "labels", "failover")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_FIELD_NUMBER: _ClassVar[int]
    service: str
    namespace: str
    labels: _containers.ScalarMap[str, str]
    failover: MetadataFailover
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ..., failover: _Optional[_Union[MetadataFailover, _Mapping]] = ...) -> None: ...

class NearbyRoutingConfig(_message.Message):
    __slots__ = ("service", "namespace", "match_level", "max_match_level", "strict_nearby")
    class LocationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[NearbyRoutingConfig.LocationLevel]
        CAMPUS: _ClassVar[NearbyRoutingConfig.LocationLevel]
        ZONE: _ClassVar[NearbyRoutingConfig.LocationLevel]
        REGION: _ClassVar[NearbyRoutingConfig.LocationLevel]
        ALL: _ClassVar[NearbyRoutingConfig.LocationLevel]
    UNKNOWN: NearbyRoutingConfig.LocationLevel
    CAMPUS: NearbyRoutingConfig.LocationLevel
    ZONE: NearbyRoutingConfig.LocationLevel
    REGION: NearbyRoutingConfig.LocationLevel
    ALL: NearbyRoutingConfig.LocationLevel
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    MATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_MATCH_LEVEL_FIELD_NUMBER: _ClassVar[int]
    STRICT_NEARBY_FIELD_NUMBER: _ClassVar[int]
    service: str
    namespace: str
    match_level: NearbyRoutingConfig.LocationLevel
    max_match_level: NearbyRoutingConfig.LocationLevel
    strict_nearby: bool
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., match_level: _Optional[_Union[NearbyRoutingConfig.LocationLevel, str]] = ..., max_match_level: _Optional[_Union[NearbyRoutingConfig.LocationLevel, str]] = ..., strict_nearby: _Optional[bool] = ...) -> None: ...

class RuleRoutingConfig(_message.Message):
    __slots__ = ("sources", "destinations", "rules")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[SourceService]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationGroup]
    rules: _containers.RepeatedCompositeFieldContainer[SubRuleRouting]
    def __init__(self, sources: _Optional[_Iterable[_Union[SourceService, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationGroup, _Mapping]]] = ..., rules: _Optional[_Iterable[_Union[SubRuleRouting, _Mapping]]] = ...) -> None: ...

class SubRuleRouting(_message.Message):
    __slots__ = ("name", "sources", "destinations")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    sources: _containers.RepeatedCompositeFieldContainer[SourceService]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationGroup]
    def __init__(self, name: _Optional[str] = ..., sources: _Optional[_Iterable[_Union[SourceService, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationGroup, _Mapping]]] = ...) -> None: ...

class SourceService(_message.Message):
    __slots__ = ("service", "namespace", "arguments")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    service: str
    namespace: str
    arguments: _containers.RepeatedCompositeFieldContainer[SourceMatch]
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., arguments: _Optional[_Iterable[_Union[SourceMatch, _Mapping]]] = ...) -> None: ...

class DestinationGroup(_message.Message):
    __slots__ = ("service", "namespace", "labels", "priority", "weight", "transfer", "isolate", "name")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_FIELD_NUMBER: _ClassVar[int]
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    service: str
    namespace: str
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    priority: int
    weight: int
    transfer: str
    isolate: bool
    name: str
    def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[int] = ..., weight: _Optional[int] = ..., transfer: _Optional[str] = ..., isolate: _Optional[bool] = ..., name: _Optional[str] = ...) -> None: ...

class SourceMatch(_message.Message):
    __slots__ = ("type", "key", "value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM: _ClassVar[SourceMatch.Type]
        METHOD: _ClassVar[SourceMatch.Type]
        HEADER: _ClassVar[SourceMatch.Type]
        QUERY: _ClassVar[SourceMatch.Type]
        CALLER_IP: _ClassVar[SourceMatch.Type]
        PATH: _ClassVar[SourceMatch.Type]
        COOKIE: _ClassVar[SourceMatch.Type]
        CALLER_METADATA: _ClassVar[SourceMatch.Type]
    CUSTOM: SourceMatch.Type
    METHOD: SourceMatch.Type
    HEADER: SourceMatch.Type
    QUERY: SourceMatch.Type
    CALLER_IP: SourceMatch.Type
    PATH: SourceMatch.Type
    COOKIE: SourceMatch.Type
    CALLER_METADATA: SourceMatch.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: SourceMatch.Type
    key: str
    value: _model_pb2.MatchString
    def __init__(self, type: _Optional[_Union[SourceMatch.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
