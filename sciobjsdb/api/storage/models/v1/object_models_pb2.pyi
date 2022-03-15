from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Object(_message.Message):
    __slots__ = ["content_len", "created", "dataset_id", "filename", "filetype", "generated", "id", "labels", "location", "metadata", "object_group_id", "origin", "project_id", "stats", "status", "upload_id"]
    CONTENT_LEN_FIELD_NUMBER: ClassVar[int]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    FILENAME_FIELD_NUMBER: ClassVar[int]
    FILETYPE_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: ClassVar[int]
    content_len: int
    created: _timestamp_pb2.Timestamp
    dataset_id: str
    filename: str
    filetype: str
    generated: _timestamp_pb2.Timestamp
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    location: _common_models_pb2.Location
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    object_group_id: str
    origin: _common_models_pb2.Origin
    project_id: str
    stats: ObjectStats
    status: _common_models_pb2.Status
    upload_id: str
    def __init__(self, id: Optional[str] = ..., filename: Optional[str] = ..., filetype: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., location: Optional[Union[_common_models_pb2.Location, Mapping]] = ..., origin: Optional[Union[_common_models_pb2.Origin, Mapping]] = ..., content_len: Optional[int] = ..., upload_id: Optional[str] = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., object_group_id: Optional[str] = ..., dataset_id: Optional[str] = ..., project_id: Optional[str] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., stats: Optional[Union[ObjectStats, Mapping]] = ...) -> None: ...

class ObjectGroup(_message.Message):
    __slots__ = ["created", "dataset_id", "description", "generated", "id", "labels", "metadata", "name", "objects", "project_id", "stats", "status"]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    created: _timestamp_pb2.Timestamp
    dataset_id: str
    description: str
    generated: _timestamp_pb2.Timestamp
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    project_id: str
    stats: ObjectGroupStats
    status: _common_models_pb2.Status
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., dataset_id: Optional[str] = ..., project_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., objects: Optional[Iterable[Union[Object, Mapping]]] = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., stats: Optional[Union[ObjectGroupStats, Mapping]] = ...) -> None: ...

class ObjectGroupStats(_message.Message):
    __slots__ = ["acc_size", "avg_object_size", "object_count"]
    ACC_SIZE_FIELD_NUMBER: ClassVar[int]
    AVG_OBJECT_SIZE_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    acc_size: int
    avg_object_size: float
    object_count: int
    def __init__(self, object_count: Optional[int] = ..., acc_size: Optional[int] = ..., avg_object_size: Optional[float] = ...) -> None: ...

class ObjectStats(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
