from pathlib import Path
from sched import Event
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
        for directory, extensions in directories.items():
            if extension in extensions:
                destination = Path(directory) / file_path.name
                file_path.rename(destination)
                print(f"Moved: {file_path} to {destination}")
                break
    

    
        