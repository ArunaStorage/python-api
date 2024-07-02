# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v2 import info_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2


class StorageStatusServiceStub(object):
    """StorageStatusService

    Status: BETA

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of storage components
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStorageVersion = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetStorageVersion',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.FromString,
                )
        self.GetStorageStatus = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetStorageStatus',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.FromString,
                )
        self.GetPubkeys = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetPubkeys',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.FromString,
                )
        self.GetAnnouncements = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncements',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsResponse.FromString,
                )
        self.GetAnnouncementsByType = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncementsByType',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeResponse.FromString,
                )
        self.GetAnnouncement = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncement',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementResponse.FromString,
                )
        self.SetAnnouncements = channel.unary_unary(
                '/aruna.api.storage.services.v2.StorageStatusService/SetAnnouncements',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsResponse.FromString,
                )


class StorageStatusServiceServicer(object):
    """StorageStatusService

    Status: BETA

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of storage components
    """

    def GetStorageVersion(self, request, context):
        """GetStorageVersion

        Status: BETA

        A request to get the current version of the server application
        String representation and https://semver.org/
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStorageStatus(self, request, context):
        """GetStorageStatus

        Status: ALPHA

        A request to get the current status of the storage components by location(s)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPubkeys(self, request, context):
        """GetPubkeys

        Status: BETA

        Get all public keys of all storage components
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnnouncements(self, request, context):
        """Get Announcements

        Status: BETA

        Query global announcements optionally filtered by specific ids. 
        - Returns all announcements if no ids are provided
        - Returns only the specific announcements if ids are provided
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnnouncementsByType(self, request, context):
        """GetAnnouncementsByType

        Status: BETA

        Query global announcements by type
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnnouncement(self, request, context):
        """Get a specific Announcement

        Status: BETA

        Query a specific global announcement by its id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAnnouncements(self, request, context):
        """SetAnnouncements

        Status: BETA

        Update / add global announcements
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StorageStatusServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStorageVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageVersion,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.SerializeToString,
            ),
            'GetStorageStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageStatus,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.SerializeToString,
            ),
            'GetPubkeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPubkeys,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.SerializeToString,
            ),
            'GetAnnouncements': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnnouncements,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsResponse.SerializeToString,
            ),
            'GetAnnouncementsByType': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnnouncementsByType,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeResponse.SerializeToString,
            ),
            'GetAnnouncement': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnnouncement,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementResponse.SerializeToString,
            ),
            'SetAnnouncements': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAnnouncements,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v2.StorageStatusService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StorageStatusService(object):
    """StorageStatusService

    Status: BETA

    This is a generic service that contains utility functions 
    these functions are used to query additional meta-information
    about the status of storage components
    """

    @staticmethod
    def GetStorageVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetStorageVersion',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStorageStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetStorageStatus',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetStorageStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPubkeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetPubkeys',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetPubkeysResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnnouncements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncements',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnnouncementsByType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncementsByType',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementsByTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnnouncement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/GetAnnouncement',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.GetAnnouncementResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAnnouncements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.StorageStatusService/SetAnnouncements',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_info__service__pb2.SetAnnouncementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
