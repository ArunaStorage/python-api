from pprint import pprint
import grpc
import requests

from sciobjsdb.api.storage.services.v1.dataset_object_service_pb2_grpc import DatasetObjectsServiceStub
from sciobjsdb.api.storage.services.v1.dataset_service_pb2_grpc import DatasetServiceStub
from sciobjsdb.api.storage.services.v1.object_load_pb2_grpc import ObjectLoadServiceStub
from sciobjsdb.api.storage.services.v1.project_service_pb2_grpc import ProjectServiceStub

from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import CreateDatasetRequest, GetDatasetObjectsRequest, GetDatasetObjectsResponse
from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import CreateDatasetResponse
from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import GetDatasetRequest
from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import GetDatasetResponse
from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import GetDatasetObjectGroupsRequest
from sciobjsdb.api.storage.services.v1.dataset_service_models_pb2 import GetDatasetObjectGroupsResponse


from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import AddObjectRequest, CreateObjectRequest, FinishObjectUploadResponse, UpdateObjectGroupRequest, UpdateObjectsRequests
from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectResponse
from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import FinishObjectUploadRequest
from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import FinishObjectUploadRequest


from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectGroupRequest
from sciobjsdb.api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectGroupResponse

from sciobjsdb.api.storage.services.v1.object_load_models_pb2 import CreateDownloadLinkRequest
from sciobjsdb.api.storage.services.v1.object_load_models_pb2 import CreateDownloadLinkResponse

from sciobjsdb.api.storage.models.v1.common_models_pb2 import Label

# Read TLS credentials from local trusted certificates
credentials = grpc.ssl_channel_credentials()

# Create a TLS based channel with the api endpoint using the trusted certs
channel = grpc.secure_channel(
    "api.scienceobjectsdb.nfdi-dev.gi.denbi.de", credentials)

# Create clients for the individual services using the channel
project_client = ProjectServiceStub(channel)
dataset_client = DatasetServiceStub(channel)
dataset_object_client = DatasetObjectsServiceStub(channel)
object_load_client = ObjectLoadServiceStub(channel)


# Set project id and API token obtained from the website
project_id = "id"
api_token = b'token'

# Create the metadata for authentication that needs to be issued with each call
# Please mind the trailing comma
auth_metadata = (('api_token', api_token),)

# Example of an associated label, currently does nothing
label1 = Label()
label1.key = "foo"
label1.value = "baa"

# Create a dataset request
create_dataset_request = CreateDatasetRequest()
create_dataset_request.labels.append(label1)
create_dataset_request.description = "a test dataset"
create_dataset_request.project_id = project_id
create_dataset_request.name = "test"

# Run the call to create a dataset with the request and the metadata for authorization
# Due to the internals of gRPC code generation linting is difficult.
# To make programming easier it is advised to add type hints after call in order have better linting
# Usually this follow the pattern of name of the functioncal + "Response" more details can be found in the
# API description
dataset: CreateDatasetResponse = dataset_client.CreateDataset(
    request=create_dataset_request, metadata=auth_metadata)


# Example of an associated label, currently does nothing
labelfw = Label()
labelfw.key = "genomic.bioinformatics/read_orientation"
labelfw.value = "forward"

# Example of an associated label, currently does nothing
labelrev = Label()
labelrev.key = "genomic.bioinformatics/read_orientation"
labelrev.value = "forward"

# Example of an associated label, currently does nothing
labelexperiment = Label()
labelexperiment.key = "genomic.bioinformatics/experiment_id"
labelexperiment.value = "10"

# Create objects that need to be uploaded in an objectgroup
object1 = CreateObjectRequest()
object1.content_len = 10
object1.filename = "fw_reads.fasta"
object1.filetype = "fasta"
object1.dataset_id = dataset.id
object1.labels.append(labelfw)
object1.labels.append(labelexperiment)

object2 = CreateObjectRequest()
object2.content_len = 15
object2.filename = "rev_reads.fasta"
object2.filetype = "fasta"
object2.dataset_id = dataset.id
object1.labels.append(labelrev)
object1.labels.append(labelexperiment)

object1Response: CreateObjectResponse = dataset_object_client.CreateObject(
    request=object1, metadata=auth_metadata)
object2Response: CreateObjectResponse = dataset_object_client.CreateObject(
    request=object2, metadata=auth_metadata)

requests.put(object1Response.upload_link, data="0123456789")
requests.put(object2Response.upload_link, data="ABCDEFGHIJKLMNO")

object1FinishUploadRequest = FinishObjectUploadRequest()
object1FinishUploadRequest.id = object1Response.id

object2FinishUploadRequest = FinishObjectUploadRequest()
object2FinishUploadRequest.id = object2Response.id


object1FinishResponse: FinishObjectUploadResponse = dataset_object_client.FinishObjectUpload(
    request=object1FinishUploadRequest, metadata=auth_metadata)
object2FinishResponse: FinishObjectUploadResponse = dataset_object_client.FinishObjectUpload(
    request=object2FinishUploadRequest, metadata=auth_metadata)


add_object_1_request: AddObjectRequest = AddObjectRequest()
add_object_1_request.id = object1Response.id

add_object_2_request: AddObjectRequest = AddObjectRequest()
add_object_2_request.id = object2Response.id

# Create the associated object group with
create_object_group_request: CreateObjectGroupRequest = CreateObjectGroupRequest()
create_object_group_request.dataset_id = dataset.id
create_object_group_request.create_revision_request.name = "testrevision"
create_object_group_request.create_revision_request.description = "test"
create_object_group_request.create_revision_request.update_objects.add_objects.append(
    add_object_1_request)
create_object_group_request.create_revision_request.update_objects.add_objects.append(
    add_object_2_request)


# Create the object group
object_group: CreateObjectGroupResponse = dataset_object_client.CreateObjectGroup(
    request=create_object_group_request, metadata=auth_metadata)


get_dataset_request = GetDatasetRequest()
get_dataset_request.id = dataset.id

# Get a dataset by id
dataset_response: GetDatasetResponse = dataset_client.GetDataset(
    request=get_dataset_request, metadata=auth_metadata)
print(dataset_response.dataset.name)

# Get object group by reques
dataset_object_groups_request = GetDatasetObjectGroupsRequest()
dataset_object_groups_request.id = dataset.id

dataset_object_groups: GetDatasetObjectGroupsResponse = dataset_client.GetDatasetObjectGroups(
    request=dataset_object_groups_request, metadata=auth_metadata)
for object_group_from_call in dataset_object_groups.object_groups:
    for object in object_group_from_call.current_revision.objects:
        # Create a presigned download link for an object
        # The link can also be used in a browser
        create_dl_link_request = CreateDownloadLinkRequest()
        create_dl_link_request.id = object.id

        link: CreateDownloadLinkResponse = object_load_client.CreateDownloadLink(
            request=create_dl_link_request, metadata=auth_metadata)
        print(requests.get(link.download_link).text)


get_dataset_objects_request: GetDatasetObjectsRequest = GetDatasetObjectsRequest()
get_dataset_objects_request.id = dataset.id
get_dataset_objects_request.label_filter.labels.append(labelexperiment)

filtered_dataset_objects: GetDatasetObjectsResponse = dataset_client.GetDatasetObjects(
    request=get_dataset_objects_request, metadata=auth_metadata)
pprint(filtered_dataset_objects.objects)
