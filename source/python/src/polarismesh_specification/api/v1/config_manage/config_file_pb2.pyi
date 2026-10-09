from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigFileSupportedClient(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLIENT_SDK: _ClassVar[ConfigFileSupportedClient]
    CLIENT_AGENT: _ClassVar[ConfigFileSupportedClient]
    CLIENT_ALL: _ClassVar[ConfigFileSupportedClient]

class ConfigClientType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SDK: _ClassVar[ConfigClientType]
    Agent: _ClassVar[ConfigClientType]

class ConflictHandling(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFLICT_HANDLING_SKIP: _ClassVar[ConflictHandling]
    CONFLICT_HANDLING_OVERWRITE: _ClassVar[ConflictHandling]
CLIENT_SDK: ConfigFileSupportedClient
CLIENT_AGENT: ConfigFileSupportedClient
CLIENT_ALL: ConfigFileSupportedClient
SDK: ConfigClientType
Agent: ConfigClientType
CONFLICT_HANDLING_SKIP: ConflictHandling
CONFLICT_HANDLING_OVERWRITE: ConflictHandling

class ConfigFileGroup(_message.Message):
    __slots__ = ("id", "name", "namespace", "comment", "create_time", "create_by", "modify_time", "modify_by", "fileCount", "user_ids", "group_ids", "remove_user_ids", "remove_group_ids", "editable", "owner", "business", "department", "metadata", "deleteable")
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
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    FILECOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_FIELD_NUMBER: _ClassVar[int]
    DEPARTMENT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DELETEABLE_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.UInt64Value
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    fileCount: _wrappers_pb2.UInt64Value
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    editable: _wrappers_pb2.BoolValue
    owner: _wrappers_pb2.StringValue
    business: _wrappers_pb2.StringValue
    department: _wrappers_pb2.StringValue
    metadata: _containers.ScalarMap[str, str]
    deleteable: _wrappers_pb2.BoolValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., fileCount: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., business: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., department: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., deleteable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ConfigFilePersistent(_message.Message):
    __slots__ = ("encoding", "path", "post_cmd")
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    POST_CMD_FIELD_NUMBER: _ClassVar[int]
    encoding: str
    path: str
    post_cmd: str
    def __init__(self, encoding: _Optional[str] = ..., path: _Optional[str] = ..., post_cmd: _Optional[str] = ...) -> None: ...

class ConfigFile(_message.Message):
    __slots__ = ("id", "name", "namespace", "group", "content", "format", "comment", "status", "tags", "create_time", "create_by", "modify_time", "modify_by", "release_time", "release_by", "encrypted", "encrypt_algo", "supported_client", "persistent")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BY_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_ALGO_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.UInt64Value
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    status: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    create_time: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    release_time: _wrappers_pb2.StringValue
    release_by: _wrappers_pb2.StringValue
    encrypted: _wrappers_pb2.BoolValue
    encrypt_algo: _wrappers_pb2.StringValue
    supported_client: ConfigFileSupportedClient
    persistent: ConfigFilePersistent
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., encrypted: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., encrypt_algo: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., supported_client: _Optional[_Union[ConfigFileSupportedClient, str]] = ..., persistent: _Optional[_Union[ConfigFilePersistent, _Mapping]] = ...) -> None: ...

class ConfigFileTag(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: _wrappers_pb2.StringValue
    value: _wrappers_pb2.StringValue
    def __init__(self, key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileRelease(_message.Message):
    __slots__ = ("id", "name", "namespace", "group", "file_name", "content", "comment", "md5", "version", "create_time", "create_by", "modify_time", "modify_by", "tags", "active", "format", "release_description", "release_type", "beta_labels", "config_file_id", "supported_client", "persistent")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BETA_LABELS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.UInt64Value
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    md5: _wrappers_pb2.StringValue
    version: _wrappers_pb2.UInt64Value
    create_time: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    active: _wrappers_pb2.BoolValue
    format: _wrappers_pb2.StringValue
    release_description: _wrappers_pb2.StringValue
    release_type: _wrappers_pb2.StringValue
    beta_labels: _containers.RepeatedCompositeFieldContainer[_model_pb2.ClientLabel]
    config_file_id: _wrappers_pb2.UInt64Value
    supported_client: ConfigFileSupportedClient
    persistent: ConfigFilePersistent
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., active: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., beta_labels: _Optional[_Iterable[_Union[_model_pb2.ClientLabel, _Mapping]]] = ..., config_file_id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., supported_client: _Optional[_Union[ConfigFileSupportedClient, str]] = ..., persistent: _Optional[_Union[ConfigFilePersistent, _Mapping]] = ...) -> None: ...

class ConfigFileReleaseHistory(_message.Message):
    __slots__ = ("id", "name", "namespace", "group", "file_name", "content", "format", "comment", "md5", "type", "status", "tags", "create_time", "create_by", "modify_time", "modify_by", "reason", "release_description", "supported_client", "persistent")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.UInt64Value
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    md5: _wrappers_pb2.StringValue
    type: _wrappers_pb2.StringValue
    status: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    create_time: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    reason: _wrappers_pb2.StringValue
    release_description: _wrappers_pb2.StringValue
    supported_client: ConfigFileSupportedClient
    persistent: ConfigFilePersistent
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., reason: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., supported_client: _Optional[_Union[ConfigFileSupportedClient, str]] = ..., persistent: _Optional[_Union[ConfigFilePersistent, _Mapping]] = ...) -> None: ...

class ConfigFileTemplate(_message.Message):
    __slots__ = ("id", "name", "content", "format", "comment", "create_time", "create_by", "modify_time", "modify_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    id: _wrappers_pb2.UInt64Value
    name: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ClientConfigFileInfo(_message.Message):
    __slots__ = ("namespace", "group", "file_name", "content", "version", "md5", "tags", "encrypted", "public_key", "name", "release_time", "client_type", "supported_client", "persistent")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    namespace: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    version: _wrappers_pb2.UInt64Value
    md5: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    encrypted: _wrappers_pb2.BoolValue
    public_key: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    release_time: _wrappers_pb2.StringValue
    client_type: ConfigClientType
    supported_client: ConfigFileSupportedClient
    persistent: ConfigFilePersistent
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., encrypted: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., public_key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., client_type: _Optional[_Union[ConfigClientType, str]] = ..., supported_client: _Optional[_Union[ConfigFileSupportedClient, str]] = ..., persistent: _Optional[_Union[ConfigFilePersistent, _Mapping]] = ...) -> None: ...

class ClientWatchConfigFileRequest(_message.Message):
    __slots__ = ("client_ip", "service_name", "watch_files", "client_type")
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    WATCH_FILES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_ip: _wrappers_pb2.StringValue
    service_name: _wrappers_pb2.StringValue
    watch_files: _containers.RepeatedCompositeFieldContainer[ClientConfigFileInfo]
    client_type: ConfigClientType
    def __init__(self, client_ip: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., watch_files: _Optional[_Iterable[_Union[ClientConfigFileInfo, _Mapping]]] = ..., client_type: _Optional[_Union[ConfigClientType, str]] = ...) -> None: ...

class ConfigFileExportRequest(_message.Message):
    __slots__ = ("namespace", "groups", "names", "ids")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    namespace: _wrappers_pb2.StringValue
    groups: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    names: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., names: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., ids: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ...) -> None: ...

