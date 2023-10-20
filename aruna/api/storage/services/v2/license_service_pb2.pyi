from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateLicenseRequest(_message.Message):
    __slots__ = ["tag", "name", "text", "url"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    tag: str
    name: str
    text: str
    url: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CreateLicenseResponse(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class GetLicenseRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class GetLicenseResponse(_message.Message):
    __slots__ = ["license"]
    LICENSE_FIELD_NUMBER: _ClassVar[int]
    license: _models_pb2.License
    def __init__(self, license: _Optional[_Union[_models_pb2.License, _Mapping]] = ...) -> None: ...

class ListLicensesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListLicensesResponse(_message.Message):
    __slots__ = ["licenses"]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    licenses: _containers.RepeatedCompositeFieldContainer[_models_pb2.License]
    def __init__(self, licenses: _Optional[_Iterable[_Union[_models_pb2.License, _Mapping]]] = ...) -> None: ...
