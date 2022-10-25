from google.api import visibility_pb2 as _visibility_pb2
from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from aruna.api.notification.services.v1 import notification_service_pb2 as _notification_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterEventRequest(_message.Message):
    __slots__ = ["event_resource", "event_type", "resource_id"]
    EVENT_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    event_resource: _models_pb2.ResourceType
    event_type: _notification_service_pb2.EventType
    resource_id: str
    def __init__(self, event_resource: _Optional[_Union[_models_pb2.ResourceType, str]] = ..., resource_id: _Optional[str] = ..., event_type: _Optional[_Union[_notification_service_pb2.EventType, str]] = ...) -> None: ...

class RegisterEventResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
