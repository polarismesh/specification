from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import any_pb2 as _any_pb2
from ..model import namespace_pb2 as _namespace_pb2
from ..service_manage import service_pb2 as _service_pb2
from ..traffic_manage import routing_pb2 as _routing_pb2
from ..traffic_manage import ratelimit_pb2 as _ratelimit_pb2
from ..fault_tolerance import circuitbreaker_pb2 as _circuitbreaker_pb2
from ..model import model_pb2 as _model_pb2
from ..service_manage import client_pb2 as _client_pb2
from ..service_manage import configrelease_pb2 as _configrelease_pb2
from ..fault_tolerance import fault_detector_pb2 as _fault_detector_pb2
from ..security import auth_pb2 as _auth_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BatchQueryResponse(_message.Message):
    __slots__ = ["aliases", "amount", "authStrategies", "clients", "code", "configWithServices", "data", "info", "instances", "namespaces", "rateLimits", "routings", "services", "size", "userGroups", "users"]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHSTRATEGIES_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGWITHSERVICES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    RATELIMITS_FIELD_NUMBER: _ClassVar[int]
    ROUTINGS_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    USERGROUPS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    aliases: _containers.RepeatedCompositeFieldContainer[_service_pb2.ServiceAlias]
    amount: _wrappers_pb2.UInt32Value
    authStrategies: _containers.RepeatedCompositeFieldContainer[_auth_pb2.AuthStrategy]
    clients: _containers.RepeatedCompositeFieldContainer[_client_pb2.Client]
    code: _wrappers_pb2.UInt32Value
    configWithServices: _containers.RepeatedCompositeFieldContainer[_configrelease_pb2.ConfigWithService]
    data: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    info: _wrappers_pb2.StringValue
    instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.Instance]
    namespaces: _containers.RepeatedCompositeFieldContainer[_namespace_pb2.Namespace]
    rateLimits: _containers.RepeatedCompositeFieldContainer[_ratelimit_pb2.Rule]
    routings: _containers.RepeatedCompositeFieldContainer[_routing_pb2.Routing]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    size: _wrappers_pb2.UInt32Value
    userGroups: _containers.RepeatedCompositeFieldContainer[_auth_pb2.UserGroup]
    users: _containers.RepeatedCompositeFieldContainer[_auth_pb2.User]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., amount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., size: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., namespaces: _Optional[_Iterable[_Union[_namespace_pb2.Namespace, _Mapping]]] = ..., services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ..., instances: _Optional[_Iterable[_Union[_service_pb2.Instance, _Mapping]]] = ..., routings: _Optional[_Iterable[_Union[_routing_pb2.Routing, _Mapping]]] = ..., aliases: _Optional[_Iterable[_Union[_service_pb2.ServiceAlias, _Mapping]]] = ..., rateLimits: _Optional[_Iterable[_Union[_ratelimit_pb2.Rule, _Mapping]]] = ..., configWithServices: _Optional[_Iterable[_Union[_configrelease_pb2.ConfigWithService, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_auth_pb2.User, _Mapping]]] = ..., userGroups: _Optional[_Iterable[_Union[_auth_pb2.UserGroup, _Mapping]]] = ..., authStrategies: _Optional[_Iterable[_Union[_auth_pb2.AuthStrategy, _Mapping]]] = ..., clients: _Optional[_Iterable[_Union[_client_pb2.Client, _Mapping]]] = ..., data: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class BatchWriteResponse(_message.Message):
    __slots__ = ["code", "info", "responses", "size"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    responses: _containers.RepeatedCompositeFieldContainer[Response]
    size: _wrappers_pb2.UInt32Value
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., size: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., responses: _Optional[_Iterable[_Union[Response, _Mapping]]] = ...) -> None: ...

