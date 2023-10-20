from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateProjectRequest(_message.Message):
    __slots__ = ["name", "description", "key_values", "relations", "data_class", "preferred_endpoint", "metadata_license_tag", "default_data_license_tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    data_class: _models_pb2.DataClass
    preferred_endpoint: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ..., preferred_endpoint: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class GetProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class GetProjectsRequest(_message.Message):
    __slots__ = ["project_ids"]
    PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    project_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetProjectsResponse(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_models_pb2.Project]
    def __init__(self, projects: _Optional[_Iterable[_Union[_models_pb2.Project, _Mapping]]] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProjectNameRequest(_message.Message):
    __slots__ = ["project_id", "name"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateProjectNameResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectDescriptionRequest(_message.Message):
    __slots__ = ["project_id", "description"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    description: str
    def __init__(self, project_id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateProjectDescriptionResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectKeyValuesRequest(_message.Message):
    __slots__ = ["project_id", "add_key_values", "remove_key_values"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    add_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    remove_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, project_id: _Optional[str] = ..., add_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., remove_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class UpdateProjectKeyValuesResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectDataClassRequest(_message.Message):
    __slots__ = ["project_id", "data_class"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    data_class: _models_pb2.DataClass
    def __init__(self, project_id: _Optional[str] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ...) -> None: ...

class UpdateProjectDataClassResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class ArchiveProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ArchiveProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...

class UpdateProjectLicensesRequest(_message.Message):
    __slots__ = ["project_id", "metadata_license_tag", "default_data_license_tag"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, project_id: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class UpdateProjectLicensesResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _models_pb2.Project
    def __init__(self, project: _Optional[_Union[_models_pb2.Project, _Mapping]] = ...) -> None: ...
