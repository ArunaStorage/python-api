from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddEndpointRequest(_message.Message):
    __slots__ = ["documentation_path", "ep_type", "internal_hostname", "is_public", "name", "proxy_hostname"]
    DOCUMENTATION_PATH_FIELD_NUMBER: _ClassVar[int]
    EP_TYPE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROXY_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    documentation_path: str
    ep_type: _models_pb2.EndpointType
    internal_hostname: str
    is_public: bool
    name: str
    proxy_hostname: str
    def __init__(self, name: _Optional[str] = ..., ep_type: _Optional[_Union[_models_pb2.EndpointType, str]] = ..., proxy_hostname: _Optional[str] = ..., internal_hostname: _Optional[str] = ..., documentation_path: _Optional[str] = ..., is_public: bool = ...) -> None: ...

class AddEndpointResponse(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: _models_pb2.Endpoint
    def __init__(self, endpoint: _Optional[_Union[_models_pb2.Endpoint, _Mapping]] = ...) -> None: ...

class DeleteEndpointRequest(_message.Message):
    __slots__ = ["endpoint_id"]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    def __init__(self, endpoint_id: _Optional[str] = ...) -> None: ...

class DeleteEndpointResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDefaultEndpointRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetDefaultEndpointResponse(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: _models_pb2.Endpoint
    def __init__(self, endpoint: _Optional[_Union[_models_pb2.Endpoint, _Mapping]] = ...) -> None: ...

class GetEndpointRequest(_message.Message):
    __slots__ = ["endpoint_id", "endpoint_name"]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    endpoint_id: str
    endpoint_name: str
    def __init__(self, endpoint_name: _Optional[str] = ..., endpoint_id: _Optional[str] = ...) -> None: ...

class GetEndpointResponse(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: _models_pb2.Endpoint
    def __init__(self, endpoint: _Optional[_Union[_models_pb2.Endpoint, _Mapping]] = ...) -> None: ...

class GetEndpointsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetEndpointsResponse(_message.Message):
    __slots__ = ["endpoints"]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    endpoints: _containers.RepeatedCompositeFieldContainer[_models_pb2.Endpoint]
    def __init__(self, endpoints: _Optional[_Iterable[_Union[_models_pb2.Endpoint, _Mapping]]] = ...) -> None: ...
