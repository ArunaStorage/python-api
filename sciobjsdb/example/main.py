import grpc
#from sciobjsdb.api.storage.services.v1.project_service_pb2_grpc import ProjectServiceStub
#from sciobjsdb.api.storage.services.v1.dataset_service_pb2_grpc import DatasetServiceStub
#from sciobjsdb.api.storage.services.v1.dataset_object_service_pb2_grpc import DatasetObjectsServiceStub
#from sciobjsdb.api.storage.services.v1.object_load_pb2_grpc import ObjectLoadServiceStub

from ..api.storage.services.v1.dataset_service_models_pb2 import CreateDatasetRequest

#channel = grpc.insecure_channel('test')
#project_client = ProjectServiceStub(channel)
#dataset_client = DatasetServiceStub(channel)
#dataset_object_client = DatasetObjectsServiceStub(channel)
#object_load_client = ObjectLoadServiceStub(channel)

create_dataset_request = CreateDatasetRequest()