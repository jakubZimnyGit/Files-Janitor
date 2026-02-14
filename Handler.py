from pathlib import Path
from watchdog.events import FileSystemEventHandler

class FileMoveHandler(FileSystemEventHandler):
    def __init__(self, config: dict):
        # Przyjmujemy słownik z main.py
        self.directories = config

    def on_created(self, event):
        if not event.is_directory:
            self._process_file(Path(event.src_path))

    def _process_file(self, file_path: Path):
        extension = file_path.suffix.lower()
        
        # Używamy self.directories przekazanego w __init__
        for directory_name, extensions in self.directories.items():
            if extension in extensions:
                dest_dir = Path(file_path.parent) / directory_name
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                destination = dest_dir / file_path.name
                
                if not destination.exists():
                    try:
                        file_path.rename(destination)
                        print(f"Moved: {file_path.name}")
                    except Exception as e:
                        print(f"Error: {e}")
                break
    

    
        