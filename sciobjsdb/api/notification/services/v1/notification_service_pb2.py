# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/notification/services/v1/notification_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from sciobjsdb.api.notification.services.v1 import notification_service_models_pb2 as sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAsciobjsdb/api/notification/services/v1/notification_service.proto\x12&sciobjsdb.api.notification.services.v1\x1a\x1cgoogle/api/annotations.proto\x1aHsciobjsdb/api/notification/services/v1/notification_service_models.proto2\xe7\x03\n\x19UpdateNotificationService\x12\xe5\x01\n\x19\x43reateEventStreamingGroup\x12H.sciobjsdb.api.notification.services.v1.CreateEventStreamingGroupRequest\x1aI.sciobjsdb.api.notification.services.v1.CreateEventStreamingGroupResponse\"3\x82\xd3\xe4\x93\x02-:\x01*\"(/api/v1/eventstream/createstreaminggroup\x12\xe1\x01\n\x17NotificationStreamGroup\x12\x46.sciobjsdb.api.notification.services.v1.NotificationStreamGroupRequest\x1aG.sciobjsdb.api.notification.services.v1.NotificationStreamGroupResponse\"1\x82\xd3\xe4\x93\x02+:\x01*\"&/api/v1/eventstreamgroup/notifications(\x01\x30\x01\x42\xac\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x1aUpdateNotificationServicesP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')



_UPDATENOTIFICATIONSERVICE = DESCRIPTOR.services_by_name['UpdateNotificationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\032UpdateNotificationServicesP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _UPDATENOTIFICATIONSERVICE.methods_by_name['CreateEventStreamingGroup']._options = None
  _UPDATENOTIFICATIONSERVICE.methods_by_name['CreateEventStreamingGroup']._serialized_options = b'\202\323\344\223\002-:\001*\"(/api/v1/eventstream/createstreaminggroup'
  _UPDATENOTIFICATIONSERVICE.methods_by_name['NotificationStreamGroup']._options = None
  _UPDATENOTIFICATIONSERVICE.methods_by_name['NotificationStreamGroup']._serialized_options = b'\202\323\344\223\002+:\001*\"&/api/v1/eventstreamgroup/notifications'
  _UPDATENOTIFICATIONSERVICE._serialized_start=214
  _UPDATENOTIFICATIONSERVICE._serialized_end=701
# @@protoc_insertion_point(module_scope)