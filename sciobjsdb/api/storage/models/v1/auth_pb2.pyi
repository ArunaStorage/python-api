from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTokenRequest(_message.Message):
    __slots__ = ["expires", "resource", "resource_id", "rights"]
    EXPIRES_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
    RIGHTS_FIELD_NUMBER: ClassVar[int]
    expires: _timestamp_pb2.Timestamp
    resource: _common_models_pb2.Resource
    resource_id: str
    rights: _containers.RepeatedScalarFieldContainer[_common_models_pb2.Right]
    def __init__(self, resource_id: Optional[str] = ..., rights: Optional[Iterable[Union[_common_models_pb2.Right, str]]] = ..., resource: Optional[Union[_common_models_pb2.Resource, str]] = ..., expires: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class TokenEntry(_message.Message):
    __slots__ = ["created", "expires", "id", "resource", "token", "user_id"]
    CREATED_FIELD_NUMBER: ClassVar[int]
    EXPIRES_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    USER_ID_FIELD_NUMBER: ClassVar[int]
    created: _timestamp_pb2.Timestamp
    expires: _timestamp_pb2.Timestamp
    id: str
    resource: _common_models_pb2.Resource
    token: str
    user_id: _common_models_pb2.User
    def __init__(self, id: Optional[str] = ..., user_id: Optional[Union[_common_models_pb2.User, Mapping]] = ..., token: Optional[str] = ..., resource: Optional[Union[_common_models_pb2.Resource, str]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., expires: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class TokenList(_message.Message):
    __slots__ = ["project_id", "token"]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    project_id: str
    token: _containers.RepeatedCompositeFieldContainer[TokenEntry]
    def __init__(self, project_id: Optional[str] = ..., token: Optional[Iterable[Union[TokenEntry, Mapping]]] = ...) -> None: ...
