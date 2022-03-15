from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as _dataset_pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as _object_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ["description", "labels", "metadata", "name", "project_id"]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    project_id: str
    def __init__(self, name: Optional[str] = ..., description: Optional[str] = ..., project_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ...) -> None: ...

class CreateDatasetResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteDatasetResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteDatasetVersionRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteDatasetVersionResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDatasetObjectGroupsRequest(_message.Message):
    __slots__ = ["id", "page_request"]
    ID_FIELD_NUMBER: ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: ClassVar[int]
    id: str
    page_request: _common_models_pb2.PageRequest
    def __init__(self, id: Optional[str] = ..., page_request: Optional[Union[_common_models_pb2.PageRequest, Mapping]] = ...) -> None: ...

class GetDatasetObjectGroupsResponse(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: ClassVar[int]
    object_groups: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroup]
    def __init__(self, object_groups: Optional[Iterable[Union[_object_models_pb2.ObjectGroup, Mapping]]] = ...) -> None: ...

class GetDatasetRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetDatasetResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: ClassVar[int]
    dataset: _dataset_pb2.Dataset
    def __init__(self, dataset: Optional[Union[_dataset_pb2.Dataset, Mapping]] = ...) -> None: ...

class GetDatasetVersionObjectGroupsRequest(_message.Message):
    __slots__ = ["id", "page_request"]
    ID_FIELD_NUMBER: ClassVar[int]
    PAGE_REQUEST_FIELD_NUMBER: ClassVar[int]
    id: str
    page_request: _common_models_pb2.PageRequest
    def __init__(self, id: Optional[str] = ..., page_request: Optional[Union[_common_models_pb2.PageRequest, Mapping]] = ...) -> None: ...

class GetDatasetVersionObjectGroupsResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: ClassVar[int]
    object_group: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroup]
    def __init__(self, object_group: Optional[Iterable[Union[_object_models_pb2.ObjectGroup, Mapping]]] = ...) -> None: ...

class GetDatasetVersionRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetDatasetVersionResponse(_message.Message):
    __slots__ = ["dataset_version"]
    DATASET_VERSION_FIELD_NUMBER: ClassVar[int]
    dataset_version: _dataset_pb2.DatasetVersion
    def __init__(self, dataset_version: Optional[Union[_dataset_pb2.DatasetVersion, Mapping]] = ...) -> None: ...

class GetDatasetVersionsRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetDatasetVersionsResponse(_message.Message):
    __slots__ = ["dataset_versions"]
    DATASET_VERSIONS_FIELD_NUMBER: ClassVar[int]
    dataset_versions: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.DatasetVersion]
    def __init__(self, dataset_versions: Optional[Iterable[Union[_dataset_pb2.DatasetVersion, Mapping]]] = ...) -> None: ...

class GetObjectGroupsInDateRangeRequest(_message.Message):
    __slots__ = ["end", "id", "start"]
    END_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    START_FIELD_NUMBER: ClassVar[int]
    end: _timestamp_pb2.Timestamp
    id: str
    start: _timestamp_pb2.Timestamp
    def __init__(self, id: Optional[str] = ..., start: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., end: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class GetObjectGroupsInDateRangeResponse(_message.Message):
    __slots__ = ["object_groups"]
    OBJECT_GROUPS_FIELD_NUMBER: ClassVar[int]
    object_groups: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroup]
    def __init__(self, object_groups: Optional[Iterable[Union[_object_models_pb2.ObjectGroup, Mapping]]] = ...) -> None: ...

