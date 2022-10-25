from aruna.api.storage.models.v1 import auth_pb2 as _auth_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ActivateUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAPITokenRequest(_message.Message):
    __slots__ = ["collection_id", "expires_at", "name", "permission", "project_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    expires_at: ExpiresAt
    name: str
    permission: _auth_pb2.Permission
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[ExpiresAt, _Mapping]] = ..., permission: _Optional[_Union[_auth_pb2.Permission, str]] = ...) -> None: ...

class CreateAPITokenResponse(_message.Message):
    __slots__ = ["token", "token_secret"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.Token
    token_secret: str
    def __init__(self, token: _Optional[_Union[_auth_pb2.Token, _Mapping]] = ..., token_secret: _Optional[str] = ...) -> None: ...

class DeleteAPITokenRequest(_message.Message):
    __slots__ = ["token_id"]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class DeleteAPITokenResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteAPITokensRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DeleteAPITokensResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExpiresAt(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAPITokenRequest(_message.Message):
    __slots__ = ["token_id"]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class GetAPITokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.Token
    def __init__(self, token: _Optional[_Union[_auth_pb2.Token, _Mapping]] = ...) -> None: ...

class GetAPITokensRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAPITokensResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Token]
    def __init__(self, token: _Optional[_Iterable[_Union[_auth_pb2.Token, _Mapping]]] = ...) -> None: ...

class GetNotActivatedUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNotActivatedUsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_auth_pb2.User]
    def __init__(self, users: _Optional[_Iterable[_Union[_auth_pb2.User, _Mapping]]] = ...) -> None: ...

class GetUserProjectsRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserProjectsResponse(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[UserProject]
    def __init__(self, projects: _Optional[_Iterable[_Union[UserProject, _Mapping]]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["project_permissions", "user"]
    PROJECT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    project_permissions: _containers.RepeatedCompositeFieldContainer[_auth_pb2.ProjectPermission]
    user: _auth_pb2.User
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ..., project_permissions: _Optional[_Iterable[_Union[_auth_pb2.ProjectPermission, _Mapping]]] = ...) -> None: ...

class RegisterUserRequest(_message.Message):
    __slots__ = ["display_name"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    def __init__(self, display_name: _Optional[str] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UpdateUserDisplayNameRequest(_message.Message):
    __slots__ = ["new_display_name"]
    NEW_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    new_display_name: str
    def __init__(self, new_display_name: _Optional[str] = ...) -> None: ...

class UpdateUserDisplayNameResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _auth_pb2.User
    def __init__(self, user: _Optional[_Union[_auth_pb2.User, _Mapping]] = ...) -> None: ...

class UserProject(_message.Message):
    __slots__ = ["description", "id", "name"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
