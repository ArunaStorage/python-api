from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLICATION_STATUS_UNSPECIFIED: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_WAITING: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_RUNNING: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_FINISHED: _ClassVar[ReplicationStatus]
    REPLICATION_STATUS_ERROR: _ClassVar[ReplicationStatus]
REPLICATION_STATUS_UNSPECIFIED: ReplicationStatus
REPLICATION_STATUS_WAITING: ReplicationStatus
REPLICATION_STATUS_RUNNING: ReplicationStatus
REPLICATION_STATUS_FINISHED: ReplicationStatus
REPLICATION_STATUS_ERROR: ReplicationStatus

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
    status: ReplicationStatus
    def __init__(self, status: _Optional[_Union[ReplicationStatus, str]] = ...) -> None: ...

class PartialReplicateDataRequest(_message.Message):
    __slots__ = ("resource_id", "endpoint_id")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    endpoint_id: str
    def __init__(self, resource_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class PartialReplicateDataResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ReplicationStatus
    def __init__(self, status: _Optional[_Union[ReplicationStatus, str]] = ...) -> None: ...

class UpdateReplicationStatusRequest(_message.Message):
    __slots__ = ("resource_id", "endpoint_id", "status")
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    endpoint_id: str
    status: ReplicationStatus
    def __init__(self, resource_id: _Optional[str] = ..., endpoint_id: _Optional[str] = ..., status: _Optional[_Union[ReplicationStatus, str]] = ...) -> None: ...

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
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: ReplicationStatus
    def __init__(self, status: _Optional[_Union[ReplicationStatus, str]] = ...) -> None: ...

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
