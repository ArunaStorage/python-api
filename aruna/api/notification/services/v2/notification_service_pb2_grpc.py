# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.notification.services.v2 import notification_service_pb2 as aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2


class EventNotificationServiceStub(object):
    """EventNotificationService

    A service to receive events in the AOS storage
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStreamConsumer = channel.unary_unary(
                '/aruna.api.notification.services.v2.EventNotificationService/CreateStreamConsumer',
                request_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerResponse.FromString,
                )
        self.GetEventMessageBatch = channel.unary_unary(
                '/aruna.api.notification.services.v2.EventNotificationService/GetEventMessageBatch',
                request_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchResponse.FromString,
                )
        self.GetEventMessageStream = channel.unary_stream(
                '/aruna.api.notification.services.v2.EventNotificationService/GetEventMessageStream',
                request_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamResponse.FromString,
                )
        self.AcknowledgeMessageBatch = channel.unary_unary(
                '/aruna.api.notification.services.v2.EventNotificationService/AcknowledgeMessageBatch',
                request_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchResponse.FromString,
                )
        self.DeleteStreamConsumer = channel.unary_unary(
                '/aruna.api.notification.services.v2.EventNotificationService/DeleteStreamConsumer',
                request_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerResponse.FromString,
                )


class EventNotificationServiceServicer(object):
    """EventNotificationService

    A service to receive events in the AOS storage
    """

    def CreateStreamConsumer(self, request, context):
        """CreateStreamConsumer

        Creates a new event stream consumer.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventMessageBatch(self, request, context):
        """GetEventMessageBatch

        Reads a set of messages from a given stream group 
        Each message contains a separate acknowledgement message thatis protected by a salt and an hmac for verification.
        The message can be send directly through the AcknowledgeMessageBatch call to acknowledge the message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEventMessageStream(self, request, context):
        """GetEventMessageBatch

        Opens a stream which pushes each received notification individual and just-in-time.
        Each message contains a separate acknowledgement message that is protected by a salt and an hmac for verification.
        The message can be send directly through the AcknowledgeMessageBatch call to acknowledge the message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcknowledgeMessageBatch(self, request, context):
        """AcknowledgeMessageBatch

        List of messages to acknowledge
        Each reply is protected by a salt and and hmac that verifies the message
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStreamConsumer(self, request, context):
        """DeleteEventStreamingGroup

        Deletes an existing event stream consumer by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventNotificationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStreamConsumer': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStreamConsumer,
                    request_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerRequest.FromString,
                    response_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerResponse.SerializeToString,
            ),
            'GetEventMessageBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEventMessageBatch,
                    request_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchRequest.FromString,
                    response_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchResponse.SerializeToString,
            ),
            'GetEventMessageStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetEventMessageStream,
                    request_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamRequest.FromString,
                    response_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamResponse.SerializeToString,
            ),
            'AcknowledgeMessageBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.AcknowledgeMessageBatch,
                    request_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchRequest.FromString,
                    response_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchResponse.SerializeToString,
            ),
            'DeleteStreamConsumer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStreamConsumer,
                    request_deserializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerRequest.FromString,
                    response_serializer=aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.notification.services.v2.EventNotificationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventNotificationService(object):
    """EventNotificationService

    A service to receive events in the AOS storage
    """

    @staticmethod
    def CreateStreamConsumer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.notification.services.v2.EventNotificationService/CreateStreamConsumer',
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerRequest.SerializeToString,
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.CreateStreamConsumerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventMessageBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.notification.services.v2.EventNotificationService/GetEventMessageBatch',
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchRequest.SerializeToString,
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEventMessageStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/aruna.api.notification.services.v2.EventNotificationService/GetEventMessageStream',
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamRequest.SerializeToString,
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.GetEventMessageStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcknowledgeMessageBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.notification.services.v2.EventNotificationService/AcknowledgeMessageBatch',
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchRequest.SerializeToString,
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.AcknowledgeMessageBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStreamConsumer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.notification.services.v2.EventNotificationService/DeleteStreamConsumer',
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerRequest.SerializeToString,
            aruna_dot_api_dot_notification_dot_services_dot_v2_dot_notification__service__pb2.DeleteStreamConsumerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
