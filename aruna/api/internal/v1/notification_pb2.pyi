from google.api import visibility_pb2 as _visibility_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.notification.services.v1 import notification_service_pb2 as _notification_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateStreamGroupRequest(_message.Message):
    __slots__ = ["event_type", "notify_on_sub_resource", "resource_id", "resource_type", "token"]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_SUB_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    event_type: _notification_service_pb2.EventType
    notify_on_sub_resource: bool
    resource_id: str
    resource_type: _models_pb2.ResourceType
    token: str
    def __init__(self, token: _Optional[str] = ..., event_type: _Optional[_Union[_notification_service_pb2.EventType, str]] = ..., resource_type: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., notify_on_sub_resource: bool = ...) -> None: ...

class CreateStreamGroupResponse(_message.Message):
    __slots__ = ["stream_group"]
    STREAM_GROUP_FIELD_NUMBER: _ClassVar[int]
    stream_group: StreamGroup
    def __init__(self, stream_group: _Optional[_Union[StreamGroup, _Mapping]] = ...) -> None: ...

class DeleteStreamGroupRequest(_message.Message):
    __slots__ = ["stream_group_id", "token"]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    stream_group_id: str
    token: str
    def __init__(self, token: _Optional[str] = ..., stream_group_id: _Optional[str] = ...) -> None: ...

class DeleteStreamGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EmitEventRequest(_message.Message):
    __slots__ = ["event_resource", "event_type", "relations", "resource_id"]
    EVENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    event_resource: _models_pb2.ResourceType
    event_type: _notification_service_pb2.EventType
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    resource_id: str
    def __init__(self, event_resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., event_type: _Optional[_Union[_notification_service_pb2.EventType, str]] = ..., relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ...) -> None: ...

class EmitEventResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetSharedRevisionRequest(_message.Message):
    __slots__ = ["resource_id", "resource_type"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    resource_type: _models_pb2.ResourceType
    def __init__(self, resource_type: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ...) -> None: ...

class GetSharedRevisionResponse(_message.Message):
    __slots__ = ["shared_revision_id"]
    SHARED_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    shared_revision_id: str
    def __init__(self, shared_revision_id: _Optional[str] = ...) -> None: ...

class GetStreamGroupRequest(_message.Message):
    __slots__ = ["stream_group_id", "token"]
    STREAM_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    stream_group_id: str
    token: str
    def __init__(self, token: _Optional[str] = ..., stream_group_id: _Optional[str] = ...) -> None: ...

class GetStreamGroupResponse(_message.Message):
    __slots__ = ["stream_group"]
    STREAM_GROUP_FIELD_NUMBER: _ClassVar[int]
    stream_group: StreamGroup
    def __init__(self, stream_group: _Optional[_Union[StreamGroup, _Mapping]] = ...) -> None: ...

class ObjectGroupRelation(_message.Message):
    __slots__ = ["object_group_ids", "shared_object_group_id"]
    OBJECT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    SHARED_OBJECT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    object_group_ids: _containers.RepeatedScalarFieldContainer[str]
    shared_object_group_id: str
    def __init__(self, shared_object_group_id: _Optional[str] = ..., object_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class Relation(_message.Message):
    __slots__ = ["collection", "object_groups", "project", "shared_object"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    SHARED_OBJECT_FIELD_NUMBER: _ClassVar[int]
    collection: str
    object_groups: _containers.RepeatedCompositeFieldContainer[ObjectGroupRelation]
    project: str
    shared_object: str
    def __init__(self, shared_object: _Optional[str] = ..., object_groups: _Optional[_Iterable[_Union[ObjectGroupRelation, _Mapping]]] = ..., collection: _Optional[str] = ..., project: _Optional[str] = ...) -> None: ...

class StreamGroup(_message.Message):
    __slots__ = ["event_type", "id", "notify_on_sub_resource", "resource_id", "resource_type"]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_ON_SUB_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    event_type: _notification_service_pb2.EventType
    id: str
    notify_on_sub_resource: bool
    resource_id: str
    resource_type: _models_pb2.ResourceType
    def __init__(self, id: _Optional[str] = ..., event_type: _Optional[_Union[_notification_service_pb2.EventType, str]] = ..., resource_type: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., notify_on_sub_resource: bool = ...) -> None: ...
