# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sciobjsdb.api.storage.services.v1 import object_load_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2


class ObjectLoadServiceStub(object):
    """Handles object up and downloads
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUploadLink = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateUploadLink',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkResponse.FromString,
                )
        self.CreateDownloadLink = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLink',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkResponse.FromString,
                )
        self.CreateDownloadLinkBatch = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLinkBatch',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchResponse.FromString,
                )
        self.CreateDownloadLinkStream = channel.unary_stream(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLinkStream',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamResponse.FromString,
                )
        self.StartMultipartUpload = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/StartMultipartUpload',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadResponse.FromString,
                )
        self.GetMultipartUploadLink = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/GetMultipartUploadLink',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkResponse.FromString,
                )
        self.CompleteMultipartUpload = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CompleteMultipartUpload',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadResponse.FromString,
                )


class ObjectLoadServiceServicer(object):
    """Handles object up and downloads
    """

    def CreateUploadLink(self, request, context):
        """Creates an upload link for an object to upload the actual data object
        Returns a presigned https PUT request
        Can only be used to upload objects < 4GB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDownloadLink(self, request, context):
        """Creates a download link for an object
        Returns a presigned https GET request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDownloadLinkBatch(self, request, context):
        """Creates links for multiple objects at once
        The order of the requested objects is preserved in the response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDownloadLinkStream(self, request, context):
        """Creates a stream of objects and presigned links based on the provided query
        This can be used retrieve a large number of ObjectGroups as a stream that would otherwise cause issues with the connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartMultipartUpload(self, request, context):
        """Initiates a multipart upload for an object
        This is intended to be used for larger objects
        For further information please read the Amazon S3 documentation on multipart uploads
        Has to be used together with GetMultipartUploadLink and CompleteMultipartUpload
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMultipartUploadLink(self, request, context):
        """Returns a part of an multipart upload.
        Each but the last part needs to be bigger than 5MB in order to use this functionality
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CompleteMultipartUpload(self, request, context):
        """CompleteMultipartUploadRequest Finishes a multipart upload after all parts have been uploaded
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ObjectLoadServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUploadLink': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUploadLink,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkResponse.SerializeToString,
            ),
            'CreateDownloadLink': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDownloadLink,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkResponse.SerializeToString,
            ),
            'CreateDownloadLinkBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDownloadLinkBatch,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchResponse.SerializeToString,
            ),
            'CreateDownloadLinkStream': grpc.unary_stream_rpc_method_handler(
                    servicer.CreateDownloadLinkStream,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamResponse.SerializeToString,
            ),
            'StartMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.StartMultipartUpload,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadResponse.SerializeToString,
            ),
            'GetMultipartUploadLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMultipartUploadLink,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkResponse.SerializeToString,
            ),
            'CompleteMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.CompleteMultipartUpload,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sciobjsdb.api.storage.services.v1.ObjectLoadService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ObjectLoadService(object):
    """Handles object up and downloads
    """

    @staticmethod
    def CreateUploadLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateUploadLink',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateUploadLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDownloadLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLink',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDownloadLinkBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLinkBatch',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDownloadLinkStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CreateDownloadLinkStream',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CreateDownloadLinkStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartMultipartUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/StartMultipartUpload',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.StartMultipartUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMultipartUploadLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/GetMultipartUploadLink',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.GetMultipartUploadLinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CompleteMultipartUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.ObjectLoadService/CompleteMultipartUpload',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_object__load__models__pb2.CompleteMultipartUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
