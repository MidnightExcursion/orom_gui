from PyQt5.QtWidgets import  QWidget, QGridLayout, QPushButton, QMessageBox

from gui.widgets.light_indicator import LightIndicator

from gui.graphs.mass_histogram import MassHistogram
from gui.graphs.momentum_distributions import MomentumDistributions
from gui.graphs.hit_matrix import HitDisplayPlot
from gui.graphs.vertex_distributions import VertexDistributions


class MainMenuTab(QWidget):
    def __init__(self, tab_widget):

    
        super().__init__()

        self.name = "Dashboard"

        self.tab_widget = tab_widget

        self.initialize_ui()

    def initialize_ui(self):
        """
        # Description:
        Simply initialize the user-interface of the widget.
        """

        # (1): Initialize the layout as a QGrid:
        main_menu_tab_layout = QGridLayout()

        # (2): Begin to initialize the various `pyqtgraphs` that we will use:

        # (2.1): `pyqtgraphs` | Mass Histogram:
        self.plot_mass_histogram = MassHistogram()

        # (2.2): `pyqtgraphs` | Momentum Distributions: 
        self.plot_momentum_distribution = MomentumDistributions()

        # (2.3): `pyqtgraphs` | Hit Display:
        self.plot_hit_display = HitDisplayPlot()

        # (2.4): `pyqtgraphs` | Vertex Distributions:
        self.plot_vertex_plot = VertexDistributions()
        
        # (3): Begin to add widgets (graphs) to the layout:

        # (3.1): Layout | Add Mass Histogram plot:
        main_menu_tab_layout.addWidget(self.plot_mass_histogram, 0, 0)

        # (3.2): Layout | Add Momentum Distribution plot:
        main_menu_tab_layout.addWidget(self.plot_momentum_distribution, 1, 0)

        # (3.3): Layout | Add Hit Display plot:
        main_menu_tab_layout.addWidget(self.plot_hit_display, 2, 0)

        # (3.4): Layout | Add Vertex Distribution plot:
        main_menu_tab_layout.addWidget(self.plot_vertex_plot, 3, 0)

        # (4): Set the layout of the Main Menu:
        self.setLayout(main_menu_tab_layout)

    def propagate_data_to_all_graphs(self, data_packet):
        print(data_packet)
        reconstructed_data_filename = data_packet['filename']
        reconstructed_data_filepath = data_packet['filepath']
        reconstructed_data_output_data = data_packet['file_output_data']
        reconstructed_data_hit_matrix = data_packet['file_hit_matrix']
        reconstructed_data_hit_matrix_for_event = data_packet['file_hit_matrix_for_event']
        event_number = data_packet['event_number']
        reconstructed_data_track_data = data_packet['file_track_data']
        

        # (2): Passing subsections of `data_packet` to all the component graphs:                                                                                                                                             

        # (2.1): Passing Data | Mass Histogram:
        self.plot_mass_histogram.update_histogram_data(reconstructed_data_output_data, event_number)

        # (2.2): Passing Data | Momentum Distribution:
        self.plot_momentum_distribution.update_momentum_distribution(
            reconstructed_data_output_data,
            event_number)

        # (2.3): Passing Data | Hit Display:
        self.plot_hit_display.update_hit_data(
            reconstructed_data_hit_matrix,
            reconstructed_data_hit_matrix_for_event,
            reconstructed_data_track_data,
            None,
            event_number)
        
        # (2.4): Passing Data | Vertex Display:
        self.plot_vertex_plot.update_vertex_data(reconstructed_data_output_data)
