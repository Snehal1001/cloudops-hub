from uuid import uuid4

from azure.storage.blob import BlobServiceClient

from app.core.config import settings

blob_service_client = BlobServiceClient.from_connection_string(
    settings.AZURE_STORAGE_CONNECTION_STRING
)

container_client = blob_service_client.get_container_client(
    settings.AZURE_STORAGE_CONTAINER
)

class BlobService:
    @staticmethod
    def upload_file(file_name: str, file_data):
        unique_file_name = f"{uuid4()}-{file_name}"
        
        blob_client = container_client.get_blob_client(
            unique_file_name
        )

        blob_client.upload_blob(file_data)

        return blob_client.url