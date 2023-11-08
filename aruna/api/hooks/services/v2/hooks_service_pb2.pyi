from google.api import annotations_pb2 as _annotations_pb2
from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TriggerType]
    TRIGGER_TYPE_HOOK_ADDED: _ClassVar[TriggerType]
    TRIGGER_TYPE_RESOURCE_CREATED: _ClassVar[TriggerType]
    TRIGGER_TYPE_LABEL_ADDED: _ClassVar[TriggerType]
    TRIGGER_TYPE_STATIC_LABEL_ADDED: _ClassVar[TriggerType]
    TRIGGER_TYPE_HOOK_STATUS_CHANGED: _ClassVar[TriggerType]
    TRIGGER_TYPE_OBJECT_FINISHED: _ClassVar[TriggerType]

class Method(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    METHOD_UNSPECIFIED: _ClassVar[Method]
    METHOD_PUT: _ClassVar[Method]
    METHOD_POST: _ClassVar[Method]
TRIGGER_TYPE_UNSPECIFIED: TriggerType
TRIGGER_TYPE_HOOK_ADDED: TriggerType
TRIGGER_TYPE_RESOURCE_CREATED: TriggerType
TRIGGER_TYPE_LABEL_ADDED: TriggerType
TRIGGER_TYPE_STATIC_LABEL_ADDED: TriggerType
TRIGGER_TYPE_HOOK_STATUS_CHANGED: TriggerType
TRIGGER_TYPE_OBJECT_FINISHED: TriggerType
METHOD_UNSPECIFIED: Method
METHOD_PUT: Method
METHOD_POST: Method

class Trigger(_message.Message):
    __slots__ = ("trigger_type", "filters")
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    trigger_type: TriggerType
    filters: _containers.RepeatedCompositeFieldContainer[Filter]
    def __init__(self, trigger_type: _Optional[_Union[TriggerType, str]] = ..., filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ...) -> None: ...

class ExternalHook(_message.Message):
    __slots__ = ("url", "credentials", "custom_template", "method")
    URL_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    url: str
    credentials: Credentials
    custom_template: str
    method: Method
    def __init__(self, url: _Optional[str] = ..., credentials: _Optional[_Union[Credentials, _Mapping]] = ..., custom_template: _Optional[str] = ..., method: _Optional[_Union[Method, str]] = ...) -> None: ...

class AddLabel(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class AddHook(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class InternalHook(_message.Message):
    __slots__ = ("add_label", "add_hook", "add_relation")
    ADD_LABEL_FIELD_NUMBER: _ClassVar[int]
    ADD_HOOK_FIELD_NUMBER: _ClassVar[int]
    ADD_RELATION_FIELD_NUMBER: _ClassVar[int]
    add_label: AddLabel
    add_hook: AddHook
    add_relation: _models_pb2.Relation
    def __init__(self, add_label: _Optional[_Union[AddLabel, _Mapping]] = ..., add_hook: _Optional[_Union[AddHook, _Mapping]] = ..., add_relation: _Optional[_Union[_models_pb2.Relation, _Mapping]] = ...) -> None: ...

class Hook(_message.Message):
    __slots__ = ("external_hook", "internal_hook")
    EXTERNAL_HOOK_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_HOOK_FIELD_NUMBER: _ClassVar[int]
    external_hook: ExternalHook
    internal_hook: InternalHook
    def __init__(self, external_hook: _Optional[_Union[ExternalHook, _Mapping]] = ..., internal_hook: _Optional[_Union[InternalHook, _Mapping]] = ...) -> None: ...

class Credentials(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("name", "key_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    key_value: _models_pb2.KeyValue
    def __init__(self, name: _Optional[str] = ..., key_value: _Optional[_Union[_models_pb2.KeyValue, _Mapping]] = ...) -> None: ...

class CreateHookRequest(_message.Message):
    __slots__ = ("name", "trigger", "hook", "timeout", "project_ids", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    trigger: Trigger
    hook: Hook
    timeout: int
    project_ids: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, name: _Optional[str] = ..., trigger: _Optional[_Union[Trigger, _Mapping]] = ..., hook: _Optional[_Union[Hook, _Mapping]] = ..., timeout: _Optional[int] = ..., project_ids: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

class CreateHookResponse(_message.Message):
    __slots__ = ("hook_id",)
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    def __init__(self, hook_id: _Optional[str] = ...) -> None: ...

class DeleteHookRequest(_message.Message):
    __slots__ = ("hook_id",)
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    def __init__(self, hook_id: _Optional[str] = ...) -> None: ...

class DeleteHookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HookCallbackRequest(_message.Message):
    __slots__ = ("finished", "error", "secret", "hook_id", "object_id", "pubkey_serial")
    FINISHED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PUBKEY_SERIAL_FIELD_NUMBER: _ClassVar[int]
    finished: Finished
    error: Error
    secret: str
    hook_id: str
    object_id: str
    pubkey_serial: int
    def __init__(self, finished: _Optional[_Union[Finished, _Mapping]] = ..., error: _Optional[_Union[Error, _Mapping]] = ..., secret: _Optional[str] = ..., hook_id: _Optional[str] = ..., object_id: _Optional[str] = ..., pubkey_serial: _Optional[int] = ...) -> None: ...

class Finished(_message.Message):
    __slots__ = ("add_key_values", "remove_key_values")
    ADD_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    add_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    remove_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, add_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., remove_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("error",)
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: str
    def __init__(self, error: _Optional[str] = ...) -> None: ...

class HookCallbackResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProjectHooksRequest(_message.Message):
    __slots__ = ("project_id",)
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListOwnedHooksRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class HookInfo(_message.Message):
    __slots__ = ("hook_id", "project_ids", "name", "description", "hook", "trigger", "timeout")
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    project_ids: _containers.RepeatedScalarFieldContainer[str]
    name: str
    description: str
    hook: Hook
    trigger: Trigger
    timeout: int
    def __init__(self, hook_id: _Optional[str] = ..., project_ids: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., hook: _Optional[_Union[Hook, _Mapping]] = ..., trigger: _Optional[_Union[Trigger, _Mapping]] = ..., timeout: _Optional[int] = ...) -> None: ...

class ListProjectHooksResponse(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[HookInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[HookInfo, _Mapping]]] = ...) -> None: ...

class ListOwnedHooksResponse(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[HookInfo]
    def __init__(self, infos: _Optional[_Iterable[_Union[HookInfo, _Mapping]]] = ...) -> None: ...

class AddProjectsToHookRequest(_message.Message):
    __slots__ = ("hook_id", "project_ids")
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    hook_id: str
    project_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, hook_id: _Optional[str] = ..., project_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AddProjectsToHookResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
