# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/services/v1/dataset_service_models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.models.v1 import dataset_pb2 as api_dot_models_dot_v1_dot_dataset__pb2
from api.models.v1 import common_models_pb2 as api_dot_models_dot_v1_dot_common__models__pb2
from api.models.v1 import object_models_pb2 as api_dot_models_dot_v1_dot_object__models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/services/v1/dataset_service_models.proto',
  package='api.services.v1',
  syntax='proto3',
  serialized_options=b'\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\024DatasetServiceModelsP\001Z2github.com/ScienceObjectsDB/go-api/api/services/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,api/services/v1/dataset_service_models.proto\x12\x0f\x61pi.services.v1\x1a\x1b\x61pi/models/v1/dataset.proto\x1a!api/models/v1/common_models.proto\x1a!api/models/v1/object_models.proto\"\x89\x01\n\x14\x43reateDatasetRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12$\n\x06labels\x18\x04 \x03(\x0b\x32\x14.api.models.v1.Label\x12)\n\x08metadata\x18\x05 \x03(\x0b\x32\x17.api.models.v1.Metadata\"#\n\x15\x43reateDatasetResponse\x12\n\n\x02id\x18\x01 \x01(\t\"\x1f\n\x11GetDatasetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"=\n\x12GetDatasetResponse\x12\'\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x16.api.models.v1.Dataset\"\'\n\x19GetDatasetVersionsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"U\n\x1aGetDatasetVersionsResponse\x12\x37\n\x10\x64\x61taset_versions\x18\x01 \x03(\x0b\x32\x1d.api.models.v1.DatasetVersion\"+\n\x1dGetDatasetObjectGroupsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"S\n\x1eGetDatasetObjectGroupsResponse\x12\x31\n\robject_groups\x18\x01 \x03(\x0b\x32\x1a.api.models.v1.ObjectGroup\"3\n%GetCurrentObjectGroupRevisionsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"l\n&GetCurrentObjectGroupRevisionsResponse\x12\x42\n\x16object_group_revisions\x18\x01 \x03(\x0b\x32\".api.models.v1.ObjectGroupRevision\"W\n\x19UpdateDatasetFieldRequest\x12:\n\x0eupdate_request\x18\x01 \x01(\x0b\x32\".api.models.v1.UpdateFieldsRequest\"\x1c\n\x1aUpdateDatasetFieldResponse\"\"\n\x14\x44\x65leteDatasetRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteDatasetResponse\"\xea\x01\n\x1cReleaseDatasetVersionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\'\n\x07version\x18\x03 \x01(\x0b\x32\x16.api.models.v1.Version\x12\x18\n\x10object_group_ids\x18\x04 \x03(\t\x12$\n\x06labels\x18\x05 \x03(\x0b\x32\x14.api.models.v1.Label\x12)\n\x08metadata\x18\x06 \x03(\x0b\x32\x17.api.models.v1.Metadata\x12\x14\n\x0crevision_ids\x18\x07 \x03(\t\"+\n\x1dReleaseDatasetVersionResponse\x12\n\n\x02id\x18\x01 \x01(\t\"&\n\x18GetDatasetVersionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"S\n\x19GetDatasetVersionResponse\x12\x36\n\x0f\x64\x61taset_version\x18\x01 \x01(\x0b\x32\x1d.api.models.v1.DatasetVersion\".\n GetDatsetVersionRevisionsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"f\n!GetDatsetVersionRevisionsResponse\x12\x41\n\x15object_group_revision\x18\x01 \x03(\x0b\x32\".api.models.v1.ObjectGroupRevision\")\n\x1b\x44\x65leteDatasetVersionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1e\n\x1c\x44\x65leteDatasetVersionResponseB\x82\x01\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\x14\x44\x61tasetServiceModelsP\x01Z2github.com/ScienceObjectsDB/go-api/api/services/v1b\x06proto3'
  ,
  dependencies=[api_dot_models_dot_v1_dot_dataset__pb2.DESCRIPTOR,api_dot_models_dot_v1_dot_common__models__pb2.DESCRIPTOR,api_dot_models_dot_v1_dot_object__models__pb2.DESCRIPTOR,])




