import os
import logging
import sys
from azure.storage.blob import ContainerClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def get_blob_container_client():
    storage_account = "21312wsaasas"
    container_name = "testeasd"

    sas_token = os.getenv("AZURE_STORAGE_SAS")

    if not sas_token:
        logging.error("AZURE_STORAGE_SAS no está definido.")
        sys.exit(1)

    account_url = f"https://{storage_account}.blob.core.windows.net"

    return ContainerClient(
        account_url=account_url,
        container_name=container_name,
        credential=sas_token
    )

def list_blobs():
    try:
        container_client = get_blob_container_client()

        logging.info("Intentando listar blobs...")
        blobs = list(container_client.list_blobs())

        logging.info(f"Conexión exitosa. Total blobs encontrados: {len(blobs)}")

        for blob in blobs:
            logging.info(f"Blob: {blob.name}")

    except Exception as e:
        logging.error(f"Error de conexión o listado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    list_blobs()
