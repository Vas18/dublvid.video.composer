from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
from urllib.parse import urlparse
import os


#Функция подключения к серверу
class Azure():
    def __init__(self):
        #Получение значение переменных среды
        load_dotenv()
        self.account = os.getenv("ACCOUNT_NAME")
        self.conn_str = os.getenv("CONNECT_STR")
        self.input_container = os.getenv("INPUT_CONTAINER_NAME")
        self.output_container = os.getenv("OUTPUT_CONTAINER_NAME")

    #Получаем имя файла
    def GetBlobName(self, url):
        parsed_url = urlparse(url)
        path = parsed_url.path
        filename = path.split('/')[-1]
        return filename

    def DownloadBlob(self, url):
        #Получем имя объекта из ссылки
        blob_name = self.GetBlobName(url)

        #Образуем соединение
        blob_service_client = BlobServiceClient.from_connection_string(self.conn_str)
        blob_client = blob_service_client.get_blob_client(container=self.input_container, blob=blob_name)
        
        #Создаем директорию если её нету
        if not os.path.exists('media'):
            os.makedirs('media')

        #Сохранение
        file_path = os.path.join('media', blob_name)
        with open(file=file_path, mode="wb") as sample_blob:
            download_stream = blob_client.download_blob()
            sample_blob.write(download_stream.readall())
        print(f"Скачивание {blob_name} завершено.")
        return file_path

    def UploadBlob(self, out_path):
        filename = out_path.replace("media/", "")
        blob = BlobClient.from_connection_string(conn_str=self.conn_str, container_name=self.output_container, blob_name=filename)
        with open(out_path, "rb") as data:
            blob.upload_blob(data, overwrite=True)
        return blob.primary_endpoint
    