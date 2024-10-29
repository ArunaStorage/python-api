# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aruna/api/notification/services/v2/notification_service.proto
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
    'aruna/api/notification/services/v2/notification_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=aruna/api/notification/services/v2/notification_service.proto\x12\"aruna.api.notification.services.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1bgoogle/api/visibility.proto\"\xd6\x01\n\x08Resource\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x34\n\x16persistent_resource_id\x18\x02 \x01(\x08R\x14persistentResourceId\x12\x1a\n\x08\x63hecksum\x18\x03 \x01(\tR\x08\x63hecksum\x12W\n\x10resource_variant\x18\x04 \x01(\x0e\x32,.aruna.api.storage.models.v2.ResourceVariantR\x0fresourceVariant\"\x8a\x01\n\x0eResourceTarget\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12W\n\x10resource_variant\x18\x02 \x01(\x0e\x32,.aruna.api.storage.models.v2.ResourceVariantR\x0fresourceVariant\"\xa9\x04\n\x1b\x43reateStreamConsumerRequest\x12P\n\x08resource\x18\x01 \x01(\x0b\x32\x32.aruna.api.notification.services.v2.ResourceTargetH\x00R\x08resource\x12\x14\n\x04user\x18\x02 \x01(\tH\x00R\x04user\x12&\n\rannouncements\x18\x03 \x01(\x08H\x00R\rannouncements\x12\x12\n\x03\x61ll\x18\x04 \x01(\x08H\x00R\x03\x61ll\x12\x31\n\x14include_subresources\x18\x05 \x01(\x08R\x13includeSubresources\x12N\n\nstream_all\x18\x06 \x01(\x0b\x32-.aruna.api.notification.services.v2.StreamAllH\x01R\tstreamAll\x12^\n\x10stream_from_date\x18\x07 \x01(\x0b\x32\x32.aruna.api.notification.services.v2.StreamFromDateH\x01R\x0estreamFromDate\x12j\n\x14stream_from_sequence\x18\x08 \x01(\x0b\x32\x36.aruna.api.notification.services.v2.StreamFromSequenceH\x01R\x12streamFromSequenceB\x08\n\x06targetB\r\n\x0bstream_type\"G\n\x1c\x43reateStreamConsumerResponse\x12\'\n\x0fstream_consumer\x18\x01 \x01(\tR\x0estreamConsumer\"e\n\x1bGetEventMessageBatchRequest\x12\'\n\x0fstream_consumer\x18\x01 \x01(\tR\x0estreamConsumer\x12\x1d\n\nbatch_size\x18\x02 \x01(\rR\tbatchSize\"l\n\x1cGetEventMessageBatchResponse\x12L\n\x08messages\x18\x01 \x03(\x0b\x32\x30.aruna.api.notification.services.v2.EventMessageR\x08messages\"G\n\x1cGetEventMessageStreamRequest\x12\'\n\x0fstream_consumer\x18\x01 \x01(\tR\x0estreamConsumer\"k\n\x1dGetEventMessageStreamResponse\x12J\n\x07message\x18\x01 \x01(\x0b\x32\x30.aruna.api.notification.services.v2.EventMessageR\x07message\"e\n\x1e\x41\x63knowledgeMessageBatchRequest\x12\x43\n\x07replies\x18\x01 \x03(\x0b\x32).aruna.api.notification.services.v2.ReplyR\x07replies\"!\n\x1f\x41\x63knowledgeMessageBatchResponse\"F\n\x1b\x44\x65leteStreamConsumerRequest\x12\'\n\x0fstream_consumer\x18\x01 \x01(\tR\x0estreamConsumer\"\x1e\n\x1c\x44\x65leteStreamConsumerResponse\"0\n\x12StreamFromSequence\x12\x1a\n\x08sequence\x18\x01 \x01(\x04R\x08sequence\"J\n\x0eStreamFromDate\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"\x0b\n\tStreamAll\"\xb5\x02\n\x0c\x45ventMessage\x12Z\n\x0eresource_event\x18\x01 \x01(\x0b\x32\x31.aruna.api.notification.services.v2.ResourceEventH\x00R\rresourceEvent\x12N\n\nuser_event\x18\x02 \x01(\x0b\x32-.aruna.api.notification.services.v2.UserEventH\x00R\tuserEvent\x12\x66\n\x12\x61nnouncement_event\x18\x03 \x01(\x0b\x32\x35.aruna.api.notification.services.v2.AnnouncementEventH\x00R\x11\x61nnouncementEventB\x11\n\x0fmessage_variant\"\xf1\x01\n\rResourceEvent\x12H\n\x08resource\x18\x01 \x01(\x0b\x32,.aruna.api.notification.services.v2.ResourceR\x08resource\x12U\n\revent_variant\x18\x02 \x01(\x0e\x32\x30.aruna.api.notification.services.v2.EventVariantR\x0c\x65ventVariant\x12?\n\x05reply\x18\x03 \x01(\x0b\x32).aruna.api.notification.services.v2.ReplyR\x05reply\"\xd8\x01\n\tUserEvent\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12U\n\revent_variant\x18\x02 \x01(\x0e\x32\x30.aruna.api.notification.services.v2.EventVariantR\x0c\x65ventVariant\x12\x1a\n\x08\x63hecksum\x18\x03 \x01(\tR\x08\x63hecksum\x12?\n\x05reply\x18\x04 \x01(\x0b\x32).aruna.api.notification.services.v2.ReplyR\x05reply\"E\n\x05Reply\x12\x14\n\x05reply\x18\x01 \x01(\tR\x05reply\x12\x12\n\x04salt\x18\x02 \x01(\tR\x04salt\x12\x12\n\x04hmac\x18\x03 \x01(\tR\x04hmac\"\xa9\x01\n\x11ScheduledDowntime\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x1c\n\tcomponent\x18\x02 \x01(\tR\tcomponent\x12.\n\x04\x66rom\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x04\x66rom\x12*\n\x02to\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02to\"g\n\nNewVersion\x12\x1a\n\x08location\x18\x01 \x01(\tR\x08location\x12\x1c\n\tcomponent\x18\x02 \x01(\tR\tcomponent\x12\x1f\n\x0bnew_version\x18\x03 \x01(\tR\nnewVersion\"#\n\tNewPubkey\x12\x16\n\x06pubkey\x18\x01 \x01(\tR\x06pubkey\"\xe1\x03\n\x11\x41nnouncementEvent\x12+\n\x11new_data_proxy_id\x18\x01 \x01(\tH\x00R\x0enewDataProxyId\x12\x31\n\x14remove_data_proxy_id\x18\x02 \x01(\tH\x00R\x11removeDataProxyId\x12\x31\n\x14update_data_proxy_id\x18\x03 \x01(\tH\x00R\x11updateDataProxyId\x12\x1f\n\nnew_pubkey\x18\x04 \x01(\x05H\x00R\tnewPubkey\x12%\n\rremove_pubkey\x18\x05 \x01(\x05H\x00R\x0cremovePubkey\x12S\n\x08\x64owntime\x18\x06 \x01(\x0b\x32\x35.aruna.api.notification.services.v2.ScheduledDowntimeH\x00R\x08\x64owntime\x12J\n\x07version\x18\x07 \x01(\x0b\x32..aruna.api.notification.services.v2.NewVersionH\x00R\x07version\x12?\n\x05reply\x18\x08 \x01(\x0b\x32).aruna.api.notification.services.v2.ReplyR\x05replyB\x0f\n\revent_variant*\xba\x01\n\x0c\x45ventVariant\x12\x1d\n\x19\x45VENT_VARIANT_UNSPECIFIED\x10\x00\x12\x19\n\x15\x45VENT_VARIANT_CREATED\x10\x01\x12\x1b\n\x17\x45VENT_VARIANT_AVAILABLE\x10\x02\x12\x19\n\x15\x45VENT_VARIANT_UPDATED\x10\x03\x12\x19\n\x15\x45VENT_VARIANT_DELETED\x10\x04\x12\x1d\n\x19\x45VENT_VARIANT_SNAPSHOTTED\x10\x05\x32\xaa\x08\n\x18\x45ventNotificationService\x12\xc1\x01\n\x14\x43reateStreamConsumer\x12?.aruna.api.notification.services.v2.CreateStreamConsumerRequest\x1a@.aruna.api.notification.services.v2.CreateStreamConsumerResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v2/notifications/consumers:\x01*\x12\xcc\x01\n\x14GetEventMessageBatch\x12?.aruna.api.notification.services.v2.GetEventMessageBatchRequest\x1a@.aruna.api.notification.services.v2.GetEventMessageBatchResponse\"1\x82\xd3\xe4\x93\x02+\x12)/v2/notifications/{stream_consumer}/batch\x12\xd2\x01\n\x15GetEventMessageStream\x12@.aruna.api.notification.services.v2.GetEventMessageStreamRequest\x1a\x41.aruna.api.notification.services.v2.GetEventMessageStreamResponse\"2\x82\xd3\xe4\x93\x02,\x12*/v2/notifications/{stream_consumer}/stream0\x01\x12\xcc\x01\n\x17\x41\x63knowledgeMessageBatch\x12\x42.aruna.api.notification.services.v2.AcknowledgeMessageBatchRequest\x1a\x43.aruna.api.notification.services.v2.AcknowledgeMessageBatchResponse\"(\x82\xd3\xe4\x93\x02\"2\x1d/v2/notifications/acknowledge:\x01*\x12\xc6\x01\n\x14\x44\x65leteStreamConsumer\x12?.aruna.api.notification.services.v2.DeleteStreamConsumerRequest\x1a@.aruna.api.notification.services.v2.DeleteStreamConsumerResponse\"+\x82\xd3\xe4\x93\x02%*#/v2/notifications/{stream_consumer}\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\xa9\x01\nCcom.github.ArunaStorage.java_api.aruna.api.notification.services.v2B\x1aUpdateNotificationServicesP\x01ZDgithub.com/ArunaStorage/go-api/v2/aruna/api/notification/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.notification.services.v2.notification_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\nCcom.github.ArunaStorage.java_api.aruna.api.notification.services.v2B\032UpdateNotificationServicesP\001ZDgithub.com/ArunaStorage/go-api/v2/aruna/api/notification/services/v2'
  _globals['_EVENTNOTIFICATIONSERVICE']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['CreateStreamConsumer']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['CreateStreamConsumer']._serialized_options = b'\202\323\344\223\002 \"\033/v2/notifications/consumers:\001*'
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['GetEventMessageBatch']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['GetEventMessageBatch']._serialized_options = b'\202\323\344\223\002+\022)/v2/notifications/{stream_consumer}/batch'
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['GetEventMessageStream']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['GetEventMessageStream']._serialized_options = b'\202\323\344\223\002,\022*/v2/notifications/{stream_consumer}/stream'
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['AcknowledgeMessageBatch']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['AcknowledgeMessageBatch']._serialized_options = b'\202\323\344\223\002\"2\035/v2/notifications/acknowledge:\001*'
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['DeleteStreamConsumer']._loaded_options = None
  _globals['_EVENTNOTIFICATIONSERVICE'].methods_by_name['DeleteStreamConsumer']._serialized_options = b'\202\323\344\223\002%*#/v2/notifications/{stream_consumer}'
  _globals['_EVENTVARIANT']._serialized_start=3643
  _globals['_EVENTVARIANT']._serialized_end=3829
  _globals['_RESOURCE']._serialized_start=236
  _globals['_RESOURCE']._serialized_end=450
  _globals['_RESOURCETARGET']._serialized_start=453
  _globals['_RESOURCETARGET']._serialized_end=591
  _globals['_CREATESTREAMCONSUMERREQUEST']._serialized_start=594
  _globals['_CREATESTREAMCONSUMERREQUEST']._serialized_end=1147
  _globals['_CREATESTREAMCONSUMERRESPONSE']._serialized_start=1149
  _globals['_CREATESTREAMCONSUMERRESPONSE']._serialized_end=1220
  _globals['_GETEVENTMESSAGEBATCHREQUEST']._serialized_start=1222
  _globals['_GETEVENTMESSAGEBATCHREQUEST']._serialized_end=1323
  _globals['_GETEVENTMESSAGEBATCHRESPONSE']._serialized_start=1325
  _globals['_GETEVENTMESSAGEBATCHRESPONSE']._serialized_end=1433
  _globals['_GETEVENTMESSAGESTREAMREQUEST']._serialized_start=1435
  _globals['_GETEVENTMESSAGESTREAMREQUEST']._serialized_end=1506
  _globals['_GETEVENTMESSAGESTREAMRESPONSE']._serialized_start=1508
  _globals['_GETEVENTMESSAGESTREAMRESPONSE']._serialized_end=1615
  _globals['_ACKNOWLEDGEMESSAGEBATCHREQUEST']._serialized_start=1617
  _globals['_ACKNOWLEDGEMESSAGEBATCHREQUEST']._serialized_end=1718
  _globals['_ACKNOWLEDGEMESSAGEBATCHRESPONSE']._serialized_start=1720
  _globals['_ACKNOWLEDGEMESSAGEBATCHRESPONSE']._serialized_end=1753
  _globals['_DELETESTREAMCONSUMERREQUEST']._serialized_start=1755
  _globals['_DELETESTREAMCONSUMERREQUEST']._serialized_end=1825
  _globals['_DELETESTREAMCONSUMERRESPONSE']._serialized_start=1827
  _globals['_DELETESTREAMCONSUMERRESPONSE']._serialized_end=1857
  _globals['_STREAMFROMSEQUENCE']._serialized_start=1859
  _globals['_STREAMFROMSEQUENCE']._serialized_end=1907
  _globals['_STREAMFROMDATE']._serialized_start=1909
  _globals['_STREAMFROMDATE']._serialized_end=1983
  _globals['_STREAMALL']._serialized_start=1985
  _globals['_STREAMALL']._serialized_end=1996
  _globals['_EVENTMESSAGE']._serialized_start=1999
  _globals['_EVENTMESSAGE']._serialized_end=2308
  _globals['_RESOURCEEVENT']._serialized_start=2311
  _globals['_RESOURCEEVENT']._serialized_end=2552
  _globals['_USEREVENT']._serialized_start=2555
  _globals['_USEREVENT']._serialized_end=2771
  _globals['_REPLY']._serialized_start=2773
  _globals['_REPLY']._serialized_end=2842
  _globals['_SCHEDULEDDOWNTIME']._serialized_start=2845
  _globals['_SCHEDULEDDOWNTIME']._serialized_end=3014
  _globals['_NEWVERSION']._serialized_start=3016
  _globals['_NEWVERSION']._serialized_end=3119
  _globals['_NEWPUBKEY']._serialized_start=3121
  _globals['_NEWPUBKEY']._serialized_end=3156
  _globals['_ANNOUNCEMENTEVENT']._serialized_start=3159
  _globals['_ANNOUNCEMENTEVENT']._serialized_end=3640
  _globals['_EVENTNOTIFICATIONSERVICE']._serialized_start=3832
  _globals['_EVENTNOTIFICATIONSERVICE']._serialized_end=4898
# @@protoc_insertion_point(module_scope)
