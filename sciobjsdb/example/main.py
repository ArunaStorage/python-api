import grpc
import requests

from sciobjsdb.api.storage.services.v1.dataset_object_service_pb2_grpc import DatasetObjectsServiceStub
from sciobjsdb.api.storage.services.v1.dataset_service_pb2_grpc import DatasetServiceStub
from sciobjsdb.api.storage.services.v1.object_load_pb2_grpc import ObjectLoadServiceStub
from sciobjsdb.api.storage.services.v1.project_service_pb2_grpc import ProjectServiceStub

from ..api.storage.services.v1.dataset_service_models_pb2 import CreateDatasetRequest
from ..api.storage.services.v1.dataset_service_models_pb2 import CreateDatasetResponse
from ..api.storage.services.v1.dataset_service_models_pb2 import GetDatasetRequest
from ..api.storage.services.v1.dataset_service_models_pb2 import GetDatasetResponse
from ..api.storage.services.v1.dataset_service_models_pb2 import GetDatasetObjectGroupsRequest
from ..api.storage.services.v1.dataset_service_models_pb2 import GetDatasetObjectGroupsResponse

from ..api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectGroupRequest
from ..api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectGroupResponse
from ..api.storage.services.v1.dataset_object_service_models_pb2 import FinishObjectGroupUploadRequest
from ..api.storage.services.v1.dataset_object_service_models_pb2 import FinishObjectGroupUploadResponse


from ..api.storage.services.v1.dataset_object_service_models_pb2 import CreateObjectRequest

from ..api.storage.services.v1.object_load_models_pb2 import CreateDownloadLinkRequest
from ..api.storage.services.v1.object_load_models_pb2 import CreateDownloadLinkResponse




from ..api.storage.models.v1.common_models_pb2 import Label

#Read TLS credentials from local trusted certificates
credentials = grpc.ssl_channel_credentials()

#Create a TLS based channel with the api endpoint using the trusted certs
channel = grpc.secure_channel("api.scienceobjectsdb.nfdi-dev.gi.denbi.de", credentials)

#Create clients for the individual services using the channel
project_client = ProjectServiceStub(channel)
dataset_client = DatasetServiceStub(channel)
dataset_object_client = DatasetObjectsServiceStub(channel)
object_load_client = ObjectLoadServiceStub(channel)


#Set project id and API token obtained from the website
project_id = "3aff6938-f319-4512-bab9-420b5f0f59f3"
api_token =  b'zVGRlnR68qBvK7EPo2/fo2WDHDg4iXQkB8Pd1zl3E7wf4hKhjVjAQRu/Ov10'

#Create the metadata for authentication that needs to be issued with each call
#Please mind the trailing comma
auth_metadata = (('api_token', api_token),)

#Example of an associated label, currently does nothing
label1 = Label()
label1.key = "foo"
label1.value = "baa"

#Create a dataset request
create_dataset_request = CreateDatasetRequest()
create_dataset_request.labels.append(label1)
create_dataset_request.description = "a test dataset"
create_dataset_request.project_id = project_id
create_dataset_request.name = "foo"

#Run the call to create a dataset with the request and the metadata for authorization
#Due to the internals of gRPC code generation linting is difficult.
#To make programming easier it is advised to add type hints after call in order have better linting
#Usually this follow the pattern of name of the functioncal + "Response" more details can be found in the
#API description
dataset: CreateDatasetResponse = dataset_client.CreateDataset(
    request = create_dataset_request, metadata = auth_metadata)

#Create objects that need to be uploaded in an objectgroup
object1 = CreateObjectRequest()
object1.content_len = 10
object1.filename = "file1.bin"
object1.filetype = "bin"

object2 = CreateObjectRequest()
object2.content_len = 15
object2.filename = "file2.bin"
object2.filetype = "bin"


#Create the associated object group with 
create_object_group_request = CreateObjectGroupRequest()
create_object_group_request.dataset_id = dataset.id
create_object_group_request.name = "testdataset"
create_object_group_request.description = "a test object group"
create_object_group_request.labels.append(label1)
#If this is set an upload link will be available for each object
create_object_group_request.include_object_link = True
#Append the objects to the object list
#This will only create a meta object in the core storage, with no underlaying data object
#The underlaying data object has to be uploaded separately and the upload process will only
#be finished if the FinishObjectGroupUpload routine has been called on the associated object group
create_object_group_request.objects.append(object1)
create_object_group_request.objects.append(object2)

#Create the object group
object_group: CreateObjectGroupResponse = dataset_object_client.CreateObjectGroup( request = create_object_group_request, metadata = auth_metadata)

#In the response of the group upload there is a list of upload links for put requests to upload the actual data
#The list appears in order of the original object list and contains details about the meta objects as well as an object upload link
#if the option has been set in the create object group request.
link1 = object_group.object_links[0]
link2 = object_group.object_links[1]

#Upload the actual data
requests.put(link1.link, data="0123456789")
requests.put(link2.link, data="ABCDEFGHIJKLMNO")

#Request to signal that the upload has been finished.
finish_request = FinishObjectGroupUploadRequest()
finish_request.id = object_group.object_group_id

#Finish upload call. After this call no data should be uploaded
dataset_object_client.FinishObjectGroupUpload( request = finish_request, metadata = auth_metadata)



get_dataset_request = GetDatasetRequest()
get_dataset_request.id = dataset.id

#Get a dataset by id
dataset_response: GetDatasetResponse = dataset_client.GetDataset(request = get_dataset_request, metadata = auth_metadata)
print(dataset_response.dataset.name)

#Get object group by reques
dataset_object_groups_request = GetDatasetObjectGroupsRequest()
dataset_object_groups_request.id = dataset.id

dataset_object_groups: GetDatasetObjectGroupsResponse = dataset_client.GetDatasetObjectGroups( request = dataset_object_groups_request, metadata = auth_metadata)
for object_group_from_call in dataset_object_groups.object_groups:
    for object in object_group_from_call.objects:
        #Create a presigned download link for an object
        #The link can also be used in a browser
        create_dl_link_request = CreateDownloadLinkRequest()
        create_dl_link_request.id = object.id
        
        link: CreateDownloadLinkResponse = object_load_client.CreateDownloadLink( request = create_dl_link_request, metadata = auth_metadata)
        print(requests.get(link.download_link).text)
    