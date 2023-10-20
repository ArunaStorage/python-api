from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DATA_CLASS_UNSPECIFIED: _ClassVar[DataClass]
    DATA_CLASS_PUBLIC: _ClassVar[DataClass]
    DATA_CLASS_PRIVATE: _ClassVar[DataClass]
    DATA_CLASS_WORKSPACE: _ClassVar[DataClass]
    DATA_CLASS_CONFIDENTIAL: _ClassVar[DataClass]

class EndpointVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ENDPOINT_VARIANT_UNSPECIFIED: _ClassVar[EndpointVariant]
    ENDPOINT_VARIANT_PERSISTENT: _ClassVar[EndpointVariant]
    ENDPOINT_VARIANT_VOLATILE: _ClassVar[EndpointVariant]

class EndpointHostVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    ENDPOINT_HOST_VARIANT_UNSPECIFIED: _ClassVar[EndpointHostVariant]
    ENDPOINT_HOST_VARIANT_GRPC: _ClassVar[EndpointHostVariant]
    ENDPOINT_HOST_VARIANT_S3: _ClassVar[EndpointHostVariant]

class PermissionLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PERMISSION_LEVEL_UNSPECIFIED: _ClassVar[PermissionLevel]
    PERMISSION_LEVEL_NONE: _ClassVar[PermissionLevel]
    PERMISSION_LEVEL_READ: _ClassVar[PermissionLevel]
    PERMISSION_LEVEL_APPEND: _ClassVar[PermissionLevel]
    PERMISSION_LEVEL_WRITE: _ClassVar[PermissionLevel]
    PERMISSION_LEVEL_ADMIN: _ClassVar[PermissionLevel]

class KeyValueVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    KEY_VALUE_VARIANT_UNSPECIFIED: _ClassVar[KeyValueVariant]
    KEY_VALUE_VARIANT_LABEL: _ClassVar[KeyValueVariant]
    KEY_VALUE_VARIANT_STATIC_LABEL: _ClassVar[KeyValueVariant]
    KEY_VALUE_VARIANT_HOOK: _ClassVar[KeyValueVariant]
    KEY_VALUE_VARIANT_HOOK_STATUS: _ClassVar[KeyValueVariant]

class ExternalRelationVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EXTERNAL_RELATION_VARIANT_UNSPECIFIED: _ClassVar[ExternalRelationVariant]
    EXTERNAL_RELATION_VARIANT_URL: _ClassVar[ExternalRelationVariant]
    EXTERNAL_RELATION_VARIANT_IDENTIFIER: _ClassVar[ExternalRelationVariant]
    EXTERNAL_RELATION_VARIANT_CUSTOM: _ClassVar[ExternalRelationVariant]

class InternalRelationVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INTERNAL_RELATION_VARIANT_UNSPECIFIED: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_BELONGS_TO: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_ORIGIN: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_VERSION: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_METADATA: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_POLICY: _ClassVar[InternalRelationVariant]
    INTERNAL_RELATION_VARIANT_CUSTOM: _ClassVar[InternalRelationVariant]

class RelationDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RELATION_DIRECTION_UNSPECIFIED: _ClassVar[RelationDirection]
    RELATION_DIRECTION_INBOUND: _ClassVar[RelationDirection]
    RELATION_DIRECTION_OUTBOUND: _ClassVar[RelationDirection]

class ResourceAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RESOURCE_ACTION_UNSPECIFIED: _ClassVar[ResourceAction]
    RESOURCE_ACTION_CREATE: _ClassVar[ResourceAction]
    RESOURCE_ACTION_APPEND: _ClassVar[ResourceAction]
    RESOURCE_ACTION_UPDATE: _ClassVar[ResourceAction]
    RESOURCE_ACTION_READ: _ClassVar[ResourceAction]
    RESOURCE_ACTION_DELETE: _ClassVar[ResourceAction]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    STATUS_UNSPECIFIED: _ClassVar[Status]
    STATUS_INITIALIZING: _ClassVar[Status]
    STATUS_VALIDATING: _ClassVar[Status]
    STATUS_AVAILABLE: _ClassVar[Status]
    STATUS_UNAVAILABLE: _ClassVar[Status]
    STATUS_ERROR: _ClassVar[Status]
    STATUS_DELETED: _ClassVar[Status]

class ComponentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPONENT_STATUS_UNSPECIFIED: _ClassVar[ComponentStatus]
    COMPONENT_STATUS_INITIALIZING: _ClassVar[ComponentStatus]
    COMPONENT_STATUS_AVAILABLE: _ClassVar[ComponentStatus]
    COMPONENT_STATUS_DEGRADED: _ClassVar[ComponentStatus]
    COMPONENT_STATUS_UNAVAILABLE: _ClassVar[ComponentStatus]
    COMPONENT_STATUS_MAINTENANCE: _ClassVar[ComponentStatus]

class Hashalgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    HASHALGORITHM_UNSPECIFIED: _ClassVar[Hashalgorithm]
    HASHALGORITHM_MD5: _ClassVar[Hashalgorithm]
    HASHALGORITHM_SHA256: _ClassVar[Hashalgorithm]

class ResourceVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RESOURCE_VARIANT_UNSPECIFIED: _ClassVar[ResourceVariant]
    RESOURCE_VARIANT_PROJECT: _ClassVar[ResourceVariant]
    RESOURCE_VARIANT_COLLECTION: _ClassVar[ResourceVariant]
    RESOURCE_VARIANT_DATASET: _ClassVar[ResourceVariant]
    RESOURCE_VARIANT_OBJECT: _ClassVar[ResourceVariant]
DATA_CLASS_UNSPECIFIED: DataClass
DATA_CLASS_PUBLIC: DataClass
DATA_CLASS_PRIVATE: DataClass
DATA_CLASS_WORKSPACE: DataClass
DATA_CLASS_CONFIDENTIAL: DataClass
ENDPOINT_VARIANT_UNSPECIFIED: EndpointVariant
ENDPOINT_VARIANT_PERSISTENT: EndpointVariant
ENDPOINT_VARIANT_VOLATILE: EndpointVariant
ENDPOINT_HOST_VARIANT_UNSPECIFIED: EndpointHostVariant
ENDPOINT_HOST_VARIANT_GRPC: EndpointHostVariant
ENDPOINT_HOST_VARIANT_S3: EndpointHostVariant
PERMISSION_LEVEL_UNSPECIFIED: PermissionLevel
PERMISSION_LEVEL_NONE: PermissionLevel
PERMISSION_LEVEL_READ: PermissionLevel
PERMISSION_LEVEL_APPEND: PermissionLevel
PERMISSION_LEVEL_WRITE: PermissionLevel
PERMISSION_LEVEL_ADMIN: PermissionLevel
KEY_VALUE_VARIANT_UNSPECIFIED: KeyValueVariant
KEY_VALUE_VARIANT_LABEL: KeyValueVariant
KEY_VALUE_VARIANT_STATIC_LABEL: KeyValueVariant
KEY_VALUE_VARIANT_HOOK: KeyValueVariant
KEY_VALUE_VARIANT_HOOK_STATUS: KeyValueVariant
EXTERNAL_RELATION_VARIANT_UNSPECIFIED: ExternalRelationVariant
EXTERNAL_RELATION_VARIANT_URL: ExternalRelationVariant
EXTERNAL_RELATION_VARIANT_IDENTIFIER: ExternalRelationVariant
EXTERNAL_RELATION_VARIANT_CUSTOM: ExternalRelationVariant
INTERNAL_RELATION_VARIANT_UNSPECIFIED: InternalRelationVariant
INTERNAL_RELATION_VARIANT_BELONGS_TO: InternalRelationVariant
INTERNAL_RELATION_VARIANT_ORIGIN: InternalRelationVariant
INTERNAL_RELATION_VARIANT_VERSION: InternalRelationVariant
INTERNAL_RELATION_VARIANT_METADATA: InternalRelationVariant
INTERNAL_RELATION_VARIANT_POLICY: InternalRelationVariant
INTERNAL_RELATION_VARIANT_CUSTOM: InternalRelationVariant
RELATION_DIRECTION_UNSPECIFIED: RelationDirection
RELATION_DIRECTION_INBOUND: RelationDirection
RELATION_DIRECTION_OUTBOUND: RelationDirection
RESOURCE_ACTION_UNSPECIFIED: ResourceAction
RESOURCE_ACTION_CREATE: ResourceAction
RESOURCE_ACTION_APPEND: ResourceAction
RESOURCE_ACTION_UPDATE: ResourceAction
RESOURCE_ACTION_READ: ResourceAction
RESOURCE_ACTION_DELETE: ResourceAction
STATUS_UNSPECIFIED: Status
STATUS_INITIALIZING: Status
STATUS_VALIDATING: Status
STATUS_AVAILABLE: Status
STATUS_UNAVAILABLE: Status
STATUS_ERROR: Status
STATUS_DELETED: Status
COMPONENT_STATUS_UNSPECIFIED: ComponentStatus
COMPONENT_STATUS_INITIALIZING: ComponentStatus
COMPONENT_STATUS_AVAILABLE: ComponentStatus
COMPONENT_STATUS_DEGRADED: ComponentStatus
COMPONENT_STATUS_UNAVAILABLE: ComponentStatus
COMPONENT_STATUS_MAINTENANCE: ComponentStatus
HASHALGORITHM_UNSPECIFIED: Hashalgorithm
HASHALGORITHM_MD5: Hashalgorithm
HASHALGORITHM_SHA256: Hashalgorithm
RESOURCE_VARIANT_UNSPECIFIED: ResourceVariant
RESOURCE_VARIANT_PROJECT: ResourceVariant
RESOURCE_VARIANT_COLLECTION: ResourceVariant
RESOURCE_VARIANT_DATASET: ResourceVariant
RESOURCE_VARIANT_OBJECT: ResourceVariant

