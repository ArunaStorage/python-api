# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/dataproxy/services/v2/dataproxy_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7aruna/api/dataproxy/services/v2/dataproxy_service.proto\x12\x1f\x61runa.api.dataproxy.services.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\x1a(aruna/api/storage/models/v2/models.proto\"O\n\x0bInitMessage\x12!\n\x0c\x64\x61taproxy_id\x18\x01 \x01(\tR\x0b\x64\x61taproxyId\x12\x1d\n\nobject_ids\x18\x02 \x03(\tR\tobjectIds\"-\n\x0eInfoAckMessage\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\"K\n\x0f\x43hunkAckMessage\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1b\n\tchunk_idx\x18\x02 \x01(\x03R\x08\x63hunkIdx\"M\n\x11RetryChunkMessage\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1b\n\tchunk_idx\x18\x02 \x01(\x03R\x08\x63hunkIdx\"\x07\n\x05\x45mpty\"\xd8\x01\n\x0c\x45rrorMessage\x12U\n\x0bretry_chunk\x18\x01 \x01(\x0b\x32\x32.aruna.api.dataproxy.services.v2.RetryChunkMessageH\x00R\nretryChunk\x12>\n\x05\x61\x62ort\x18\x02 \x01(\x0b\x32&.aruna.api.dataproxy.services.v2.EmptyH\x00R\x05\x61\x62ort\x12(\n\x0fretry_object_id\x18\x03 \x01(\tH\x00R\rretryObjectIdB\x07\n\x05\x65rror\"\xda\x03\n\x16PullReplicationRequest\x12Q\n\x0cinit_message\x18\x01 \x01(\x0b\x32,.aruna.api.dataproxy.services.v2.InitMessageH\x00R\x0binitMessage\x12[\n\x10info_ack_message\x18\x02 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.InfoAckMessageH\x00R\x0einfoAckMessage\x12^\n\x11\x63hunk_ack_message\x18\x03 \x01(\x0b\x32\x30.aruna.api.dataproxy.services.v2.ChunkAckMessageH\x00R\x0f\x63hunkAckMessage\x12T\n\rerror_message\x18\x04 \x01(\x0b\x32-.aruna.api.dataproxy.services.v2.ErrorMessageH\x00R\x0c\x65rrorMessage\x12O\n\x0e\x66inish_message\x18\x05 \x01(\x0b\x32&.aruna.api.dataproxy.services.v2.EmptyH\x00R\rfinishMessageB\t\n\x07message\"\x0b\n\tHandshake\"#\n\x04Skip\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\"\xaa\x01\n\nObjectInfo\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x16\n\x06\x63hunks\x18\x02 \x01(\x03R\x06\x63hunks\x12\x19\n\x08raw_size\x18\x03 \x01(\x03R\x07rawSize\x12\'\n\x0f\x63ompressed_size\x18\x04 \x01(\x03R\x0e\x63ompressedSize\x12\x19\n\x05\x65xtra\x18\x05 \x01(\tH\x00R\x05\x65xtra\x88\x01\x01\x42\x08\n\x06_extra\"q\n\x05\x43hunk\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1b\n\tchunk_idx\x18\x02 \x01(\x03R\x08\x63hunkIdx\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta\x12\x1a\n\x08\x63hecksum\x18\x04 \x01(\tR\x08\x63hecksum\"\x8e\x03\n\x17PullReplicationResponse\x12J\n\thandshake\x18\x05 \x01(\x0b\x32*.aruna.api.dataproxy.services.v2.HandshakeH\x00R\thandshake\x12N\n\x0bobject_info\x18\x01 \x01(\x0b\x32+.aruna.api.dataproxy.services.v2.ObjectInfoH\x00R\nobjectInfo\x12>\n\x05\x63hunk\x18\x02 \x01(\x0b\x32&.aruna.api.dataproxy.services.v2.ChunkH\x00R\x05\x63hunk\x12O\n\x0e\x66inish_message\x18\x03 \x01(\x0b\x32&.aruna.api.dataproxy.services.v2.EmptyH\x00R\rfinishMessage\x12;\n\x04skip\x18\x04 \x01(\x0b\x32%.aruna.api.dataproxy.services.v2.SkipH\x00R\x04skipB\t\n\x07message\"\x96\x01\n\x08\x44\x61taInfo\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12!\n\x0c\x64ownload_url\x18\x02 \x01(\tR\x0b\x64ownloadUrl\x12%\n\x0e\x65ncryption_key\x18\x03 \x01(\tR\rencryptionKey\x12#\n\ris_compressed\x18\x04 \x01(\x08R\x0cisCompressed\"S\n\tDataInfos\x12\x46\n\tdata_info\x18\x01 \x03(\x0b\x32).aruna.api.dataproxy.services.v2.DataInfoR\x08\x64\x61taInfo\"c\n\x16PushReplicationRequest\x12I\n\ndata_infos\x18\x01 \x01(\x0b\x32*.aruna.api.dataproxy.services.v2.DataInfosR\tdataInfos\"+\n\x17PushReplicationResponse\x12\x10\n\x03\x61\x63k\x18\x01 \x01(\x08R\x03\x61\x63k\"\x17\n\x15GetCredentialsRequest\"V\n\x16GetCredentialsResponse\x12\x1d\n\naccess_key\x18\x01 \x01(\tR\taccessKey\x12\x1d\n\nsecret_key\x18\x02 \x01(\tR\tsecretKey\"\"\n CreateOrUpdateCredentialsRequest\"a\n!CreateOrUpdateCredentialsResponse\x12\x1d\n\naccess_key\x18\x01 \x01(\tR\taccessKey\x12\x1d\n\nsecret_key\x18\x02 \x01(\tR\tsecretKey\"\x1a\n\x18RevokeCredentialsRequest\"\x1b\n\x19RevokeCredentialsResponse\"2\n\x06S3Path\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\"\xb5\x01\n\x12PushReplicaRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tH\x00R\nresourceId\x12\x42\n\x07s3_path\x18\x02 \x01(\x0b\x32\'.aruna.api.dataproxy.services.v2.S3PathH\x00R\x06s3Path\x12,\n\x12target_endpoint_id\x18\x03 \x01(\tR\x10targetEndpointIdB\n\n\x08resource\"<\n\x13PushReplicaResponse\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"\x87\x01\n\x12PullReplicaRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tH\x00R\nresourceId\x12\x42\n\x07s3_path\x18\x02 \x01(\x0b\x32\'.aruna.api.dataproxy.services.v2.S3PathH\x00R\x06s3PathB\n\n\x08resource\"<\n\x13PullReplicaResponse\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"A\n\x18ReplicationStatusRequest\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"\x81\x01\n\x19ReplicationStatusResponse\x12J\n\x06status\x18\x01 \x01(\x0e\x32\x32.aruna.api.dataproxy.services.v2.ReplicationStatusR\x06status\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"~\n\x0eObjectLocation\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x1b\n\tupload_id\x18\x03 \x01(\tR\x08uploadId\x12%\n\x0e\x63ontent_length\x18\x04 \x01(\tR\rcontentLength\"s\n\x10PutObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\"\x13\n\x11PutObjectResponse\"_\n\x10GetObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"\'\n\x11GetObjectResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"`\n\x11HeadObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"S\n\x12HeadObjectResponse\x12%\n\x0e\x63ontent_length\x18\x01 \x01(\tR\rcontentLength\x12\x16\n\x06\x65xists\x18\x02 \x01(\x08R\x06\x65xists\"i\n\x1aInitMultiPartUploadRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\":\n\x1bInitMultiPartUploadResponse\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\"\x95\x01\n\x11UploadPartRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12\x1f\n\x0bpart_number\x18\x03 \x01(\x05R\npartNumber\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\x0cR\x04\x64\x61ta\"(\n\x12UploadPartResponse\x12\x12\n\x04\x65tag\x18\x01 \x01(\tR\x04\x65tag\"D\n\rCompletedPart\x12\x1f\n\x0bpart_number\x18\x01 \x01(\x05R\npartNumber\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"\xc6\x01\n\x1e\x43ompleteMultiPartUploadRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12W\n\x0f\x63ompleted_parts\x18\x02 \x03(\x0b\x32..aruna.api.dataproxy.services.v2.CompletedPartR\x0e\x63ompletedParts\"!\n\x1f\x43ompleteMultiPartUploadResponse\"-\n\x13\x43reateBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\"\x16\n\x14\x43reateBucketResponse\"-\n\x13\x44\x65leteBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\"\x16\n\x14\x44\x65leteBucketResponse\"b\n\x13\x44\x65leteObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"\x16\n\x14\x44\x65leteObjectResponse\"m\n\x13InitLocationRequest\x12\x1f\n\x0bobject_name\x18\x01 \x01(\tR\nobjectName\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size\x12!\n\x0cis_temporary\x18\x03 \x01(\x08R\x0bisTemporary\"c\n\x14InitLocationResponse\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"\x84\x04\n\x0eIngestResource\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x07\x61uthors\x18\x04 \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\x07\x61uthors\x12\x44\n\nkey_values\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\tkeyValues\x12\x43\n\trelations\x18\x06 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\trelations\x12\x45\n\ndata_class\x18\x07 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12\x39\n\x06hashes\x18\x08 \x03(\x0b\x32!.aruna.api.storage.models.v2.HashR\x06hashes\x12\x30\n\x14metadata_license_tag\x18\t \x01(\tR\x12metadataLicenseTag\x12(\n\x10\x64\x61ta_license_tag\x18\n \x01(\tR\x0e\x64\x61taLicenseTag\"\xbc\x03\n\x1bIngestExistingObjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12%\n\rcollection_id\x18\x02 \x01(\tH\x00R\x0c\x63ollectionId\x12\x62\n\x13\x63ollection_resource\x18\x03 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.IngestResourceH\x00R\x12\x63ollectionResource\x12\x1f\n\ndataset_id\x18\x04 \x01(\tH\x01R\tdatasetId\x12\\\n\x10\x64\x61taset_resource\x18\x05 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.IngestResourceH\x01R\x0f\x64\x61tasetResource\x12G\n\x06object\x18\x06 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.IngestResourceR\x06object\x12\x12\n\x04path\x18\x07 \x01(\tR\x04pathB\x0c\n\ncollectionB\t\n\x07\x64\x61taset\";\n\x1cIngestExistingObjectResponse\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId*\xb6\x01\n\x11ReplicationStatus\x12\"\n\x1eREPLICATION_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aREPLICATION_STATUS_PENDING\x10\x01\x12\x1e\n\x1aREPLICATION_STATUS_RUNNING\x10\x02\x12\x1f\n\x1bREPLICATION_STATUS_FINISHED\x10\x03\x12\x1c\n\x18REPLICATION_STATUS_ERROR\x10\x04\x32\xc2\x02\n\x1b\x44\x61taproxyReplicationService\x12\x8a\x01\n\x0fPullReplication\x12\x37.aruna.api.dataproxy.services.v2.PullReplicationRequest\x1a\x38.aruna.api.dataproxy.services.v2.PullReplicationResponse\"\x00(\x01\x30\x01\x12\x86\x01\n\x0fPushReplication\x12\x37.aruna.api.dataproxy.services.v2.PushReplicationRequest\x1a\x38.aruna.api.dataproxy.services.v2.PushReplicationResponse\"\x00\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXY2\xbe\n\n\x17\x44\x61taproxyBackendService\x12v\n\tPutObject\x12\x31.aruna.api.dataproxy.services.v2.PutObjectRequest\x1a\x32.aruna.api.dataproxy.services.v2.PutObjectResponse\"\x00(\x01\x12v\n\tGetObject\x12\x31.aruna.api.dataproxy.services.v2.GetObjectRequest\x1a\x32.aruna.api.dataproxy.services.v2.GetObjectResponse\"\x00\x30\x01\x12w\n\nHeadObject\x12\x32.aruna.api.dataproxy.services.v2.HeadObjectRequest\x1a\x33.aruna.api.dataproxy.services.v2.HeadObjectResponse\"\x00\x12\x92\x01\n\x13InitMultiPartUpload\x12;.aruna.api.dataproxy.services.v2.InitMultiPartUploadRequest\x1a<.aruna.api.dataproxy.services.v2.InitMultiPartUploadResponse\"\x00\x12y\n\nUploadPart\x12\x32.aruna.api.dataproxy.services.v2.UploadPartRequest\x1a\x33.aruna.api.dataproxy.services.v2.UploadPartResponse\"\x00(\x01\x12\x9e\x01\n\x17\x43ompleteMultiPartUpload\x12?.aruna.api.dataproxy.services.v2.CompleteMultiPartUploadRequest\x1a@.aruna.api.dataproxy.services.v2.CompleteMultiPartUploadResponse\"\x00\x12}\n\x0c\x43reateBucket\x12\x34.aruna.api.dataproxy.services.v2.CreateBucketRequest\x1a\x35.aruna.api.dataproxy.services.v2.CreateBucketResponse\"\x00\x12}\n\x0c\x44\x65leteBucket\x12\x34.aruna.api.dataproxy.services.v2.DeleteBucketRequest\x1a\x35.aruna.api.dataproxy.services.v2.DeleteBucketResponse\"\x00\x12}\n\x0c\x44\x65leteObject\x12\x34.aruna.api.dataproxy.services.v2.DeleteObjectRequest\x1a\x35.aruna.api.dataproxy.services.v2.DeleteObjectResponse\"\x00\x12}\n\x0cInitLocation\x12\x34.aruna.api.dataproxy.services.v2.InitLocationRequest\x1a\x35.aruna.api.dataproxy.services.v2.InitLocationResponse\"\x00\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXY2\x93\x08\n\x14\x44\x61taproxyUserService\x12\x9a\x01\n\x0eGetCredentials\x12\x36.aruna.api.dataproxy.services.v2.GetCredentialsRequest\x1a\x37.aruna.api.dataproxy.services.v2.GetCredentialsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v2/credentials\x12\xbe\x01\n\x19\x43reateOrUpdateCredentials\x12\x41.aruna.api.dataproxy.services.v2.CreateOrUpdateCredentialsRequest\x1a\x42.aruna.api.dataproxy.services.v2.CreateOrUpdateCredentialsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v2/credentials:\x01*\x12\xa3\x01\n\x11RevokeCredentials\x12\x39.aruna.api.dataproxy.services.v2.RevokeCredentialsRequest\x1a:.aruna.api.dataproxy.services.v2.RevokeCredentialsResponse\"\x17\x82\xd3\xe4\x93\x02\x11*\x0f/v2/credentials\x12\x95\x01\n\x0bPushReplica\x12\x33.aruna.api.dataproxy.services.v2.PushReplicaRequest\x1a\x34.aruna.api.dataproxy.services.v2.PushReplicaResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/replica/push:\x01*\x12\x95\x01\n\x0bPullReplica\x12\x33.aruna.api.dataproxy.services.v2.PullReplicaRequest\x1a\x34.aruna.api.dataproxy.services.v2.PullReplicaResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/replica/pull:\x01*\x12\xb7\x01\n\x11ReplicationStatus\x12\x39.aruna.api.dataproxy.services.v2.ReplicationStatusRequest\x1a:.aruna.api.dataproxy.services.v2.ReplicationStatusResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v2/replica/{replication_id}/status\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXY2\xc2\x01\n\x19\x44\x61taproxyIngestionService\x12\x95\x01\n\x14IngestExistingObject\x12<.aruna.api.dataproxy.services.v2.IngestExistingObjectRequest\x1a=.aruna.api.dataproxy.services.v2.IngestExistingObjectResponse\"\x00\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXYB\x96\x01\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\x10\x44\x61taProxyServiceP\x01Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.dataproxy.services.v2.dataproxy_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\020DataProxyServiceP\001Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2'
  _globals['_DATAPROXYREPLICATIONSERVICE']._loaded_options = None
  _globals['_DATAPROXYREPLICATIONSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYBACKENDSERVICE']._loaded_options = None
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYUSERSERVICE']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['GetCredentials']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['GetCredentials']._serialized_options = b'\202\323\344\223\002\021\022\017/v2/credentials'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['CreateOrUpdateCredentials']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['CreateOrUpdateCredentials']._serialized_options = b'\202\323\344\223\002\024\"\017/v2/credentials:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['RevokeCredentials']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['RevokeCredentials']._serialized_options = b'\202\323\344\223\002\021*\017/v2/credentials'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PushReplica']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PushReplica']._serialized_options = b'\202\323\344\223\002\025\"\020/v2/replica/push:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PullReplica']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PullReplica']._serialized_options = b'\202\323\344\223\002\025\"\020/v2/replica/pull:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['ReplicationStatus']._loaded_options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['ReplicationStatus']._serialized_options = b'\202\323\344\223\002%\022#/v2/replica/{replication_id}/status'
  _globals['_DATAPROXYINGESTIONSERVICE']._loaded_options = None
  _globals['_DATAPROXYINGESTIONSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_REPLICATIONSTATUS']._serialized_start=6067
  _globals['_REPLICATIONSTATUS']._serialized_end=6249
  _globals['_INITMESSAGE']._serialized_start=193
  _globals['_INITMESSAGE']._serialized_end=272
  _globals['_INFOACKMESSAGE']._serialized_start=274
  _globals['_INFOACKMESSAGE']._serialized_end=319
  _globals['_CHUNKACKMESSAGE']._serialized_start=321
  _globals['_CHUNKACKMESSAGE']._serialized_end=396
  _globals['_RETRYCHUNKMESSAGE']._serialized_start=398
  _globals['_RETRYCHUNKMESSAGE']._serialized_end=475
  _globals['_EMPTY']._serialized_start=477
  _globals['_EMPTY']._serialized_end=484
  _globals['_ERRORMESSAGE']._serialized_start=487
  _globals['_ERRORMESSAGE']._serialized_end=703
  _globals['_PULLREPLICATIONREQUEST']._serialized_start=706
  _globals['_PULLREPLICATIONREQUEST']._serialized_end=1180
  _globals['_HANDSHAKE']._serialized_start=1182
  _globals['_HANDSHAKE']._serialized_end=1193
  _globals['_SKIP']._serialized_start=1195
  _globals['_SKIP']._serialized_end=1230
  _globals['_OBJECTINFO']._serialized_start=1233
  _globals['_OBJECTINFO']._serialized_end=1403
  _globals['_CHUNK']._serialized_start=1405
  _globals['_CHUNK']._serialized_end=1518
  _globals['_PULLREPLICATIONRESPONSE']._serialized_start=1521
  _globals['_PULLREPLICATIONRESPONSE']._serialized_end=1919
  _globals['_DATAINFO']._serialized_start=1922
  _globals['_DATAINFO']._serialized_end=2072
  _globals['_DATAINFOS']._serialized_start=2074
  _globals['_DATAINFOS']._serialized_end=2157
  _globals['_PUSHREPLICATIONREQUEST']._serialized_start=2159
  _globals['_PUSHREPLICATIONREQUEST']._serialized_end=2258
  _globals['_PUSHREPLICATIONRESPONSE']._serialized_start=2260
  _globals['_PUSHREPLICATIONRESPONSE']._serialized_end=2303
  _globals['_GETCREDENTIALSREQUEST']._serialized_start=2305
  _globals['_GETCREDENTIALSREQUEST']._serialized_end=2328
  _globals['_GETCREDENTIALSRESPONSE']._serialized_start=2330
  _globals['_GETCREDENTIALSRESPONSE']._serialized_end=2416
  _globals['_CREATEORUPDATECREDENTIALSREQUEST']._serialized_start=2418
  _globals['_CREATEORUPDATECREDENTIALSREQUEST']._serialized_end=2452
  _globals['_CREATEORUPDATECREDENTIALSRESPONSE']._serialized_start=2454
  _globals['_CREATEORUPDATECREDENTIALSRESPONSE']._serialized_end=2551
  _globals['_REVOKECREDENTIALSREQUEST']._serialized_start=2553
  _globals['_REVOKECREDENTIALSREQUEST']._serialized_end=2579
  _globals['_REVOKECREDENTIALSRESPONSE']._serialized_start=2581
  _globals['_REVOKECREDENTIALSRESPONSE']._serialized_end=2608
  _globals['_S3PATH']._serialized_start=2610
  _globals['_S3PATH']._serialized_end=2660
  _globals['_PUSHREPLICAREQUEST']._serialized_start=2663
  _globals['_PUSHREPLICAREQUEST']._serialized_end=2844
  _globals['_PUSHREPLICARESPONSE']._serialized_start=2846
  _globals['_PUSHREPLICARESPONSE']._serialized_end=2906
  _globals['_PULLREPLICAREQUEST']._serialized_start=2909
  _globals['_PULLREPLICAREQUEST']._serialized_end=3044
  _globals['_PULLREPLICARESPONSE']._serialized_start=3046
  _globals['_PULLREPLICARESPONSE']._serialized_end=3106
  _globals['_REPLICATIONSTATUSREQUEST']._serialized_start=3108
  _globals['_REPLICATIONSTATUSREQUEST']._serialized_end=3173
  _globals['_REPLICATIONSTATUSRESPONSE']._serialized_start=3176
  _globals['_REPLICATIONSTATUSRESPONSE']._serialized_end=3305
  _globals['_OBJECTLOCATION']._serialized_start=3307
  _globals['_OBJECTLOCATION']._serialized_end=3433
  _globals['_PUTOBJECTREQUEST']._serialized_start=3435
  _globals['_PUTOBJECTREQUEST']._serialized_end=3550
  _globals['_PUTOBJECTRESPONSE']._serialized_start=3552
  _globals['_PUTOBJECTRESPONSE']._serialized_end=3571
  _globals['_GETOBJECTREQUEST']._serialized_start=3573
  _globals['_GETOBJECTREQUEST']._serialized_end=3668
  _globals['_GETOBJECTRESPONSE']._serialized_start=3670
  _globals['_GETOBJECTRESPONSE']._serialized_end=3709
  _globals['_HEADOBJECTREQUEST']._serialized_start=3711
  _globals['_HEADOBJECTREQUEST']._serialized_end=3807
  _globals['_HEADOBJECTRESPONSE']._serialized_start=3809
  _globals['_HEADOBJECTRESPONSE']._serialized_end=3892
  _globals['_INITMULTIPARTUPLOADREQUEST']._serialized_start=3894
  _globals['_INITMULTIPARTUPLOADREQUEST']._serialized_end=3999
  _globals['_INITMULTIPARTUPLOADRESPONSE']._serialized_start=4001
  _globals['_INITMULTIPARTUPLOADRESPONSE']._serialized_end=4059
  _globals['_UPLOADPARTREQUEST']._serialized_start=4062
  _globals['_UPLOADPARTREQUEST']._serialized_end=4211
  _globals['_UPLOADPARTRESPONSE']._serialized_start=4213
  _globals['_UPLOADPARTRESPONSE']._serialized_end=4253
  _globals['_COMPLETEDPART']._serialized_start=4255
  _globals['_COMPLETEDPART']._serialized_end=4323
  _globals['_COMPLETEMULTIPARTUPLOADREQUEST']._serialized_start=4326
  _globals['_COMPLETEMULTIPARTUPLOADREQUEST']._serialized_end=4524
  _globals['_COMPLETEMULTIPARTUPLOADRESPONSE']._serialized_start=4526
  _globals['_COMPLETEMULTIPARTUPLOADRESPONSE']._serialized_end=4559
  _globals['_CREATEBUCKETREQUEST']._serialized_start=4561
  _globals['_CREATEBUCKETREQUEST']._serialized_end=4606
  _globals['_CREATEBUCKETRESPONSE']._serialized_start=4608
  _globals['_CREATEBUCKETRESPONSE']._serialized_end=4630
  _globals['_DELETEBUCKETREQUEST']._serialized_start=4632
  _globals['_DELETEBUCKETREQUEST']._serialized_end=4677
  _globals['_DELETEBUCKETRESPONSE']._serialized_start=4679
  _globals['_DELETEBUCKETRESPONSE']._serialized_end=4701
  _globals['_DELETEOBJECTREQUEST']._serialized_start=4703
  _globals['_DELETEOBJECTREQUEST']._serialized_end=4801
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=4803
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=4825
  _globals['_INITLOCATIONREQUEST']._serialized_start=4827
  _globals['_INITLOCATIONREQUEST']._serialized_end=4936
  _globals['_INITLOCATIONRESPONSE']._serialized_start=4938
  _globals['_INITLOCATIONRESPONSE']._serialized_end=5037
  _globals['_INGESTRESOURCE']._serialized_start=5040
  _globals['_INGESTRESOURCE']._serialized_end=5556
  _globals['_INGESTEXISTINGOBJECTREQUEST']._serialized_start=5559
  _globals['_INGESTEXISTINGOBJECTREQUEST']._serialized_end=6003
  _globals['_INGESTEXISTINGOBJECTRESPONSE']._serialized_start=6005
  _globals['_INGESTEXISTINGOBJECTRESPONSE']._serialized_end=6064
  _globals['_DATAPROXYREPLICATIONSERVICE']._serialized_start=6252
  _globals['_DATAPROXYREPLICATIONSERVICE']._serialized_end=6574
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_start=6577
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_end=7919
  _globals['_DATAPROXYUSERSERVICE']._serialized_start=7922
  _globals['_DATAPROXYUSERSERVICE']._serialized_end=8965
  _globals['_DATAPROXYINGESTIONSERVICE']._serialized_start=8968
  _globals['_DATAPROXYINGESTIONSERVICE']._serialized_end=9162
# @@protoc_insertion_point(module_scope)
