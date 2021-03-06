# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/models/v1/dataset.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_object__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-sciobjsdb/api/storage/models/v1/dataset.proto\x12\x1fsciobjsdb.api.storage.models.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\x1a\x33sciobjsdb/api/storage/models/v1/object_models.proto\"\xc2\x04\n\x07\x44\x61taset\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x34\n\x07\x63reated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12>\n\x06labels\x18\x05 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x06 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\x12\x1d\n\nproject_id\x18\x07 \x01(\tR\tprojectId\x12\x1b\n\tis_public\x18\x08 \x01(\x08R\x08isPublic\x12?\n\x06status\x18\t \x01(\x0e\x32\'.sciobjsdb.api.storage.models.v1.StatusR\x06status\x12\x16\n\x06\x62ucket\x18\n \x01(\tR\x06\x62ucket\x12\x43\n\x05stats\x18\x0b \x01(\x0b\x32-.sciobjsdb.api.storage.models.v1.DatasetStatsR\x05stats\x12R\n\x10metadata_objects\x18\x0c \x03(\x0b\x32\'.sciobjsdb.api.storage.models.v1.ObjectR\x0fmetadataObjects\"\xcb\x05\n\x0e\x44\x61tasetVersion\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\ndataset_id\x18\x04 \x01(\tR\tdatasetId\x12>\n\x06labels\x18\x05 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x06 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\x12\x34\n\x07\x63reated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x42\n\x07version\x18\x08 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.VersionR\x07version\x12(\n\x10object_group_ids\x18\t \x03(\tR\x0eobjectGroupIds\x12!\n\x0cobject_count\x18\n \x01(\x03R\x0bobjectCount\x12?\n\x06status\x18\x0b \x01(\x0e\x32\'.sciobjsdb.api.storage.models.v1.StatusR\x06status\x12\x1d\n\nproject_id\x18\x0c \x01(\tR\tprojectId\x12J\n\x05stats\x18\r \x01(\x0b\x32\x34.sciobjsdb.api.storage.models.v1.DatasetVersionStatsR\x05stats\x12R\n\x10metadata_objects\x18\x0e \x03(\x0b\x32\'.sciobjsdb.api.storage.models.v1.ObjectR\x0fmetadataObjects\"\xa2\x01\n\x0c\x44\x61tasetStats\x12!\n\x0cobject_count\x18\x01 \x01(\x03R\x0bobjectCount\x12,\n\x12object_group_count\x18\x02 \x01(\x03R\x10objectGroupCount\x12\x19\n\x08\x61\x63\x63_size\x18\x03 \x01(\x03R\x07\x61\x63\x63Size\x12&\n\x0f\x61vg_object_size\x18\x04 \x01(\x01R\ravgObjectSize\"\xa9\x01\n\x13\x44\x61tasetVersionStats\x12!\n\x0cobject_count\x18\x01 \x01(\x03R\x0bobjectCount\x12,\n\x12object_group_count\x18\x02 \x01(\x03R\x10objectGroupCount\x12\x19\n\x08\x61\x63\x63_size\x18\x03 \x01(\x03R\x07\x61\x63\x63Size\x12&\n\x0f\x61vg_object_size\x18\x04 \x01(\x01R\ravgObjectSizeB\x9b\x01\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\rDatasetModelsP\x01ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.models.v1.dataset_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\rDatasetModelsP\001ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1'
  _DATASET._serialized_start=222
  _DATASET._serialized_end=800
  _DATASETVERSION._serialized_start=803
  _DATASETVERSION._serialized_end=1518
  _DATASETSTATS._serialized_start=1521
  _DATASETSTATS._serialized_end=1683
  _DATASETVERSIONSTATS._serialized_start=1686
  _DATASETVERSIONSTATS._serialized_end=1855
# @@protoc_insertion_point(module_scope)
