from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceFeatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Service_Feature_Type_MS_Unknown: _ClassVar[ServiceFeatureType]
    Service_Feature_Type_MCP_Unknown: _ClassVar[ServiceFeatureType]
    Service_Feature_Type_MCP_Tool: _ClassVar[ServiceFeatureType]
    Service_Feature_Type_MCP_Resource: _ClassVar[ServiceFeatureType]
    Service_Feature_Type_MCP_Prompt: _ClassVar[ServiceFeatureType]

class ServiceFeatureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Service_Feature_Status_Enabled: _ClassVar[ServiceFeatureStatus]
    Service_Feature_Status_Disabled: _ClassVar[ServiceFeatureStatus]
Service_Feature_Type_MS_Unknown: ServiceFeatureType
Service_Feature_Type_MCP_Unknown: ServiceFeatureType
Service_Feature_Type_MCP_Tool: ServiceFeatureType
Service_Feature_Type_MCP_Resource: ServiceFeatureType
Service_Feature_Type_MCP_Prompt: ServiceFeatureType
Service_Feature_Status_Enabled: ServiceFeatureStatus
Service_Feature_Status_Disabled: ServiceFeatureStatus

class ServiceContract(_message.Message):
    __slots__ = ("id", "name", "namespace", "service", "protocol", "version", "revision", "content", "interfaces", "ctime", "mtime", "status", "type", "metadata", "content_digest", "service_features")
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
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    namespace: str
    service: str
    protocol: str
    version: str
    revision: str
    content: str
    interfaces: _containers.RepeatedCompositeFieldContainer[InterfaceDescriptor]
    ctime: str
    mtime: str
    status: str
    type: str
    metadata: _containers.ScalarMap[str, str]
    content_digest: str
    service_features: _containers.RepeatedCompositeFieldContainer[ServiceFeature]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ..., protocol: _Optional[str] = ..., version: _Optional[str] = ..., revision: _Optional[str] = ..., content: _Optional[str] = ..., interfaces: _Optional[_Iterable[_Union[InterfaceDescriptor, _Mapping]]] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., status: _Optional[str] = ..., type: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., content_digest: _Optional[str] = ..., service_features: _Optional[_Iterable[_Union[ServiceFeature, _Mapping]]] = ...) -> None: ...

class InterfaceDescriptor(_message.Message):
    __slots__ = ("id", "method", "path", "content", "source", "revision", "ctime", "mtime", "name", "namespace", "service", "protocol", "version", "type", "content_digest")
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[InterfaceDescriptor.Source]
        Manual: _ClassVar[InterfaceDescriptor.Source]
        Client: _ClassVar[InterfaceDescriptor.Source]
    UNKNOWN: InterfaceDescriptor.Source
    Manual: InterfaceDescriptor.Source
    Client: InterfaceDescriptor.Source
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DIGEST_FIELD_NUMBER: _ClassVar[int]
    id: str
    method: str
    path: str
    content: str
    source: InterfaceDescriptor.Source
    revision: str
    ctime: str
    mtime: str
    name: str
    namespace: str
    service: str
    protocol: str
    version: str
    type: str
    content_digest: str
    def __init__(self, id: _Optional[str] = ..., method: _Optional[str] = ..., path: _Optional[str] = ..., content: _Optional[str] = ..., source: _Optional[_Union[InterfaceDescriptor.Source, str]] = ..., revision: _Optional[str] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., name: _Optional[str] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ..., protocol: _Optional[str] = ..., version: _Optional[str] = ..., type: _Optional[str] = ..., content_digest: _Optional[str] = ...) -> None: ...

class ServiceFeature(_message.Message):
    __slots__ = ("id", "type", "name", "description", "content", "status", "ctime", "mtime")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: ServiceFeatureType
    name: str
    description: str
    content: str
    status: ServiceFeatureStatus
    ctime: str
    mtime: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[ServiceFeatureType, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., content: _Optional[str] = ..., status: _Optional[_Union[ServiceFeatureStatus, str]] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ...) -> None: ...
