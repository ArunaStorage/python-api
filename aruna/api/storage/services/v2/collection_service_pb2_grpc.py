# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v2 import collection_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2


class CollectionServiceStub(object):
    """CollectionService

    Contains all methods that get/create or update Collection and associated resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCollection = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/CreateCollection',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionResponse.FromString,
                )
        self.GetCollection = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/GetCollection',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionResponse.FromString,
                )
        self.GetCollections = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/GetCollections',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsResponse.FromString,
                )
        self.DeleteCollection = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/DeleteCollection',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionResponse.FromString,
                )
        self.UpdateCollectionName = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionName',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameResponse.FromString,
                )
        self.UpdateCollectionDescription = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionDescription',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionResponse.FromString,
                )
        self.UpdateCollectionKeyValues = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionKeyValues',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesResponse.FromString,
                )
        self.UpdateCollectionDataClass = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionDataClass',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassResponse.FromString,
                )
        self.SnapshotCollection = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/SnapshotCollection',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionResponse.FromString,
                )
        self.UpdateCollectionLicenses = channel.unary_unary(
                '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionLicenses',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesResponse.FromString,
                )


class CollectionServiceServicer(object):
    """CollectionService

    Contains all methods that get/create or update Collection and associated resources
    """

    def CreateCollection(self, request, context):
        """CreateNewCollection

        Status: BETA

        creates a new Collection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCollection(self, request, context):
        """GetCollection

        Status: BETA

        Request a specific collection by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCollections(self, request, context):
        """GetCollections

        Status: BETA

        Queries multiple collections by ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCollection(self, request, context):
        """DeleteCollection

        Status: STABLE

        This request deletes the collection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionName(self, request, context):
        """UpdateCollectionName

        Status: BETA

        Updates the collection name. Caveat! Will rename the "s3 bucket" for data proxies! 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionDescription(self, request, context):
        """UpdateCollectionDescription

        Status: BETA

        Updates the collection description.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionKeyValues(self, request, context):
        """UpdateCollectionKeyValues

        Status: BETA

        Updates the collection key values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionDataClass(self, request, context):
        """UpdateCollectionDataClass

        Status: BETA

        Updates the collection name. All (meta) data will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SnapshotCollection(self, request, context):
        """SnapshotCollectionRequest

        Status: BETA

        Archives the full collection, rendering all downstream relations immutable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCollectionLicenses(self, request, context):
        """UpdateLicenses

        Status: BETA

        Updates the collections metadata license and/or default data license.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCollection,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionResponse.SerializeToString,
            ),
            'GetCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCollection,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionResponse.SerializeToString,
            ),
            'GetCollections': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCollections,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsResponse.SerializeToString,
            ),
            'DeleteCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCollection,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionResponse.SerializeToString,
            ),
            'UpdateCollectionName': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionName,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameResponse.SerializeToString,
            ),
            'UpdateCollectionDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionDescription,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionResponse.SerializeToString,
            ),
            'UpdateCollectionKeyValues': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionKeyValues,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesResponse.SerializeToString,
            ),
            'UpdateCollectionDataClass': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionDataClass,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassResponse.SerializeToString,
            ),
            'SnapshotCollection': grpc.unary_unary_rpc_method_handler(
                    servicer.SnapshotCollection,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionResponse.SerializeToString,
            ),
            'UpdateCollectionLicenses': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCollectionLicenses,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v2.CollectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CollectionService(object):
    """CollectionService

    Contains all methods that get/create or update Collection and associated resources
    """

    @staticmethod
    def CreateCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/CreateCollection',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.CreateCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/GetCollection',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCollections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/GetCollections',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.GetCollectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/DeleteCollection',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.DeleteCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionName',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionDescription',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDescriptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionKeyValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionKeyValues',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionKeyValuesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionDataClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionDataClass',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionDataClassResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SnapshotCollection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/SnapshotCollection',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.SnapshotCollectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateCollectionLicenses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.CollectionService/UpdateCollectionLicenses',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_collection__service__pb2.UpdateCollectionLicensesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
