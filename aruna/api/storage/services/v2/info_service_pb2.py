# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/info_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0aruna/api/storage/services/v2/info_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1a\n\x18GetStorageVersionRequest\"\x92\x01\n\x0fSemanticVersion\x12%\n\x0eversion_string\x18\x01 \x01(\tR\rversionString\x12\x14\n\x05major\x18\x02 \x01(\x05R\x05major\x12\x14\n\x05minor\x18\x03 \x01(\x05R\x05minor\x12\x14\n\x05patch\x18\x04 \x01(\x05R\x05patch\x12\x16\n\x06labels\x18\x05 \x01(\tR\x06labels\"x\n\x0fLocationVersion\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12I\n\x07version\x18\x02 \x03(\x0b\x32/.aruna.api.storage.services.v2.ComponentVersionR\x07version\"p\n\x10\x43omponentVersion\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12H\n\x07version\x18\x02 \x01(\x0b\x32..aruna.api.storage.services.v2.SemanticVersionR\x07version\"v\n\x19GetStorageVersionResponse\x12Y\n\x10location_version\x18\x01 \x03(\x0b\x32..aruna.api.storage.services.v2.LocationVersionR\x0flocationVersion\"\x19\n\x17GetStorageStatusRequest\"\x87\x01\n\x0eLocationStatus\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12Y\n\x10\x63omponent_status\x18\x02 \x03(\x0b\x32..aruna.api.storage.services.v2.ComponentStatusR\x0f\x63omponentStatus\"k\n\x0f\x43omponentStatus\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x44\n\x06status\x18\x02 \x01(\x0e\x32,.aruna.api.storage.models.v2.ComponentStatusR\x06status\"r\n\x18GetStorageStatusResponse\x12V\n\x0flocation_status\x18\x01 \x03(\x0b\x32-.aruna.api.storage.services.v2.LocationStatusR\x0elocationStatus\"\x13\n\x11GetPubkeysRequest\"S\n\x12GetPubkeysResponse\x12=\n\x07pubkeys\x18\x01 \x03(\x0b\x32#.aruna.api.storage.models.v2.PubkeyR\x07pubkeys\"r\n\x0b\x41nouncement\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07\x63ontent\x18\x02 \x01(\tR\x07\x63ontent\x12\x39\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\"\x18\n\x16GetAnouncementsRequest\"i\n\x17GetAnouncementsResponse\x12N\n\x0c\x61nouncements\x18\x01 \x03(\x0b\x32*.aruna.api.storage.services.v2.AnouncementR\x0c\x61nouncements\"\xa6\x01\n\x16SetAnouncementsRequest\x12[\n\x13\x61nouncements_upsert\x18\x01 \x03(\x0b\x32*.aruna.api.storage.services.v2.AnouncementR\x12\x61nouncementsUpsert\x12/\n\x13\x61nouncements_delete\x18\x02 \x03(\tR\x12\x61nouncementsDelete\"i\n\x17SetAnouncementsResponse\x12N\n\x0c\x61nouncements\x18\x01 \x03(\x0b\x32*.aruna.api.storage.services.v2.AnouncementR\x0c\x61nouncements2\xb1\x06\n\x14StorageStatusService\x12\xa0\x01\n\x11GetStorageVersion\x12\x37.aruna.api.storage.services.v2.GetStorageVersionRequest\x1a\x38.aruna.api.storage.services.v2.GetStorageVersionResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v2/info/version\x12\x9c\x01\n\x10GetStorageStatus\x12\x36.aruna.api.storage.services.v2.GetStorageStatusRequest\x1a\x37.aruna.api.storage.services.v2.GetStorageStatusResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v2/info/status\x12\x8b\x01\n\nGetPubkeys\x12\x30.aruna.api.storage.services.v2.GetPubkeysRequest\x1a\x31.aruna.api.storage.services.v2.GetPubkeysResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v2/info/pubkeys\x12\x9f\x01\n\x0fGetAnouncements\x12\x35.aruna.api.storage.services.v2.GetAnouncementsRequest\x1a\x36.aruna.api.storage.services.v2.GetAnouncementsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v2/info/anouncements\x12\xa6\x01\n\x0fSetAnouncements\x12\x35.aruna.api.storage.services.v2.SetAnouncementsRequest\x1a\x36.aruna.api.storage.services.v2.SetAnouncementsResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v2/info/anouncements/set:\x01*B\x96\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x14StorageStatusServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.info_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\024StorageStatusServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2'
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetStorageVersion']._options = None
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetStorageVersion']._serialized_options = b'\202\323\344\223\002\022\022\020/v2/info/version'
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetStorageStatus']._options = None
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetStorageStatus']._serialized_options = b'\202\323\344\223\002\021\022\017/v2/info/status'
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetPubkeys']._options = None
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetPubkeys']._serialized_options = b'\202\323\344\223\002\022\022\020/v2/info/pubkeys'
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetAnouncements']._options = None
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['GetAnouncements']._serialized_options = b'\202\323\344\223\002\027\022\025/v2/info/anouncements'
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['SetAnouncements']._options = None
  _globals['_STORAGESTATUSSERVICE'].methods_by_name['SetAnouncements']._serialized_options = b'\202\323\344\223\002\036\"\031/v2/info/anouncements/set:\001*'
  _globals['_GETSTORAGEVERSIONREQUEST']._serialized_start=188
  _globals['_GETSTORAGEVERSIONREQUEST']._serialized_end=214
  _globals['_SEMANTICVERSION']._serialized_start=217
  _globals['_SEMANTICVERSION']._serialized_end=363
  _globals['_LOCATIONVERSION']._serialized_start=365
  _globals['_LOCATIONVERSION']._serialized_end=485
  _globals['_COMPONENTVERSION']._serialized_start=487
  _globals['_COMPONENTVERSION']._serialized_end=599
  _globals['_GETSTORAGEVERSIONRESPONSE']._serialized_start=601
  _globals['_GETSTORAGEVERSIONRESPONSE']._serialized_end=719
  _globals['_GETSTORAGESTATUSREQUEST']._serialized_start=721
  _globals['_GETSTORAGESTATUSREQUEST']._serialized_end=746
  _globals['_LOCATIONSTATUS']._serialized_start=749
  _globals['_LOCATIONSTATUS']._serialized_end=884
  _globals['_COMPONENTSTATUS']._serialized_start=886
  _globals['_COMPONENTSTATUS']._serialized_end=993
  _globals['_GETSTORAGESTATUSRESPONSE']._serialized_start=995
  _globals['_GETSTORAGESTATUSRESPONSE']._serialized_end=1109
  _globals['_GETPUBKEYSREQUEST']._serialized_start=1111
  _globals['_GETPUBKEYSREQUEST']._serialized_end=1130
  _globals['_GETPUBKEYSRESPONSE']._serialized_start=1132
  _globals['_GETPUBKEYSRESPONSE']._serialized_end=1215
  _globals['_ANOUNCEMENT']._serialized_start=1217
  _globals['_ANOUNCEMENT']._serialized_end=1331
  _globals['_GETANOUNCEMENTSREQUEST']._serialized_start=1333
  _globals['_GETANOUNCEMENTSREQUEST']._serialized_end=1357
  _globals['_GETANOUNCEMENTSRESPONSE']._serialized_start=1359
  _globals['_GETANOUNCEMENTSRESPONSE']._serialized_end=1464
  _globals['_SETANOUNCEMENTSREQUEST']._serialized_start=1467
  _globals['_SETANOUNCEMENTSREQUEST']._serialized_end=1633
  _globals['_SETANOUNCEMENTSRESPONSE']._serialized_start=1635
  _globals['_SETANOUNCEMENTSRESPONSE']._serialized_end=1740
  _globals['_STORAGESTATUSSERVICE']._serialized_start=1743
  _globals['_STORAGESTATUSSERVICE']._serialized_end=2560
# @@protoc_insertion_point(module_scope)