from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRuleRequest(_message.Message):
    __slots__ = ("rule", "description", "public")
    RULE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    rule: str
    description: str
    public: bool
    def __init__(self, rule: _Optional[str] = ..., description: _Optional[str] = ..., public: bool = ...) -> None: ...

class CreateRuleResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRuleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("id", "rule", "description", "public", "owner")
    ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule: str
    description: str
    public: bool
    owner: str
    def __init__(self, id: _Optional[str] = ..., rule: _Optional[str] = ..., description: _Optional[str] = ..., public: bool = ..., owner: _Optional[str] = ...) -> None: ...

class GetRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]] = ...) -> None: ...

class ListRuleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRuleResponse(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    def __init__(self, rules: _Optional[_Iterable[_Union[Rule, _Mapping]]] = ...) -> None: ...

class UpdateRuleRequest(_message.Message):
    __slots__ = ("id", "rule", "description", "public")
    ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule: str
    description: str
    public: bool
    def __init__(self, id: _Optional[str] = ..., rule: _Optional[str] = ..., description: _Optional[str] = ..., public: bool = ...) -> None: ...

class UpdateRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: Rule
    def __init__(self, rule: _Optional[_Union[Rule, _Mapping]] = ...) -> None: ...

class DeleteRuleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteRuleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateRuleBindingRequest(_message.Message):
    __slots__ = ("rule_id", "object_id", "cascading")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CASCADING_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    object_id: str
    cascading: bool
    def __init__(self, rule_id: _Optional[str] = ..., object_id: _Optional[str] = ..., cascading: bool = ...) -> None: ...

class CreateRuleBindingResponse(_message.Message):
    __slots__ = ("rule_id", "object_id", "cascading")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CASCADING_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    object_id: str
    cascading: bool
    def __init__(self, rule_id: _Optional[str] = ..., object_id: _Optional[str] = ..., cascading: bool = ...) -> None: ...

class DeleteRuleBindingRequest(_message.Message):
    __slots__ = ("rule_id", "object_id")
    RULE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    rule_id: str
    object_id: str
    def __init__(self, rule_id: _Optional[str] = ..., object_id: _Optional[str] = ...) -> None: ...

class DeleteRuleBindingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
