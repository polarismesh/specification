from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONLY_READ: _ClassVar[AuthAction]
    READ_WRITE: _ClassVar[AuthAction]
    ALLOW: _ClassVar[AuthAction]
    DENY: _ClassVar[AuthAction]

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Namespaces: _ClassVar[ResourceType]
    Services: _ClassVar[ResourceType]
    ConfigGroups: _ClassVar[ResourceType]
    RouteRules: _ClassVar[ResourceType]
    RateLimitRules: _ClassVar[ResourceType]
    CircuitBreakerRules: _ClassVar[ResourceType]
    FaultDetectRules: _ClassVar[ResourceType]
    LaneRules: _ClassVar[ResourceType]
    Users: _ClassVar[ResourceType]
    UserGroups: _ClassVar[ResourceType]
    Roles: _ClassVar[ResourceType]
    PolicyRules: _ClassVar[ResourceType]
ONLY_READ: AuthAction
READ_WRITE: AuthAction
ALLOW: AuthAction
DENY: AuthAction
Namespaces: ResourceType
Services: ResourceType
ConfigGroups: ResourceType
RouteRules: ResourceType
RateLimitRules: ResourceType
CircuitBreakerRules: ResourceType
FaultDetectRules: ResourceType
LaneRules: ResourceType
Users: ResourceType
UserGroups: ResourceType
Roles: ResourceType
PolicyRules: ResourceType