_CREATEDATASETREQUEST = _descriptor.Descriptor(
  name='CreateDatasetRequest',
  full_name='api.services.v1.CreateDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.services.v1.CreateDatasetRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='api.services.v1.CreateDatasetRequest.project_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='api.services.v1.CreateDatasetRequest.labels', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='api.services.v1.CreateDatasetRequest.metadata', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=165,
  serialized_end=302,
)


_CREATEDATASETRESPONSE = _descriptor.Descriptor(
  name='CreateDatasetResponse',
  full_name='api.services.v1.CreateDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.CreateDatasetResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=304,
  serialized_end=339,
)


_GETDATASETREQUEST = _descriptor.Descriptor(
  name='GetDatasetRequest',
  full_name='api.services.v1.GetDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetDatasetRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=341,
  serialized_end=372,
)


_GETDATASETRESPONSE = _descriptor.Descriptor(
  name='GetDatasetResponse',
  full_name='api.services.v1.GetDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset', full_name='api.services.v1.GetDatasetResponse.dataset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=374,
  serialized_end=435,
)


_GETDATASETVERSIONSREQUEST = _descriptor.Descriptor(
  name='GetDatasetVersionsRequest',
  full_name='api.services.v1.GetDatasetVersionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetDatasetVersionsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=437,
  serialized_end=476,
)


_GETDATASETVERSIONSRESPONSE = _descriptor.Descriptor(
  name='GetDatasetVersionsResponse',
  full_name='api.services.v1.GetDatasetVersionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_versions', full_name='api.services.v1.GetDatasetVersionsResponse.dataset_versions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=478,
  serialized_end=563,
)


_GETDATASETOBJECTGROUPSREQUEST = _descriptor.Descriptor(
  name='GetDatasetObjectGroupsRequest',
  full_name='api.services.v1.GetDatasetObjectGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetDatasetObjectGroupsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=565,
  serialized_end=608,
)


_GETDATASETOBJECTGROUPSRESPONSE = _descriptor.Descriptor(
  name='GetDatasetObjectGroupsResponse',
  full_name='api.services.v1.GetDatasetObjectGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_groups', full_name='api.services.v1.GetDatasetObjectGroupsResponse.object_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=610,
  serialized_end=693,
)


_GETCURRENTOBJECTGROUPREVISIONSREQUEST = _descriptor.Descriptor(
  name='GetCurrentObjectGroupRevisionsRequest',
  full_name='api.services.v1.GetCurrentObjectGroupRevisionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetCurrentObjectGroupRevisionsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=695,
  serialized_end=746,
)


_GETCURRENTOBJECTGROUPREVISIONSRESPONSE = _descriptor.Descriptor(
  name='GetCurrentObjectGroupRevisionsResponse',
  full_name='api.services.v1.GetCurrentObjectGroupRevisionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_group_revisions', full_name='api.services.v1.GetCurrentObjectGroupRevisionsResponse.object_group_revisions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=748,
  serialized_end=856,
)


_UPDATEDATASETFIELDREQUEST = _descriptor.Descriptor(
  name='UpdateDatasetFieldRequest',
  full_name='api.services.v1.UpdateDatasetFieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_request', full_name='api.services.v1.UpdateDatasetFieldRequest.update_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=858,
  serialized_end=945,
)


_UPDATEDATASETFIELDRESPONSE = _descriptor.Descriptor(
  name='UpdateDatasetFieldResponse',
  full_name='api.services.v1.UpdateDatasetFieldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=947,
  serialized_end=975,
)


_DELETEDATASETREQUEST = _descriptor.Descriptor(
  name='DeleteDatasetRequest',
  full_name='api.services.v1.DeleteDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.DeleteDatasetRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=977,
  serialized_end=1011,
)


