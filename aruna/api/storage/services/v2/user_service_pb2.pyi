from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REFERENCE_TYPE_UNSPECIFIED: _ClassVar[ReferenceType]
    REFERENCE_TYPE_USER: _ClassVar[ReferenceType]
    REFERENCE_TYPE_RESOURCE: _ClassVar[ReferenceType]

class PersonalNotificationVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PERSONAL_NOTIFICATION_VARIANT_UNSPECIFIED: _ClassVar[PersonalNotificationVariant]
    PERSONAL_NOTIFICATION_VARIANT_ACCESS_REQUESTED: _ClassVar[PersonalNotificationVariant]
    PERSONAL_NOTIFICATION_VARIANT_PERMISSION_GRANTED: _ClassVar[PersonalNotificationVariant]
    PERSONAL_NOTIFICATION_VARIANT_PERMISSION_REVOKED: _ClassVar[PersonalNotificationVariant]
    PERSONAL_NOTIFICATION_VARIANT_PERMISSION_UPDATED: _ClassVar[PersonalNotificationVariant]
    PERSONAL_NOTIFICATION_VARIANT_ANNOUNCEMENT: _ClassVar[PersonalNotificationVariant]
REFERENCE_TYPE_UNSPECIFIED: ReferenceType
REFERENCE_TYPE_USER: ReferenceType
REFERENCE_TYPE_RESOURCE: ReferenceType
PERSONAL_NOTIFICATION_VARIANT_UNSPECIFIED: PersonalNotificationVariant
PERSONAL_NOTIFICATION_VARIANT_ACCESS_REQUESTED: PersonalNotificationVariant
PERSONAL_NOTIFICATION_VARIANT_PERMISSION_GRANTED: PersonalNotificationVariant
PERSONAL_NOTIFICATION_VARIANT_PERMISSION_REVOKED: PersonalNotificationVariant
PERSONAL_NOTIFICATION_VARIANT_PERMISSION_UPDATED: PersonalNotificationVariant
PERSONAL_NOTIFICATION_VARIANT_ANNOUNCEMENT: PersonalNotificationVariant

class RegisterUserRequest(_message.Message):
    __slots__ = ["display_name", "email", "project"]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    email: str
    project: str
    def __init__(self, display_name: _Optional[str] = ..., email: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class RegisterUserResponse(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class CreateAPITokenRequest(_message.Message):
    __slots__ = ["name", "permission", "expires_at"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    name: str
    permission: _models_pb2.Permission
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., permission: _Optional[_Union[_models_pb2.Permission, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAPITokenResponse(_message.Message):
    __slots__ = ["token", "token_secret"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
    token: _models_pb2.Token
    token_secret: str
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ..., token_secret: _Optional[str] = ...) -> None: ...

class GetAPITokenRequest(_message.Message):
    __slots__ = ["token_id"]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: str
    def __init__(self, token_id: _Optional[str] = ...) -> None: ...

class GetAPITokenResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: _models_pb2.Token
    def __init__(self, token: _Optional[_Union[_models_pb2.Token, _Mapping]] = ...) -> None: ...

class GetAPITokensRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAPITokensResponse(_message.Message):
    __slots__ = ["tokens"]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_models_pb2.Token]
    def __init__(self, tokens: _Optional[_Iterable[_Union[_models_pb2.Token, _Mapping]]] = ...) -> None: ...

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

class GetUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _models_pb2.User
    def __init__(self, user: _Optional[_Union[_models_pb2.User, _Mapping]] = ...) -> None: ...

class GetUserRedactedRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class GetUserRedactedResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _models_pb2.User
    def __init__(self, user: _Optional[_Union[_models_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateUserDisplayNameRequest(_message.Message):
    __slots__ = ["new_display_name"]
    NEW_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    new_display_name: str
    def __init__(self, new_display_name: _Optional[str] = ...) -> None: ...

class UpdateUserDisplayNameResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _models_pb2.User
    def __init__(self, user: _Optional[_Union[_models_pb2.User, _Mapping]] = ...) -> None: ...

class ActivateUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ActivateUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNotActivatedUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetNotActivatedUsersResponse(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_models_pb2.User]
    def __init__(self, users: _Optional[_Iterable[_Union[_models_pb2.User, _Mapping]]] = ...) -> None: ...

class GetAllUsersRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllUsersResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[_models_pb2.User]
    def __init__(self, user: _Optional[_Iterable[_Union[_models_pb2.User, _Mapping]]] = ...) -> None: ...

class DeactivateUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DeactivateUserResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateUserEmailRequest(_message.Message):
    __slots__ = ["user_id", "new_email"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    new_email: str
    def __init__(self, user_id: _Optional[str] = ..., new_email: _Optional[str] = ...) -> None: ...

class UpdateUserEmailResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _models_pb2.User
    def __init__(self, user: _Optional[_Union[_models_pb2.User, _Mapping]] = ...) -> None: ...

class GetS3CredentialsUserRequest(_message.Message):
    __slots__ = ["user_id", "endpoint_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    endpoint_id: str
    def __init__(self, user_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetS3CredentialsUserResponse(_message.Message):
    __slots__ = ["s3_access_key", "s3_secret_key", "s3_endpoint_url"]
    S3_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    S3_ENDPOINT_URL_FIELD_NUMBER: _ClassVar[int]
    s3_access_key: str
    s3_secret_key: str
    s3_endpoint_url: str
    def __init__(self, s3_access_key: _Optional[str] = ..., s3_secret_key: _Optional[str] = ..., s3_endpoint_url: _Optional[str] = ...) -> None: ...

class GetDataproxyTokenUserRequest(_message.Message):
    __slots__ = ["user_id", "endpoint_id", "context"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    endpoint_id: str
    context: _models_pb2.Context
    def __init__(self, user_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., context: _Optional[_Union[_models_pb2.Context, _Mapping]] = ...) -> None: ...

class GetDataproxyTokenUserResponse(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class GetPersonalNotificationsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPersonalNotificationsResponse(_message.Message):
    __slots__ = ["notifications"]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[PersonalNotification]
    def __init__(self, notifications: _Optional[_Iterable[_Union[PersonalNotification, _Mapping]]] = ...) -> None: ...

class AcknowledgePersonalNotificationsRequest(_message.Message):
    __slots__ = ["notification_ids"]
    NOTIFICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    notification_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, notification_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AcknowledgePersonalNotificationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Reference(_message.Message):
    __slots__ = ["ref_type", "ref_name", "ref_value"]
    REF_TYPE_FIELD_NUMBER: _ClassVar[int]
    REF_NAME_FIELD_NUMBER: _ClassVar[int]
    REF_VALUE_FIELD_NUMBER: _ClassVar[int]
    ref_type: ReferenceType
    ref_name: str
    ref_value: str
    def __init__(self, ref_type: _Optional[_Union[ReferenceType, str]] = ..., ref_name: _Optional[str] = ..., ref_value: _Optional[str] = ...) -> None: ...

class PersonalNotification(_message.Message):
    __slots__ = ["id", "variant", "message", "refs"]
    ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REFS_FIELD_NUMBER: _ClassVar[int]
    id: str
    variant: PersonalNotificationVariant
    message: str
    refs: _containers.RepeatedCompositeFieldContainer[Reference]
    def __init__(self, id: _Optional[str] = ..., variant: _Optional[_Union[PersonalNotificationVariant, str]] = ..., message: _Optional[str] = ..., refs: _Optional[_Iterable[_Union[Reference, _Mapping]]] = ...) -> None: ...
