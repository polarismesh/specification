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
from ..service_manage import contract_pb2 as _contract_pb2
from ..traffic_manage import lane_pb2 as _lane_pb2
from ..traffic_manage import lossless_pb2 as _lossless_pb2
from ..security import block_allow_list_pb2 as _block_allow_list_pb2
from ..traffic_manage import traffic_mirroring_pb2 as _traffic_mirroring_pb2
from ..traffic_manage import fault_injection_pb2 as _fault_injection_pb2
from ..service_manage import request_pb2 as _request_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("code", "info", "client", "namespace", "service", "instance", "routing", "alias", "rateLimit", "circuitBreaker", "configRelease", "user", "userGroup", "authStrategy", "relation", "loginResponse", "modifyAuthStrategy", "modifyUserGroup", "resources", "optionSwitch", "instanceLabels", "data", "serviceContract", "clientEvent")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ROUTING_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    RATELIMIT_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    CONFIGRELEASE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    USERGROUP_FIELD_NUMBER: _ClassVar[int]
    AUTHSTRATEGY_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    LOGINRESPONSE_FIELD_NUMBER: _ClassVar[int]
    MODIFYAUTHSTRATEGY_FIELD_NUMBER: _ClassVar[int]
    MODIFYUSERGROUP_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    OPTIONSWITCH_FIELD_NUMBER: _ClassVar[int]
    INSTANCELABELS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SERVICECONTRACT_FIELD_NUMBER: _ClassVar[int]
    CLIENTEVENT_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    client: _client_pb2.Client
    namespace: _namespace_pb2.Namespace
    service: _service_pb2.Service
    instance: _service_pb2.Instance
    routing: _routing_pb2.Routing
    alias: _service_pb2.ServiceAlias
    rateLimit: _ratelimit_pb2.Rule
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    configRelease: _configrelease_pb2.ConfigRelease
    user: _auth_pb2.User
    userGroup: _auth_pb2.UserGroup
    authStrategy: _auth_pb2.AuthStrategy
    relation: _auth_pb2.UserGroupRelation
    loginResponse: _auth_pb2.LoginResponse
    modifyAuthStrategy: _auth_pb2.ModifyAuthStrategy
    modifyUserGroup: _auth_pb2.ModifyUserGroup
    resources: _auth_pb2.StrategyResources
    optionSwitch: OptionSwitch
    instanceLabels: InstanceLabels
    data: _any_pb2.Any
    serviceContract: _contract_pb2.ServiceContract
    clientEvent: _client_pb2.ClientEvent
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ..., namespace: _Optional[_Union[_namespace_pb2.Namespace, _Mapping]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., instance: _Optional[_Union[_service_pb2.Instance, _Mapping]] = ..., routing: _Optional[_Union[_routing_pb2.Routing, _Mapping]] = ..., alias: _Optional[_Union[_service_pb2.ServiceAlias, _Mapping]] = ..., rateLimit: _Optional[_Union[_ratelimit_pb2.Rule, _Mapping]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ..., configRelease: _Optional[_Union[_configrelease_pb2.ConfigRelease, _Mapping]] = ..., user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., userGroup: _Optional[_Union[_auth_pb2.UserGroup, _Mapping]] = ..., authStrategy: _Optional[_Union[_auth_pb2.AuthStrategy, _Mapping]] = ..., relation: _Optional[_Union[_auth_pb2.UserGroupRelation, _Mapping]] = ..., loginResponse: _Optional[_Union[_auth_pb2.LoginResponse, _Mapping]] = ..., modifyAuthStrategy: _Optional[_Union[_auth_pb2.ModifyAuthStrategy, _Mapping]] = ..., modifyUserGroup: _Optional[_Union[_auth_pb2.ModifyUserGroup, _Mapping]] = ..., resources: _Optional[_Union[_auth_pb2.StrategyResources, _Mapping]] = ..., optionSwitch: _Optional[_Union[OptionSwitch, _Mapping]] = ..., instanceLabels: _Optional[_Union[InstanceLabels, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., serviceContract: _Optional[_Union[_contract_pb2.ServiceContract, _Mapping]] = ..., clientEvent: _Optional[_Union[_client_pb2.ClientEvent, _Mapping]] = ...) -> None: ...

class BatchWriteResponse(_message.Message):
    __slots__ = ("code", "info", "size", "responses")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    size: _wrappers_pb2.UInt32Value
    responses: _containers.RepeatedCompositeFieldContainer[Response]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., size: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., responses: _Optional[_Iterable[_Union[Response, _Mapping]]] = ...) -> None: ...

class BatchQueryResponse(_message.Message):
    __slots__ = ("code", "info", "amount", "size", "namespaces", "services", "instances", "routings", "aliases", "rateLimits", "configWithServices", "users", "userGroups", "authStrategies", "clients", "data", "summary", "instanceSummary")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ROUTINGS_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    RATELIMITS_FIELD_NUMBER: _ClassVar[int]
    CONFIGWITHSERVICES_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    USERGROUPS_FIELD_NUMBER: _ClassVar[int]
    AUTHSTRATEGIES_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INSTANCESUMMARY_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    amount: _wrappers_pb2.UInt32Value
    size: _wrappers_pb2.UInt32Value
    namespaces: _containers.RepeatedCompositeFieldContainer[_namespace_pb2.Namespace]
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.Instance]
    routings: _containers.RepeatedCompositeFieldContainer[_routing_pb2.Routing]
    aliases: _containers.RepeatedCompositeFieldContainer[_service_pb2.ServiceAlias]
    rateLimits: _containers.RepeatedCompositeFieldContainer[_ratelimit_pb2.Rule]
    configWithServices: _containers.RepeatedCompositeFieldContainer[_configrelease_pb2.ConfigWithService]
    users: _containers.RepeatedCompositeFieldContainer[_auth_pb2.User]
    userGroups: _containers.RepeatedCompositeFieldContainer[_auth_pb2.UserGroup]
    authStrategies: _containers.RepeatedCompositeFieldContainer[_auth_pb2.AuthStrategy]
    clients: _containers.RepeatedCompositeFieldContainer[_client_pb2.Client]
    data: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    summary: _model_pb2.Summary
    instanceSummary: _containers.RepeatedCompositeFieldContainer[InstanceSummary]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., amount: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., size: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., namespaces: _Optional[_Iterable[_Union[_namespace_pb2.Namespace, _Mapping]]] = ..., services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ..., instances: _Optional[_Iterable[_Union[_service_pb2.Instance, _Mapping]]] = ..., routings: _Optional[_Iterable[_Union[_routing_pb2.Routing, _Mapping]]] = ..., aliases: _Optional[_Iterable[_Union[_service_pb2.ServiceAlias, _Mapping]]] = ..., rateLimits: _Optional[_Iterable[_Union[_ratelimit_pb2.Rule, _Mapping]]] = ..., configWithServices: _Optional[_Iterable[_Union[_configrelease_pb2.ConfigWithService, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_auth_pb2.User, _Mapping]]] = ..., userGroups: _Optional[_Iterable[_Union[_auth_pb2.UserGroup, _Mapping]]] = ..., authStrategies: _Optional[_Iterable[_Union[_auth_pb2.AuthStrategy, _Mapping]]] = ..., clients: _Optional[_Iterable[_Union[_client_pb2.Client, _Mapping]]] = ..., data: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ..., summary: _Optional[_Union[_model_pb2.Summary, _Mapping]] = ..., instanceSummary: _Optional[_Iterable[_Union[InstanceSummary, _Mapping]]] = ...) -> None: ...

