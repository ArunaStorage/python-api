from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as _object_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateObjectGroupBatchRequest(_message.Message):
    __slots__ = ["include_object_link", "requests"]
    INCLUDE_OBJECT_LINK_FIELD_NUMBER: ClassVar[int]
    REQUESTS_FIELD_NUMBER: ClassVar[int]
    include_object_link: bool
    requests: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupRequest]
    def __init__(self, requests: Optional[Iterable[Union[CreateObjectGroupRequest, Mapping]]] = ..., include_object_link: bool = ...) -> None: ...

class CreateObjectGroupBatchResponse(_message.Message):
    __slots__ = ["responses"]
    RESPONSES_FIELD_NUMBER: ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupResponse]
    def __init__(self, responses: Optional[Iterable[Union[CreateObjectGroupResponse, Mapping]]] = ...) -> None: ...

class CreateObjectGroupRequest(_message.Message):
    __slots__ = ["annotations", "dataset_id", "description", "generated", "include_object_link", "labels", "metadata_objects", "name", "objects", "subpath", "uuid"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    INCLUDE_OBJECT_LINK_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_OBJECTS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    SUBPATH_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    dataset_id: str
    description: str
    generated: _timestamp_pb2.Timestamp
    include_object_link: bool
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata_objects: _containers.RepeatedCompositeFieldContainer[CreateObjectRequest]
    name: str
    objects: _containers.RepeatedCompositeFieldContainer[CreateObjectRequest]
    subpath: _object_models_pb2.Subpath
    uuid: str
    def __init__(self, name: Optional[str] = ..., description: Optional[str] = ..., dataset_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., objects: Optional[Iterable[Union[CreateObjectRequest, Mapping]]] = ..., metadata_objects: Optional[Iterable[Union[CreateObjectRequest, Mapping]]] = ..., include_object_link: bool = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., uuid: Optional[str] = ..., subpath: Optional[Union[_object_models_pb2.Subpath, Mapping]] = ...) -> None: ...

class CreateObjectGroupResponse(_message.Message):
    __slots__ = ["metadata_object_links", "object_group_id", "object_group_name", "object_group_revision_id", "object_links", "uuid"]
    class ObjectLinks(_message.Message):
        __slots__ = ["filename", "index", "link", "object_id"]
        FILENAME_FIELD_NUMBER: ClassVar[int]
        INDEX_FIELD_NUMBER: ClassVar[int]
        LINK_FIELD_NUMBER: ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: ClassVar[int]
        filename: str
        index: int
        link: str
        object_id: str
        def __init__(self, filename: Optional[str] = ..., link: Optional[str] = ..., object_id: Optional[str] = ..., index: Optional[int] = ...) -> None: ...
    METADATA_OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_REVISION_ID_FIELD_NUMBER: ClassVar[int]
    OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    metadata_object_links: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupResponse.ObjectLinks]
    object_group_id: str
    object_group_name: str
    object_group_revision_id: str
    object_links: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupResponse.ObjectLinks]
    uuid: str
    def __init__(self, object_group_id: Optional[str] = ..., object_links: Optional[Iterable[Union[CreateObjectGroupResponse.ObjectLinks, Mapping]]] = ..., metadata_object_links: Optional[Iterable[Union[CreateObjectGroupResponse.ObjectLinks, Mapping]]] = ..., object_group_name: Optional[str] = ..., uuid: Optional[str] = ..., object_group_revision_id: Optional[str] = ...) -> None: ...

