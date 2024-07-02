from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetStorageVersionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SemanticVersion(_message.Message):
    __slots__ = ("version_string", "major", "minor", "patch", "labels")
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
    __slots__ = ("location", "version")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    location: str
    version: _containers.RepeatedCompositeFieldContainer[ComponentVersion]
    def __init__(self, location: _Optional[str] = ..., version: _Optional[_Iterable[_Union[ComponentVersion, _Mapping]]] = ...) -> None: ...

class ComponentVersion(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: SemanticVersion
    def __init__(self, name: _Optional[str] = ..., version: _Optional[_Union[SemanticVersion, _Mapping]] = ...) -> None: ...

class GetStorageVersionResponse(_message.Message):
    __slots__ = ("location_version",)
    LOCATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    location_version: _containers.RepeatedCompositeFieldContainer[LocationVersion]
    def __init__(self, location_version: _Optional[_Iterable[_Union[LocationVersion, _Mapping]]] = ...) -> None: ...

class GetStorageStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LocationStatus(_message.Message):
    __slots__ = ("location", "component_status")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    location: str
    component_status: _containers.RepeatedCompositeFieldContainer[ComponentStatus]
    def __init__(self, location: _Optional[str] = ..., component_status: _Optional[_Iterable[_Union[ComponentStatus, _Mapping]]] = ...) -> None: ...

class ComponentStatus(_message.Message):
    __slots__ = ("name", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: _models_pb2.ComponentStatus
    def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[_models_pb2.ComponentStatus, str]] = ...) -> None: ...

class GetStorageStatusResponse(_message.Message):
    __slots__ = ("location_status",)
    LOCATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    location_status: _containers.RepeatedCompositeFieldContainer[LocationStatus]
    def __init__(self, location_status: _Optional[_Iterable[_Union[LocationStatus, _Mapping]]] = ...) -> None: ...

class GetPubkeysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetPubkeysResponse(_message.Message):
    __slots__ = ("pubkeys",)
    PUBKEYS_FIELD_NUMBER: _ClassVar[int]
    pubkeys: _containers.RepeatedCompositeFieldContainer[_models_pb2.Pubkey]
    def __init__(self, pubkeys: _Optional[_Iterable[_Union[_models_pb2.Pubkey, _Mapping]]] = ...) -> None: ...

class Announcement(_message.Message):
    __slots__ = ("announcement_id", "announcement_type", "title", "teaser", "image_url", "content", "created_by", "created_at", "modified_by", "modified_at")
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEASER_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    announcement_type: _models_pb2.AnnouncementType
    title: str
    teaser: str
    image_url: str
    content: str
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    modified_by: str
    modified_at: _timestamp_pb2.Timestamp
    def __init__(self, announcement_id: _Optional[str] = ..., announcement_type: _Optional[_Union[_models_pb2.AnnouncementType, str]] = ..., title: _Optional[str] = ..., teaser: _Optional[str] = ..., image_url: _Optional[str] = ..., content: _Optional[str] = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., modified_by: _Optional[str] = ..., modified_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SetAnnouncementsRequest(_message.Message):
    __slots__ = ("announcements_upsert", "announcements_delete")
    ANNOUNCEMENTS_UPSERT_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENTS_DELETE_FIELD_NUMBER: _ClassVar[int]
    announcements_upsert: _containers.RepeatedCompositeFieldContainer[Announcement]
    announcements_delete: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, announcements_upsert: _Optional[_Iterable[_Union[Announcement, _Mapping]]] = ..., announcements_delete: _Optional[_Iterable[str]] = ...) -> None: ...

class SetAnnouncementsResponse(_message.Message):
    __slots__ = ("announcements",)
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[Announcement]
    def __init__(self, announcements: _Optional[_Iterable[_Union[Announcement, _Mapping]]] = ...) -> None: ...

class GetAnnouncementsRequest(_message.Message):
    __slots__ = ("announcement_ids", "page")
    ANNOUNCEMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    announcement_ids: _containers.RepeatedScalarFieldContainer[str]
    page: _models_pb2.PageRequest
    def __init__(self, announcement_ids: _Optional[_Iterable[str]] = ..., page: _Optional[_Union[_models_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetAnnouncementsResponse(_message.Message):
    __slots__ = ("announcements",)
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[Announcement]
    def __init__(self, announcements: _Optional[_Iterable[_Union[Announcement, _Mapping]]] = ...) -> None: ...

class GetAnnouncementsByTypeRequest(_message.Message):
    __slots__ = ("announcement_type", "page")
    ANNOUNCEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    announcement_type: _models_pb2.AnnouncementType
    page: _models_pb2.PageRequest
    def __init__(self, announcement_type: _Optional[_Union[_models_pb2.AnnouncementType, str]] = ..., page: _Optional[_Union[_models_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class GetAnnouncementsByTypeResponse(_message.Message):
    __slots__ = ("announcements",)
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    announcements: _containers.RepeatedCompositeFieldContainer[Announcement]
    def __init__(self, announcements: _Optional[_Iterable[_Union[Announcement, _Mapping]]] = ...) -> None: ...

class GetAnnouncementRequest(_message.Message):
    __slots__ = ("announcement_id",)
    ANNOUNCEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    announcement_id: str
    def __init__(self, announcement_id: _Optional[str] = ...) -> None: ...

class GetAnnouncementResponse(_message.Message):
    __slots__ = ("announcement",)
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    announcement: Announcement
    def __init__(self, announcement: _Optional[_Union[Announcement, _Mapping]] = ...) -> None: ...
