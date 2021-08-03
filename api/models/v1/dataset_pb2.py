# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/models/v1/dataset.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from api.models.v1 import common_models_pb2 as api_dot_models_dot_v1_dot_common__models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/models/v1/dataset.proto',
  package='api.models.v1',
  syntax='proto3',
  serialized_options=b'\n2com.github.ScienceObjectsDB.java_api.api.models.v1B\rDatasetModelsP\001Z0github.com/ScienceObjectsDB/go-api/api/models/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x61pi/models/v1/dataset.proto\x12\rapi.models.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!api/models/v1/common_models.proto\"\x91\x03\n\x07\x44\x61taset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x34\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12,\n\x06labels\x18\x05 \x03(\x0b\x32\x14.api.models.v1.LabelR\x06labels\x12\x33\n\x08metadata\x18\x06 \x03(\x0b\x32\x17.api.models.v1.MetadataR\x08metadata\x12\x1d\n\nproject_id\x18\x07 \x01(\tR\tprojectId\x12\x1b\n\tis_public\x18\x08 \x01(\x08R\x08isPublic\x12-\n\x06status\x18\t \x01(\x0e\x32\x15.api.models.v1.StatusR\x06status\x12<\n\x0cversion_tags\x18\n \x03(\x0b\x32\x19.api.models.v1.VersionTagR\x0bversionTags\"\xa8\x03\n\x0e\x44\x61tasetVersion\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12,\n\x06labels\x18\x04 \x03(\x0b\x32\x14.api.models.v1.LabelR\x06labels\x12\x33\n\x08metadata\x18\x05 \x03(\x0b\x32\x17.api.models.v1.MetadataR\x08metadata\x12\x34\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x30\n\x07version\x18\x07 \x01(\x0b\x32\x16.api.models.v1.VersionR\x07version\x12(\n\x10object_group_ids\x18\x08 \x03(\tR\x0eobjectGroupIds\x12!\n\x0cobject_count\x18\t \x01(\x03R\x0bobjectCount\x12-\n\x06status\x18\n \x01(\x0e\x32\x15.api.models.v1.StatusR\x06statusBw\n2com.github.ScienceObjectsDB.java_api.api.models.v1B\rDatasetModelsP\x01Z0github.com/ScienceObjectsDB/go-api/api/models/v1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,api_dot_models_dot_v1_dot_common__models__pb2.DESCRIPTOR,])




_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='api.models.v1.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.models.v1.Dataset.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.models.v1.Dataset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='api.models.v1.Dataset.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='api.models.v1.Dataset.created', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='created', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='api.models.v1.Dataset.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='api.models.v1.Dataset.metadata', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='api.models.v1.Dataset.project_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_public', full_name='api.models.v1.Dataset.is_public', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='isPublic', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.models.v1.Dataset.status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_tags', full_name='api.models.v1.Dataset.version_tags', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='versionTags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=516,
)


_DATASETVERSION = _descriptor.Descriptor(
  name='DatasetVersion',
  full_name='api.models.v1.DatasetVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.models.v1.DatasetVersion.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='api.models.v1.DatasetVersion.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='datasetId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='api.models.v1.DatasetVersion.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='api.models.v1.DatasetVersion.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='api.models.v1.DatasetVersion.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created', full_name='api.models.v1.DatasetVersion.created', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='created', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='api.models.v1.DatasetVersion.version', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_group_ids', full_name='api.models.v1.DatasetVersion.object_group_ids', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectGroupIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_count', full_name='api.models.v1.DatasetVersion.object_count', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='objectCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='api.models.v1.DatasetVersion.status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=943,
)

_DATASET.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASET.fields_by_name['labels'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._LABEL
_DATASET.fields_by_name['metadata'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._METADATA
_DATASET.fields_by_name['status'].enum_type = api_dot_models_dot_v1_dot_common__models__pb2._STATUS
_DATASET.fields_by_name['version_tags'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._VERSIONTAG
_DATASETVERSION.fields_by_name['labels'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._LABEL
_DATASETVERSION.fields_by_name['metadata'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._METADATA
_DATASETVERSION.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DATASETVERSION.fields_by_name['version'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._VERSION
_DATASETVERSION.fields_by_name['status'].enum_type = api_dot_models_dot_v1_dot_common__models__pb2._STATUS
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['DatasetVersion'] = _DATASETVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'api.models.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:api.models.v1.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

DatasetVersion = _reflection.GeneratedProtocolMessageType('DatasetVersion', (_message.Message,), {
  'DESCRIPTOR' : _DATASETVERSION,
  '__module__' : 'api.models.v1.dataset_pb2'
  # @@protoc_insertion_point(class_scope:api.models.v1.DatasetVersion)
  })
_sym_db.RegisterMessage(DatasetVersion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
