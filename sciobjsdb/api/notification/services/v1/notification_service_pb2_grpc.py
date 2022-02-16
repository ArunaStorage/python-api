# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sciobjsdb.api.notification.services.v1 import notification_service_models_pb2 as sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2


class UpdateNotificationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateEventStreamingGroup = channel.unary_unary(
                '/sciobjsdb.api.notification.services.v1.UpdateNotificationService/CreateEventStreamingGroup',
                request_serializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupResponse.FromString,
                )
        self.NotificationStreamGroup = channel.stream_stream(
                '/sciobjsdb.api.notification.services.v1.UpdateNotificationService/NotificationStreamGroup',
                request_serializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupResponse.FromString,
                )


class UpdateNotificationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateEventStreamingGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NotificationStreamGroup(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UpdateNotificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateEventStreamingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateEventStreamingGroup,
                    request_deserializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupResponse.SerializeToString,
            ),
            'NotificationStreamGroup': grpc.stream_stream_rpc_method_handler(
                    servicer.NotificationStreamGroup,
                    request_deserializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sciobjsdb.api.notification.services.v1.UpdateNotificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UpdateNotificationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateEventStreamingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.notification.services.v1.UpdateNotificationService/CreateEventStreamingGroup',
            sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupRequest.SerializeToString,
            sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.CreateEventStreamingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NotificationStreamGroup(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/sciobjsdb.api.notification.services.v1.UpdateNotificationService/NotificationStreamGroup',
            sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupRequest.SerializeToString,
            sciobjsdb_dot_api_dot_notification_dot_services_dot_v1_dot_notification__service__models__pb2.NotificationStreamGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
