import datetime

from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateLimit(_message.Message):
    __slots__ = ("rules", "revision")
    RULES_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    revision: _wrappers_pb2.StringValue
    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("id", "service", "namespace", "subset", "priority", "resource", "type", "labels", "amounts", "action", "disable", "report", "ctime", "mtime", "revision", "service_token", "adjuster", "regex_combine", "amount_mode", "failover", "cluster", "method", "arguments", "name", "etime", "max_queue_delay", "concurrencyAmount", "customResponse", "metadata", "editable", "deleteable")
    class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QPS: _ClassVar[Rule.Resource]
        CONCURRENCY: _ClassVar[Rule.Resource]
    QPS: Rule.Resource
    CONCURRENCY: Rule.Resource
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GLOBAL: _ClassVar[Rule.Type]
        LOCAL: _ClassVar[Rule.Type]
    GLOBAL: Rule.Type
    LOCAL: Rule.Type
    class AmountMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GLOBAL_TOTAL: _ClassVar[Rule.AmountMode]
        SHARE_EQUALLY: _ClassVar[Rule.AmountMode]
    GLOBAL_TOTAL: Rule.AmountMode
    SHARE_EQUALLY: Rule.AmountMode
    class FailoverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILOVER_LOCAL: _ClassVar[Rule.FailoverType]
        FAILOVER_PASS: _ClassVar[Rule.FailoverType]
    FAILOVER_LOCAL: Rule.FailoverType
    FAILOVER_PASS: Rule.FailoverType
    class SubsetEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SUBSET_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    AMOUNTS_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ADJUSTER_FIELD_NUMBER: _ClassVar[int]
    REGEX_COMBINE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MODE_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    MAX_QUEUE_DELAY_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCYAMOUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMRESPONSE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    DELETEABLE_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    subset: _containers.MessageMap[str, _model_pb2.MatchString]
    priority: _wrappers_pb2.UInt32Value
    resource: Rule.Resource
    type: Rule.Type
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    amounts: _containers.RepeatedCompositeFieldContainer[Amount]
    action: _wrappers_pb2.StringValue
    disable: _wrappers_pb2.BoolValue
    report: Report
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    adjuster: AmountAdjuster
    regex_combine: _wrappers_pb2.BoolValue
    amount_mode: Rule.AmountMode
    failover: Rule.FailoverType
    cluster: RateLimitCluster
    method: _model_pb2.MatchString
    arguments: _containers.RepeatedCompositeFieldContainer[MatchArgument]
    name: _wrappers_pb2.StringValue
    etime: _wrappers_pb2.StringValue
    max_queue_delay: _wrappers_pb2.UInt32Value
    concurrencyAmount: ConcurrencyAmount
    customResponse: CustomResponse
    metadata: _containers.ScalarMap[str, str]
    editable: bool
    deleteable: bool
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., subset: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., resource: _Optional[_Union[Rule.Resource, str]] = ..., type: _Optional[_Union[Rule.Type, str]] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., amounts: _Optional[_Iterable[_Union[Amount, _Mapping]]] = ..., action: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., disable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., report: _Optional[_Union[Report, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., adjuster: _Optional[_Union[AmountAdjuster, _Mapping]] = ..., regex_combine: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., amount_mode: _Optional[_Union[Rule.AmountMode, str]] = ..., failover: _Optional[_Union[Rule.FailoverType, str]] = ..., cluster: _Optional[_Union[RateLimitCluster, _Mapping]] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[MatchArgument, _Mapping]]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., etime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., max_queue_delay: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., concurrencyAmount: _Optional[_Union[ConcurrencyAmount, _Mapping]] = ..., customResponse: _Optional[_Union[CustomResponse, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., editable: _Optional[bool] = ..., deleteable: _Optional[bool] = ...) -> None: ...

class MatchArgument(_message.Message):
    __slots__ = ("type", "key", "value")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM: _ClassVar[MatchArgument.Type]
        METHOD: _ClassVar[MatchArgument.Type]
        HEADER: _ClassVar[MatchArgument.Type]
        QUERY: _ClassVar[MatchArgument.Type]
        CALLER_SERVICE: _ClassVar[MatchArgument.Type]
        CALLER_IP: _ClassVar[MatchArgument.Type]
        CALLER_METADATA: _ClassVar[MatchArgument.Type]
    CUSTOM: MatchArgument.Type
    METHOD: MatchArgument.Type
    HEADER: MatchArgument.Type
    QUERY: MatchArgument.Type
    CALLER_SERVICE: MatchArgument.Type
    CALLER_IP: MatchArgument.Type
    CALLER_METADATA: MatchArgument.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    type: MatchArgument.Type
    key: str
    value: _model_pb2.MatchString
    def __init__(self, type: _Optional[_Union[MatchArgument.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...

class ConcurrencyAmount(_message.Message):
    __slots__ = ("maxAmount",)
    MAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    maxAmount: int
    def __init__(self, maxAmount: _Optional[int] = ...) -> None: ...

class CustomResponse(_message.Message):
    __slots__ = ("body",)
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: str
    def __init__(self, body: _Optional[str] = ...) -> None: ...

class RateLimitCluster(_message.Message):
    __slots__ = ("service", "namespace")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Amount(_message.Message):
    __slots__ = ("maxAmount", "validDuration", "precision", "startAmount", "minAmount")
    MAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    VALIDDURATION_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    STARTAMOUNT_FIELD_NUMBER: _ClassVar[int]
    MINAMOUNT_FIELD_NUMBER: _ClassVar[int]
    maxAmount: _wrappers_pb2.UInt32Value
    validDuration: _duration_pb2.Duration
    precision: _wrappers_pb2.UInt32Value
    startAmount: _wrappers_pb2.UInt32Value
    minAmount: _wrappers_pb2.UInt32Value
    def __init__(self, maxAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., validDuration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., precision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., startAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., minAmount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ("interval", "amountPercent")
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AMOUNTPERCENT_FIELD_NUMBER: _ClassVar[int]
    interval: _duration_pb2.Duration
    amountPercent: _wrappers_pb2.UInt32Value
    def __init__(self, interval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., amountPercent: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class AmountAdjuster(_message.Message):
    __slots__ = ("climb",)
    CLIMB_FIELD_NUMBER: _ClassVar[int]
    climb: ClimbConfig
    def __init__(self, climb: _Optional[_Union[ClimbConfig, _Mapping]] = ...) -> None: ...

class ClimbConfig(_message.Message):
    __slots__ = ("enable", "metric", "policy", "throttling")
    class MetricConfig(_message.Message):
        __slots__ = ("window", "precision", "reportInterval")
        WINDOW_FIELD_NUMBER: _ClassVar[int]
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        REPORTINTERVAL_FIELD_NUMBER: _ClassVar[int]
        window: _duration_pb2.Duration
        precision: _wrappers_pb2.UInt32Value
        reportInterval: _duration_pb2.Duration
        def __init__(self, window: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., precision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., reportInterval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    class TriggerPolicy(_message.Message):
        __slots__ = ("errorRate", "slowRate")
        class ErrorRate(_message.Message):
            __slots__ = ("enable", "requestVolumeThreshold", "errorRate", "specials")
            class SpecialConfig(_message.Message):
                __slots__ = ("type", "errorCodes", "errorRate")
                TYPE_FIELD_NUMBER: _ClassVar[int]
                ERRORCODES_FIELD_NUMBER: _ClassVar[int]
                ERRORRATE_FIELD_NUMBER: _ClassVar[int]
                type: _wrappers_pb2.StringValue
                errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
                errorRate: _wrappers_pb2.Int32Value
                def __init__(self, type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., errorRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            REQUESTVOLUMETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
            ERRORRATE_FIELD_NUMBER: _ClassVar[int]
            SPECIALS_FIELD_NUMBER: _ClassVar[int]
            enable: _wrappers_pb2.BoolValue
            requestVolumeThreshold: _wrappers_pb2.UInt32Value
            errorRate: _wrappers_pb2.Int32Value
            specials: _containers.RepeatedCompositeFieldContainer[ClimbConfig.TriggerPolicy.ErrorRate.SpecialConfig]
            def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., requestVolumeThreshold: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., specials: _Optional[_Iterable[_Union[ClimbConfig.TriggerPolicy.ErrorRate.SpecialConfig, _Mapping]]] = ...) -> None: ...
        class SlowRate(_message.Message):
            __slots__ = ("enable", "maxRt", "slowRate")
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            MAXRT_FIELD_NUMBER: _ClassVar[int]
            SLOWRATE_FIELD_NUMBER: _ClassVar[int]
            enable: _wrappers_pb2.BoolValue
            maxRt: _duration_pb2.Duration
            slowRate: _wrappers_pb2.Int32Value
            def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., maxRt: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., slowRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
        ERRORRATE_FIELD_NUMBER: _ClassVar[int]
        SLOWRATE_FIELD_NUMBER: _ClassVar[int]
        errorRate: ClimbConfig.TriggerPolicy.ErrorRate
        slowRate: ClimbConfig.TriggerPolicy.SlowRate
        def __init__(self, errorRate: _Optional[_Union[ClimbConfig.TriggerPolicy.ErrorRate, _Mapping]] = ..., slowRate: _Optional[_Union[ClimbConfig.TriggerPolicy.SlowRate, _Mapping]] = ...) -> None: ...
    class ClimbThrottling(_message.Message):
        __slots__ = ("coldBelowTuneDownRate", "coldBelowTuneUpRate", "coldAboveTuneDownRate", "coldAboveTuneUpRate", "limitThresholdToTuneUp", "judgeDuration", "tuneUpPeriod", "tuneDownPeriod")
        COLDBELOWTUNEDOWNRATE_FIELD_NUMBER: _ClassVar[int]
        COLDBELOWTUNEUPRATE_FIELD_NUMBER: _ClassVar[int]
        COLDABOVETUNEDOWNRATE_FIELD_NUMBER: _ClassVar[int]
        COLDABOVETUNEUPRATE_FIELD_NUMBER: _ClassVar[int]
        LIMITTHRESHOLDTOTUNEUP_FIELD_NUMBER: _ClassVar[int]
        JUDGEDURATION_FIELD_NUMBER: _ClassVar[int]
        TUNEUPPERIOD_FIELD_NUMBER: _ClassVar[int]
        TUNEDOWNPERIOD_FIELD_NUMBER: _ClassVar[int]
        coldBelowTuneDownRate: _wrappers_pb2.Int32Value
        coldBelowTuneUpRate: _wrappers_pb2.Int32Value
        coldAboveTuneDownRate: _wrappers_pb2.Int32Value
        coldAboveTuneUpRate: _wrappers_pb2.Int32Value
        limitThresholdToTuneUp: _wrappers_pb2.Int32Value
        judgeDuration: _duration_pb2.Duration
        tuneUpPeriod: _wrappers_pb2.Int32Value
        tuneDownPeriod: _wrappers_pb2.Int32Value
        def __init__(self, coldBelowTuneDownRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldBelowTuneUpRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldAboveTuneDownRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., coldAboveTuneUpRate: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., limitThresholdToTuneUp: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., judgeDuration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., tuneUpPeriod: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., tuneDownPeriod: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_FIELD_NUMBER: _ClassVar[int]
    enable: _wrappers_pb2.BoolValue
    metric: ClimbConfig.MetricConfig
    policy: ClimbConfig.TriggerPolicy
    throttling: ClimbConfig.ClimbThrottling
    def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., metric: _Optional[_Union[ClimbConfig.MetricConfig, _Mapping]] = ..., policy: _Optional[_Union[ClimbConfig.TriggerPolicy, _Mapping]] = ..., throttling: _Optional[_Union[ClimbConfig.ClimbThrottling, _Mapping]] = ...) -> None: ...

class RateLimitExportRequest(_message.Message):
    __slots__ = ("namespace", "service", "name", "type", "disable", "start_time", "end_time", "labels", "ids")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    namespace: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    type: _wrappers_pb2.StringValue
    disable: _wrappers_pb2.BoolValue
    start_time: _wrappers_pb2.StringValue
    end_time: _wrappers_pb2.StringValue
    labels: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., disable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., start_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., end_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., labels: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ...) -> None: ...

class RateLimitExportResponse(_message.Message):
    __slots__ = ("code", "info", "data", "base64_content")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    BASE64_CONTENT_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    data: _wrappers_pb2.BytesValue
    base64_content: _wrappers_pb2.StringValue
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., data: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ..., base64_content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class RateLimitImportResponse(_message.Message):
    __slots__ = ("code", "info", "successRateLimitRules", "failRateLimitRules")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SUCCESSRATELIMITRULES_FIELD_NUMBER: _ClassVar[int]
    FAILRATELIMITRULES_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    successRateLimitRules: _containers.RepeatedCompositeFieldContainer[Rule]
    failRateLimitRules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., successRateLimitRules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ..., failRateLimitRules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ...) -> None: ...

class RateLimitImportRequest(_message.Message):
    __slots__ = ("base64_content", "namespace")
    BASE64_CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    base64_content: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    def __init__(self, base64_content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