class InstanceSummary(_message.Message):
    __slots__ = ("Namespace", "ServiceName", "metadata", "summary")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICENAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    Namespace: str
    ServiceName: str
    metadata: _containers.ScalarMap[str, str]
    summary: _model_pb2.Summary
    def __init__(self, Namespace: _Optional[str] = ..., ServiceName: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., summary: _Optional[_Union[_model_pb2.Summary, _Mapping]] = ...) -> None: ...

class DiscoverResponse(_message.Message):
    __slots__ = ("code", "info", "type", "service", "instances", "routing", "rateLimit", "circuitBreaker", "services", "namespaces", "faultDetector", "aliasFor", "lanes", "customRouteRules", "nearbyRouteRules", "lossless", "blockAllowListRule", "trafficMirroring", "faultInjection", "Direction", "losslessRuleList")
    class DiscoverResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DiscoverResponse.DiscoverResponseType]
        INSTANCE: _ClassVar[DiscoverResponse.DiscoverResponseType]
        CLUSTER: _ClassVar[DiscoverResponse.DiscoverResponseType]
        ROUTING: _ClassVar[DiscoverResponse.DiscoverResponseType]
        RATE_LIMIT: _ClassVar[DiscoverResponse.DiscoverResponseType]
        CIRCUIT_BREAKER: _ClassVar[DiscoverResponse.DiscoverResponseType]
        SERVICES: _ClassVar[DiscoverResponse.DiscoverResponseType]
        NAMESPACES: _ClassVar[DiscoverResponse.DiscoverResponseType]
        FAULT_DETECTOR: _ClassVar[DiscoverResponse.DiscoverResponseType]
        LANE: _ClassVar[DiscoverResponse.DiscoverResponseType]
        CUSTOM_ROUTE_RULE: _ClassVar[DiscoverResponse.DiscoverResponseType]
        NEARBY_ROUTE_RULE: _ClassVar[DiscoverResponse.DiscoverResponseType]
        LOSSLESS: _ClassVar[DiscoverResponse.DiscoverResponseType]
        BLOCK_ALLOW_RULE: _ClassVar[DiscoverResponse.DiscoverResponseType]
        TRAFFIC_MIRRORING: _ClassVar[DiscoverResponse.DiscoverResponseType]
        FAULT_INJECTION: _ClassVar[DiscoverResponse.DiscoverResponseType]
    UNKNOWN: DiscoverResponse.DiscoverResponseType
    INSTANCE: DiscoverResponse.DiscoverResponseType
    CLUSTER: DiscoverResponse.DiscoverResponseType
    ROUTING: DiscoverResponse.DiscoverResponseType
    RATE_LIMIT: DiscoverResponse.DiscoverResponseType
    CIRCUIT_BREAKER: DiscoverResponse.DiscoverResponseType
    SERVICES: DiscoverResponse.DiscoverResponseType
    NAMESPACES: DiscoverResponse.DiscoverResponseType
    FAULT_DETECTOR: DiscoverResponse.DiscoverResponseType
    LANE: DiscoverResponse.DiscoverResponseType
    CUSTOM_ROUTE_RULE: DiscoverResponse.DiscoverResponseType
    NEARBY_ROUTE_RULE: DiscoverResponse.DiscoverResponseType
    LOSSLESS: DiscoverResponse.DiscoverResponseType
    BLOCK_ALLOW_RULE: DiscoverResponse.DiscoverResponseType
    TRAFFIC_MIRRORING: DiscoverResponse.DiscoverResponseType
    FAULT_INJECTION: DiscoverResponse.DiscoverResponseType
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    ROUTING_FIELD_NUMBER: _ClassVar[int]
    RATELIMIT_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    FAULTDETECTOR_FIELD_NUMBER: _ClassVar[int]
    ALIASFOR_FIELD_NUMBER: _ClassVar[int]
    LANES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMROUTERULES_FIELD_NUMBER: _ClassVar[int]
    NEARBYROUTERULES_FIELD_NUMBER: _ClassVar[int]
    LOSSLESS_FIELD_NUMBER: _ClassVar[int]
    BLOCKALLOWLISTRULE_FIELD_NUMBER: _ClassVar[int]
    TRAFFICMIRRORING_FIELD_NUMBER: _ClassVar[int]
    FAULTINJECTION_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LOSSLESSRULELIST_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    type: DiscoverResponse.DiscoverResponseType
    service: _service_pb2.Service
    instances: _containers.RepeatedCompositeFieldContainer[_service_pb2.Instance]
    routing: _routing_pb2.Routing
    rateLimit: _ratelimit_pb2.RateLimit
    circuitBreaker: _circuitbreaker_pb2.CircuitBreaker
    services: _containers.RepeatedCompositeFieldContainer[_service_pb2.Service]
    namespaces: _containers.RepeatedCompositeFieldContainer[_namespace_pb2.Namespace]
    faultDetector: _fault_detector_pb2.FaultDetector
    aliasFor: _service_pb2.Service
    lanes: _containers.RepeatedCompositeFieldContainer[_lane_pb2.LaneGroup]
    customRouteRules: _containers.RepeatedCompositeFieldContainer[_routing_pb2.RouteRule]
    nearbyRouteRules: _containers.RepeatedCompositeFieldContainer[_routing_pb2.RouteRule]
    lossless: _lossless_pb2.LosslessRule
    blockAllowListRule: _containers.RepeatedCompositeFieldContainer[_block_allow_list_pb2.BlockAllowListRule]
    trafficMirroring: _containers.RepeatedCompositeFieldContainer[_traffic_mirroring_pb2.TrafficMirroring]
    faultInjection: _containers.RepeatedCompositeFieldContainer[_fault_injection_pb2.FaultInjection]
    Direction: _request_pb2.DiscoverDirection
    losslessRuleList: _containers.RepeatedCompositeFieldContainer[_lossless_pb2.LosslessRule]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[DiscoverResponse.DiscoverResponseType, str]] = ..., service: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., instances: _Optional[_Iterable[_Union[_service_pb2.Instance, _Mapping]]] = ..., routing: _Optional[_Union[_routing_pb2.Routing, _Mapping]] = ..., rateLimit: _Optional[_Union[_ratelimit_pb2.RateLimit, _Mapping]] = ..., circuitBreaker: _Optional[_Union[_circuitbreaker_pb2.CircuitBreaker, _Mapping]] = ..., services: _Optional[_Iterable[_Union[_service_pb2.Service, _Mapping]]] = ..., namespaces: _Optional[_Iterable[_Union[_namespace_pb2.Namespace, _Mapping]]] = ..., faultDetector: _Optional[_Union[_fault_detector_pb2.FaultDetector, _Mapping]] = ..., aliasFor: _Optional[_Union[_service_pb2.Service, _Mapping]] = ..., lanes: _Optional[_Iterable[_Union[_lane_pb2.LaneGroup, _Mapping]]] = ..., customRouteRules: _Optional[_Iterable[_Union[_routing_pb2.RouteRule, _Mapping]]] = ..., nearbyRouteRules: _Optional[_Iterable[_Union[_routing_pb2.RouteRule, _Mapping]]] = ..., lossless: _Optional[_Union[_lossless_pb2.LosslessRule, _Mapping]] = ..., blockAllowListRule: _Optional[_Iterable[_Union[_block_allow_list_pb2.BlockAllowListRule, _Mapping]]] = ..., trafficMirroring: _Optional[_Iterable[_Union[_traffic_mirroring_pb2.TrafficMirroring, _Mapping]]] = ..., faultInjection: _Optional[_Iterable[_Union[_fault_injection_pb2.FaultInjection, _Mapping]]] = ..., Direction: _Optional[_Union[_request_pb2.DiscoverDirection, str]] = ..., losslessRuleList: _Optional[_Iterable[_Union[_lossless_pb2.LosslessRule, _Mapping]]] = ...) -> None: ...

class OptionSwitch(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.ScalarMap[str, str]
    def __init__(self, options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class InstanceLabels(_message.Message):
    __slots__ = ("labels", "namespace", "service", "service_id")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _model_pb2.StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.StringList, _Mapping]] = ...) -> None: ...
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.MessageMap[str, _model_pb2.StringList]
    namespace: str
    service: str
    service_id: str
    def __init__(self, labels: _Optional[_Mapping[str, _model_pb2.StringList]] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...