class LoginRequest(_message.Message):
    __slots__ = ("owner", "name", "password", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    owner: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    password: _wrappers_pb2.StringValue
    options: _containers.ScalarMap[str, str]
    def __init__(self, owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("user_id", "name", "role", "owner_id", "token", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    user_id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    role: _wrappers_pb2.StringValue
    owner_id: _wrappers_pb2.StringValue
    token: _wrappers_pb2.StringValue
    options: _containers.ScalarMap[str, str]
    def __init__(self, user_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., role: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "password", "owner", "source", "auth_token", "token_enable", "comment", "ctime", "mtime", "user_type", "mobile", "email", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    USER_TYPE_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    password: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    source: _wrappers_pb2.StringValue
    auth_token: _wrappers_pb2.StringValue
    token_enable: _wrappers_pb2.BoolValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    user_type: _wrappers_pb2.StringValue
    mobile: _wrappers_pb2.StringValue
    email: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., source: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., auth_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token_enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., user_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mobile: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., email: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ModifyUserPassword(_message.Message):
    __slots__ = ("id", "old_password", "new_password")
    ID_FIELD_NUMBER: _ClassVar[int]
    OLD_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    old_password: _wrappers_pb2.StringValue
    new_password: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., old_password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., new_password: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class UserGroupRelation(_message.Message):
    __slots__ = ("group_id", "users")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    group_id: _wrappers_pb2.StringValue
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, group_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class UserGroup(_message.Message):
    __slots__ = ("id", "name", "owner", "auth_token", "token_enable", "comment", "ctime", "mtime", "relation", "user_count", "source", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    RELATION_FIELD_NUMBER: _ClassVar[int]
    USER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    auth_token: _wrappers_pb2.StringValue
    token_enable: _wrappers_pb2.BoolValue
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    relation: UserGroupRelation
    user_count: _wrappers_pb2.UInt32Value
    source: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., auth_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token_enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., relation: _Optional[_Union[UserGroupRelation, _Mapping]] = ..., user_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., source: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ModifyUserGroup(_message.Message):
    __slots__ = ("id", "owner", "name", "auth_token", "token_enable", "comment", "add_relations", "remove_relations", "metadata", "source")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENABLE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ADD_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    auth_token: _wrappers_pb2.StringValue
    token_enable: _wrappers_pb2.BoolValue
    comment: _wrappers_pb2.StringValue
    add_relations: UserGroupRelation
    remove_relations: UserGroupRelation
    metadata: _containers.ScalarMap[str, str]
    source: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., auth_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token_enable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., add_relations: _Optional[_Union[UserGroupRelation, _Mapping]] = ..., remove_relations: _Optional[_Union[UserGroupRelation, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., source: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "name", "owner", "source", "default_role", "metadata", "comment", "ctime", "mtime", "users", "user_groups")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    owner: str
    source: str
    default_role: bool
    metadata: _containers.ScalarMap[str, str]
    comment: str
    ctime: str
    mtime: str
    users: _containers.RepeatedCompositeFieldContainer[User]
    user_groups: _containers.RepeatedCompositeFieldContainer[UserGroup]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., owner: _Optional[str] = ..., source: _Optional[str] = ..., default_role: _Optional[bool] = ..., metadata: _Optional[_Mapping[str, str]] = ..., comment: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., user_groups: _Optional[_Iterable[_Union[UserGroup, _Mapping]]] = ...) -> None: ...

class Principal(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class Principals(_message.Message):
    __slots__ = ("users", "groups", "roles")
    USERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[Principal]
    groups: _containers.RepeatedCompositeFieldContainer[Principal]
    roles: _containers.RepeatedCompositeFieldContainer[Principal]
    def __init__(self, users: _Optional[_Iterable[_Union[Principal, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[Principal, _Mapping]]] = ..., roles: _Optional[_Iterable[_Union[Principal, _Mapping]]] = ...) -> None: ...

class StrategyResourceEntry(_message.Message):
    __slots__ = ("id", "namespace", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class StrategyResources(_message.Message):
    __slots__ = ("strategy_id", "namespaces", "services", "config_groups", "route_rules", "ratelimit_rules", "circuitbreaker_rules", "faultdetect_rules", "lane_rules", "users", "user_groups", "roles", "auth_policies")
    STRATEGY_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ROUTE_RULES_FIELD_NUMBER: _ClassVar[int]
    RATELIMIT_RULES_FIELD_NUMBER: _ClassVar[int]
    CIRCUITBREAKER_RULES_FIELD_NUMBER: _ClassVar[int]
    FAULTDETECT_RULES_FIELD_NUMBER: _ClassVar[int]
    LANE_RULES_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    USER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    AUTH_POLICIES_FIELD_NUMBER: _ClassVar[int]
    strategy_id: _wrappers_pb2.StringValue
    namespaces: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    services: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    config_groups: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    route_rules: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    ratelimit_rules: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    circuitbreaker_rules: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    faultdetect_rules: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    lane_rules: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    users: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    user_groups: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    roles: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    auth_policies: _containers.RepeatedCompositeFieldContainer[StrategyResourceEntry]
    def __init__(self, strategy_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespaces: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., services: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., config_groups: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., route_rules: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., ratelimit_rules: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., circuitbreaker_rules: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., faultdetect_rules: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., lane_rules: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., user_groups: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., roles: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ..., auth_policies: _Optional[_Iterable[_Union[StrategyResourceEntry, _Mapping]]] = ...) -> None: ...

class StrategyResourceLabel(_message.Message):
    __slots__ = ("key", "value", "compare_type")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COMPARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    compare_type: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., compare_type: _Optional[str] = ...) -> None: ...

class AuthStrategy(_message.Message):
    __slots__ = ("id", "name", "principals", "resources", "action", "comment", "owner", "ctime", "mtime", "auth_token", "default_strategy", "metadata", "source", "functions", "resource_labels")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    principals: Principals
    resources: StrategyResources
    action: AuthAction
    comment: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    auth_token: _wrappers_pb2.StringValue
    default_strategy: _wrappers_pb2.BoolValue
    metadata: _containers.ScalarMap[str, str]
    source: _wrappers_pb2.StringValue
    functions: _containers.RepeatedScalarFieldContainer[str]
    resource_labels: _containers.RepeatedCompositeFieldContainer[StrategyResourceLabel]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., principals: _Optional[_Union[Principals, _Mapping]] = ..., resources: _Optional[_Union[StrategyResources, _Mapping]] = ..., action: _Optional[_Union[AuthAction, str]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., auth_token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., default_strategy: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., source: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., functions: _Optional[_Iterable[str]] = ..., resource_labels: _Optional[_Iterable[_Union[StrategyResourceLabel, _Mapping]]] = ...) -> None: ...

class ModifyAuthStrategy(_message.Message):
    __slots__ = ("id", "name", "add_principals", "remove_principals", "add_resources", "remove_resources", "action", "comment", "owner", "metadata", "source", "functions", "resource_labels")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PRINCIPALS_FIELD_NUMBER: _ClassVar[int]
    ADD_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LABELS_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    add_principals: Principals
    remove_principals: Principals
    add_resources: StrategyResources
    remove_resources: StrategyResources
    action: AuthAction
    comment: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    source: _wrappers_pb2.StringValue
    functions: _containers.RepeatedScalarFieldContainer[str]
    resource_labels: _containers.RepeatedCompositeFieldContainer[StrategyResourceLabel]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., add_principals: _Optional[_Union[Principals, _Mapping]] = ..., remove_principals: _Optional[_Union[Principals, _Mapping]] = ..., add_resources: _Optional[_Union[StrategyResources, _Mapping]] = ..., remove_resources: _Optional[_Union[StrategyResources, _Mapping]] = ..., action: _Optional[_Union[AuthAction, str]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., source: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., functions: _Optional[_Iterable[str]] = ..., resource_labels: _Optional[_Iterable[_Union[StrategyResourceLabel, _Mapping]]] = ...) -> None: ...
