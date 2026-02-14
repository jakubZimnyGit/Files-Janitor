from ast import While
import time
from pathlib import Path
from watchdog.observers import Observer
from handler import FileMoveHandler


class Watcher:

    def __init__(self, path_to_watch: Path):
        self.path_to_watch = path_to_watch
        self.handler = FileMoveHandler()  
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