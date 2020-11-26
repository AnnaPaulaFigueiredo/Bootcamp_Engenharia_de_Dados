import zipfile
import requests
import os
from io import BytesIO

def create_dir( path: str):

    os.makedirs(path, exist_ok=True)

def download_site( url: str, path: str):

    filebytes = BytesIO( requests.get(url).content )

    my_zip = zipfile.ZipFile(filebytes)
    my_zip.extractall(path)

def main():

    path = "./enem_2019"
    create_dir(path)

    url = "http://download.inep.gov.br/microdados/microdados_enem_2019.zip"
    download_site(url, path)

if __name__ == "__main__":
    main()
    