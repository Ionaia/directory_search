import os
import concurrent.futures

def get_eledia_files(directory):
    """
    Sucht nach .eledia-Dateien im angegebenen Verzeichnis und seinen Unterverzeichnissen.

    Parameters:
    directory (str): Der Pfad zum Verzeichnis, in dem nach .eledia-Dateien gesucht werden soll.

    Returns:
    list: Eine Liste mit den gefundenen .eledia-Dateien.
    """
    eledia_files = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".eledia"):
                    eledia_files.append(os.path.join(root, file))
    return eledia_files

def sort_files(files):
    """
    Sortiert die Liste der Dateipfade gemäß den Anforderungen der Aufgabe.

    Parameters:
    files (list): Eine Liste mit den Dateipfaden, die sortiert werden sollen.

    Returns:
    list: Die sortierte Liste der Dateipfade.
    """
    return sorted(files)

def process_file(file):
    """
    Extrahiert Texte aus einer .eledia-Datei.

    Parameters:
    file (str): Der Pfad zur .eledia-Datei.

    Returns:
    list: Eine Liste mit den extrahierten Texten.
    """
    texts = []
    with open(file, 'r') as f:
        for line in f:
            line_id, text = line.strip().split(':', 1)
            texts.append(text.strip())
    return texts

def extract_texts(id, files):
    """
    Extrahiert den Text, der zu einer bestimmten ID gehört, aus einer Liste von Dateien.

    Parameters:
    id (int): Die ID, nach der gesucht werden soll.
    files (list): Eine Liste mit den Dateipfaden, in denen nach der ID gesucht werden soll.

    Returns:
    list: Eine Liste mit den extrahierten Texten.
    """
    texts = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                line_id, text = line.strip().split(':', 1)
                if int(line_id) == id:
                    texts.append(text.strip())
                    break
    return texts
