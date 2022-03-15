from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
RESOURCE_DATASET: Resource
RESOURCE_DATASET_VERSION: Resource
RESOURCE_OBJECT: Resource
RESOURCE_OBJECT_GROUP: Resource
RESOURCE_OBJECT_GROUP_REVISION: Resource
RESOURCE_PROJECT: Resource
RESOURCE_UNSPECIFIED: Resource
RIGHT_READ: Right
RIGHT_UNSPECIFIED: Right
RIGHT_WRITE: Right
STATUS_ARCHIVED: Status
STATUS_AVAILABLE: Status
STATUS_DELETING: Status
STATUS_INITIATING: Status
STATUS_UNSPECIFIED: Status
STATUS_UPDATING: Status

class APIToken(_message.Message):
    __slots__ = ["id", "project_id", "rights", "token"]
    ID_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    RIGHTS_FIELD_NUMBER: ClassVar[int]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    id: str
    project_id: str
    rights: _containers.RepeatedScalarFieldContainer[Right]
    token: str
    def __init__(self, id: Optional[str] = ..., token: Optional[str] = ..., rights: Optional[Iterable[Union[Right, str]]] = ..., project_id: Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class Index(_message.Message):
    __slots__ = ["end_byte", "start_byte"]
    END_BYTE_FIELD_NUMBER: ClassVar[int]
    START_BYTE_FIELD_NUMBER: ClassVar[int]
    end_byte: int
    start_byte: int
    def __init__(self, start_byte: Optional[int] = ..., end_byte: Optional[int] = ...) -> None: ...

class IndexedObjectLocation(_message.Message):
    __slots__ = ["bucket", "index", "key", "url"]
    BUCKET_FIELD_NUMBER: ClassVar[int]
    INDEX_FIELD_NUMBER: ClassVar[int]
    KEY_FIELD_NUMBER: ClassVar[int]
    URL_FIELD_NUMBER: ClassVar[int]
    bucket: str
    index: Index
    key: str
    url: str
    def __init__(self, bucket: Optional[str] = ..., key: Optional[str] = ..., url: Optional[str] = ..., index: Optional[Union[Index, Mapping]] = ...) -> None: ...

class Label(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    key: str
    value: str
    def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ["object_index_location", "object_location"]
    OBJECT_INDEX_LOCATION_FIELD_NUMBER: ClassVar[int]
    OBJECT_LOCATION_FIELD_NUMBER: ClassVar[int]
    object_index_location: IndexedObjectLocation
    object_location: ObjectLocation
    def __init__(self, object_location: Optional[Union[ObjectLocation, Mapping]] = ..., object_index_location: Optional[Union[IndexedObjectLocation, Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["key", "labels", "metadata", "simple_schema"]
    KEY_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    SIMPLE_SCHEMA_FIELD_NUMBER: ClassVar[int]
    key: str
    labels: _containers.RepeatedCompositeFieldContainer[Label]
    metadata: bytes
    simple_schema: str
    def __init__(self, key: Optional[str] = ..., labels: Optional[Iterable[Union[Label, Mapping]]] = ..., metadata: Optional[bytes] = ..., simple_schema: Optional[str] = ...) -> None: ...

class ObjectLocation(_message.Message):
    __slots__ = ["bucket", "key", "url"]
    BUCKET_FIELD_NUMBER: ClassVar[int]
    KEY_FIELD_NUMBER: ClassVar[int]
    URL_FIELD_NUMBER: ClassVar[int]
    bucket: str
    key: str
    url: str
    def __init__(self, bucket: Optional[str] = ..., key: Optional[str] = ..., url: Optional[str] = ...) -> None: ...

class Origin(_message.Message):
    __slots__ = ["link", "object_location", "origin_type"]
    class OriginType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    LINK_FIELD_NUMBER: ClassVar[int]
    OBJECT_LOCATION_FIELD_NUMBER: ClassVar[int]
    ORIGIN_TYPE_FIELD_NUMBER: ClassVar[int]
    ORIGIN_TYPE_OBJECT_STORAGE: Origin.OriginType
    ORIGIN_TYPE_ORIGIN_LINK: Origin.OriginType
    ORIGIN_TYPE_UNSPECIFIED: Origin.OriginType
    link: str
    object_location: ObjectLocation
    origin_type: Origin.OriginType
    def __init__(self, link: Optional[str] = ..., object_location: Optional[Union[ObjectLocation, Mapping]] = ..., origin_type: Optional[Union[Origin.OriginType, str]] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ["last_uuid", "page_size"]
    LAST_UUID_FIELD_NUMBER: ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: ClassVar[int]
    last_uuid: str
    page_size: int
    def __init__(self, last_uuid: Optional[str] = ..., page_size: Optional[int] = ...) -> None: ...

class UpdateFieldsRequest(_message.Message):
    __slots__ = ["id", "updated_string_fields"]
    class UpdatedStringFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: ClassVar[int]
    UPDATED_STRING_FIELDS_FIELD_NUMBER: ClassVar[int]
    id: str
    updated_string_fields: _containers.ScalarMap[str, str]
    def __init__(self, id: Optional[str] = ..., updated_string_fields: Optional[Mapping[str, str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["resource", "rights", "user_id"]
    RESOURCE_FIELD_NUMBER: ClassVar[int]
    RIGHTS_FIELD_NUMBER: ClassVar[int]
    USER_ID_FIELD_NUMBER: ClassVar[int]
    resource: Resource
    rights: _containers.RepeatedScalarFieldContainer[Right]
    user_id: str
    def __init__(self, user_id: Optional[str] = ..., rights: Optional[Iterable[Union[Right, str]]] = ..., resource: Optional[Union[Resource, str]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["major", "minor", "patch", "revision", "stage"]
    class VersionStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    MAJOR_FIELD_NUMBER: ClassVar[int]
    MINOR_FIELD_NUMBER: ClassVar[int]
    PATCH_FIELD_NUMBER: ClassVar[int]
    REVISION_FIELD_NUMBER: ClassVar[int]
    STAGE_FIELD_NUMBER: ClassVar[int]
    VERSION_STAGE_ALPHA: Version.VersionStage
    VERSION_STAGE_BETA: Version.VersionStage
    VERSION_STAGE_RC: Version.VersionStage
    VERSION_STAGE_STABLE: Version.VersionStage
    VERSION_STAGE_UNSPECIFIED: Version.VersionStage
    major: int
    minor: int
    patch: int
    revision: int
    stage: Version.VersionStage
    def __init__(self, major: Optional[int] = ..., minor: Optional[int] = ..., patch: Optional[int] = ..., revision: Optional[int] = ..., stage: Optional[Union[Version.VersionStage, str]] = ...) -> None: ...

class VersionTag(_message.Message):
    __slots__ = ["name", "version_id"]
    NAME_FIELD_NUMBER: ClassVar[int]
    VERSION_ID_FIELD_NUMBER: ClassVar[int]
    name: str
    version_id: str
    def __init__(self, name: Optional[str] = ..., version_id: Optional[str] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Right(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Resource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