class User(_message.Message):
    __slots__ = ["id", "external_id", "display_name", "active", "email", "attributes"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    external_id: str
    display_name: str
    active: bool
    email: str
    attributes: UserAttributes
    def __init__(self, id: _Optional[str] = ..., external_id: _Optional[str] = ..., display_name: _Optional[str] = ..., active: bool = ..., email: _Optional[str] = ..., attributes: _Optional[_Union[UserAttributes, _Mapping]] = ...) -> None: ...

class Permission(_message.Message):
    __slots__ = ["project_id", "collection_id", "dataset_id", "object_id", "permission_level"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    collection_id: str
    dataset_id: str
    object_id: str
    permission_level: PermissionLevel
    def __init__(self, project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., dataset_id: _Optional[str] = ..., object_id: _Optional[str] = ..., permission_level: _Optional[_Union[PermissionLevel, str]] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ["id", "name", "created_at", "expires_at", "permission"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    permission: Permission
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., permission: _Optional[_Union[Permission, _Mapping]] = ...) -> None: ...

class Pubkey(_message.Message):
    __slots__ = ["id", "key", "location"]
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    key: str
    location: str
    def __init__(self, id: _Optional[int] = ..., key: _Optional[str] = ..., location: _Optional[str] = ...) -> None: ...

class CustomAttributes(_message.Message):
    __slots__ = ["attribute_name", "attribute_value"]
    ATTRIBUTE_NAME_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    attribute_name: str
    attribute_value: str
    def __init__(self, attribute_name: _Optional[str] = ..., attribute_value: _Optional[str] = ...) -> None: ...

class UserAttributes(_message.Message):
    __slots__ = ["global_admin", "service_account", "tokens", "trusted_endpoints", "custom_attributes", "personal_permissions"]
    GLOBAL_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    global_admin: bool
    service_account: bool
    tokens: _containers.RepeatedCompositeFieldContainer[Token]
    trusted_endpoints: _containers.RepeatedScalarFieldContainer[str]
    custom_attributes: _containers.RepeatedCompositeFieldContainer[CustomAttributes]
    personal_permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    def __init__(self, global_admin: bool = ..., service_account: bool = ..., tokens: _Optional[_Iterable[_Union[Token, _Mapping]]] = ..., trusted_endpoints: _Optional[_Iterable[str]] = ..., custom_attributes: _Optional[_Iterable[_Union[CustomAttributes, _Mapping]]] = ..., personal_permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ...) -> None: ...

class KeyValue(_message.Message):
    __slots__ = ["key", "value", "variant"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    variant: KeyValueVariant
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., variant: _Optional[_Union[KeyValueVariant, str]] = ...) -> None: ...

class Relation(_message.Message):
    __slots__ = ["external", "internal"]
    EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    external: ExternalRelation
    internal: InternalRelation
    def __init__(self, external: _Optional[_Union[ExternalRelation, _Mapping]] = ..., internal: _Optional[_Union[InternalRelation, _Mapping]] = ...) -> None: ...

class ExternalRelation(_message.Message):
    __slots__ = ["identifier", "defined_variant", "custom_variant"]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DEFINED_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VARIANT_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    defined_variant: ExternalRelationVariant
    custom_variant: str
    def __init__(self, identifier: _Optional[str] = ..., defined_variant: _Optional[_Union[ExternalRelationVariant, str]] = ..., custom_variant: _Optional[str] = ...) -> None: ...

class InternalRelation(_message.Message):
    __slots__ = ["resource_id", "resource_variant", "defined_variant", "custom_variant", "direction"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    DEFINED_VARIANT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VARIANT_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    resource_variant: ResourceVariant
    defined_variant: InternalRelationVariant
    custom_variant: str
    direction: RelationDirection
    def __init__(self, resource_id: _Optional[str] = ..., resource_variant: _Optional[_Union[ResourceVariant, str]] = ..., defined_variant: _Optional[_Union[InternalRelationVariant, str]] = ..., custom_variant: _Optional[str] = ..., direction: _Optional[_Union[RelationDirection, str]] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ["start_after", "page_size"]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    start_after: str
    page_size: int
    def __init__(self, start_after: _Optional[str] = ..., page_size: _Optional[int] = ...) -> None: ...

class Stats(_message.Message):
    __slots__ = ["count", "size", "last_updated"]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    count: int
    size: int
    last_updated: _timestamp_pb2.Timestamp
    def __init__(self, count: _Optional[int] = ..., size: _Optional[int] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Hash(_message.Message):
    __slots__ = ["alg", "hash"]
    ALG_FIELD_NUMBER: _ClassVar[int]
    HASH_FIELD_NUMBER: _ClassVar[int]
    alg: Hashalgorithm
    hash: str
    def __init__(self, alg: _Optional[_Union[Hashalgorithm, str]] = ..., hash: _Optional[str] = ...) -> None: ...

class EndpointHostConfig(_message.Message):
    __slots__ = ["url", "is_primary", "ssl", "public", "host_variant"]
    URL_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SSL_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    HOST_VARIANT_FIELD_NUMBER: _ClassVar[int]
    url: str
    is_primary: bool
    ssl: bool
    public: bool
    host_variant: EndpointHostVariant
    def __init__(self, url: _Optional[str] = ..., is_primary: bool = ..., ssl: bool = ..., public: bool = ..., host_variant: _Optional[_Union[EndpointHostVariant, str]] = ...) -> None: ...

class Endpoint(_message.Message):
    __slots__ = ["id", "ep_variant", "name", "is_public", "status", "host_configs"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EP_VARIANT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HOST_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    ep_variant: EndpointVariant
    name: str
    is_public: bool
    status: ComponentStatus
    host_configs: _containers.RepeatedCompositeFieldContainer[EndpointHostConfig]
    def __init__(self, id: _Optional[str] = ..., ep_variant: _Optional[_Union[EndpointVariant, str]] = ..., name: _Optional[str] = ..., is_public: bool = ..., status: _Optional[_Union[ComponentStatus, str]] = ..., host_configs: _Optional[_Iterable[_Union[EndpointHostConfig, _Mapping]]] = ...) -> None: ...

class DataEndpoint(_message.Message):
    __slots__ = ["id", "full_synced"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FULL_SYNCED_FIELD_NUMBER: _ClassVar[int]
    id: str
    full_synced: bool
    def __init__(self, id: _Optional[str] = ..., full_synced: bool = ...) -> None: ...

class Copy(_message.Message):
    __slots__ = ["resource", "target_endpoint", "push"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PUSH_FIELD_NUMBER: _ClassVar[int]
    resource: str
    target_endpoint: str
    push: bool
    def __init__(self, resource: _Optional[str] = ..., target_endpoint: _Optional[str] = ..., push: bool = ...) -> None: ...

class Context(_message.Message):
    __slots__ = ["s3_credentials", "copy"]
    S3_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    s3_credentials: bool
    copy: Copy
    def __init__(self, s3_credentials: bool = ..., copy: _Optional[_Union[Copy, _Mapping]] = ...) -> None: ...

class License(_message.Message):
    __slots__ = ["tag", "name", "text", "url"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    tag: str
    name: str
    text: str
    url: str
    def __init__(self, tag: _Optional[str] = ..., name: _Optional[str] = ..., text: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class GenericResource(_message.Message):
    __slots__ = ["project", "collection", "dataset", "object"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    project: Project
    collection: Collection
    dataset: Dataset
    object: Object
    def __init__(self, project: _Optional[_Union[Project, _Mapping]] = ..., collection: _Optional[_Union[Collection, _Mapping]] = ..., dataset: _Optional[_Union[Dataset, _Mapping]] = ..., object: _Optional[_Union[Object, _Mapping]] = ...) -> None: ...

class Project(_message.Message):
    __slots__ = ["id", "name", "description", "key_values", "relations", "stats", "data_class", "created_at", "created_by", "status", "dynamic", "endpoints", "metadata_license_tag", "default_data_license_tag"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    stats: Stats
    data_class: DataClass
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    status: Status
    dynamic: bool
    endpoints: _containers.RepeatedCompositeFieldContainer[DataEndpoint]
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ..., data_class: _Optional[_Union[DataClass, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., dynamic: bool = ..., endpoints: _Optional[_Iterable[_Union[DataEndpoint, _Mapping]]] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class Collection(_message.Message):
    __slots__ = ["id", "name", "description", "key_values", "relations", "stats", "data_class", "created_at", "created_by", "status", "dynamic", "endpoints", "metadata_license_tag", "default_data_license_tag"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    stats: Stats
    data_class: DataClass
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    status: Status
    dynamic: bool
    endpoints: _containers.RepeatedCompositeFieldContainer[DataEndpoint]
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ..., data_class: _Optional[_Union[DataClass, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., dynamic: bool = ..., endpoints: _Optional[_Iterable[_Union[DataEndpoint, _Mapping]]] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ["id", "name", "description", "key_values", "relations", "stats", "data_class", "created_at", "created_by", "status", "dynamic", "endpoints", "metadata_license_tag", "default_data_license_tag"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    stats: Stats
    data_class: DataClass
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    status: Status
    dynamic: bool
    endpoints: _containers.RepeatedCompositeFieldContainer[DataEndpoint]
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ..., stats: _Optional[_Union[Stats, _Mapping]] = ..., data_class: _Optional[_Union[DataClass, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., dynamic: bool = ..., endpoints: _Optional[_Iterable[_Union[DataEndpoint, _Mapping]]] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ["id", "name", "description", "key_values", "relations", "content_len", "data_class", "created_at", "created_by", "status", "dynamic", "endpoints", "hashes", "metadata_license_tag", "data_license_tag"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    HASHES_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[Relation]
    content_len: int
    data_class: DataClass
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    status: Status
    dynamic: bool
    endpoints: _containers.RepeatedCompositeFieldContainer[DataEndpoint]
    hashes: _containers.RepeatedCompositeFieldContainer[Hash]
    metadata_license_tag: str
    data_license_tag: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[Relation, _Mapping]]] = ..., content_len: _Optional[int] = ..., data_class: _Optional[_Union[DataClass, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., dynamic: bool = ..., endpoints: _Optional[_Iterable[_Union[DataEndpoint, _Mapping]]] = ..., hashes: _Optional[_Iterable[_Union[Hash, _Mapping]]] = ..., metadata_license_tag: _Optional[str] = ..., data_license_tag: _Optional[str] = ...) -> None: ...
