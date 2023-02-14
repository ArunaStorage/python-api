from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DATA_CLASS_CONFIDENTIAL: DataClass
DATA_CLASS_PRIVATE: DataClass
DATA_CLASS_PROTECTED: DataClass
DATA_CLASS_PUBLIC: DataClass
DATA_CLASS_UNSPECIFIED: DataClass
DESCRIPTOR: _descriptor.FileDescriptor
ENDPOINT_TYPE_FILE: EndpointType
ENDPOINT_TYPE_S3: EndpointType
ENDPOINT_TYPE_UNSPECIFIED: EndpointType
HASHALGORITHM_MD5: Hashalgorithm
HASHALGORITHM_SHA256: Hashalgorithm
HASHALGORITHM_UNSPECIFIED: Hashalgorithm
RESOURCE_ACTION_APPEND: ResourceAction
RESOURCE_ACTION_CREATE: ResourceAction
RESOURCE_ACTION_DELETE: ResourceAction
RESOURCE_ACTION_READ: ResourceAction
RESOURCE_ACTION_UNSPECIFIED: ResourceAction
RESOURCE_ACTION_UPDATE: ResourceAction
RESOURCE_TYPE_ALL: ResourceType
RESOURCE_TYPE_COLLECTION: ResourceType
RESOURCE_TYPE_OBJECT: ResourceType
RESOURCE_TYPE_OBJECT_GROUP: ResourceType
RESOURCE_TYPE_PROJECT: ResourceType
RESOURCE_TYPE_UNSPECIFIED: ResourceType
SOURCE_TYPE_DOI: SourceType
SOURCE_TYPE_UNSPECIFIED: SourceType
SOURCE_TYPE_URL: SourceType
STATUS_AVAILABLE: Status
STATUS_ERROR: Status
STATUS_INITIALIZING: Status
STATUS_TRASH: Status
STATUS_UNAVAILABLE: Status
STATUS_UNSPECIFIED: Status

