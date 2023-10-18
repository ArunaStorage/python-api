from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStorageVersionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SemanticVersion(_message.Message):
    __slots__ = ["version_string", "major", "minor", "patch", "labels"]
    VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    version_string: str
    major: int
    minor: int
    patch: int
    labels: str
    def __init__(self, version_string: _Optional[str] = ..., major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ..., labels: _Optional[str] = ...) -> None: ...

class LocationVersion(_message.Message):
    __slots__ = ["location", "version"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    location: str
    version: _containers.RepeatedCompositeFieldContainer[ComponentVersion]
    def __init__(self, location: _Optional[str] = ..., version: _Optional[_Iterable[_Union[ComponentVersion, _Mapping]]] = ...) -> None: ...

class ComponentVersion(_message.Message):
    __slots__ = ["name", "version"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: SemanticVersion
    def __init__(self, name: _Optional[str] = ..., version: _Optional[_Union[SemanticVersion, _Mapping]] = ...) -> None: ...

class GetStorageVersionResponse(_message.Message):
    __slots__ = ["location_version"]
    LOCATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    location_version: _containers.RepeatedCompositeFieldContainer[LocationVersion]
    def __init__(self, location_version: _Optional[_Iterable[_Union[LocationVersion, _Mapping]]] = ...) -> None: ...

class GetStorageStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class LocationStatus(_message.Message):
    __slots__ = ["location", "component_status"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    location: str
    component_status: _containers.RepeatedCompositeFieldContainer[ComponentStatus]
    def __init__(self, location: _Optional[str] = ..., component_status: _Optional[_Iterable[_Union[ComponentStatus, _Mapping]]] = ...) -> None: ...

class ComponentStatus(_message.Message):
    __slots__ = ["name", "status"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: _models_pb2.ComponentStatus
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[_models_pb2.ComponentStatus, str]] = ...) -> None: ...

class GetStorageStatusResponse(_message.Message):
    __slots__ = ["location_status"]
    LOCATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    location_status: _containers.RepeatedCompositeFieldContainer[LocationStatus]
    def __init__(self, location_status: _Optional[_Iterable[_Union[LocationStatus, _Mapping]]] = ...) -> None: ...

class GetPubkeysRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPubkeysResponse(_message.Message):
    __slots__ = ["pubkeys"]
    PUBKEYS_FIELD_NUMBER: _ClassVar[int]
    pubkeys: _containers.RepeatedCompositeFieldContainer[_models_pb2.Pubkey]
    def __init__(self, pubkeys: _Optional[_Iterable[_Union[_models_pb2.Pubkey, _Mapping]]] = ...) -> None: ...

class Anouncement(_message.Message):
    __slots__ = ["id", "content", "created_at"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    content: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., content: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAnouncementsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAnouncementsResponse(_message.Message):
    __slots__ = ["anouncements"]
    ANOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    anouncements: _containers.RepeatedCompositeFieldContainer[Anouncement]
    def __init__(self, anouncements: _Optional[_Iterable[_Union[Anouncement, _Mapping]]] = ...) -> None: ...

class SetAnouncementsRequest(_message.Message):
    __slots__ = ["anouncements_upsert", "anouncements_delete"]
    ANOUNCEMENTS_UPSERT_FIELD_NUMBER: _ClassVar[int]
    ANOUNCEMENTS_DELETE_FIELD_NUMBER: _ClassVar[int]
    anouncements_upsert: _containers.RepeatedCompositeFieldContainer[Anouncement]
    anouncements_delete: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, anouncements_upsert: _Optional[_Iterable[_Union[Anouncement, _Mapping]]] = ..., anouncements_delete: _Optional[_Iterable[str]] = ...) -> None: ...

class SetAnouncementsResponse(_message.Message):
    __slots__ = ["anouncements"]
    ANOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    anouncements: _containers.RepeatedCompositeFieldContainer[Anouncement]
    def __init__(self, anouncements: _Optional[_Iterable[_Union[Anouncement, _Mapping]]] = ...) -> None: ...
