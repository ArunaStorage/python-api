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
    __slots__ = ("name", "project_id", "permission_level")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    name: str
    project_id: str
    permission_level: _models_pb2.PermissionLevel
    def __init__(self, name: _Optional[str] = ..., project_id: _Optional[str] = ..., permission_level: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class ServiceAccount(_message.Message):
    __slots__ = ("svc_account_id", "name", "permission")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    name: str
    permission: _models_pb2.Permission
    def __init__(self, svc_account_id: _Optional[str] = ..., name: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ...) -> None: ...

class CreateServiceAccountResponse(_message.Message):
    __slots__ = ("service_account",)
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    service_account: ServiceAccount
    def __init__(self, service_account: _Optional[_Union[ServiceAccount, _Mapping]] = ...) -> None: ...

class CreateServiceAccountTokenRequest(_message.Message):
    __slots__ = ("svc_account_id", "permission", "name", "expires_at")
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
    __slots__ = ("token", "token_secret")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
    token: _models_pb2.Token
    token_secret: str
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ..., token_secret: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokenRequest(_message.Message):
    __slots__ = ("svc_account_id", "token_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    token_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _models_pb2.Token
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ...) -> None: ...

class GetServiceAccountTokensRequest(_message.Message):
    __slots__ = ("svc_account_id",)
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class GetServiceAccountTokensResponse(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_models_pb2.Token]
    def __init__(self, tokens: _Optional[_Iterable[_Union[_models_pb2.Token, _Mapping]]] = ...) -> None: ...

class DeleteServiceAccountTokenRequest(_message.Message):
    __slots__ = ("svc_account_id", "token_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    token_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountTokenResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteServiceAccountTokensRequest(_message.Message):
    __slots__ = ("svc_account_id",)
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountTokensResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ("svc_account_id",)
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    def __init__(self, svc_account_id: _Optional[str] = ...) -> None: ...

class DeleteServiceAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateS3CredentialsSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class CreateS3CredentialsSvcAccountResponse(_message.Message):
    __slots__ = ("s3_access_key", "s3_secret_key", "s3_endpoint_url")
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    s3_access_key: str
    s3_secret_key: str
    s3_endpoint_url: str
    def __init__(self, s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., s3_endpoint_url: _Optional[str] = ...) -> None: ...

class GetS3CredentialsSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetS3CredentialsSvcAccountResponse(_message.Message):
    __slots__ = ("s3_access_key", "s3_secret_key", "s3_endpoint_url")
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    s3_access_key: str
    s3_secret_key: str
    s3_endpoint_url: str
    def __init__(self, s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., s3_endpoint_url: _Optional[str] = ...) -> None: ...

class DeleteS3CredentialsSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class DeleteS3CredentialsSvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateDataproxyTokenSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "context", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    context: _models_pb2.Context
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., context: _Optional[_Union[_models_pb2.Context, _Mapping]] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class CreateDataproxyTokenSvcAccountResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class AddPubkeySvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "public_key")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    public_key: str
    def __init__(self, svc_account_id: _Optional[str] = ..., public_key: _Optional[str] = ...) -> None: ...

class AddPubkeySvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddTrustedEndpointsSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class AddTrustedEndpointsSvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveTrustedEndpointsSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "endpoint_id")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    endpoint_id: str
    def __init__(self, svc_account_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class RemoveTrustedEndpointsSvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddDataProxyAttributeSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "attribute")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    attribute: _models_pb2.DataProxyAttribute
    def __init__(self, svc_account_id: _Optional[str] = ..., attribute: _Optional[_Union[_models_pb2.DataProxyAttribute, _Mapping]] = ...) -> None: ...

class AddDataProxyAttributeSvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveDataProxyAttributeSvcAccountRequest(_message.Message):
    __slots__ = ("svc_account_id", "dataproxy_id", "attribute_name")
    SVC_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DATAPROXY_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    svc_account_id: str
    dataproxy_id: str
    attribute_name: str
    def __init__(self, svc_account_id: _Optional[str] = ..., dataproxy_id: _Optional[str] = ..., attribute_name: _Optional[str] = ...) -> None: ...

class RemoveDataProxyAttributeSvcAccountResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
