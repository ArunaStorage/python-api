# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/bundler/services/v1/bundler_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/bundler/services/v1/bundler_service.proto\x12\x1d\x61runa.api.bundler.services.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\xa0\x02\n\x13\x43reateBundleRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x1d\n\nobject_ids\x18\x02 \x03(\tR\tobjectIds\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\x12M\n\x0c\x61rchive_type\x18\x04 \x01(\x0e\x32*.aruna.api.bundler.services.v1.ArchiveTypeR\x0b\x61rchiveType\x12\x39\n\nexpires_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\x12\x1f\n\x0b\x65ndpoint_id\x18\x06 \x01(\tR\nendpointId\"E\n\x14\x43reateBundleResponse\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"W\n\x13\x44\x65leteBundleRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x1b\n\tbundle_id\x18\x02 \x01(\tR\x08\x62undleId\"\x16\n\x14\x44\x65leteBundleResponse*t\n\x0b\x41rchiveType\x12\x1c\n\x18\x41RCHIVE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x41RCHIVE_TYPE_TAR_GZ\x10\x01\x12\x14\n\x10\x41RCHIVE_TYPE_ZIP\x10\x02\x12\x18\n\x14\x41RCHIVE_TYPE_TAR_ZST\x10\x03\x32\xf4\x02\n\x0e\x42undlerService\x12\xa9\x01\n\x0c\x43reateBundle\x12\x32.aruna.api.bundler.services.v1.CreateBundleRequest\x1a\x33.aruna.api.bundler.services.v1.CreateBundleResponse\"0\x82\xd3\xe4\x93\x02*:\x01*\"%/v1/collection/{collection_id}/bundle\x12\xb5\x01\n\x0c\x44\x65leteBundle\x12\x32.aruna.api.bundler.services.v1.DeleteBundleRequest\x1a\x33.aruna.api.bundler.services.v1.DeleteBundleResponse\"<\x82\xd3\xe4\x93\x02\x36:\x01**1/v1/collection/{collection_id}/bundle/{bundle_id}B\x90\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0e\x42undlerServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.bundler.services.v1.bundler_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\016BundlerServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1'
  _BUNDLERSERVICE.methods_by_name['CreateBundle']._options = None
  _BUNDLERSERVICE.methods_by_name['CreateBundle']._serialized_options = b'\202\323\344\223\002*:\001*\"%/v1/collection/{collection_id}/bundle'
  _BUNDLERSERVICE.methods_by_name['DeleteBundle']._options = None
  _BUNDLERSERVICE.methods_by_name['DeleteBundle']._serialized_options = b'\202\323\344\223\0026:\001**1/v1/collection/{collection_id}/bundle/{bundle_id}'
  _ARCHIVETYPE._serialized_start=624
  _ARCHIVETYPE._serialized_end=740
  _CREATEBUNDLEREQUEST._serialized_start=150
  _CREATEBUNDLEREQUEST._serialized_end=438
  _CREATEBUNDLERESPONSE._serialized_start=440
  _CREATEBUNDLERESPONSE._serialized_end=509
  _DELETEBUNDLEREQUEST._serialized_start=511
  _DELETEBUNDLEREQUEST._serialized_end=598
  _DELETEBUNDLERESPONSE._serialized_start=600
  _DELETEBUNDLERESPONSE._serialized_end=622
  _BUNDLERSERVICE._serialized_start=743
  _BUNDLERSERVICE._serialized_end=1115
# @@protoc_insertion_point(module_scope)