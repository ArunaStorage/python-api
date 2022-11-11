from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.storage.models.v1 import query_pb2 as _query_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateNewCollectionRequest(_message.Message):
    __slots__ = ["dataclass", "description", "hooks", "label_ontology", "labels", "name", "project_id"]
    DATACLASS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    dataclass: _models_pb2.DataClass
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    label_ontology: _models_pb2.LabelOntology
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    name: str
    project_id: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., project_id: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., label_ontology: _Optional[_Union[_models_pb2.LabelOntology, _Mapping]] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ...) -> None: ...

class CreateNewCollectionResponse(_message.Message):
    __slots__ = ["collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ["collection_id", "force"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    force: bool
    def __init__(self, collection_id: _Optional[str] = ..., force: bool = ...) -> None: ...

class DeleteCollectionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCollectionByIDRequest(_message.Message):
    __slots__ = ["collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class GetCollectionByIDResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.CollectionOverview
    def __init__(self, collection: _Optional[_Union[_models_pb2.CollectionOverview, _Mapping]] = ...) -> None: ...

class GetCollectionsRequest(_message.Message):
    __slots__ = ["label_or_id_filter", "page_request", "project_id"]
    LABEL_OR_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    label_or_id_filter: _query_pb2.LabelOrIDQuery
    page_request: _query_pb2.PageRequest
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., label_or_id_filter: _Optional[_Union[_query_pb2.LabelOrIDQuery, _Mapping]] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetCollectionsResponse(_message.Message):
    __slots__ = ["collections"]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _models_pb2.CollectionOverviews
    def __init__(self, collections: _Optional[_Union[_models_pb2.CollectionOverviews, _Mapping]] = ...) -> None: ...

class PinCollectionVersionRequest(_message.Message):
    __slots__ = ["collection_id", "version"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    version: _models_pb2.Version
    def __init__(self, collection_id: _Optional[str] = ..., version: _Optional[_Union[_models_pb2.Version, _Mapping]] = ...) -> None: ...

class PinCollectionVersionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.CollectionOverview
    def __init__(self, collection: _Optional[_Union[_models_pb2.CollectionOverview, _Mapping]] = ...) -> None: ...

class UpdateCollectionRequest(_message.Message):
    __slots__ = ["collection_id", "dataclass", "description", "hooks", "label_ontology", "labels", "name", "version"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATACLASS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    dataclass: _models_pb2.DataClass
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    label_ontology: _models_pb2.LabelOntology
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    name: str
    version: _models_pb2.Version
    def __init__(self, collection_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., label_ontology: _Optional[_Union[_models_pb2.LabelOntology, _Mapping]] = ..., dataclass: _Optional[_Union[_models_pb2.DataClass, str]] = ..., version: _Optional[_Union[_models_pb2.Version, _Mapping]] = ...) -> None: ...

class UpdateCollectionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.CollectionOverview
    def __init__(self, collection: _Optional[_Union[_models_pb2.CollectionOverview, _Mapping]] = ...) -> None: ...
