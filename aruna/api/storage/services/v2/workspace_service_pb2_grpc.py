# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v2 import workspace_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2


class WorkspaceServiceStub(object):
    """Service to manage "special" anonymous collections / workspaces 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateWorkspaceTemplate = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/CreateWorkspaceTemplate',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateResponse.FromString,
                )
        self.GetWorkspaceTemplate = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/GetWorkspaceTemplate',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateResponse.FromString,
                )
        self.ListOwnedWorkspaceTemplates = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/ListOwnedWorkspaceTemplates',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesResponse.FromString,
                )
        self.DeleteWorkspaceTemplate = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/DeleteWorkspaceTemplate',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateResponse.FromString,
                )
        self.CreateWorkspace = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/CreateWorkspace',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceResponse.FromString,
                )
        self.DeleteWorkspace = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/DeleteWorkspace',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceResponse.FromString,
                )
        self.ClaimWorkspace = channel.unary_unary(
                '/aruna.api.storage.services.v2.WorkspaceService/ClaimWorkspace',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceResponse.FromString,
                )


class WorkspaceServiceServicer(object):
    """Service to manage "special" anonymous collections / workspaces 
    """

    def CreateWorkspaceTemplate(self, request, context):
        """CreatesNewWorkspaceTemplate

        Status: ALPHA

        This will create a new template for workspaces (admin only)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWorkspaceTemplate(self, request, context):
        """GetWorkspaceTemplatesById 

        Status: ALPHA

        Gets workspace template by id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOwnedWorkspaceTemplates(self, request, context):
        """ListOwnedWorkspaceTemplates

        Status: ALPHA

        Lists owned workspace templates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteWorkspaceTemplate(self, request, context):
        """DeleteWorkspaceTemplates

        Status: ALPHA

        Deletes specified workspace templates
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWorkspace(self, request, context):
        """CreateWorkspace

        Status: ALPHA

        A new request to create a personal anonymous workspace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteWorkspace(self, request, context):
        """DeleteWorkspace

        Status: ALPHA

        Delete a workspace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClaimWorkspace(self, request, context):
        """DeleteWorkspace

        Status: ALPHA

        Claims an anonymous workspace, and transfers the owner to a regular user account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkspaceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateWorkspaceTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWorkspaceTemplate,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateResponse.SerializeToString,
            ),
            'GetWorkspaceTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWorkspaceTemplate,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateResponse.SerializeToString,
            ),
            'ListOwnedWorkspaceTemplates': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOwnedWorkspaceTemplates,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesResponse.SerializeToString,
            ),
            'DeleteWorkspaceTemplate': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteWorkspaceTemplate,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateResponse.SerializeToString,
            ),
            'CreateWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWorkspace,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceResponse.SerializeToString,
            ),
            'DeleteWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteWorkspace,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceResponse.SerializeToString,
            ),
            'ClaimWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.ClaimWorkspace,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v2.WorkspaceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkspaceService(object):
    """Service to manage "special" anonymous collections / workspaces 
    """

    @staticmethod
    def CreateWorkspaceTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/CreateWorkspaceTemplate',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWorkspaceTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/GetWorkspaceTemplate',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.GetWorkspaceTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOwnedWorkspaceTemplates(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/ListOwnedWorkspaceTemplates',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ListOwnedWorkspaceTemplatesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteWorkspaceTemplate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/DeleteWorkspaceTemplate',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceTemplateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/CreateWorkspace',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.CreateWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/DeleteWorkspace',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.DeleteWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClaimWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.WorkspaceService/ClaimWorkspace',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_workspace__service__pb2.ClaimWorkspaceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
