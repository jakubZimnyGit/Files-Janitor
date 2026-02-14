from pathlib import Path
from watcher import FolderWatcher

WATCH_PATH = Path(r'C:\Users\jakub\Downloads')

DIRECTORIES_CONFIG = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z"],
    "Executables": [".exe", ".msi"]
}

def main():
    if not WATCH_PATH.exists():
        print(f"Błąd: Folder {WATCH_PATH} nie istnieje. Sprawdź ścieżkę w main.py.")
        return    
    
    app = FolderWatcher(WATCH_PATH, DIRECTORIES_CONFIG)
    
    try:
        app.start()
    except Exception as e:
        print(f"Wystąpił krytyczny błąd podczas pracy programu: {e}")

if __name__ == "__main__":
    main()