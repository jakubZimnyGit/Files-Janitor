from pathlib import Path
from watchdog.events import FileSystemEventHandler

directories = {"C:\Users\jakub\Documents": [".pdf", ".docx", ".txt"],
               "C:\Users\jakub\Pictures": [".jpg", ".png", ".jpeg"],
               "C:\Users\jakub\Music": [".mp3", ".wav", ".flac"]}

class FileMoveHandler(FileSystemEventHandler):
    
    def on_modified(self, event):
        if not event.is_directory:
            self._process_file(Path(event.src_path))
    
    def _process_file(self, file_path: Path):
        extension = file_path.suffix.lower()
        for directory_name, extensions in directories.items():
        
            if extension in extensions:
                dest_dir = Path(directory_name)
                dest_dir.mkdir(parents=True, exist_ok=True)
                destination = dest_dir / file_path.name

                if destination.exists():
                    print(f"Ostrzeżenie: Plik {file_path.name} już istnieje w miejscu docelowym.")
                    return 

                try:
                    file_path.rename(destination)
                    print(f"Sukces: Przeniesiono {file_path.name} do {directory_name}")
                except PermissionError:
                    print(f"Błąd: Brak uprawnień do przeniesienia {file_path.name}")
                except Exception as e:
                    print(f"Wystąpił nieoczekiwany błąd: {e}")

                break
    

    
        