class Collection(_message.Message):
    __slots__ = ["created", "description", "hooks", "id", "is_public", "label_ontology", "labels", "latest", "name", "object_groups", "objects", "semantic_version", "specifications", "stats"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    is_public: bool
    label_ontology: LabelOntology
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    latest: bool
    name: str
    object_groups: _containers.RepeatedCompositeFieldContainer[ObjectGroup]
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    semantic_version: Version
    specifications: _containers.RepeatedCompositeFieldContainer[Object]
    stats: CollectionStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., label_ontology: _Optional[_Union[LabelOntology, _Mapping]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., specifications: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., object_groups: _Optional[_Iterable[_Union[ObjectGroup, _Mapping]]] = ..., semantic_version: _Optional[_Union[Version, _Mapping]] = ..., latest: bool = ..., stats: _Optional[_Union[CollectionStats, _Mapping]] = ..., is_public: bool = ...) -> None: ...

class CollectionOverview(_message.Message):
    __slots__ = ["created", "description", "hooks", "id", "is_public", "label_ontology", "labels", "latest", "name", "semantic_version", "stats"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    is_public: bool
    label_ontology: LabelOntology
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    latest: bool
    name: str
    semantic_version: Version
    stats: CollectionStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., label_ontology: _Optional[_Union[LabelOntology, _Mapping]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., semantic_version: _Optional[_Union[Version, _Mapping]] = ..., latest: bool = ..., stats: _Optional[_Union[CollectionStats, _Mapping]] = ..., is_public: bool = ...) -> None: ...

class CollectionOverviews(_message.Message):
    __slots__ = ["collection_overviews"]
    COLLECTION_OVERVIEWS_FIELD_NUMBER: _ClassVar[int]
    collection_overviews: _containers.RepeatedCompositeFieldContainer[CollectionOverview]
    def __init__(self, collection_overviews: _Optional[_Iterable[_Union[CollectionOverview, _Mapping]]] = ...) -> None: ...

class CollectionStats(_message.Message):
    __slots__ = ["last_updated", "object_group_count", "object_stats"]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STATS_FIELD_NUMBER: _ClassVar[int]
    last_updated: _timestamp_pb2.Timestamp
    object_group_count: int
    object_stats: Stats
    def __init__(self, object_stats: _Optional[_Union[Stats, _Mapping]] = ..., object_group_count: _Optional[int] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CollectionWithID(_message.Message):
    __slots__ = ["created", "description", "hooks", "id", "is_public", "label_ontology", "labels", "latest", "name", "object_groups", "objects", "semantic_version", "specifications", "stats"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LABEL_ONTOLOGY_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SEMANTIC_VERSION_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    created: _timestamp_pb2.Timestamp
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    is_public: bool
    label_ontology: LabelOntology
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    latest: bool
    name: str
    object_groups: _containers.RepeatedScalarFieldContainer[str]
    objects: _containers.RepeatedScalarFieldContainer[str]
    semantic_version: Version
    specifications: _containers.RepeatedScalarFieldContainer[str]
    stats: CollectionStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., label_ontology: _Optional[_Union[LabelOntology, _Mapping]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., objects: _Optional[_Iterable[str]] = ..., specifications: _Optional[_Iterable[str]] = ..., object_groups: _Optional[_Iterable[str]] = ..., semantic_version: _Optional[_Union[Version, _Mapping]] = ..., latest: bool = ..., stats: _Optional[_Union[CollectionStats, _Mapping]] = ..., is_public: bool = ...) -> None: ...

class CollectionWithIDs(_message.Message):
    __slots__ = ["collection_with_ids"]
    COLLECTION_WITH_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_with_ids: _containers.RepeatedCompositeFieldContainer[CollectionWithID]
    def __init__(self, collection_with_ids: _Optional[_Iterable[_Union[CollectionWithID, _Mapping]]] = ...) -> None: ...

class Collections(_message.Message):
    __slots__ = ["collections"]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedCompositeFieldContainer[Collection]
    def __init__(self, collections: _Optional[_Iterable[_Union[Collection, _Mapping]]] = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ["documentation_path", "ep_type", "id", "internal_hostname", "is_default", "is_public", "name", "proxy_hostname"]
    DOCUMENTATION_PATH_FIELD_NUMBER: _ClassVar[int]
    EP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROXY_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    documentation_path: str
    ep_type: EndpointType
    id: str
    internal_hostname: str
    is_default: bool
    is_public: bool
    name: str
    proxy_hostname: str
    def __init__(self, id: _Optional[str] = ..., ep_type: _Optional[_Union[EndpointType, str]] = ..., name: _Optional[str] = ..., proxy_hostname: _Optional[str] = ..., internal_hostname: _Optional[str] = ..., documentation_path: _Optional[str] = ..., is_public: bool = ..., is_default: bool = ...) -> None: ...

class Hash(_message.Message):
    __slots__ = ["alg", "hash"]
    ALG_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    alg: Hashalgorithm
    hash: str
    def __init__(self, alg: _Optional[_Union[Hashalgorithm, str]] = ..., hash: _Optional[str] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class LabelOntology(_message.Message):
    __slots__ = ["required_label_keys"]
    REQUIRED_LABEL_KEYS_FIELD_NUMBER: _ClassVar[int]
    required_label_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, required_label_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ["auto_update", "content_len", "created", "data_class", "filename", "hash", "hooks", "id", "labels", "latest", "origin", "rev_number", "source", "status"]
    AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LATEST_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REV_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    auto_update: bool
    content_len: int
    created: _timestamp_pb2.Timestamp
    data_class: DataClass
    filename: str
    hash: Hash
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    latest: bool
    origin: Origin
    rev_number: int
    source: Source
    status: Status
    def __init__(self, id: _Optional[str] = ..., filename: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., content_len: _Optional[int] = ..., status: _Optional[_Union[Status, str]] = ..., origin: _Optional[_Union[Origin, _Mapping]] = ..., data_class: _Optional[_Union[DataClass, str]] = ..., hash: _Optional[_Union[Hash, _Mapping]] = ..., rev_number: _Optional[int] = ..., source: _Optional[_Union[Source, _Mapping]] = ..., latest: bool = ..., auto_update: bool = ...) -> None: ...

class ObjectGroup(_message.Message):
    __slots__ = ["description", "hooks", "id", "labels", "meta_objects", "name", "objects", "rev_number", "stats"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    META_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    REV_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    meta_objects: _containers.RepeatedCompositeFieldContainer[Object]
    name: str
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    rev_number: int
    stats: ObjectGroupStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., objects: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., meta_objects: _Optional[_Iterable[_Union[Object, _Mapping]]] = ..., stats: _Optional[_Union[ObjectGroupStats, _Mapping]] = ..., rev_number: _Optional[int] = ...) -> None: ...

class ObjectGroupOverview(_message.Message):
    __slots__ = ["description", "hooks", "id", "labels", "name", "rev_number", "stats"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REV_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    name: str
    rev_number: int
    stats: ObjectGroupStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., stats: _Optional[_Union[ObjectGroupStats, _Mapping]] = ..., rev_number: _Optional[int] = ...) -> None: ...

class ObjectGroupOverviews(_message.Message):
    __slots__ = ["object_group_overviews"]
    OBJECT_GROUP_OVERVIEWS_FIELD_NUMBER: _ClassVar[int]
    object_group_overviews: _containers.RepeatedCompositeFieldContainer[ObjectGroupOverview]
    def __init__(self, object_group_overviews: _Optional[_Iterable[_Union[ObjectGroupOverview, _Mapping]]] = ...) -> None: ...

class ObjectGroupStats(_message.Message):
    __slots__ = ["last_updated", "object_stats"]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    OBJECT_STATS_FIELD_NUMBER: _ClassVar[int]
    last_updated: _timestamp_pb2.Timestamp
    object_stats: Stats
    def __init__(self, object_stats: _Optional[_Union[Stats, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ObjectGroupWithID(_message.Message):
    __slots__ = ["description", "hooks", "id", "labels", "meta_object_ids", "name", "object_ids", "rev_number", "stats"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    META_OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    REV_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    description: str
    hooks: _containers.RepeatedCompositeFieldContainer[KeyValue]
    id: str
    labels: _containers.RepeatedCompositeFieldContainer[KeyValue]
    meta_object_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    object_ids: _containers.RepeatedScalarFieldContainer[str]
    rev_number: int
    stats: ObjectGroupStats
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., labels: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., object_ids: _Optional[_Iterable[str]] = ..., meta_object_ids: _Optional[_Iterable[str]] = ..., stats: _Optional[_Union[ObjectGroupStats, _Mapping]] = ..., rev_number: _Optional[int] = ...) -> None: ...

class ObjectGroupWithIDs(_message.Message):
    __slots__ = ["object_group_with_ids"]
    OBJECT_GROUP_WITH_IDS_FIELD_NUMBER: _ClassVar[int]
    object_group_with_ids: _containers.RepeatedCompositeFieldContainer[ObjectGroupWithID]
    def __init__(self, object_group_with_ids: _Optional[_Iterable[_Union[ObjectGroupWithID, _Mapping]]] = ...) -> None: ...

class ObjectGroups(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    object_groups: _containers.RepeatedCompositeFieldContainer[ObjectGroup]
    def __init__(self, object_groups: _Optional[_Iterable[_Union[ObjectGroup, _Mapping]]] = ...) -> None: ...

class Objects(_message.Message):
    __slots__ = ["objects"]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[Object]
    def __init__(self, objects: _Optional[_Iterable[_Union[Object, _Mapping]]] = ...) -> None: ...

class Origin(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Source(_message.Message):
    __slots__ = ["identifier", "source_type"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    source_type: SourceType
    def __init__(self, identifier: _Optional[str] = ..., source_type: _Optional[_Union[SourceType, str]] = ...) -> None: ...

class Stats(_message.Message):
    __slots__ = ["acc_size", "count"]
    ACC_SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    acc_size: int
    count: int
    def __init__(self, count: _Optional[int] = ..., acc_size: _Optional[int] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["major", "minor", "patch"]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ...) -> None: ...

class ResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ResourceAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Hashalgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DataClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class EndpointType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
