from azure.storage.blob import BlobServiceClient
from datetime import datetime
import os
from datetime import datetime
import pytz

CONNECTION_STRING = os.getenv(
    "AZURE_CONNECTION_STRING"
)

CONTAINER_NAME = "bronze"

def upload_file_to_blob(local_file_path):

    # ----------------------------------------
    # CONNECT TO AZURE STORAGE
    # ----------------------------------------

    blob_service_client = (
        BlobServiceClient.from_connection_string(
            CONNECTION_STRING
        )
    )

    # ----------------------------------------
    # CREATE PARTITION PATH
    # ----------------------------------------

    india_timezone = pytz.timezone("Asia/Kolkata")
    today = datetime.now(india_timezone)

    blob_path = (
        f"coingecko/"
        f"year={today.year}/"
        f"month={today.month:02}/"
        f"day={today.day:02}/"
        f"memecoin_data_{today.date()}.csv"
    )

    # ----------------------------------------
    # CREATE BLOB CLIENT
    # ----------------------------------------

    blob_client = blob_service_client.get_blob_client(
        container=CONTAINER_NAME,
        blob=blob_path
    )

    # ----------------------------------------
    # UPLOAD FILE
    # ----------------------------------------

    with open(local_file_path, "rb") as data:

        blob_client.upload_blob(
            data,
            overwrite=True
        )

    print("File uploaded successfully!")
    print(f"Blob Path: {blob_path}")