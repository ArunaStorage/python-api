from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as _dataset_pb2
from sciobjsdb.api.storage.models.v1 import projects_pb2 as _projects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddUserToProjectRequest(_message.Message):
    __slots__ = ["project_id", "scope", "user_id"]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    SCOPE_FIELD_NUMBER: ClassVar[int]
    USER_ID_FIELD_NUMBER: ClassVar[int]
    project_id: str
    scope: _containers.RepeatedScalarFieldContainer[_common_models_pb2.Right]
    user_id: str
    def __init__(self, user_id: Optional[str] = ..., scope: Optional[Iterable[Union[_common_models_pb2.Right, str]]] = ..., project_id: Optional[str] = ...) -> None: ...

class AddUserToProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAPITokenRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class CreateAPITokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    token: _common_models_pb2.APIToken
    def __init__(self, token: Optional[Union[_common_models_pb2.APIToken, Mapping]] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ["annotations", "description", "labels", "name"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    name: str
    def __init__(self, name: Optional[str] = ..., description: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteAPITokenRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteAPITokenResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAPITokenRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAPITokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    token: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.APIToken]
    def __init__(self, token: Optional[Iterable[Union[_common_models_pb2.APIToken, Mapping]]] = ...) -> None: ...

class GetProjectDatasetsRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetProjectDatasetsResponse(_message.Message):
    __slots__ = ["datasets"]
    DATASETS_FIELD_NUMBER: ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    def __init__(self, datasets: Optional[Iterable[Union[_dataset_pb2.Dataset, Mapping]]] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: ClassVar[int]
    project: _projects_pb2.Project
    def __init__(self, project: Optional[Union[_projects_pb2.Project, Mapping]] = ...) -> None: ...

class GetUserProjectsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetUserProjectsResponse(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_projects_pb2.Project]
    def __init__(self, projects: Optional[Iterable[Union[_projects_pb2.Project, Mapping]]] = ...) -> None: ...
