# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: aruna/api/storage/services/v2/object_service.proto
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
    'aruna/api/storage/services/v2/object_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2aruna/api/storage/services/v2/object_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\"\xfc\x04\n\x13\x43reateObjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\x0c \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x44\n\nkey_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\tkeyValues\x12\x43\n\trelations\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\trelations\x12\x45\n\ndata_class\x18\x05 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12\x1f\n\nproject_id\x18\x06 \x01(\tH\x00R\tprojectId\x12%\n\rcollection_id\x18\x07 \x01(\tH\x00R\x0c\x63ollectionId\x12\x1f\n\ndataset_id\x18\x08 \x01(\tH\x00R\tdatasetId\x12\x39\n\x06hashes\x18\t \x03(\x0b\x32!.aruna.api.storage.models.v2.HashR\x06hashes\x12\x30\n\x14metadata_license_tag\x18\n \x01(\tR\x12metadataLicenseTag\x12(\n\x10\x64\x61ta_license_tag\x18\x0b \x01(\tR\x0e\x64\x61taLicenseTag\x12=\n\x07\x61uthors\x18\r \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\x07\x61uthorsB\x08\n\x06parent\"S\n\x14\x43reateObjectResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"\x8e\x01\n\x13GetUploadURLRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1c\n\tmultipart\x18\x02 \x01(\x08R\tmultipart\x12\x1f\n\x0bpart_number\x18\x03 \x01(\x05R\npartNumber\x12\x1b\n\tupload_id\x18\x04 \x01(\tR\x08uploadId\"E\n\x14GetUploadURLResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x1b\n\tupload_id\x18\x02 \x01(\tR\x08uploadId\"4\n\x15GetDownloadURLRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\"*\n\x16GetDownloadURLResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"7\n\rCompletedPart\x12\x12\n\x04\x65tag\x18\x01 \x01(\tR\x04\x65tag\x12\x12\n\x04part\x18\x02 \x01(\x03R\x04part\"\x89\x02\n\x1a\x46inishObjectStagingRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1f\n\x0b\x63ontent_len\x18\x02 \x01(\x03R\ncontentLen\x12\x39\n\x06hashes\x18\x03 \x03(\x0b\x32!.aruna.api.storage.models.v2.HashR\x06hashes\x12U\n\x0f\x63ompleted_parts\x18\x04 \x03(\x0b\x32,.aruna.api.storage.services.v2.CompletedPartR\x0e\x63ompletedParts\x12\x1b\n\tupload_id\x18\x05 \x01(\tR\x08uploadId\"Z\n\x1b\x46inishObjectStagingResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"\xdb\x05\n\x13UpdateObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x17\n\x04name\x18\x02 \x01(\tH\x01R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x02R\x0b\x64\x65scription\x88\x01\x01\x12K\n\x0e\x61\x64\x64_key_values\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0c\x61\x64\x64KeyValues\x12Q\n\x11remove_key_values\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0fremoveKeyValues\x12\x45\n\ndata_class\x18\x07 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12\x1f\n\nproject_id\x18\x08 \x01(\tH\x00R\tprojectId\x12%\n\rcollection_id\x18\t \x01(\tH\x00R\x0c\x63ollectionId\x12\x1f\n\ndataset_id\x18\n \x01(\tH\x00R\tdatasetId\x12\x39\n\x06hashes\x18\x0c \x03(\x0b\x32!.aruna.api.storage.models.v2.HashR\x06hashes\x12%\n\x0e\x66orce_revision\x18\r \x01(\x08R\rforceRevision\x12\x35\n\x14metadata_license_tag\x18\x0e \x01(\tH\x03R\x12metadataLicenseTag\x88\x01\x01\x12-\n\x10\x64\x61ta_license_tag\x18\x0f \x01(\tH\x04R\x0e\x64\x61taLicenseTag\x88\x01\x01\x42\x08\n\x06parentB\x07\n\x05_nameB\x0e\n\x0c_descriptionB\x17\n\x15_metadata_license_tagB\x13\n\x11_data_license_tag\"v\n\x14UpdateObjectResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\x12!\n\x0cnew_revision\x18\x02 \x01(\x08R\x0bnewRevision\"\xa4\x01\n\x12\x43loneObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x1f\n\nproject_id\x18\x02 \x01(\tH\x00R\tprojectId\x12%\n\rcollection_id\x18\x03 \x01(\tH\x00R\x0c\x63ollectionId\x12\x1f\n\ndataset_id\x18\x04 \x01(\tH\x00R\tdatasetIdB\x08\n\x06parent\"R\n\x13\x43loneObjectResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"Y\n\x13\x44\x65leteObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12%\n\x0ewith_revisions\x18\x02 \x01(\x08R\rwithRevisions\"\x16\n\x14\x44\x65leteObjectResponse\"/\n\x10GetObjectRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\"P\n\x11GetObjectResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"2\n\x11GetObjectsRequest\x12\x1d\n\nobject_ids\x18\x01 \x03(\tR\tobjectIds\"S\n\x12GetObjectsResponse\x12=\n\x07objects\x18\x01 \x03(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x07objects\"8\n\x19GetObjectRevisionsRequest\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\"[\n\x1aGetObjectRevisionsResponse\x12=\n\x07objects\x18\x01 \x03(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x07objects\"=\n\x1eGetLatestObjectRevisionRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\"^\n\x1fGetLatestObjectRevisionResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"]\n\x19GetObjectEndpointsRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\"M\n\x18UpdateObjectTitleRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\"X\n\x19UpdateObjectTitleResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"\xcb\x01\n\x1aUpdateObjectAuthorsRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x44\n\x0b\x61\x64\x64_authors\x18\x02 \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\naddAuthors\x12J\n\x0eremove_authors\x18\x03 \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\rremoveAuthors\"Z\n\x1bUpdateObjectAuthorsResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object\"p\n\x16SetObjectHashesRequest\x12\x1b\n\tobject_id\x18\x01 \x01(\tR\x08objectId\x12\x39\n\x06hashes\x18\x02 \x03(\x0b\x32!.aruna.api.storage.models.v2.HashR\x06hashes\"V\n\x17SetObjectHashesResponse\x12;\n\x06object\x18\x01 \x01(\x0b\x32#.aruna.api.storage.models.v2.ObjectR\x06object2\xc3\x0f\n\rObjectService\x12\x8f\x01\n\x0c\x43reateObject\x12\x32.aruna.api.storage.services.v2.CreateObjectRequest\x1a\x33.aruna.api.storage.services.v2.CreateObjectResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/v2/objects:\x01*\x12\x9f\x01\n\x0cGetUploadURL\x12\x32.aruna.api.storage.services.v2.GetUploadURLRequest\x1a\x33.aruna.api.storage.services.v2.GetUploadURLResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v2/objects/{object_id}/upload\x12\xa7\x01\n\x0eGetDownloadURL\x12\x34.aruna.api.storage.services.v2.GetDownloadURLRequest\x1a\x35.aruna.api.storage.services.v2.GetDownloadURLResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v2/objects/{object_id}/download\x12\xb7\x01\n\x13\x46inishObjectStaging\x12\x39.aruna.api.storage.services.v2.FinishObjectStagingRequest\x1a:.aruna.api.storage.services.v2.FinishObjectStagingResponse\")\x82\xd3\xe4\x93\x02#2\x1e/v2/objects/{object_id}/finish:\x01*\x12\x9b\x01\n\x0cUpdateObject\x12\x32.aruna.api.storage.services.v2.UpdateObjectRequest\x1a\x33.aruna.api.storage.services.v2.UpdateObjectResponse\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v2/objects/{object_id}:\x01*\x12\x96\x01\n\x0b\x43loneObject\x12\x31.aruna.api.storage.services.v2.CloneObjectRequest\x1a\x32.aruna.api.storage.services.v2.CloneObjectResponse\" \x82\xd3\xe4\x93\x02\x1a\"\x15/v2/{object_id}/clone:\x01*\x12\x9b\x01\n\x0c\x44\x65leteObject\x12\x32.aruna.api.storage.services.v2.DeleteObjectRequest\x1a\x33.aruna.api.storage.services.v2.DeleteObjectResponse\"\"\x82\xd3\xe4\x93\x02\x1c*\x17/v2/objects/{object_id}:\x01*\x12\x8f\x01\n\tGetObject\x12/.aruna.api.storage.services.v2.GetObjectRequest\x1a\x30.aruna.api.storage.services.v2.GetObjectResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v2/objects/{object_id}\x12\x86\x01\n\nGetObjects\x12\x30.aruna.api.storage.services.v2.GetObjectsRequest\x1a\x31.aruna.api.storage.services.v2.GetObjectsResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v2/objects\x12\xb0\x01\n\x11UpdateObjectTitle\x12\x37.aruna.api.storage.services.v2.UpdateObjectTitleRequest\x1a\x38.aruna.api.storage.services.v2.UpdateObjectTitleResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v2/objects/{object_id}/title:\x01*\x12\xb8\x01\n\x13UpdateObjectAuthors\x12\x39.aruna.api.storage.services.v2.UpdateObjectAuthorsRequest\x1a:.aruna.api.storage.services.v2.UpdateObjectAuthorsResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v2/objects/{object_id}/authors:\x01*\x12\xab\x01\n\x0fSetObjectHashes\x12\x35.aruna.api.storage.services.v2.SetObjectHashesRequest\x1a\x36.aruna.api.storage.services.v2.SetObjectHashesResponse\")\x82\xd3\xe4\x93\x02#\"\x1e/v2/objects/{object_id}/hashes:\x01*\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x92\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\rObjectServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.object_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\rObjectServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_OBJECTSERVICE']._loaded_options = None
  _globals['_OBJECTSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_OBJECTSERVICE'].methods_by_name['CreateObject']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['CreateObject']._serialized_options = b'\202\323\344\223\002\020\"\013/v2/objects:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['GetUploadURL']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['GetUploadURL']._serialized_options = b'\202\323\344\223\002 \022\036/v2/objects/{object_id}/upload'
  _globals['_OBJECTSERVICE'].methods_by_name['GetDownloadURL']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['GetDownloadURL']._serialized_options = b'\202\323\344\223\002\"\022 /v2/objects/{object_id}/download'
  _globals['_OBJECTSERVICE'].methods_by_name['FinishObjectStaging']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['FinishObjectStaging']._serialized_options = b'\202\323\344\223\002#2\036/v2/objects/{object_id}/finish:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObject']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObject']._serialized_options = b'\202\323\344\223\002\034\"\027/v2/objects/{object_id}:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['CloneObject']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['CloneObject']._serialized_options = b'\202\323\344\223\002\032\"\025/v2/{object_id}/clone:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['DeleteObject']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['DeleteObject']._serialized_options = b'\202\323\344\223\002\034*\027/v2/objects/{object_id}:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['GetObject']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['GetObject']._serialized_options = b'\202\323\344\223\002\031\022\027/v2/objects/{object_id}'
  _globals['_OBJECTSERVICE'].methods_by_name['GetObjects']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['GetObjects']._serialized_options = b'\202\323\344\223\002\r\022\013/v2/objects'
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObjectTitle']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObjectTitle']._serialized_options = b'\202\323\344\223\002\"\"\035/v2/objects/{object_id}/title:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObjectAuthors']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['UpdateObjectAuthors']._serialized_options = b'\202\323\344\223\002$\"\037/v2/objects/{object_id}/authors:\001*'
  _globals['_OBJECTSERVICE'].methods_by_name['SetObjectHashes']._loaded_options = None
  _globals['_OBJECTSERVICE'].methods_by_name['SetObjectHashes']._serialized_options = b'\202\323\344\223\002#\"\036/v2/objects/{object_id}/hashes:\001*'
  _globals['_CREATEOBJECTREQUEST']._serialized_start=187
  _globals['_CREATEOBJECTREQUEST']._serialized_end=823
  _globals['_CREATEOBJECTRESPONSE']._serialized_start=825
  _globals['_CREATEOBJECTRESPONSE']._serialized_end=908
  _globals['_GETUPLOADURLREQUEST']._serialized_start=911
  _globals['_GETUPLOADURLREQUEST']._serialized_end=1053
  _globals['_GETUPLOADURLRESPONSE']._serialized_start=1055
  _globals['_GETUPLOADURLRESPONSE']._serialized_end=1124
  _globals['_GETDOWNLOADURLREQUEST']._serialized_start=1126
  _globals['_GETDOWNLOADURLREQUEST']._serialized_end=1178
  _globals['_GETDOWNLOADURLRESPONSE']._serialized_start=1180
  _globals['_GETDOWNLOADURLRESPONSE']._serialized_end=1222
  _globals['_COMPLETEDPART']._serialized_start=1224
  _globals['_COMPLETEDPART']._serialized_end=1279
  _globals['_FINISHOBJECTSTAGINGREQUEST']._serialized_start=1282
  _globals['_FINISHOBJECTSTAGINGREQUEST']._serialized_end=1547
  _globals['_FINISHOBJECTSTAGINGRESPONSE']._serialized_start=1549
  _globals['_FINISHOBJECTSTAGINGRESPONSE']._serialized_end=1639
  _globals['_UPDATEOBJECTREQUEST']._serialized_start=1642
  _globals['_UPDATEOBJECTREQUEST']._serialized_end=2373
  _globals['_UPDATEOBJECTRESPONSE']._serialized_start=2375
  _globals['_UPDATEOBJECTRESPONSE']._serialized_end=2493
  _globals['_CLONEOBJECTREQUEST']._serialized_start=2496
  _globals['_CLONEOBJECTREQUEST']._serialized_end=2660
  _globals['_CLONEOBJECTRESPONSE']._serialized_start=2662
  _globals['_CLONEOBJECTRESPONSE']._serialized_end=2744
  _globals['_DELETEOBJECTREQUEST']._serialized_start=2746
  _globals['_DELETEOBJECTREQUEST']._serialized_end=2835
  _globals['_DELETEOBJECTRESPONSE']._serialized_start=2837
  _globals['_DELETEOBJECTRESPONSE']._serialized_end=2859
  _globals['_GETOBJECTREQUEST']._serialized_start=2861
  _globals['_GETOBJECTREQUEST']._serialized_end=2908
  _globals['_GETOBJECTRESPONSE']._serialized_start=2910
  _globals['_GETOBJECTRESPONSE']._serialized_end=2990
  _globals['_GETOBJECTSREQUEST']._serialized_start=2992
  _globals['_GETOBJECTSREQUEST']._serialized_end=3042
  _globals['_GETOBJECTSRESPONSE']._serialized_start=3044
  _globals['_GETOBJECTSRESPONSE']._serialized_end=3127
  _globals['_GETOBJECTREVISIONSREQUEST']._serialized_start=3129
  _globals['_GETOBJECTREVISIONSREQUEST']._serialized_end=3185
  _globals['_GETOBJECTREVISIONSRESPONSE']._serialized_start=3187
  _globals['_GETOBJECTREVISIONSRESPONSE']._serialized_end=3278
  _globals['_GETLATESTOBJECTREVISIONREQUEST']._serialized_start=3280
  _globals['_GETLATESTOBJECTREVISIONREQUEST']._serialized_end=3341
  _globals['_GETLATESTOBJECTREVISIONRESPONSE']._serialized_start=3343
  _globals['_GETLATESTOBJECTREVISIONRESPONSE']._serialized_end=3437
  _globals['_GETOBJECTENDPOINTSREQUEST']._serialized_start=3439
  _globals['_GETOBJECTENDPOINTSREQUEST']._serialized_end=3532
  _globals['_UPDATEOBJECTTITLEREQUEST']._serialized_start=3534
  _globals['_UPDATEOBJECTTITLEREQUEST']._serialized_end=3611
  _globals['_UPDATEOBJECTTITLERESPONSE']._serialized_start=3613
  _globals['_UPDATEOBJECTTITLERESPONSE']._serialized_end=3701
  _globals['_UPDATEOBJECTAUTHORSREQUEST']._serialized_start=3704
  _globals['_UPDATEOBJECTAUTHORSREQUEST']._serialized_end=3907
  _globals['_UPDATEOBJECTAUTHORSRESPONSE']._serialized_start=3909
  _globals['_UPDATEOBJECTAUTHORSRESPONSE']._serialized_end=3999
  _globals['_SETOBJECTHASHESREQUEST']._serialized_start=4001
  _globals['_SETOBJECTHASHESREQUEST']._serialized_end=4113
  _globals['_SETOBJECTHASHESRESPONSE']._serialized_start=4115
  _globals['_SETOBJECTHASHESRESPONSE']._serialized_end=4201
  _globals['_OBJECTSERVICE']._serialized_start=4204
  _globals['_OBJECTSERVICE']._serialized_end=6191
# @@protoc_insertion_point(module_scope)
