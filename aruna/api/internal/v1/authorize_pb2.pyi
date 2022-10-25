from google.api import visibility_pb2 as _visibility_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Authorization(_message.Message):
    __slots__ = ["accesskey", "is_token", "secretkey"]
    ACCESSKEY_FIELD_NUMBER: _ClassVar[int]
    IS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SECRETKEY_FIELD_NUMBER: _ClassVar[int]
    accesskey: str
    is_token: bool
    secretkey: str
    def __init__(self, secretkey: _Optional[str] = ..., accesskey: _Optional[str] = ..., is_token: bool = ...) -> None: ...

class AuthorizeRequest(_message.Message):
    __slots__ = ["resource", "resource_action", "resource_id"]
    RESOURCE_ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource: _models_pb2.ResourceType
    resource_action: _models_pb2.ResourceAction
    resource_id: str
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., resource_action: _Optional[_Union[_models_pb2.ResourceAction, str]] = ...) -> None: ...

class AuthorizeResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...
