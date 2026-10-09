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

class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[Level]
    SERVICE: _ClassVar[Level]
    METHOD: _ClassVar[Level]
    GROUP: _ClassVar[Level]
    INSTANCE: _ClassVar[Level]
UNKNOWN: Level
SERVICE: Level
METHOD: Level
GROUP: Level
INSTANCE: Level

class CircuitBreaker(_message.Message):
    __slots__ = ("id", "version", "name", "namespace", "service", "service_namespace", "inbounds", "outbounds", "token", "owners", "business", "department", "comment", "ctime", "mtime", "revision", "rules")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    INBOUNDS_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    version: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    service_namespace: _wrappers_pb2.StringValue
    inbounds: _containers.RepeatedCompositeFieldContainer[CbRule]
    outbounds: _containers.RepeatedCompositeFieldContainer[CbRule]
    token: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    business: _wrappers_pb2.StringValue
    department: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    rules: _containers.RepeatedCompositeFieldContainer[CircuitBreakerRule]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., inbounds: _Optional[_Iterable[_Union[CbRule, _Mapping]]] = ..., outbounds: _Optional[_Iterable[_Union[CbRule, _Mapping]]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., business: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., department: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rules: _Optional[_Iterable[_Union[CircuitBreakerRule, _Mapping]]] = ...) -> None: ...

