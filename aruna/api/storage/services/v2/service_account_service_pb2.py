# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/service_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;aruna/api/storage/services/v2/service_account_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/api/visibility.proto\"z\n\x1b\x43reateServiceAccountRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12G\n\npermission\x18\x02 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\"\x93\x01\n\x0eServiceAccount\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12G\n\npermission\x18\x03 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\"v\n\x1c\x43reateServiceAccountResponse\x12V\n\x0fservice_account\x18\x01 \x01(\x0b\x32-.aruna.api.storage.services.v2.ServiceAccountR\x0eserviceAccount\"\xe0\x01\n CreateServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12G\n\npermission\x18\x02 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x39\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"\x80\x01\n!CreateServiceAccountTokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x05token\x12!\n\x0ctoken_secret\x18\x02 \x01(\tR\x0btokenSecret\"\x93\x01\n\"SetServiceAccountPermissionRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12G\n\npermission\x18\x02 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\"}\n#SetServiceAccountPermissionResponse\x12V\n\x0fservice_account\x18\x01 \x01(\x0b\x32-.aruna.api.storage.services.v2.ServiceAccountR\x0eserviceAccount\"`\n\x1dGetServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x19\n\x08token_id\x18\x02 \x01(\tR\x07tokenId\"Z\n\x1eGetServiceAccountTokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x05token\"F\n\x1eGetServiceAccountTokensRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"]\n\x1fGetServiceAccountTokensResponse\x12:\n\x06tokens\x18\x01 \x03(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x06tokens\"c\n DeleteServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x19\n\x08token_id\x18\x02 \x01(\tR\x07tokenId\"#\n!DeleteServiceAccountTokenResponse\"I\n!DeleteServiceAccountTokensRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"$\n\"DeleteServiceAccountTokensResponse\"C\n\x1b\x44\x65leteServiceAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"\x1e\n\x1c\x44\x65leteServiceAccountResponse\"j\n!GetS3CredentialsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"\x94\x01\n\"GetS3CredentialsSvcAccountResponse\x12\"\n\rs3_access_key\x18\x01 \x01(\tR\x0bs3AccessKey\x12\"\n\rs3_secret_key\x18\x02 \x01(\tR\x0bs3SecretKey\x12&\n\x0fs3_endpoint_url\x18\x03 \x01(\tR\rs3EndpointUrl\"\x9e\x01\n\"GetDataproxyTokenSvcAccountRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\x12>\n\x07\x63ontext\x18\x03 \x01(\x0b\x32$.aruna.api.storage.models.v2.ContextR\x07\x63ontext\";\n#GetDataproxyTokenSvcAccountResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token2\xe9\x10\n\x15ServiceAccountService\x12\xaf\x01\n\x14\x43reateServiceAccount\x12:.aruna.api.storage.services.v2.CreateServiceAccountRequest\x1a;.aruna.api.storage.services.v2.CreateServiceAccountResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v2/service_account:\x01*\x12\xd5\x01\n\x19\x43reateServiceAccountToken\x12?.aruna.api.storage.services.v2.CreateServiceAccountTokenRequest\x1a@.aruna.api.storage.services.v2.CreateServiceAccountTokenResponse\"5\x82\xd3\xe4\x93\x02/\"*/v2/service_account/{svc_account_id}/token:\x01*\x12\xe1\x01\n\x1bSetServiceAccountPermission\x12\x41.aruna.api.storage.services.v2.SetServiceAccountPermissionRequest\x1a\x42.aruna.api.storage.services.v2.SetServiceAccountPermissionResponse\";\x82\xd3\xe4\x93\x02\x35\x1a\x30/v2/service_account/{svc_account_id}/permissions:\x01*\x12\xd4\x01\n\x16GetServiceAccountToken\x12<.aruna.api.storage.services.v2.GetServiceAccountTokenRequest\x1a=.aruna.api.storage.services.v2.GetServiceAccountTokenResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v2/service_account/{svc_account_id}/token/{token_id}\x12\xcd\x01\n\x17GetServiceAccountTokens\x12=.aruna.api.storage.services.v2.GetServiceAccountTokensRequest\x1a>.aruna.api.storage.services.v2.GetServiceAccountTokensResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v2/service_account/{svc_account_id}/tokens\x12\xdd\x01\n\x19\x44\x65leteServiceAccountToken\x12?.aruna.api.storage.services.v2.DeleteServiceAccountTokenRequest\x1a@.aruna.api.storage.services.v2.DeleteServiceAccountTokenResponse\"=\x82\xd3\xe4\x93\x02\x37*5/v2/service_account/{svc_account_id}/token/{token_id}\x12\xd6\x01\n\x1a\x44\x65leteServiceAccountTokens\x12@.aruna.api.storage.services.v2.DeleteServiceAccountTokensRequest\x1a\x41.aruna.api.storage.services.v2.DeleteServiceAccountTokensResponse\"3\x82\xd3\xe4\x93\x02-*+/v2/service_account/{svc_account_id}/tokens\x12\xbd\x01\n\x14\x44\x65leteServiceAccount\x12:.aruna.api.storage.services.v2.DeleteServiceAccountRequest\x1a;.aruna.api.storage.services.v2.DeleteServiceAccountResponse\",\x82\xd3\xe4\x93\x02&*$/v2/service_account/{svc_account_id}\x12\xde\x01\n\x1aGetS3CredentialsSvcAccount\x12@.aruna.api.storage.services.v2.GetS3CredentialsSvcAccountRequest\x1a\x41.aruna.api.storage.services.v2.GetS3CredentialsSvcAccountResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/v2/service_account/{svc_account_id}/s3_credentials\x12\xd0\x01\n\x1bGetDataproxyTokenSvcAccount\x12\x41.aruna.api.storage.services.v2.GetDataproxyTokenSvcAccountRequest\x1a\x42.aruna.api.storage.services.v2.GetDataproxyTokenSvcAccountResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v2/user/{user_id}/svc_proxy_token\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x9a\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x15ServiceAccountServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.service_account_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\025ServiceAccountServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_SERVICEACCOUNTSERVICE']._options = None
  _globals['_SERVICEACCOUNTSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._serialized_options = b'\202\323\344\223\002\030\"\023/v2/service_account:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccountToken']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccountToken']._serialized_options = b'\202\323\344\223\002/\"*/v2/service_account/{svc_account_id}/token:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['SetServiceAccountPermission']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['SetServiceAccountPermission']._serialized_options = b'\202\323\344\223\0025\0320/v2/service_account/{svc_account_id}/permissions:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountToken']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountToken']._serialized_options = b'\202\323\344\223\0027\0225/v2/service_account/{svc_account_id}/token/{token_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountTokens']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountTokens']._serialized_options = b'\202\323\344\223\002-\022+/v2/service_account/{svc_account_id}/tokens'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountToken']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountToken']._serialized_options = b'\202\323\344\223\0027*5/v2/service_account/{svc_account_id}/token/{token_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountTokens']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountTokens']._serialized_options = b'\202\323\344\223\002-*+/v2/service_account/{svc_account_id}/tokens'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._serialized_options = b'\202\323\344\223\002&*$/v2/service_account/{svc_account_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetS3CredentialsSvcAccount']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetS3CredentialsSvcAccount']._serialized_options = b'\202\323\344\223\0025\0223/v2/service_account/{svc_account_id}/s3_credentials'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetDataproxyTokenSvcAccount']._options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetDataproxyTokenSvcAccount']._serialized_options = b'\202\323\344\223\002$\022\"/v2/user/{user_id}/svc_proxy_token'
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_start=228
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_end=350
  _globals['_SERVICEACCOUNT']._serialized_start=353
  _globals['_SERVICEACCOUNT']._serialized_end=500
  _globals['_CREATESERVICEACCOUNTRESPONSE']._serialized_start=502
  _globals['_CREATESERVICEACCOUNTRESPONSE']._serialized_end=620
  _globals['_CREATESERVICEACCOUNTTOKENREQUEST']._serialized_start=623
  _globals['_CREATESERVICEACCOUNTTOKENREQUEST']._serialized_end=847
  _globals['_CREATESERVICEACCOUNTTOKENRESPONSE']._serialized_start=850
  _globals['_CREATESERVICEACCOUNTTOKENRESPONSE']._serialized_end=978
  _globals['_SETSERVICEACCOUNTPERMISSIONREQUEST']._serialized_start=981
  _globals['_SETSERVICEACCOUNTPERMISSIONREQUEST']._serialized_end=1128
  _globals['_SETSERVICEACCOUNTPERMISSIONRESPONSE']._serialized_start=1130
  _globals['_SETSERVICEACCOUNTPERMISSIONRESPONSE']._serialized_end=1255
  _globals['_GETSERVICEACCOUNTTOKENREQUEST']._serialized_start=1257
  _globals['_GETSERVICEACCOUNTTOKENREQUEST']._serialized_end=1353
  _globals['_GETSERVICEACCOUNTTOKENRESPONSE']._serialized_start=1355
  _globals['_GETSERVICEACCOUNTTOKENRESPONSE']._serialized_end=1445
  _globals['_GETSERVICEACCOUNTTOKENSREQUEST']._serialized_start=1447
  _globals['_GETSERVICEACCOUNTTOKENSREQUEST']._serialized_end=1517
  _globals['_GETSERVICEACCOUNTTOKENSRESPONSE']._serialized_start=1519
  _globals['_GETSERVICEACCOUNTTOKENSRESPONSE']._serialized_end=1612
  _globals['_DELETESERVICEACCOUNTTOKENREQUEST']._serialized_start=1614
  _globals['_DELETESERVICEACCOUNTTOKENREQUEST']._serialized_end=1713
  _globals['_DELETESERVICEACCOUNTTOKENRESPONSE']._serialized_start=1715
  _globals['_DELETESERVICEACCOUNTTOKENRESPONSE']._serialized_end=1750
  _globals['_DELETESERVICEACCOUNTTOKENSREQUEST']._serialized_start=1752
  _globals['_DELETESERVICEACCOUNTTOKENSREQUEST']._serialized_end=1825
  _globals['_DELETESERVICEACCOUNTTOKENSRESPONSE']._serialized_start=1827
  _globals['_DELETESERVICEACCOUNTTOKENSRESPONSE']._serialized_end=1863
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_start=1865
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_end=1932
  _globals['_DELETESERVICEACCOUNTRESPONSE']._serialized_start=1934
  _globals['_DELETESERVICEACCOUNTRESPONSE']._serialized_end=1964
  _globals['_GETS3CREDENTIALSSVCACCOUNTREQUEST']._serialized_start=1966
  _globals['_GETS3CREDENTIALSSVCACCOUNTREQUEST']._serialized_end=2072
  _globals['_GETS3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_start=2075
  _globals['_GETS3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_end=2223
  _globals['_GETDATAPROXYTOKENSVCACCOUNTREQUEST']._serialized_start=2226
  _globals['_GETDATAPROXYTOKENSVCACCOUNTREQUEST']._serialized_end=2384
  _globals['_GETDATAPROXYTOKENSVCACCOUNTRESPONSE']._serialized_start=2386
  _globals['_GETDATAPROXYTOKENSVCACCOUNTRESPONSE']._serialized_end=2445
  _globals['_SERVICEACCOUNTSERVICE']._serialized_start=2448
  _globals['_SERVICEACCOUNTSERVICE']._serialized_end=4601
# @@protoc_insertion_point(module_scope)
