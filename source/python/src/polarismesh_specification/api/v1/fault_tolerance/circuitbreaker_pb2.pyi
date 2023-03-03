from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GROUP: Level
INSTANCE: Level
METHOD: Level
SERVICE: Level
UNKNOWN: Level

class CbPolicy(_message.Message):
    __slots__ = ["consecutive", "errorRate", "judgeDuration", "maxEjectionPercent", "slowRate"]
    class ConsecutiveErrConfig(_message.Message):
        __slots__ = ["consecutiveErrorToOpen", "consecutiveErrorToPreserved", "enable"]
        CONSECUTIVEERRORTOOPEN_FIELD_NUMBER: _ClassVar[int]
        CONSECUTIVEERRORTOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        consecutiveErrorToOpen: _wrappers_pb2.UInt32Value
        consecutiveErrorToPreserved: _wrappers_pb2.UInt32Value
        enable: _wrappers_pb2.BoolValue
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., consecutiveErrorToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., consecutiveErrorToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    class ErrRateConfig(_message.Message):
        __slots__ = ["enable", "errorRateToOpen", "errorRateToPreserved", "requestVolumeThreshold", "specials"]
        class SpecialConfig(_message.Message):
            __slots__ = ["errorCodes", "errorRateToOpen", "errorRateToPreserved", "type"]
            ERRORCODES_FIELD_NUMBER: _ClassVar[int]
            ERRORRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
            ERRORRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
            errorRateToOpen: _wrappers_pb2.UInt32Value
            errorRateToPreserved: _wrappers_pb2.UInt32Value
            type: _wrappers_pb2.StringValue
            def __init__(self, type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ..., errorRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        ERRORRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
        ERRORRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        REQUESTVOLUMETHRESHOLD_FIELD_NUMBER: _ClassVar[int]
        SPECIALS_FIELD_NUMBER: _ClassVar[int]
        enable: _wrappers_pb2.BoolValue
        errorRateToOpen: _wrappers_pb2.UInt32Value
        errorRateToPreserved: _wrappers_pb2.UInt32Value
        requestVolumeThreshold: _wrappers_pb2.UInt32Value
        specials: _containers.RepeatedCompositeFieldContainer[CbPolicy.ErrRateConfig.SpecialConfig]
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., requestVolumeThreshold: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., errorRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., specials: _Optional[_Iterable[_Union[CbPolicy.ErrRateConfig.SpecialConfig, _Mapping]]] = ...) -> None: ...
    class SlowRateConfig(_message.Message):
        __slots__ = ["enable", "maxRt", "slowRateToOpen", "slowRateToPreserved"]
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        MAXRT_FIELD_NUMBER: _ClassVar[int]
        SLOWRATETOOPEN_FIELD_NUMBER: _ClassVar[int]
        SLOWRATETOPRESERVED_FIELD_NUMBER: _ClassVar[int]
        enable: _wrappers_pb2.BoolValue
        maxRt: _duration_pb2.Duration
        slowRateToOpen: _wrappers_pb2.UInt32Value
        slowRateToPreserved: _wrappers_pb2.UInt32Value
        def __init__(self, enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., maxRt: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., slowRateToPreserved: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., slowRateToOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    CONSECUTIVE_FIELD_NUMBER: _ClassVar[int]
    ERRORRATE_FIELD_NUMBER: _ClassVar[int]
    JUDGEDURATION_FIELD_NUMBER: _ClassVar[int]
    MAXEJECTIONPERCENT_FIELD_NUMBER: _ClassVar[int]
    SLOWRATE_FIELD_NUMBER: _ClassVar[int]
    consecutive: CbPolicy.ConsecutiveErrConfig
    errorRate: CbPolicy.ErrRateConfig
    judgeDuration: _duration_pb2.Duration
    maxEjectionPercent: _wrappers_pb2.UInt32Value
    slowRate: CbPolicy.SlowRateConfig
    def __init__(self, errorRate: _Optional[_Union[CbPolicy.ErrRateConfig, _Mapping]] = ..., slowRate: _Optional[_Union[CbPolicy.SlowRateConfig, _Mapping]] = ..., judgeDuration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maxEjectionPercent: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., consecutive: _Optional[_Union[CbPolicy.ConsecutiveErrConfig, _Mapping]] = ...) -> None: ...

class CbRule(_message.Message):
    __slots__ = ["destinations", "sources"]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[DestinationSet]
    sources: _containers.RepeatedCompositeFieldContainer[SourceMatcher]
    def __init__(self, sources: _Optional[_Iterable[_Union[SourceMatcher, _Mapping]]] = ..., destinations: _Optional[_Iterable[_Union[DestinationSet, _Mapping]]] = ...) -> None: ...

class CircuitBreaker(_message.Message):
    __slots__ = ["business", "comment", "ctime", "department", "id", "inbounds", "mtime", "name", "namespace", "outbounds", "owners", "revision", "rules", "service", "service_namespace", "token", "version"]
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INBOUNDS_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDS_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    business: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    department: _wrappers_pb2.StringValue
    id: _wrappers_pb2.StringValue
    inbounds: _containers.RepeatedCompositeFieldContainer[CbRule]
    mtime: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    outbounds: _containers.RepeatedCompositeFieldContainer[CbRule]
    owners: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    rules: _containers.RepeatedCompositeFieldContainer[CircuitBreakerRule]
    service: _wrappers_pb2.StringValue
    service_namespace: _wrappers_pb2.StringValue
    token: _wrappers_pb2.StringValue
    version: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., inbounds: _Optional[_Iterable[_Union[CbRule, _Mapping]]] = ..., outbounds: _Optional[_Iterable[_Union[CbRule, _Mapping]]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., business: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., department: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., rules: _Optional[_Iterable[_Union[CircuitBreakerRule, _Mapping]]] = ...) -> None: ...

class CircuitBreakerRule(_message.Message):
    __slots__ = ["ctime", "description", "enable", "error_conditions", "etime", "fallbackConfig", "faultDetectConfig", "id", "level", "max_ejection_percent", "mtime", "name", "namespace", "recoverCondition", "revision", "rule_matcher", "trigger_condition"]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    FALLBACKCONFIG_FIELD_NUMBER: _ClassVar[int]
    FAULTDETECTCONFIG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MAX_EJECTION_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECOVERCONDITION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    RULE_MATCHER_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    ctime: str
    description: str
    enable: bool
    error_conditions: _containers.RepeatedCompositeFieldContainer[ErrorCondition]
    etime: str
    fallbackConfig: FallbackConfig
    faultDetectConfig: FaultDetectConfig
    id: str
    level: Level
    max_ejection_percent: int
    mtime: str
    name: str
    namespace: str
    recoverCondition: RecoverCondition
    revision: str
    rule_matcher: RuleMatcher
    trigger_condition: _containers.RepeatedCompositeFieldContainer[TriggerCondition]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., enable: bool = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., description: _Optional[str] = ..., level: _Optional[_Union[Level, str]] = ..., rule_matcher: _Optional[_Union[RuleMatcher, _Mapping]] = ..., error_conditions: _Optional[_Iterable[_Union[ErrorCondition, _Mapping]]] = ..., trigger_condition: _Optional[_Iterable[_Union[TriggerCondition, _Mapping]]] = ..., max_ejection_percent: _Optional[int] = ..., recoverCondition: _Optional[_Union[RecoverCondition, _Mapping]] = ..., faultDetectConfig: _Optional[_Union[FaultDetectConfig, _Mapping]] = ..., fallbackConfig: _Optional[_Union[FallbackConfig, _Mapping]] = ...) -> None: ...

