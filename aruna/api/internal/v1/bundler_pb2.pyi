from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bundle(_message.Message):
    __slots__ = ["bundle_id", "expires_at", "object_refs"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_REFS_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    expires_at: _timestamp_pb2.Timestamp
    object_refs: _containers.RepeatedCompositeFieldContainer[ObjectRef]
    def __init__(self, bundle_id: _Optional[str] = ..., object_refs: _Optional[_Iterable[_Union[ObjectRef, _Mapping]]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EnableBundleRequest(_message.Message):
    __slots__ = ["bundle"]
    BUNDLE_FIELD_NUMBER: _ClassVar[int]
    bundle: Bundle
    def __init__(self, bundle: _Optional[_Union[Bundle, _Mapping]] = ...) -> None: ...

class EnableBundleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBundlesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetBundlesResponse(_message.Message):
    __slots__ = ["bundles"]
    BUNDLES_FIELD_NUMBER: _ClassVar[int]
    bundles: _containers.RepeatedCompositeFieldContainer[Bundle]
    def __init__(self, bundles: _Optional[_Iterable[_Union[Bundle, _Mapping]]] = ...) -> None: ...

class InvalidateBundleRequest(_message.Message):
    __slots__ = ["bundle_id"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class InvalidateBundleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ObjectRef(_message.Message):
    __slots__ = ["encryption_key", "object_location", "object_path"]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    encryption_key: str
    object_location: str
    object_path: str
    def __init__(self, object_location: _Optional[str] = ..., encryption_key: _Optional[str] = ..., object_path: _Optional[str] = ...) -> None: ...

class PrepareBundleRequest(_message.Message):
    __slots__ = ["bundle_id"]
    BUNDLE_ID_FIELD_NUMBER: _ClassVar[int]
    bundle_id: str
    def __init__(self, bundle_id: _Optional[str] = ...) -> None: ...

class PrepareBundleResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