_DELETEDATASETRESPONSE = _descriptor.Descriptor(
  name='DeleteDatasetResponse',
  full_name='api.services.v1.DeleteDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1013,
  serialized_end=1036,
)


_RELEASEDATASETVERSIONREQUEST = _descriptor.Descriptor(
  name='ReleaseDatasetVersionRequest',
  full_name='api.services.v1.ReleaseDatasetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.services.v1.ReleaseDatasetVersionRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='api.services.v1.ReleaseDatasetVersionRequest.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='api.services.v1.ReleaseDatasetVersionRequest.version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='object_group_ids', full_name='api.services.v1.ReleaseDatasetVersionRequest.object_group_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='api.services.v1.ReleaseDatasetVersionRequest.labels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='api.services.v1.ReleaseDatasetVersionRequest.metadata', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_ids', full_name='api.services.v1.ReleaseDatasetVersionRequest.revision_ids', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1039,
  serialized_end=1273,
)


_RELEASEDATASETVERSIONRESPONSE = _descriptor.Descriptor(
  name='ReleaseDatasetVersionResponse',
  full_name='api.services.v1.ReleaseDatasetVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.ReleaseDatasetVersionResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1275,
  serialized_end=1318,
)


_GETDATASETVERSIONREQUEST = _descriptor.Descriptor(
  name='GetDatasetVersionRequest',
  full_name='api.services.v1.GetDatasetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetDatasetVersionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1320,
  serialized_end=1358,
)


_GETDATASETVERSIONRESPONSE = _descriptor.Descriptor(
  name='GetDatasetVersionResponse',
  full_name='api.services.v1.GetDatasetVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_version', full_name='api.services.v1.GetDatasetVersionResponse.dataset_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1360,
  serialized_end=1443,
)


_GETDATSETVERSIONREVISIONSREQUEST = _descriptor.Descriptor(
  name='GetDatsetVersionRevisionsRequest',
  full_name='api.services.v1.GetDatsetVersionRevisionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.GetDatsetVersionRevisionsRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1445,
  serialized_end=1491,
)


_GETDATSETVERSIONREVISIONSRESPONSE = _descriptor.Descriptor(
  name='GetDatsetVersionRevisionsResponse',
  full_name='api.services.v1.GetDatsetVersionRevisionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_group_revision', full_name='api.services.v1.GetDatsetVersionRevisionsResponse.object_group_revision', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1493,
  serialized_end=1595,
)


_DELETEDATASETVERSIONREQUEST = _descriptor.Descriptor(
  name='DeleteDatasetVersionRequest',
  full_name='api.services.v1.DeleteDatasetVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='api.services.v1.DeleteDatasetVersionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1597,
  serialized_end=1638,
)


_DELETEDATASETVERSIONRESPONSE = _descriptor.Descriptor(
  name='DeleteDatasetVersionResponse',
  full_name='api.services.v1.DeleteDatasetVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1640,
  serialized_end=1670,
)

