# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/models/v1/common_models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3sciobjsdb/api/storage/models/v1/common_models.proto\x12\x1fsciobjsdb.api.storage.models.v1\"\xe0\x01\n\x08Location\x12Z\n\x0fobject_location\x18\x01 \x01(\x0b\x32/.sciobjsdb.api.storage.models.v1.ObjectLocationH\x00R\x0eobjectLocation\x12l\n\x15object_index_location\x18\x02 \x01(\x0b\x32\x36.sciobjsdb.api.storage.models.v1.IndexedObjectLocationH\x00R\x13objectIndexLocationB\n\n\x08location\"L\n\x0eObjectLocation\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\"\x91\x01\n\x15IndexedObjectLocation\x12\x16\n\x06\x62ucket\x18\x01 \x01(\tR\x06\x62ucket\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x12<\n\x05index\x18\x04 \x01(\x0b\x32&.sciobjsdb.api.storage.models.v1.IndexR\x05index\"A\n\x05Index\x12\x1d\n\nstart_byte\x18\x01 \x01(\x03R\tstartByte\x12\x19\n\x08\x65nd_byte\x18\x02 \x01(\x03R\x07\x65ndByte\"\xc1\x02\n\x06Origin\x12\x12\n\x04link\x18\x01 \x01(\tR\x04link\x12Z\n\x0fobject_location\x18\x02 \x01(\x0b\x32/.sciobjsdb.api.storage.models.v1.ObjectLocationH\x00R\x0eobjectLocation\x12S\n\x0borigin_type\x18\x03 \x01(\x0e\x32\x32.sciobjsdb.api.storage.models.v1.Origin.OriginTypeR\noriginType\"f\n\nOriginType\x12\x1b\n\x17ORIGIN_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aORIGIN_TYPE_OBJECT_STORAGE\x10\x01\x12\x1b\n\x17ORIGIN_TYPE_ORIGIN_LINK\x10\x02\x42\n\n\x08location\"\xc5\x02\n\x07Version\x12\x14\n\x05major\x18\x01 \x01(\x05R\x05major\x12\x14\n\x05minor\x18\x02 \x01(\x05R\x05minor\x12\x14\n\x05patch\x18\x03 \x01(\x05R\x05patch\x12\x1a\n\x08revision\x18\x04 \x01(\x05R\x08revision\x12K\n\x05stage\x18\x05 \x01(\x0e\x32\x35.sciobjsdb.api.storage.models.v1.Version.VersionStageR\x05stage\"\x8e\x01\n\x0cVersionStage\x12\x1d\n\x19VERSION_STAGE_UNSPECIFIED\x10\x00\x12\x18\n\x14VERSION_STAGE_STABLE\x10\x01\x12\x14\n\x10VERSION_STAGE_RC\x10\x02\x12\x16\n\x12VERSION_STAGE_BETA\x10\x03\x12\x17\n\x13VERSION_STAGE_ALPHA\x10\x04\"/\n\x05Label\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\x14\n\x02ID\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\xf1\x01\n\x13UpdateFieldsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x81\x01\n\x15updated_string_fields\x18\x02 \x03(\x0b\x32M.sciobjsdb.api.storage.models.v1.UpdateFieldsRequest.UpdatedStringFieldsEntryR\x13updatedStringFields\x1a\x46\n\x18UpdatedStringFieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xa6\x01\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12>\n\x06rights\x18\x02 \x03(\x0e\x32&.sciobjsdb.api.storage.models.v1.RightR\x06rights\x12\x45\n\x08resource\x18\x03 \x01(\x0e\x32).sciobjsdb.api.storage.models.v1.ResourceR\x08resource\"\xa9\x01\n\x08Metadata\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12>\n\x06labels\x18\x02 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12\x1a\n\x08metadata\x18\x03 \x01(\x0cR\x08metadata\x12%\n\rsimple_schema\x18\x04 \x01(\tH\x00R\x0csimpleSchemaB\x08\n\x06schema\"?\n\nVersionTag\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nversion_id\x18\x02 \x01(\tR\tversionId\"\x8f\x01\n\x08\x41PIToken\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\x12>\n\x06rights\x18\x03 \x03(\x0e\x32&.sciobjsdb.api.storage.models.v1.RightR\x06rights\x12\x1d\n\nproject_id\x18\x04 \x01(\tR\tprojectId\"\x07\n\x05\x45mpty\"G\n\x0bPageRequest\x12\x1b\n\tlast_uuid\x18\x01 \x01(\tR\x08lastUuid\x12\x1b\n\tpage_size\x18\x02 \x01(\x04R\x08pageSize*\x8c\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x15\n\x11STATUS_INITIATING\x10\x01\x12\x14\n\x10STATUS_AVAILABLE\x10\x02\x12\x13\n\x0fSTATUS_UPDATING\x10\x03\x12\x13\n\x0fSTATUS_ARCHIVED\x10\x04\x12\x13\n\x0fSTATUS_DELETING\x10\x05*?\n\x05Right\x12\x15\n\x11RIGHT_UNSPECIFIED\x10\x00\x12\x0e\n\nRIGHT_READ\x10\x01\x12\x0f\n\x0bRIGHT_WRITE\x10\x02*\xc2\x01\n\x08Resource\x12\x18\n\x14RESOURCE_UNSPECIFIED\x10\x00\x12\x14\n\x10RESOURCE_PROJECT\x10\x01\x12\x14\n\x10RESOURCE_DATASET\x10\x02\x12\x1c\n\x18RESOURCE_DATASET_VERSION\x10\x03\x12\x13\n\x0fRESOURCE_OBJECT\x10\x04\x12\x19\n\x15RESOURCE_OBJECT_GROUP\x10\x05\x12\"\n\x1eRESOURCE_OBJECT_GROUP_REVISION\x10\x06\x42\x9a\x01\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\x0c\x43ommonModelsP\x01ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1b\x06proto3')

