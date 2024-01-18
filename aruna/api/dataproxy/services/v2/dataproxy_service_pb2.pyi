from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLICATION_STATUS_UNSPECIFIED: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_PENDING: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_RUNNING: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_FINISHED: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_ERROR: _ClassVar[ReplicationStatus]
REPLICATION_STATUS_UNSPECIFIED: ReplicationStatus
REPLICATION_STATUS_PENDING: ReplicationStatus
REPLICATION_STATUS_RUNNING: ReplicationStatus
REPLICATION_STATUS_FINISHED: ReplicationStatus
REPLICATION_STATUS_ERROR: ReplicationStatus

class InitMessage(_message.Message):
    __slots__ = ("dataproxy_id", "object_ids")
    DATAPROXY_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    dataproxy_id: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dataproxy_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class InfoAckMessage(_message.Message):
    __slots__ = ("object_id",)
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    def __init__(self, object_id: _Optional[str] = ...) -> None: ...

class ChunkAckMessage(_message.Message):
    __slots__ = ("object_id", "chunk_idx")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_IDX_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    chunk_idx: int
    def __init__(self, object_id: _Optional[str] = ..., chunk_idx: _Optional[int] = ...) -> None: ...

class RetryChunkMessage(_message.Message):
    __slots__ = ("object_id", "chunk_idx")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_IDX_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    chunk_idx: int
    def __init__(self, object_id: _Optional[str] = ..., chunk_idx: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ErrorMessage(_message.Message):
    __slots__ = ("retry_chunk", "abort", "retry_object_id")
    RETRY_CHUNK_FIELD_NUMBER: _ClassVar[int]
    ABORT_FIELD_NUMBER: _ClassVar[int]
    RETRY_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    retry_chunk: RetryChunkMessage
    abort: Empty
    retry_object_id: str
    def __init__(self, retry_chunk: _Optional[_Union[RetryChunkMessage, _Mapping]] = ..., abort: _Optional[_Union[Empty, _Mapping]] = ..., retry_object_id: _Optional[str] = ...) -> None: ...

class PullReplicationRequest(_message.Message):
    __slots__ = ("init_message", "info_ack_message", "chunk_ack_message", "error_message", "finish_message")
    INIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INFO_ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_ACK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FINISH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    init_message: InitMessage
    info_ack_message: InfoAckMessage
    chunk_ack_message: ChunkAckMessage
    error_message: ErrorMessage
    finish_message: Empty
    def __init__(self, init_message: _Optional[_Union[InitMessage, _Mapping]] = ..., info_ack_message: _Optional[_Union[InfoAckMessage, _Mapping]] = ..., chunk_ack_message: _Optional[_Union[ChunkAckMessage, _Mapping]] = ..., error_message: _Optional[_Union[ErrorMessage, _Mapping]] = ..., finish_message: _Optional[_Union[Empty, _Mapping]] = ...) -> None: ...

class ObjectInfo(_message.Message):
    __slots__ = ("object_id", "chunks", "raw_size", "block_list", "extra")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_FIELD_NUMBER: _ClassVar[int]
    RAW_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_LIST_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    chunks: int
    raw_size: int
    block_list: _containers.RepeatedScalarFieldContainer[int]
    extra: str
    def __init__(self, object_id: _Optional[str] = ..., chunks: _Optional[int] = ..., raw_size: _Optional[int] = ..., block_list: _Optional[_Iterable[int]] = ..., extra: _Optional[str] = ...) -> None: ...

class Chunk(_message.Message):
    __slots__ = ("object_id", "chunk_idx", "data", "checksum")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_IDX_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    chunk_idx: int
    data: bytes
    checksum: str
    def __init__(self, object_id: _Optional[str] = ..., chunk_idx: _Optional[int] = ..., data: _Optional[bytes] = ..., checksum: _Optional[str] = ...) -> None: ...

class PullReplicationResponse(_message.Message):
    __slots__ = ("object_info", "chunk", "finish_message")
    OBJECT_INFO_FIELD_NUMBER: _ClassVar[int]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    FINISH_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    object_info: ObjectInfo
    chunk: Chunk
    finish_message: Empty
    def __init__(self, object_info: _Optional[_Union[ObjectInfo, _Mapping]] = ..., chunk: _Optional[_Union[Chunk, _Mapping]] = ..., finish_message: _Optional[_Union[Empty, _Mapping]] = ...) -> None: ...

class DataInfo(_message.Message):
    __slots__ = ("object_id", "download_url", "encryption_key", "is_compressed")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    download_url: str
    encryption_key: str
    is_compressed: bool
    def __init__(self, object_id: _Optional[str] = ..., download_url: _Optional[str] = ..., encryption_key: _Optional[str] = ..., is_compressed: bool = ...) -> None: ...

class DataInfos(_message.Message):
    __slots__ = ("data_info",)
    DATA_INFO_FIELD_NUMBER: _ClassVar[int]
    data_info: _containers.RepeatedCompositeFieldContainer[DataInfo]
    def __init__(self, data_info: _Optional[_Iterable[_Union[DataInfo, _Mapping]]] = ...) -> None: ...

class PushReplicationRequest(_message.Message):
    __slots__ = ("data_infos",)
    DATA_INFOS_FIELD_NUMBER: _ClassVar[int]
    data_infos: DataInfos
    def __init__(self, data_infos: _Optional[_Union[DataInfos, _Mapping]] = ...) -> None: ...

class PushReplicationResponse(_message.Message):
    __slots__ = ("ack",)
    ACK_FIELD_NUMBER: _ClassVar[int]
    ack: bool
    def __init__(self, ack: bool = ...) -> None: ...

class GetCredentialsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCredentialsResponse(_message.Message):
    __slots__ = ("access_key", "secret_key")
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    access_key: str
    secret_key: str
    def __init__(self, access_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class S3Path(_message.Message):
    __slots__ = ("bucket", "key")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    key: str
    def __init__(self, bucket: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...

class PushReplicaRequest(_message.Message):
    __slots__ = ("resource_id", "s3_path", "target_endpoint_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    S3_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    s3_path: S3Path
    target_endpoint_id: str
    def __init__(self, resource_id: _Optional[str] = ..., s3_path: _Optional[_Union[S3Path, _Mapping]] = ..., target_endpoint_id: _Optional[str] = ...) -> None: ...

class PushReplicaResponse(_message.Message):
    __slots__ = ("replication_id",)
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: str
    def __init__(self, replication_id: _Optional[str] = ...) -> None: ...

class PullReplicaRequest(_message.Message):
    __slots__ = ("resource_id", "s3_path")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    S3_PATH_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    s3_path: S3Path
    def __init__(self, resource_id: _Optional[str] = ..., s3_path: _Optional[_Union[S3Path, _Mapping]] = ...) -> None: ...

class PullReplicaResponse(_message.Message):
    __slots__ = ("replication_id",)
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: str
    def __init__(self, replication_id: _Optional[str] = ...) -> None: ...

class ReplicationStatusRequest(_message.Message):
    __slots__ = ("replication_id",)
    REPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    replication_id: str
    def __init__(self, replication_id: _Optional[str] = ...) -> None: ...

class ReplicationStatusResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: ReplicationStatus
    message: str
    def __init__(self, status: _Optional[_Union[ReplicationStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ObjectLocation(_message.Message):
    __slots__ = ("bucket", "key", "upload_id", "content_length")
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    key: str
    upload_id: str
    content_length: str
    def __init__(self, bucket: _Optional[str] = ..., key: _Optional[str] = ..., upload_id: _Optional[str] = ..., content_length: _Optional[str] = ...) -> None: ...

class PutObjectRequest(_message.Message):
    __slots__ = ("location", "data")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    data: bytes
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ..., data: _Optional[bytes] = ...) -> None: ...

class PutObjectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetObjectRequest(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ...) -> None: ...

class GetObjectResponse(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class HeadObjectRequest(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ...) -> None: ...

class HeadObjectResponse(_message.Message):
    __slots__ = ("content_length", "exists")
    CONTENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    content_length: str
    exists: bool
    def __init__(self, content_length: _Optional[str] = ..., exists: bool = ...) -> None: ...

class InitMultiPartUploadRequest(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ...) -> None: ...

class InitMultiPartUploadResponse(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UploadPartRequest(_message.Message):
    __slots__ = ("location", "part_number", "data")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    part_number: int
    data: bytes
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ..., part_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadPartResponse(_message.Message):
    __slots__ = ("etag",)
    ETAG_FIELD_NUMBER: _ClassVar[int]
    etag: str
    def __init__(self, etag: _Optional[str] = ...) -> None: ...

class CompletedPart(_message.Message):
    __slots__ = ("part_number", "etag")
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    part_number: int
    etag: str
    def __init__(self, part_number: _Optional[int] = ..., etag: _Optional[str] = ...) -> None: ...

class CompleteMultiPartUploadRequest(_message.Message):
    __slots__ = ("location", "completed_parts")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PARTS_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    completed_parts: _containers.RepeatedCompositeFieldContainer[CompletedPart]
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ..., completed_parts: _Optional[_Iterable[_Union[CompletedPart, _Mapping]]] = ...) -> None: ...

class CompleteMultiPartUploadResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateBucketRequest(_message.Message):
    __slots__ = ("bucket",)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    def __init__(self, bucket: _Optional[str] = ...) -> None: ...

class CreateBucketResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteBucketRequest(_message.Message):
    __slots__ = ("bucket",)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    def __init__(self, bucket: _Optional[str] = ...) -> None: ...

class DeleteBucketResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitLocationRequest(_message.Message):
    __slots__ = ("object_name", "size", "is_temporary")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    object_name: str
    size: int
    is_temporary: bool
    def __init__(self, object_name: _Optional[str] = ..., size: _Optional[int] = ..., is_temporary: bool = ...) -> None: ...

class InitLocationResponse(_message.Message):
    __slots__ = ("location",)
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    location: ObjectLocation
    def __init__(self, location: _Optional[_Union[ObjectLocation, _Mapping]] = ...) -> None: ...
