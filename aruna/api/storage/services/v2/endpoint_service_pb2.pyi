from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEndpointRequest(_message.Message):
    __slots__ = ["name", "ep_variant", "is_public", "pubkey", "host_configs"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EP_VARIANT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    HOST_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ep_variant: _models_pb2.EndpointVariant
    is_public: bool
    pubkey: str
    host_configs: _containers.RepeatedCompositeFieldContainer[_models_pb2.EndpointHostConfig]
    def __init__(self, name: _Optional[str] = ..., ep_variant: _Optional[_Union[_models_pb2.EndpointVariant, str]] = ..., is_public: bool = ..., pubkey: _Optional[str] = ..., host_configs: _Optional[_Iterable[_Union[_models_pb2.EndpointHostConfig, _Mapping]]] = ...) -> None: ...

class CreateEndpointResponse(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: _models_pb2.Endpoint
    def __init__(self, endpoint: _Optional[_Union[_models_pb2.Endpoint, _Mapping]] = ...) -> None: ...

class FullSyncEndpointRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FullSyncEndpointResponse(_message.Message):
    __slots__ = ["generic_resource", "user", "pubkey"]
    GENERIC_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    generic_resource: _models_pb2.GenericResource
    user: _models_pb2.User
    pubkey: _models_pb2.Pubkey
    def __init__(self, generic_resource: _Optional[_Union[_models_pb2.GenericResource, _Mapping]] = ..., user: _Optional[_Union[_models_pb2.User, _Mapping]] = ..., pubkey: _Optional[_Union[_models_pb2.Pubkey, _Mapping]] = ...) -> None: ...

class GetEndpointRequest(_message.Message):
    __slots__ = ["endpoint_name", "endpoint_id"]
    ENDPOINT_NAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint_name: str
    endpoint_id: str
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
