from aruna.api.storage.models.v1 import models_pb2 as _models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
INTERNAL_ACTION_ADD_HOOK: InternalAction
INTERNAL_ACTION_ADD_LABEL: InternalAction
INTERNAL_ACTION_CREATE_READ_REFERENCE: InternalAction
INTERNAL_ACTION_CREATE_WRITE_REFERENCE: InternalAction
INTERNAL_ACTION_UNSPECIFIED: InternalAction
TRIGGER_TYPE_HOOK_ADDED: TriggerType
TRIGGER_TYPE_UNSPECIFIED: TriggerType

class CreateHookRequest(_message.Message):
    __slots__ = ["hook", "project_id", "timeout", "trigger"]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    hook: Hook
    project_id: str
    timeout: int
    trigger: Trigger
    def __init__(self, trigger: _Optional[_Union[Trigger, _Mapping]] = ..., hook: _Optional[_Union[Hook, _Mapping]] = ..., timeout: _Optional[int] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreateHookResponse(_message.Message):
    __slots__ = ["hook_id"]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    def __init__(self, hook_id: _Optional[str] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class DeleteHookRequest(_message.Message):
    __slots__ = ["hook_id"]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    def __init__(self, hook_id: _Optional[str] = ...) -> None: ...

class DeleteHookResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExternalHook(_message.Message):
    __slots__ = ["credentials", "json_template", "url"]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    JSON_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    credentials: Credentials
    json_template: str
    url: str
    def __init__(self, url: _Optional[str] = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ..., json_template: _Optional[str] = ...) -> None: ...

class Hook(_message.Message):
    __slots__ = ["external_hook", "internal_hook"]
    EXTERNAL_HOOK_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_HOOK_FIELD_NUMBER: _ClassVar[int]
    external_hook: ExternalHook
    internal_hook: InternalHook
    def __init__(self, external_hook: _Optional[_Union[ExternalHook, _Mapping]] = ..., internal_hook: _Optional[_Union[InternalHook, _Mapping]] = ...) -> None: ...

class HookCallbackRequest(_message.Message):
    __slots__ = ["hooks", "labels", "success"]
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    hooks: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    labels: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    success: bool
    def __init__(self, success: bool = ..., labels: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., hooks: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class HookCallbackResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HookInfo(_message.Message):
    __slots__ = ["hook", "hook_id", "timeout", "trigger"]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    hook: Hook
    hook_id: str
    timeout: int
    trigger: Trigger
    def __init__(self, hook_id: _Optional[str] = ..., hook: _Optional[_Union[Hook, _Mapping]] = ..., trigger: _Optional[_Union[Trigger, _Mapping]] = ..., timeout: _Optional[int] = ...) -> None: ...

class InternalHook(_message.Message):
    __slots__ = ["internal_action", "target_id", "value"]
    INTERNAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    internal_action: InternalAction
    target_id: str
    value: str
    def __init__(self, internal_action: _Optional[_Union[InternalAction, str]] = ..., target_id: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ListHooksRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListHooksResponse(_message.Message):
    __slots__ = ["infos"]
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[HookInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[HookInfo, _Mapping]]] = ...) -> None: ...

class Trigger(_message.Message):
    __slots__ = ["key", "trigger_type", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    trigger_type: TriggerType
    value: str
    def __init__(self, trigger_type: _Optional[_Union[TriggerType, str]] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class InternalAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
