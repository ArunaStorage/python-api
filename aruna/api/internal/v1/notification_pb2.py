# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/internal/v1/notification.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from aruna.api.storage.models.v1 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_models__pb2
from aruna.api.notification.services.v1 import notification_service_pb2 as aruna_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(aruna/api/internal/v1/notification.proto\x12\x15\x61runa.api.internal.v1\x1a\x1bgoogle/api/visibility.proto\x1a(aruna/api/storage/models/v1/models.proto\x1a=aruna/api/notification/services/v1/notification_service.proto\"\xbd\x01\n\tRelations\x12#\n\rshared_object\x18\x01 \x01(\tR\x0csharedObject\x12!\n\x0cobject_group\x18\x02 \x01(\tR\x0bobjectGroup\x12.\n\x13shared_object_group\x18\x03 \x01(\tR\x11sharedObjectGroup\x12\x1e\n\ncollection\x18\x04 \x01(\tR\ncollection\x12\x18\n\x07project\x18\x05 \x01(\tR\x07project\"\x93\x02\n\x10\x45mitEventRequest\x12P\n\x0e\x65vent_resource\x18\x01 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\reventResource\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12L\n\nevent_type\x18\x03 \x01(\x0e\x32-.aruna.api.notification.services.v1.EventTypeR\teventType\x12>\n\trelations\x18\x04 \x01(\x0b\x32 .aruna.api.internal.v1.RelationsR\trelations\"\x13\n\x11\x45mitEventResponse\"\x91\x02\n\x0bStreamGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12L\n\nevent_type\x18\x02 \x01(\x0e\x32-.aruna.api.notification.services.v1.EventTypeR\teventType\x12N\n\rresource_type\x18\x03 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\x12\x33\n\x16notify_on_sub_resource\x18\x05 \x01(\x08R\x13notifyOnSubResource\"\xa4\x02\n\x18\x43reateStreamGroupRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12L\n\nevent_type\x18\x02 \x01(\x0e\x32-.aruna.api.notification.services.v1.EventTypeR\teventType\x12N\n\rresource_type\x18\x03 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\x12\x33\n\x16notify_on_sub_resource\x18\x05 \x01(\x08R\x13notifyOnSubResource\"b\n\x19\x43reateStreamGroupResponse\x12\x45\n\x0cstream_group\x18\x01 \x01(\x0b\x32\".aruna.api.internal.v1.StreamGroupR\x0bstreamGroup\"U\n\x15GetStreamGroupRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12&\n\x0fstream_group_id\x18\x02 \x01(\tR\rstreamGroupId\"_\n\x16GetStreamGroupResponse\x12\x45\n\x0cstream_group\x18\x01 \x01(\x0b\x32\".aruna.api.internal.v1.StreamGroupR\x0bstreamGroup\"X\n\x18\x44\x65leteStreamGroupRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\x12&\n\x0fstream_group_id\x18\x02 \x01(\tR\rstreamGroupId\"\x1b\n\x19\x44\x65leteStreamGroupResponse\"\x8b\x01\n\x18GetSharedRevisionRequest\x12N\n\rresource_type\x18\x01 \x01(\x0e\x32).aruna.api.storage.models.v1.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"I\n\x19GetSharedRevisionResponse\x12,\n\x12shared_revision_id\x18\x01 \x01(\tR\x10sharedRevisionId2\x91\x01\n\x1bInternalEventEmitterService\x12`\n\tEmitEvent\x12\'.aruna.api.internal.v1.EmitEventRequest\x1a(.aruna.api.internal.v1.EmitEventResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL2\x87\x04\n\x14InternalEventService\x12x\n\x11\x43reateStreamGroup\x12/.aruna.api.internal.v1.CreateStreamGroupRequest\x1a\x30.aruna.api.internal.v1.CreateStreamGroupResponse\"\x00\x12o\n\x0eGetStreamGroup\x12,.aruna.api.internal.v1.GetStreamGroupRequest\x1a-.aruna.api.internal.v1.GetStreamGroupResponse\"\x00\x12x\n\x11\x44\x65leteStreamGroup\x12/.aruna.api.internal.v1.DeleteStreamGroupRequest\x1a\x30.aruna.api.internal.v1.DeleteStreamGroupResponse\"\x00\x12x\n\x11GetSharedRevision\x12/.aruna.api.internal.v1.GetSharedRevisionRequest\x1a\x30.aruna.api.internal.v1.GetSharedRevisionResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB6Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.internal.v1.notification_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1'
  _INTERNALEVENTEMITTERSERVICE._options = None
  _INTERNALEVENTEMITTERSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _INTERNALEVENTSERVICE._options = None
  _INTERNALEVENTSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _RELATIONS._serialized_start=202
  _RELATIONS._serialized_end=391
  _EMITEVENTREQUEST._serialized_start=394
  _EMITEVENTREQUEST._serialized_end=669
  _EMITEVENTRESPONSE._serialized_start=671
  _EMITEVENTRESPONSE._serialized_end=690
  _STREAMGROUP._serialized_start=693
  _STREAMGROUP._serialized_end=966
  _CREATESTREAMGROUPREQUEST._serialized_start=969
  _CREATESTREAMGROUPREQUEST._serialized_end=1261
  _CREATESTREAMGROUPRESPONSE._serialized_start=1263
  _CREATESTREAMGROUPRESPONSE._serialized_end=1361
  _GETSTREAMGROUPREQUEST._serialized_start=1363
  _GETSTREAMGROUPREQUEST._serialized_end=1448
  _GETSTREAMGROUPRESPONSE._serialized_start=1450
  _GETSTREAMGROUPRESPONSE._serialized_end=1545
  _DELETESTREAMGROUPREQUEST._serialized_start=1547
  _DELETESTREAMGROUPREQUEST._serialized_end=1635
  _DELETESTREAMGROUPRESPONSE._serialized_start=1637
  _DELETESTREAMGROUPRESPONSE._serialized_end=1664
  _GETSHAREDREVISIONREQUEST._serialized_start=1667
  _GETSHAREDREVISIONREQUEST._serialized_end=1806
  _GETSHAREDREVISIONRESPONSE._serialized_start=1808
  _GETSHAREDREVISIONRESPONSE._serialized_end=1881
  _INTERNALEVENTEMITTERSERVICE._serialized_start=1884
  _INTERNALEVENTEMITTERSERVICE._serialized_end=2029
  _INTERNALEVENTSERVICE._serialized_start=2032
  _INTERNALEVENTSERVICE._serialized_end=2551
# @@protoc_insertion_point(module_scope)