class DestinationSet(_message.Message):
    __slots__ = ["errorCodes", "metadata", "method", "metricPrecision", "metricWindow", "namespace", "policy", "recover", "resource", "scope", "service", "type", "updateInterval"]
    class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Scope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    ALL: DestinationSet.Scope
    CURRENT: DestinationSet.Scope
    ERRORCODES_FIELD_NUMBER: _ClassVar[int]
    GLOBAL: DestinationSet.Type
    INSTANCE: DestinationSet.Resource
    LOCAL: DestinationSet.Type
    METADATA_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    METRICPRECISION_FIELD_NUMBER: _ClassVar[int]
    METRICWINDOW_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    POLICY_FIELD_NUMBER: _ClassVar[int]
    RECOVER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SUBSET: DestinationSet.Resource
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATEINTERVAL_FIELD_NUMBER: _ClassVar[int]
    errorCodes: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    metadata: _containers.MessageMap[str, _model_pb2.MatchString]
    method: _model_pb2.MatchString
    metricPrecision: _wrappers_pb2.UInt32Value
    metricWindow: _duration_pb2.Duration
    namespace: _wrappers_pb2.StringValue
    policy: CbPolicy
    recover: RecoverConfig
    resource: DestinationSet.Resource
    scope: DestinationSet.Scope
    service: _wrappers_pb2.StringValue
    type: DestinationSet.Type
    updateInterval: _duration_pb2.Duration
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, _model_pb2.MatchString]] = ..., resource: _Optional[_Union[DestinationSet.Resource, str]] = ..., type: _Optional[_Union[DestinationSet.Type, str]] = ..., scope: _Optional[_Union[DestinationSet.Scope, str]] = ..., metricWindow: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., metricPrecision: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., updateInterval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., recover: _Optional[_Union[RecoverConfig, _Mapping]] = ..., policy: _Optional[_Union[CbPolicy, _Mapping]] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ..., errorCodes: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ...) -> None: ...

