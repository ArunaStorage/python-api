# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/services/v1/project_service_models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_dataset__pb2
from sciobjsdb.api.storage.models.v1 import projects_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_projects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>sciobjsdb/api/storage/services/v1/project_service_models.proto\x12!sciobjsdb.api.storage.services.v1\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\x1a-sciobjsdb/api/storage/models/v1/dataset.proto\x1a.sciobjsdb/api/storage/models/v1/projects.proto\"\xdb\x01\n\x14\x43reateProjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12M\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32+.sciobjsdb.api.storage.models.v1.AnnotationR\x0b\x61nnotations\"\'\n\x15\x43reateProjectResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x8f\x01\n\x17\x41\x64\x64UserToProjectRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12<\n\x05scope\x18\x02 \x03(\x0e\x32&.sciobjsdb.api.storage.models.v1.RightR\x05scope\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\"\x1a\n\x18\x41\x64\x64UserToProjectResponse\"\'\n\x15\x43reateAPITokenRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"Y\n\x16\x43reateAPITokenResponse\x12?\n\x05token\x18\x01 \x01(\x0b\x32).sciobjsdb.api.storage.models.v1.APITokenR\x05token\"+\n\x19GetProjectDatasetsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"b\n\x1aGetProjectDatasetsResponse\x12\x44\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32(.sciobjsdb.api.storage.models.v1.DatasetR\x08\x64\x61tasets\"\x18\n\x16GetUserProjectsRequest\"_\n\x17GetUserProjectsResponse\x12\x44\n\x08projects\x18\x01 \x03(\x0b\x32(.sciobjsdb.api.storage.models.v1.ProjectR\x08projects\"#\n\x11GetProjectRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"X\n\x12GetProjectResponse\x12\x42\n\x07project\x18\x01 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.ProjectR\x07project\"V\n\x13GetAPITokenResponse\x12?\n\x05token\x18\x01 \x03(\x0b\x32).sciobjsdb.api.storage.models.v1.APITokenR\x05token\"\x14\n\x12GetAPITokenRequest\"\'\n\x15\x44\x65leteAPITokenRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x18\n\x16\x44\x65leteAPITokenResponse\"&\n\x14\x44\x65leteProjectRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x17\n\x15\x44\x65leteProjectResponseB\xa9\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x17ProjectAPIServiceModelsP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.services.v1.project_service_models_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\027ProjectAPIServiceModelsP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _CREATEPROJECTREQUEST._serialized_start=250
  _CREATEPROJECTREQUEST._serialized_end=469
  _CREATEPROJECTRESPONSE._serialized_start=471
  _CREATEPROJECTRESPONSE._serialized_end=510
  _ADDUSERTOPROJECTREQUEST._serialized_start=513
  _ADDUSERTOPROJECTREQUEST._serialized_end=656
  _ADDUSERTOPROJECTRESPONSE._serialized_start=658
  _ADDUSERTOPROJECTRESPONSE._serialized_end=684
  _CREATEAPITOKENREQUEST._serialized_start=686
  _CREATEAPITOKENREQUEST._serialized_end=725
  _CREATEAPITOKENRESPONSE._serialized_start=727
  _CREATEAPITOKENRESPONSE._serialized_end=816
  _GETPROJECTDATASETSREQUEST._serialized_start=818
  _GETPROJECTDATASETSREQUEST._serialized_end=861
  _GETPROJECTDATASETSRESPONSE._serialized_start=863
  _GETPROJECTDATASETSRESPONSE._serialized_end=961
  _GETUSERPROJECTSREQUEST._serialized_start=963
  _GETUSERPROJECTSREQUEST._serialized_end=987
  _GETUSERPROJECTSRESPONSE._serialized_start=989
  _GETUSERPROJECTSRESPONSE._serialized_end=1084
  _GETPROJECTREQUEST._serialized_start=1086
  _GETPROJECTREQUEST._serialized_end=1121
  _GETPROJECTRESPONSE._serialized_start=1123
  _GETPROJECTRESPONSE._serialized_end=1211
  _GETAPITOKENRESPONSE._serialized_start=1213
  _GETAPITOKENRESPONSE._serialized_end=1299
  _GETAPITOKENREQUEST._serialized_start=1301
  _GETAPITOKENREQUEST._serialized_end=1321
  _DELETEAPITOKENREQUEST._serialized_start=1323
  _DELETEAPITOKENREQUEST._serialized_end=1362
  _DELETEAPITOKENRESPONSE._serialized_start=1364
  _DELETEAPITOKENRESPONSE._serialized_end=1388
  _DELETEPROJECTREQUEST._serialized_start=1390
  _DELETEPROJECTREQUEST._serialized_end=1428
  _DELETEPROJECTRESPONSE._serialized_start=1430
  _DELETEPROJECTRESPONSE._serialized_end=1453
# @@protoc_insertion_point(module_scope)
