from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LabelFilter(_message.Message):
    __slots__ = ["and_or_or", "keys_only", "labels"]
    AND_OR_OR_FIELD_NUMBER: _ClassVar[int]
    KEYS_ONLY_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    and_or_or: bool
    keys_only: bool
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., and_or_or: bool = ..., keys_only: bool = ...) -> None: ...

class LabelOrIDQuery(_message.Message):
    __slots__ = ["ids", "labels"]
    IDS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    labels: LabelFilter
    def __init__(self, labels: _Optional[_Union[LabelFilter, _Mapping]] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ["last_uuid", "page_size"]
    LAST_UUID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    last_uuid: str
    page_size: int
    def __init__(self, last_uuid: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...