class SourceMatcher(_message.Message):
    __slots__ = ("service", "namespace", "labels")
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
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class RecoverConfig(_message.Message):
    __slots__ = ("sleepWindow", "maxRetryAfterHalfOpen", "requestRateAfterHalfOpen", "successRateToClose", "requestCountAfterHalfOpen", "outlierDetectWhen")
    class OutlierDetectWhen(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NEVER: _ClassVar[RecoverConfig.OutlierDetectWhen]
        ON_RECOVER: _ClassVar[RecoverConfig.OutlierDetectWhen]
        ALWAYS: _ClassVar[RecoverConfig.OutlierDetectWhen]
    NEVER: RecoverConfig.OutlierDetectWhen
    ON_RECOVER: RecoverConfig.OutlierDetectWhen
    ALWAYS: RecoverConfig.OutlierDetectWhen
    SLEEPWINDOW_FIELD_NUMBER: _ClassVar[int]
    MAXRETRYAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    REQUESTRATEAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    SUCCESSRATETOCLOSE_FIELD_NUMBER: _ClassVar[int]
    REQUESTCOUNTAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    OUTLIERDETECTWHEN_FIELD_NUMBER: _ClassVar[int]
    sleepWindow: _duration_pb2.Duration
    maxRetryAfterHalfOpen: _wrappers_pb2.UInt32Value
    requestRateAfterHalfOpen: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    successRateToClose: _wrappers_pb2.UInt32Value
    requestCountAfterHalfOpen: _wrappers_pb2.UInt32Value
    outlierDetectWhen: RecoverConfig.OutlierDetectWhen
    def __init__(self, sleepWindow: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., maxRetryAfterHalfOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., requestRateAfterHalfOpen: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ..., successRateToClose: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., requestCountAfterHalfOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., outlierDetectWhen: _Optional[_Union[RecoverConfig.OutlierDetectWhen, str]] = ...) -> None: ...

class CbPolicy(_message.Message):
    __slots__ = ("errorRate", "slowRate", "judgeDuration", "maxEjectionPercent", "consecutive")
    class ErrRateConfig(_message.Message):
        __slots__ = ("enable", "requestVolumeThreshold", "errorRateToPreserved", "errorRateToOpen", "specials")
        class SpecialConfig(_message.Message):
            __slots__ = ("type", "errorCodes", "errorRateToPreserved", "errorRateToOpen")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            ERRORCODES_FIELD_NUMBER: _ClassVar[int]
            ERRORRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
            ERRORRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
            type: _wrappers_pb2.StringValue
            errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
            errorRateToPreserved: _wrappers_pb2.UInt32Value
            errorRateToOpen: _wrappers_pb2.UInt32Value
            def __init__(self, type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., errorRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        REQUESTVOLUMETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
        ERRORRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        ERRORRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
        SPECIALS_FIELD_NUMBER: _ClassVar[int]
        enable: _wrappers_pb2.BoolValue
        requestVolumeThreshold: _wrappers_pb2.UInt32Value
        errorRateToPreserved: _wrappers_pb2.UInt32Value
        errorRateToOpen: _wrappers_pb2.UInt32Value
        specials: _containers.RepeatedCompositeFieldContainer[CbPolicy.ErrRateConfig.SpecialConfig]
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., requestVolumeThreshold: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., specials: _Optional[_Iterable[_Union[CbPolicy.ErrRateConfig.SpecialConfig, _Mapping]]] = ...) -> None: ...
    class SlowRateConfig(_message.Message):
        __slots__ = ("enable", "maxRt", "slowRateToPreserved", "slowRateToOpen")
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        MAXRT_FIELD_NUMBER: _ClassVar[int]
        SLOWRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        SLOWRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
        enable: _wrappers_pb2.BoolValue
        maxRt: _duration_pb2.Duration
        slowRateToPreserved: _wrappers_pb2.UInt32Value
        slowRateToOpen: _wrappers_pb2.UInt32Value
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., maxRt: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., slowRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., slowRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    class ConsecutiveErrConfig(_message.Message):
        __slots__ = ("enable", "consecutiveErrorToPreserved", "consecutiveErrorToOpen")
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        CONSECUTIVEERRORTOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        CONSECUTIVEERRORTOOPEN_FIELD_NUMBER: _ClassVar[int]
        enable: _wrappers_pb2.BoolValue
        consecutiveErrorToPreserved: _wrappers_pb2.UInt32Value
        consecutiveErrorToOpen: _wrappers_pb2.UInt32Value
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., consecutiveErrorToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., consecutiveErrorToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    ERRORRATE_FIELD_NUMBER: _ClassVar[int]
    SLOWRATE_FIELD_NUMBER: _ClassVar[int]
    JUDGEDURATION_FIELD_NUMBER: _ClassVar[int]
    MAXEJECTIONPERCENT_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVE_FIELD_NUMBER: _ClassVar[int]
    errorRate: CbPolicy.ErrRateConfig
    slowRate: CbPolicy.SlowRateConfig
    judgeDuration: _duration_pb2.Duration
    maxEjectionPercent: _wrappers_pb2.UInt32Value
    consecutive: CbPolicy.ConsecutiveErrConfig
    def __init__(self, errorRate: _Optional[_Union[CbPolicy.ErrRateConfig, _Mapping]] = ..., slowRate: _Optional[_Union[CbPolicy.SlowRateConfig, _Mapping]] = ..., judgeDuration: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., maxEjectionPercent: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., consecutive: _Optional[_Union[CbPolicy.ConsecutiveErrConfig, _Mapping]] = ...) -> None: ...

class DestinationSet(_message.Message):
    __slots__ = ("service", "namespace", "metadata", "resource", "type", "scope", "metricWindow", "metricPrecision", "updateInterval", "recover", "policy", "method", "errorCodes")
    class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUBSET: _ClassVar[DestinationSet.Resource]
        INSTANCE: _ClassVar[DestinationSet.Resource]
    SUBSET: DestinationSet.Resource
    INSTANCE: DestinationSet.Resource
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        GLOBAL: _ClassVar[DestinationSet.Type]
        LOCAL: _ClassVar[DestinationSet.Type]
    GLOBAL: DestinationSet.Type
    LOCAL: DestinationSet.Type
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[DestinationSet.Scope]
        CURRENT: _ClassVar[DestinationSet.Scope]
    ALL: DestinationSet.Scope
    CURRENT: DestinationSet.Scope
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
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    METRICWINDOW_FIELD_NUMBER: _ClassVar[int]
    METRICPRECISION_FIELD_NUMBER: _ClassVar[int]
    UPDATEINTERVAL_FIELD_NUMBER: _ClassVar[int]
    RECOVER_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    ERRORCODES_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    resource: DestinationSet.Resource
    type: DestinationSet.Type
    scope: DestinationSet.Scope
    metricWindow: _duration_pb2.Duration
    metricPrecision: _wrappers_pb2.UInt32Value
    updateInterval: _duration_pb2.Duration
    recover: RecoverConfig
    policy: CbPolicy
    method: _model_pb2.MatchString
    errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., resource: _Optional[_Union[DestinationSet.Resource, str]] = ..., type: _Optional[_Union[DestinationSet.Type, str]] = ..., scope: _Optional[_Union[DestinationSet.Scope, str]] = ..., metricWindow: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., metricPrecision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., updateInterval: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., recover: _Optional[_Union[RecoverConfig, _Mapping]] = ..., policy: _Optional[_Union[CbPolicy, _Mapping]] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ...) -> None: ...

