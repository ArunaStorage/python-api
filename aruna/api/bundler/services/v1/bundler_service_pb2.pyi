from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ARCHIVE_TYPE_TAR_GZ: ArchiveType
ARCHIVE_TYPE_TAR_ZST: ArchiveType
ARCHIVE_TYPE_UNSPECIFIED: ArchiveType
ARCHIVE_TYPE_ZIP: ArchiveType
DESCRIPTOR: _descriptor.FileDescriptor

class CreateBundleRequest(_message.Message):
    __slots__ = ["archive_type", "collection_id", "endpoint_id", "expires_at", "filename", "object_ids"]
    ARCHIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    archive_type: ArchiveType
    collection_id: str
    endpoint_id: str
    expires_at: _timestamp_pb2.Timestamp
    filename: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ..., filename: _Optional[str] = ..., archive_type: _Optional[_Union[ArchiveType, str]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class CreateBundleResponse(_message.Message):
    __slots__ = ["bundle_id", "url"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    url: str
    def __init__(self, bundle_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class DeleteBundleRequest(_message.Message):
    __slots__ = ["bundle_id", "collection_id"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ..., bundle_id: _Optional[str] = ...) -> None: ...

class DeleteBundleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ArchiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
