# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/models/v1/projects.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.sciobjsdb/api/storage/models/v1/projects.proto\x12\x1fsciobjsdb.api.storage.models.v1\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\"\xb9\x03\n\x07Project\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\x12;\n\x05users\x18\x06 \x03(\x0b\x32%.sciobjsdb.api.storage.models.v1.UserR\x05users\x12\x16\n\x06\x62ucket\x18\x07 \x01(\tR\x06\x62ucket\x12?\n\x06status\x18\x08 \x01(\x0e\x32\'.sciobjsdb.api.storage.models.v1.StatusR\x06status\x12\x43\n\x05stats\x18\t \x01(\x0b\x32-.sciobjsdb.api.storage.models.v1.ProjectStatsR\x05stats\"\xc1\x01\n\x0cProjectStats\x12!\n\x0cobject_count\x18\x01 \x01(\x03R\x0bobjectCount\x12,\n\x12object_group_count\x18\x02 \x01(\x03R\x10objectGroupCount\x12\x19\n\x08\x61\x63\x63_size\x18\x03 \x01(\x03R\x07\x61\x63\x63Size\x12&\n\x0f\x61vg_object_size\x18\x04 \x01(\x01R\ravgObjectSize\x12\x1d\n\nuser_count\x18\x05 \x01(\x03R\tuserCountB\x9b\x01\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\rProjectModelsP\x01ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.models.v1.projects_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\rProjectModelsP\001ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1'
  _PROJECT._serialized_start=137
  _PROJECT._serialized_end=578
  _PROJECTSTATS._serialized_start=581
  _PROJECTSTATS._serialized_end=774
# @@protoc_insertion_point(module_scope)
