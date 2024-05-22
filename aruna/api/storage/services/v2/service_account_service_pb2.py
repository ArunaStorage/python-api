# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/service_account_service.proto
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
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;aruna/api/storage/services/v2/service_account_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/api/visibility.proto\"\xa9\x01\n\x1b\x43reateServiceAccountRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12W\n\x10permission_level\x18\x03 \x01(\x0e\x32,.aruna.api.storage.models.v2.PermissionLevelR\x0fpermissionLevel\"\x93\x01\n\x0eServiceAccount\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12G\n\npermission\x18\x03 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\"v\n\x1c\x43reateServiceAccountResponse\x12V\n\x0fservice_account\x18\x01 \x01(\x0b\x32-.aruna.api.storage.services.v2.ServiceAccountR\x0eserviceAccount\"\xe0\x01\n CreateServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12G\n\npermission\x18\x02 \x01(\x0b\x32\'.aruna.api.storage.models.v2.PermissionR\npermission\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x39\n\nexpires_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"\x80\x01\n!CreateServiceAccountTokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x05token\x12!\n\x0ctoken_secret\x18\x02 \x01(\tR\x0btokenSecret\"`\n\x1dGetServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x19\n\x08token_id\x18\x02 \x01(\tR\x07tokenId\"Z\n\x1eGetServiceAccountTokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x05token\"F\n\x1eGetServiceAccountTokensRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"]\n\x1fGetServiceAccountTokensResponse\x12:\n\x06tokens\x18\x01 \x03(\x0b\x32\".aruna.api.storage.models.v2.TokenR\x06tokens\"c\n DeleteServiceAccountTokenRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x19\n\x08token_id\x18\x02 \x01(\tR\x07tokenId\"#\n!DeleteServiceAccountTokenResponse\"I\n!DeleteServiceAccountTokensRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"$\n\"DeleteServiceAccountTokensResponse\"C\n\x1b\x44\x65leteServiceAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\"\x1e\n\x1c\x44\x65leteServiceAccountResponse\"m\n$CreateS3CredentialsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"\x97\x01\n%CreateS3CredentialsSvcAccountResponse\x12\"\n\rs3_access_key\x18\x01 \x01(\tR\x0bs3AccessKey\x12\"\n\rs3_secret_key\x18\x02 \x01(\tR\x0bs3SecretKey\x12&\n\x0fs3_endpoint_url\x18\x03 \x01(\tR\rs3EndpointUrl\"j\n!GetS3CredentialsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"\x94\x01\n\"GetS3CredentialsSvcAccountResponse\x12\"\n\rs3_access_key\x18\x01 \x01(\tR\x0bs3AccessKey\x12\"\n\rs3_secret_key\x18\x02 \x01(\tR\x0bs3SecretKey\x12&\n\x0fs3_endpoint_url\x18\x03 \x01(\tR\rs3EndpointUrl\"m\n$DeleteS3CredentialsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"\'\n%DeleteS3CredentialsSvcAccountResponse\"\xbf\x01\n%CreateDataproxyTokenSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x43\n\x07\x63ontext\x18\x03 \x01(\x0b\x32$.aruna.api.storage.models.v2.ContextH\x00R\x07\x63ontext\x88\x01\x01\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointIdB\n\n\x08_context\">\n&CreateDataproxyTokenSvcAccountResponse\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"a\n\x1a\x41\x64\x64PubkeySvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1d\n\npublic_key\x18\x02 \x01(\tR\tpublicKey\"\x1d\n\x1b\x41\x64\x64PubkeySvcAccountResponse\"m\n$AddTrustedEndpointsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"\'\n%AddTrustedEndpointsSvcAccountResponse\"p\n\'RemoveTrustedEndpointsSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12\x1f\n\x0b\x65ndpoint_id\x18\x02 \x01(\tR\nendpointId\"*\n(RemoveTrustedEndpointsSvcAccountResponse\"\x9d\x01\n&AddDataProxyAttributeSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12M\n\tattribute\x18\x02 \x01(\x0b\x32/.aruna.api.storage.models.v2.DataProxyAttributeR\tattribute\")\n\'AddDataProxyAttributeSvcAccountResponse\"\x9b\x01\n)RemoveDataProxyAttributeSvcAccountRequest\x12$\n\x0esvc_account_id\x18\x01 \x01(\tR\x0csvcAccountId\x12!\n\x0c\x64\x61taproxy_id\x18\x02 \x01(\tR\x0b\x64\x61taproxyId\x12%\n\x0e\x61ttribute_name\x18\x03 \x01(\tR\rattributeName\",\n*RemoveDataProxyAttributeSvcAccountResponse2\xf6\x1c\n\x15ServiceAccountService\x12\xb0\x01\n\x14\x43reateServiceAccount\x12:.aruna.api.storage.services.v2.CreateServiceAccountRequest\x1a;.aruna.api.storage.services.v2.CreateServiceAccountResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v2/service_accounts:\x01*\x12\xd7\x01\n\x19\x43reateServiceAccountToken\x12?.aruna.api.storage.services.v2.CreateServiceAccountTokenRequest\x1a@.aruna.api.storage.services.v2.CreateServiceAccountTokenResponse\"7\x82\xd3\xe4\x93\x02\x31\",/v2/service_accounts/{svc_account_id}/tokens:\x01*\x12\xd6\x01\n\x16GetServiceAccountToken\x12<.aruna.api.storage.services.v2.GetServiceAccountTokenRequest\x1a=.aruna.api.storage.services.v2.GetServiceAccountTokenResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/v2/service_accounts/{svc_account_id}/tokens/{token_id}\x12\xce\x01\n\x17GetServiceAccountTokens\x12=.aruna.api.storage.services.v2.GetServiceAccountTokensRequest\x1a>.aruna.api.storage.services.v2.GetServiceAccountTokensResponse\"4\x82\xd3\xe4\x93\x02.\x12,/v2/service_accounts/{svc_account_id}/tokens\x12\xdf\x01\n\x19\x44\x65leteServiceAccountToken\x12?.aruna.api.storage.services.v2.DeleteServiceAccountTokenRequest\x1a@.aruna.api.storage.services.v2.DeleteServiceAccountTokenResponse\"?\x82\xd3\xe4\x93\x02\x39*7/v2/service_accounts/{svc_account_id}/tokens/{token_id}\x12\xd7\x01\n\x1a\x44\x65leteServiceAccountTokens\x12@.aruna.api.storage.services.v2.DeleteServiceAccountTokensRequest\x1a\x41.aruna.api.storage.services.v2.DeleteServiceAccountTokensResponse\"4\x82\xd3\xe4\x93\x02.*,/v2/service_accounts/{svc_account_id}/tokens\x12\xbe\x01\n\x14\x44\x65leteServiceAccount\x12:.aruna.api.storage.services.v2.DeleteServiceAccountRequest\x1a;.aruna.api.storage.services.v2.DeleteServiceAccountResponse\"-\x82\xd3\xe4\x93\x02\'*%/v2/service_accounts/{svc_account_id}\x12\xf6\x01\n\x1d\x43reateS3CredentialsSvcAccount\x12\x43.aruna.api.storage.services.v2.CreateS3CredentialsSvcAccountRequest\x1a\x44.aruna.api.storage.services.v2.CreateS3CredentialsSvcAccountResponse\"J\x82\xd3\xe4\x93\x02\x44\x32\x42/v2/service_accounts/{svc_account_id}/s3_credentials/{endpoint_id}\x12\xf0\x01\n\x1aGetS3CredentialsSvcAccount\x12@.aruna.api.storage.services.v2.GetS3CredentialsSvcAccountRequest\x1a\x41.aruna.api.storage.services.v2.GetS3CredentialsSvcAccountResponse\"M\x82\xd3\xe4\x93\x02G\x12\x45/v2/user/s3_credentials/{svc_account_id}/s3_credentials/{endpoint_id}\x12\x83\x02\n\x1d\x44\x65leteS3CredentialsSvcAccount\x12\x43.aruna.api.storage.services.v2.DeleteS3CredentialsSvcAccountRequest\x1a\x44.aruna.api.storage.services.v2.DeleteS3CredentialsSvcAccountResponse\"W\x82\xd3\xe4\x93\x02Q2L/v2/user/s3_credentials/{svc_account_id}/s3_credentials/{endpoint_id}/revoke:\x01*\x12\xfa\x01\n\x1e\x43reateDataproxyTokenSvcAccount\x12\x44.aruna.api.storage.services.v2.CreateDataproxyTokenSvcAccountRequest\x1a\x45.aruna.api.storage.services.v2.CreateDataproxyTokenSvcAccountResponse\"K\x82\xd3\xe4\x93\x02\x45\"@/v2/service_accounts/{svc_account_id}/proxy_tokens/{endpoint_id}:\x01*\x12\xc5\x01\n\x13\x41\x64\x64PubkeySvcAccount\x12\x39.aruna.api.storage.services.v2.AddPubkeySvcAccountRequest\x1a:.aruna.api.storage.services.v2.AddPubkeySvcAccountResponse\"7\x82\xd3\xe4\x93\x02\x31\",/v2/service_accounts/{svc_account_id}/pubkey:\x01*\x12\xee\x01\n\x1d\x41\x64\x64TrustedEndpointsSvcAccount\x12\x43.aruna.api.storage.services.v2.AddTrustedEndpointsSvcAccountRequest\x1a\x44.aruna.api.storage.services.v2.AddTrustedEndpointsSvcAccountResponse\"B\x82\xd3\xe4\x93\x02<\"7/v2/service_accounts/{svc_account_id}/trusted_endpoints:\x01*\x12\xf4\x01\n RemoveTrustedEndpointsSvcAccount\x12\x46.aruna.api.storage.services.v2.RemoveTrustedEndpointsSvcAccountRequest\x1aG.aruna.api.storage.services.v2.RemoveTrustedEndpointsSvcAccountResponse\"?\x82\xd3\xe4\x93\x02\x39*7/v2/service_accounts/{svc_account_id}/trusted_endpoints\x12\xf8\x01\n\x1f\x41\x64\x64\x44\x61taProxyAttributeSvcAccount\x12\x45.aruna.api.storage.services.v2.AddDataProxyAttributeSvcAccountRequest\x1a\x46.aruna.api.storage.services.v2.AddDataProxyAttributeSvcAccountResponse\"F\x82\xd3\xe4\x93\x02@\";/v2/service_accounts/{svc_account_id}/attributes/data_proxy:\x01*\x12\xfe\x01\n\"RemoveDataProxyAttributeSvcAccount\x12H.aruna.api.storage.services.v2.RemoveDataProxyAttributeSvcAccountRequest\x1aI.aruna.api.storage.services.v2.RemoveDataProxyAttributeSvcAccountResponse\"C\x82\xd3\xe4\x93\x02=*;/v2/service_accounts/{svc_account_id}/attributes/data_proxy\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x9a\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x15ServiceAccountServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.service_account_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\025ServiceAccountServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_SERVICEACCOUNTSERVICE']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccount']._serialized_options = b'\202\323\344\223\002\031\"\024/v2/service_accounts:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccountToken']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateServiceAccountToken']._serialized_options = b'\202\323\344\223\0021\",/v2/service_accounts/{svc_account_id}/tokens:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountToken']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountToken']._serialized_options = b'\202\323\344\223\0029\0227/v2/service_accounts/{svc_account_id}/tokens/{token_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountTokens']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetServiceAccountTokens']._serialized_options = b'\202\323\344\223\002.\022,/v2/service_accounts/{svc_account_id}/tokens'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountToken']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountToken']._serialized_options = b'\202\323\344\223\0029*7/v2/service_accounts/{svc_account_id}/tokens/{token_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountTokens']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccountTokens']._serialized_options = b'\202\323\344\223\002.*,/v2/service_accounts/{svc_account_id}/tokens'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteServiceAccount']._serialized_options = b'\202\323\344\223\002\'*%/v2/service_accounts/{svc_account_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateS3CredentialsSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateS3CredentialsSvcAccount']._serialized_options = b'\202\323\344\223\002D2B/v2/service_accounts/{svc_account_id}/s3_credentials/{endpoint_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetS3CredentialsSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['GetS3CredentialsSvcAccount']._serialized_options = b'\202\323\344\223\002G\022E/v2/user/s3_credentials/{svc_account_id}/s3_credentials/{endpoint_id}'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteS3CredentialsSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['DeleteS3CredentialsSvcAccount']._serialized_options = b'\202\323\344\223\002Q2L/v2/user/s3_credentials/{svc_account_id}/s3_credentials/{endpoint_id}/revoke:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateDataproxyTokenSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['CreateDataproxyTokenSvcAccount']._serialized_options = b'\202\323\344\223\002E\"@/v2/service_accounts/{svc_account_id}/proxy_tokens/{endpoint_id}:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddPubkeySvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddPubkeySvcAccount']._serialized_options = b'\202\323\344\223\0021\",/v2/service_accounts/{svc_account_id}/pubkey:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddTrustedEndpointsSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddTrustedEndpointsSvcAccount']._serialized_options = b'\202\323\344\223\002<\"7/v2/service_accounts/{svc_account_id}/trusted_endpoints:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['RemoveTrustedEndpointsSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['RemoveTrustedEndpointsSvcAccount']._serialized_options = b'\202\323\344\223\0029*7/v2/service_accounts/{svc_account_id}/trusted_endpoints'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddDataProxyAttributeSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['AddDataProxyAttributeSvcAccount']._serialized_options = b'\202\323\344\223\002@\";/v2/service_accounts/{svc_account_id}/attributes/data_proxy:\001*'
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['RemoveDataProxyAttributeSvcAccount']._loaded_options = None
  _globals['_SERVICEACCOUNTSERVICE'].methods_by_name['RemoveDataProxyAttributeSvcAccount']._serialized_options = b'\202\323\344\223\002=*;/v2/service_accounts/{svc_account_id}/attributes/data_proxy'
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_start=229
  _globals['_CREATESERVICEACCOUNTREQUEST']._serialized_end=398
  _globals['_SERVICEACCOUNT']._serialized_start=401
  _globals['_SERVICEACCOUNT']._serialized_end=548
  _globals['_CREATESERVICEACCOUNTRESPONSE']._serialized_start=550
  _globals['_CREATESERVICEACCOUNTRESPONSE']._serialized_end=668
  _globals['_CREATESERVICEACCOUNTTOKENREQUEST']._serialized_start=671
  _globals['_CREATESERVICEACCOUNTTOKENREQUEST']._serialized_end=895
  _globals['_CREATESERVICEACCOUNTTOKENRESPONSE']._serialized_start=898
  _globals['_CREATESERVICEACCOUNTTOKENRESPONSE']._serialized_end=1026
  _globals['_GETSERVICEACCOUNTTOKENREQUEST']._serialized_start=1028
  _globals['_GETSERVICEACCOUNTTOKENREQUEST']._serialized_end=1124
  _globals['_GETSERVICEACCOUNTTOKENRESPONSE']._serialized_start=1126
  _globals['_GETSERVICEACCOUNTTOKENRESPONSE']._serialized_end=1216
  _globals['_GETSERVICEACCOUNTTOKENSREQUEST']._serialized_start=1218
  _globals['_GETSERVICEACCOUNTTOKENSREQUEST']._serialized_end=1288
  _globals['_GETSERVICEACCOUNTTOKENSRESPONSE']._serialized_start=1290
  _globals['_GETSERVICEACCOUNTTOKENSRESPONSE']._serialized_end=1383
  _globals['_DELETESERVICEACCOUNTTOKENREQUEST']._serialized_start=1385
  _globals['_DELETESERVICEACCOUNTTOKENREQUEST']._serialized_end=1484
  _globals['_DELETESERVICEACCOUNTTOKENRESPONSE']._serialized_start=1486
  _globals['_DELETESERVICEACCOUNTTOKENRESPONSE']._serialized_end=1521
  _globals['_DELETESERVICEACCOUNTTOKENSREQUEST']._serialized_start=1523
  _globals['_DELETESERVICEACCOUNTTOKENSREQUEST']._serialized_end=1596
  _globals['_DELETESERVICEACCOUNTTOKENSRESPONSE']._serialized_start=1598
  _globals['_DELETESERVICEACCOUNTTOKENSRESPONSE']._serialized_end=1634
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_start=1636
  _globals['_DELETESERVICEACCOUNTREQUEST']._serialized_end=1703
  _globals['_DELETESERVICEACCOUNTRESPONSE']._serialized_start=1705
  _globals['_DELETESERVICEACCOUNTRESPONSE']._serialized_end=1735
  _globals['_CREATES3CREDENTIALSSVCACCOUNTREQUEST']._serialized_start=1737
  _globals['_CREATES3CREDENTIALSSVCACCOUNTREQUEST']._serialized_end=1846
  _globals['_CREATES3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_start=1849
  _globals['_CREATES3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_end=2000
  _globals['_GETS3CREDENTIALSSVCACCOUNTREQUEST']._serialized_start=2002
  _globals['_GETS3CREDENTIALSSVCACCOUNTREQUEST']._serialized_end=2108
  _globals['_GETS3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_start=2111
  _globals['_GETS3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_end=2259
  _globals['_DELETES3CREDENTIALSSVCACCOUNTREQUEST']._serialized_start=2261
  _globals['_DELETES3CREDENTIALSSVCACCOUNTREQUEST']._serialized_end=2370
  _globals['_DELETES3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_start=2372
  _globals['_DELETES3CREDENTIALSSVCACCOUNTRESPONSE']._serialized_end=2411
  _globals['_CREATEDATAPROXYTOKENSVCACCOUNTREQUEST']._serialized_start=2414
  _globals['_CREATEDATAPROXYTOKENSVCACCOUNTREQUEST']._serialized_end=2605
  _globals['_CREATEDATAPROXYTOKENSVCACCOUNTRESPONSE']._serialized_start=2607
  _globals['_CREATEDATAPROXYTOKENSVCACCOUNTRESPONSE']._serialized_end=2669
  _globals['_ADDPUBKEYSVCACCOUNTREQUEST']._serialized_start=2671
  _globals['_ADDPUBKEYSVCACCOUNTREQUEST']._serialized_end=2768
  _globals['_ADDPUBKEYSVCACCOUNTRESPONSE']._serialized_start=2770
  _globals['_ADDPUBKEYSVCACCOUNTRESPONSE']._serialized_end=2799
  _globals['_ADDTRUSTEDENDPOINTSSVCACCOUNTREQUEST']._serialized_start=2801
  _globals['_ADDTRUSTEDENDPOINTSSVCACCOUNTREQUEST']._serialized_end=2910
  _globals['_ADDTRUSTEDENDPOINTSSVCACCOUNTRESPONSE']._serialized_start=2912
  _globals['_ADDTRUSTEDENDPOINTSSVCACCOUNTRESPONSE']._serialized_end=2951
  _globals['_REMOVETRUSTEDENDPOINTSSVCACCOUNTREQUEST']._serialized_start=2953
  _globals['_REMOVETRUSTEDENDPOINTSSVCACCOUNTREQUEST']._serialized_end=3065
  _globals['_REMOVETRUSTEDENDPOINTSSVCACCOUNTRESPONSE']._serialized_start=3067
  _globals['_REMOVETRUSTEDENDPOINTSSVCACCOUNTRESPONSE']._serialized_end=3109
  _globals['_ADDDATAPROXYATTRIBUTESVCACCOUNTREQUEST']._serialized_start=3112
  _globals['_ADDDATAPROXYATTRIBUTESVCACCOUNTREQUEST']._serialized_end=3269
  _globals['_ADDDATAPROXYATTRIBUTESVCACCOUNTRESPONSE']._serialized_start=3271
  _globals['_ADDDATAPROXYATTRIBUTESVCACCOUNTRESPONSE']._serialized_end=3312
  _globals['_REMOVEDATAPROXYATTRIBUTESVCACCOUNTREQUEST']._serialized_start=3315
  _globals['_REMOVEDATAPROXYATTRIBUTESVCACCOUNTREQUEST']._serialized_end=3470
  _globals['_REMOVEDATAPROXYATTRIBUTESVCACCOUNTRESPONSE']._serialized_start=3472
  _globals['_REMOVEDATAPROXYATTRIBUTESVCACCOUNTRESPONSE']._serialized_end=3516
  _globals['_SERVICEACCOUNTSERVICE']._serialized_start=3519
  _globals['_SERVICEACCOUNTSERVICE']._serialized_end=7221
# @@protoc_insertion_point(module_scope)
