from google.protobuf import timestamp_pb2 as _timestamp_pb2
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
    __slots__ = ["archive_type", "expires_at", "filename", "object_ids"]
    ARCHIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    archive_type: ArchiveType
    expires_at: _timestamp_pb2.Timestamp
    filename: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_ids: _Optional[_Iterable[str]] = ..., filename: _Optional[str] = ..., archive_type: _Optional[_Union[ArchiveType, str]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateBundleResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DeleteBundleRequest(_message.Message):
    __slots__ = ["bundle_id"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class DeleteBundleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ArchiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
