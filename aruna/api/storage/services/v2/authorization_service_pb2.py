# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aruna/api/storage/services/v2/authorization_service.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'aruna/api/storage/services/v2/authorization_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9aruna/api/storage/services/v2/authorization_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\"\x9f\x01\n\x0eUserPermission\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12W\n\x10permission_level\x18\x03 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\x0fpermissionLevel\"\x90\x01\n\x15ResourceAuthorization\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12V\n\x0fuser_permission\x18\x02 \x03(\x0b\x32-.aruna.api.storage.services.v2.UserPermissionR\x0euserPermission\"\xaf\x01\n\x1a\x43reateAuthorizationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12W\n\x10permission_level\x18\x03 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\x0fpermissionLevel\"\xcd\x01\n\x1b\x43reateAuthorizationResponse\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12\x1b\n\tuser_name\x18\x03 \x01(\tR\x08userName\x12W\n\x10permission_level\x18\x04 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\x0fpermissionLevel\"Y\n\x18GetAuthorizationsRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x1c\n\trecursive\x18\x02 \x01(\x08R\trecursive\"y\n\x19GetAuthorizationsResponse\x12\\\n\x0e\x61uthorizations\x18\x01 \x03(\x0b\x32\x34.aruna.api.storage.services.v2.ResourceAuthorizationR\x0e\x61uthorizations\"V\n\x1a\x44\x65leteAuthorizationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1d\n\x1b\x44\x65leteAuthorizationResponse\"\xaf\x01\n\x1aUpdateAuthorizationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12W\n\x10permission_level\x18\x03 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\x0fpermissionLevel\"u\n\x1bUpdateAuthorizationResponse\x12V\n\x0fuser_permission\x18\x01 \x01(\x0b\x32-.aruna.api.storage.services.v2.UserPermissionR\x0euserPermission2\xef\x05\n\x14\x41uthorizationService\x12\xab\x01\n\x13\x43reateAuthorization\x12\x39.aruna.api.storage.services.v2.CreateAuthorizationRequest\x1a:.aruna.api.storage.services.v2.CreateAuthorizationResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v2/authorizations:\x01*\x12\xb0\x01\n\x11GetAuthorizations\x12\x37.aruna.api.storage.services.v2.GetAuthorizationsRequest\x1a\x38.aruna.api.storage.services.v2.GetAuthorizationsResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v2/authorizations/{resource_id}\x12\xb9\x01\n\x13\x44\x65leteAuthorization\x12\x39.aruna.api.storage.services.v2.DeleteAuthorizationRequest\x1a:.aruna.api.storage.services.v2.DeleteAuthorizationResponse\"+\x82\xd3\xe4\x93\x02%* /v2/authorizations/{resource_id}:\x01*\x12\xb9\x01\n\x13UpdateAuthorization\x12\x39.aruna.api.storage.services.v2.UpdateAuthorizationRequest\x1a:.aruna.api.storage.services.v2.UpdateAuthorizationResponse\"+\x82\xd3\xe4\x93\x02%2 /v2/authorizations/{resource_id}:\x01*B\x99\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x14\x41uthorizationServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.authorization_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\024AuthorizationServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['CreateAuthorization']._loaded_options = None
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['CreateAuthorization']._serialized_options = b'\202\323\344\223\002\027\"\022/v2/authorizations:\001*'
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['GetAuthorizations']._loaded_options = None
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['GetAuthorizations']._serialized_options = b'\202\323\344\223\002\"\022 /v2/authorizations/{resource_id}'
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['DeleteAuthorization']._loaded_options = None
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['DeleteAuthorization']._serialized_options = b'\202\323\344\223\002%* /v2/authorizations/{resource_id}:\001*'
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['UpdateAuthorization']._loaded_options = None
  _globals['_AUTHORIZATIONSERVICE'].methods_by_name['UpdateAuthorization']._serialized_options = b'\202\323\344\223\002%2 /v2/authorizations/{resource_id}:\001*'
  _globals['_USERPERMISSION']._serialized_start=165
  _globals['_USERPERMISSION']._serialized_end=324
  _globals['_RESOURCEAUTHORIZATION']._serialized_start=327
  _globals['_RESOURCEAUTHORIZATION']._serialized_end=471
  _globals['_CREATEAUTHORIZATIONREQUEST']._serialized_start=474
  _globals['_CREATEAUTHORIZATIONREQUEST']._serialized_end=649
  _globals['_CREATEAUTHORIZATIONRESPONSE']._serialized_start=652
  _globals['_CREATEAUTHORIZATIONRESPONSE']._serialized_end=857
  _globals['_GETAUTHORIZATIONSREQUEST']._serialized_start=859
  _globals['_GETAUTHORIZATIONSREQUEST']._serialized_end=948
  _globals['_GETAUTHORIZATIONSRESPONSE']._serialized_start=950
  _globals['_GETAUTHORIZATIONSRESPONSE']._serialized_end=1071
  _globals['_DELETEAUTHORIZATIONREQUEST']._serialized_start=1073
  _globals['_DELETEAUTHORIZATIONREQUEST']._serialized_end=1159
  _globals['_DELETEAUTHORIZATIONRESPONSE']._serialized_start=1161
  _globals['_DELETEAUTHORIZATIONRESPONSE']._serialized_end=1190
  _globals['_UPDATEAUTHORIZATIONREQUEST']._serialized_start=1193
  _globals['_UPDATEAUTHORIZATIONREQUEST']._serialized_end=1368
  _globals['_UPDATEAUTHORIZATIONRESPONSE']._serialized_start=1370
  _globals['_UPDATEAUTHORIZATIONRESPONSE']._serialized_end=1487
  _globals['_AUTHORIZATIONSERVICE']._serialized_start=1490
  _globals['_AUTHORIZATIONSERVICE']._serialized_end=2241
# @@protoc_insertion_point(module_scope)
