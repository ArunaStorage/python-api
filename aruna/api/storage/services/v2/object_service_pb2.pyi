from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateObjectRequest(_message.Message):
    __slots__ = ["name", "description", "key_values", "relations", "data_class", "project_id", "collection_id", "dataset_id", "hashes", "metadata_license_tag", "data_license_tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    data_class: _models_pb2.DataClass
    project_id: str
    collection_id: str
    dataset_id: str
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    metadata_license_tag: str
    data_license_tag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ..., project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., metadata_license_tag: _Optional[str] = ..., data_license_tag: _Optional[str] = ...) -> None: ...

class CreateObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class GetUploadURLRequest(_message.Message):
    __slots__ = ["object_id", "multipart", "part_number"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MULTIPART_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    multipart: bool
    part_number: int
    def __init__(self, object_id: _Optional[str] = ..., multipart: bool = ..., part_number: _Optional[int] = ...) -> None: ...

class GetUploadURLResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetDownloadURLRequest(_message.Message):
    __slots__ = ["object_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    def __init__(self, object_id: _Optional[str] = ...) -> None: ...

class GetDownloadURLResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CompletedParts(_message.Message):
    __slots__ = ["etag", "part"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PART_FIELD_NUMBER: _ClassVar[int]
    etag: str
    part: int
    def __init__(self, etag: _Optional[str] = ..., part: _Optional[int] = ...) -> None: ...

class FinishObjectStagingRequest(_message.Message):
    __slots__ = ["object_id", "content_len", "hashes", "completed_parts"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_PARTS_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    content_len: int
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    completed_parts: _containers.RepeatedCompositeFieldContainer[CompletedParts]
    def __init__(self, object_id: _Optional[str] = ..., content_len: _Optional[int] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., completed_parts: _Optional[_Iterable[_Union[CompletedParts, _Mapping]]] = ...) -> None: ...

class FinishObjectStagingResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class UpdateObjectRequest(_message.Message):
    __slots__ = ["object_id", "name", "description", "add_key_values", "remove_key_values", "data_class", "project_id", "collection_id", "dataset_id", "hashes", "force_revision", "metadata_license_tag", "data_license_tag"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADD_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    FORCE_REVISION_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    name: str
    description: str
    add_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    remove_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    data_class: _models_pb2.DataClass
    project_id: str
    collection_id: str
    dataset_id: str
    hashes: _containers.RepeatedCompositeFieldContainer[_models_pb2.Hash]
    force_revision: bool
    metadata_license_tag: str
    data_license_tag: str
    def __init__(self, object_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., add_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., remove_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ..., project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., hashes: _Optional[_Iterable[_Union[_models_pb2.Hash, _Mapping]]] = ..., force_revision: bool = ..., metadata_license_tag: _Optional[str] = ..., data_license_tag: _Optional[str] = ...) -> None: ...

class UpdateObjectResponse(_message.Message):
    __slots__ = ["object", "new_revision"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    NEW_REVISION_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    new_revision: bool
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ..., new_revision: bool = ...) -> None: ...

class CloneObjectRequest(_message.Message):
    __slots__ = ["object_id", "project_id", "collection_id", "dataset_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    project_id: str
    collection_id: str
    dataset_id: str
    def __init__(self, object_id: _Optional[str] = ..., project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ...) -> None: ...

class CloneObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ["object_id", "with_revisions"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    WITH_REVISIONS_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    with_revisions: bool
    def __init__(self, object_id: _Optional[str] = ..., with_revisions: bool = ...) -> None: ...

class DeleteObjectResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetObjectRequest(_message.Message):
    __slots__ = ["object_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    def __init__(self, object_id: _Optional[str] = ...) -> None: ...

class GetObjectResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class GetObjectsRequest(_message.Message):
    __slots__ = ["object_ids"]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetObjectsResponse(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_models_pb2.Object]
    def __init__(self, objects: _Optional[_Iterable[_Union[_models_pb2.Object, _Mapping]]] = ...) -> None: ...

class GetObjectRevisionsRequest(_message.Message):
    __slots__ = ["object_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    def __init__(self, object_id: _Optional[str] = ...) -> None: ...

class GetObjectRevisionsResponse(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_models_pb2.Object]
    def __init__(self, objects: _Optional[_Iterable[_Union[_models_pb2.Object, _Mapping]]] = ...) -> None: ...

class GetLatestObjectRevisionRequest(_message.Message):
    __slots__ = ["object_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    def __init__(self, object_id: _Optional[str] = ...) -> None: ...

class GetLatestObjectRevisionResponse(_message.Message):
    __slots__ = ["object"]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ...) -> None: ...

class GetObjectEndpointsRequest(_message.Message):
    __slots__ = ["collection_id", "object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    def __init__(self, collection_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...