_STATUS = DESCRIPTOR.enum_types_by_name['Status']
Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_RIGHT = DESCRIPTOR.enum_types_by_name['Right']
Right = enum_type_wrapper.EnumTypeWrapper(_RIGHT)
_RESOURCE = DESCRIPTOR.enum_types_by_name['Resource']
Resource = enum_type_wrapper.EnumTypeWrapper(_RESOURCE)
STATUS_UNSPECIFIED = 0
STATUS_INITIATING = 1
STATUS_AVAILABLE = 2
STATUS_UPDATING = 3
STATUS_ARCHIVED = 4
STATUS_DELETING = 5
RIGHT_UNSPECIFIED = 0
RIGHT_READ = 1
RIGHT_WRITE = 2
RESOURCE_UNSPECIFIED = 0
RESOURCE_PROJECT = 1
RESOURCE_DATASET = 2
RESOURCE_DATASET_VERSION = 3
RESOURCE_OBJECT = 4
RESOURCE_OBJECT_GROUP = 5
RESOURCE_OBJECT_GROUP_REVISION = 6


_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_OBJECTLOCATION = DESCRIPTOR.message_types_by_name['ObjectLocation']
_INDEXEDOBJECTLOCATION = DESCRIPTOR.message_types_by_name['IndexedObjectLocation']
_INDEX = DESCRIPTOR.message_types_by_name['Index']
_ORIGIN = DESCRIPTOR.message_types_by_name['Origin']
_VERSION = DESCRIPTOR.message_types_by_name['Version']
_LABEL = DESCRIPTOR.message_types_by_name['Label']
_ID = DESCRIPTOR.message_types_by_name['ID']
_UPDATEFIELDSREQUEST = DESCRIPTOR.message_types_by_name['UpdateFieldsRequest']
_UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY = _UPDATEFIELDSREQUEST.nested_types_by_name['UpdatedStringFieldsEntry']
_USER = DESCRIPTOR.message_types_by_name['User']
_METADATA = DESCRIPTOR.message_types_by_name['Metadata']
_VERSIONTAG = DESCRIPTOR.message_types_by_name['VersionTag']
_APITOKEN = DESCRIPTOR.message_types_by_name['APIToken']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_PAGEREQUEST = DESCRIPTOR.message_types_by_name['PageRequest']
_ORIGIN_ORIGINTYPE = _ORIGIN.enum_types_by_name['OriginType']
_VERSION_VERSIONSTAGE = _VERSION.enum_types_by_name['VersionStage']
Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Location)
  })
_sym_db.RegisterMessage(Location)

ObjectLocation = _reflection.GeneratedProtocolMessageType('ObjectLocation', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTLOCATION,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.ObjectLocation)
  })
_sym_db.RegisterMessage(ObjectLocation)

IndexedObjectLocation = _reflection.GeneratedProtocolMessageType('IndexedObjectLocation', (_message.Message,), {
  'DESCRIPTOR' : _INDEXEDOBJECTLOCATION,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.IndexedObjectLocation)
  })
