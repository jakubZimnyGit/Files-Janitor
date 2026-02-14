from ast import While
import time
from pathlib import Path
from watchdog.observers import Observer
from handler import FileMoveHandler


class FolderWatcher:

    def __init__(self, path_to_watch: Path, directories_config: dict = None):
        self.path_to_watch = path_to_watch
        self.handler = FileMoveHandler(directories_config)
        self.observer = Observer()

    def start(self):
        self.observer.schedule(self.handler, str(self.path_to_watch), recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        
        self.observer.join()