class CbRule(_message.Message):
    __slots__ = ("sources", "destinations")
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[SourceMatcher]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationSet]
    def __init__(self, sources: _Optional[_Iterable[_Union[SourceMatcher, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationSet, _Mapping]]] = ...) -> None: ...

class RuleMatcher(_message.Message):
    __slots__ = ("source", "destination")
    class SourceService(_message.Message):
        __slots__ = ("service", "namespace")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        service: str
        namespace: str
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...
    class DestinationService(_message.Message):
        __slots__ = ("service", "namespace", "method")
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        service: str
        namespace: str
        method: _model_pb2.MatchString
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    source: RuleMatcher.SourceService
    destination: RuleMatcher.DestinationService
    def __init__(self, source: _Optional[_Union[RuleMatcher.SourceService, _Mapping]] = ..., destination: _Optional[_Union[RuleMatcher.DestinationService, _Mapping]] = ...) -> None: ...

class CircuitBreakerRule(_message.Message):
    __slots__ = ("id", "name", "namespace", "enable", "revision", "ctime", "mtime", "etime", "description", "level", "rule_matcher", "error_conditions", "trigger_condition", "max_ejection_percent", "recoverCondition", "faultDetectConfig", "fallbackConfig", "block_configs", "priority", "metadata", "regex_separate")
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
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    RULE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    MAX_EJECTION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    RECOVERCONDITION_FIELD_NUMBER: _ClassVar[int]
    FAULTDETECTCONFIG_FIELD_NUMBER: _ClassVar[int]
    FALLBACKCONFIG_FIELD_NUMBER: _ClassVar[int]
    BLOCK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    REGEX_SEPARATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    namespace: str
    enable: bool
    revision: str
    ctime: str
    mtime: str
    etime: str
    description: str
    level: Level
    rule_matcher: RuleMatcher
    error_conditions: _containers.RepeatedCompositeFieldContainer[ErrorCondition]
    trigger_condition: _containers.RepeatedCompositeFieldContainer[TriggerCondition]
    max_ejection_percent: int
    recoverCondition: RecoverCondition
    faultDetectConfig: FaultDetectConfig
    fallbackConfig: FallbackConfig
    block_configs: _containers.RepeatedCompositeFieldContainer[BlockConfig]
    priority: int
    metadata: _containers.ScalarMap[str, str]
    regex_separate: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., enable: _Optional[bool] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., description: _Optional[str] = ..., level: _Optional[_Union[Level, str]] = ..., rule_matcher: _Optional[_Union[RuleMatcher, _Mapping]] = ..., error_conditions: _Optional[_Iterable[_Union[ErrorCondition, _Mapping]]] = ..., trigger_condition: _Optional[_Iterable[_Union[TriggerCondition, _Mapping]]] = ..., max_ejection_percent: _Optional[int] = ..., recoverCondition: _Optional[_Union[RecoverCondition, _Mapping]] = ..., faultDetectConfig: _Optional[_Union[FaultDetectConfig, _Mapping]] = ..., fallbackConfig: _Optional[_Union[FallbackConfig, _Mapping]] = ..., block_configs: _Optional[_Iterable[_Union[BlockConfig, _Mapping]]] = ..., priority: _Optional[int] = ..., metadata: _Optional[_Mapping[str, str]] = ..., regex_separate: _Optional[bool] = ...) -> None: ...