class DiscoverResponse(_message.Message):
    __slots__ = ["circuitBreaker", "code", "faultDetector", "info", "instances", "namespaces", "rateLimit", "routing", "service", "services", "type"]
    class DiscoverResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_BREAKER: DiscoverResponse.DiscoverResponseType
    CLUSTER: DiscoverResponse.DiscoverResponseType
    CODE_FIELD_NUMBER: _ClassVar[int]
    FAULTDETECTOR_FIELD_NUMBER: _ClassVar[int]
    FAULT_DETECTOR: DiscoverResponse.DiscoverResponseType
    INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCE: DiscoverResponse.DiscoverResponseType
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES: DiscoverResponse.DiscoverResponseType
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    RATELIMIT_FIELD_NUMBER: _ClassVar[int]
    RATE_LIMIT: DiscoverResponse.DiscoverResponseType
    ROUTING: DiscoverResponse.DiscoverResponseType
    ROUTING_FIELD_NUMBER: _ClassVar[int]
    SERVICES: DiscoverResponse.DiscoverResponseType
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: DiscoverResponse.DiscoverResponseType
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    code: _wrappers_pb2.UInt32Value
    faultDetector: _fault_detector_pb2.FaultDetector
    info: _wrappers_pb2.StringValue
    instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.Instance]
    namespaces: _containers.RepeatedCompositeFieldContainer[_namespace_pb2.Namespace]
    rateLimit: _ratelimit_pb2.RateLimit
    routing: _routing_pb2.Routing
    service: _service_pb2.Service
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    type: DiscoverResponse.DiscoverResponseType
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[DiscoverResponse.DiscoverResponseType, str]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[_service_pb2.Instance, _Mapping]]] = ..., routing: _Optional[_Union[_routing_pb2.Routing, _Mapping]] = ..., rateLimit: _Optional[_Union[_ratelimit_pb2.RateLimit, _Mapping]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ..., services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ..., namespaces: _Optional[_Iterable[_Union[_namespace_pb2.Namespace, _Mapping]]] = ..., faultDetector: _Optional[_Union[_fault_detector_pb2.FaultDetector, _Mapping]] = ...) -> None: ...

class InstanceLabels(_message.Message):
    __slots__ = ["labels"]
    class LabelsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.StringList, _Mapping]] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.MessageMap[str, _model_pb2.StringList]
    def __init__(self, labels: _Optional[_Mapping[str, _model_pb2.StringList]] = ...) -> None: ...

class OptionSwitch(_message.Message):
    __slots__ = ["options"]
    class OptionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.ScalarMap[str, str]
    def __init__(self, options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["alias", "authStrategy", "circuitBreaker", "client", "code", "configRelease", "data", "info", "instance", "instanceLabels", "loginResponse", "modifyAuthStrategy", "modifyUserGroup", "namespace", "optionSwitch", "rateLimit", "relation", "resources", "routing", "service", "user", "userGroup"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    AUTHSTRATEGY_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGRELEASE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    INSTANCELABELS_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    LOGINRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MODIFYAUTHSTRATEGY_FIELD_NUMBER: _ClassVar[int]
    MODIFYUSERGROUP_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OPTIONSWITCH_FIELD_NUMBER: _ClassVar[int]
    RATELIMIT_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    USERGROUP_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    alias: _service_pb2.ServiceAlias
    authStrategy: _auth_pb2.AuthStrategy
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    client: _client_pb2.Client
    code: _wrappers_pb2.UInt32Value
    configRelease: _configrelease_pb2.ConfigRelease
    data: _any_pb2.Any
    info: _wrappers_pb2.StringValue
    instance: _service_pb2.Instance
    instanceLabels: InstanceLabels
    loginResponse: _auth_pb2.LoginResponse
    modifyAuthStrategy: _auth_pb2.ModifyAuthStrategy
    modifyUserGroup: _auth_pb2.ModifyUserGroup
    namespace: _namespace_pb2.Namespace
    optionSwitch: OptionSwitch
    rateLimit: _ratelimit_pb2.Rule
    relation: _auth_pb2.UserGroupRelation
    resources: _auth_pb2.StrategyResources
    routing: _routing_pb2.Routing
    service: _service_pb2.Service
    user: _auth_pb2.User
    userGroup: _auth_pb2.UserGroup
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ..., namespace: _Optional[_Union[_namespace_pb2.Namespace, _Mapping]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., instance: _Optional[_Union[_service_pb2.Instance, _Mapping]] = ..., routing: _Optional[_Union[_routing_pb2.Routing, _Mapping]] = ..., alias: _Optional[_Union[_service_pb2.ServiceAlias, _Mapping]] = ..., rateLimit: _Optional[_Union[_ratelimit_pb2.Rule, _Mapping]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ..., configRelease: _Optional[_Union[_configrelease_pb2.ConfigRelease, _Mapping]] = ..., user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., userGroup: _Optional[_Union[_auth_pb2.UserGroup, _Mapping]] = ..., authStrategy: _Optional[_Union[_auth_pb2.AuthStrategy, _Mapping]] = ..., relation: _Optional[_Union[_auth_pb2.UserGroupRelation, _Mapping]] = ..., loginResponse: _Optional[_Union[_auth_pb2.LoginResponse, _Mapping]] = ..., modifyAuthStrategy: _Optional[_Union[_auth_pb2.ModifyAuthStrategy, _Mapping]] = ..., modifyUserGroup: _Optional[_Union[_auth_pb2.ModifyUserGroup, _Mapping]] = ..., resources: _Optional[_Union[_auth_pb2.StrategyResources, _Mapping]] = ..., optionSwitch: _Optional[_Union[OptionSwitch, _Mapping]] = ..., instanceLabels: _Optional[_Union[InstanceLabels, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
