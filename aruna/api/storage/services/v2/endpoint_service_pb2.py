# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/endpoint_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4aruna/api/storage/services/v2/endpoint_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\"\x81\x02\n\x15\x43reateEndpointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12K\n\nep_variant\x18\x02 \x01(\x0e\x32,.aruna.api.storage.models.v2.EndpointVariantR\tepVariant\x12\x1b\n\tis_public\x18\x03 \x01(\x08R\x08isPublic\x12\x16\n\x06pubkey\x18\x04 \x01(\tR\x06pubkey\x12R\n\x0chost_configs\x18\x05 \x03(\x0b\x32/.aruna.api.storage.models.v2.EndpointHostConfigR\x0bhostConfigs\"[\n\x16\x43reateEndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v2.EndpointR\x08\x65ndpoint\"\x19\n\x17\x46ullSyncEndpointRequest\"\xf7\x01\n\x18\x46ullSyncEndpointResponse\x12Y\n\x10generic_resource\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v2.GenericResourceH\x00R\x0fgenericResource\x12\x37\n\x04user\x18\x02 \x01(\x0b\x32!.aruna.api.storage.models.v2.UserH\x00R\x04user\x12=\n\x06pubkey\x18\x03 \x01(\x0b\x32#.aruna.api.storage.models.v2.PubkeyH\x00R\x06pubkeyB\x08\n\x06target\"j\n\x12GetEndpointRequest\x12%\n\rendpoint_name\x18\x01 \x01(\tH\x00R\x0c\x65ndpointName\x12!\n\x0b\x65ndpoint_id\x18\x02 \x01(\tH\x00R\nendpointIdB\n\n\x08\x65ndpoint\"X\n\x13GetEndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v2.EndpointR\x08\x65ndpoint\"\x15\n\x13GetEndpointsRequest\"[\n\x14GetEndpointsResponse\x12\x43\n\tendpoints\x18\x01 \x03(\x0b\x32%.aruna.api.storage.models.v2.EndpointR\tendpoints\"8\n\x15\x44\x65leteEndpointRequest\x12\x1f\n\x0b\x65ndpoint_id\x18\x01 \x01(\tR\nendpointId\"\x18\n\x16\x44\x65leteEndpointResponse\"\x1b\n\x19GetDefaultEndpointRequest\"_\n\x1aGetDefaultEndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v2.EndpointR\x08\x65ndpoint2\xb9\x07\n\x0f\x45ndpointService\x12\x96\x01\n\x0e\x43reateEndpoint\x12\x34.aruna.api.storage.services.v2.CreateEndpointRequest\x1a\x35.aruna.api.storage.services.v2.CreateEndpointResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v2/endpoint:\x01*\x12\xa0\x01\n\x10\x46ullSyncEndpoint\x12\x36.aruna.api.storage.services.v2.FullSyncEndpointRequest\x1a\x37.aruna.api.storage.services.v2.FullSyncEndpointResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v2/endpoint/sync0\x01\x12\x8a\x01\n\x0bGetEndpoint\x12\x31.aruna.api.storage.services.v2.GetEndpointRequest\x1a\x32.aruna.api.storage.services.v2.GetEndpointResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v2/endpoint\x12\x8e\x01\n\x0cGetEndpoints\x12\x32.aruna.api.storage.services.v2.GetEndpointsRequest\x1a\x33.aruna.api.storage.services.v2.GetEndpointsResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v2/endpoints\x12\xa1\x01\n\x0e\x44\x65leteEndpoint\x12\x34.aruna.api.storage.services.v2.DeleteEndpointRequest\x1a\x35.aruna.api.storage.services.v2.DeleteEndpointResponse\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v2/endpoint/{endpoint_id}\x12\xa7\x01\n\x12GetDefaultEndpoint\x12\x38.aruna.api.storage.services.v2.GetDefaultEndpointRequest\x1a\x39.aruna.api.storage.services.v2.GetDefaultEndpointResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v2/endpoint/defaultB\x94\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x0f\x45ndpointServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.endpoint_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\017EndpointServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_ENDPOINTSERVICE'].methods_by_name['CreateEndpoint']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['CreateEndpoint']._serialized_options = b'\202\323\344\223\002\021\"\014/v2/endpoint:\001*'
  _globals['_ENDPOINTSERVICE'].methods_by_name['FullSyncEndpoint']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['FullSyncEndpoint']._serialized_options = b'\202\323\344\223\002\023\022\021/v2/endpoint/sync'
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoint']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoint']._serialized_options = b'\202\323\344\223\002\016\022\014/v2/endpoint'
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoints']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoints']._serialized_options = b'\202\323\344\223\002\017\022\r/v2/endpoints'
  _globals['_ENDPOINTSERVICE'].methods_by_name['DeleteEndpoint']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['DeleteEndpoint']._serialized_options = b'\202\323\344\223\002\034*\032/v2/endpoint/{endpoint_id}'
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetDefaultEndpoint']._options = None
  _globals['_ENDPOINTSERVICE'].methods_by_name['GetDefaultEndpoint']._serialized_options = b'\202\323\344\223\002\026\022\024/v2/endpoint/default'
  _globals['_CREATEENDPOINTREQUEST']._serialized_start=160
  _globals['_CREATEENDPOINTREQUEST']._serialized_end=417
  _globals['_CREATEENDPOINTRESPONSE']._serialized_start=419
  _globals['_CREATEENDPOINTRESPONSE']._serialized_end=510
  _globals['_FULLSYNCENDPOINTREQUEST']._serialized_start=512
  _globals['_FULLSYNCENDPOINTREQUEST']._serialized_end=537
  _globals['_FULLSYNCENDPOINTRESPONSE']._serialized_start=540
  _globals['_FULLSYNCENDPOINTRESPONSE']._serialized_end=787
  _globals['_GETENDPOINTREQUEST']._serialized_start=789
  _globals['_GETENDPOINTREQUEST']._serialized_end=895
  _globals['_GETENDPOINTRESPONSE']._serialized_start=897
  _globals['_GETENDPOINTRESPONSE']._serialized_end=985
  _globals['_GETENDPOINTSREQUEST']._serialized_start=987
  _globals['_GETENDPOINTSREQUEST']._serialized_end=1008
  _globals['_GETENDPOINTSRESPONSE']._serialized_start=1010
  _globals['_GETENDPOINTSRESPONSE']._serialized_end=1101
  _globals['_DELETEENDPOINTREQUEST']._serialized_start=1103
  _globals['_DELETEENDPOINTREQUEST']._serialized_end=1159
  _globals['_DELETEENDPOINTRESPONSE']._serialized_start=1161
  _globals['_DELETEENDPOINTRESPONSE']._serialized_end=1185
  _globals['_GETDEFAULTENDPOINTREQUEST']._serialized_start=1187
  _globals['_GETDEFAULTENDPOINTREQUEST']._serialized_end=1214
  _globals['_GETDEFAULTENDPOINTRESPONSE']._serialized_start=1216
  _globals['_GETDEFAULTENDPOINTRESPONSE']._serialized_end=1311
  _globals['_ENDPOINTSERVICE']._serialized_start=1314
  _globals['_ENDPOINTSERVICE']._serialized_end=2267
# @@protoc_insertion_point(module_scope)