_CREATEDATASETREQUEST.fields_by_name['labels'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._LABEL
_CREATEDATASETREQUEST.fields_by_name['metadata'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._METADATA
_GETDATASETRESPONSE.fields_by_name['dataset'].message_type = api_dot_models_dot_v1_dot_dataset__pb2._DATASET
_GETDATASETVERSIONSRESPONSE.fields_by_name['dataset_versions'].message_type = api_dot_models_dot_v1_dot_dataset__pb2._DATASETVERSION
_GETDATASETOBJECTGROUPSRESPONSE.fields_by_name['object_groups'].message_type = api_dot_models_dot_v1_dot_object__models__pb2._OBJECTGROUP
_GETCURRENTOBJECTGROUPREVISIONSRESPONSE.fields_by_name['object_group_revisions'].message_type = api_dot_models_dot_v1_dot_object__models__pb2._OBJECTGROUPREVISION
_UPDATEDATASETFIELDREQUEST.fields_by_name['update_request'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._UPDATEFIELDSREQUEST
_RELEASEDATASETVERSIONREQUEST.fields_by_name['version'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._VERSION
_RELEASEDATASETVERSIONREQUEST.fields_by_name['labels'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._LABEL
_RELEASEDATASETVERSIONREQUEST.fields_by_name['metadata'].message_type = api_dot_models_dot_v1_dot_common__models__pb2._METADATA
_GETDATASETVERSIONRESPONSE.fields_by_name['dataset_version'].message_type = api_dot_models_dot_v1_dot_dataset__pb2._DATASETVERSION
_GETDATSETVERSIONREVISIONSRESPONSE.fields_by_name['object_group_revision'].message_type = api_dot_models_dot_v1_dot_object__models__pb2._OBJECTGROUPREVISION
DESCRIPTOR.message_types_by_name['CreateDatasetRequest'] = _CREATEDATASETREQUEST
DESCRIPTOR.message_types_by_name['CreateDatasetResponse'] = _CREATEDATASETRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetRequest'] = _GETDATASETREQUEST
DESCRIPTOR.message_types_by_name['GetDatasetResponse'] = _GETDATASETRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetVersionsRequest'] = _GETDATASETVERSIONSREQUEST
DESCRIPTOR.message_types_by_name['GetDatasetVersionsResponse'] = _GETDATASETVERSIONSRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetObjectGroupsRequest'] = _GETDATASETOBJECTGROUPSREQUEST
DESCRIPTOR.message_types_by_name['GetDatasetObjectGroupsResponse'] = _GETDATASETOBJECTGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['GetCurrentObjectGroupRevisionsRequest'] = _GETCURRENTOBJECTGROUPREVISIONSREQUEST
DESCRIPTOR.message_types_by_name['GetCurrentObjectGroupRevisionsResponse'] = _GETCURRENTOBJECTGROUPREVISIONSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateDatasetFieldRequest'] = _UPDATEDATASETFIELDREQUEST
DESCRIPTOR.message_types_by_name['UpdateDatasetFieldResponse'] = _UPDATEDATASETFIELDRESPONSE
DESCRIPTOR.message_types_by_name['DeleteDatasetRequest'] = _DELETEDATASETREQUEST
DESCRIPTOR.message_types_by_name['DeleteDatasetResponse'] = _DELETEDATASETRESPONSE
DESCRIPTOR.message_types_by_name['ReleaseDatasetVersionRequest'] = _RELEASEDATASETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['ReleaseDatasetVersionResponse'] = _RELEASEDATASETVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetVersionRequest'] = _GETDATASETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['GetDatasetVersionResponse'] = _GETDATASETVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['GetDatsetVersionRevisionsRequest'] = _GETDATSETVERSIONREVISIONSREQUEST
DESCRIPTOR.message_types_by_name['GetDatsetVersionRevisionsResponse'] = _GETDATSETVERSIONREVISIONSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteDatasetVersionRequest'] = _DELETEDATASETVERSIONREQUEST
DESCRIPTOR.message_types_by_name['DeleteDatasetVersionResponse'] = _DELETEDATASETVERSIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.CreateDatasetRequest)
  })
_sym_db.RegisterMessage(CreateDatasetRequest)

CreateDatasetResponse = _reflection.GeneratedProtocolMessageType('CreateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.CreateDatasetResponse)
  })
_sym_db.RegisterMessage(CreateDatasetResponse)

GetDatasetRequest = _reflection.GeneratedProtocolMessageType('GetDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetRequest)
  })
_sym_db.RegisterMessage(GetDatasetRequest)

GetDatasetResponse = _reflection.GeneratedProtocolMessageType('GetDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetResponse)
  })
_sym_db.RegisterMessage(GetDatasetResponse)