_sym_db.RegisterMessage(IndexedObjectLocation)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {
  'DESCRIPTOR' : _INDEX,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Index)
  })
_sym_db.RegisterMessage(Index)

Origin = _reflection.GeneratedProtocolMessageType('Origin', (_message.Message,), {
  'DESCRIPTOR' : _ORIGIN,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Origin)
  })
_sym_db.RegisterMessage(Origin)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), {
  'DESCRIPTOR' : _VERSION,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Version)
  })
_sym_db.RegisterMessage(Version)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Label)
  })
_sym_db.RegisterMessage(Label)

ID = _reflection.GeneratedProtocolMessageType('ID', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.ID)
  })
_sym_db.RegisterMessage(ID)

UpdateFieldsRequest = _reflection.GeneratedProtocolMessageType('UpdateFieldsRequest', (_message.Message,), {

  'UpdatedStringFieldsEntry' : _reflection.GeneratedProtocolMessageType('UpdatedStringFieldsEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY,
    '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
    # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.UpdateFieldsRequest.UpdatedStringFieldsEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEFIELDSREQUEST,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.UpdateFieldsRequest)
  })
_sym_db.RegisterMessage(UpdateFieldsRequest)
_sym_db.RegisterMessage(UpdateFieldsRequest.UpdatedStringFieldsEntry)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.User)
  })
_sym_db.RegisterMessage(User)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), {
  'DESCRIPTOR' : _METADATA,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Metadata)
  })
_sym_db.RegisterMessage(Metadata)

VersionTag = _reflection.GeneratedProtocolMessageType('VersionTag', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONTAG,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.VersionTag)
  })
_sym_db.RegisterMessage(VersionTag)

APIToken = _reflection.GeneratedProtocolMessageType('APIToken', (_message.Message,), {
  'DESCRIPTOR' : _APITOKEN,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.APIToken)
  })
_sym_db.RegisterMessage(APIToken)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.Empty)
  })
_sym_db.RegisterMessage(Empty)

PageRequest = _reflection.GeneratedProtocolMessageType('PageRequest', (_message.Message,), {
  'DESCRIPTOR' : _PAGEREQUEST,
  '__module__' : 'sciobjsdb.api.storage.models.v1.common_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.models.v1.PageRequest)
  })
_sym_db.RegisterMessage(PageRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\014CommonModelsP\001ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1'
  _UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY._options = None
  _UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY._serialized_options = b'8\001'
  _STATUS._serialized_start=2210
  _STATUS._serialized_end=2350
  _RIGHT._serialized_start=2352
  _RIGHT._serialized_end=2415
  _RESOURCE._serialized_start=2418
  _RESOURCE._serialized_end=2612
  _LOCATION._serialized_start=89
  _LOCATION._serialized_end=313
  _OBJECTLOCATION._serialized_start=315
  _OBJECTLOCATION._serialized_end=391
  _INDEXEDOBJECTLOCATION._serialized_start=394
  _INDEXEDOBJECTLOCATION._serialized_end=539
  _INDEX._serialized_start=541
  _INDEX._serialized_end=606
  _ORIGIN._serialized_start=609
  _ORIGIN._serialized_end=930
  _ORIGIN_ORIGINTYPE._serialized_start=816
  _ORIGIN_ORIGINTYPE._serialized_end=918
  _VERSION._serialized_start=933
  _VERSION._serialized_end=1258
  _VERSION_VERSIONSTAGE._serialized_start=1116
  _VERSION_VERSIONSTAGE._serialized_end=1258
  _LABEL._serialized_start=1260
  _LABEL._serialized_end=1307
  _ID._serialized_start=1309
  _ID._serialized_end=1329
  _UPDATEFIELDSREQUEST._serialized_start=1332
  _UPDATEFIELDSREQUEST._serialized_end=1573
  _UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY._serialized_start=1503
  _UPDATEFIELDSREQUEST_UPDATEDSTRINGFIELDSENTRY._serialized_end=1573
  _USER._serialized_start=1576
  _USER._serialized_end=1742
  _METADATA._serialized_start=1745
  _METADATA._serialized_end=1914
  _VERSIONTAG._serialized_start=1916
  _VERSIONTAG._serialized_end=1979
  _APITOKEN._serialized_start=1982
  _APITOKEN._serialized_end=2125
  _EMPTY._serialized_start=2127
  _EMPTY._serialized_end=2134
  _PAGEREQUEST._serialized_start=2136
  _PAGEREQUEST._serialized_end=2207
# @@protoc_insertion_point(module_scope)