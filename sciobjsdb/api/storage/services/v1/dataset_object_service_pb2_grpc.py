# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sciobjsdb.api.storage.services.v1 import dataset_object_service_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2


class DatasetObjectsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateObjectGroup = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/CreateObjectGroup',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupResponse.FromString,
                )
        self.CreateObjectGroupBatch = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/CreateObjectGroupBatch',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchResponse.FromString,
                )
        self.GetObjectGroup = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/GetObjectGroup',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupResponse.FromString,
                )
        self.FinishObjectUpload = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/FinishObjectUpload',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadResponse.FromString,
                )
        self.FinishObjectGroupUpload = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/FinishObjectGroupUpload',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadResponse.FromString,
                )
        self.DeleteObjectGroup = channel.unary_unary(
                '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/DeleteObjectGroup',
                request_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupRequest.SerializeToString,
                response_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupResponse.FromString,
                )


class DatasetObjectsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateObjectGroup(self, request, context):
        """Creates a new object group
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateObjectGroupBatch(self, request, context):
        """Batch request of CreateObjectGroup
        The call will preserve the ordering of the request in the response
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetObjectGroup(self, request, context):
        """Returns the object group with the given ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinishObjectUpload(self, request, context):
        """Finishes the upload process for an object
        This will change the status of the objects to "available"
        Experimental, might change this to FinishObjectGroupUpload
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FinishObjectGroupUpload(self, request, context):
        """Finishes the upload process for an objectgroup
        This will change the status of the objectgroup to "available"
        Experimental, might change this to FinishObjectGroupUpload
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteObjectGroup(self, request, context):
        """Deletes the given object group
        This will also delete all associated objects both as metadata objects and the actual objects in the object storage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasetObjectsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateObjectGroup,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupResponse.SerializeToString,
            ),
            'CreateObjectGroupBatch': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateObjectGroupBatch,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchResponse.SerializeToString,
            ),
            'GetObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetObjectGroup,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupResponse.SerializeToString,
            ),
            'FinishObjectUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishObjectUpload,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadResponse.SerializeToString,
            ),
            'FinishObjectGroupUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.FinishObjectGroupUpload,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadResponse.SerializeToString,
            ),
            'DeleteObjectGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteObjectGroup,
                    request_deserializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupRequest.FromString,
                    response_serializer=sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sciobjsdb.api.storage.services.v1.DatasetObjectsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasetObjectsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/CreateObjectGroup',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateObjectGroupBatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/CreateObjectGroupBatch',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.CreateObjectGroupBatchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/GetObjectGroup',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.GetObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishObjectUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/FinishObjectUpload',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FinishObjectGroupUpload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/FinishObjectGroupUpload',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.FinishObjectGroupUploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteObjectGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sciobjsdb.api.storage.services.v1.DatasetObjectsService/DeleteObjectGroup',
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupRequest.SerializeToString,
            sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2.DeleteObjectGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
