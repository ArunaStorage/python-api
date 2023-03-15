from google.api import visibility_pb2 as _visibility_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
ID_TYPE_PATH: IdType
ID_TYPE_UNSPECIFIED: IdType
ID_TYPE_UUID: IdType

class Authorization(_message.Message):
    __slots__ = ["accesskey", "secretkey"]
    ACCESSKEY_FIELD_NUMBER: _ClassVar[int]
    SECRETKEY_FIELD_NUMBER: _ClassVar[int]
    accesskey: str
    secretkey: str
    def __init__(self, secretkey: _Optional[str] = ..., accesskey: _Optional[str] = ...) -> None: ...

class AuthorizeRequest(_message.Message):
    __slots__ = ["authorization", "identifier", "resource", "resource_action"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ACTION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    authorization: Authorization
    identifier: Identifier
    resource: _models_pb2.ResourceType
    resource_action: _models_pb2.ResourceAction
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., identifier: _Optional[_Union[Identifier, _Mapping]] = ..., resource_action: _Optional[_Union[_models_pb2.ResourceAction, str]] = ..., authorization: _Optional[_Union[Authorization, _Mapping]] = ...) -> None: ...

class AuthorizeResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class GetSecretRequest(_message.Message):
    __slots__ = ["accesskey"]
    ACCESSKEY_FIELD_NUMBER: _ClassVar[int]
    accesskey: str
    def __init__(self, accesskey: _Optional[str] = ...) -> None: ...

class GetSecretResponse(_message.Message):
    __slots__ = ["authorization"]
    AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    authorization: Authorization
    def __init__(self, authorization: _Optional[_Union[Authorization, _Mapping]] = ...) -> None: ...

class Identifier(_message.Message):
    __slots__ = ["idtype", "name"]
    IDTYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    idtype: IdType
    name: str
    def __init__(self, name: _Optional[str] = ..., idtype: _Optional[_Union[IdType, str]] = ...) -> None: ...

class IdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
