from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBundleRequest(_message.Message):
    __slots__ = ("resource_ids", "filename", "expires_at")
    RESOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    resource_ids: _containers.RepeatedScalarFieldContainer[str]
    filename: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, resource_ids: _Optional[_Iterable[str]] = ..., filename: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateBundleResponse(_message.Message):
    __slots__ = ("bundle_id", "bundle_url")
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_URL_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    bundle_url: str
    def __init__(self, bundle_id: _Optional[str] = ..., bundle_url: _Optional[str] = ...) -> None: ...

class DeleteBundleRequest(_message.Message):
    __slots__ = ("bundle_id",)
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class DeleteBundleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
