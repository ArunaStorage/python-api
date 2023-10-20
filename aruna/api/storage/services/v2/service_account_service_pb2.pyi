from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ["name", "permission"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    permission: _models_pb2.Permission
    def __init__(self, name: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ["svc_account_id", "name", "permission"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    name: str
    permission: _models_pb2.Permission
    def __init__(self, svc_account_id: _Optional[str] = ..., name: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ...) -> None: ...

class CreateServiceAccountResponse(_message.Message):
    __slots__ = ["service_account"]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class CreateServiceAccountTokenRequest(_message.Message):
    __slots__ = ["svc_account_id", "permission", "name", "expires_at"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    permission: _models_pb2.Permission
    name: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, svc_account_id: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ..., name: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateServiceAccountTokenResponse(_message.Message):
    __slots__ = ["token", "token_secret"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
    token: _models_pb2.Token
    token_secret: str
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ..., token_secret: _Optional[str] = ...) -> None: ...

class SetServiceAccountPermissionRequest(_message.Message):
    __slots__ = ["svc_account_id", "permission"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    permission: _models_pb2.Permission
    def __init__(self, svc_account_id: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ...) -> None: ...

class SetServiceAccountPermissionResponse(_message.Message):
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
    token: _models_pb2.Token
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ...) -> None: ...

class GetServiceAccountTokensRequest(_message.Message):
    __slots__ = ["svc_account_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokensResponse(_message.Message):
    __slots__ = ["tokens"]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_models_pb2.Token]
    def __init__(self, tokens: _Optional[_Iterable[_Union[_models_pb2.Token, _Mapping]]] = ...) -> None: ...

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

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ["svc_account_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetS3CredentialsSvcAccountRequest(_message.Message):
    __slots__ = ["svc_account_id", "endpoint_id"]
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetS3CredentialsSvcAccountResponse(_message.Message):
    __slots__ = ["s3_access_key", "s3_secret_key", "s3_endpoint_url"]
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    s3_access_key: str
    s3_secret_key: str
    s3_endpoint_url: str
    def __init__(self, s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., s3_endpoint_url: _Optional[str] = ...) -> None: ...

class GetDataproxyTokenSvcAccountRequest(_message.Message):
    __slots__ = ["user_id", "endpoint_id", "context"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    endpoint_id: str
    context: _models_pb2.Context
    def __init__(self, user_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., context: _Optional[_Union[_models_pb2.Context, _Mapping]] = ...) -> None: ...

class GetDataproxyTokenSvcAccountResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
