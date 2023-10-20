from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCollectionRequest(_message.Message):
    __slots__ = ["name", "description", "key_values", "relations", "data_class", "project_id", "metadata_license_tag", "default_data_license_tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    data_class: _models_pb2.DataClass
    project_id: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ..., project_id: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class CreateCollectionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class GetCollectionRequest(_message.Message):
    __slots__ = ["collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class GetCollectionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class GetCollectionsRequest(_message.Message):
    __slots__ = ["collection_ids"]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetCollectionsResponse(_message.Message):
    __slots__ = ["collections"]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[_models_pb2.Collection]
    def __init__(self, collections: _Optional[_Iterable[_Union[_models_pb2.Collection, _Mapping]]] = ...) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ["collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class DeleteCollectionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCollectionNameRequest(_message.Message):
    __slots__ = ["collection_id", "name"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    name: str
    def __init__(self, collection_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateCollectionNameResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class UpdateCollectionDescriptionRequest(_message.Message):
    __slots__ = ["collection_id", "description"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    description: str
    def __init__(self, collection_id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateCollectionDescriptionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class UpdateCollectionKeyValuesRequest(_message.Message):
    __slots__ = ["collection_id", "add_key_values", "remove_key_values"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    add_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    remove_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, collection_id: _Optional[str] = ..., add_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., remove_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class UpdateCollectionKeyValuesResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class UpdateCollectionDataClassRequest(_message.Message):
    __slots__ = ["collection_id", "data_class"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    data_class: _models_pb2.DataClass
    def __init__(self, collection_id: _Optional[str] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ...) -> None: ...

class UpdateCollectionDataClassResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class SnapshotCollectionRequest(_message.Message):
    __slots__ = ["collection_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    def __init__(self, collection_id: _Optional[str] = ...) -> None: ...

class SnapshotCollectionResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...

class UpdateCollectionLicensesRequest(_message.Message):
    __slots__ = ["collection_id", "metadata_license_tag", "default_data_license_tag"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, collection_id: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class UpdateCollectionLicensesResponse(_message.Message):
    __slots__ = ["collection"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _models_pb2.Collection
    def __init__(self, collection: _Optional[_Union[_models_pb2.Collection, _Mapping]] = ...) -> None: ...
