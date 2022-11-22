from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
STATUS_AVAILABLE: Status
STATUS_DEGRADED: Status
STATUS_UNAVAILABLE: Status
STATUS_UNKNOWN: Status
STATUS_UNSPECIFIED: Status

class ComponentStatus(_message.Message):
    __slots__ = ["component_name", "location_status"]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    component_name: str
    location_status: _containers.RepeatedCompositeFieldContainer[LocationStatus]
    def __init__(self, component_name: _Optional[str] = ..., location_status: _Optional[_Iterable[_Union[LocationStatus, _Mapping]]] = ...) -> None: ...

class ComponentVersion(_message.Message):
    __slots__ = ["component_name", "location_version"]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    component_name: str
    location_version: _containers.RepeatedCompositeFieldContainer[LocationVersion]
    def __init__(self, component_name: _Optional[str] = ..., location_version: _Optional[_Iterable[_Union[LocationVersion, _Mapping]]] = ...) -> None: ...

class GetResourceHierarchyRequest(_message.Message):
    __slots__ = ["resource_id", "resource_type"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    resource_type: _models_pb2.ResourceType
    def __init__(self, resource_id: _Optional[str] = ..., resource_type: _Optional[_Union[_models_pb2.ResourceType, str]] = ...) -> None: ...

class GetResourceHierarchyResponse(_message.Message):
    __slots__ = ["hierarchies"]
    HIERARCHIES_FIELD_NUMBER: _ClassVar[int]
    hierarchies: _containers.RepeatedCompositeFieldContainer[Hierarchy]
    def __init__(self, hierarchies: _Optional[_Iterable[_Union[Hierarchy, _Mapping]]] = ...) -> None: ...

class GetStorageStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetStorageStatusResponse(_message.Message):
    __slots__ = ["component_status"]
    COMPONENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    component_status: _containers.RepeatedCompositeFieldContainer[ComponentStatus]
    def __init__(self, component_status: _Optional[_Iterable[_Union[ComponentStatus, _Mapping]]] = ...) -> None: ...

class GetStorageVersionRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetStorageVersionResponse(_message.Message):
    __slots__ = ["component_version"]
    COMPONENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    component_version: _containers.RepeatedCompositeFieldContainer[ComponentVersion]
    def __init__(self, component_version: _Optional[_Iterable[_Union[ComponentVersion, _Mapping]]] = ...) -> None: ...

class Hierarchy(_message.Message):
    __slots__ = ["collection_id", "object_group_ids", "object_id", "project_id"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    object_group_ids: _containers.RepeatedScalarFieldContainer[str]
    object_id: str
    project_id: str
    def __init__(self, object_id: _Optional[str] = ..., object_group_ids: _Optional[_Iterable[str]] = ..., collection_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class LocationStatus(_message.Message):
    __slots__ = ["location", "status"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    location: str
    status: Status
    def __init__(self, location: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class LocationVersion(_message.Message):
    __slots__ = ["location", "version"]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    location: str
    version: SemanticVersion
    def __init__(self, location: _Optional[str] = ..., version: _Optional[_Union[SemanticVersion, _Mapping]] = ...) -> None: ...

class SemanticVersion(_message.Message):
    __slots__ = ["labels", "major", "minor", "patch", "version_string"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    VERSION_STRING_FIELD_NUMBER: _ClassVar[int]
    labels: str
    major: int
    minor: int
    patch: int
    version_string: str
    def __init__(self, version_string: _Optional[str] = ..., major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ..., labels: _Optional[str] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
