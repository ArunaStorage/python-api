from google.api import annotations_pb2 as _annotations_pb2
from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicateProjectDataRequest(_message.Message):
    __slots__ = ("project_id", "endpoint_id")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    endpoint_id: str
    def __init__(self, project_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class ReplicateProjectDataResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _models_pb2.ReplicationStatus
    def __init__(self, status: _Optional[_Union[_models_pb2.ReplicationStatus, str]] = ...) -> None: ...

class PartialReplicateDataRequest(_message.Message):
    __slots__ = ("collection_id", "dataset_id", "object_id", "endpoint_id")
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    dataset_id: str
    object_id: str
    endpoint_id: str
    def __init__(self, collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., object_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class PartialReplicateDataResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _models_pb2.ReplicationStatus
    def __init__(self, status: _Optional[_Union[_models_pb2.ReplicationStatus, str]] = ...) -> None: ...

class UpdateReplicationStatusRequest(_message.Message):
    __slots__ = ("object_id", "endpoint_id", "status")
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    endpoint_id: str
    status: _models_pb2.ReplicationStatus
    def __init__(self, object_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., status: _Optional[_Union[_models_pb2.ReplicationStatus, str]] = ...) -> None: ...

class UpdateReplicationStatusResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetReplicationStatusRequest(_message.Message):
    __slots__ = ("resource_id", "endpoint_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    endpoint_id: str
    def __init__(self, resource_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetReplicationStatusResponse(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[ReplicationInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[ReplicationInfo, _Mapping]]] = ...) -> None: ...

class ReplicationInfo(_message.Message):
    __slots__ = ("project_id", "collection_id", "dataset_id", "object_id", "endpoint_info")
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_INFO_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    collection_id: str
    dataset_id: str
    object_id: str
    endpoint_info: _models_pb2.DataEndpoint
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., object_id: _Optional[str] = ..., endpoint_info: _Optional[_Union[_models_pb2.DataEndpoint, _Mapping]] = ...) -> None: ...

class DeleteReplicationRequest(_message.Message):
    __slots__ = ("resource_id", "endpoint_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    endpoint_id: str
    def __init__(self, resource_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class DeleteReplicationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