GetDatasetVersionsRequest = _reflection.GeneratedProtocolMessageType('GetDatasetVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONSREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetVersionsRequest)
  })
_sym_db.RegisterMessage(GetDatasetVersionsRequest)

GetDatasetVersionsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONSRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetVersionsResponse)
  })
_sym_db.RegisterMessage(GetDatasetVersionsResponse)

GetDatasetObjectGroupsRequest = _reflection.GeneratedProtocolMessageType('GetDatasetObjectGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETOBJECTGROUPSREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetObjectGroupsRequest)
  })
_sym_db.RegisterMessage(GetDatasetObjectGroupsRequest)

GetDatasetObjectGroupsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetObjectGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETOBJECTGROUPSRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetObjectGroupsResponse)
  })
_sym_db.RegisterMessage(GetDatasetObjectGroupsResponse)

GetCurrentObjectGroupRevisionsRequest = _reflection.GeneratedProtocolMessageType('GetCurrentObjectGroupRevisionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCURRENTOBJECTGROUPREVISIONSREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetCurrentObjectGroupRevisionsRequest)
  })
_sym_db.RegisterMessage(GetCurrentObjectGroupRevisionsRequest)

GetCurrentObjectGroupRevisionsResponse = _reflection.GeneratedProtocolMessageType('GetCurrentObjectGroupRevisionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCURRENTOBJECTGROUPREVISIONSRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetCurrentObjectGroupRevisionsResponse)
  })
_sym_db.RegisterMessage(GetCurrentObjectGroupRevisionsResponse)

UpdateDatasetFieldRequest = _reflection.GeneratedProtocolMessageType('UpdateDatasetFieldRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETFIELDREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.UpdateDatasetFieldRequest)
  })
_sym_db.RegisterMessage(UpdateDatasetFieldRequest)

UpdateDatasetFieldResponse = _reflection.GeneratedProtocolMessageType('UpdateDatasetFieldResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETFIELDRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.UpdateDatasetFieldResponse)
  })
_sym_db.RegisterMessage(UpdateDatasetFieldResponse)

DeleteDatasetRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.DeleteDatasetRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetRequest)

DeleteDatasetResponse = _reflection.GeneratedProtocolMessageType('DeleteDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.DeleteDatasetResponse)
  })
_sym_db.RegisterMessage(DeleteDatasetResponse)

ReleaseDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('ReleaseDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEDATASETVERSIONREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.ReleaseDatasetVersionRequest)
  })
_sym_db.RegisterMessage(ReleaseDatasetVersionRequest)

ReleaseDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('ReleaseDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEDATASETVERSIONRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.ReleaseDatasetVersionResponse)
  })
_sym_db.RegisterMessage(ReleaseDatasetVersionResponse)

GetDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('GetDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetVersionRequest)
  })
_sym_db.RegisterMessage(GetDatasetVersionRequest)

GetDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('GetDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatasetVersionResponse)
  })
_sym_db.RegisterMessage(GetDatasetVersionResponse)

GetDatsetVersionRevisionsRequest = _reflection.GeneratedProtocolMessageType('GetDatsetVersionRevisionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATSETVERSIONREVISIONSREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatsetVersionRevisionsRequest)
  })
_sym_db.RegisterMessage(GetDatsetVersionRevisionsRequest)

GetDatsetVersionRevisionsResponse = _reflection.GeneratedProtocolMessageType('GetDatsetVersionRevisionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATSETVERSIONREVISIONSRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.GetDatsetVersionRevisionsResponse)
  })
_sym_db.RegisterMessage(GetDatsetVersionRevisionsResponse)

DeleteDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETVERSIONREQUEST,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.DeleteDatasetVersionRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetVersionRequest)

DeleteDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('DeleteDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETVERSIONRESPONSE,
  '__module__' : 'api.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:api.services.v1.DeleteDatasetVersionResponse)
  })
_sym_db.RegisterMessage(DeleteDatasetVersionResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
