from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModifyRelationsRequest(_message.Message):
    __slots__ = ["resource_id", "add_relations", "remove_relations"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_RELATIONS_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    add_relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    remove_relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    def __init__(self, resource_id: _Optional[str] = ..., add_relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ..., remove_relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ...) -> None: ...

class ModifyRelationsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetHierarchyRequest(_message.Message):
    __slots__ = ["resource_id"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class DatasetRelations(_message.Message):
    __slots__ = ["origin", "object_children"]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    origin: str
    object_children: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, origin: _Optional[str] = ..., object_children: _Optional[_Iterable[str]] = ...) -> None: ...

class CollectionRelations(_message.Message):
    __slots__ = ["origin", "dataset_children", "object_children"]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    DATASET_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    origin: str
    dataset_children: _containers.RepeatedCompositeFieldContainer[DatasetRelations]
    object_children: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, origin: _Optional[str] = ..., dataset_children: _Optional[_Iterable[_Union[DatasetRelations, _Mapping]]] = ..., object_children: _Optional[_Iterable[str]] = ...) -> None: ...

class ProjectRelations(_message.Message):
    __slots__ = ["origin", "collection_children", "dataset_children", "object_children"]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    DATASET_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    OBJECT_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    origin: str
    collection_children: _containers.RepeatedCompositeFieldContainer[CollectionRelations]
    dataset_children: _containers.RepeatedCompositeFieldContainer[DatasetRelations]
    object_children: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, origin: _Optional[str] = ..., collection_children: _Optional[_Iterable[_Union[CollectionRelations, _Mapping]]] = ..., dataset_children: _Optional[_Iterable[_Union[DatasetRelations, _Mapping]]] = ..., object_children: _Optional[_Iterable[str]] = ...) -> None: ...

class GetHierarchyResponse(_message.Message):
    __slots__ = ["project", "collection", "dataset"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    project: ProjectRelations
    collection: CollectionRelations
    dataset: DatasetRelations
    def __init__(self, project: _Optional[_Union[ProjectRelations, _Mapping]] = ..., collection: _Optional[_Union[CollectionRelations, _Mapping]] = ..., dataset: _Optional[_Union[DatasetRelations, _Mapping]] = ...) -> None: ...