class ErrorCondition(_message.Message):
    __slots__ = ["condition", "input_type"]
    class InputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    DELAY: ErrorCondition.InputType
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RET_CODE: ErrorCondition.InputType
    UNKNOWN: ErrorCondition.InputType
    condition: _model_pb2.MatchString
    input_type: ErrorCondition.InputType
    def __init__(self, input_type: _Optional[_Union[ErrorCondition.InputType, str]] = ..., condition: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...

class FallbackConfig(_message.Message):
    __slots__ = ["enable", "response"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    response: FallbackResponse
    def __init__(self, enable: bool = ..., response: _Optional[_Union[FallbackResponse, _Mapping]] = ...) -> None: ...

class FallbackResponse(_message.Message):
    __slots__ = ["body", "code", "headers"]
    class MessageHeader(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    body: str
    code: int
    headers: _containers.RepeatedCompositeFieldContainer[FallbackResponse.MessageHeader]
    def __init__(self, code: _Optional[int] = ..., headers: _Optional[_Iterable[_Union[FallbackResponse.MessageHeader, _Mapping]]] = ..., body: _Optional[str] = ...) -> None: ...

class FaultDetectConfig(_message.Message):
    __slots__ = ["enable"]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    def __init__(self, enable: bool = ...) -> None: ...

class RecoverCondition(_message.Message):
    __slots__ = ["consecutiveSuccess", "sleep_window"]
    CONSECUTIVESUCCESS_FIELD_NUMBER: _ClassVar[int]
    SLEEP_WINDOW_FIELD_NUMBER: _ClassVar[int]
    consecutiveSuccess: int
    sleep_window: int
    def __init__(self, sleep_window: _Optional[int] = ..., consecutiveSuccess: _Optional[int] = ...) -> None: ...

class RecoverConfig(_message.Message):
    __slots__ = ["maxRetryAfterHalfOpen", "outlierDetectWhen", "requestCountAfterHalfOpen", "requestRateAfterHalfOpen", "sleepWindow", "successRateToClose"]
    class OutlierDetectWhen(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALWAYS: RecoverConfig.OutlierDetectWhen
    MAXRETRYAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    NEVER: RecoverConfig.OutlierDetectWhen
    ON_RECOVER: RecoverConfig.OutlierDetectWhen
    OUTLIERDETECTWHEN_FIELD_NUMBER: _ClassVar[int]
    REQUESTCOUNTAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    REQUESTRATEAFTERHALFOPEN_FIELD_NUMBER: _ClassVar[int]
    SLEEPWINDOW_FIELD_NUMBER: _ClassVar[int]
    SUCCESSRATETOCLOSE_FIELD_NUMBER: _ClassVar[int]
    maxRetryAfterHalfOpen: _wrappers_pb2.UInt32Value
    outlierDetectWhen: RecoverConfig.OutlierDetectWhen
    requestCountAfterHalfOpen: _wrappers_pb2.UInt32Value
    requestRateAfterHalfOpen: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    sleepWindow: _duration_pb2.Duration
    successRateToClose: _wrappers_pb2.UInt32Value
    def __init__(self, sleepWindow: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maxRetryAfterHalfOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., requestRateAfterHalfOpen: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ..., successRateToClose: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., requestCountAfterHalfOpen: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., outlierDetectWhen: _Optional[_Union[RecoverConfig.OutlierDetectWhen, str]] = ...) -> None: ...

class RuleMatcher(_message.Message):
    __slots__ = ["destination", "source"]
    class DestinationService(_message.Message):
        __slots__ = ["method", "namespace", "service"]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        method: _model_pb2.MatchString
        namespace: str
        service: str
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ..., method: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    class SourceService(_message.Message):
        __slots__ = ["namespace", "service"]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        namespace: str
        service: str
        def __init__(self, service: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    destination: RuleMatcher.DestinationService
    source: RuleMatcher.SourceService
    def __init__(self, source: _Optional[_Union[RuleMatcher.SourceService, _Mapping]] = ..., destination: _Optional[_Union[RuleMatcher.DestinationService, _Mapping]] = ...) -> None: ...

class SourceMatcher(_message.Message):
    __slots__ = ["labels", "namespace", "service"]
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.MatchString
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.MessageMap[str, _model_pb2.MatchString]
    namespace: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., labels: _Optional[_Mapping[str, _model_pb2.MatchString]] = ...) -> None: ...

class TriggerCondition(_message.Message):
    __slots__ = ["error_count", "error_percent", "interval", "minimum_request", "trigger_type"]
    class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONSECUTIVE_ERROR: TriggerCondition.TriggerType
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_PERCENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE: TriggerCondition.TriggerType
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: TriggerCondition.TriggerType
    error_count: int
    error_percent: int
    interval: int
    minimum_request: int
    trigger_type: TriggerCondition.TriggerType
    def __init__(self, trigger_type: _Optional[_Union[TriggerCondition.TriggerType, str]] = ..., error_count: _Optional[int] = ..., error_percent: _Optional[int] = ..., interval: _Optional[int] = ..., minimum_request: _Optional[int] = ...) -> None: ...

class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
