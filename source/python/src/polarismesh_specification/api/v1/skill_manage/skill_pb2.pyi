from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkillResource(_message.Message):
    __slots__ = ("id", "name", "namespace", "description", "status", "tags", "examples", "ext", "source", "version_info", "meta_version", "scope", "owner", "download_count", "create_time", "modify_time")
    class ExtEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    META_VERSION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    namespace: str
    description: str
    status: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    examples: _containers.RepeatedScalarFieldContainer[str]
    ext: _containers.ScalarMap[str, str]
    source: str
    version_info: VersionInfo
    meta_version: int
    scope: str
    owner: str
    download_count: int
    create_time: str
    modify_time: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., examples: _Optional[_Iterable[str]] = ..., ext: _Optional[_Mapping[str, str]] = ..., source: _Optional[str] = ..., version_info: _Optional[_Union[VersionInfo, _Mapping]] = ..., meta_version: _Optional[int] = ..., scope: _Optional[str] = ..., owner: _Optional[str] = ..., download_count: _Optional[int] = ..., create_time: _Optional[str] = ..., modify_time: _Optional[str] = ...) -> None: ...

class VersionInfo(_message.Message):
    __slots__ = ("active_version", "latest_version", "total_versions")
    ACTIVE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    active_version: str
    latest_version: str
    total_versions: int
    def __init__(self, active_version: _Optional[str] = ..., latest_version: _Optional[str] = ..., total_versions: _Optional[int] = ...) -> None: ...

class SkillResourceVersion(_message.Message):
    __slots__ = ("id", "name", "namespace", "version", "author", "description", "status", "storage", "download_count", "create_time", "modify_time")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    namespace: str
    version: str
    author: str
    description: str
    status: str
    storage: StorageInfo
    download_count: int
    create_time: str
    modify_time: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., version: _Optional[str] = ..., author: _Optional[str] = ..., description: _Optional[str] = ..., status: _Optional[str] = ..., storage: _Optional[_Union[StorageInfo, _Mapping]] = ..., download_count: _Optional[int] = ..., create_time: _Optional[str] = ..., modify_time: _Optional[str] = ...) -> None: ...

class StorageInfo(_message.Message):
    __slots__ = ("provider", "files", "scope", "content_digest")
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    provider: str
    files: _containers.RepeatedScalarFieldContainer[str]
    scope: str
    content_digest: str
    def __init__(self, provider: _Optional[str] = ..., files: _Optional[_Iterable[str]] = ..., scope: _Optional[str] = ..., content_digest: _Optional[str] = ...) -> None: ...
