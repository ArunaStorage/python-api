# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/dataproxy/services/v2/dataproxy_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7aruna/api/dataproxy/services/v2/dataproxy_service.proto\x12\x1f\x61runa.api.dataproxy.services.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\"[\n\rDataProxyInfo\x12!\n\x0c\x64\x61taproxy_id\x18\x01 \x01(\tR\x0b\x64\x61taproxyId\x12\'\n\x0f\x61vailable_space\x18\x02 \x01(\x03R\x0e\x61vailableSpace\"\x8a\x01\n\x19RequestReplicationRequest\x12\x42\n\x04info\x18\x01 \x01(\x0b\x32..aruna.api.dataproxy.services.v2.DataProxyInfoR\x04info\x12)\n\x10user_initialized\x18\x02 \x01(\x08R\x0fuserInitialized\"\x96\x01\n\x08\x44\x61taInfo\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12!\n\x0c\x64ownload_url\x18\x02 \x01(\tR\x0b\x64ownloadUrl\x12%\n\x0e\x65ncryption_key\x18\x03 \x01(\tR\rencryptionKey\x12#\n\ris_compressed\x18\x04 \x01(\x08R\x0cisCompressed\"S\n\tDataInfos\x12\x46\n\tdata_info\x18\x01 \x03(\x0b\x32).aruna.api.dataproxy.services.v2.DataInfoR\x08\x64\x61taInfo\"\x89\x01\n\x1aRequestReplicationResponse\x12K\n\ndata_infos\x18\x01 \x01(\x0b\x32*.aruna.api.dataproxy.services.v2.DataInfosH\x00R\tdataInfos\x12\x12\n\x03\x61\x63k\x18\x02 \x01(\x08H\x00R\x03\x61\x63kB\n\n\x08response\"c\n\x16InitReplicationRequest\x12I\n\ndata_infos\x18\x01 \x01(\x0b\x32*.aruna.api.dataproxy.services.v2.DataInfosR\tdataInfos\"+\n\x17InitReplicationResponse\x12\x10\n\x03\x61\x63k\x18\x01 \x01(\x08R\x03\x61\x63k\"\x17\n\x15GetCredentialsRequest\"V\n\x16GetCredentialsResponse\x12\x1d\n\naccess_key\x18\x01 \x01(\tR\taccessKey\x12\x1d\n\nsecret_key\x18\x02 \x01(\tR\tsecretKey\"2\n\x06S3Path\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\"\xb0\x01\n\x12PushReplicaRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tH\x00R\nresourceId\x12\x42\n\x07s3_path\x18\x02 \x01(\x0b\x32\'.aruna.api.dataproxy.services.v2.S3PathH\x00R\x06s3Path\x12\'\n\x0ftarget_location\x18\x03 \x01(\tR\x0etargetLocationB\n\n\x08resource\"<\n\x13PushReplicaResponse\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"\x87\x01\n\x12PullReplicaRequest\x12!\n\x0bresource_id\x18\x01 \x01(\tH\x00R\nresourceId\x12\x42\n\x07s3_path\x18\x02 \x01(\x0b\x32\'.aruna.api.dataproxy.services.v2.S3PathH\x00R\x06s3PathB\n\n\x08resource\"<\n\x13PullReplicaResponse\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"A\n\x18ReplicationStatusRequest\x12%\n\x0ereplication_id\x18\x01 \x01(\tR\rreplicationId\"\x81\x01\n\x19ReplicationStatusResponse\x12J\n\x06status\x18\x01 \x01(\x0e\x32\x32.aruna.api.dataproxy.services.v2.ReplicationStatusR\x06status\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\"~\n\x0eObjectLocation\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x1b\n\tupload_id\x18\x03 \x01(\tR\x08uploadId\x12%\n\x0e\x63ontent_length\x18\x04 \x01(\tR\rcontentLength\"s\n\x10PutObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12\x12\n\x04\x64\x61ta\x18\x02 \x01(\x0cR\x04\x64\x61ta\"\x13\n\x11PutObjectResponse\"_\n\x10GetObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"\'\n\x11GetObjectResponse\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"`\n\x11HeadObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"S\n\x12HeadObjectResponse\x12%\n\x0e\x63ontent_length\x18\x01 \x01(\tR\rcontentLength\x12\x16\n\x06\x65xists\x18\x02 \x01(\x08R\x06\x65xists\"i\n\x1aInitMultiPartUploadRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\":\n\x1bInitMultiPartUploadResponse\x12\x1b\n\tupload_id\x18\x01 \x01(\tR\x08uploadId\"\x95\x01\n\x11UploadPartRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12\x1f\n\x0bpart_number\x18\x03 \x01(\x05R\npartNumber\x12\x12\n\x04\x64\x61ta\x18\x04 \x01(\x0cR\x04\x64\x61ta\"(\n\x12UploadPartResponse\x12\x12\n\x04\x65tag\x18\x01 \x01(\tR\x04\x65tag\"D\n\rCompletedPart\x12\x1f\n\x0bpart_number\x18\x01 \x01(\x05R\npartNumber\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\"\xc6\x01\n\x1e\x43ompleteMultiPartUploadRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\x12W\n\x0f\x63ompleted_parts\x18\x02 \x03(\x0b\x32..aruna.api.dataproxy.services.v2.CompletedPartR\x0e\x63ompletedParts\"!\n\x1f\x43ompleteMultiPartUploadResponse\"-\n\x13\x43reateBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\"\x16\n\x14\x43reateBucketResponse\"-\n\x13\x44\x65leteBucketRequest\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\"\x16\n\x14\x44\x65leteBucketResponse\"b\n\x13\x44\x65leteObjectRequest\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location\"\x16\n\x14\x44\x65leteObjectResponse\"m\n\x13InitLocationRequest\x12\x1f\n\x0bobject_name\x18\x01 \x01(\tR\nobjectName\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size\x12!\n\x0cis_temporary\x18\x03 \x01(\x08R\x0bisTemporary\"c\n\x14InitLocationResponse\x12K\n\x08location\x18\x01 \x01(\x0b\x32/.aruna.api.dataproxy.services.v2.ObjectLocationR\x08location*\xb6\x01\n\x11ReplicationStatus\x12\"\n\x1eREPLICATION_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1aREPLICATION_STATUS_PENDING\x10\x01\x12\x1e\n\x1aREPLICATION_STATUS_RUNNING\x10\x02\x12\x1f\n\x1bREPLICATION_STATUS_FINISHED\x10\x03\x12\x1c\n\x18REPLICATION_STATUS_ERROR\x10\x04\x32\xbc\x02\n\x10\x44\x61taproxyService\x12\x8f\x01\n\x12RequestReplication\x12:.aruna.api.dataproxy.services.v2.RequestReplicationRequest\x1a;.aruna.api.dataproxy.services.v2.RequestReplicationResponse\"\x00\x12\x86\x01\n\x0fInitReplication\x12\x37.aruna.api.dataproxy.services.v2.InitReplicationRequest\x1a\x38.aruna.api.dataproxy.services.v2.InitReplicationResponse\"\x00\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXY2\xbe\n\n\x17\x44\x61taproxyBackendService\x12v\n\tPutObject\x12\x31.aruna.api.dataproxy.services.v2.PutObjectRequest\x1a\x32.aruna.api.dataproxy.services.v2.PutObjectResponse\"\x00(\x01\x12v\n\tGetObject\x12\x31.aruna.api.dataproxy.services.v2.GetObjectRequest\x1a\x32.aruna.api.dataproxy.services.v2.GetObjectResponse\"\x00\x30\x01\x12w\n\nHeadObject\x12\x32.aruna.api.dataproxy.services.v2.HeadObjectRequest\x1a\x33.aruna.api.dataproxy.services.v2.HeadObjectResponse\"\x00\x12\x92\x01\n\x13InitMultiPartUpload\x12;.aruna.api.dataproxy.services.v2.InitMultiPartUploadRequest\x1a<.aruna.api.dataproxy.services.v2.InitMultiPartUploadResponse\"\x00\x12y\n\nUploadPart\x12\x32.aruna.api.dataproxy.services.v2.UploadPartRequest\x1a\x33.aruna.api.dataproxy.services.v2.UploadPartResponse\"\x00(\x01\x12\x9e\x01\n\x17\x43ompleteMultiPartUpload\x12?.aruna.api.dataproxy.services.v2.CompleteMultiPartUploadRequest\x1a@.aruna.api.dataproxy.services.v2.CompleteMultiPartUploadResponse\"\x00\x12}\n\x0c\x43reateBucket\x12\x34.aruna.api.dataproxy.services.v2.CreateBucketRequest\x1a\x35.aruna.api.dataproxy.services.v2.CreateBucketResponse\"\x00\x12}\n\x0c\x44\x65leteBucket\x12\x34.aruna.api.dataproxy.services.v2.DeleteBucketRequest\x1a\x35.aruna.api.dataproxy.services.v2.DeleteBucketResponse\"\x00\x12}\n\x0c\x44\x65leteObject\x12\x34.aruna.api.dataproxy.services.v2.DeleteObjectRequest\x1a\x35.aruna.api.dataproxy.services.v2.DeleteObjectResponse\"\x00\x12}\n\x0cInitLocation\x12\x34.aruna.api.dataproxy.services.v2.InitLocationRequest\x1a\x35.aruna.api.dataproxy.services.v2.InitLocationResponse\"\x00\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXY2\x9e\x05\n\x14\x44\x61taproxyUserService\x12\x9d\x01\n\x0eGetCredentials\x12\x36.aruna.api.dataproxy.services.v2.GetCredentialsRequest\x1a\x37.aruna.api.dataproxy.services.v2.GetCredentialsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v2/credentials:\x01*\x12\x95\x01\n\x0bPushReplica\x12\x33.aruna.api.dataproxy.services.v2.PushReplicaRequest\x1a\x34.aruna.api.dataproxy.services.v2.PushReplicaResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/replica/push:\x01*\x12\x95\x01\n\x0bPullReplica\x12\x33.aruna.api.dataproxy.services.v2.PullReplicaRequest\x1a\x34.aruna.api.dataproxy.services.v2.PullReplicaResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/replica/pull:\x01*\x12\xa6\x01\n\x11ReplicationStatus\x12\x39.aruna.api.dataproxy.services.v2.ReplicationStatusRequest\x1a:.aruna.api.dataproxy.services.v2.ReplicationStatusResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v2/replica/status\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXYB\x96\x01\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\x10\x44\x61taProxyServiceP\x01Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.dataproxy.services.v2.dataproxy_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\020DataProxyServiceP\001Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2'
  _globals['_DATAPROXYSERVICE']._options = None
  _globals['_DATAPROXYSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYBACKENDSERVICE']._options = None
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYUSERSERVICE']._options = None
  _globals['_DATAPROXYUSERSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['GetCredentials']._options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['GetCredentials']._serialized_options = b'\202\323\344\223\002\024\"\017/v2/credentials:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PushReplica']._options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PushReplica']._serialized_options = b'\202\323\344\223\002\025\"\020/v2/replica/push:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PullReplica']._options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['PullReplica']._serialized_options = b'\202\323\344\223\002\025\"\020/v2/replica/pull:\001*'
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['ReplicationStatus']._options = None
  _globals['_DATAPROXYUSERSERVICE'].methods_by_name['ReplicationStatus']._serialized_options = b'\202\323\344\223\002\024\022\022/v2/replica/status'
  _globals['_REPLICATIONSTATUS']._serialized_start=3447
  _globals['_REPLICATIONSTATUS']._serialized_end=3629
  _globals['_DATAPROXYINFO']._serialized_start=151
  _globals['_DATAPROXYINFO']._serialized_end=242
  _globals['_REQUESTREPLICATIONREQUEST']._serialized_start=245
  _globals['_REQUESTREPLICATIONREQUEST']._serialized_end=383
  _globals['_DATAINFO']._serialized_start=386
  _globals['_DATAINFO']._serialized_end=536
  _globals['_DATAINFOS']._serialized_start=538
  _globals['_DATAINFOS']._serialized_end=621
  _globals['_REQUESTREPLICATIONRESPONSE']._serialized_start=624
  _globals['_REQUESTREPLICATIONRESPONSE']._serialized_end=761
  _globals['_INITREPLICATIONREQUEST']._serialized_start=763
  _globals['_INITREPLICATIONREQUEST']._serialized_end=862
  _globals['_INITREPLICATIONRESPONSE']._serialized_start=864
  _globals['_INITREPLICATIONRESPONSE']._serialized_end=907
  _globals['_GETCREDENTIALSREQUEST']._serialized_start=909
  _globals['_GETCREDENTIALSREQUEST']._serialized_end=932
  _globals['_GETCREDENTIALSRESPONSE']._serialized_start=934
  _globals['_GETCREDENTIALSRESPONSE']._serialized_end=1020
  _globals['_S3PATH']._serialized_start=1022
  _globals['_S3PATH']._serialized_end=1072
  _globals['_PUSHREPLICAREQUEST']._serialized_start=1075
  _globals['_PUSHREPLICAREQUEST']._serialized_end=1251
  _globals['_PUSHREPLICARESPONSE']._serialized_start=1253
  _globals['_PUSHREPLICARESPONSE']._serialized_end=1313
  _globals['_PULLREPLICAREQUEST']._serialized_start=1316
  _globals['_PULLREPLICAREQUEST']._serialized_end=1451
  _globals['_PULLREPLICARESPONSE']._serialized_start=1453
  _globals['_PULLREPLICARESPONSE']._serialized_end=1513
  _globals['_REPLICATIONSTATUSREQUEST']._serialized_start=1515
  _globals['_REPLICATIONSTATUSREQUEST']._serialized_end=1580
  _globals['_REPLICATIONSTATUSRESPONSE']._serialized_start=1583
  _globals['_REPLICATIONSTATUSRESPONSE']._serialized_end=1712
  _globals['_OBJECTLOCATION']._serialized_start=1714
  _globals['_OBJECTLOCATION']._serialized_end=1840
  _globals['_PUTOBJECTREQUEST']._serialized_start=1842
  _globals['_PUTOBJECTREQUEST']._serialized_end=1957
  _globals['_PUTOBJECTRESPONSE']._serialized_start=1959
  _globals['_PUTOBJECTRESPONSE']._serialized_end=1978
  _globals['_GETOBJECTREQUEST']._serialized_start=1980
  _globals['_GETOBJECTREQUEST']._serialized_end=2075
  _globals['_GETOBJECTRESPONSE']._serialized_start=2077
  _globals['_GETOBJECTRESPONSE']._serialized_end=2116
  _globals['_HEADOBJECTREQUEST']._serialized_start=2118
  _globals['_HEADOBJECTREQUEST']._serialized_end=2214
  _globals['_HEADOBJECTRESPONSE']._serialized_start=2216
  _globals['_HEADOBJECTRESPONSE']._serialized_end=2299
  _globals['_INITMULTIPARTUPLOADREQUEST']._serialized_start=2301
  _globals['_INITMULTIPARTUPLOADREQUEST']._serialized_end=2406
  _globals['_INITMULTIPARTUPLOADRESPONSE']._serialized_start=2408
  _globals['_INITMULTIPARTUPLOADRESPONSE']._serialized_end=2466
  _globals['_UPLOADPARTREQUEST']._serialized_start=2469
  _globals['_UPLOADPARTREQUEST']._serialized_end=2618
  _globals['_UPLOADPARTRESPONSE']._serialized_start=2620
  _globals['_UPLOADPARTRESPONSE']._serialized_end=2660
  _globals['_COMPLETEDPART']._serialized_start=2662
  _globals['_COMPLETEDPART']._serialized_end=2730
  _globals['_COMPLETEMULTIPARTUPLOADREQUEST']._serialized_start=2733
  _globals['_COMPLETEMULTIPARTUPLOADREQUEST']._serialized_end=2931
  _globals['_COMPLETEMULTIPARTUPLOADRESPONSE']._serialized_start=2933
  _globals['_COMPLETEMULTIPARTUPLOADRESPONSE']._serialized_end=2966
  _globals['_CREATEBUCKETREQUEST']._serialized_start=2968
  _globals['_CREATEBUCKETREQUEST']._serialized_end=3013
  _globals['_CREATEBUCKETRESPONSE']._serialized_start=3015
  _globals['_CREATEBUCKETRESPONSE']._serialized_end=3037
  _globals['_DELETEBUCKETREQUEST']._serialized_start=3039
  _globals['_DELETEBUCKETREQUEST']._serialized_end=3084
  _globals['_DELETEBUCKETRESPONSE']._serialized_start=3086
  _globals['_DELETEBUCKETRESPONSE']._serialized_end=3108
  _globals['_DELETEOBJECTREQUEST']._serialized_start=3110
  _globals['_DELETEOBJECTREQUEST']._serialized_end=3208
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=3210
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=3232
  _globals['_INITLOCATIONREQUEST']._serialized_start=3234
  _globals['_INITLOCATIONREQUEST']._serialized_end=3343
  _globals['_INITLOCATIONRESPONSE']._serialized_start=3345
  _globals['_INITLOCATIONRESPONSE']._serialized_end=3444
  _globals['_DATAPROXYSERVICE']._serialized_start=3632
  _globals['_DATAPROXYSERVICE']._serialized_end=3948
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_start=3951
  _globals['_DATAPROXYBACKENDSERVICE']._serialized_end=5293
  _globals['_DATAPROXYUSERSERVICE']._serialized_start=5296
  _globals['_DATAPROXYUSERSERVICE']._serialized_end=5966
# @@protoc_insertion_point(module_scope)
