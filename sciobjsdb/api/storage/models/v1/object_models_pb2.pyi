from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Object(_message.Message):
    __slots__ = ["annotations", "content_len", "created", "dataset_id", "default_location", "fileformat", "filename", "filetype", "generated", "id", "labels", "locations", "object_group_id", "origin", "project_id", "stats", "status"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: ClassVar[int]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DEFAULT_LOCATION_FIELD_NUMBER: ClassVar[int]
    FILEFORMAT_FIELD_NUMBER: ClassVar[int]
    FILENAME_FIELD_NUMBER: ClassVar[int]
    FILETYPE_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    LOCATIONS_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    content_len: int
    created: _timestamp_pb2.Timestamp
    dataset_id: str
    default_location: _common_models_pb2.Location
    fileformat: str
    filename: str
    filetype: str
    generated: _timestamp_pb2.Timestamp
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    locations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Location]
    object_group_id: str
    origin: _common_models_pb2.Origin
    project_id: str
    stats: ObjectStats
    status: _common_models_pb2.Status
    def __init__(self, id: Optional[str] = ..., filename: Optional[str] = ..., filetype: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., locations: Optional[Iterable[Union[_common_models_pb2.Location, Mapping]]] = ..., default_location: Optional[Union[_common_models_pb2.Location, Mapping]] = ..., origin: Optional[Union[_common_models_pb2.Origin, Mapping]] = ..., content_len: Optional[int] = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., object_group_id: Optional[str] = ..., dataset_id: Optional[str] = ..., project_id: Optional[str] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., stats: Optional[Union[ObjectStats, Mapping]] = ..., fileformat: Optional[str] = ...) -> None: ...

class ObjectGroup(_message.Message):
    __slots__ = ["current_revision", "dataset_id", "id", "project_id", "revision_counter"]
    CURRENT_REVISION_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    REVISION_COUNTER_FIELD_NUMBER: ClassVar[int]
    current_revision: ObjectGroupRevision
    dataset_id: str
    id: str
    project_id: str
    revision_counter: int
    def __init__(self, id: Optional[str] = ..., revision_counter: Optional[int] = ..., current_revision: Optional[Union[ObjectGroupRevision, Mapping]] = ..., dataset_id: Optional[str] = ..., project_id: Optional[str] = ...) -> None: ...

class ObjectGroupRevision(_message.Message):
    __slots__ = ["annotations", "created", "dataset_id", "description", "generated", "id", "labels", "metadata_objects", "name", "object_group_id", "objects", "project_id", "revision_number", "stats", "status", "subpath"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_OBJECTS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    REVISION_NUMBER_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    SUBPATH_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    created: _timestamp_pb2.Timestamp
    dataset_id: str
    description: str
    generated: _timestamp_pb2.Timestamp
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata_objects: _containers.RepeatedCompositeFieldContainer[Object]
    name: str
    object_group_id: str
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    project_id: str
    revision_number: int
    stats: ObjectGroupStats
    status: _common_models_pb2.Status
    subpath: Subpath
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., dataset_id: Optional[str] = ..., project_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., objects: Optional[Iterable[Union[Object, Mapping]]] = ..., metadata_objects: Optional[Iterable[Union[Object, Mapping]]] = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., stats: Optional[Union[ObjectGroupStats, Mapping]] = ..., subpath: Optional[Union[Subpath, Mapping]] = ..., object_group_id: Optional[str] = ..., revision_number: Optional[int] = ...) -> None: ...

class ObjectGroupStats(_message.Message):
    __slots__ = ["acc_size", "avg_object_size", "meta_object_count", "object_count"]
    ACC_SIZE_FIELD_NUMBER: ClassVar[int]
    AVG_OBJECT_SIZE_FIELD_NUMBER: ClassVar[int]
    META_OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    acc_size: int
    avg_object_size: float
    meta_object_count: int
    object_count: int
    def __init__(self, object_count: Optional[int] = ..., acc_size: Optional[int] = ..., avg_object_size: Optional[float] = ..., meta_object_count: Optional[int] = ...) -> None: ...

class ObjectStats(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Subpath(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: ClassVar[int]
    path: str
    def __init__(self, path: Optional[str] = ...) -> None: ...
