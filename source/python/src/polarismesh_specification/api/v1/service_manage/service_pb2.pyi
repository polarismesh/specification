from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICE_TYPE_MICROSERVICE: _ClassVar[ServiceType]
    SERVICE_TYPE_MCP_SERVER: _ClassVar[ServiceType]
    SERVICE_TYPE_AI_AGENT: _ClassVar[ServiceType]

class ServiceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL: _ClassVar[ServiceStatus]
    ABNORMAL: _ClassVar[ServiceStatus]
    OFFLINE: _ClassVar[ServiceStatus]

class AliasType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[AliasType]
    CL5SID: _ClassVar[AliasType]
SERVICE_TYPE_MICROSERVICE: ServiceType
SERVICE_TYPE_MCP_SERVER: ServiceType
SERVICE_TYPE_AI_AGENT: ServiceType
NORMAL: ServiceStatus
ABNORMAL: ServiceStatus
OFFLINE: ServiceStatus
DEFAULT: AliasType
CL5SID: AliasType

class Service(_message.Message):
    __slots__ = ("name", "namespace", "metadata", "ports", "business", "department", "cmdb_mod1", "cmdb_mod2", "cmdb_mod3", "comment", "owners", "token", "ctime", "mtime", "revision", "platform_id", "total_instance_count", "healthy_instance_count", "user_ids", "group_ids", "remove_user_ids", "remove_group_ids", "id", "editable", "export_to", "sync_to_global_registry", "isolate_instance_count", "service_status", "deleteable", "service_type", "extended_metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD1_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD2_FIELD_NUMBER: _ClassVar[int]
    CMDB_MOD3_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TO_FIELD_NUMBER: _ClassVar[int]
    SYNC_TO_GLOBAL_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    ISOLATE_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    DELETEABLE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    ports: _wrappers_pb2.StringValue
    business: _wrappers_pb2.StringValue
    department: _wrappers_pb2.StringValue
    cmdb_mod1: _wrappers_pb2.StringValue
    cmdb_mod2: _wrappers_pb2.StringValue
    cmdb_mod3: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    token: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    platform_id: _wrappers_pb2.StringValue
    total_instance_count: _wrappers_pb2.UInt32Value
    healthy_instance_count: _wrappers_pb2.UInt32Value
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    id: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    export_to: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    sync_to_global_registry: bool
    isolate_instance_count: _wrappers_pb2.UInt32Value
    service_status: ServiceStatus
    deleteable: _wrappers_pb2.BoolValue
    service_type: ServiceType
    extended_metadata: _containers.RepeatedCompositeFieldContainer[ExtendedMetadata]
    def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., ports: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., business: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., department: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod1: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod2: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., cmdb_mod3: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., platform_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., healthy_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., export_to: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., sync_to_global_registry: _Optional[bool] = ..., isolate_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., service_status: _Optional[_Union[ServiceStatus, str]] = ..., deleteable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., service_type: _Optional[_Union[ServiceType, str]] = ..., extended_metadata: _Optional[_Iterable[_Union[ExtendedMetadata, _Mapping]]] = ...) -> None: ...

class ExtendedMetadata(_message.Message):
    __slots__ = ("type", "agent_skill")
    class ExtendedMetadataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTENDED_METADATA_UNKNOWN: _ClassVar[ExtendedMetadata.ExtendedMetadataType]
        EXTENDED_METADATA_SKILL: _ClassVar[ExtendedMetadata.ExtendedMetadataType]
    EXTENDED_METADATA_UNKNOWN: ExtendedMetadata.ExtendedMetadataType
    EXTENDED_METADATA_SKILL: ExtendedMetadata.ExtendedMetadataType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILL_FIELD_NUMBER: _ClassVar[int]
    type: ExtendedMetadata.ExtendedMetadataType
    agent_skill: AgentSkill
    def __init__(self, type: _Optional[_Union[ExtendedMetadata.ExtendedMetadataType, str]] = ..., agent_skill: _Optional[_Union[AgentSkill, _Mapping]] = ...) -> None: ...

class AgentSkill(_message.Message):
    __slots__ = ("id", "name", "description", "tags", "examples", "input_modes", "output_modes", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    INPUT_MODES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_MODES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    examples: _containers.RepeatedScalarFieldContainer[str]
    input_modes: _containers.RepeatedScalarFieldContainer[str]
    output_modes: _containers.RepeatedScalarFieldContainer[str]
    version: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., examples: _Optional[_Iterable[str]] = ..., input_modes: _Optional[_Iterable[str]] = ..., output_modes: _Optional[_Iterable[str]] = ..., version: _Optional[str] = ...) -> None: ...

class ServiceAlias(_message.Message):
    __slots__ = ("service", "namespace", "alias", "alias_namespace", "type", "owners", "comment", "service_token", "ctime", "mtime", "id", "editable", "deleteable", "export_to", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    ALIAS_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    DELETEABLE_FIELD_NUMBER: _ClassVar[int]
    EXPORT_TO_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    alias: _wrappers_pb2.StringValue
    alias_namespace: _wrappers_pb2.StringValue
    type: AliasType
    owners: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    id: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    deleteable: _wrappers_pb2.BoolValue
    export_to: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., alias: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., alias_namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[AliasType, str]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., deleteable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., export_to: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Instance(_message.Message):
    __slots__ = ("id", "service", "namespace", "vpc_id", "host", "port", "protocol", "version", "priority", "weight", "enable_health_check", "health_check", "healthy", "isolate", "location", "metadata", "logic_set", "ctime", "mtime", "revision", "service_token")
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
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_FIELD_NUMBER: _ClassVar[int]
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    ISOLATE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LOGIC_SET_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    service: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    vpc_id: _wrappers_pb2.StringValue
    host: _wrappers_pb2.StringValue
    port: _wrappers_pb2.UInt32Value
    protocol: _wrappers_pb2.StringValue
    version: _wrappers_pb2.StringValue
    priority: _wrappers_pb2.UInt32Value
    weight: _wrappers_pb2.UInt32Value
    enable_health_check: _wrappers_pb2.BoolValue
    health_check: HealthCheck
    healthy: _wrappers_pb2.BoolValue
    isolate: _wrappers_pb2.BoolValue
    location: _model_pb2.Location
    metadata: _containers.ScalarMap[str, str]
    logic_set: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    revision: _wrappers_pb2.StringValue
    service_token: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., vpc_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., host: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., protocol: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., priority: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., weight: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., enable_health_check: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., health_check: _Optional[_Union[HealthCheck, _Mapping]] = ..., healthy: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., isolate: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., location: _Optional[_Union[_model_pb2.Location, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., logic_set: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class HealthCheck(_message.Message):
    __slots__ = ("type", "heartbeat")
    class HealthCheckType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[HealthCheck.HealthCheckType]
        HEARTBEAT: _ClassVar[HealthCheck.HealthCheckType]
    UNKNOWN: HealthCheck.HealthCheckType
    HEARTBEAT: HealthCheck.HealthCheckType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    type: HealthCheck.HealthCheckType
    heartbeat: HeartbeatHealthCheck
    def __init__(self, type: _Optional[_Union[HealthCheck.HealthCheckType, str]] = ..., heartbeat: _Optional[_Union[HeartbeatHealthCheck, _Mapping]] = ...) -> None: ...

class HeartbeatHealthCheck(_message.Message):
    __slots__ = ("ttl",)
    TTL_FIELD_NUMBER: _ClassVar[int]
    ttl: _wrappers_pb2.UInt32Value
    def __init__(self, ttl: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
