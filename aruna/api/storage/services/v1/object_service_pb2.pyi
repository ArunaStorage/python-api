from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.storage.models.v1 import query_pb2 as _query_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddLabelToObjectRequest(_message.Message):
    __slots__ = ["collection_id", "labels_to_add", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    labels_to_add: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., labels_to_add: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class AddLabelToObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class CloneObjectRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "target_collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    target_collection_id: str
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., target_collection_id: _Optional[str] = ...) -> None: ...

class CloneObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class CompletedParts(_message.Message):
    __slots__ = ["etag", "part"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    etag: str
    part: int
    def __init__(self, etag: _Optional[str] = ..., part: _Optional[int] = ...) -> None: ...

class CreateDownloadLinksStreamRequest(_message.Message):
    __slots__ = ["collection_id", "objects"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    objects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_id: _Optional[str] = ..., objects: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateDownloadLinksStreamResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: URL
    def __init__(self, url: _Optional[_Union[URL, _Mapping]] = ...) -> None: ...

class CreateObjectReferenceRequest(_message.Message):
    __slots__ = ["auto_update", "collection_id", "object_id", "target_collection_id", "writeable"]
    AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    WRITEABLE_FIELD_NUMBER: _ClassVar[int]
    auto_update: bool
    collection_id: str
    object_id: str
    target_collection_id: str
    writeable: bool
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., target_collection_id: _Optional[str] = ..., writeable: bool = ..., auto_update: bool = ...) -> None: ...

class CreateObjectReferenceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ["collection_id", "force", "object_id", "with_revisions"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WITH_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    force: bool
    object_id: str
    with_revisions: bool
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., with_revisions: bool = ..., force: bool = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteObjectsRequest(_message.Message):
    __slots__ = ["collection_id", "force", "object_ids", "with_revisions"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    WITH_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    force: bool
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    with_revisions: bool
    def __init__(self, object_ids: _Optional[_Iterable[str]] = ..., collection_id: _Optional[str] = ..., with_revisions: bool = ..., force: bool = ...) -> None: ...

class DeleteObjectsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishObjectStagingRequest(_message.Message):
    __slots__ = ["auto_update", "collection_id", "completed_parts", "hash", "no_upload", "object_id", "upload_id"]
    AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PARTS_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    NO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    auto_update: bool
    collection_id: str
    completed_parts: _containers.RepeatedCompositeFieldContainer[CompletedParts]
    hash: _models_pb2.Hash
    no_upload: bool
    object_id: str
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., hash: _Optional[_Union[_models_pb2.Hash, _Mapping]] = ..., no_upload: bool = ..., completed_parts: _Optional[_Iterable[_Union[CompletedParts, _Mapping]]] = ..., auto_update: bool = ...) -> None: ...

class FinishObjectStagingResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class GetDownloadLinksBatchRequest(_message.Message):
    __slots__ = ["collection_id", "objects"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    objects: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_id: _Optional[str] = ..., objects: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDownloadLinksBatchResponse(_message.Message):
    __slots__ = ["urls"]
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedCompositeFieldContainer[URL]
    def __init__(self, urls: _Optional[_Iterable[_Union[URL, _Mapping]]] = ...) -> None: ...

class GetDownloadURLRequest(_message.Message):
    __slots__ = ["collection_id", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class GetDownloadURLResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: URL
    def __init__(self, url: _Optional[_Union[URL, _Mapping]] = ...) -> None: ...

class GetLatestObjectRevisionRequest(_message.Message):
    __slots__ = ["collection_id", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class GetLatestObjectRevisionResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class GetObjectByIDRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "with_url"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WITH_URL_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    with_url: bool
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., with_url: bool = ...) -> None: ...

class GetObjectByIDResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: ObjectWithURL
    def __init__(self, object: _Optional[_Union[ObjectWithURL, _Mapping]] = ...) -> None: ...

class GetObjectEndpointsRequest(_message.Message):
    __slots__ = ["collection_id", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class GetObjectEndpointsResponse(_message.Message):
    __slots__ = ["endpoints"]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[_models_pb2.Endpoint]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[_models_pb2.Endpoint, _Mapping]]] = ...) -> None: ...

class GetObjectRevisionsRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "page_request", "with_url"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WITH_URL_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    page_request: _query_pb2.PageRequest
    with_url: bool
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ..., with_url: bool = ...) -> None: ...

class GetObjectRevisionsResponse(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[ObjectWithURL]
    def __init__(self, objects: _Optional[_Iterable[_Union[ObjectWithURL, _Mapping]]] = ...) -> None: ...

class GetObjectsRequest(_message.Message):
    __slots__ = ["collection_id", "label_id_filter", "page_request", "with_url"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    WITH_URL_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    label_id_filter: _query_pb2.LabelOrIDQuery
    page_request: _query_pb2.PageRequest
    with_url: bool
    def __init__(self, collection_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ..., label_id_filter: _Optional[_Union[_query_pb2.LabelOrIDQuery, _Mapping]] = ..., with_url: bool = ...) -> None: ...

class GetObjectsResponse(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[ObjectWithURL]
    def __init__(self, objects: _Optional[_Iterable[_Union[ObjectWithURL, _Mapping]]] = ...) -> None: ...

class GetReferencesRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "with_revisions"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WITH_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    with_revisions: bool
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., with_revisions: bool = ...) -> None: ...

class GetReferencesResponse(_message.Message):
    __slots__ = ["references"]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    references: _containers.RepeatedCompositeFieldContainer[ObjectReference]
    def __init__(self, references: _Optional[_Iterable[_Union[ObjectReference, _Mapping]]] = ...) -> None: ...

class GetUploadURLRequest(_message.Message):
    __slots__ = ["collection_id", "multipart", "object_id", "part_number", "upload_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    multipart: bool
    object_id: str
    part_number: int
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., multipart: bool = ..., part_number: _Optional[int] = ...) -> None: ...

class GetUploadURLResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: URL
    def __init__(self, url: _Optional[_Union[URL, _Mapping]] = ...) -> None: ...

class InitializeNewObjectRequest(_message.Message):
    __slots__ = ["collection_id", "is_specification", "multipart", "object", "preferred_endpoint_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    is_specification: bool
    multipart: bool
    object: StageObject
    preferred_endpoint_id: str
    def __init__(self, object: _Optional[_Union[StageObject, _Mapping]] = ..., collection_id: _Optional[str] = ..., preferred_endpoint_id: _Optional[str] = ..., multipart: bool = ..., is_specification: bool = ...) -> None: ...

class InitializeNewObjectResponse(_message.Message):
    __slots__ = ["collection_id", "object_id", "upload_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class ObjectReference(_message.Message):
    __slots__ = ["collection_id", "is_writeable", "object_id", "revision_number"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_WRITEABLE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    is_writeable: bool
    object_id: str
    revision_number: int
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., revision_number: _Optional[int] = ..., is_writeable: bool = ...) -> None: ...

class ObjectWithURL(_message.Message):
    __slots__ = ["object", "url"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    url: str
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ..., url: _Optional[str] = ...) -> None: ...

class SetHooksOfObjectRequest(_message.Message):
    __slots__ = ["collection_id", "hooks", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class SetHooksOfObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class StageObject(_message.Message):
    __slots__ = ["collection_id", "content_len", "dataclass", "description", "filename", "hooks", "labels", "source"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: _ClassVar[int]
    DATACLASS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    content_len: int
    dataclass: _models_pb2.DataClass
    description: str
    filename: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    source: _models_pb2.Source
    def __init__(self, filename: _Optional[str] = ..., description: _Optional[str] = ..., collection_id: _Optional[str] = ..., content_len: _Optional[int] = ..., source: _Optional[_Union[_models_pb2.Source, _Mapping]] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class URL(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class UpdateObjectRequest(_message.Message):
    __slots__ = ["collection_id", "is_specification", "multi_part", "object", "object_id", "preferred_endpoint_id", "reupload"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SPECIFICATION_FIELD_NUMBER: _ClassVar[int]
    MULTI_PART_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    REUPLOAD_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    is_specification: bool
    multi_part: bool
    object: StageObject
    object_id: str
    preferred_endpoint_id: str
    reupload: bool
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., object: _Optional[_Union[StageObject, _Mapping]] = ..., reupload: bool = ..., preferred_endpoint_id: _Optional[str] = ..., multi_part: bool = ..., is_specification: bool = ...) -> None: ...

class UpdateObjectResponse(_message.Message):
    __slots__ = ["collection_id", "object_id", "staging_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STAGING_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    staging_id: str
    def __init__(self, object_id: _Optional[str] = ..., staging_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...
