from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Dataset(_message.Message):
    __slots__ = ["bucket", "created", "description", "id", "is_public", "labels", "metadata", "name", "project_id", "stats", "status"]
    BUCKET_FIELD_NUMBER: ClassVar[int]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    bucket: str
    created: _timestamp_pb2.Timestamp
    description: str
    id: str
    is_public: bool
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    project_id: str
    stats: DatasetStats
    status: _common_models_pb2.Status
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., project_id: Optional[str] = ..., is_public: bool = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., bucket: Optional[str] = ..., stats: Optional[Union[DatasetStats, Mapping]] = ...) -> None: ...

class DatasetStats(_message.Message):
    __slots__ = ["acc_size", "avg_object_size", "object_count", "object_group_count"]
    ACC_SIZE_FIELD_NUMBER: ClassVar[int]
    AVG_OBJECT_SIZE_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_COUNT_FIELD_NUMBER: ClassVar[int]
    acc_size: int
    avg_object_size: float
    object_count: int
    object_group_count: int
    def __init__(self, object_count: Optional[int] = ..., object_group_count: Optional[int] = ..., acc_size: Optional[int] = ..., avg_object_size: Optional[float] = ...) -> None: ...

class DatasetVersion(_message.Message):
    __slots__ = ["created", "dataset_id", "description", "id", "labels", "metadata", "name", "object_count", "object_group_ids", "project_id", "stats", "status", "version"]
    CREATED_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_IDS_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    created: _timestamp_pb2.Timestamp
    dataset_id: str
    description: str
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    object_count: int
    object_group_ids: _containers.RepeatedScalarFieldContainer[str]
    project_id: str
    stats: DatasetVersionStats
    status: _common_models_pb2.Status
    version: _common_models_pb2.Version
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., dataset_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., created: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., version: Optional[Union[_common_models_pb2.Version, Mapping]] = ..., object_group_ids: Optional[Iterable[str]] = ..., object_count: Optional[int] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., project_id: Optional[str] = ..., stats: Optional[Union[DatasetVersionStats, Mapping]] = ...) -> None: ...

class DatasetVersionStats(_message.Message):
    __slots__ = ["acc_size", "avg_object_size", "object_count", "object_group_count"]
    ACC_SIZE_FIELD_NUMBER: ClassVar[int]
    AVG_OBJECT_SIZE_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_COUNT_FIELD_NUMBER: ClassVar[int]
    acc_size: int
    avg_object_size: float
    object_count: int
    object_group_count: int
    def __init__(self, object_count: Optional[int] = ..., object_group_count: Optional[int] = ..., acc_size: Optional[int] = ..., avg_object_size: Optional[float] = ...) -> None: ...
