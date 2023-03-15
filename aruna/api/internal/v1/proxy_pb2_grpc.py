# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.internal.v1 import proxy_pb2 as aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2


class InternalProxyServiceStub(object):
    """Definition for the internal API that is used to communicate with all internal
    components.

    All uploads should follow this procedure:
    1. Init a new upload.
    2. Create a Upload Presigned URL (The URL should contain a specifier for the
    upload and part id)
    3. Use the presigned URL to upload individual parts, 1-x times.
    4. When all parts are uploaded, call FinishPresignedUpload to complete the
    upload and provide the parts list.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitMultipartUpload = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyService/InitMultipartUpload',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadResponse.FromString,
                )
        self.FinishMultipartUpload = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyService/FinishMultipartUpload',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadResponse.FromString,
                )
        self.DeleteObject = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyService/DeleteObject',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectResponse.FromString,
                )


class InternalProxyServiceServicer(object):
    """Definition for the internal API that is used to communicate with all internal
    components.

    All uploads should follow this procedure:
    1. Init a new upload.
    2. Create a Upload Presigned URL (The URL should contain a specifier for the
    upload and part id)
    3. Use the presigned URL to upload individual parts, 1-x times.
    4. When all parts are uploaded, call FinishPresignedUpload to complete the
    upload and provide the parts list.

    """

    def InitMultipartUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinishMultipartUpload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InternalProxyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.InitMultipartUpload,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadResponse.SerializeToString,
            ),
            'FinishMultipartUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishMultipartUpload,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadResponse.SerializeToString,
            ),
            'DeleteObject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteObject,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.internal.v1.InternalProxyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InternalProxyService(object):
    """Definition for the internal API that is used to communicate with all internal
    components.

    All uploads should follow this procedure:
    1. Init a new upload.
    2. Create a Upload Presigned URL (The URL should contain a specifier for the
    upload and part id)
    3. Use the presigned URL to upload individual parts, 1-x times.
    4. When all parts are uploaded, call FinishPresignedUpload to complete the
    upload and provide the parts list.

    """

    @staticmethod
    def InitMultipartUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyService/InitMultipartUpload',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.InitMultipartUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishMultipartUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyService/FinishMultipartUpload',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinishMultipartUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyService/DeleteObject',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.DeleteObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class InternalProxyNotifierServiceStub(object):
    """This service enables a "return" channel for dataproxy to aruna server communication
    Mainly used to notify the backend of validation / move events after the upload of new files
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetOrCreateObjectByPath = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyNotifierService/GetOrCreateObjectByPath',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathResponse.FromString,
                )
        self.FinalizeObject = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyNotifierService/FinalizeObject',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectResponse.FromString,
                )
        self.GetEncryptionKey = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyNotifierService/GetEncryptionKey',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyResponse.FromString,
                )
        self.GetObjectLocation = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyNotifierService/GetObjectLocation',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationResponse.FromString,
                )
        self.GetCollectionByBucket = channel.unary_unary(
                '/aruna.api.internal.v1.InternalProxyNotifierService/GetCollectionByBucket',
                request_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketResponse.FromString,
                )


class InternalProxyNotifierServiceServicer(object):
    """This service enables a "return" channel for dataproxy to aruna server communication
    Mainly used to notify the backend of validation / move events after the upload of new files
    """

    def GetOrCreateObjectByPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinalizeObject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEncryptionKey(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectLocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCollectionByBucket(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InternalProxyNotifierServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetOrCreateObjectByPath': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrCreateObjectByPath,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathResponse.SerializeToString,
            ),
            'FinalizeObject': grpc.unary_unary_rpc_method_handler(
                    servicer.FinalizeObject,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectResponse.SerializeToString,
            ),
            'GetEncryptionKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEncryptionKey,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyResponse.SerializeToString,
            ),
            'GetObjectLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectLocation,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationResponse.SerializeToString,
            ),
            'GetCollectionByBucket': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCollectionByBucket,
                    request_deserializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketRequest.FromString,
                    response_serializer=aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.internal.v1.InternalProxyNotifierService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InternalProxyNotifierService(object):
    """This service enables a "return" channel for dataproxy to aruna server communication
    Mainly used to notify the backend of validation / move events after the upload of new files
    """

    @staticmethod
    def GetOrCreateObjectByPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyNotifierService/GetOrCreateObjectByPath',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetOrCreateObjectByPathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinalizeObject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyNotifierService/FinalizeObject',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.FinalizeObjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEncryptionKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyNotifierService/GetEncryptionKey',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetEncryptionKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyNotifierService/GetObjectLocation',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetObjectLocationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCollectionByBucket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.internal.v1.InternalProxyNotifierService/GetCollectionByBucket',
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketRequest.SerializeToString,
            aruna_dot_api_dot_internal_dot_v1_dot_proxy__pb2.GetCollectionByBucketResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
