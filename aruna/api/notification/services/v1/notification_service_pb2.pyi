from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
EVENT_TYPE_ALL: EventType
EVENT_TYPE_AVAILABLE: EventType
EVENT_TYPE_CREATED: EventType
EVENT_TYPE_DELETED: EventType
EVENT_TYPE_METADATA_UPDATED: EventType
EVENT_TYPE_UNSPECIFIED: EventType
EVENT_TYPE_UPDATED: EventType

class AcknowledgeMessageBatchRequest(_message.Message):
    __slots__ = ["replies"]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    replies: _containers.RepeatedCompositeFieldContainer[Reply]
    def __init__(self, replies: _Optional[_Iterable[_Union[Reply, _Mapping]]] = ...) -> None: ...

class AcknowledgeMessageBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateEventStreamingGroupRequest(_message.Message):
    __slots__ = ["hierarchy", "include_subresource", "resource", "resource_id", "stream_all", "stream_from_date", "stream_from_sequence"]
    HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUBRESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ALL_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    hierarchy: EventStreamingGroupHierarchy
    include_subresource: bool
    resource: _models_pb2.ResourceType
    resource_id: str
    stream_all: StreamAll
    stream_from_date: StreamFromDate
    stream_from_sequence: StreamFromSequence
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., include_subresource: bool = ..., stream_all: _Optional[_Union[StreamAll, _Mapping]] = ..., stream_from_date: _Optional[_Union[StreamFromDate, _Mapping]] = ..., stream_from_sequence: _Optional[_Union[StreamFromSequence, _Mapping]] = ..., hierarchy: _Optional[_Union[EventStreamingGroupHierarchy, _Mapping]] = ...) -> None: ...

class CreateEventStreamingGroupResponse(_message.Message):
    __slots__ = ["stream_group_id"]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    stream_group_id: str
    def __init__(self, stream_group_id: _Optional[str] = ...) -> None: ...

class DeleteEventStreamingGroupRequest(_message.Message):
    __slots__ = ["stream_group_id"]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    stream_group_id: str
    def __init__(self, stream_group_id: _Optional[str] = ...) -> None: ...

class DeleteEventStreamingGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventNotificationMessage(_message.Message):
    __slots__ = ["reply", "resource", "resource_id", "updated_type"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TYPE_FIELD_NUMBER: _ClassVar[int]
    reply: Reply
    resource: _models_pb2.ResourceType
    resource_id: str
    updated_type: EventType
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., updated_type: _Optional[_Union[EventType, str]] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class EventStreamingGroupHierarchy(_message.Message):
    __slots__ = ["collection_id", "object_group_id", "object_id", "project_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_group_id: str
    object_id: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., object_id: _Optional[str] = ..., object_group_id: _Optional[str] = ...) -> None: ...

class GetEventMessageBatchRequest(_message.Message):
    __slots__ = ["batch_size", "stream_group_id"]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    batch_size: int
    stream_group_id: str
    def __init__(self, stream_group_id: _Optional[str] = ..., batch_size: _Optional[int] = ...) -> None: ...

class GetEventMessageBatchResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[EventNotificationMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[EventNotificationMessage, _Mapping]]] = ...) -> None: ...

class GetEventMessageBatchStreamRequest(_message.Message):
    __slots__ = ["batch_size", "stream_group_id"]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    batch_size: int
    stream_group_id: str
    def __init__(self, stream_group_id: _Optional[str] = ..., batch_size: _Optional[int] = ...) -> None: ...

class GetEventMessageBatchStreamResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[EventNotificationMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[EventNotificationMessage, _Mapping]]] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["hmac", "reply", "salt"]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    hmac: str
    reply: str
    salt: str
    def __init__(self, reply: _Optional[str] = ..., salt: _Optional[str] = ..., hmac: _Optional[str] = ...) -> None: ...

class StreamAll(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StreamFromDate(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamFromSequence(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    def __init__(self, sequence: _Optional[int] = ...) -> None: ...

class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
