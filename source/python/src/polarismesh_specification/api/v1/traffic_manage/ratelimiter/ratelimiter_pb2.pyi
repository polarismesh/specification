from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RateLimitCmd(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INIT: _ClassVar[RateLimitCmd]
    ACQUIRE: _ClassVar[RateLimitCmd]
    BATCH_INIT: _ClassVar[RateLimitCmd]
    BATCH_ACQUIRE: _ClassVar[RateLimitCmd]

class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADAPTIVE: _ClassVar[Mode]
    BATCH_OCCUPY: _ClassVar[Mode]
    BATCH_SHARE: _ClassVar[Mode]

class QuotaMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WHOLE: _ClassVar[QuotaMode]
    DIVIDE: _ClassVar[QuotaMode]
INIT: RateLimitCmd
ACQUIRE: RateLimitCmd
BATCH_INIT: RateLimitCmd
BATCH_ACQUIRE: RateLimitCmd
ADAPTIVE: Mode
BATCH_OCCUPY: Mode
BATCH_SHARE: Mode
WHOLE: QuotaMode
DIVIDE: QuotaMode

class RateLimitRequest(_message.Message):
    __slots__ = ("cmd", "rateLimitInitRequest", "rateLimitReportRequest", "rateLimitBatchInitRequest")
    CMD_FIELD_NUMBER: _ClassVar[int]
    RATELIMITINITREQUEST_FIELD_NUMBER: _ClassVar[int]
    RATELIMITREPORTREQUEST_FIELD_NUMBER: _ClassVar[int]
    RATELIMITBATCHINITREQUEST_FIELD_NUMBER: _ClassVar[int]
    cmd: RateLimitCmd
    rateLimitInitRequest: RateLimitInitRequest
    rateLimitReportRequest: RateLimitReportRequest
    rateLimitBatchInitRequest: RateLimitBatchInitRequest
    def __init__(self, cmd: _Optional[_Union[RateLimitCmd, str]] = ..., rateLimitInitRequest: _Optional[_Union[RateLimitInitRequest, _Mapping]] = ..., rateLimitReportRequest: _Optional[_Union[RateLimitReportRequest, _Mapping]] = ..., rateLimitBatchInitRequest: _Optional[_Union[RateLimitBatchInitRequest, _Mapping]] = ...) -> None: ...

class RateLimitResponse(_message.Message):
    __slots__ = ("cmd", "rateLimitInitResponse", "rateLimitReportResponse", "rateLimitBatchInitResponse")
    CMD_FIELD_NUMBER: _ClassVar[int]
    RATELIMITINITRESPONSE_FIELD_NUMBER: _ClassVar[int]
    RATELIMITREPORTRESPONSE_FIELD_NUMBER: _ClassVar[int]
    RATELIMITBATCHINITRESPONSE_FIELD_NUMBER: _ClassVar[int]
    cmd: RateLimitCmd
    rateLimitInitResponse: RateLimitInitResponse
    rateLimitReportResponse: RateLimitReportResponse
    rateLimitBatchInitResponse: RateLimitBatchInitResponse
    def __init__(self, cmd: _Optional[_Union[RateLimitCmd, str]] = ..., rateLimitInitResponse: _Optional[_Union[RateLimitInitResponse, _Mapping]] = ..., rateLimitReportResponse: _Optional[_Union[RateLimitReportResponse, _Mapping]] = ..., rateLimitBatchInitResponse: _Optional[_Union[RateLimitBatchInitResponse, _Mapping]] = ...) -> None: ...

class RateLimitInitRequest(_message.Message):
    __slots__ = ("target", "clientId", "totals", "slideCount", "mode")
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    TOTALS_FIELD_NUMBER: _ClassVar[int]
    SLIDECOUNT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    target: LimitTarget
    clientId: str
    totals: _containers.RepeatedCompositeFieldContainer[QuotaTotal]
    slideCount: int
    mode: Mode
    def __init__(self, target: _Optional[_Union[LimitTarget, _Mapping]] = ..., clientId: _Optional[str] = ..., totals: _Optional[_Iterable[_Union[QuotaTotal, _Mapping]]] = ..., slideCount: _Optional[int] = ..., mode: _Optional[_Union[Mode, str]] = ...) -> None: ...

class RateLimitInitResponse(_message.Message):
    __slots__ = ("code", "target", "clientKey", "counters", "slideCount", "timestamp")
    CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CLIENTKEY_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    SLIDECOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    code: int
    target: LimitTarget
    clientKey: int
    counters: _containers.RepeatedCompositeFieldContainer[QuotaCounter]
    slideCount: int
    timestamp: int
    def __init__(self, code: _Optional[int] = ..., target: _Optional[_Union[LimitTarget, _Mapping]] = ..., clientKey: _Optional[int] = ..., counters: _Optional[_Iterable[_Union[QuotaCounter, _Mapping]]] = ..., slideCount: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class RateLimitBatchInitRequest(_message.Message):
    __slots__ = ("request", "clientId")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    request: _containers.RepeatedCompositeFieldContainer[RateLimitInitRequest]
    clientId: str
    def __init__(self, request: _Optional[_Iterable[_Union[RateLimitInitRequest, _Mapping]]] = ..., clientId: _Optional[str] = ...) -> None: ...

class LabeledQuotaCounter(_message.Message):
    __slots__ = ("labels", "counters")
    LABELS_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    labels: str
    counters: _containers.RepeatedCompositeFieldContainer[QuotaCounter]
    def __init__(self, labels: _Optional[str] = ..., counters: _Optional[_Iterable[_Union[QuotaCounter, _Mapping]]] = ...) -> None: ...

class BatchInitResult(_message.Message):
    __slots__ = ("code", "target", "counters", "slideCount")
    CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    SLIDECOUNT_FIELD_NUMBER: _ClassVar[int]
    code: int
    target: LimitTarget
    counters: _containers.RepeatedCompositeFieldContainer[LabeledQuotaCounter]
    slideCount: int
    def __init__(self, code: _Optional[int] = ..., target: _Optional[_Union[LimitTarget, _Mapping]] = ..., counters: _Optional[_Iterable[_Union[LabeledQuotaCounter, _Mapping]]] = ..., slideCount: _Optional[int] = ...) -> None: ...

class RateLimitBatchInitResponse(_message.Message):
    __slots__ = ("code", "clientKey", "timestamp", "result")
    CODE_FIELD_NUMBER: _ClassVar[int]
    CLIENTKEY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    code: int
    clientKey: int
    timestamp: int
    result: _containers.RepeatedCompositeFieldContainer[BatchInitResult]
    def __init__(self, code: _Optional[int] = ..., clientKey: _Optional[int] = ..., timestamp: _Optional[int] = ..., result: _Optional[_Iterable[_Union[BatchInitResult, _Mapping]]] = ...) -> None: ...

class RateLimitReportRequest(_message.Message):
    __slots__ = ("clientKey", "quotaUses", "timestamp")
    CLIENTKEY_FIELD_NUMBER: _ClassVar[int]
    QUOTAUSES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    clientKey: int
    quotaUses: _containers.RepeatedCompositeFieldContainer[QuotaSum]
    timestamp: int
    def __init__(self, clientKey: _Optional[int] = ..., quotaUses: _Optional[_Iterable[_Union[QuotaSum, _Mapping]]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class RateLimitReportResponse(_message.Message):
    __slots__ = ("code", "quotaLefts", "timestamp")
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUOTALEFTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    code: int
    quotaLefts: _containers.RepeatedCompositeFieldContainer[QuotaLeft]
    timestamp: int
    def __init__(self, code: _Optional[int] = ..., quotaLefts: _Optional[_Iterable[_Union[QuotaLeft, _Mapping]]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class LimitTarget(_message.Message):
    __slots__ = ("namespace", "service", "labels", "labels_list")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABELS_LIST_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    service: str
    labels: str
    labels_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace: _Optional[str] = ..., service: _Optional[str] = ..., labels: _Optional[str] = ..., labels_list: _Optional[_Iterable[str]] = ...) -> None: ...

class QuotaTotal(_message.Message):
    __slots__ = ("mode", "duration", "maxAmount")
    MODE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    MAXAMOUNT_FIELD_NUMBER: _ClassVar[int]
    mode: QuotaMode
    duration: int
    maxAmount: int
    def __init__(self, mode: _Optional[_Union[QuotaMode, str]] = ..., duration: _Optional[int] = ..., maxAmount: _Optional[int] = ...) -> None: ...

class QuotaCounter(_message.Message):
    __slots__ = ("duration", "counterKey", "left", "mode", "clientCount")
    DURATION_FIELD_NUMBER: _ClassVar[int]
    COUNTERKEY_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CLIENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    duration: int
    counterKey: int
    left: int
    mode: Mode
    clientCount: int
    def __init__(self, duration: _Optional[int] = ..., counterKey: _Optional[int] = ..., left: _Optional[int] = ..., mode: _Optional[_Union[Mode, str]] = ..., clientCount: _Optional[int] = ...) -> None: ...

class QuotaSum(_message.Message):
    __slots__ = ("counterKey", "used", "limited")
    COUNTERKEY_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    LIMITED_FIELD_NUMBER: _ClassVar[int]
    counterKey: int
    used: int
    limited: int
    def __init__(self, counterKey: _Optional[int] = ..., used: _Optional[int] = ..., limited: _Optional[int] = ...) -> None: ...

class QuotaLeft(_message.Message):
    __slots__ = ("counterKey", "left", "mode", "clientCount")
    COUNTERKEY_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CLIENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    counterKey: int
    left: int
    mode: Mode
    clientCount: int
    def __init__(self, counterKey: _Optional[int] = ..., left: _Optional[int] = ..., mode: _Optional[_Union[Mode, str]] = ..., clientCount: _Optional[int] = ...) -> None: ...

class TimeAdjustRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TimeAdjustResponse(_message.Message):
    __slots__ = ("serverTimestamp",)
    SERVERTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    serverTimestamp: int
    def __init__(self, serverTimestamp: _Optional[int] = ...) -> None: ...
