from google.api import visibility_pb2 as _visibility_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.notification.services.v1 import notification_service_pb2 as _notification_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionResource(_message.Message):
    __slots__ = ["collection_id", "project_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    project_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["event_resource", "event_type", "resource_id", "resources"]
    EVENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    event_resource: _models_pb2.ResourceType
    event_type: _notification_service_pb2.EventType
    resource_id: str
    resources: _containers.RepeatedCompositeFieldContainer[EmittedResource]
    def __init__(self, event_resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., event_type: _Optional[_Union[_notification_service_pb2.EventType, str]] = ..., resources: _Optional[_Iterable[_Union[EmittedResource, _Mapping]]] = ...) -> None: ...

class EmitEventResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EmittedResource(_message.Message):
    __slots__ = ["collection", "object", "object_group", "project"]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUP_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    collection: CollectionResource
    object: ObjectResource
    object_group: ObjectGroupResource
    project: ProjectResource
    def __init__(self, project: _Optional[_Union[ProjectResource, _Mapping]] = ..., collection: _Optional[_Union[CollectionResource, _Mapping]] = ..., object: _Optional[_Union[ObjectResource, _Mapping]] = ..., object_group: _Optional[_Union[ObjectGroupResource, _Mapping]] = ...) -> None: ...

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

class ObjectGroupResource(_message.Message):
    __slots__ = ["collection_id", "object_group_id", "project_id", "shared_object_group_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SHARED_OBJECT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_group_id: str
    project_id: str
    shared_object_group_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., shared_object_group_id: _Optional[str] = ..., object_group_id: _Optional[str] = ...) -> None: ...

class ObjectResource(_message.Message):
    __slots__ = ["collection_id", "object_id", "project_id", "shared_object_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SHARED_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_id: str
    project_id: str
    shared_object_id: str
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., shared_object_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class ProjectResource(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

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
