from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Project(_message.Message):
    __slots__ = ["annotations", "bucket", "description", "id", "labels", "name", "stats", "status", "users"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    BUCKET_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    STATS_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    USERS_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    bucket: str
    description: str
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    name: str
    stats: ProjectStats
    status: _common_models_pb2.Status
    users: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.User]
    def __init__(self, id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., users: Optional[Iterable[Union[_common_models_pb2.User, Mapping]]] = ..., bucket: Optional[str] = ..., status: Optional[Union[_common_models_pb2.Status, str]] = ..., stats: Optional[Union[ProjectStats, Mapping]] = ...) -> None: ...

class ProjectStats(_message.Message):
    __slots__ = ["acc_size", "avg_object_size", "object_count", "object_group_count", "user_count"]
    ACC_SIZE_FIELD_NUMBER: ClassVar[int]
    AVG_OBJECT_SIZE_FIELD_NUMBER: ClassVar[int]
    OBJECT_COUNT_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_COUNT_FIELD_NUMBER: ClassVar[int]
    USER_COUNT_FIELD_NUMBER: ClassVar[int]
    acc_size: int
    avg_object_size: float
    object_count: int
    object_group_count: int
    user_count: int
    def __init__(self, object_count: Optional[int] = ..., object_group_count: Optional[int] = ..., acc_size: Optional[int] = ..., avg_object_size: Optional[float] = ..., user_count: Optional[int] = ...) -> None: ...