class ErrorCondition(_message.Message):
    __slots__ = ("input_type", "condition")
    class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ErrorCondition.InputType]
        RET_CODE: _ClassVar[ErrorCondition.InputType]
        DELAY: _ClassVar[ErrorCondition.InputType]
    UNKNOWN: ErrorCondition.InputType
    RET_CODE: ErrorCondition.InputType
    DELAY: ErrorCondition.InputType
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    input_type: ErrorCondition.InputType
    condition: _model_pb2.MatchString
    def __init__(self, input_type: _Optional[_Union[ErrorCondition.InputType, str]] = ..., condition: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...

class TriggerCondition(_message.Message):
    __slots__ = ("trigger_type", "error_count", "error_percent", "interval", "minimum_request")
    class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TriggerCondition.TriggerType]
        ERROR_RATE: _ClassVar[TriggerCondition.TriggerType]
        CONSECUTIVE_ERROR: _ClassVar[TriggerCondition.TriggerType]
    UNKNOWN: TriggerCondition.TriggerType
    ERROR_RATE: TriggerCondition.TriggerType
    CONSECUTIVE_ERROR: TriggerCondition.TriggerType
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_PERCENT_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    trigger_type: TriggerCondition.TriggerType
    error_count: int
    error_percent: int
    interval: int
    minimum_request: int
    def __init__(self, trigger_type: _Optional[_Union[TriggerCondition.TriggerType, str]] = ..., error_count: _Optional[int] = ..., error_percent: _Optional[int] = ..., interval: _Optional[int] = ..., minimum_request: _Optional[int] = ...) -> None: ...

class RecoverCondition(_message.Message):
    __slots__ = ("sleep_window", "consecutiveSuccess")
    SLEEP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CONSECUTIVESUCCESS_FIELD_NUMBER: _ClassVar[int]
    sleep_window: int
    consecutiveSuccess: int
    def __init__(self, sleep_window: _Optional[int] = ..., consecutiveSuccess: _Optional[int] = ...) -> None: ...

class FaultDetectConfig(_message.Message):
    __slots__ = ("enable",)
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    def __init__(self, enable: _Optional[bool] = ...) -> None: ...

class BlockConfig(_message.Message):
    __slots__ = ("name", "api", "error_conditions", "trigger_conditions", "recoverCondition")
    NAME_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    RECOVERCONDITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    api: _model_pb2.API
    error_conditions: _containers.RepeatedCompositeFieldContainer[ErrorCondition]
    trigger_conditions: _containers.RepeatedCompositeFieldContainer[TriggerCondition]
    recoverCondition: RecoverCondition
    def __init__(self, name: _Optional[str] = ..., api: _Optional[_Union[_model_pb2.API, _Mapping]] = ..., error_conditions: _Optional[_Iterable[_Union[ErrorCondition, _Mapping]]] = ..., trigger_conditions: _Optional[_Iterable[_Union[TriggerCondition, _Mapping]]] = ..., recoverCondition: _Optional[_Union[RecoverCondition, _Mapping]] = ...) -> None: ...

class FallbackConfig(_message.Message):
    __slots__ = ("enable", "response")
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    response: FallbackResponse
    def __init__(self, enable: _Optional[bool] = ..., response: _Optional[_Union[FallbackResponse, _Mapping]] = ...) -> None: ...

class FallbackResponse(_message.Message):
    __slots__ = ("code", "headers", "body")
    class MessageHeader(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    code: int
    headers: _containers.RepeatedCompositeFieldContainer[FallbackResponse.MessageHeader]
    body: str
    def __init__(self, code: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[FallbackResponse.MessageHeader, _Mapping]]] = ..., body: _Optional[str] = ...) -> None: ...
