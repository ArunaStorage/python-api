from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.storage.models.v1 import query_pb2 as _query_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddLabelsToObjectGroupRequest(_message.Message):
    __slots__ = ["collection_id", "group_id", "labels_to_add"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    group_id: str
    labels_to_add: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, collection_id: _Optional[str] = ..., group_id: _Optional[str] = ..., labels_to_add: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class AddLabelsToObjectGroupResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: _ClassVar[int]
    object_group: _models_pb2.ObjectGroupOverview
    def __init__(self, object_group: _Optional[_Union[_models_pb2.ObjectGroupOverview, _Mapping]] = ...) -> None: ...

class CreateObjectGroupRequest(_message.Message):
    __slots__ = ["collection_id", "description", "hooks", "labels", "meta_object_ids", "name", "object_ids"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    META_OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    meta_object_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., collection_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ..., meta_object_ids: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class CreateObjectGroupResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: _ClassVar[int]
    object_group: _models_pb2.ObjectGroupOverview
    def __init__(self, object_group: _Optional[_Union[_models_pb2.ObjectGroupOverview, _Mapping]] = ...) -> None: ...

class DeleteObjectGroupRequest(_message.Message):
    __slots__ = ["collection_id", "group_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    group_id: str
    def __init__(self, group_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class DeleteObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetObjectGroupByIdRequest(_message.Message):
    __slots__ = ["collection_id", "group_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    group_id: str
    def __init__(self, group_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

class GetObjectGroupByIdResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: _ClassVar[int]
    object_group: _models_pb2.ObjectGroupOverview
    def __init__(self, object_group: _Optional[_Union[_models_pb2.ObjectGroupOverview, _Mapping]] = ...) -> None: ...

class GetObjectGroupHistoryRequest(_message.Message):
    __slots__ = ["collection_id", "group_id", "page_request"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    group_id: str
    page_request: _query_pb2.PageRequest
    def __init__(self, collection_id: _Optional[str] = ..., group_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetObjectGroupHistoryResponse(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    object_groups: _models_pb2.ObjectGroupOverviews
    def __init__(self, object_groups: _Optional[_Union[_models_pb2.ObjectGroupOverviews, _Mapping]] = ...) -> None: ...

class GetObjectGroupObjectsRequest(_message.Message):
    __slots__ = ["collection_id", "group_id", "meta_only", "page_request"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    META_ONLY_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    group_id: str
    meta_only: bool
    page_request: _query_pb2.PageRequest
    def __init__(self, collection_id: _Optional[str] = ..., group_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ..., meta_only: bool = ...) -> None: ...

class GetObjectGroupObjectsResponse(_message.Message):
    __slots__ = ["object_group_objects"]
    OBJECT_GROUP_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    object_group_objects: _containers.RepeatedCompositeFieldContainer[ObjectGroupObject]
    def __init__(self, object_group_objects: _Optional[_Iterable[_Union[ObjectGroupObject, _Mapping]]] = ...) -> None: ...

class GetObjectGroupsFromObjectRequest(_message.Message):
    __slots__ = ["collection_id", "object_id", "page_request"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    page_request: _query_pb2.PageRequest
    def __init__(self, object_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetObjectGroupsFromObjectResponse(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    object_groups: _models_pb2.ObjectGroupOverviews
    def __init__(self, object_groups: _Optional[_Union[_models_pb2.ObjectGroupOverviews, _Mapping]] = ...) -> None: ...

class GetObjectGroupsRequest(_message.Message):
    __slots__ = ["collection_id", "label_id_filter", "page_request"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_ID_FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    label_id_filter: _query_pb2.LabelOrIDQuery
    page_request: _query_pb2.PageRequest
    def __init__(self, collection_id: _Optional[str] = ..., page_request: _Optional[_Union[_query_pb2.PageRequest, _Mapping]] = ..., label_id_filter: _Optional[_Union[_query_pb2.LabelOrIDQuery, _Mapping]] = ...) -> None: ...

class GetObjectGroupsResponse(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    object_groups: _models_pb2.ObjectGroupOverviews
    def __init__(self, object_groups: _Optional[_Union[_models_pb2.ObjectGroupOverviews, _Mapping]] = ...) -> None: ...

class ObjectGroupObject(_message.Message):
    __slots__ = ["is_metadata", "object"]
    IS_METADATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    is_metadata: bool
    object: _models_pb2.Object
    def __init__(self, object: _Optional[_Union[_models_pb2.Object, _Mapping]] = ..., is_metadata: bool = ...) -> None: ...

class UpdateObjectGroupRequest(_message.Message):
    __slots__ = ["collection_id", "description", "group_id", "hooks", "labels", "meta_object_ids", "name", "object_ids"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    META_OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    description: str
    group_id: str
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    meta_object_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., collection_id: _Optional[str] = ..., object_ids: _Optional[_Iterable[str]] = ..., meta_object_ids: _Optional[_Iterable[str]] = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class UpdateObjectGroupResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: _ClassVar[int]
    object_group: _models_pb2.ObjectGroupOverview
    def __init__(self, object_group: _Optional[_Union[_models_pb2.ObjectGroupOverview, _Mapping]] = ...) -> None: ...