class GetObjectGroupsStreamLinkRequest(_message.Message):
    __slots__ = ["dataset", "dataset_version", "date_range", "expiry", "group_ids", "stream_type"]
    class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class DatasetQuery(_message.Message):
        __slots__ = ["dataset_id"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        def __init__(self, dataset_id: Optional[str] = ...) -> None: ...
    class DatasetVersionQuery(_message.Message):
        __slots__ = ["dataset_id", "dataset_version_id"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        DATASET_VERSION_ID_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        dataset_version_id: str
        def __init__(self, dataset_id: Optional[str] = ..., dataset_version_id: Optional[str] = ...) -> None: ...
    class DateRangeQuery(_message.Message):
        __slots__ = ["dataset_id", "end", "start"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        END_FIELD_NUMBER: ClassVar[int]
        START_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        end: _timestamp_pb2.Timestamp
        start: _timestamp_pb2.Timestamp
        def __init__(self, dataset_id: Optional[str] = ..., start: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., end: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...
    class GroupIDsQuery(_message.Message):
        __slots__ = ["dataset_id", "object_groups"]
        DATASET_ID_FIELD_NUMBER: ClassVar[int]
        OBJECT_GROUPS_FIELD_NUMBER: ClassVar[int]
        dataset_id: str
        object_groups: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, dataset_id: Optional[str] = ..., object_groups: Optional[Iterable[str]] = ...) -> None: ...
    DATASET_FIELD_NUMBER: ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: ClassVar[int]
    DATE_RANGE_FIELD_NUMBER: ClassVar[int]
    EXPIRY_FIELD_NUMBER: ClassVar[int]
    GROUP_IDS_FIELD_NUMBER: ClassVar[int]
    STREAM_TYPE_BASE64NEWLINE: GetObjectGroupsStreamLinkRequest.StreamType
    STREAM_TYPE_FIELD_NUMBER: ClassVar[int]
    STREAM_TYPE_TARGZ: GetObjectGroupsStreamLinkRequest.StreamType
    STREAM_TYPE_UNSPECIFIED: GetObjectGroupsStreamLinkRequest.StreamType
    STREAM_TYPE_ZIP: GetObjectGroupsStreamLinkRequest.StreamType
    dataset: GetObjectGroupsStreamLinkRequest.DatasetQuery
    dataset_version: GetObjectGroupsStreamLinkRequest.DatasetVersionQuery
    date_range: GetObjectGroupsStreamLinkRequest.DateRangeQuery
    expiry: _timestamp_pb2.Timestamp
    group_ids: GetObjectGroupsStreamLinkRequest.GroupIDsQuery
    stream_type: GetObjectGroupsStreamLinkRequest.StreamType
    def __init__(self, stream_type: Optional[Union[GetObjectGroupsStreamLinkRequest.StreamType, str]] = ..., group_ids: Optional[Union[GetObjectGroupsStreamLinkRequest.GroupIDsQuery, Mapping]] = ..., date_range: Optional[Union[GetObjectGroupsStreamLinkRequest.DateRangeQuery, Mapping]] = ..., dataset: Optional[Union[GetObjectGroupsStreamLinkRequest.DatasetQuery, Mapping]] = ..., dataset_version: Optional[Union[GetObjectGroupsStreamLinkRequest.DatasetVersionQuery, Mapping]] = ..., expiry: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class GetObjectGroupsStreamLinkResponse(_message.Message):
    __slots__ = ["url"]
    URL_FIELD_NUMBER: ClassVar[int]
    url: str
    def __init__(self, url: Optional[str] = ...) -> None: ...

class ReleaseDatasetVersionRequest(_message.Message):
    __slots__ = ["dataset_id", "description", "labels", "metadata", "name", "object_group_ids", "version"]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_IDS_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    dataset_id: str
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    object_group_ids: _containers.RepeatedScalarFieldContainer[str]
    version: _common_models_pb2.Version
    def __init__(self, name: Optional[str] = ..., dataset_id: Optional[str] = ..., version: Optional[Union[_common_models_pb2.Version, Mapping]] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., object_group_ids: Optional[Iterable[str]] = ..., description: Optional[str] = ...) -> None: ...

class ReleaseDatasetVersionResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class UpdateDatasetFieldRequest(_message.Message):
    __slots__ = ["update_request"]
    UPDATE_REQUEST_FIELD_NUMBER: ClassVar[int]
    update_request: _common_models_pb2.UpdateFieldsRequest
    def __init__(self, update_request: Optional[Union[_common_models_pb2.UpdateFieldsRequest, Mapping]] = ...) -> None: ...

class UpdateDatasetFieldResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
