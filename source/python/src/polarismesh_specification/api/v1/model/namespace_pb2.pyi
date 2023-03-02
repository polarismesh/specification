from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Namespace(_message.Message):
    __slots__ = ["comment", "ctime", "editable", "group_ids", "id", "mtime", "name", "owners", "remove_group_ids", "remove_user_ids", "token", "total_health_instance_count", "total_instance_count", "total_service_count", "user_ids"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    EDITABLE_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_USER_IDS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HEALTH_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INSTANCE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SERVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    comment: _wrappers_pb2.StringValue
    ctime: _wrappers_pb2.StringValue
    editable: _wrappers_pb2.BoolValue
    group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    id: _wrappers_pb2.StringValue
    mtime: _wrappers_pb2.StringValue
    name: _wrappers_pb2.StringValue
    owners: _wrappers_pb2.StringValue
    remove_group_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    remove_user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    token: _wrappers_pb2.StringValue
    total_health_instance_count: _wrappers_pb2.UInt32Value
    total_instance_count: _wrappers_pb2.UInt32Value
    total_service_count: _wrappers_pb2.UInt32Value
    user_ids: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., comment: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., owners: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., token: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., ctime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., mtime: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total_service_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., total_health_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., total_instance_count: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_user_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., remove_group_ids: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ..., id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., editable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
