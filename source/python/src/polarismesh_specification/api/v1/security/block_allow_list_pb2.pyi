from ..model import model_pb2 as _model_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BlockAllowListRule(_message.Message):
    __slots__ = ("id", "name", "metadata", "namespace", "service", "description", "priority", "enable", "ctime", "mtime", "etime", "blockAllowConfig", "revision")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    CTIME_FIELD_NUMBER: _ClassVar[int]
    MTIME_FIELD_NUMBER: _ClassVar[int]
    ETIME_FIELD_NUMBER: _ClassVar[int]
    BLOCKALLOWCONFIG_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    metadata: _containers.ScalarMap[str, str]
    namespace: str
    service: str
    description: str
    priority: int
    enable: bool
    ctime: str
    mtime: str
    etime: str
    blockAllowConfig: _containers.RepeatedCompositeFieldContainer[BlockAllowConfig]
    revision: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., namespace: _Optional[str] = ..., service: _Optional[str] = ..., description: _Optional[str] = ..., priority: _Optional[int] = ..., enable: _Optional[bool] = ..., ctime: _Optional[str] = ..., mtime: _Optional[str] = ..., etime: _Optional[str] = ..., blockAllowConfig: _Optional[_Iterable[_Union[BlockAllowConfig, _Mapping]]] = ..., revision: _Optional[str] = ...) -> None: ...

class BlockAllowConfig(_message.Message):
    __slots__ = ("api", "arguments", "blockAllowPolicy")
    class BlockAllowPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOW_LIST: _ClassVar[BlockAllowConfig.BlockAllowPolicy]
        BLOCK_LIST: _ClassVar[BlockAllowConfig.BlockAllowPolicy]
    ALLOW_LIST: BlockAllowConfig.BlockAllowPolicy
    BLOCK_LIST: BlockAllowConfig.BlockAllowPolicy
    class MatchArgument(_message.Message):
        __slots__ = ("type", "key", "value")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CUSTOM: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            HEADER: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            QUERY: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            CALLER_SERVICE: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            CALLER_IP: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            CALLER_METADATA: _ClassVar[BlockAllowConfig.MatchArgument.Type]
            CALLEE_METADATA: _ClassVar[BlockAllowConfig.MatchArgument.Type]
        CUSTOM: BlockAllowConfig.MatchArgument.Type
        HEADER: BlockAllowConfig.MatchArgument.Type
        QUERY: BlockAllowConfig.MatchArgument.Type
        CALLER_SERVICE: BlockAllowConfig.MatchArgument.Type
        CALLER_IP: BlockAllowConfig.MatchArgument.Type
        CALLER_METADATA: BlockAllowConfig.MatchArgument.Type
        CALLEE_METADATA: BlockAllowConfig.MatchArgument.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        type: BlockAllowConfig.MatchArgument.Type
        key: str
        value: _model_pb2.MatchString
        def __init__(self, type: _Optional[_Union[BlockAllowConfig.MatchArgument.Type, str]] = ..., key: _Optional[str] = ..., value: _Optional[_Union[_model_pb2.MatchString, _Mapping]] = ...) -> None: ...
    API_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    BLOCKALLOWPOLICY_FIELD_NUMBER: _ClassVar[int]
    api: _model_pb2.API
    arguments: _containers.RepeatedCompositeFieldContainer[BlockAllowConfig.MatchArgument]
    blockAllowPolicy: BlockAllowConfig.BlockAllowPolicy
    def __init__(self, api: _Optional[_Union[_model_pb2.API, _Mapping]] = ..., arguments: _Optional[_Iterable[_Union[BlockAllowConfig.MatchArgument, _Mapping]]] = ..., blockAllowPolicy: _Optional[_Union[BlockAllowConfig.BlockAllowPolicy, str]] = ...) -> None: ...
