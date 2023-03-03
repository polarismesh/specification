from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CL5SID: AliasType
DEFAULT: AliasType
DESCRIPTOR: _descriptor.FileDescriptor

class HealthCheck(_message.Message):
    __slots__ = ["heartbeat", "type"]
    class HealthCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    HEARTBEAT: HealthCheck.HealthCheckType
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: HealthCheck.HealthCheckType
    heartbeat: HeartbeatHealthCheck
    type: HealthCheck.HealthCheckType
    def __init__(self, type: _Optional[_Union[HealthCheck.HealthCheckType, str]] = ..., heartbeat: _Optional[_Union[HeartbeatHealthCheck, _Mapping]] = ...) -> None: ...

class HeartbeatHealthCheck(_message.Message):
    __slots__ = ["ttl"]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ttl: _wrappers_pb2.UInt32Value
    def __init__(self, ttl: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class Instance(_message.Message):
    __slots__ = ["ctime", "enable_health_check", "health_check", "healthy", "host", "id", "isolate", "location", "logic_set", "metadata", "mtime", "namespace", "port", "priority", "protocol", "revision", "service", "service_token", "version", "vpc_id", "weight"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CTIME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOGIC_SET_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ctime: _wrappers_pb2.StringValue
    enable_health_check: _wrappers_pb2.BoolValue
    health_check: HealthCheck
    healthy: _wrappers_pb2.BoolValue
    host: _wrappers_pb2.StringValue
    id: _wrappers_pb2.StringValue
    isolate: _wrappers_pb2.BoolValue
    location: _model_pb2.Location
    logic_set: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    mtime: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    port: _wrappers_pb2.UInt32Value
    priority: _wrappers_pb2.UInt32Value
    protocol: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    version: _wrappers_pb2.StringValue
    vpc_id: _wrappers_pb2.StringValue
    weight: _wrappers_pb2.UInt32Value
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., vpc_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., host: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., protocol: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., weight: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., enable_health_check: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., health_check: _Optional[_Union[HealthCheck, _Mapping]] = ..., healthy: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., isolate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., location: _Optional[_Union[_model_pb2.Location, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., logic_set: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ["business", "cmdb_mod1", "cmdb_mod2", "cmdb_mod3", "comment", "ctime", "department", "editable", "group_ids", "healthy_instance_count", "id", "metadata", "mtime", "name", "namespace", "owners", "platform_id", "ports", "remove_group_ids", "remove_user_ids", "revision", "token", "total_instance_count", "user_ids"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD1_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD2_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD3_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    business: _wrappers_pb2.StringValue
    cmdb_mod1: _wrappers_pb2.StringValue
    cmdb_mod2: _wrappers_pb2.StringValue
    cmdb_mod3: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    department: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    healthy_instance_count: _wrappers_pb2.UInt32Value
    id: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    mtime: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    platform_id: _wrappers_pb2.StringValue
    ports: _wrappers_pb2.StringValue
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    revision: _wrappers_pb2.StringValue
    token: _wrappers_pb2.StringValue
    total_instance_count: _wrappers_pb2.UInt32Value
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., ports: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., business: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., department: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod1: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod2: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod3: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., platform_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., healthy_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ServiceAlias(_message.Message):
    __slots__ = ["alias", "alias_namespace", "comment", "ctime", "editable", "id", "mtime", "namespace", "owners", "service", "service_token", "type"]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    alias: _wrappers_pb2.StringValue
    alias_namespace: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    id: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    type: AliasType
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., alias: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., alias_namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[AliasType, str]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class AliasType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
