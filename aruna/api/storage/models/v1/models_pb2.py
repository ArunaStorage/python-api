# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/models/v1/models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(aruna/api/storage/models/v1/models.proto\x12\x1b\x61runa.api.storage.models.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"2\n\x08KeyValue\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"?\n\rLabelOntology\x12.\n\x13required_label_keys\x18\x01 \x03(\tR\x11requiredLabelKeys\"8\n\x05Stats\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\x12\x19\n\x08\x61\x63\x63_size\x18\x02 \x01(\x03R\x07\x61\x63\x63Size\"\xc5\x01\n\x0f\x43ollectionStats\x12\x45\n\x0cobject_stats\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v1.StatsR\x0bobjectStats\x12,\n\x12object_group_count\x18\x02 \x01(\x03R\x10objectGroupCount\x12=\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\"\x98\x01\n\x10ObjectGroupStats\x12\x45\n\x0cobject_stats\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v1.StatsR\x0bobjectStats\x12=\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\"K\n\x07Version\x12\x14\n\x05major\x18\x01 \x01(\x05R\x05major\x12\x14\n\x05minor\x18\x02 \x01(\x05R\x05minor\x12\x14\n\x05patch\x18\x03 \x01(\x05R\x05patch\"X\n\x04Hash\x12<\n\x03\x61lg\x18\x01 \x01(\x0e\x32*.aruna.api.storage.models.v1.HashalgorithmR\x03\x61lg\x12\x12\n\x04hash\x18\x02 \x01(\tR\x04hash\"\x1e\n\x06Origin\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02idJ\x04\x08\x01\x10\x02\"r\n\x06Source\x12\x1e\n\nidentifier\x18\x01 \x01(\tR\nidentifier\x12H\n\x0bsource_type\x18\x02 \x01(\x0e\x32\'.aruna.api.storage.models.v1.SourceTypeR\nsourceType\"\xb1\x02\n\x08\x45ndpoint\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x42\n\x07\x65p_type\x18\x02 \x01(\x0e\x32).aruna.api.storage.models.v1.EndpointTypeR\x06\x65pType\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12%\n\x0eproxy_hostname\x18\x04 \x01(\tR\rproxyHostname\x12+\n\x11internal_hostname\x18\x05 \x01(\tR\x10internalHostname\x12-\n\x12\x64ocumentation_path\x18\x06 \x01(\tR\x11\x64ocumentationPath\x12\x1b\n\tis_public\x18\x07 \x01(\x08R\x08isPublic\x12\x1d\n\nis_default\x18\x08 \x01(\x08R\tisDefault\"\x94\x05\n\x06Object\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12=\n\x06labels\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12\x34\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x1f\n\x0b\x63ontent_len\x18\x07 \x01(\x03R\ncontentLen\x12;\n\x06status\x18\x08 \x01(\x0e\x32#.aruna.api.storage.models.v1.StatusR\x06status\x12;\n\x06origin\x18\t \x01(\x0b\x32#.aruna.api.storage.models.v1.OriginR\x06origin\x12\x45\n\ndata_class\x18\n \x01(\x0e\x32&.aruna.api.storage.models.v1.DataClassR\tdataClass\x12\x35\n\x04hash\x18\x0b \x01(\x0b\x32!.aruna.api.storage.models.v1.HashR\x04hash\x12\x1d\n\nrev_number\x18\x0c \x01(\x03R\trevNumber\x12;\n\x06source\x18\r \x01(\x0b\x32#.aruna.api.storage.models.v1.SourceR\x06source\x12\x16\n\x06latest\x18\x0e \x01(\x08R\x06latest\x12\x1f\n\x0b\x61uto_update\x18\x0f \x01(\x08R\nautoUpdate\"H\n\x07Objects\x12=\n\x07objects\x18\x01 \x03(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x07objects\"\xba\x03\n\x0bObjectGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x06 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x07 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12=\n\x07objects\x18\x08 \x03(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x07objects\x12\x46\n\x0cmeta_objects\x18\t \x03(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x0bmetaObjects\x12\x43\n\x05stats\x18\n \x01(\x0b\x32-.aruna.api.storage.models.v1.ObjectGroupStatsR\x05stats\x12\x1d\n\nrev_number\x18\x0b \x01(\x03R\trevNumber\"]\n\x0cObjectGroups\x12M\n\robject_groups\x18\x01 \x03(\x0b\x32(.aruna.api.storage.models.v1.ObjectGroupR\x0cobjectGroups\"\xbb\x02\n\x13ObjectGroupOverview\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x06 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x07 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12\x43\n\x05stats\x18\x08 \x01(\x0b\x32-.aruna.api.storage.models.v1.ObjectGroupStatsR\x05stats\x12\x1d\n\nrev_number\x18\t \x01(\x03R\trevNumber\"~\n\x14ObjectGroupOverviews\x12\x66\n\x16object_group_overviews\x18\x01 \x03(\x0b\x32\x30.aruna.api.storage.models.v1.ObjectGroupOverviewR\x14objectGroupOverviews\"\x80\x03\n\x11ObjectGroupWithID\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x06 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x07 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12\x1d\n\nobject_ids\x18\x08 \x03(\tR\tobjectIds\x12&\n\x0fmeta_object_ids\x18\t \x03(\tR\rmetaObjectIds\x12\x43\n\x05stats\x18\n \x01(\x0b\x32-.aruna.api.storage.models.v1.ObjectGroupStatsR\x05stats\x12\x1d\n\nrev_number\x18\x0b \x01(\x03R\trevNumber\"w\n\x12ObjectGroupWithIDs\x12\x61\n\x15object_group_with_ids\x18\x01 \x03(\x0b\x32..aruna.api.storage.models.v1.ObjectGroupWithIDR\x12objectGroupWithIds\"\x8b\x06\n\nCollection\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12Q\n\x0elabel_ontology\x18\x06 \x01(\x0b\x32*.aruna.api.storage.models.v1.LabelOntologyR\rlabelOntology\x12\x34\n\x07\x63reated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12=\n\x07objects\x18\x08 \x03(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x07objects\x12K\n\x0especifications\x18\t \x03(\x0b\x32#.aruna.api.storage.models.v1.ObjectR\x0especifications\x12M\n\robject_groups\x18\n \x03(\x0b\x32(.aruna.api.storage.models.v1.ObjectGroupR\x0cobjectGroups\x12Q\n\x10semantic_version\x18\x0c \x01(\x0b\x32$.aruna.api.storage.models.v1.VersionH\x00R\x0fsemanticVersion\x12\x18\n\x06latest\x18\r \x01(\x08H\x00R\x06latest\x12\x42\n\x05stats\x18\x0e \x01(\x0b\x32,.aruna.api.storage.models.v1.CollectionStatsR\x05stats\x12\x1b\n\tis_public\x18\x0f \x01(\x08R\x08isPublicB\t\n\x07version\"X\n\x0b\x43ollections\x12I\n\x0b\x63ollections\x18\x01 \x03(\x0b\x32\'.aruna.api.storage.models.v1.CollectionR\x0b\x63ollections\"\xb8\x04\n\x12\x43ollectionOverview\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12Q\n\x0elabel_ontology\x18\x06 \x01(\x0b\x32*.aruna.api.storage.models.v1.LabelOntologyR\rlabelOntology\x12\x34\n\x07\x63reated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12Q\n\x10semantic_version\x18\x0c \x01(\x0b\x32$.aruna.api.storage.models.v1.VersionH\x00R\x0fsemanticVersion\x12\x18\n\x06latest\x18\r \x01(\x08H\x00R\x06latest\x12\x42\n\x05stats\x18\x0e \x01(\x0b\x32,.aruna.api.storage.models.v1.CollectionStatsR\x05stats\x12\x1b\n\tis_public\x18\x0f \x01(\x08R\x08isPublicB\t\n\x07version\"y\n\x13\x43ollectionOverviews\x12\x62\n\x14\x63ollection_overviews\x18\x01 \x03(\x0b\x32/.aruna.api.storage.models.v1.CollectionOverviewR\x13\x63ollectionOverviews\"\x9d\x05\n\x10\x43ollectionWithID\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12=\n\x06labels\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x06labels\x12;\n\x05hooks\x18\x05 \x03(\x0b\x32%.aruna.api.storage.models.v1.KeyValueR\x05hooks\x12Q\n\x0elabel_ontology\x18\x06 \x01(\x0b\x32*.aruna.api.storage.models.v1.LabelOntologyR\rlabelOntology\x12\x34\n\x07\x63reated\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x18\n\x07objects\x18\x08 \x03(\tR\x07objects\x12&\n\x0especifications\x18\t \x03(\tR\x0especifications\x12#\n\robject_groups\x18\n \x03(\tR\x0cobjectGroups\x12Q\n\x10semantic_version\x18\x0c \x01(\x0b\x32$.aruna.api.storage.models.v1.VersionH\x00R\x0fsemanticVersion\x12\x18\n\x06latest\x18\r \x01(\x08H\x00R\x06latest\x12\x42\n\x05stats\x18\x0e \x01(\x0b\x32,.aruna.api.storage.models.v1.CollectionStatsR\x05stats\x12\x1b\n\tis_public\x18\x0f \x01(\x08R\x08isPublicB\t\n\x07version\"r\n\x11\x43ollectionWithIDs\x12]\n\x13\x63ollection_with_ids\x18\x01 \x03(\x0b\x32-.aruna.api.storage.models.v1.CollectionWithIDR\x11\x63ollectionWithIds*\xb7\x01\n\x0cResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15RESOURCE_TYPE_PROJECT\x10\x01\x12\x1c\n\x18RESOURCE_TYPE_COLLECTION\x10\x02\x12\x1e\n\x1aRESOURCE_TYPE_OBJECT_GROUP\x10\x03\x12\x18\n\x14RESOURCE_TYPE_OBJECT\x10\x04\x12\x15\n\x11RESOURCE_TYPE_ALL\x10\x05*\xbb\x01\n\x0eResourceAction\x12\x1f\n\x1bRESOURCE_ACTION_UNSPECIFIED\x10\x00\x12\x1a\n\x16RESOURCE_ACTION_CREATE\x10\x01\x12\x1a\n\x16RESOURCE_ACTION_APPEND\x10\x02\x12\x1a\n\x16RESOURCE_ACTION_UPDATE\x10\x03\x12\x18\n\x14RESOURCE_ACTION_READ\x10\x04\x12\x1a\n\x16RESOURCE_ACTION_DELETE\x10\x05*\x8b\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x17\n\x13STATUS_INITIALIZING\x10\x01\x12\x14\n\x10STATUS_AVAILABLE\x10\x02\x12\x16\n\x12STATUS_UNAVAILABLE\x10\x03\x12\x10\n\x0cSTATUS_ERROR\x10\x04\x12\x10\n\x0cSTATUS_TRASH\x10\x05*k\n\rHashalgorithm\x12\x1d\n\x19HASHALGORITHM_UNSPECIFIED\x10\x00\x12\x15\n\x11HASHALGORITHM_MD5\x10\x01\x12\x18\n\x14HASHALGORITHM_SHA256\x10\x03\"\x04\x08\x02\x10\x02\"\x04\x08\x04\x10\x07*\x8d\x01\n\tDataClass\x12\x1a\n\x16\x44\x41TA_CLASS_UNSPECIFIED\x10\x00\x12\x15\n\x11\x44\x41TA_CLASS_PUBLIC\x10\x01\x12\x16\n\x12\x44\x41TA_CLASS_PRIVATE\x10\x02\x12\x1b\n\x17\x44\x41TA_CLASS_CONFIDENTIAL\x10\x03\x12\x18\n\x14\x44\x41TA_CLASS_PROTECTED\x10\x04*S\n\nSourceType\x12\x1b\n\x17SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSOURCE_TYPE_URL\x10\x01\x12\x13\n\x0fSOURCE_TYPE_DOI\x10\x02*[\n\x0c\x45ndpointType\x12\x1d\n\x19\x45NDPOINT_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x45NDPOINT_TYPE_S3\x10\x01\x12\x16\n\x12\x45NDPOINT_TYPE_FILE\x10\x02\x42<Z:github.com/ArunaStorage/go-api/aruna/api/storage/models/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.models.v1.models_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z:github.com/ArunaStorage/go-api/aruna/api/storage/models/v1'
  _RESOURCETYPE._serialized_start=5845
  _RESOURCETYPE._serialized_end=6028
  _RESOURCEACTION._serialized_start=6031
  _RESOURCEACTION._serialized_end=6218
  _STATUS._serialized_start=6221
  _STATUS._serialized_end=6360
  _HASHALGORITHM._serialized_start=6362
  _HASHALGORITHM._serialized_end=6469
  _DATACLASS._serialized_start=6472
  _DATACLASS._serialized_end=6613
  _SOURCETYPE._serialized_start=6615
  _SOURCETYPE._serialized_end=6698
  _ENDPOINTTYPE._serialized_start=6700
  _ENDPOINTTYPE._serialized_end=6791
  _KEYVALUE._serialized_start=106
  _KEYVALUE._serialized_end=156
  _LABELONTOLOGY._serialized_start=158
  _LABELONTOLOGY._serialized_end=221
  _STATS._serialized_start=223
  _STATS._serialized_end=279
  _COLLECTIONSTATS._serialized_start=282
  _COLLECTIONSTATS._serialized_end=479
  _OBJECTGROUPSTATS._serialized_start=482
  _OBJECTGROUPSTATS._serialized_end=634
  _VERSION._serialized_start=636
  _VERSION._serialized_end=711
  _HASH._serialized_start=713
  _HASH._serialized_end=801
  _ORIGIN._serialized_start=803
  _ORIGIN._serialized_end=833
  _SOURCE._serialized_start=835
  _SOURCE._serialized_end=949
  _ENDPOINT._serialized_start=952
  _ENDPOINT._serialized_end=1257
  _OBJECT._serialized_start=1260
  _OBJECT._serialized_end=1920
  _OBJECTS._serialized_start=1922
  _OBJECTS._serialized_end=1994
  _OBJECTGROUP._serialized_start=1997
  _OBJECTGROUP._serialized_end=2439
  _OBJECTGROUPS._serialized_start=2441
  _OBJECTGROUPS._serialized_end=2534
  _OBJECTGROUPOVERVIEW._serialized_start=2537
  _OBJECTGROUPOVERVIEW._serialized_end=2852
  _OBJECTGROUPOVERVIEWS._serialized_start=2854
  _OBJECTGROUPOVERVIEWS._serialized_end=2980
  _OBJECTGROUPWITHID._serialized_start=2983
  _OBJECTGROUPWITHID._serialized_end=3367
  _OBJECTGROUPWITHIDS._serialized_start=3369
  _OBJECTGROUPWITHIDS._serialized_end=3488
  _COLLECTION._serialized_start=3491
  _COLLECTION._serialized_end=4270
  _COLLECTIONS._serialized_start=4272
  _COLLECTIONS._serialized_end=4360
  _COLLECTIONOVERVIEW._serialized_start=4363
  _COLLECTIONOVERVIEW._serialized_end=4931
  _COLLECTIONOVERVIEWS._serialized_start=4933
  _COLLECTIONOVERVIEWS._serialized_end=5054
  _COLLECTIONWITHID._serialized_start=5057
  _COLLECTIONWITHID._serialized_end=5726
  _COLLECTIONWITHIDS._serialized_start=5728
  _COLLECTIONWITHIDS._serialized_end=5842
# @@protoc_insertion_point(module_scope)
