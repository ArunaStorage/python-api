# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v1/endpoint_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v1 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4aruna/api/storage/services/v1/endpoint_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a(aruna/api/storage/models/v1/models.proto\x1a\x1cgoogle/api/annotations.proto\"\xa4\x02\n\x12\x41\x64\x64\x45ndpointRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x42\n\x07\x65p_type\x18\x02 \x01(\x0e\x32).aruna.api.storage.models.v1.EndpointTypeR\x06\x65pType\x12%\n\x0eproxy_hostname\x18\x03 \x01(\tR\rproxyHostname\x12+\n\x11internal_hostname\x18\x04 \x01(\tR\x10internalHostname\x12-\n\x12\x64ocumentation_path\x18\x05 \x01(\tR\x11\x64ocumentationPath\x12\x1b\n\tis_public\x18\x06 \x01(\x08R\x08isPublic\x12\x16\n\x06pubkey\x18\x07 \x01(\tR\x06pubkey\"}\n\x13\x41\x64\x64\x45ndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v1.EndpointR\x08\x65ndpoint\x12#\n\rpubkey_serial\x18\x02 \x01(\x03R\x0cpubkeySerial\"j\n\x12GetEndpointRequest\x12%\n\rendpoint_name\x18\x01 \x01(\tH\x00R\x0c\x65ndpointName\x12!\n\x0b\x65ndpoint_id\x18\x02 \x01(\tH\x00R\nendpointIdB\n\n\x08\x65ndpoint\"X\n\x13GetEndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v1.EndpointR\x08\x65ndpoint\"\x15\n\x13GetEndpointsRequest\"[\n\x14GetEndpointsResponse\x12\x43\n\tendpoints\x18\x01 \x03(\x0b\x32%.aruna.api.storage.models.v1.EndpointR\tendpoints\"8\n\x15\x44\x65leteEndpointRequest\x12\x1f\n\x0b\x65ndpoint_id\x18\x01 \x01(\tR\nendpointId\"\x18\n\x16\x44\x65leteEndpointResponse\"\x1b\n\x19GetDefaultEndpointRequest\"_\n\x1aGetDefaultEndpointResponse\x12\x41\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32%.aruna.api.storage.models.v1.EndpointR\x08\x65ndpoint2\x8d\x06\n\x0f\x45ndpointService\x12\x8d\x01\n\x0b\x41\x64\x64\x45ndpoint\x12\x31.aruna.api.storage.services.v1.AddEndpointRequest\x1a\x32.aruna.api.storage.services.v1.AddEndpointResponse\"\x17\x82\xd3\xe4\x93\x02\x11:\x01*\"\x0c/v1/endpoint\x12\x8a\x01\n\x0bGetEndpoint\x12\x31.aruna.api.storage.services.v1.GetEndpointRequest\x1a\x32.aruna.api.storage.services.v1.GetEndpointResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/endpoint\x12\x8e\x01\n\x0cGetEndpoints\x12\x32.aruna.api.storage.services.v1.GetEndpointsRequest\x1a\x33.aruna.api.storage.services.v1.GetEndpointsResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/endpoints\x12\xa1\x01\n\x0e\x44\x65leteEndpoint\x12\x34.aruna.api.storage.services.v1.DeleteEndpointRequest\x1a\x35.aruna.api.storage.services.v1.DeleteEndpointResponse\"\"\x82\xd3\xe4\x93\x02\x1c*\x1a/v1/endpoint/{endpoint_id}\x12\xa7\x01\n\x12GetDefaultEndpoint\x12\x38.aruna.api.storage.services.v1.GetDefaultEndpointRequest\x1a\x39.aruna.api.storage.services.v1.GetDefaultEndpointResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/endpoint/defaultB\x91\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0f\x45ndpointServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v1.endpoint_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\017EndpointServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1'
  _ENDPOINTSERVICE.methods_by_name['AddEndpoint']._options = None
  _ENDPOINTSERVICE.methods_by_name['AddEndpoint']._serialized_options = b'\202\323\344\223\002\021:\001*\"\014/v1/endpoint'
  _ENDPOINTSERVICE.methods_by_name['GetEndpoint']._options = None
  _ENDPOINTSERVICE.methods_by_name['GetEndpoint']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/endpoint'
  _ENDPOINTSERVICE.methods_by_name['GetEndpoints']._options = None
  _ENDPOINTSERVICE.methods_by_name['GetEndpoints']._serialized_options = b'\202\323\344\223\002\017\022\r/v1/endpoints'
  _ENDPOINTSERVICE.methods_by_name['DeleteEndpoint']._options = None
  _ENDPOINTSERVICE.methods_by_name['DeleteEndpoint']._serialized_options = b'\202\323\344\223\002\034*\032/v1/endpoint/{endpoint_id}'
  _ENDPOINTSERVICE.methods_by_name['GetDefaultEndpoint']._options = None
  _ENDPOINTSERVICE.methods_by_name['GetDefaultEndpoint']._serialized_options = b'\202\323\344\223\002\026\022\024/v1/endpoint/default'
  _ADDENDPOINTREQUEST._serialized_start=160
  _ADDENDPOINTREQUEST._serialized_end=452
  _ADDENDPOINTRESPONSE._serialized_start=454
  _ADDENDPOINTRESPONSE._serialized_end=579
  _GETENDPOINTREQUEST._serialized_start=581
  _GETENDPOINTREQUEST._serialized_end=687
  _GETENDPOINTRESPONSE._serialized_start=689
  _GETENDPOINTRESPONSE._serialized_end=777
  _GETENDPOINTSREQUEST._serialized_start=779
  _GETENDPOINTSREQUEST._serialized_end=800
  _GETENDPOINTSRESPONSE._serialized_start=802
  _GETENDPOINTSRESPONSE._serialized_end=893
  _DELETEENDPOINTREQUEST._serialized_start=895
  _DELETEENDPOINTREQUEST._serialized_end=951
  _DELETEENDPOINTRESPONSE._serialized_start=953
  _DELETEENDPOINTRESPONSE._serialized_end=977
  _GETDEFAULTENDPOINTREQUEST._serialized_start=979
  _GETDEFAULTENDPOINTREQUEST._serialized_end=1006
  _GETDEFAULTENDPOINTRESPONSE._serialized_start=1008
  _GETDEFAULTENDPOINTRESPONSE._serialized_end=1103
  _ENDPOINTSERVICE._serialized_start=1106
  _ENDPOINTSERVICE._serialized_end=1887
# @@protoc_insertion_point(module_scope)
