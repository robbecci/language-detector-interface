import requests
import tarfile
import os

# URL del file compresso con tutte le frasi di Tatoeba
URL = "https://downloads.tatoeba.org/exports/sentences.tar.bz2"
DEST_ARCHIVE = "data/sentences.tar.bz2"
DEST_FOLDER = "data"

def download_file():
    print("Scaricamento in corso...")
    response = requests.get(URL, stream=True)
    response.raise_for_status()  # si ferma se c'è un errore (es. link rotto)

    with open(DEST_ARCHIVE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Download completato.")

def extract_file():
    print("Estrazione in corso...")
    with tarfile.open(DEST_ARCHIVE, "r:bz2") as tar:
        tar.extractall(DEST_FOLDER)
    print("Estrazione completata.")

if __name__ == "__main__":
    os.makedirs(DEST_FOLDER, exist_ok=True)
    download_file()
    extract_file()