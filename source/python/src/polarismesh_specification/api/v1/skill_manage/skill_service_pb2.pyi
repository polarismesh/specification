from ..skill_manage import skill_pb2 as _skill_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSkillRequest(_message.Message):
    __slots__ = ("name", "namespace", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    version: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class GetSkillResponse(_message.Message):
    __slots__ = ("code", "info", "resource", "version", "content")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    code: int
    info: str
    resource: _skill_pb2.SkillResource
    version: _skill_pb2.SkillResourceVersion
    content: str
    def __init__(self, code: _Optional[int] = ..., info: _Optional[str] = ..., resource: _Optional[_Union[_skill_pb2.SkillResource, _Mapping]] = ..., version: _Optional[_Union[_skill_pb2.SkillResourceVersion, _Mapping]] = ..., content: _Optional[str] = ...) -> None: ...

class ListSkillsRequest(_message.Message):
    __slots__ = ("namespace", "name", "tag", "owner", "scope", "keyword", "order_by", "order_type", "offset", "limit")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    tag: str
    owner: str
    scope: str
    keyword: str
    order_by: str
    order_type: str
    offset: int
    limit: int
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., tag: _Optional[str] = ..., owner: _Optional[str] = ..., scope: _Optional[str] = ..., keyword: _Optional[str] = ..., order_by: _Optional[str] = ..., order_type: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListSkillsResponse(_message.Message):
    __slots__ = ("code", "info", "total", "resources")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    code: int
    info: str
    total: int
    resources: _containers.RepeatedCompositeFieldContainer[_skill_pb2.SkillResource]
    def __init__(self, code: _Optional[int] = ..., info: _Optional[str] = ..., total: _Optional[int] = ..., resources: _Optional[_Iterable[_Union[_skill_pb2.SkillResource, _Mapping]]] = ...) -> None: ...

class DownloadSkillRequest(_message.Message):
    __slots__ = ("name", "namespace", "version", "tag", "format")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    namespace: str
    version: str
    tag: str
    format: str
    def __init__(self, name: _Optional[str] = ..., namespace: _Optional[str] = ..., version: _Optional[str] = ..., tag: _Optional[str] = ..., format: _Optional[str] = ...) -> None: ...

class DownloadSkillResponse(_message.Message):
    __slots__ = ("code", "info", "version", "content_type", "content", "zip_chunk", "total_size", "filename")
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ZIP_CHUNK_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    code: int
    info: str
    version: str
    content_type: str
    content: str
    zip_chunk: bytes
    total_size: int
    filename: str
    def __init__(self, code: _Optional[int] = ..., info: _Optional[str] = ..., version: _Optional[str] = ..., content_type: _Optional[str] = ..., content: _Optional[str] = ..., zip_chunk: _Optional[bytes] = ..., total_size: _Optional[int] = ..., filename: _Optional[str] = ...) -> None: ...
