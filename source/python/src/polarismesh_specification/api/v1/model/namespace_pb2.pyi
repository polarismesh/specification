from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Namespace(_message.Message):
    __slots__ = ("name", "comment", "owners", "token", "ctime", "mtime", "total_service_count", "total_health_instance_count", "total_instance_count", "user_ids", "group_ids", "remove_user_ids", "remove_group_ids", "id", "editable", "service_export_to", "metadata", "sync_to_global_registry", "deleteable")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SERVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HEALTH_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_EXPORT_TO_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    SYNC_TO_GLOBAL_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    DELETEABLE_FIELD_NUMBER: _ClassVar[int]
    name: _wrappers_pb2.StringValue
    comment: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    token: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    total_service_count: _wrappers_pb2.UInt32Value
    total_health_instance_count: _wrappers_pb2.UInt32Value
    total_instance_count: _wrappers_pb2.UInt32Value
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    id: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    service_export_to: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    metadata: _containers.ScalarMap[str, str]
    sync_to_global_registry: bool
    deleteable: _wrappers_pb2.BoolValue
    def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total_service_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., total_health_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., total_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., service_export_to: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., sync_to_global_registry: _Optional[bool] = ..., deleteable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
