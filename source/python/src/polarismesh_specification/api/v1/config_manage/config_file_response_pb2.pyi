from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..config_manage import config_file_pb2 as _config_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigBatchQueryResponse(_message.Message):
    __slots__ = ["code", "configFileGroups", "configFileReleaseHistories", "configFileReleases", "configFileTemplates", "configFiles", "info", "total"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILEGROUPS_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILERELEASEHISTORIES_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILERELEASES_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILES_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILETEMPLATES_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    configFileGroups: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFileGroup]
    configFileReleaseHistories: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFileReleaseHistory]
    configFileReleases: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFileRelease]
    configFileTemplates: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFileTemplate]
    configFiles: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFile]
    info: _wrappers_pb2.StringValue
    total: _wrappers_pb2.UInt32Value
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., configFileGroups: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFileGroup, _Mapping]]] = ..., configFiles: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFile, _Mapping]]] = ..., configFileReleases: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFileRelease, _Mapping]]] = ..., configFileReleaseHistories: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFileReleaseHistory, _Mapping]]] = ..., configFileTemplates: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFileTemplate, _Mapping]]] = ...) -> None: ...

class ConfigBatchWriteResponse(_message.Message):
    __slots__ = ["code", "info", "responses", "total"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    responses: _containers.RepeatedCompositeFieldContainer[ConfigResponse]
    total: _wrappers_pb2.UInt32Value
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., total: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., responses: _Optional[_Iterable[_Union[ConfigResponse, _Mapping]]] = ...) -> None: ...

class ConfigClientResponse(_message.Message):
    __slots__ = ["code", "configFile", "info"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    configFile: _config_file_pb2.ClientConfigFileInfo
    info: _wrappers_pb2.StringValue
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., configFile: _Optional[_Union[_config_file_pb2.ClientConfigFileInfo, _Mapping]] = ...) -> None: ...

class ConfigExportResponse(_message.Message):
    __slots__ = ["code", "data", "info"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    data: _wrappers_pb2.BytesValue
    info: _wrappers_pb2.StringValue
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., data: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class ConfigImportResponse(_message.Message):
    __slots__ = ["code", "createConfigFiles", "info", "overwriteConfigFiles", "skipConfigFiles"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CREATECONFIGFILES_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    OVERWRITECONFIGFILES_FIELD_NUMBER: _ClassVar[int]
    SKIPCONFIGFILES_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    createConfigFiles: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFile]
    info: _wrappers_pb2.StringValue
    overwriteConfigFiles: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFile]
    skipConfigFiles: _containers.RepeatedCompositeFieldContainer[_config_file_pb2.ConfigFile]
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., createConfigFiles: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFile, _Mapping]]] = ..., skipConfigFiles: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFile, _Mapping]]] = ..., overwriteConfigFiles: _Optional[_Iterable[_Union[_config_file_pb2.ConfigFile, _Mapping]]] = ...) -> None: ...

class ConfigResponse(_message.Message):
    __slots__ = ["code", "configFile", "configFileGroup", "configFileRelease", "configFileReleaseHistory", "configFileTemplate", "info"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILEGROUP_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILERELEASEHISTORY_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILERELEASE_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILETEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CONFIGFILE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    configFile: _config_file_pb2.ConfigFile
    configFileGroup: _config_file_pb2.ConfigFileGroup
    configFileRelease: _config_file_pb2.ConfigFileRelease
    configFileReleaseHistory: _config_file_pb2.ConfigFileReleaseHistory
    configFileTemplate: _config_file_pb2.ConfigFileTemplate
    info: _wrappers_pb2.StringValue
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., configFileGroup: _Optional[_Union[_config_file_pb2.ConfigFileGroup, _Mapping]] = ..., configFile: _Optional[_Union[_config_file_pb2.ConfigFile, _Mapping]] = ..., configFileRelease: _Optional[_Union[_config_file_pb2.ConfigFileRelease, _Mapping]] = ..., configFileReleaseHistory: _Optional[_Union[_config_file_pb2.ConfigFileReleaseHistory, _Mapping]] = ..., configFileTemplate: _Optional[_Union[_config_file_pb2.ConfigFileTemplate, _Mapping]] = ...) -> None: ...

class ConfigSimpleResponse(_message.Message):
    __slots__ = ["code", "info"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    code: _wrappers_pb2.UInt32Value
    info: _wrappers_pb2.StringValue
    def __init__(self, code: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., info: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...
