from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as _dataset_pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as _object_models_pb2
from sciobjsdb.api.storage.services.v1 import dataset_object_service_models_pb2 as _dataset_object_service_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ["annotations", "description", "labels", "metadata_objects", "name", "project_id"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_OBJECTS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata_objects: _containers.RepeatedCompositeFieldContainer[_dataset_object_service_models_pb2.CreateObjectRequest]
    name: str
    project_id: str
    def __init__(self, name: Optional[str] = ..., description: Optional[str] = ..., project_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., metadata_objects: Optional[Iterable[Union[_dataset_object_service_models_pb2.CreateObjectRequest, Mapping]]] = ...) -> None: ...

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
    __slots__ = ["object_group_revisions"]
    OBJECT_GROUP_REVISIONS_FIELD_NUMBER: ClassVar[int]
    object_group_revisions: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroupRevision]
    def __init__(self, object_group_revisions: Optional[Iterable[Union[_object_models_pb2.ObjectGroupRevision, Mapping]]] = ...) -> None: ...

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

class GetObjectGroupRevisionsInDateRangeRequest(_message.Message):
    __slots__ = ["end", "id", "start"]
    END_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    START_FIELD_NUMBER: ClassVar[int]
    end: _timestamp_pb2.Timestamp
    id: str
    start: _timestamp_pb2.Timestamp
    def __init__(self, id: Optional[str] = ..., start: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., end: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class GetObjectGroupRevisionsInDateRangeResponse(_message.Message):
    __slots__ = ["object_group_revisions"]
    OBJECT_GROUP_REVISIONS_FIELD_NUMBER: ClassVar[int]
    object_group_revisions: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroupRevision]
    def __init__(self, object_group_revisions: Optional[Iterable[Union[_object_models_pb2.ObjectGroupRevision, Mapping]]] = ...) -> None: ...

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
    __slots__ = ["annotations", "dataset_id", "description", "labels", "name", "object_group_revision_ids", "version"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_REVISION_IDS_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    dataset_id: str
    description: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    name: str
    object_group_revision_ids: _containers.RepeatedScalarFieldContainer[str]
    version: _common_models_pb2.Version
    def __init__(self, name: Optional[str] = ..., dataset_id: Optional[str] = ..., version: Optional[Union[_common_models_pb2.Version, Mapping]] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., object_group_revision_ids: Optional[Iterable[str]] = ..., description: Optional[str] = ...) -> None: ...

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
