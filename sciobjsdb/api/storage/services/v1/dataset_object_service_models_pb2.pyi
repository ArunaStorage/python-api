from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as _common_models_pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as _object_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddObjectRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class CreateObjectFromUpdate(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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
    __slots__ = ["create_revision_request", "dataset_id"]
    CREATE_REVISION_REQUEST_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    create_revision_request: CreateObjectGroupRevisionRequest
    dataset_id: str
    def __init__(self, create_revision_request: Optional[Union[CreateObjectGroupRevisionRequest, Mapping]] = ..., dataset_id: Optional[str] = ...) -> None: ...

class CreateObjectGroupResponse(_message.Message):
    __slots__ = ["create_revision_response", "object_group_id", "object_group_name"]
    CREATE_REVISION_RESPONSE_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_NAME_FIELD_NUMBER: ClassVar[int]
    create_revision_response: CreateObjectGroupRevisionResponse
    object_group_id: str
    object_group_name: str
    def __init__(self, object_group_id: Optional[str] = ..., object_group_name: Optional[str] = ..., create_revision_response: Optional[Union[CreateObjectGroupRevisionResponse, Mapping]] = ...) -> None: ...

class CreateObjectGroupRevisionRequest(_message.Message):
    __slots__ = ["annotations", "description", "generated", "include_object_link", "labels", "name", "object_group_id", "update_meta_objects", "update_objects"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    INCLUDE_OBJECT_LINK_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    UPDATE_META_OBJECTS_FIELD_NUMBER: ClassVar[int]
    UPDATE_OBJECTS_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    description: str
    generated: _timestamp_pb2.Timestamp
    include_object_link: bool
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    name: str
    object_group_id: str
    update_meta_objects: UpdateObjectsRequests
    update_objects: UpdateObjectsRequests
    def __init__(self, update_objects: Optional[Union[UpdateObjectsRequests, Mapping]] = ..., update_meta_objects: Optional[Union[UpdateObjectsRequests, Mapping]] = ..., object_group_id: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., include_object_link: bool = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class CreateObjectGroupRevisionResponse(_message.Message):
    __slots__ = ["data_objects", "id", "meta_objects", "metadata_object_links", "object_links"]
    class ObjectLinks(_message.Message):
        __slots__ = ["link", "object_id"]
        LINK_FIELD_NUMBER: ClassVar[int]
        OBJECT_ID_FIELD_NUMBER: ClassVar[int]
        link: str
        object_id: str
        def __init__(self, link: Optional[str] = ..., object_id: Optional[str] = ...) -> None: ...
    DATA_OBJECTS_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    METADATA_OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    META_OBJECTS_FIELD_NUMBER: ClassVar[int]
    OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    data_objects: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.Object]
    id: str
    meta_objects: _containers.RepeatedCompositeFieldContainer[_object_models_pb2.Object]
    metadata_object_links: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupRevisionResponse.ObjectLinks]
    object_links: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupRevisionResponse.ObjectLinks]
    def __init__(self, id: Optional[str] = ..., data_objects: Optional[Iterable[Union[_object_models_pb2.Object, Mapping]]] = ..., meta_objects: Optional[Iterable[Union[_object_models_pb2.Object, Mapping]]] = ..., object_links: Optional[Iterable[Union[CreateObjectGroupRevisionResponse.ObjectLinks, Mapping]]] = ..., metadata_object_links: Optional[Iterable[Union[CreateObjectGroupRevisionResponse.ObjectLinks, Mapping]]] = ...) -> None: ...

class CreateObjectRequest(_message.Message):
    __slots__ = ["annotations", "content_len", "dataset_id", "filename", "filetype", "labels", "origin", "subpath"]
    ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    CONTENT_LEN_FIELD_NUMBER: ClassVar[int]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    FILENAME_FIELD_NUMBER: ClassVar[int]
    FILETYPE_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    SUBPATH_FIELD_NUMBER: ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Annotation]
    content_len: int
    dataset_id: str
    filename: str
    filetype: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    origin: _common_models_pb2.Origin
    subpath: _object_models_pb2.Subpath
    def __init__(self, filename: Optional[str] = ..., filetype: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., annotations: Optional[Iterable[Union[_common_models_pb2.Annotation, Mapping]]] = ..., content_len: Optional[int] = ..., origin: Optional[Union[_common_models_pb2.Origin, Mapping]] = ..., subpath: Optional[Union[_object_models_pb2.Subpath, Mapping]] = ..., dataset_id: Optional[str] = ...) -> None: ...

class CreateObjectResponse(_message.Message):
    __slots__ = ["id", "upload_link"]
    ID_FIELD_NUMBER: ClassVar[int]
    UPLOAD_LINK_FIELD_NUMBER: ClassVar[int]
    id: str
    upload_link: str
    def __init__(self, id: Optional[str] = ..., upload_link: Optional[str] = ...) -> None: ...

class DeleteObject(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteObjectGroupRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteObjectRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

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

class GetObjectRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class UpdateObjectGroupRequest(_message.Message):
    __slots__ = ["create_revision_request", "id"]
    CREATE_REVISION_REQUEST_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    create_revision_request: CreateObjectGroupRevisionRequest
    id: str
    def __init__(self, id: Optional[str] = ..., create_revision_request: Optional[Union[CreateObjectGroupRevisionRequest, Mapping]] = ...) -> None: ...

class UpdateObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateObjectRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateObjectsRequests(_message.Message):
    __slots__ = ["add_objects", "delete_objects", "update_objects"]
    ADD_OBJECTS_FIELD_NUMBER: ClassVar[int]
    DELETE_OBJECTS_FIELD_NUMBER: ClassVar[int]
    UPDATE_OBJECTS_FIELD_NUMBER: ClassVar[int]
    add_objects: _containers.RepeatedCompositeFieldContainer[AddObjectRequest]
    delete_objects: _containers.RepeatedCompositeFieldContainer[DeleteObjectRequest]
    update_objects: _containers.RepeatedCompositeFieldContainer[UpdateObjectRequest]
    def __init__(self, add_objects: Optional[Iterable[Union[AddObjectRequest, Mapping]]] = ..., update_objects: Optional[Iterable[Union[UpdateObjectRequest, Mapping]]] = ..., delete_objects: Optional[Iterable[Union[DeleteObjectRequest, Mapping]]] = ...) -> None: ...
