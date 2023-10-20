from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EVENT_VARIANT_UNSPECIFIED: _ClassVar[EventVariant]
    EVENT_VARIANT_CREATED: _ClassVar[EventVariant]
    EVENT_VARIANT_AVAILABLE: _ClassVar[EventVariant]
    EVENT_VARIANT_UPDATED: _ClassVar[EventVariant]
    EVENT_VARIANT_DELETED: _ClassVar[EventVariant]
    EVENT_VARIANT_SNAPSHOTTED: _ClassVar[EventVariant]
EVENT_VARIANT_UNSPECIFIED: EventVariant
EVENT_VARIANT_CREATED: EventVariant
EVENT_VARIANT_AVAILABLE: EventVariant
EVENT_VARIANT_UPDATED: EventVariant
EVENT_VARIANT_DELETED: EventVariant
EVENT_VARIANT_SNAPSHOTTED: EventVariant

class Resource(_message.Message):
    __slots__ = ["resource_id", "persistent_resource_id", "checksum", "resource_variant"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    PERSISTENT_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    persistent_resource_id: bool
    checksum: str
    resource_variant: _models_pb2.ResourceVariant
    def __init__(self, resource_id: _Optional[str] = ..., persistent_resource_id: bool = ..., checksum: _Optional[str] = ..., resource_variant: _Optional[_Union[_models_pb2.ResourceVariant, str]] = ...) -> None: ...

class ResourceTarget(_message.Message):
    __slots__ = ["resource_id", "resource_variant"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    resource_variant: _models_pb2.ResourceVariant
    def __init__(self, resource_id: _Optional[str] = ..., resource_variant: _Optional[_Union[_models_pb2.ResourceVariant, str]] = ...) -> None: ...

class CreateStreamConsumerRequest(_message.Message):
    __slots__ = ["resource", "user", "anouncements", "all", "include_subresources", "stream_all", "stream_from_date", "stream_from_sequence"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ANOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUBRESOURCES_FIELD_NUMBER: _ClassVar[int]
    STREAM_ALL_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_DATE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FROM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    resource: ResourceTarget
    user: str
    anouncements: bool
    all: bool
    include_subresources: bool
    stream_all: StreamAll
    stream_from_date: StreamFromDate
    stream_from_sequence: StreamFromSequence
    def __init__(self, resource: _Optional[_Union[ResourceTarget, _Mapping]] = ..., user: _Optional[str] = ..., anouncements: bool = ..., all: bool = ..., include_subresources: bool = ..., stream_all: _Optional[_Union[StreamAll, _Mapping]] = ..., stream_from_date: _Optional[_Union[StreamFromDate, _Mapping]] = ..., stream_from_sequence: _Optional[_Union[StreamFromSequence, _Mapping]] = ...) -> None: ...

class CreateStreamConsumerResponse(_message.Message):
    __slots__ = ["stream_consumer"]
    STREAM_CONSUMER_FIELD_NUMBER: _ClassVar[int]
    stream_consumer: str
    def __init__(self, stream_consumer: _Optional[str] = ...) -> None: ...

class GetEventMessageBatchRequest(_message.Message):
    __slots__ = ["stream_consumer", "batch_size"]
    STREAM_CONSUMER_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    stream_consumer: str
    batch_size: int
    def __init__(self, stream_consumer: _Optional[str] = ..., batch_size: _Optional[int] = ...) -> None: ...

class GetEventMessageBatchResponse(_message.Message):
    __slots__ = ["messages"]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[EventMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[EventMessage, _Mapping]]] = ...) -> None: ...

class GetEventMessageStreamRequest(_message.Message):
    __slots__ = ["stream_consumer"]
    STREAM_CONSUMER_FIELD_NUMBER: _ClassVar[int]
    stream_consumer: str
    def __init__(self, stream_consumer: _Optional[str] = ...) -> None: ...

class GetEventMessageStreamResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: EventMessage
    def __init__(self, message: _Optional[_Union[EventMessage, _Mapping]] = ...) -> None: ...

class AcknowledgeMessageBatchRequest(_message.Message):
    __slots__ = ["replies"]
    REPLIES_FIELD_NUMBER: _ClassVar[int]
    replies: _containers.RepeatedCompositeFieldContainer[Reply]
    def __init__(self, replies: _Optional[_Iterable[_Union[Reply, _Mapping]]] = ...) -> None: ...

class AcknowledgeMessageBatchResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteStreamConsumerRequest(_message.Message):
    __slots__ = ["stream_consumer"]
    STREAM_CONSUMER_FIELD_NUMBER: _ClassVar[int]
    stream_consumer: str
    def __init__(self, stream_consumer: _Optional[str] = ...) -> None: ...

class DeleteStreamConsumerResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StreamFromSequence(_message.Message):
    __slots__ = ["sequence"]
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    def __init__(self, sequence: _Optional[int] = ...) -> None: ...

class StreamFromDate(_message.Message):
    __slots__ = ["timestamp"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamAll(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EventMessage(_message.Message):
    __slots__ = ["resource_event", "user_event", "announcement_event"]
    RESOURCE_EVENT_FIELD_NUMBER: _ClassVar[int]
    USER_EVENT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_EVENT_FIELD_NUMBER: _ClassVar[int]
    resource_event: ResourceEvent
    user_event: UserEvent
    announcement_event: AnouncementEvent
    def __init__(self, resource_event: _Optional[_Union[ResourceEvent, _Mapping]] = ..., user_event: _Optional[_Union[UserEvent, _Mapping]] = ..., announcement_event: _Optional[_Union[AnouncementEvent, _Mapping]] = ...) -> None: ...

class ResourceEvent(_message.Message):
    __slots__ = ["resource", "event_variant", "reply"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_VARIANT_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    resource: Resource
    event_variant: EventVariant
    reply: Reply
    def __init__(self, resource: _Optional[_Union[Resource, _Mapping]] = ..., event_variant: _Optional[_Union[EventVariant, str]] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class UserEvent(_message.Message):
    __slots__ = ["user_id", "event_variant", "checksum", "reply"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    event_variant: EventVariant
    checksum: str
    reply: Reply
    def __init__(self, user_id: _Optional[str] = ..., event_variant: _Optional[_Union[EventVariant, str]] = ..., checksum: _Optional[str] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...

class Reply(_message.Message):
    __slots__ = ["reply", "salt", "hmac"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    reply: str
    salt: str
    hmac: str
    def __init__(self, reply: _Optional[str] = ..., salt: _Optional[str] = ..., hmac: _Optional[str] = ...) -> None: ...

class ScheduledDowntime(_message.Message):
    __slots__ = ["location", "component", "to"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    location: str
    component: str
    to: _timestamp_pb2.Timestamp
    def __init__(self, location: _Optional[str] = ..., component: _Optional[str] = ..., to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class NewVersion(_message.Message):
    __slots__ = ["location", "component", "new_version"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_FIELD_NUMBER: _ClassVar[int]
    NEW_VERSION_FIELD_NUMBER: _ClassVar[int]
    location: str
    component: str
    new_version: str
    def __init__(self, location: _Optional[str] = ..., component: _Optional[str] = ..., new_version: _Optional[str] = ...) -> None: ...

class NewPubkey(_message.Message):
    __slots__ = ["pubkey"]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    pubkey: str
    def __init__(self, pubkey: _Optional[str] = ...) -> None: ...

class AnouncementEvent(_message.Message):
    __slots__ = ["new_data_proxy_id", "remove_data_proxy_id", "update_data_proxy_id", "new_pubkey", "remove_pubkey", "downtime", "version", "reply"]
    NEW_DATA_PROXY_ID_FIELD_NUMBER: _ClassVar[int]
    REMOVE_DATA_PROXY_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DATA_PROXY_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PUBKEY_FIELD_NUMBER: _ClassVar[int]
    DOWNTIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    new_data_proxy_id: str
    remove_data_proxy_id: str
    update_data_proxy_id: str
    new_pubkey: int
    remove_pubkey: int
    downtime: ScheduledDowntime
    version: NewVersion
    reply: Reply
    def __init__(self, new_data_proxy_id: _Optional[str] = ..., remove_data_proxy_id: _Optional[str] = ..., update_data_proxy_id: _Optional[str] = ..., new_pubkey: _Optional[int] = ..., remove_pubkey: _Optional[int] = ..., downtime: _Optional[_Union[ScheduledDowntime, _Mapping]] = ..., version: _Optional[_Union[NewVersion, _Mapping]] = ..., reply: _Optional[_Union[Reply, _Mapping]] = ...) -> None: ...
