from datetime import datetime

from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout

from gui.widgets.central_menu import CentralMenu

class CommandHistoryTab(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        
        self.name = "Command History"

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def update_output(self, data_packet):
        now = datetime.now()
        year_month_day_time = now.strftime("%Y/%m/%d, %H:%M:%S")
        file_name = data_packet["file_name"]
        file_path = data_packet["file_path"]
        message = f"> [{year_month_day_time}]: Now reading [{file_name}] from [{file_path}]"
        self.text_edit.append(message)

    def closeEvent(self, event):
        self.thread.stop()
        self.thread.wait()
        event.accept()