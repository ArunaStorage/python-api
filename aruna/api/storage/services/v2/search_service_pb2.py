# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aruna/api/storage/services/v2/search_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'aruna/api/storage/services/v2/search_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2aruna/api/storage/services/v2/search_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\"t\n\x16SearchResourcesRequest\x12\x14\n\x05query\x18\x01 \x01(\tR\x05query\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x14\n\x05limit\x18\x03 \x01(\x03R\x05limit\x12\x16\n\x06offset\x18\x04 \x01(\x03R\x06offset\"\xad\x01\n\x17SearchResourcesResponse\x12J\n\tresources\x18\x01 \x03(\x0b\x32,.aruna.api.storage.models.v2.GenericResourceR\tresources\x12\'\n\x0f\x65stimated_total\x18\x02 \x01(\x03R\x0e\x65stimatedTotal\x12\x1d\n\nlast_index\x18\x03 \x01(\x03R\tlastIndex\"5\n\x12GetResourceRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\"\xb0\x01\n\x16ResourceWithPermission\x12H\n\x08resource\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v2.GenericResourceR\x08resource\x12L\n\npermission\x18\x02 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\npermission\"h\n\x13GetResourceResponse\x12Q\n\x08resource\x18\x01 \x01(\x0b\x32\x35.aruna.api.storage.services.v2.ResourceWithPermissionR\x08resource\"8\n\x13GetResourcesRequest\x12!\n\x0cresource_ids\x18\x01 \x03(\tR\x0bresourceIds\"k\n\x14GetResourcesResponse\x12S\n\tresources\x18\x01 \x03(\x0b\x32\x35.aruna.api.storage.services.v2.ResourceWithPermissionR\tresources\"Y\n\x1cRequestResourceAccessRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"\x1f\n\x1dRequestResourceAccessResponse2\x97\x05\n\rSearchService\x12\x97\x01\n\x0fSearchResources\x12\x35.aruna.api.storage.services.v2.SearchResourcesRequest\x1a\x36.aruna.api.storage.services.v2.SearchResourcesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v2/search:\x01*\x12\x99\x01\n\x0bGetResource\x12\x31.aruna.api.storage.services.v2.GetResourceRequest\x1a\x32.aruna.api.storage.services.v2.GetResourceResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v2/resources/{resource_id}\x12\x8e\x01\n\x0cGetResources\x12\x32.aruna.api.storage.services.v2.GetResourcesRequest\x1a\x33.aruna.api.storage.services.v2.GetResourcesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v2/resources\x12\xbe\x01\n\x15RequestResourceAccess\x12;.aruna.api.storage.services.v2.RequestResourceAccessRequest\x1a<.aruna.api.storage.services.v2.RequestResourceAccessResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v2/resources/{resource_id}/accessB\x92\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\rSearchServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.search_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\rSearchServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_SEARCHSERVICE'].methods_by_name['SearchResources']._loaded_options = None
  _globals['_SEARCHSERVICE'].methods_by_name['SearchResources']._serialized_options = b'\202\323\344\223\002\017\"\n/v2/search:\001*'
  _globals['_SEARCHSERVICE'].methods_by_name['GetResource']._loaded_options = None
  _globals['_SEARCHSERVICE'].methods_by_name['GetResource']._serialized_options = b'\202\323\344\223\002\035\022\033/v2/resources/{resource_id}'
  _globals['_SEARCHSERVICE'].methods_by_name['GetResources']._loaded_options = None
  _globals['_SEARCHSERVICE'].methods_by_name['GetResources']._serialized_options = b'\202\323\344\223\002\017\022\r/v2/resources'
  _globals['_SEARCHSERVICE'].methods_by_name['RequestResourceAccess']._loaded_options = None
  _globals['_SEARCHSERVICE'].methods_by_name['RequestResourceAccess']._serialized_options = b'\202\323\344\223\002$\022\"/v2/resources/{resource_id}/access'
  _globals['_SEARCHRESOURCESREQUEST']._serialized_start=157
  _globals['_SEARCHRESOURCESREQUEST']._serialized_end=273
  _globals['_SEARCHRESOURCESRESPONSE']._serialized_start=276
  _globals['_SEARCHRESOURCESRESPONSE']._serialized_end=449
  _globals['_GETRESOURCEREQUEST']._serialized_start=451
  _globals['_GETRESOURCEREQUEST']._serialized_end=504
  _globals['_RESOURCEWITHPERMISSION']._serialized_start=507
  _globals['_RESOURCEWITHPERMISSION']._serialized_end=683
  _globals['_GETRESOURCERESPONSE']._serialized_start=685
  _globals['_GETRESOURCERESPONSE']._serialized_end=789
  _globals['_GETRESOURCESREQUEST']._serialized_start=791
  _globals['_GETRESOURCESREQUEST']._serialized_end=847
  _globals['_GETRESOURCESRESPONSE']._serialized_start=849
  _globals['_GETRESOURCESRESPONSE']._serialized_end=956
  _globals['_REQUESTRESOURCEACCESSREQUEST']._serialized_start=958
  _globals['_REQUESTRESOURCEACCESSREQUEST']._serialized_end=1047
  _globals['_REQUESTRESOURCEACCESSRESPONSE']._serialized_start=1049
  _globals['_REQUESTRESOURCEACCESSRESPONSE']._serialized_end=1080
  _globals['_SEARCHSERVICE']._serialized_start=1083
  _globals['_SEARCHSERVICE']._serialized_end=1746
# @@protoc_insertion_point(module_scope)
