# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/relations_service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5aruna/api/storage/services/v2/relations_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\"\xd7\x01\n\x16ModifyRelationsRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12J\n\radd_relations\x18\x02 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\x0c\x61\x64\x64Relations\x12P\n\x10remove_relations\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\x0fremoveRelations\"\x19\n\x17ModifyRelationsResponse\"6\n\x13GetHierarchyRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\"S\n\x10\x44\x61tasetRelations\x12\x16\n\x06origin\x18\x01 \x01(\tR\x06origin\x12\'\n\x0fobject_children\x18\x02 \x03(\tR\x0eobjectChildren\"\xb2\x01\n\x13\x43ollectionRelations\x12\x16\n\x06origin\x18\x01 \x01(\tR\x06origin\x12Z\n\x10\x64\x61taset_children\x18\x02 \x03(\x0b\x32/.aruna.api.storage.services.v2.DatasetRelationsR\x0f\x64\x61tasetChildren\x12\'\n\x0fobject_children\x18\x03 \x03(\tR\x0eobjectChildren\"\x94\x02\n\x10ProjectRelations\x12\x16\n\x06origin\x18\x01 \x01(\tR\x06origin\x12\x63\n\x13\x63ollection_children\x18\x02 \x03(\x0b\x32\x32.aruna.api.storage.services.v2.CollectionRelationsR\x12\x63ollectionChildren\x12Z\n\x10\x64\x61taset_children\x18\x03 \x03(\x0b\x32/.aruna.api.storage.services.v2.DatasetRelationsR\x0f\x64\x61tasetChildren\x12\'\n\x0fobject_children\x18\x04 \x03(\tR\x0eobjectChildren\"\x8f\x02\n\x14GetHierarchyResponse\x12K\n\x07project\x18\x01 \x01(\x0b\x32/.aruna.api.storage.services.v2.ProjectRelationsH\x00R\x07project\x12T\n\ncollection\x18\x02 \x01(\x0b\x32\x32.aruna.api.storage.services.v2.CollectionRelationsH\x00R\ncollection\x12K\n\x07\x64\x61taset\x18\x03 \x01(\x0b\x32/.aruna.api.storage.services.v2.DatasetRelationsH\x00R\x07\x64\x61tasetB\x07\n\x05graph2\xd8\x02\n\x10RelationsService\x12\x9a\x01\n\x0fModifyRelations\x12\x35.aruna.api.storage.services.v2.ModifyRelationsRequest\x1a\x36.aruna.api.storage.services.v2.ModifyRelationsResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v2/relations:\x01*\x12\xa6\x01\n\x0cGetHierarchy\x12\x32.aruna.api.storage.services.v2.GetHierarchyRequest\x1a\x33.aruna.api.storage.services.v2.GetHierarchyResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v2/relations/{resource_id}/hierarchyB\x95\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x10RelationsServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.relations_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\020RelationsServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_RELATIONSSERVICE'].methods_by_name['ModifyRelations']._options = None
  _globals['_RELATIONSSERVICE'].methods_by_name['ModifyRelations']._serialized_options = b'\202\323\344\223\002\022\"\r/v2/relations:\001*'
  _globals['_RELATIONSSERVICE'].methods_by_name['GetHierarchy']._options = None
  _globals['_RELATIONSSERVICE'].methods_by_name['GetHierarchy']._serialized_options = b'\202\323\344\223\002\'\022%/v2/relations/{resource_id}/hierarchy'
  _globals['_MODIFYRELATIONSREQUEST']._serialized_start=161
  _globals['_MODIFYRELATIONSREQUEST']._serialized_end=376
  _globals['_MODIFYRELATIONSRESPONSE']._serialized_start=378
  _globals['_MODIFYRELATIONSRESPONSE']._serialized_end=403
  _globals['_GETHIERARCHYREQUEST']._serialized_start=405
  _globals['_GETHIERARCHYREQUEST']._serialized_end=459
  _globals['_DATASETRELATIONS']._serialized_start=461
  _globals['_DATASETRELATIONS']._serialized_end=544
  _globals['_COLLECTIONRELATIONS']._serialized_start=547
  _globals['_COLLECTIONRELATIONS']._serialized_end=725
  _globals['_PROJECTRELATIONS']._serialized_start=728
  _globals['_PROJECTRELATIONS']._serialized_end=1004
  _globals['_GETHIERARCHYRESPONSE']._serialized_start=1007
  _globals['_GETHIERARCHYRESPONSE']._serialized_end=1278
  _globals['_RELATIONSSERVICE']._serialized_start=1281
  _globals['_RELATIONSSERVICE']._serialized_end=1625
# @@protoc_insertion_point(module_scope)
