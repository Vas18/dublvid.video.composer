from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv
import os

#Функция подключения к серверу
def ConnectToAzure():
    #Получение значение переменных среды
    load_dotenv()
    account = os.getenv("ACCOUNT_NAME")
    conn_str = os.getenv("CONNECT_STR")
    input_container = os.getenv("INPUT_CONTAINER_NAME")
    output_container = os.getenv("OUTPUT_CONTAINER_NAME")
    
    #Установка соединения=
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    
    #Получение данных из контейнера
    container_client = blob_service_client.get_container_client(input_container)
    blob_list = []
    for blob_i in container_client.list_blobs():
        blob_list.append(blob_i.name)
    print(blob_list)

def main():
    ConnectToAzure()

if __name__ == "__main__":
    main()