class ConfigFileImportRequest(_message.Message):
    __slots__ = ("namespace", "base64Content", "conflict_handling")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    BASE64CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_HANDLING_FIELD_NUMBER: _ClassVar[int]
    namespace: _wrappers_pb2.StringValue
    base64Content: _wrappers_pb2.StringValue
    conflict_handling: ConflictHandling
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., base64Content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., conflict_handling: _Optional[_Union[ConflictHandling, str]] = ...) -> None: ...

class ConfigFilePublishInfo(_message.Message):
    __slots__ = ("release_name", "namespace", "group", "file_name", "content", "comment", "format", "release_description", "create_by", "modify_by", "tags", "md5", "encrypted", "encrypt_algo", "supported_client", "persistent")
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPT_ALGO_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLIENT_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_FIELD_NUMBER: _ClassVar[int]
    release_name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    release_description: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    md5: _wrappers_pb2.StringValue
    encrypted: _wrappers_pb2.BoolValue
    encrypt_algo: _wrappers_pb2.StringValue
    supported_client: ConfigFileSupportedClient
    persistent: ConfigFilePersistent
    def __init__(self, release_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., encrypted: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., encrypt_algo: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., supported_client: _Optional[_Union[ConfigFileSupportedClient, str]] = ..., persistent: _Optional[_Union[ConfigFilePersistent, _Mapping]] = ...) -> None: ...

