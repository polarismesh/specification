from google.protobuf import any_pb2 as _any_pb2
from ..model import model_pb2 as _model_pb2
from ..traffic_manage import routing_pb2 as _routing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrafficEntry(_message.Message):
    __slots__ = ("type", "selector")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    type: str
    selector: _any_pb2.Any
    def __init__(self, type: _Optional[str] = ..., selector: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class TSEGatewaySelector(_message.Message):
    __slots__ = ("instance_id", "services")
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    instance_id: str
    services: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, instance_id: _Optional[str] = ..., services: _Optional[_Iterable[str]] = ...) -> None: ...

class ServiceGatewaySelector(_message.Message):
    __slots__ = ("namespace", "service", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    service: str
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    def __init__(self, namespace: _Optional[str] = ..., service: _Optional[str] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class ServiceSelector(_message.Message):
    __slots__ = ("namespace", "service", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    service: str
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    def __init__(self, namespace: _Optional[str] = ..., service: _Optional[str] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class LaneGroup(_message.Message):
    __slots__ = ("id", "name", "entries", "destinations", "revision", "description", "ctime", "mtime", "rules", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    entries: _containers.RepeatedCompositeFieldContainer[TrafficEntry]
    destinations: _containers.RepeatedCompositeFieldContainer[_routing_pb2.DestinationGroup]
    revision: str
    description: str
    ctime: str
    mtime: str
    rules: _containers.RepeatedCompositeFieldContainer[LaneRule]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[TrafficEntry, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[_routing_pb2.DestinationGroup, _Mapping]]] = ..., revision: _Optional[str] = ..., description: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., rules: _Optional[_Iterable[_Union[LaneRule, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TrafficMatchRule(_message.Message):
    __slots__ = ("arguments", "matchMode")
    class TrafficMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AND: _ClassVar[TrafficMatchRule.TrafficMatchMode]
        OR: _ClassVar[TrafficMatchRule.TrafficMatchMode]
    AND: TrafficMatchRule.TrafficMatchMode
    OR: TrafficMatchRule.TrafficMatchMode
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    MATCHMODE_FIELD_NUMBER: _ClassVar[int]
    arguments: _containers.RepeatedCompositeFieldContainer[_routing_pb2.SourceMatch]
    matchMode: TrafficMatchRule.TrafficMatchMode
    def __init__(self, arguments: _Optional[_Iterable[_Union[_routing_pb2.SourceMatch, _Mapping]]] = ..., matchMode: _Optional[_Union[TrafficMatchRule.TrafficMatchMode, str]] = ...) -> None: ...

class TrafficGray(_message.Message):
    __slots__ = ("mode", "percentage", "warmup")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERCENTAGE: _ClassVar[TrafficGray.Mode]
        WARMUP: _ClassVar[TrafficGray.Mode]
    PERCENTAGE: TrafficGray.Mode
    WARMUP: TrafficGray.Mode
    class Percentage(_message.Message):
        __slots__ = ("percent",)
        PERCENT_FIELD_NUMBER: _ClassVar[int]
        percent: int
        def __init__(self, percent: _Optional[int] = ...) -> None: ...
    class Warmup(_message.Message):
        __slots__ = ("intervalSecond", "curvature")
        INTERVALSECOND_FIELD_NUMBER: _ClassVar[int]
        CURVATURE_FIELD_NUMBER: _ClassVar[int]
        intervalSecond: int
        curvature: int
        def __init__(self, intervalSecond: _Optional[int] = ..., curvature: _Optional[int] = ...) -> None: ...
    MODE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    WARMUP_FIELD_NUMBER: _ClassVar[int]
    mode: TrafficGray.Mode
    percentage: TrafficGray.Percentage
    warmup: TrafficGray.Warmup
    def __init__(self, mode: _Optional[_Union[TrafficGray.Mode, str]] = ..., percentage: _Optional[_Union[TrafficGray.Percentage, _Mapping]] = ..., warmup: _Optional[_Union[TrafficGray.Warmup, _Mapping]] = ...) -> None: ...

class LaneRule(_message.Message):
    __slots__ = ("id", "name", "group_name", "traffic_match_rule", "default_label_value", "enable", "match_mode", "traffic_gray", "revision", "ctime", "mtime", "etime", "priority", "description", "label_key")
    class LaneMatchMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRICT: _ClassVar[LaneRule.LaneMatchMode]
        PERMISSIVE: _ClassVar[LaneRule.LaneMatchMode]
    STRICT: LaneRule.LaneMatchMode
    PERMISSIVE: LaneRule.LaneMatchMode
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_MATCH_RULE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LABEL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    MATCH_MODE_FIELD_NUMBER: _ClassVar[int]
    TRAFFIC_GRAY_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    group_name: str
    traffic_match_rule: TrafficMatchRule
    default_label_value: str
    enable: bool
    match_mode: LaneRule.LaneMatchMode
    traffic_gray: TrafficGray
    revision: str
    ctime: str
    mtime: str
    etime: str
    priority: int
    description: str
    label_key: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., group_name: _Optional[str] = ..., traffic_match_rule: _Optional[_Union[TrafficMatchRule, _Mapping]] = ..., default_label_value: _Optional[str] = ..., enable: _Optional[bool] = ..., match_mode: _Optional[_Union[LaneRule.LaneMatchMode, str]] = ..., traffic_gray: _Optional[_Union[TrafficGray, _Mapping]] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., priority: _Optional[int] = ..., description: _Optional[str] = ..., label_key: _Optional[str] = ...) -> None: ...
