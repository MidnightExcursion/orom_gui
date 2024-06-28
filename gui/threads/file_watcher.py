import os

import time

from gui.statics.statics import _PATH_FOR_RECONSTRUCTED_DATA, _PATH_FOR_RAW_DATA

from PyQt5.QtCore import QThread, pyqtSignal

from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler

from PyQt5.QtCore import QThread, pyqtSignal

class FileWatcherThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self):

        super().__init__()
        self.running = True

    def run(self):

        # (2): Initialize the function that runs when a *FileSystemEvent* occurs:
        event_handler = FileWatcher(self.result_signal)

        # (3): Initialize a Watchdog Observer:
        observer = Observer()

        # (4): Schedule the event handler:
        observer.schedule(event_handler, _PATH_FOR_RAW_DATA, recursive = False)
        observer.schedule(event_handler, _PATH_FOR_RECONSTRUCTED_DATA, recursive = False)

        # (5): Start the actual observing:
        observer.start()
        self.result_signal.emit(f"> [FileWatcherThread]: Observing raw data at: {_PATH_FOR_RAW_DATA}")
        self.result_signal.emit(f"> [FileWatcherThread]: Observing reconstructed directory at: {_PATH_FOR_RECONSTRUCTED_DATA}")

        # (6.1): Attempt to actually begin watching the directory:
        try:

            while self.running:
                time.sleep(1)

        # (6.2): Error is thrown only if the user exits:
        except KeyboardInterrupt:
            observer.stop()
            self.result_signal.emit(f"> [FileWatcherThread]: Stopped observing raw data at: {_PATH_FOR_RAW_DATA}")
            self.result_signal.emit(f"> [FileWatcherThread]: Stopped observing reconstructed directory at: {_PATH_FOR_RECONSTRUCTED_DATA}")
        
        observer.join()
        self.result_signal.emit(f"> [FileWatcherThread]: Unloaded watchdog observer.")

    def stop(self):
        self.running = False

class FileWatcher(FileSystemEventHandler):

    def __init__(self, result_signal):
        super().__init__()
        self.result_signal = result_signal

    def on_created(self, event):
        self.result_signal.emit("> [FileWatcher]: Detected event!")
        if event.is_directory:
            self.result_signal.emit("> [FileWatcher]: New directory detected!")
        elif event.src_path.endswith('.root'):
            self.result_signal.emit(f"> [FileWatcher]: New .root reconstructed file at: {event.src_path}")
        elif event.src_path.endswith('.npy'):
            self.result_signal.emit(f"> [FileWatcher]: New .npy reconstructed file at: {event.src_path}")
        elif event.src_path.endswith('.npz'):
            self.result_signal.emit(f"> [FileWatcher]: New .npz reconstructed file at: {event.src_path}")