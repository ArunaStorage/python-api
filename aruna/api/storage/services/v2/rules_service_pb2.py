# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/rules_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1aruna/api/storage/services/v2/rules_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a\x1cgoogle/api/annotations.proto\"a\n\x11\x43reateRuleRequest\x12\x12\n\x04rule\x18\x01 \x01(\tR\x04rule\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06public\x18\x03 \x01(\x08R\x06public\"$\n\x12\x43reateRuleResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\" \n\x0eGetRuleRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"z\n\x04Rule\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04rule\x18\x02 \x01(\tR\x04rule\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06public\x18\x04 \x01(\x08R\x06public\x12\x14\n\x05owner\x18\x05 \x01(\tR\x05owner\"J\n\x0fGetRuleResponse\x12\x37\n\x04rule\x18\x01 \x01(\x0b\x32#.aruna.api.storage.services.v2.RuleR\x04rule\"\x11\n\x0fListRuleRequest\"M\n\x10ListRuleResponse\x12\x39\n\x05rules\x18\x01 \x03(\x0b\x32#.aruna.api.storage.services.v2.RuleR\x05rules\"q\n\x11UpdateRuleRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04rule\x18\x02 \x01(\tR\x04rule\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06public\x18\x04 \x01(\x08R\x06public\"M\n\x12UpdateRuleResponse\x12\x37\n\x04rule\x18\x01 \x01(\x0b\x32#.aruna.api.storage.services.v2.RuleR\x04rule\"#\n\x11\x44\x65leteRuleRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x14\n\x12\x44\x65leteRuleResponse\"n\n\x18\x43reateRuleBindingRequest\x12\x17\n\x07rule_id\x18\x01 \x01(\tR\x06ruleId\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x12\x1c\n\tcascading\x18\x03 \x01(\x08R\tcascading\"o\n\x19\x43reateRuleBindingResponse\x12\x17\n\x07rule_id\x18\x01 \x01(\tR\x06ruleId\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x12\x1c\n\tcascading\x18\x03 \x01(\x08R\tcascading\"P\n\x18\x44\x65leteRuleBindingRequest\x12\x17\n\x07rule_id\x18\x01 \x01(\tR\x06ruleId\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\"\x1b\n\x19\x44\x65leteRuleBindingResponse2\xa9\x08\n\x0cRulesService\x12\x87\x01\n\nCreateRule\x12\x30.aruna.api.storage.services.v2.CreateRuleRequest\x1a\x31.aruna.api.storage.services.v2.CreateRuleResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/v2/rules:\x01*\x12\x80\x01\n\x07GetRule\x12-.aruna.api.storage.services.v2.GetRuleRequest\x1a..aruna.api.storage.services.v2.GetRuleResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v2/rules/{id}\x12\x83\x01\n\x08ListRule\x12..aruna.api.storage.services.v2.ListRuleRequest\x1a/.aruna.api.storage.services.v2.ListRuleResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v2/rules/list\x12\x8c\x01\n\nUpdateRule\x12\x30.aruna.api.storage.services.v2.UpdateRuleRequest\x1a\x31.aruna.api.storage.services.v2.UpdateRuleResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x32\x0e/v2/rules/{id}:\x01*\x12\x89\x01\n\nDeleteRule\x12\x30.aruna.api.storage.services.v2.DeleteRuleRequest\x1a\x31.aruna.api.storage.services.v2.DeleteRuleResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v2/rules/{id}\x12\xaf\x01\n\x11\x43reateRuleBinding\x12\x37.aruna.api.storage.services.v2.CreateRuleBindingRequest\x1a\x38.aruna.api.storage.services.v2.CreateRuleBindingResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v2/rules/{rule_id}/bindings:\x01*\x12\xb8\x01\n\x11\x44\x65leteRuleBinding\x12\x37.aruna.api.storage.services.v2.DeleteRuleBindingRequest\x1a\x38.aruna.api.storage.services.v2.DeleteRuleBindingResponse\"0\x82\xd3\xe4\x93\x02**(/v2/rules/{rule_id}/bindings/{object_id}B\x91\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x0cRulesServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.rules_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\014RulesServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_RULESSERVICE'].methods_by_name['CreateRule']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['CreateRule']._serialized_options = b'\202\323\344\223\002\016\"\t/v2/rules:\001*'
  _globals['_RULESSERVICE'].methods_by_name['GetRule']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['GetRule']._serialized_options = b'\202\323\344\223\002\020\022\016/v2/rules/{id}'
  _globals['_RULESSERVICE'].methods_by_name['ListRule']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['ListRule']._serialized_options = b'\202\323\344\223\002\020\022\016/v2/rules/list'
  _globals['_RULESSERVICE'].methods_by_name['UpdateRule']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['UpdateRule']._serialized_options = b'\202\323\344\223\002\0232\016/v2/rules/{id}:\001*'
  _globals['_RULESSERVICE'].methods_by_name['DeleteRule']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['DeleteRule']._serialized_options = b'\202\323\344\223\002\020*\016/v2/rules/{id}'
  _globals['_RULESSERVICE'].methods_by_name['CreateRuleBinding']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['CreateRuleBinding']._serialized_options = b'\202\323\344\223\002!\"\034/v2/rules/{rule_id}/bindings:\001*'
  _globals['_RULESSERVICE'].methods_by_name['DeleteRuleBinding']._loaded_options = None
  _globals['_RULESSERVICE'].methods_by_name['DeleteRuleBinding']._serialized_options = b'\202\323\344\223\002**(/v2/rules/{rule_id}/bindings/{object_id}'
  _globals['_CREATERULEREQUEST']._serialized_start=114
  _globals['_CREATERULEREQUEST']._serialized_end=211
  _globals['_CREATERULERESPONSE']._serialized_start=213
  _globals['_CREATERULERESPONSE']._serialized_end=249
  _globals['_GETRULEREQUEST']._serialized_start=251
  _globals['_GETRULEREQUEST']._serialized_end=283
  _globals['_RULE']._serialized_start=285
  _globals['_RULE']._serialized_end=407
  _globals['_GETRULERESPONSE']._serialized_start=409
  _globals['_GETRULERESPONSE']._serialized_end=483
  _globals['_LISTRULEREQUEST']._serialized_start=485
  _globals['_LISTRULEREQUEST']._serialized_end=502
  _globals['_LISTRULERESPONSE']._serialized_start=504
  _globals['_LISTRULERESPONSE']._serialized_end=581
  _globals['_UPDATERULEREQUEST']._serialized_start=583
  _globals['_UPDATERULEREQUEST']._serialized_end=696
  _globals['_UPDATERULERESPONSE']._serialized_start=698
  _globals['_UPDATERULERESPONSE']._serialized_end=775
  _globals['_DELETERULEREQUEST']._serialized_start=777
  _globals['_DELETERULEREQUEST']._serialized_end=812
  _globals['_DELETERULERESPONSE']._serialized_start=814
  _globals['_DELETERULERESPONSE']._serialized_end=834
  _globals['_CREATERULEBINDINGREQUEST']._serialized_start=836
  _globals['_CREATERULEBINDINGREQUEST']._serialized_end=946
  _globals['_CREATERULEBINDINGRESPONSE']._serialized_start=948
  _globals['_CREATERULEBINDINGRESPONSE']._serialized_end=1059
  _globals['_DELETERULEBINDINGREQUEST']._serialized_start=1061
  _globals['_DELETERULEBINDINGREQUEST']._serialized_end=1141
  _globals['_DELETERULEBINDINGRESPONSE']._serialized_start=1143
  _globals['_DELETERULEBINDINGRESPONSE']._serialized_end=1170
  _globals['_RULESSERVICE']._serialized_start=1173
  _globals['_RULESSERVICE']._serialized_end=2238
# @@protoc_insertion_point(module_scope)
