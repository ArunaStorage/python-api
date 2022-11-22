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

class CreateEventStreamingGroupRequest(_message.Message):
    __slots__ = ["include_subresource", "resource", "resource_id", "stream_all", "stream_from_date", "stream_from_sequence", "stream_group_id"]
    INCLUDE_SUBRESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ALL_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    include_subresource: bool
    resource: _models_pb2.ResourceType
    resource_id: str
    stream_all: StreamAll
    stream_from_date: StreamFromDate
    stream_from_sequence: StreamFromSequence
    stream_group_id: str
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., include_subresource: bool = ..., stream_all: _Optional[_Union[StreamAll, _Mapping]] = ..., stream_from_date: _Optional[_Union[StreamFromDate, _Mapping]] = ..., stream_from_sequence: _Optional[_Union[StreamFromSequence, _Mapping]] = ..., stream_group_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["resource", "resource_id", "updated_type"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource: _models_pb2.ResourceType
    resource_id: str
    updated_type: EventType
    def __init__(self, resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., updated_type: _Optional[_Union[EventType, str]] = ...) -> None: ...

class NotficationStreamAck(_message.Message):
    __slots__ = ["ack_chunk_id"]
    ACK_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    ack_chunk_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ack_chunk_id: _Optional[_Iterable[str]] = ...) -> None: ...

class NotificationStreamInit(_message.Message):
    __slots__ = ["stream_group_id"]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    stream_group_id: str
    def __init__(self, stream_group_id: _Optional[str] = ...) -> None: ...

class NotificationStreamResponse(_message.Message):
    __slots__ = ["message", "sequence", "timestamp"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message: EventNotificationMessage
    sequence: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, message: _Optional[_Union[EventNotificationMessage, _Mapping]] = ..., sequence: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ReadStreamGroupMessagesRequest(_message.Message):
    __slots__ = ["ack", "close", "init"]
    ACK_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    INIT_FIELD_NUMBER: _ClassVar[int]
    ack: NotficationStreamAck
    close: bool
    init: NotificationStreamInit
    def __init__(self, init: _Optional[_Union[NotificationStreamInit, _Mapping]] = ..., ack: _Optional[_Union[NotficationStreamAck, _Mapping]] = ..., close: bool = ...) -> None: ...

class ReadStreamGroupMessagesResponse(_message.Message):
    __slots__ = ["ack_chunk_id", "notification"]
    ACK_CHUNK_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    ack_chunk_id: str
    notification: _containers.RepeatedCompositeFieldContainer[NotificationStreamResponse]
    def __init__(self, notification: _Optional[_Iterable[_Union[NotificationStreamResponse, _Mapping]]] = ..., ack_chunk_id: _Optional[str] = ...) -> None: ...

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
