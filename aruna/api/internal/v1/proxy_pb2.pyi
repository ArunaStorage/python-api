from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.internal.v1 import authorize_pb2 as _authorize_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
LOCATION_TYPE_FILE: LocationType
LOCATION_TYPE_S3: LocationType
LOCATION_TYPE_UNSPECIFIED: LocationType

class CreateBucketRequest(_message.Message):
    __slots__ = ["bucket_name"]
    BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
    bucket_name: str
    def __init__(self, bucket_name: _Optional[str] = ...) -> None: ...

class CreateBucketResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreatePresignedDownloadRequest(_message.Message):
    __slots__ = ["filename", "is_public", "location", "range"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    filename: str
    is_public: bool
    location: Location
    range: Range
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., is_public: bool = ..., range: _Optional[_Union[Range, _Mapping]] = ..., filename: _Optional[str] = ...) -> None: ...

class CreatePresignedDownloadResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CreatePresignedUploadUrlRequest(_message.Message):
    __slots__ = ["location", "multipart", "part_number", "upload_id"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    location: Location
    multipart: bool
    part_number: int
    upload_id: str
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., multipart: bool = ...) -> None: ...

class CreatePresignedUploadUrlResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ["location"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: Location
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinalizeObjectRequest(_message.Message):
    __slots__ = ["before_location", "final_location", "hashes"]
    BEFORE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    FINAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    before_location: Location
    final_location: Location
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    def __init__(self, before_location: _Optional[_Union[Location, _Mapping]] = ..., final_location: _Optional[_Union[Location, _Mapping]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ...) -> None: ...

class FinalizeObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishPresignedUploadRequest(_message.Message):
    __slots__ = ["bucket", "key", "multipart", "part_etags", "upload_id"]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    PART_ETAGS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    key: str
    multipart: bool
    part_etags: _containers.RepeatedCompositeFieldContainer[PartETag]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., part_etags: _Optional[_Iterable[_Union[PartETag, _Mapping]]] = ..., bucket: _Optional[str] = ..., key: _Optional[str] = ..., multipart: bool = ...) -> None: ...

class FinishPresignedUploadResponse(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class GetEncryptionKeyRequest(_message.Message):
    __slots__ = ["identifier"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    identifier: _authorize_pb2.Identifier
    def __init__(self, identifier: _Optional[_Union[_authorize_pb2.Identifier, _Mapping]] = ...) -> None: ...

class GetEncryptionKeyResponse(_message.Message):
    __slots__ = ["encryption_key"]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    encryption_key: str
    def __init__(self, encryption_key: _Optional[str] = ...) -> None: ...

class InitPresignedUploadRequest(_message.Message):
    __slots__ = ["location", "multipart"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    location: Location
    multipart: bool
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ..., multipart: bool = ...) -> None: ...

class InitPresignedUploadResponse(_message.Message):
    __slots__ = ["upload_id"]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["bucket", "path", "type"]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    path: str
    type: LocationType
    def __init__(self, type: _Optional[_Union[LocationType, str]] = ..., bucket: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class MoveObjectRequest(_message.Message):
    __slots__ = ["to"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: Location
    def __init__(self, to: _Optional[_Union[Location, _Mapping]] = ..., **kwargs) -> None: ...

class MoveObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PartETag(_message.Message):
    __slots__ = ["etag", "part_number"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    etag: str
    part_number: int
    def __init__(self, part_number: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...

class Range(_message.Message):
    __slots__ = ["end", "start"]
    END_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    end: int
    start: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...

class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
