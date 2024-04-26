import os
from file_operations import get_eledia_files, sort_files, extract_texts

def eledia_text(id_input, directory_input):
    """
    Extrahiert Texte aus .eledia-Dateien basierend auf einer ID und einem Verzeichnis.

    Parameters:
    id_input (int): Die ID, nach der gesucht werden soll.
    directory_input (str): Der Pfad zum Verzeichnis, in dem nach .eledia-Dateien gesucht werden soll.

    Returns:
    str: Eine Zeichenfolge mit den extrahierten Texten, getrennt durch Leerzeichen.
    """
    # Liste aller .eledia-Dateien im Verzeichnis und seinen Unterverzeichnissen erhalten
    eledia_files = get_eledia_files(directory_input)

    # Dateien gemäß den Anforderungen der Aufgabe sortieren
    sorted_files = sort_files(eledia_files)

    # Texte extrahieren, die der gegebenen ID entsprechen
    texts = extract_texts(id_input, sorted_files)

    # Die extrahierten Texte mit einem Leerzeichen verbinden und zurückgeben
    return ' '.join(texts)

if __name__ == "__main__":
    try:
        id_input = int(input("Bitte geben Sie die ID ein: "))
        directory_input = input("Bitte geben Sie den Verzeichnis-Pfad ein: ")

        # Überprüfe, ob das Verzeichnis existiert
        if not os.path.isdir(directory_input):
            raise ValueError("Das angegebene Verzeichnis existiert nicht.")

        result = eledia_text(id_input, directory_input)
        
        # Überprüfe, ob Texte für die angegebene ID gefunden wurden
        if not result:
            print(f"Es wurden keine Texte für die ID {id_input} gefunden.")
        else:
            print("Ergebnis:", result)

        # Zusätzlich alle .eledia-Dateien ausgeben
        eledia_files = get_eledia_files(directory_input)
        for file in eledia_files:
            with open(file, 'r') as f:
                file_content = f.read()
                print(f"Inhalt von {file}:")
                print(file_content)
                print()  # Leerzeile zur besseren Lesbarkeit einfügen

    except ValueError as e:
        print("Fehler:", e)
