from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientConfigFileInfo(_message.Message):
    __slots__ = ["content", "file_name", "group", "md5", "namespace", "version"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    content: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    md5: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    version: _wrappers_pb2.UInt64Value
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ClientWatchConfigFileRequest(_message.Message):
    __slots__ = ["client_ip", "service_name", "watch_files"]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    WATCH_FILES_FIELD_NUMBER: _ClassVar[int]
    client_ip: _wrappers_pb2.StringValue
    service_name: _wrappers_pb2.StringValue
    watch_files: _containers.RepeatedCompositeFieldContainer[ClientConfigFileInfo]
    def __init__(self, client_ip: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., service_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., watch_files: _Optional[_Iterable[_Union[ClientConfigFileInfo, _Mapping]]] = ...) -> None: ...

class ConfigFile(_message.Message):
    __slots__ = ["comment", "content", "create_by", "create_time", "format", "group", "id", "modify_by", "modify_time", "name", "namespace", "release_by", "release_time", "status", "tags"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_BY_FIELD_NUMBER: _ClassVar[int]
    RELEASE_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    id: _wrappers_pb2.UInt64Value
    modify_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    release_by: _wrappers_pb2.StringValue
    release_time: _wrappers_pb2.StringValue
    status: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., release_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileExportRequest(_message.Message):
    __slots__ = ["groups", "names", "namespace"]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    names: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    namespace: _wrappers_pb2.StringValue
    def __init__(self, namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., names: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ...) -> None: ...

class ConfigFileGroup(_message.Message):
    __slots__ = ["comment", "create_by", "create_time", "editable", "fileCount", "group_ids", "id", "modify_by", "modify_time", "name", "namespace", "owner", "remove_group_ids", "remove_user_ids", "user_ids"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    FILECOUNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    fileCount: _wrappers_pb2.UInt64Value
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    id: _wrappers_pb2.UInt64Value
    modify_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    owner: _wrappers_pb2.StringValue
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., fileCount: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., owner: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileRelease(_message.Message):
    __slots__ = ["comment", "content", "create_by", "create_time", "file_name", "group", "id", "md5", "modify_by", "modify_time", "name", "namespace", "version"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    id: _wrappers_pb2.UInt64Value
    md5: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    version: _wrappers_pb2.UInt64Value
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., version: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileReleaseHistory(_message.Message):
    __slots__ = ["comment", "content", "create_by", "create_time", "file_name", "format", "group", "id", "md5", "modify_by", "modify_time", "name", "namespace", "status", "tags", "type"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    file_name: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    group: _wrappers_pb2.StringValue
    id: _wrappers_pb2.UInt64Value
    md5: _wrappers_pb2.StringValue
    modify_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    namespace: _wrappers_pb2.StringValue
    status: _wrappers_pb2.StringValue
    tags: _containers.RepeatedCompositeFieldContainer[ConfigFileTag]
    type: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., namespace: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., group: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., file_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., md5: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., type: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., status: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[ConfigFileTag, _Mapping]]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileTag(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: _wrappers_pb2.StringValue
    value: _wrappers_pb2.StringValue
    def __init__(self, key: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., value: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class ConfigFileTemplate(_message.Message):
    __slots__ = ["comment", "content", "create_by", "create_time", "format", "id", "modify_by", "modify_time", "name"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_BY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODIFY_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    content: _wrappers_pb2.StringValue
    create_by: _wrappers_pb2.StringValue
    create_time: _wrappers_pb2.StringValue
    format: _wrappers_pb2.StringValue
    id: _wrappers_pb2.UInt64Value
    modify_by: _wrappers_pb2.StringValue
    modify_time: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., content: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., format: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., create_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_time: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., modify_by: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
