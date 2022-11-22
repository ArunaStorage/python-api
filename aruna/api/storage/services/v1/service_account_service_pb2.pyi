from aruna.api.storage.models.v1 import auth_pb2 as _auth_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ["name", "permission", "project_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    permission: _auth_pb2.Permission
    project_id: str
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., permission: _Optional[_Union[_auth_pb2.Permission, str]] = ...) -> None: ...

class CreateServiceAccountResponse(_message.Message):
    __slots__ = ["service_account"]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class CreateServiceAccountTokenRequest(_message.Message):
    __slots__ = ["collection_id", "expires_at", "name", "permission", "svc_account_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    expires_at: _timestamp_pb2.Timestamp
    name: str
    permission: _auth_pb2.Permission
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., permission: _Optional[_Union[_auth_pb2.Permission, str]] = ...) -> None: ...

class CreateServiceAccountTokenResponse(_message.Message):
    __slots__ = ["token", "token_secret"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.Token
    token_secret: str
    def __init__(self, token: _Optional[_Union[_auth_pb2.Token, _Mapping]] = ..., token_secret: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ["svc_account_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteServiceAccountTokenRequest(_message.Message):
    __slots__ = ["svc_account_id", "token_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    token_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountTokenResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteServiceAccountTokensRequest(_message.Message):
    __slots__ = ["svc_account_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountTokensResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EditServiceAccountPermissionRequest(_message.Message):
    __slots__ = ["new_permission", "svc_account_id"]
    NEW_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    new_permission: _auth_pb2.Permission
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., new_permission: _Optional[_Union[_auth_pb2.Permission, str]] = ...) -> None: ...

class EditServiceAccountPermissionResponse(_message.Message):
    __slots__ = ["service_account"]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class GetServiceAccountTokenRequest(_message.Message):
    __slots__ = ["svc_account_id", "token_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    token_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _auth_pb2.Token
    def __init__(self, token: _Optional[_Union[_auth_pb2.Token, _Mapping]] = ...) -> None: ...

class GetServiceAccountTokensRequest(_message.Message):
    __slots__ = ["svc_account_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokensResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _containers.RepeatedCompositeFieldContainer[_auth_pb2.Token]
    def __init__(self, token: _Optional[_Iterable[_Union[_auth_pb2.Token, _Mapping]]] = ...) -> None: ...

class GetServiceAccountsByProjectRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountsByProjectResponse(_message.Message):
    __slots__ = ["svc_accounts"]
    SVC_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    svc_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    def __init__(self, svc_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]] = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ["name", "permission", "project_id", "svc_account_id"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    permission: _auth_pb2.Permission
    project_id: str
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., project_id: _Optional[str] = ..., name: _Optional[str] = ..., permission: _Optional[_Union[_auth_pb2.Permission, str]] = ...) -> None: ...
