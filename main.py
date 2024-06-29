# Native Package | sys:
import sys

# External Package | PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QTabWidget, QVBoxLayout, QTextEdit

from PyQt5.QtCore import QThread, pyqtSignal, QObject

from gui.widgets.central_menu import CentralMenu

from gui.tabs.tab_main_menu import MainMenuTab
from gui.tabs.tab_logging import LoggingTab
from gui.tabs.tab_vertex import VertexTab
from gui.tabs.tab_mass_histogram import MassHistogramTab
from gui.tabs.tab_hit_matrix import HitMatrixTab
from gui.tabs.tab_history import CommandHistoryTab

from gui.statics.statics import _APPLICATION_NAME
from gui.statics.statics import _WINDOW_MAIN_APP_WIDTH
from gui.statics.statics import _WINDOW_MAIN_APP_HEIGHT

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = _APPLICATION_NAME
        self.setWindowTitle(self.title)

        self.window_left = 100
        self.window_top = 100
        self.window_width = _WINDOW_MAIN_APP_WIDTH
        self.window_height = _WINDOW_MAIN_APP_HEIGHT
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)

        self.initialize_ui()

    def initialize_ui(self):

        # (1): Initialize the central widget that contains all the GUI:
        self.central_widget = QWidget()

        # (2): Initialie the central tab that contains all the GUI tabs:
        self.central_tab = QTabWidget()

        # (3.1): Initialize Tabs | Main Menu / Dashboard
        self.main_menu_tab = MainMenuTab(self.central_tab)

        # (3.2): Initialize Tabs | LoggingTab:
        self.logging_tab = LoggingTab()

        # (3.3): Initialize Tabs | VertexTab:
        self.vertex_tab = VertexTab()

        # (3.4): Initialize Tabs | MassHistogramTab:
        self.mass_histogram = MassHistogramTab()

        # (3.5): Initialize Tabs | HitMatrixTab:
        self.hit_matrix = HitMatrixTab()

        # (3.7): Initialize Tabs | CommandHistoryTab:
        self.command_history = CommandHistoryTab()

        self.main_menu_widget = CentralMenu()
        self.main_menu_widget.state_updated.connect(self.state_update_detected)

        # (): Adding tabs to the central layout:
        self.central_tab.addTab(self.main_menu_tab, self.main_menu_tab.name)
        self.central_tab.addTab(self.vertex_tab, self.vertex_tab.name)
        self.central_tab.addTab(self.mass_histogram, self.mass_histogram.name)
        self.central_tab.addTab(self.hit_matrix, self.hit_matrix.name)
        self.central_tab.addTab(self.logging_tab, self.logging_tab.name)
        self.central_tab.addTab(self.command_history, self.command_history.name)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.main_menu_widget)
        self.layout.addWidget(self.central_tab)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def propagate_data_to_tabs(self, data_packet):
        """
        # Description:
        We pass the data packet from the `.npy` file to all
        of the tabs that require it for plotting.
        """
        reconstructed_data_filename = data_packet['filename']
        reconstructed_data_filepath = data_packet['filepath']
        reconstructed_data_output_data = data_packet['file_output_data']
        reconstructed_data_hit_matrix = data_packet['file_hit_matrix']
        reconstructed_data_hit_matrix_for_event = data_packet['file_hit_matrix_for_event']
        event_number = data_packet['event_number']
        reconstructed_data_track_data = data_packet['file_track_data']

        # (1): Reconstructed Logs:
        # Needs nothng

        # (2): Vertex Display:
        self.vertex_tab.update_vertex_data(reconstructed_data_output_data)

        # (3): Mass Histogram:
        self.mass_histogram.update_histogram_data(reconstructed_data_output_data)

        # (4): Hit Display:
        self.hit_matrix.update_hit_data(
            reconstructed_data_hit_matrix,
            reconstructed_data_hit_matrix_for_event,
            event_number)

        # (6): 

        # (7): Command History:
        command_history_data_packet = {
            'file_name': reconstructed_data_filename,
            'file_path': reconstructed_data_filepath
        }
        self.command_history.update_output(command_history_data_packet)

    def state_update_detected(self, data):
        print(f"> Now shifting to new .npz file.")
        self.propagate_data_to_tabs(data)


def main():

    # (1): Initialize the application as a QApplication:
    application = QApplication([])

    # (2): Initialize the main window:
    main_application_window = MainWindow()

    # (3): Show the main window:
    main_application_window.show()

    # (4): Close the application when finished:
    sys.exit(application.exec_())



if __name__ == "__main__":
    main()