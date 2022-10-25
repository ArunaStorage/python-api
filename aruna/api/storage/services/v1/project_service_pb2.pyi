from aruna.api.storage.models.v1 import auth_pb2 as _auth_pb2
from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddUserToProjectRequest(_message.Message):
    __slots__ = ["project_id", "user_permission"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_permission: _auth_pb2.ProjectPermission
    def __init__(self, project_id: _Optional[str] = ..., user_permission: _Optional[_Union[_auth_pb2.ProjectPermission, _Mapping]] = ...) -> None: ...

class AddUserToProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ["description", "name"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class DestroyProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class DestroyProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EditUserPermissionsForProjectRequest(_message.Message):
    __slots__ = ["project_id", "user_permission"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_permission: _auth_pb2.ProjectPermission
    def __init__(self, project_id: _Optional[str] = ..., user_permission: _Optional[_Union[_auth_pb2.ProjectPermission, _Mapping]] = ...) -> None: ...

class EditUserPermissionsForProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class GetProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _auth_pb2.ProjectOverview
    def __init__(self, project: _Optional[_Union[_auth_pb2.ProjectOverview, _Mapping]] = ...) -> None: ...

class GetProjectsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetProjectsResponse(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[_auth_pb2.ProjectOverview]
    def __init__(self, projects: _Optional[_Iterable[_Union[_auth_pb2.ProjectOverview, _Mapping]]] = ...) -> None: ...

class GetUserPermissionsForProjectRequest(_message.Message):
    __slots__ = ["project_id", "user_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_id: str
    def __init__(self, project_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class GetUserPermissionsForProjectResponse(_message.Message):
    __slots__ = ["user_permission"]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    user_permission: _auth_pb2.ProjectPermissionDisplayName
    def __init__(self, user_permission: _Optional[_Union[_auth_pb2.ProjectPermissionDisplayName, _Mapping]] = ...) -> None: ...

class RemoveUserFromProjectRequest(_message.Message):
    __slots__ = ["project_id", "user_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_id: str
    def __init__(self, project_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RemoveUserFromProjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ["description", "name", "project_id"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    name: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateProjectResponse(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: _auth_pb2.ProjectOverview
    def __init__(self, project: _Optional[_Union[_auth_pb2.ProjectOverview, _Mapping]] = ...) -> None: ...
