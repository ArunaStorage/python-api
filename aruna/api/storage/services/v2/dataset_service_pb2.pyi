from aruna.api.storage.models.v2 import models_pb2 as _models_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import visibility_pb2 as _visibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ["name", "description", "key_values", "relations", "data_class", "project_id", "collection_id", "metadata_license_tag", "default_data_license_tag"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    relations: _containers.RepeatedCompositeFieldContainer[_models_pb2.Relation]
    data_class: _models_pb2.DataClass
    project_id: str
    collection_id: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., relations: _Optional[_Iterable[_Union[_models_pb2.Relation, _Mapping]]] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ..., project_id: _Optional[str] = ..., collection_id: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class CreateDatasetResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class GetDatasetRequest(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class GetDatasetResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class GetDatasetsRequest(_message.Message):
    __slots__ = ["dataset_ids"]
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, dataset_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class GetDatasetsResponse(_message.Message):
    __slots__ = ["datasets"]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[_models_pb2.Dataset]
    def __init__(self, datasets: _Optional[_Iterable[_Union[_models_pb2.Dataset, _Mapping]]] = ...) -> None: ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class DeleteDatasetResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateDatasetNameRequest(_message.Message):
    __slots__ = ["dataset_id", "name"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    name: str
    def __init__(self, dataset_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateDatasetNameResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class UpdateDatasetDescriptionRequest(_message.Message):
    __slots__ = ["dataset_id", "description"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    description: str
    def __init__(self, dataset_id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class UpdateDatasetDescriptionResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class UpdateDatasetKeyValuesRequest(_message.Message):
    __slots__ = ["dataset_id", "add_key_values", "remove_key_values"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    REMOVE_KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    add_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    remove_key_values: _containers.RepeatedCompositeFieldContainer[_models_pb2.KeyValue]
    def __init__(self, dataset_id: _Optional[str] = ..., add_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ..., remove_key_values: _Optional[_Iterable[_Union[_models_pb2.KeyValue, _Mapping]]] = ...) -> None: ...

class UpdateDatasetKeyValuesResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class UpdateDatasetDataClassRequest(_message.Message):
    __slots__ = ["dataset_id", "data_class"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_CLASS_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    data_class: _models_pb2.DataClass
    def __init__(self, dataset_id: _Optional[str] = ..., data_class: _Optional[_Union[_models_pb2.DataClass, str]] = ...) -> None: ...

class UpdateDatasetDataClassResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class SnapshotDatasetRequest(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class SnapshotDatasetResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...

class UpdateDatasetLicensesRequest(_message.Message):
    __slots__ = ["dataset_id", "metadata_license_tag", "default_data_license_tag"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_DATA_LICENSE_TAG_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    metadata_license_tag: str
    default_data_license_tag: str
    def __init__(self, dataset_id: _Optional[str] = ..., metadata_license_tag: _Optional[str] = ..., default_data_license_tag: _Optional[str] = ...) -> None: ...

class UpdateDatasetLicensesResponse(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _models_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_models_pb2.Dataset, _Mapping]] = ...) -> None: ...
