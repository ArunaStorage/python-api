# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/hooks/services/v2/hooks_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/aruna/api/hooks/services/v2/hooks_service.proto\x12\x1b\x61runa.api.hooks.services.v2\x1a\x1cgoogle/api/annotations.proto\x1a(aruna/api/storage/models/v2/models.proto\"~\n\x07Trigger\x12K\n\x0ctrigger_type\x18\x01 \x01(\x0e\x32(.aruna.api.hooks.services.v2.TriggerTypeR\x0btriggerType\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value\"\xeb\x01\n\x0c\x45xternalHook\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12J\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32(.aruna.api.hooks.services.v2.CredentialsR\x0b\x63redentials\x12,\n\x0f\x63ustom_template\x18\x03 \x01(\tH\x00R\x0e\x63ustomTemplate\x88\x01\x01\x12;\n\x06method\x18\x05 \x01(\x0e\x32#.aruna.api.hooks.services.v2.MethodR\x06methodB\x12\n\x10_custom_template\"2\n\x08\x41\x64\x64Label\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"1\n\x07\x41\x64\x64Hook\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\xf6\x01\n\x0cInternalHook\x12\x44\n\tadd_label\x18\x01 \x01(\x0b\x32%.aruna.api.hooks.services.v2.AddLabelH\x00R\x08\x61\x64\x64Label\x12\x41\n\x08\x61\x64\x64_hook\x18\x02 \x01(\x0b\x32$.aruna.api.hooks.services.v2.AddHookH\x00R\x07\x61\x64\x64Hook\x12J\n\x0c\x61\x64\x64_relation\x18\x03 \x01(\x0b\x32%.aruna.api.storage.models.v2.RelationH\x00R\x0b\x61\x64\x64RelationB\x11\n\x0finternal_action\"\xb7\x01\n\x04Hook\x12P\n\rexternal_hook\x18\x01 \x01(\x0b\x32).aruna.api.hooks.services.v2.ExternalHookH\x00R\x0c\x65xternalHook\x12P\n\rinternal_hook\x18\x02 \x01(\x0b\x32).aruna.api.hooks.services.v2.InternalHookH\x00R\x0cinternalHookB\x0b\n\thook_type\"#\n\x0b\x43redentials\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"\xfb\x01\n\x11\x43reateHookRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12>\n\x07trigger\x18\x02 \x01(\x0b\x32$.aruna.api.hooks.services.v2.TriggerR\x07trigger\x12\x35\n\x04hook\x18\x03 \x01(\x0b\x32!.aruna.api.hooks.services.v2.HookR\x04hook\x12\x18\n\x07timeout\x18\x04 \x01(\x04R\x07timeout\x12\x1f\n\x0bproject_ids\x18\x05 \x03(\tR\nprojectIds\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\"-\n\x12\x43reateHookResponse\x12\x17\n\x07hook_id\x18\x01 \x01(\tR\x06hookId\",\n\x11\x44\x65leteHookRequest\x12\x17\n\x07hook_id\x18\x01 \x01(\tR\x06hookId\"\x14\n\x12\x44\x65leteHookResponse\"\x93\x02\n\x13HookCallbackRequest\x12\x43\n\x08\x66inished\x18\x01 \x01(\x0b\x32%.aruna.api.hooks.services.v2.FinishedH\x00R\x08\x66inished\x12:\n\x05\x65rror\x18\x02 \x01(\x0b\x32\".aruna.api.hooks.services.v2.ErrorH\x00R\x05\x65rror\x12\x16\n\x06secret\x18\x03 \x01(\tR\x06secret\x12\x17\n\x07hook_id\x18\x04 \x01(\tR\x06hookId\x12\x1b\n\tobject_id\x18\x05 \x01(\tR\x08objectId\x12#\n\rpubkey_serial\x18\x06 \x01(\x05R\x0cpubkeySerialB\x08\n\x06status\"\xaa\x01\n\x08\x46inished\x12K\n\x0e\x61\x64\x64_key_values\x18\x01 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0c\x61\x64\x64KeyValues\x12Q\n\x11remove_key_values\x18\x02 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0fremoveKeyValues\"\x1d\n\x05\x45rror\x12\x14\n\x05\x65rror\x18\x01 \x01(\tR\x05\x65rror\"\x16\n\x14HookCallbackResponse\"8\n\x17ListProjectHooksRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"0\n\x15ListOwnedHooksRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x8b\x02\n\x08HookInfo\x12\x17\n\x07hook_id\x18\x01 \x01(\tR\x06hookId\x12\x1f\n\x0bproject_ids\x18\x02 \x03(\tR\nprojectIds\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x35\n\x04hook\x18\x05 \x01(\x0b\x32!.aruna.api.hooks.services.v2.HookR\x04hook\x12>\n\x07trigger\x18\x06 \x01(\x0b\x32$.aruna.api.hooks.services.v2.TriggerR\x07trigger\x12\x18\n\x07timeout\x18\x07 \x01(\x04R\x07timeout\"W\n\x18ListProjectHooksResponse\x12;\n\x05infos\x18\x01 \x03(\x0b\x32%.aruna.api.hooks.services.v2.HookInfoR\x05infos\"U\n\x16ListOwnedHooksResponse\x12;\n\x05infos\x18\x01 \x03(\x0b\x32%.aruna.api.hooks.services.v2.HookInfoR\x05infos\"T\n\x18\x41\x64\x64ProjectsToHookRequest\x12\x17\n\x07hook_id\x18\x01 \x01(\tR\x06hookId\x12\x1f\n\x0bproject_ids\x18\x02 \x03(\tR\nprojectIds\"\x1b\n\x19\x41\x64\x64ProjectsToHookResponse*\xd2\x01\n\x0bTriggerType\x12\x1c\n\x18TRIGGER_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17TRIGGER_TYPE_HOOK_ADDED\x10\x01\x12\x1f\n\x1bTRIGGER_TYPE_OBJECT_CREATED\x10\x02\x12\x1c\n\x18TRIGGER_TYPE_LABEL_ADDED\x10\x03\x12#\n\x1fTRIGGER_TYPE_STATIC_LABEL_ADDED\x10\x04\x12$\n TRIGGER_TYPE_HOOK_STATUS_CHANGED\x10\x05*A\n\x06Method\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x0e\n\nMETHOD_PUT\x10\x01\x12\x0f\n\x0bMETHOD_POST\x10\x02\x32\x9d\x07\n\x0cHooksService\x12\x82\x01\n\nCreateHook\x12..aruna.api.hooks.services.v2.CreateHookRequest\x1a/.aruna.api.hooks.services.v2.CreateHookResponse\"\x13\x82\xd3\xe4\x93\x02\r\"\x08/v2/hook:\x01*\x12\xa1\x01\n\x11\x41\x64\x64ProjectsToHook\x12\x35.aruna.api.hooks.services.v2.AddProjectsToHookRequest\x1a\x36.aruna.api.hooks.services.v2.AddProjectsToHookResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v2/hook/{hook_id}:\x01*\x12\xa7\x01\n\x10ListProjectHooks\x12\x34.aruna.api.hooks.services.v2.ListProjectHooksRequest\x1a\x35.aruna.api.hooks.services.v2.ListProjectHooksResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v2/hooks/project/{project_id}\x12\x9c\x01\n\x0eListOwnedHooks\x12\x32.aruna.api.hooks.services.v2.ListOwnedHooksRequest\x1a\x33.aruna.api.hooks.services.v2.ListOwnedHooksResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/hooks/owner/{user_id}\x12\x89\x01\n\nDeleteHook\x12..aruna.api.hooks.services.v2.DeleteHookRequest\x1a/.aruna.api.hooks.services.v2.DeleteHookResponse\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/v2/hook/{hook_id}\x12\x8e\x01\n\x0cHookCallback\x12\x30.aruna.api.hooks.services.v2.HookCallbackRequest\x1a\x31.aruna.api.hooks.services.v2.HookCallbackResponse\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/v2/hook/callbackB\x8e\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x0cHooksServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.hooks.services.v2.hooks_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\014HooksServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v2'
  _globals['_HOOKSSERVICE'].methods_by_name['CreateHook']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['CreateHook']._serialized_options = b'\202\323\344\223\002\r\"\010/v2/hook:\001*'
  _globals['_HOOKSSERVICE'].methods_by_name['AddProjectsToHook']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['AddProjectsToHook']._serialized_options = b'\202\323\344\223\002\027\"\022/v2/hook/{hook_id}:\001*'
  _globals['_HOOKSSERVICE'].methods_by_name['ListProjectHooks']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['ListProjectHooks']._serialized_options = b'\202\323\344\223\002 \022\036/v2/hooks/project/{project_id}'
  _globals['_HOOKSSERVICE'].methods_by_name['ListOwnedHooks']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['ListOwnedHooks']._serialized_options = b'\202\323\344\223\002\033\022\031/v2/hooks/owner/{user_id}'
  _globals['_HOOKSSERVICE'].methods_by_name['DeleteHook']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['DeleteHook']._serialized_options = b'\202\323\344\223\002\024*\022/v2/hook/{hook_id}'
  _globals['_HOOKSSERVICE'].methods_by_name['HookCallback']._options = None
  _globals['_HOOKSSERVICE'].methods_by_name['HookCallback']._serialized_options = b'\202\323\344\223\002\023*\021/v2/hook/callback'
  _globals['_TRIGGERTYPE']._serialized_start=2638
  _globals['_TRIGGERTYPE']._serialized_end=2848
  _globals['_METHOD']._serialized_start=2850
  _globals['_METHOD']._serialized_end=2915
  _globals['_TRIGGER']._serialized_start=152
  _globals['_TRIGGER']._serialized_end=278
  _globals['_EXTERNALHOOK']._serialized_start=281
  _globals['_EXTERNALHOOK']._serialized_end=516
  _globals['_ADDLABEL']._serialized_start=518
  _globals['_ADDLABEL']._serialized_end=568
  _globals['_ADDHOOK']._serialized_start=570
  _globals['_ADDHOOK']._serialized_end=619
  _globals['_INTERNALHOOK']._serialized_start=622
  _globals['_INTERNALHOOK']._serialized_end=868
  _globals['_HOOK']._serialized_start=871
  _globals['_HOOK']._serialized_end=1054
  _globals['_CREDENTIALS']._serialized_start=1056
  _globals['_CREDENTIALS']._serialized_end=1091
  _globals['_CREATEHOOKREQUEST']._serialized_start=1094
  _globals['_CREATEHOOKREQUEST']._serialized_end=1345
  _globals['_CREATEHOOKRESPONSE']._serialized_start=1347
  _globals['_CREATEHOOKRESPONSE']._serialized_end=1392
  _globals['_DELETEHOOKREQUEST']._serialized_start=1394
  _globals['_DELETEHOOKREQUEST']._serialized_end=1438
  _globals['_DELETEHOOKRESPONSE']._serialized_start=1440
  _globals['_DELETEHOOKRESPONSE']._serialized_end=1460
  _globals['_HOOKCALLBACKREQUEST']._serialized_start=1463
  _globals['_HOOKCALLBACKREQUEST']._serialized_end=1738
  _globals['_FINISHED']._serialized_start=1741
  _globals['_FINISHED']._serialized_end=1911
  _globals['_ERROR']._serialized_start=1913
  _globals['_ERROR']._serialized_end=1942
  _globals['_HOOKCALLBACKRESPONSE']._serialized_start=1944
  _globals['_HOOKCALLBACKRESPONSE']._serialized_end=1966
  _globals['_LISTPROJECTHOOKSREQUEST']._serialized_start=1968
  _globals['_LISTPROJECTHOOKSREQUEST']._serialized_end=2024
  _globals['_LISTOWNEDHOOKSREQUEST']._serialized_start=2026
  _globals['_LISTOWNEDHOOKSREQUEST']._serialized_end=2074
  _globals['_HOOKINFO']._serialized_start=2077
  _globals['_HOOKINFO']._serialized_end=2344
  _globals['_LISTPROJECTHOOKSRESPONSE']._serialized_start=2346
  _globals['_LISTPROJECTHOOKSRESPONSE']._serialized_end=2433
  _globals['_LISTOWNEDHOOKSRESPONSE']._serialized_start=2435
  _globals['_LISTOWNEDHOOKSRESPONSE']._serialized_end=2520
  _globals['_ADDPROJECTSTOHOOKREQUEST']._serialized_start=2522
  _globals['_ADDPROJECTSTOHOOKREQUEST']._serialized_end=2606
  _globals['_ADDPROJECTSTOHOOKRESPONSE']._serialized_start=2608
  _globals['_ADDPROJECTSTOHOOKRESPONSE']._serialized_end=2635
  _globals['_HOOKSSERVICE']._serialized_start=2918
  _globals['_HOOKSSERVICE']._serialized_end=3843
# @@protoc_insertion_point(module_scope)
