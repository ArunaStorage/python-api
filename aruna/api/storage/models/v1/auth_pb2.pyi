from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
PERMISSION_ADMIN: Permission
PERMISSION_APPEND: Permission
PERMISSION_MODIFY: Permission
PERMISSION_NONE: Permission
PERMISSION_READ: Permission
PERMISSION_UNSPECIFIED: Permission
PERM_TYPE_ANONYMOUS: PermType
PERM_TYPE_TOKEN: PermType
PERM_TYPE_UNSPECIFIED: PermType
PERM_TYPE_USER: PermType
TOKEN_TYPE_PERSONAL: TokenType
TOKEN_TYPE_SCOPED: TokenType
TOKEN_TYPE_UNSPECIFIED: TokenType

class Project(_message.Message):
    __slots__ = ["collection_ids", "description", "id", "name", "user_permissions"]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    description: str
    id: str
    name: str
    user_permissions: _containers.RepeatedCompositeFieldContainer[ProjectPermission]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., user_permissions: _Optional[_Iterable[_Union[ProjectPermission, _Mapping]]] = ..., collection_ids: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

class ProjectOverview(_message.Message):
    __slots__ = ["collection_ids", "description", "id", "name", "user_ids"]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    description: str
    id: str
    name: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., collection_ids: _Optional[_Iterable[str]] = ..., user_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ProjectPermission(_message.Message):
    __slots__ = ["permission", "project_id", "service_account", "user_id"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    permission: Permission
    project_id: str
    service_account: bool
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., project_id: _Optional[str] = ..., permission: _Optional[_Union[Permission, str]] = ..., service_account: bool = ...) -> None: ...

class ProjectPermissionDisplayName(_message.Message):
    __slots__ = ["display_name", "permission", "project_id", "user_id"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    permission: Permission
    project_id: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., project_id: _Optional[str] = ..., permission: _Optional[_Union[Permission, str]] = ..., display_name: _Optional[str] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["collection_id", "created_at", "expires_at", "id", "name", "permission", "project_id", "token_type"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    id: str
    name: str
    permission: Permission
    project_id: str
    token_type: TokenType
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., token_type: _Optional[_Union[TokenType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., collection_id: _Optional[str] = ..., project_id: _Optional[str] = ..., permission: _Optional[_Union[Permission, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["active", "display_name", "external_id", "id", "is_admin"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    active: bool
    display_name: str
    external_id: str
    id: str
    is_admin: bool
    def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., display_name: _Optional[str] = ..., active: bool = ..., is_admin: bool = ...) -> None: ...

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PermType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TokenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
