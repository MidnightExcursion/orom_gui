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
from gui.tabs.tab_momentum_distributions import MomentumDistributionTab
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

        # (2): Initialize the central tab that contains all the GUI tabs:
        self.central_tab = QTabWidget()

        # (3.1): Initialize Tabs | Main Menu / Dashboard
        self.main_menu_tab = MainMenuTab(self.central_tab)

        # (3.2): Initialize Tabs | MassHistogramTab:
        self.mass_histogram = MassHistogramTab()

        # (3.3): Initialize Tabs | MomentumDistributionTab:
        self.momentum_distribution = MomentumDistributionTab()

        # (3.4): Initialize Tabs | HitMatrixTab:
        self.hit_matrix = HitMatrixTab()

        # (3.5): Initialize Tabs | VertexTab:
        self.vertex_tab = VertexTab()

        # (3.6): Initialize Tabs | LoggingTab:
        self.logging_tab = LoggingTab()

        # (3.7): Initialize Tabs | CommandHistoryTab:
        self.command_history = CommandHistoryTab()

        # (4): Initialize the central menu of buttons that control the application:

        # (4.1): Initialize the CentralMenu() widget:
        self.main_menu_widget = CentralMenu()

        # (4.2): Connect the emit `state_updated` to the socket `state_update_detected`:
        self.main_menu_widget.state_updated.connect(self.state_update_detected)

        # (5): Adding tabs to the central layout:

        # (5.1): Adding Tabs | Main Menu:
        self.central_tab.addTab(self.main_menu_tab, self.main_menu_tab.name)

        # (5.2): Adding Tabs | Mass Histogram:
        self.central_tab.addTab(self.mass_histogram, self.mass_histogram.name)

        # (5.3): Adding Tabs | Momentum Distribution:
        self.central_tab.addTab(self.momentum_distribution, self.momentum_distribution.name)

        # (5.4): Adding Tabs | Hit Display:
        self.central_tab.addTab(self.hit_matrix, self.hit_matrix.name)

        # (5.5): Adding Tabs | Vertex Displays:
        self.central_tab.addTab(self.vertex_tab, self.vertex_tab.name)

        # (5.6): Adding Tabs | Logging Tab:
        self.central_tab.addTab(self.logging_tab, self.logging_tab.name)

        # (5.7): Adding Tabs | Command History:
        self.central_tab.addTab(self.command_history, self.command_history.name)

        # (6): Handle the GUI layout: two big boxes stacked vertically in one large box:

        # (6.1): Initialize a vertical box:
        self.main_layout = QVBoxLayout()

        # (6.2): Add to the vertical box the Main Menu:
        self.main_layout.addWidget(self.main_menu_widget)

        # (6.3): Add to the vertical the central tab (that contains all the other tabs):
        self.main_layout.addWidget(self.central_tab)
        
        # (6.4): Conclude GUI layout setup:
        self.central_widget.setLayout(self.main_layout)

        # (7): Define the central widget of the application to be that widget that contains everything we just did:
        self.setCentralWidget(self.central_widget)

    def propagate_data_to_tabs(self, data_packet: dict):
        """
        # Description:
        We pass the data packet from the `.npy` file to all
        of the tabs that require it for plotting.

        # Arguments:
        data_packet: dict
            The packet that contains all the relevant data that will
            end up in all the GUI windows, tab, and plots.
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
        self.mass_histogram.update_histogram_data(reconstructed_data_output_data, event_number)

        # (4): Hit Display:
        self.hit_matrix.update_hit_data(
            reconstructed_data_hit_matrix,
            reconstructed_data_hit_matrix_for_event,
            event_number)

        # (6): 
        self.momentum_distribution.update_momentum_distribution(
            reconstructed_data_output_data,
            event_number)

        # (7): Command History:
        command_history_data_packet = {
            'file_name': reconstructed_data_filename,
            'file_path': reconstructed_data_filepath
        }
        self.command_history.update_output(command_history_data_packet)

    def state_update_detected(self, data: dict):
        """
        # Description:
        We provide an intermediary function that captures the data 
        to be emitted to all the GUI components. The main purpose
        of this function is to just activate `propagate_data_to_tabs`
        provided `data` is not `None`.

        # Arguments:
        data: (dict)
            The dictionary of data that will be sent to all the GUI
            components.
        """
        if not isinstance(data, None):
            self.propagate_data_to_tabs(data)
        else:
            pass


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