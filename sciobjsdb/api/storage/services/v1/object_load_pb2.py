# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/services/v1/object_load.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sciobjsdb.api.storage.services.v1 import object_load_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3sciobjsdb/api/storage/services/v1/object_load.proto\x12!sciobjsdb.api.storage.services.v1\x1a:sciobjsdb/api/storage/services/v1/object_load_models.proto\x1a\x1cgoogle/api/annotations.proto2\xc0\x0b\n\x11ObjectLoadService\x12\xb3\x01\n\x10\x43reateUploadLink\x12:.sciobjsdb.api.storage.services.v1.CreateUploadLinkRequest\x1a;.sciobjsdb.api.storage.services.v1.CreateUploadLinkResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/api/v1/objectload/upload/{id}\x12\xbb\x01\n\x12\x43reateDownloadLink\x12<.sciobjsdb.api.storage.services.v1.CreateDownloadLinkRequest\x1a=.sciobjsdb.api.storage.services.v1.CreateDownloadLinkResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /api/v1/objectload/download/{id}\x12\xce\x01\n\x17\x43reateDownloadLinkBatch\x12\x41.sciobjsdb.api.storage.services.v1.CreateDownloadLinkBatchRequest\x1a\x42.sciobjsdb.api.storage.services.v1.CreateDownloadLinkBatchResponse\",\x82\xd3\xe4\x93\x02&:\x01*\"!/api/v1/objectload/download_batch\x12\xda\x01\n\x18\x43reateDownloadLinkStream\x12\x42.sciobjsdb.api.storage.services.v1.CreateDownloadLinkStreamRequest\x1a\x43.sciobjsdb.api.storage.services.v1.CreateDownloadLinkStreamResponse\"3\x82\xd3\xe4\x93\x02-:\x01*\"(/api/v1/objectload/download_batch_stream0\x01\x12\xc7\x01\n\x14StartMultipartUpload\x12>.sciobjsdb.api.storage.services.v1.StartMultipartUploadRequest\x1a?.sciobjsdb.api.storage.services.v1.StartMultipartUploadResponse\".\x82\xd3\xe4\x93\x02(\"&/api/v1/objectload/init_multipart/{id}\x12\xe9\x01\n\x16GetMultipartUploadLink\x12@.sciobjsdb.api.storage.services.v1.GetMultipartUploadLinkRequest\x1a\x41.sciobjsdb.api.storage.services.v1.GetMultipartUploadLinkResponse\"J\x82\xd3\xe4\x93\x02\x44\x12\x42/api/v1/objectload/upload_multipart_part/{object_id}/{upload_part}\x12\xd2\x01\n\x17\x43ompleteMultipartUpload\x12\x41.sciobjsdb.api.storage.services.v1.CompleteMultipartUploadRequest\x1a\x42.sciobjsdb.api.storage.services.v1.CompleteMultipartUploadResponse\"0\x82\xd3\xe4\x93\x02*:\x01*\"%/api/v1/objectload/complete_multipartB\xa4\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x12ObjectLoadServicesP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.services.v1.object_load_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\022ObjectLoadServicesP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _OBJECTLOADSERVICE.methods_by_name['CreateUploadLink']._options = None
  _OBJECTLOADSERVICE.methods_by_name['CreateUploadLink']._serialized_options = b'\202\323\344\223\002 \022\036/api/v1/objectload/upload/{id}'
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLink']._options = None
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLink']._serialized_options = b'\202\323\344\223\002\"\022 /api/v1/objectload/download/{id}'
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLinkBatch']._options = None
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLinkBatch']._serialized_options = b'\202\323\344\223\002&:\001*\"!/api/v1/objectload/download_batch'
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLinkStream']._options = None
  _OBJECTLOADSERVICE.methods_by_name['CreateDownloadLinkStream']._serialized_options = b'\202\323\344\223\002-:\001*\"(/api/v1/objectload/download_batch_stream'
  _OBJECTLOADSERVICE.methods_by_name['StartMultipartUpload']._options = None
  _OBJECTLOADSERVICE.methods_by_name['StartMultipartUpload']._serialized_options = b'\202\323\344\223\002(\"&/api/v1/objectload/init_multipart/{id}'
  _OBJECTLOADSERVICE.methods_by_name['GetMultipartUploadLink']._options = None
  _OBJECTLOADSERVICE.methods_by_name['GetMultipartUploadLink']._serialized_options = b'\202\323\344\223\002D\022B/api/v1/objectload/upload_multipart_part/{object_id}/{upload_part}'
  _OBJECTLOADSERVICE.methods_by_name['CompleteMultipartUpload']._options = None
  _OBJECTLOADSERVICE.methods_by_name['CompleteMultipartUpload']._serialized_options = b'\202\323\344\223\002*:\001*\"%/api/v1/objectload/complete_multipart'
  _OBJECTLOADSERVICE._serialized_start=181
  _OBJECTLOADSERVICE._serialized_end=1653
# @@protoc_insertion_point(module_scope)
