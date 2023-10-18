from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchResourcesRequest(_message.Message):
    __slots__ = ["query", "filter", "limit", "offset"]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    query: str
    filter: str
    limit: int
    offset: int
    def __init__(self, query: _Optional[str] = ..., filter: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class SearchResourcesResponse(_message.Message):
    __slots__ = ["resources", "estimated_total", "last_index"]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOTAL_FIELD_NUMBER: _ClassVar[int]
    LAST_INDEX_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[_models_pb2.GenericResource]
    estimated_total: int
    last_index: int
    def __init__(self, resources: _Optional[_Iterable[_Union[_models_pb2.GenericResource, _Mapping]]] = ..., estimated_total: _Optional[int] = ..., last_index: _Optional[int] = ...) -> None: ...

class GetResourceRequest(_message.Message):
    __slots__ = ["resource_id"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    def __init__(self, resource_id: _Optional[str] = ...) -> None: ...

class ResourceWithPermission(_message.Message):
    __slots__ = ["resource", "permission"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    resource: _models_pb2.GenericResource
    permission: _models_pb2.PermissionLevel
    def __init__(self, resource: _Optional[_Union[_models_pb2.GenericResource, _Mapping]] = ..., permission: _Optional[_Union[_models_pb2.PermissionLevel, str]] = ...) -> None: ...

class GetResourceResponse(_message.Message):
    __slots__ = ["resource"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: ResourceWithPermission
    def __init__(self, resource: _Optional[_Union[ResourceWithPermission, _Mapping]] = ...) -> None: ...

class GetResourcesRequest(_message.Message):
    __slots__ = ["resource_ids"]
    RESOURCE_IDS_FIELD_NUMBER: _ClassVar[int]
    resource_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, resource_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetResourcesResponse(_message.Message):
    __slots__ = ["resources"]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    resources: _containers.RepeatedCompositeFieldContainer[ResourceWithPermission]
    def __init__(self, resources: _Optional[_Iterable[_Union[ResourceWithPermission, _Mapping]]] = ...) -> None: ...

class RequestResourceAccessRequest(_message.Message):
    __slots__ = ["resource_id", "message"]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    resource_id: str
    message: str
    def __init__(self, resource_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class RequestResourceAccessResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
