from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEventStreamingGroupRequest(_message.Message):
    __slots__ = ["include_subresource", "resource", "resource_id", "stream_all", "stream_from_date", "stream_from_sequence", "stream_group_id"]
    class EventResources(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EVENT_RESOURCES_ALL_RESOURCE: CreateEventStreamingGroupRequest.EventResources
    EVENT_RESOURCES_DATASET_RESOURCE: CreateEventStreamingGroupRequest.EventResources
    EVENT_RESOURCES_DATASET_VERSION_RESOURCE: CreateEventStreamingGroupRequest.EventResources
    EVENT_RESOURCES_OBJECT_GROUP_RESOURCE: CreateEventStreamingGroupRequest.EventResources
    EVENT_RESOURCES_PROJECT_RESOURCE: CreateEventStreamingGroupRequest.EventResources
    EVENT_RESOURCES_UNSPECIFIED: CreateEventStreamingGroupRequest.EventResources
    INCLUDE_SUBRESOURCE_FIELD_NUMBER: ClassVar[int]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
    STREAM_ALL_FIELD_NUMBER: ClassVar[int]
    STREAM_FROM_DATE_FIELD_NUMBER: ClassVar[int]
    STREAM_FROM_SEQUENCE_FIELD_NUMBER: ClassVar[int]
    STREAM_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    include_subresource: bool
    resource: CreateEventStreamingGroupRequest.EventResources
    resource_id: str
    stream_all: StreamAll
    stream_from_date: StreamFromDate
    stream_from_sequence: StreamFromSequence
    stream_group_id: str
    def __init__(self, resource: Optional[Union[CreateEventStreamingGroupRequest.EventResources, str]] = ..., resource_id: Optional[str] = ..., include_subresource: bool = ..., stream_all: Optional[Union[StreamAll, Mapping]] = ..., stream_from_date: Optional[Union[StreamFromDate, Mapping]] = ..., stream_from_sequence: Optional[Union[StreamFromSequence, Mapping]] = ..., stream_group_id: Optional[str] = ...) -> None: ...

class CreateEventStreamingGroupResponse(_message.Message):
    __slots__ = ["stream_group_id"]
    STREAM_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    stream_group_id: str
    def __init__(self, stream_group_id: Optional[str] = ...) -> None: ...

class EventNotificationMessage(_message.Message):
    __slots__ = ["resource", "resource_id", "updated_type"]
    class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: ClassVar[int]
    UPDATED_TYPE_FIELD_NUMBER: ClassVar[int]
    UPDATE_TYPE_AVAILABLE: EventNotificationMessage.UpdateType
    UPDATE_TYPE_CREATED: EventNotificationMessage.UpdateType
    UPDATE_TYPE_DELETED: EventNotificationMessage.UpdateType
    UPDATE_TYPE_METADATA_UPDATED: EventNotificationMessage.UpdateType
    UPDATE_TYPE_UNSPECIFIED: EventNotificationMessage.UpdateType
    UPDATE_TYPE_UPDATED: EventNotificationMessage.UpdateType
    resource: _common_models_pb2.Resource
    resource_id: str
    updated_type: EventNotificationMessage.UpdateType
    def __init__(self, resource: Optional[Union[_common_models_pb2.Resource, str]] = ..., resource_id: Optional[str] = ..., updated_type: Optional[Union[EventNotificationMessage.UpdateType, str]] = ...) -> None: ...

class NotficationStreamAck(_message.Message):
    __slots__ = ["ack_chunk_id"]
    ACK_CHUNK_ID_FIELD_NUMBER: ClassVar[int]
    ack_chunk_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ack_chunk_id: Optional[Iterable[str]] = ...) -> None: ...

class NotificationStreamGroupRequest(_message.Message):
    __slots__ = ["ack", "close", "init"]
    ACK_FIELD_NUMBER: ClassVar[int]
    CLOSE_FIELD_NUMBER: ClassVar[int]
    INIT_FIELD_NUMBER: ClassVar[int]
    ack: NotficationStreamAck
    close: bool
    init: NotificationStreamInit
    def __init__(self, init: Optional[Union[NotificationStreamInit, Mapping]] = ..., ack: Optional[Union[NotficationStreamAck, Mapping]] = ..., close: bool = ...) -> None: ...

class NotificationStreamGroupResponse(_message.Message):
    __slots__ = ["ack_chunk_id", "notification"]
    ACK_CHUNK_ID_FIELD_NUMBER: ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: ClassVar[int]
    ack_chunk_id: str
    notification: _containers.RepeatedCompositeFieldContainer[NotificationStreamResponse]
    def __init__(self, notification: Optional[Iterable[Union[NotificationStreamResponse, Mapping]]] = ..., ack_chunk_id: Optional[str] = ...) -> None: ...

class NotificationStreamInit(_message.Message):
    __slots__ = ["stream_group_id"]
    STREAM_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    stream_group_id: str
    def __init__(self, stream_group_id: Optional[str] = ...) -> None: ...

class NotificationStreamResponse(_message.Message):
    __slots__ = ["message", "sequence", "timestamp"]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    SEQUENCE_FIELD_NUMBER: ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    message: EventNotificationMessage
    sequence: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, message: Optional[Union[EventNotificationMessage, Mapping]] = ..., sequence: Optional[int] = ..., timestamp: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class StreamAll(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StreamFromDate(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class StreamFromSequence(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: ClassVar[int]
    sequence: int
    def __init__(self, sequence: Optional[int] = ...) -> None: ...
