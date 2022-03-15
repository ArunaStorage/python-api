from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as _object_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteMultipartUploadRequest(_message.Message):
    __slots__ = ["object_id", "parts"]
    OBJECT_ID_FIELD_NUMBER: ClassVar[int]
    PARTS_FIELD_NUMBER: ClassVar[int]
    object_id: str
    parts: _containers.RepeatedCompositeFieldContainer[CompletedParts]
    def __init__(self, object_id: Optional[str] = ..., parts: Optional[Iterable[Union[CompletedParts, Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CompletedParts(_message.Message):
    __slots__ = ["etag", "part"]
    ETAG_FIELD_NUMBER: ClassVar[int]
    PART_FIELD_NUMBER: ClassVar[int]
    etag: str
    part: int
    def __init__(self, etag: Optional[str] = ..., part: Optional[int] = ...) -> None: ...

class CreateDownloadLinkBatchRequest(_message.Message):
    __slots__ = ["requests"]
    REQUESTS_FIELD_NUMBER: ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[CreateDownloadLinkRequest]
    def __init__(self, requests: Optional[Iterable[Union[CreateDownloadLinkRequest, Mapping]]] = ...) -> None: ...

class CreateDownloadLinkBatchResponse(_message.Message):
    __slots__ = ["links"]
    LINKS_FIELD_NUMBER: ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[CreateDownloadLinkResponse]
    def __init__(self, links: Optional[Iterable[Union[CreateDownloadLinkResponse, Mapping]]] = ...) -> None: ...

class CreateDownloadLinkRequest(_message.Message):
    __slots__ = ["id", "range"]
    class Range(_message.Message):
        __slots__ = ["end_byte", "start_byte"]
        END_BYTE_FIELD_NUMBER: ClassVar[int]
        START_BYTE_FIELD_NUMBER: ClassVar[int]
        end_byte: int
        start_byte: int
        def __init__(self, start_byte: Optional[int] = ..., end_byte: Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: ClassVar[int]
    RANGE_FIELD_NUMBER: ClassVar[int]
    id: str
    range: CreateDownloadLinkRequest.Range
    def __init__(self, id: Optional[str] = ..., range: Optional[Union[CreateDownloadLinkRequest.Range, Mapping]] = ...) -> None: ...

class CreateDownloadLinkResponse(_message.Message):
    __slots__ = ["download_link", "object"]
    DOWNLOAD_LINK_FIELD_NUMBER: ClassVar[int]
    OBJECT_FIELD_NUMBER: ClassVar[int]
    download_link: str
    object: _object_models_pb2.Object
    def __init__(self, download_link: Optional[str] = ..., object: Optional[Union[_object_models_pb2.Object, Mapping]] = ...) -> None: ...

class CreateDownloadLinkStreamRequest(_message.Message):
    __slots__ = ["dataset", "dataset_version", "date_range"]
    class DatasetQuery(_message.Message):
        __slots__ = ["dataset_id"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        def __init__(self, dataset_id: Optional[str] = ...) -> None: ...
    class DatasetVersionQuery(_message.Message):
        __slots__ = ["dataset_id", "dataset_version_id"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        DATASET_VERSION_ID_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        dataset_version_id: str
        def __init__(self, dataset_id: Optional[str] = ..., dataset_version_id: Optional[str] = ...) -> None: ...
    class DateRangeQuery(_message.Message):
        __slots__ = ["dataset_id", "end", "start"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        END_FIELD_NUMBER: ClassVar[int]
        START_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        end: _timestamp_pb2.Timestamp
        start: _timestamp_pb2.Timestamp
        def __init__(self, dataset_id: Optional[str] = ..., start: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., end: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...
    DATASET_FIELD_NUMBER: ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: ClassVar[int]
    dataset: CreateDownloadLinkStreamRequest.DatasetQuery
    dataset_version: CreateDownloadLinkStreamRequest.DatasetVersionQuery
    date_range: CreateDownloadLinkStreamRequest.DateRangeQuery
    def __init__(self, dataset: Optional[Union[CreateDownloadLinkStreamRequest.DatasetQuery, Mapping]] = ..., dataset_version: Optional[Union[CreateDownloadLinkStreamRequest.DatasetVersionQuery, Mapping]] = ..., date_range: Optional[Union[CreateDownloadLinkStreamRequest.DateRangeQuery, Mapping]] = ...) -> None: ...

class CreateDownloadLinkStreamResponse(_message.Message):
    __slots__ = ["links"]
    LINKS_FIELD_NUMBER: ClassVar[int]
    links: LinksResponse
    def __init__(self, links: Optional[Union[LinksResponse, Mapping]] = ...) -> None: ...

class CreateUploadLink(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class CreateUploadLinkRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class CreateUploadLinkResponse(_message.Message):
    __slots__ = ["upload_link"]
    UPLOAD_LINK_FIELD_NUMBER: ClassVar[int]
    upload_link: str
    def __init__(self, upload_link: Optional[str] = ...) -> None: ...

class GetMultipartUploadLinkRequest(_message.Message):
    __slots__ = ["object_id", "upload_part"]
    OBJECT_ID_FIELD_NUMBER: ClassVar[int]
    UPLOAD_PART_FIELD_NUMBER: ClassVar[int]
    object_id: str
    upload_part: int
    def __init__(self, object_id: Optional[str] = ..., upload_part: Optional[int] = ...) -> None: ...

class GetMultipartUploadLinkResponse(_message.Message):
    __slots__ = ["object", "upload_link"]
    OBJECT_FIELD_NUMBER: ClassVar[int]
    UPLOAD_LINK_FIELD_NUMBER: ClassVar[int]
    object: _object_models_pb2.Object
    upload_link: str
    def __init__(self, upload_link: Optional[str] = ..., object: Optional[Union[_object_models_pb2.Object, Mapping]] = ...) -> None: ...

class InnerLinksResponse(_message.Message):
    __slots__ = ["object_links"]
    OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    object_links: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_links: Optional[Iterable[str]] = ...) -> None: ...

class LinksResponse(_message.Message):
    __slots__ = ["object_group_links", "object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_LINKS_FIELD_NUMBER: ClassVar[int]
    object_group_links: _containers.RepeatedCompositeFieldContainer[InnerLinksResponse]
    object_groups: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroup]
    def __init__(self, object_groups: Optional[Iterable[Union[_object_models_pb2.ObjectGroup, Mapping]]] = ..., object_group_links: Optional[Iterable[Union[InnerLinksResponse, Mapping]]] = ...) -> None: ...

class StartMultipartUploadRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class StartMultipartUploadResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: ClassVar[int]
    object: _object_models_pb2.Object
    def __init__(self, object: Optional[Union[_object_models_pb2.Object, Mapping]] = ...) -> None: ...
