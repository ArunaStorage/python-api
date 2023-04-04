from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.storage.services.v1 import object_service_pb2 as _object_service_pb2
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

class DeleteObjectRequest(_message.Message):
    __slots__ = ["location"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: Location
    def __init__(self, location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinalizeObjectRequest(_message.Message):
    __slots__ = ["collection_id", "content_length", "hashes", "location", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    content_length: int
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    location: Location
    object_id: str
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., content_length: _Optional[int] = ...) -> None: ...

class FinalizeObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishMultipartUploadRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "part_etags", "path", "upload_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PART_ETAGS_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    part_etags: _containers.RepeatedCompositeFieldContainer[PartETag]
    path: str
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., path: _Optional[str] = ..., object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., part_etags: _Optional[_Iterable[_Union[PartETag, _Mapping]]] = ...) -> None: ...

class FinishMultipartUploadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCollectionByBucketRequest(_message.Message):
    __slots__ = ["access_key", "bucket"]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    bucket: str
    def __init__(self, bucket: _Optional[str] = ..., access_key: _Optional[str] = ...) -> None: ...

class GetCollectionByBucketResponse(_message.Message):
    __slots__ = ["collection_id", "project_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class GetObjectLocationRequest(_message.Message):
    __slots__ = ["access_key", "endpoint_id", "path", "revision_id"]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    endpoint_id: str
    path: str
    revision_id: str
    def __init__(self, path: _Optional[str] = ..., revision_id: _Optional[str] = ..., access_key: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetObjectLocationResponse(_message.Message):
    __slots__ = ["location", "object"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    location: Location
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ..., location: _Optional[_Union[Location, _Mapping]] = ...) -> None: ...

class GetOrCreateEncryptionKeyRequest(_message.Message):
    __slots__ = ["endpoint_id", "hash", "path"]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    hash: str
    path: str
    def __init__(self, path: _Optional[str] = ..., hash: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetOrCreateEncryptionKeyResponse(_message.Message):
    __slots__ = ["created", "encryption_key"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    created: bool
    encryption_key: str
    def __init__(self, encryption_key: _Optional[str] = ..., created: bool = ...) -> None: ...

class GetOrCreateObjectByPathRequest(_message.Message):
    __slots__ = ["access_key", "endpoint_id", "get_only", "object", "path"]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    GET_ONLY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    endpoint_id: str
    get_only: bool
    object: _object_service_pb2.StageObject
    path: str
    def __init__(self, path: _Optional[str] = ..., access_key: _Optional[str] = ..., object: _Optional[_Union[_object_service_pb2.StageObject, _Mapping]] = ..., get_only: bool = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetOrCreateObjectByPathResponse(_message.Message):
    __slots__ = ["collection_id", "created", "dataclass", "hashes", "object_id", "revision_number"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DATACLASS_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    created: bool
    dataclass: _models_pb2.DataClass
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    object_id: str
    revision_number: int
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., revision_number: _Optional[int] = ..., created: bool = ...) -> None: ...

class InitMultipartUploadRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "path"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    path: str
    def __init__(self, path: _Optional[str] = ..., object_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class InitMultipartUploadResponse(_message.Message):
    __slots__ = ["upload_id"]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["bucket", "encryption_key", "endpoint_id", "is_compressed", "is_encrypted", "path", "type"]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    IS_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    encryption_key: str
    endpoint_id: str
    is_compressed: bool
    is_encrypted: bool
    path: str
    type: LocationType
    def __init__(self, type: _Optional[_Union[LocationType, str]] = ..., bucket: _Optional[str] = ..., path: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., is_compressed: bool = ..., is_encrypted: bool = ..., encryption_key: _Optional[str] = ...) -> None: ...

class PartETag(_message.Message):
    __slots__ = ["etag", "part_number"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    etag: str
    part_number: int
    def __init__(self, part_number: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...

class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