class CreateObjectRequest(_message.Message):
    __slots__ = ["annotations", "content_len", "filename", "filetype", "labels", "origin", "subpath"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: ClassVar[int]
    FILENAME_FIELD_NUMBER: ClassVar[int]
    FILETYPE_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    SUBPATH_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    content_len: int
    filename: str
    filetype: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    origin: _common_models_pb2.Origin
    subpath: _object_models_pb2.Subpath
    def __init__(self, filename: Optional[str] = ..., filetype: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., content_len: Optional[int] = ..., origin: Optional[Union[_common_models_pb2.Origin, Mapping]] = ..., subpath: Optional[Union[_object_models_pb2.Subpath, Mapping]] = ...) -> None: ...

class DeleteObjectGroupRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishObjectGroupRevisionUploadRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class FinishObjectGroupRevisionUploadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishObjectUploadRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class FinishObjectUploadResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetObjectGroupRequest(_message.Message):
    __slots__ = ["id", "pagination"]
    class ObjectGroupRevisionPagination(_message.Message):
        __slots__ = ["last_revision_number", "start_revision_number"]
        LAST_REVISION_NUMBER_FIELD_NUMBER: ClassVar[int]
        START_REVISION_NUMBER_FIELD_NUMBER: ClassVar[int]
        last_revision_number: int
        start_revision_number: int
        def __init__(self, start_revision_number: Optional[int] = ..., last_revision_number: Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: ClassVar[int]
    PAGINATION_FIELD_NUMBER: ClassVar[int]
    id: str
    pagination: GetObjectGroupRequest.ObjectGroupRevisionPagination
    def __init__(self, id: Optional[str] = ..., pagination: Optional[Union[GetObjectGroupRequest.ObjectGroupRevisionPagination, Mapping]] = ...) -> None: ...

class GetObjectGroupResponse(_message.Message):
    __slots__ = ["object_group", "object_group_revisions"]
    OBJECT_GROUP_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_REVISIONS_FIELD_NUMBER: ClassVar[int]
    object_group: _object_models_pb2.ObjectGroup
    object_group_revisions: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.ObjectGroupRevision]
    def __init__(self, object_group: Optional[Union[_object_models_pb2.ObjectGroup, Mapping]] = ..., object_group_revisions: Optional[Iterable[Union[_object_models_pb2.ObjectGroupRevision, Mapping]]] = ...) -> None: ...

class GetObjectGroupRevisionRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetObjectGroupRevisionResponse(_message.Message):
    __slots__ = ["object_group_revision"]
    OBJECT_GROUP_REVISION_FIELD_NUMBER: ClassVar[int]
    object_group_revision: _object_models_pb2.ObjectGroupRevision
    def __init__(self, object_group_revision: Optional[Union[_object_models_pb2.ObjectGroupRevision, Mapping]] = ...) -> None: ...

class UpdateObjectGroupRequest(_message.Message):
    __slots__ = ["id", "parent_revision_id", "update_meta_objects", "update_objects"]
    ID_FIELD_NUMBER: ClassVar[int]
    PARENT_REVISION_ID_FIELD_NUMBER: ClassVar[int]
    UPDATE_META_OBJECTS_FIELD_NUMBER: ClassVar[int]
    UPDATE_OBJECTS_FIELD_NUMBER: ClassVar[int]
    id: str
    parent_revision_id: str
    update_meta_objects: UpdateObjectsRequests
    update_objects: UpdateObjectsRequests
    def __init__(self, id: Optional[str] = ..., parent_revision_id: Optional[str] = ..., update_objects: Optional[Union[UpdateObjectsRequests, Mapping]] = ..., update_meta_objects: Optional[Union[UpdateObjectsRequests, Mapping]] = ...) -> None: ...

class UpdateObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateObjectRequest(_message.Message):
    __slots__ = ["id", "updated_object"]
    ID_FIELD_NUMBER: ClassVar[int]
    UPDATED_OBJECT_FIELD_NUMBER: ClassVar[int]
    id: str
    updated_object: CreateObjectRequest
    def __init__(self, id: Optional[str] = ..., updated_object: Optional[Union[CreateObjectRequest, Mapping]] = ...) -> None: ...

class UpdateObjectsRequests(_message.Message):
    __slots__ = ["add_objects", "delete_objects", "update_object"]
    ADD_OBJECTS_FIELD_NUMBER: ClassVar[int]
    DELETE_OBJECTS_FIELD_NUMBER: ClassVar[int]
    UPDATE_OBJECT_FIELD_NUMBER: ClassVar[int]
    add_objects: _containers.RepeatedCompositeFieldContainer[CreateObjectRequest]
    delete_objects: _containers.RepeatedScalarFieldContainer[str]
    update_object: _containers.RepeatedCompositeFieldContainer[UpdateObjectRequest]
    def __init__(self, add_objects: Optional[Iterable[Union[CreateObjectRequest, Mapping]]] = ..., update_object: Optional[Iterable[Union[UpdateObjectRequest, Mapping]]] = ..., delete_objects: Optional[Iterable[str]] = ...) -> None: ...
