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
    __slots__ = ["dataset_id", "description", "generated", "include_object_link", "labels", "metadata", "name", "objects", "uuid"]
    DATASET_ID_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    GENERATED_FIELD_NUMBER: ClassVar[int]
    INCLUDE_OBJECT_LINK_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    dataset_id: str
    description: str
    generated: _timestamp_pb2.Timestamp
    include_object_link: bool
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    name: str
    objects: _containers.RepeatedCompositeFieldContainer[CreateObjectRequest]
    uuid: str
    def __init__(self, name: Optional[str] = ..., description: Optional[str] = ..., dataset_id: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., objects: Optional[Iterable[Union[CreateObjectRequest, Mapping]]] = ..., include_object_link: bool = ..., generated: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., uuid: Optional[str] = ...) -> None: ...

class CreateObjectGroupResponse(_message.Message):
    __slots__ = ["object_group_id", "object_group_name", "object_links", "uuid"]
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
    OBJECT_GROUP_ID_FIELD_NUMBER: ClassVar[int]
    OBJECT_GROUP_NAME_FIELD_NUMBER: ClassVar[int]
    OBJECT_LINKS_FIELD_NUMBER: ClassVar[int]
    UUID_FIELD_NUMBER: ClassVar[int]
    object_group_id: str
    object_group_name: str
    object_links: _containers.RepeatedCompositeFieldContainer[CreateObjectGroupResponse.ObjectLinks]
    uuid: str
    def __init__(self, object_group_id: Optional[str] = ..., object_links: Optional[Iterable[Union[CreateObjectGroupResponse.ObjectLinks, Mapping]]] = ..., object_group_name: Optional[str] = ..., uuid: Optional[str] = ...) -> None: ...

class CreateObjectRequest(_message.Message):
    __slots__ = ["content_len", "filename", "filetype", "labels", "metadata", "origin"]
    CONTENT_LEN_FIELD_NUMBER: ClassVar[int]
    FILENAME_FIELD_NUMBER: ClassVar[int]
    FILETYPE_FIELD_NUMBER: ClassVar[int]
    LABELS_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    content_len: int
    filename: str
    filetype: str
    labels: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Label]
    metadata: _containers.RepeatedCompositeFieldContainer[_common_models_pb2.Metadata]
    origin: _common_models_pb2.Origin
    def __init__(self, filename: Optional[str] = ..., filetype: Optional[str] = ..., labels: Optional[Iterable[Union[_common_models_pb2.Label, Mapping]]] = ..., metadata: Optional[Iterable[Union[_common_models_pb2.Metadata, Mapping]]] = ..., content_len: Optional[int] = ..., origin: Optional[Union[_common_models_pb2.Origin, Mapping]] = ...) -> None: ...

class DeleteObjectGroupRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class DeleteObjectGroupResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FinishObjectGroupUploadRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class FinishObjectGroupUploadResponse(_message.Message):
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
    __slots__ = ["id"]
    ID_FIELD_NUMBER: ClassVar[int]
    id: str
    def __init__(self, id: Optional[str] = ...) -> None: ...

class GetObjectGroupResponse(_message.Message):
    __slots__ = ["object_group"]
    OBJECT_GROUP_FIELD_NUMBER: ClassVar[int]
    object_group: _object_models_pb2.ObjectGroup
    def __init__(self, object_group: Optional[Union[_object_models_pb2.ObjectGroup, Mapping]] = ...) -> None: ...
