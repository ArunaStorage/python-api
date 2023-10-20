from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateWorkspaceTemplateRequest(_message.Message):
    __slots__ = ["owner_id", "prefix", "name", "hook_ids", "description", "endpoint_id"]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    owner_id: str
    prefix: str
    name: str
    hook_ids: _containers.RepeatedScalarFieldContainer[str]
    description: str
    endpoint_id: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, owner_id: _Optional[str] = ..., prefix: _Optional[str] = ..., name: _Optional[str] = ..., hook_ids: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., endpoint_id: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateWorkspaceTemplateResponse(_message.Message):
    __slots__ = ["template_id"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class GetWorkspaceTemplateRequest(_message.Message):
    __slots__ = ["template_id"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class GetWorkspaceTemplateResponse(_message.Message):
    __slots__ = ["workspace"]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: WorkspaceInfo
    def __init__(self, workspace: _Optional[_Union[WorkspaceInfo, _Mapping]] = ...) -> None: ...

class DeleteWorkspaceTemplateRequest(_message.Message):
    __slots__ = ["template_id"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class DeleteWorkspaceTemplateResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOwnedWorkspaceTemplatesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListOwnedWorkspaceTemplatesResponse(_message.Message):
    __slots__ = ["workspaces"]
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[WorkspaceInfo]
    def __init__(self, workspaces: _Optional[_Iterable[_Union[WorkspaceInfo, _Mapping]]] = ...) -> None: ...

class WorkspaceInfo(_message.Message):
    __slots__ = ["workspace_id", "name", "description", "owner", "prefix", "hook_ids", "endpoint_ids"]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    HOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_IDS_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    name: str
    description: str
    owner: str
    prefix: str
    hook_ids: str
    endpoint_ids: str
    def __init__(self, workspace_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., owner: _Optional[str] = ..., prefix: _Optional[str] = ..., hook_ids: _Optional[str] = ..., endpoint_ids: _Optional[str] = ...) -> None: ...

class CreateWorkspaceRequest(_message.Message):
    __slots__ = ["workspace_template", "description"]
    WORKSPACE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    workspace_template: str
    description: str
    def __init__(self, workspace_template: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class CreateWorkspaceResponse(_message.Message):
    __slots__ = ["workspace_id", "token", "access_key", "secret_key"]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    token: str
    access_key: str
    secret_key: str
    def __init__(self, workspace_id: _Optional[str] = ..., token: _Optional[str] = ..., access_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class DeleteWorkspaceRequest(_message.Message):
    __slots__ = ["workspace_id"]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    def __init__(self, workspace_id: _Optional[str] = ...) -> None: ...

class DeleteWorkspaceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ClaimWorkspaceRequest(_message.Message):
    __slots__ = ["workspace_id", "token"]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    workspace_id: str
    token: str
    def __init__(self, workspace_id: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class ClaimWorkspaceResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
