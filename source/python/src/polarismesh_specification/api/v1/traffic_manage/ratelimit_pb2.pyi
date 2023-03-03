from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Amount(_message.Message):
    __slots__ = ["maxAmount", "minAmount", "precision", "startAmount", "validDuration"]
    MAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    STARTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDDURATION_FIELD_NUMBER: _ClassVar[int]
    maxAmount: _wrappers_pb2.UInt32Value
    minAmount: _wrappers_pb2.UInt32Value
    precision: _wrappers_pb2.UInt32Value
    startAmount: _wrappers_pb2.UInt32Value
    validDuration: _duration_pb2.Duration
    def __init__(self, maxAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., validDuration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., precision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., startAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., minAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class AmountAdjuster(_message.Message):
    __slots__ = ["climb"]
    CLIMB_FIELD_NUMBER: _ClassVar[int]
    climb: ClimbConfig
    def __init__(self, climb: _Optional[_Union[ClimbConfig, _Mapping]] = ...) -> None: ...

class ClimbConfig(_message.Message):
    __slots__ = ["enable", "metric", "policy", "throttling"]
    class ClimbThrottling(_message.Message):
        __slots__ = ["coldAboveTuneDownRate", "coldAboveTuneUpRate", "coldBelowTuneDownRate", "coldBelowTuneUpRate", "judgeDuration", "limitThresholdToTuneUp", "tuneDownPeriod", "tuneUpPeriod"]
        COLDABOVETUNEDOWNRATE_FIELD_NUMBER: _ClassVar[int]
        COLDABOVETUNEUPRATE_FIELD_NUMBER: _ClassVar[int]
        COLDBELOWTUNEDOWNRATE_FIELD_NUMBER: _ClassVar[int]
        COLDBELOWTUNEUPRATE_FIELD_NUMBER: _ClassVar[int]
        JUDGEDURATION_FIELD_NUMBER: _ClassVar[int]
        LIMITTHRESHOLDTOTUNEUP_FIELD_NUMBER: _ClassVar[int]
        TUNEDOWNPERIOD_FIELD_NUMBER: _ClassVar[int]
        TUNEUPPERIOD_FIELD_NUMBER: _ClassVar[int]
        coldAboveTuneDownRate: _wrappers_pb2.Int32Value
        coldAboveTuneUpRate: _wrappers_pb2.Int32Value
        coldBelowTuneDownRate: _wrappers_pb2.Int32Value
        coldBelowTuneUpRate: _wrappers_pb2.Int32Value
        judgeDuration: _duration_pb2.Duration
        limitThresholdToTuneUp: _wrappers_pb2.Int32Value
        tuneDownPeriod: _wrappers_pb2.Int32Value
        tuneUpPeriod: _wrappers_pb2.Int32Value
        def __init__(self, coldBelowTuneDownRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldBelowTuneUpRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldAboveTuneDownRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldAboveTuneUpRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., limitThresholdToTuneUp: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., judgeDuration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tuneUpPeriod: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., tuneDownPeriod: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    class MetricConfig(_message.Message):
        __slots__ = ["precision", "reportInterval", "window"]
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        REPORTINTERVAL_FIELD_NUMBER: _ClassVar[int]
        WINDOW_FIELD_NUMBER: _ClassVar[int]
        precision: _wrappers_pb2.UInt32Value
        reportInterval: _duration_pb2.Duration
        window: _duration_pb2.Duration
        def __init__(self, window: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., precision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., reportInterval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class TriggerPolicy(_message.Message):
        __slots__ = ["errorRate", "slowRate"]
        class ErrorRate(_message.Message):
            __slots__ = ["enable", "errorRate", "requestVolumeThreshold", "specials"]
            class SpecialConfig(_message.Message):
                __slots__ = ["errorCodes", "errorRate", "type"]
                ERRORCODES_FIELD_NUMBER: _ClassVar[int]
                ERRORRATE_FIELD_NUMBER: _ClassVar[int]
                TYPE_FIELD_NUMBER: _ClassVar[int]
                errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
                errorRate: _wrappers_pb2.Int32Value
                type: _wrappers_pb2.StringValue
                def __init__(self, type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., errorRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            ERRORRATE_FIELD_NUMBER: _ClassVar[int]
            REQUESTVOLUMETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
            SPECIALS_FIELD_NUMBER: _ClassVar[int]
            enable: _wrappers_pb2.BoolValue
            errorRate: _wrappers_pb2.Int32Value
            requestVolumeThreshold: _wrappers_pb2.UInt32Value
            specials: _containers.RepeatedCompositeFieldContainer[ClimbConfig.TriggerPolicy.ErrorRate.SpecialConfig]
            def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., requestVolumeThreshold: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., specials: _Optional[_Iterable[_Union[ClimbConfig.TriggerPolicy.ErrorRate.SpecialConfig, _Mapping]]] = ...) -> None: ...
        class SlowRate(_message.Message):
            __slots__ = ["enable", "maxRt", "slowRate"]
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            MAXRT_FIELD_NUMBER: _ClassVar[int]
            SLOWRATE_FIELD_NUMBER: _ClassVar[int]
            enable: _wrappers_pb2.BoolValue
            maxRt: _duration_pb2.Duration
            slowRate: _wrappers_pb2.Int32Value
            def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., maxRt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., slowRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        ERRORRATE_FIELD_NUMBER: _ClassVar[int]
        SLOWRATE_FIELD_NUMBER: _ClassVar[int]
        errorRate: ClimbConfig.TriggerPolicy.ErrorRate
        slowRate: ClimbConfig.TriggerPolicy.SlowRate
        def __init__(self, errorRate: _Optional[_Union[ClimbConfig.TriggerPolicy.ErrorRate, _Mapping]] = ..., slowRate: _Optional[_Union[ClimbConfig.TriggerPolicy.SlowRate, _Mapping]] = ...) -> None: ...
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_FIELD_NUMBER: _ClassVar[int]
    enable: _wrappers_pb2.BoolValue
    metric: ClimbConfig.MetricConfig
    policy: ClimbConfig.TriggerPolicy
    throttling: ClimbConfig.ClimbThrottling
    def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., metric: _Optional[_Union[ClimbConfig.MetricConfig, _Mapping]] = ..., policy: _Optional[_Union[ClimbConfig.TriggerPolicy, _Mapping]] = ..., throttling: _Optional[_Union[ClimbConfig.ClimbThrottling, _Mapping]] = ...) -> None: ...

class MatchArgument(_message.Message):
    __slots__ = ["key", "type", "value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CALLER_IP: MatchArgument.Type
    CALLER_SERVICE: MatchArgument.Type
    CUSTOM: MatchArgument.Type
    HEADER: MatchArgument.Type
    KEY_FIELD_NUMBER: _ClassVar[int]
    METHOD: MatchArgument.Type
    QUERY: MatchArgument.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    type: MatchArgument.Type
    value: _model_pb2.MatchString
    def __init__(self, type: _Optional[_Union[MatchArgument.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...

class RateLimit(_message.Message):
    __slots__ = ["revision", "rules"]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    revision: _wrappers_pb2.StringValue
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RateLimitCluster(_message.Message):
    __slots__ = ["namespace", "service"]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    namespace: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ["amountPercent", "interval"]
    AMOUNTPERCENT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    amountPercent: _wrappers_pb2.UInt32Value
    interval: _duration_pb2.Duration
    def __init__(self, interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., amountPercent: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ["action", "adjuster", "amount_mode", "amounts", "arguments", "cluster", "ctime", "disable", "etime", "failover", "id", "labels", "max_queue_delay", "method", "mtime", "name", "namespace", "priority", "regex_combine", "report", "resource", "revision", "service", "service_token", "subset", "type"]
    class AmountMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class FailoverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    class SubsetEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ADJUSTER_FIELD_NUMBER: _ClassVar[int]
    AMOUNTS_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MODE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY: Rule.Resource
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_LOCAL: Rule.FailoverType
    FAILOVER_PASS: Rule.FailoverType
    GLOBAL: Rule.Type
    GLOBAL_TOTAL: Rule.AmountMode
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCAL: Rule.Type
    MAX_QUEUE_DELAY_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    QPS: Rule.Resource
    REGEX_COMBINE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHARE_EQUALLY: Rule.AmountMode
    SUBSET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    action: _wrappers_pb2.StringValue
    adjuster: AmountAdjuster
    amount_mode: Rule.AmountMode
    amounts: _containers.RepeatedCompositeFieldContainer[Amount]
    arguments: _containers.RepeatedCompositeFieldContainer[MatchArgument]
    cluster: RateLimitCluster
    ctime: _wrappers_pb2.StringValue
    disable: _wrappers_pb2.BoolValue
    etime: _wrappers_pb2.StringValue
    failover: Rule.FailoverType
    id: _wrappers_pb2.StringValue
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    max_queue_delay: _wrappers_pb2.UInt32Value
    method: _model_pb2.MatchString
    mtime: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    priority: _wrappers_pb2.UInt32Value
    regex_combine: _wrappers_pb2.BoolValue
    report: Report
    resource: Rule.Resource
    revision: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    subset: _containers.MessageMap[str, _model_pb2.MatchString]
    type: Rule.Type
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., subset: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., resource: _Optional[_Union[Rule.Resource, str]] = ..., type: _Optional[_Union[Rule.Type, str]] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., amounts: _Optional[_Iterable[_Union[Amount, _Mapping]]] = ..., action: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., disable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., report: _Optional[_Union[Report, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., adjuster: _Optional[_Union[AmountAdjuster, _Mapping]] = ..., regex_combine: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., amount_mode: _Optional[_Union[Rule.AmountMode, str]] = ..., failover: _Optional[_Union[Rule.FailoverType, str]] = ..., cluster: _Optional[_Union[RateLimitCluster, _Mapping]] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[MatchArgument, _Mapping]]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., etime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_queue_delay: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