class ConfigFileGroupRequest(_message.Message):
    __slots__ = ("revision", "config_file_group", "client_labels", "client_type")
    class ClientLabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_GROUP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LABELS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    revision: _wrappers_pb2.StringValue
    config_file_group: ConfigFileGroup
    client_labels: _containers.ScalarMap[str, str]
    client_type: ConfigClientType
    def __init__(self, revision: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., config_file_group: _Optional[_Union[ConfigFileGroup, _Mapping]] = ..., client_labels: _Optional[_Mapping[str, str]] = ..., client_type: _Optional[_Union[ConfigClientType, str]] = ...) -> None: ...

class ConfigDiscoverRequest(_message.Message):
    __slots__ = ("type", "config_file", "revision")
    class ConfigDiscoverRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ConfigDiscoverRequest.ConfigDiscoverRequestType]
        CONFIG_FILE: _ClassVar[ConfigDiscoverRequest.ConfigDiscoverRequestType]
        CONFIG_FILE_Names: _ClassVar[ConfigDiscoverRequest.ConfigDiscoverRequestType]
        CONFIG_FILE_GROUPS: _ClassVar[ConfigDiscoverRequest.ConfigDiscoverRequestType]
    UNKNOWN: ConfigDiscoverRequest.ConfigDiscoverRequestType
    CONFIG_FILE: ConfigDiscoverRequest.ConfigDiscoverRequestType
    CONFIG_FILE_Names: ConfigDiscoverRequest.ConfigDiscoverRequestType
    CONFIG_FILE_GROUPS: ConfigDiscoverRequest.ConfigDiscoverRequestType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    type: ConfigDiscoverRequest.ConfigDiscoverRequestType
    config_file: ClientConfigFileInfo
    revision: str
    def __init__(self, type: _Optional[_Union[ConfigDiscoverRequest.ConfigDiscoverRequestType, str]] = ..., config_file: _Optional[_Union[ClientConfigFileInfo, _Mapping]] = ..., revision: _Optional[str] = ...) -> None: ...

class ConfigDiscoverResponse(_message.Message):
    __slots__ = ("code", "info", "revision", "type", "config_file", "config_file_names", "config_file_groups")
    class ConfigDiscoverResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ConfigDiscoverResponse.ConfigDiscoverResponseType]
        CONFIG_FILE: _ClassVar[ConfigDiscoverResponse.ConfigDiscoverResponseType]
        CONFIG_FILE_Names: _ClassVar[ConfigDiscoverResponse.ConfigDiscoverResponseType]
        CONFIG_FILE_GROUPS: _ClassVar[ConfigDiscoverResponse.ConfigDiscoverResponseType]
    UNKNOWN: ConfigDiscoverResponse.ConfigDiscoverResponseType
    CONFIG_FILE: ConfigDiscoverResponse.ConfigDiscoverResponseType
    CONFIG_FILE_Names: ConfigDiscoverResponse.ConfigDiscoverResponseType
    CONFIG_FILE_GROUPS: ConfigDiscoverResponse.ConfigDiscoverResponseType
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_NAMES_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FILE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    code: int
    info: str
    revision: str
    type: ConfigDiscoverResponse.ConfigDiscoverResponseType
    config_file: ClientConfigFileInfo
    config_file_names: _containers.RepeatedCompositeFieldContainer[ClientConfigFileInfo]
    config_file_groups: _containers.RepeatedCompositeFieldContainer[ConfigFileGroup]
    def __init__(self, code: _Optional[int] = ..., info: _Optional[str] = ..., revision: _Optional[str] = ..., type: _Optional[_Union[ConfigDiscoverResponse.ConfigDiscoverResponseType, str]] = ..., config_file: _Optional[_Union[ClientConfigFileInfo, _Mapping]] = ..., config_file_names: _Optional[_Iterable[_Union[ClientConfigFileInfo, _Mapping]]] = ..., config_file_groups: _Optional[_Iterable[_Union[ConfigFileGroup, _Mapping]]] = ...) -> None: ...
