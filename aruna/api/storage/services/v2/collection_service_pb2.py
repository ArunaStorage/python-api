# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/collection_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6aruna/api/storage/services/v2/collection_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\"\xcc\x04\n\x17\x43reateCollectionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05title\x18\t \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x44\n\nkey_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\tkeyValues\x12\x43\n\trelations\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\trelations\x12\x45\n\ndata_class\x18\x05 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12\x1f\n\nproject_id\x18\x06 \x01(\tH\x00R\tprojectId\x12\x35\n\x14metadata_license_tag\x18\x07 \x01(\tH\x01R\x12metadataLicenseTag\x88\x01\x01\x12<\n\x18\x64\x65\x66\x61ult_data_license_tag\x18\x08 \x01(\tH\x02R\x15\x64\x65\x66\x61ultDataLicenseTag\x88\x01\x01\x12=\n\x07\x61uthors\x18\n \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\x07\x61uthorsB\x08\n\x06parentB\x17\n\x15_metadata_license_tagB\x1b\n\x19_default_data_license_tag\"c\n\x18\x43reateCollectionResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\";\n\x14GetCollectionRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\"`\n\x15GetCollectionResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\">\n\x15GetCollectionsRequest\x12%\n\x0e\x63ollection_ids\x18\x01 \x03(\tR\rcollectionIds\"c\n\x16GetCollectionsResponse\x12I\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\x0b\x63ollections\">\n\x17\x44\x65leteCollectionRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\"\x1a\n\x18\x44\x65leteCollectionResponse\"V\n\x1bUpdateCollectionNameRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"g\n\x1cUpdateCollectionNameResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"k\n\"UpdateCollectionDescriptionRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"n\n#UpdateCollectionDescriptionResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"\xe7\x01\n UpdateCollectionKeyValuesRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12K\n\x0e\x61\x64\x64_key_values\x18\x02 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0c\x61\x64\x64KeyValues\x12Q\n\x11remove_key_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0fremoveKeyValues\"l\n!UpdateCollectionKeyValuesResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"\x8e\x01\n UpdateCollectionDataClassRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x45\n\ndata_class\x18\x02 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\"l\n!UpdateCollectionDataClassResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"@\n\x19SnapshotCollectionRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\"e\n\x1aSnapshotCollectionResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"\xb1\x01\n\x1fUpdateCollectionLicensesRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x30\n\x14metadata_license_tag\x18\x02 \x01(\tR\x12metadataLicenseTag\x12\x37\n\x18\x64\x65\x66\x61ult_data_license_tag\x18\x03 \x01(\tR\x15\x64\x65\x66\x61ultDataLicenseTag\"k\n UpdateCollectionLicensesResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"Y\n\x1cUpdateCollectionTitleRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\"h\n\x1dUpdateCollectionTitleResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection\"\xd7\x01\n\x1eUpdateCollectionAuthorsRequest\x12#\n\rcollection_id\x18\x01 \x01(\tR\x0c\x63ollectionId\x12\x44\n\x0b\x61\x64\x64_authors\x18\x02 \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\naddAuthors\x12J\n\x0eremove_authors\x18\x03 \x03(\x0b\x32#.aruna.api.storage.models.v2.AuthorR\rremoveAuthors\"j\n\x1fUpdateCollectionAuthorsResponse\x12G\n\ncollection\x18\x01 \x01(\x0b\x32\'.aruna.api.storage.models.v2.CollectionR\ncollection2\xaf\x12\n\x11\x43ollectionService\x12\x9f\x01\n\x10\x43reateCollection\x12\x36.aruna.api.storage.services.v2.CreateCollectionRequest\x1a\x37.aruna.api.storage.services.v2.CreateCollectionResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v2/collections:\x01*\x12\xa3\x01\n\rGetCollection\x12\x33.aruna.api.storage.services.v2.GetCollectionRequest\x1a\x34.aruna.api.storage.services.v2.GetCollectionResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v2/collections/{collection_id}\x12\x96\x01\n\x0eGetCollections\x12\x34.aruna.api.storage.services.v2.GetCollectionsRequest\x1a\x35.aruna.api.storage.services.v2.GetCollectionsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v2/collections\x12\xac\x01\n\x10\x44\x65leteCollection\x12\x36.aruna.api.storage.services.v2.DeleteCollectionRequest\x1a\x37.aruna.api.storage.services.v2.DeleteCollectionResponse\"\'\x82\xd3\xe4\x93\x02!*\x1f/v2/collections/{collection_id}\x12\xc0\x01\n\x14UpdateCollectionName\x12:.aruna.api.storage.services.v2.UpdateCollectionNameRequest\x1a;.aruna.api.storage.services.v2.UpdateCollectionNameResponse\"/\x82\xd3\xe4\x93\x02)2$/v2/collections/{collection_id}/name:\x01*\x12\xdc\x01\n\x1bUpdateCollectionDescription\x12\x41.aruna.api.storage.services.v2.UpdateCollectionDescriptionRequest\x1a\x42.aruna.api.storage.services.v2.UpdateCollectionDescriptionResponse\"6\x82\xd3\xe4\x93\x02\x30\x32+/v2/collections/{collection_id}/description:\x01*\x12\xd5\x01\n\x19UpdateCollectionKeyValues\x12?.aruna.api.storage.services.v2.UpdateCollectionKeyValuesRequest\x1a@.aruna.api.storage.services.v2.UpdateCollectionKeyValuesResponse\"5\x82\xd3\xe4\x93\x02/2*/v2/collections/{collection_id}/key_values:\x01*\x12\xd5\x01\n\x19UpdateCollectionDataClass\x12?.aruna.api.storage.services.v2.UpdateCollectionDataClassRequest\x1a@.aruna.api.storage.services.v2.UpdateCollectionDataClassResponse\"5\x82\xd3\xe4\x93\x02/2*/v2/collections/{collection_id}/data_class:\x01*\x12\xbe\x01\n\x12SnapshotCollection\x12\x38.aruna.api.storage.services.v2.SnapshotCollectionRequest\x1a\x39.aruna.api.storage.services.v2.SnapshotCollectionResponse\"3\x82\xd3\xe4\x93\x02-\"(/v2/collections/{collection_id}/snapshot:\x01*\x12\xd0\x01\n\x18UpdateCollectionLicenses\x12>.aruna.api.storage.services.v2.UpdateCollectionLicensesRequest\x1a?.aruna.api.storage.services.v2.UpdateCollectionLicensesResponse\"3\x82\xd3\xe4\x93\x02-2(/v2/collections/{collection_id}/licenses:\x01*\x12\xc4\x01\n\x15UpdateCollectionTitle\x12;.aruna.api.storage.services.v2.UpdateCollectionTitleRequest\x1a<.aruna.api.storage.services.v2.UpdateCollectionTitleResponse\"0\x82\xd3\xe4\x93\x02*2%/v2/collections/{collection_id}/title:\x01*\x12\xcc\x01\n\x17UpdateCollectionAuthors\x12=.aruna.api.storage.services.v2.UpdateCollectionAuthorsRequest\x1a>.aruna.api.storage.services.v2.UpdateCollectionAuthorsResponse\"2\x82\xd3\xe4\x93\x02,2\'/v2/collections/{collection_id}/authors:\x01*\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x96\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x11\x43ollectionServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.collection_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\021CollectionServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_COLLECTIONSERVICE']._loaded_options = None
  _globals['_COLLECTIONSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_COLLECTIONSERVICE'].methods_by_name['CreateCollection']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['CreateCollection']._serialized_options = b'\202\323\344\223\002\024\"\017/v2/collections:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['GetCollection']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['GetCollection']._serialized_options = b'\202\323\344\223\002!\022\037/v2/collections/{collection_id}'
  _globals['_COLLECTIONSERVICE'].methods_by_name['GetCollections']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['GetCollections']._serialized_options = b'\202\323\344\223\002\021\022\017/v2/collections'
  _globals['_COLLECTIONSERVICE'].methods_by_name['DeleteCollection']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['DeleteCollection']._serialized_options = b'\202\323\344\223\002!*\037/v2/collections/{collection_id}'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionName']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionName']._serialized_options = b'\202\323\344\223\002)2$/v2/collections/{collection_id}/name:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionDescription']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionDescription']._serialized_options = b'\202\323\344\223\00202+/v2/collections/{collection_id}/description:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionKeyValues']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionKeyValues']._serialized_options = b'\202\323\344\223\002/2*/v2/collections/{collection_id}/key_values:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionDataClass']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionDataClass']._serialized_options = b'\202\323\344\223\002/2*/v2/collections/{collection_id}/data_class:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['SnapshotCollection']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['SnapshotCollection']._serialized_options = b'\202\323\344\223\002-\"(/v2/collections/{collection_id}/snapshot:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionLicenses']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionLicenses']._serialized_options = b'\202\323\344\223\002-2(/v2/collections/{collection_id}/licenses:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionTitle']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionTitle']._serialized_options = b'\202\323\344\223\002*2%/v2/collections/{collection_id}/title:\001*'
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionAuthors']._loaded_options = None
  _globals['_COLLECTIONSERVICE'].methods_by_name['UpdateCollectionAuthors']._serialized_options = b'\202\323\344\223\002,2\'/v2/collections/{collection_id}/authors:\001*'
  _globals['_CREATECOLLECTIONREQUEST']._serialized_start=191
  _globals['_CREATECOLLECTIONREQUEST']._serialized_end=779
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_start=781
  _globals['_CREATECOLLECTIONRESPONSE']._serialized_end=880
  _globals['_GETCOLLECTIONREQUEST']._serialized_start=882
  _globals['_GETCOLLECTIONREQUEST']._serialized_end=941
  _globals['_GETCOLLECTIONRESPONSE']._serialized_start=943
  _globals['_GETCOLLECTIONRESPONSE']._serialized_end=1039
  _globals['_GETCOLLECTIONSREQUEST']._serialized_start=1041
  _globals['_GETCOLLECTIONSREQUEST']._serialized_end=1103
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_start=1105
  _globals['_GETCOLLECTIONSRESPONSE']._serialized_end=1204
  _globals['_DELETECOLLECTIONREQUEST']._serialized_start=1206
  _globals['_DELETECOLLECTIONREQUEST']._serialized_end=1268
  _globals['_DELETECOLLECTIONRESPONSE']._serialized_start=1270
  _globals['_DELETECOLLECTIONRESPONSE']._serialized_end=1296
  _globals['_UPDATECOLLECTIONNAMEREQUEST']._serialized_start=1298
  _globals['_UPDATECOLLECTIONNAMEREQUEST']._serialized_end=1384
  _globals['_UPDATECOLLECTIONNAMERESPONSE']._serialized_start=1386
  _globals['_UPDATECOLLECTIONNAMERESPONSE']._serialized_end=1489
  _globals['_UPDATECOLLECTIONDESCRIPTIONREQUEST']._serialized_start=1491
  _globals['_UPDATECOLLECTIONDESCRIPTIONREQUEST']._serialized_end=1598
  _globals['_UPDATECOLLECTIONDESCRIPTIONRESPONSE']._serialized_start=1600
  _globals['_UPDATECOLLECTIONDESCRIPTIONRESPONSE']._serialized_end=1710
  _globals['_UPDATECOLLECTIONKEYVALUESREQUEST']._serialized_start=1713
  _globals['_UPDATECOLLECTIONKEYVALUESREQUEST']._serialized_end=1944
  _globals['_UPDATECOLLECTIONKEYVALUESRESPONSE']._serialized_start=1946
  _globals['_UPDATECOLLECTIONKEYVALUESRESPONSE']._serialized_end=2054
  _globals['_UPDATECOLLECTIONDATACLASSREQUEST']._serialized_start=2057
  _globals['_UPDATECOLLECTIONDATACLASSREQUEST']._serialized_end=2199
  _globals['_UPDATECOLLECTIONDATACLASSRESPONSE']._serialized_start=2201
  _globals['_UPDATECOLLECTIONDATACLASSRESPONSE']._serialized_end=2309
  _globals['_SNAPSHOTCOLLECTIONREQUEST']._serialized_start=2311
  _globals['_SNAPSHOTCOLLECTIONREQUEST']._serialized_end=2375
  _globals['_SNAPSHOTCOLLECTIONRESPONSE']._serialized_start=2377
  _globals['_SNAPSHOTCOLLECTIONRESPONSE']._serialized_end=2478
  _globals['_UPDATECOLLECTIONLICENSESREQUEST']._serialized_start=2481
  _globals['_UPDATECOLLECTIONLICENSESREQUEST']._serialized_end=2658
  _globals['_UPDATECOLLECTIONLICENSESRESPONSE']._serialized_start=2660
  _globals['_UPDATECOLLECTIONLICENSESRESPONSE']._serialized_end=2767
  _globals['_UPDATECOLLECTIONTITLEREQUEST']._serialized_start=2769
  _globals['_UPDATECOLLECTIONTITLEREQUEST']._serialized_end=2858
  _globals['_UPDATECOLLECTIONTITLERESPONSE']._serialized_start=2860
  _globals['_UPDATECOLLECTIONTITLERESPONSE']._serialized_end=2964
  _globals['_UPDATECOLLECTIONAUTHORSREQUEST']._serialized_start=2967
  _globals['_UPDATECOLLECTIONAUTHORSREQUEST']._serialized_end=3182
  _globals['_UPDATECOLLECTIONAUTHORSRESPONSE']._serialized_start=3184
  _globals['_UPDATECOLLECTIONAUTHORSRESPONSE']._serialized_end=3290
  _globals['_COLLECTIONSERVICE']._serialized_start=3293
  _globals['_COLLECTIONSERVICE']._serialized_end=5644
# @@protoc_insertion_point(module_scope)
