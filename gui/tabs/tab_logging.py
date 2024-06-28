from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

from gui.widgets.central_menu import CentralMenu
from gui.threads.file_watcher import FileWatcherThread

class LoggingTab(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        
        self.name = "Reconstructed Logs"

        self.thread = FileWatcherThread()
        self.thread.result_signal.connect(self.update_output)
        self.thread.start()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def update_output(self, result):
        self.text_edit.append(result)

    def closeEvent(self, event):
        self.thread.stop()
        self.thread.wait()
        event.accept()