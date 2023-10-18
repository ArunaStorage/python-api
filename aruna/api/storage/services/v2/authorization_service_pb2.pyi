from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserPermission(_message.Message):
    __slots__ = ["user_id", "user_name", "permission_level"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_name: str
    permission_level: _models_pb2.PermissionLevel
    def __init__(self, user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., permission_level: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class ResourceAuthorization(_message.Message):
    __slots__ = ["resource_id", "user_permission"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    user_permission: _containers.RepeatedCompositeFieldContainer[UserPermission]
    def __init__(self, resource_id: _Optional[str] = ..., user_permission: _Optional[_Iterable[_Union[UserPermission, _Mapping]]] = ...) -> None: ...

class CreateAuthorizationRequest(_message.Message):
    __slots__ = ["resource_id", "user_id", "permission_level"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    user_id: str
    permission_level: _models_pb2.PermissionLevel
    def __init__(self, resource_id: _Optional[str] = ..., user_id: _Optional[str] = ..., permission_level: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class CreateAuthorizationResponse(_message.Message):
    __slots__ = ["resource_id", "user_id", "user_name", "permission_level"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    user_id: str
    user_name: str
    permission_level: _models_pb2.PermissionLevel
    def __init__(self, resource_id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., permission_level: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class GetAuthorizationsRequest(_message.Message):
    __slots__ = ["resource_id", "recursive"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    recursive: bool
    def __init__(self, resource_id: _Optional[str] = ..., recursive: bool = ...) -> None: ...

class GetAuthorizationsResponse(_message.Message):
    __slots__ = ["authorizations"]
    AUTHORIZATIONS_FIELD_NUMBER: _ClassVar[int]
    authorizations: _containers.RepeatedCompositeFieldContainer[ResourceAuthorization]
    def __init__(self, authorizations: _Optional[_Iterable[_Union[ResourceAuthorization, _Mapping]]] = ...) -> None: ...

class DeleteAuthorizationRequest(_message.Message):
    __slots__ = ["resource_id", "user_id"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    user_id: str
    def __init__(self, resource_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DeleteAuthorizationResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAuthorizationRequest(_message.Message):
    __slots__ = ["resource_id", "user_id", "permission_level"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    user_id: str
    permission_level: _models_pb2.PermissionLevel
    def __init__(self, resource_id: _Optional[str] = ..., user_id: _Optional[str] = ..., permission_level: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class UpdateAuthorizationResponse(_message.Message):
    __slots__ = ["user_permission"]
    USER_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    user_permission: UserPermission
    def __init__(self, user_permission: _Optional[_Union[UserPermission, _Mapping]] = ...) -> None: ...
