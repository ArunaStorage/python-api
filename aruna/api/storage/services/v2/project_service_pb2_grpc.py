# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from aruna.api.storage.services.v2 import project_service_pb2 as aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2


class ProjectServiceStub(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateProject = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/CreateProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/GetProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectResponse.FromString,
                )
        self.GetProjects = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/GetProjects',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsResponse.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/DeleteProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectResponse.FromString,
                )
        self.UpdateProjectName = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/UpdateProjectName',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameResponse.FromString,
                )
        self.UpdateProjectDescription = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/UpdateProjectDescription',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionResponse.FromString,
                )
        self.UpdateProjectKeyValues = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/UpdateProjectKeyValues',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesResponse.FromString,
                )
        self.UpdateProjectDataClass = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/UpdateProjectDataClass',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassResponse.FromString,
                )
        self.UpdateProjectLicenses = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/UpdateProjectLicenses',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesResponse.FromString,
                )
        self.ArchiveProject = channel.unary_unary(
                '/aruna.api.storage.services.v2.ProjectService/ArchiveProject',
                request_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectRequest.SerializeToString,
                response_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectResponse.FromString,
                )


class ProjectServiceServicer(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    def CreateProject(self, request, context):
        """CreateProject

        Status: BETA

        Creates a new project. All subsequent resources are part of a project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """GetProject

        Status: BETA

        Requests a project (by id)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjects(self, request, context):
        """GetProjects

        Status: BETA

        Admin request to get all projects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """DeleteProject

        Status: BETA

        Deletes the project and all its associated data. Must be empty!
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectName(self, request, context):
        """UpdateProjectName

        Status: BETA

        Updates the project name. Caveat! Will rename the "s3 bucket" for data proxies! 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectDescription(self, request, context):
        """UpdateProjectDescription

        Status: BETA

        Updates the project name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectKeyValues(self, request, context):
        """UpdateProjectKeyValues

        Status: BETA

        Updates the project key values.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectDataClass(self, request, context):
        """UpdateProjectDataClass

        Status: BETA

        Updates the project name. All (meta) data will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectLicenses(self, request, context):
        """UpdateLicense

        Status: BETA

        Updates the project license. All (meta) data will be overwritten.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArchiveProject(self, request, context):
        """ArchiveProjectRequest

        Status: BETA

        Archives the full project, rendering all downstream relations immutable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectResponse.SerializeToString,
            ),
            'GetProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjects,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsResponse.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectResponse.SerializeToString,
            ),
            'UpdateProjectName': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectName,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameResponse.SerializeToString,
            ),
            'UpdateProjectDescription': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectDescription,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionResponse.SerializeToString,
            ),
            'UpdateProjectKeyValues': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectKeyValues,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesResponse.SerializeToString,
            ),
            'UpdateProjectDataClass': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectDataClass,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassResponse.SerializeToString,
            ),
            'UpdateProjectLicenses': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectLicenses,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesResponse.SerializeToString,
            ),
            'ArchiveProject': grpc.unary_unary_rpc_method_handler(
                    servicer.ArchiveProject,
                    request_deserializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectRequest.FromString,
                    response_serializer=aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'aruna.api.storage.services.v2.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """ProjectService

    Contains all methods that get/create or update Projects and associated resources
    """

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/CreateProject',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/GetProject',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/GetProjects',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.GetProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/DeleteProject',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.DeleteProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/UpdateProjectName',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectDescription(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/UpdateProjectDescription',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDescriptionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectKeyValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/UpdateProjectKeyValues',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectKeyValuesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectDataClass(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/UpdateProjectDataClass',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectDataClassResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectLicenses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/UpdateProjectLicenses',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.UpdateProjectLicensesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArchiveProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/aruna.api.storage.services.v2.ProjectService/ArchiveProject',
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectRequest.SerializeToString,
            aruna_dot_api_dot_storage_dot_services_dot_v2_dot_project__service__pb2.ArchiveProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
