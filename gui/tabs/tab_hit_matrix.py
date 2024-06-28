import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit

import numpy as np

import pyqtgraph as pg

from gui.graphs.hit_matrix import HitDisplayPlot

class HitMatrixTab(QWidget):
    def __init__(self):
        super().__init__()

        self.name = "Hit Display"

        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()
        self.hit_display_plot = HitDisplayPlot()
        layout.addWidget(self.hit_display_plot)
        self.setLayout(layout)

    def update_hit_data(self, hit_data, track_data):
        """
        Update the tab with the hit data and track data.

        :param hit_data: A rank-3 numpy array where the first index is 
                         the event number, and each event is a rank-2 matrix of 0s and 1s.
        :param track_data: Additional track data (not used in this example).
        """
        self.hit_display_plot.update_hit_data(hit_data)

    # def initialize_ui(self):
    #     layout = QVBoxLayout()

    #     self.hit_display_plot_widget = pg.PlotWidget()
    #     self.hit_display_plot_widget.setBackground('white')
    #     hit_display_plot_item = self.hit_display_plot_widget.getPlotItem()

    #     hit_display_plot_item.showGrid(x = True,y = True)
    #     hit_display_plot_item.setTitle('SpinQuest | Hit Distribution')
    #     hit_display_plot_item.setLabel('bottom',"Detector ID")
    #     hit_display_plot_item.setLabel('left',"Element ID")

    #     layout.addWidget(self.hit_display_plot_widget)

    #     self.setLayout(layout)

    # def update_hit_data(self, hit_data, track_data):
    #     """
    #     # Description:
    #     Upon initialization, we queue into the directory with
    #     all the reconstructed data is located and simply
    #     display it. We outsource this particular functionality
    #     to another function located in `modules/physics/`

    #     # Arguments:
    #     :param hit_data: A rank-3 numpy array where the first index is 
    #         the event number, and each event is a rank-2 matrix of 0s and 1s.

    #     # Additional Information:
    #     The track data is unusual.
    #     """

    #     print(track_data)

    #     number_of_events_in_spill = len(hit_data)

    #     hit_detectorIDs = []
    #     hit_elementIDs = []

    #     track_detectorIDs = []
    #     track_elementIDs = []

    #     for hit_matrix_for_event in hit_data:

    #         hit_indices = np.argwhere(hit_matrix_for_event == 1)
    #         hit_detectorIDs.extend(hit_indices[:, 0])  # column indices
    #         hit_elementIDs.extend(hit_indices[:, 1])  # row indices

    #     # Create a scatter plot item with aggregated hit coordinates
    #     self.hit_display = pg.ScatterPlotItem(
    #         x = np.array(hit_detectorIDs), y = np.array(hit_elementIDs), symbol = 's', size = 15, brush = (255, 0, 0, 5)
    #     )

    #     # self.track_display = pg.ScatterPlotItem(
    #     #     x = np.array(track_detectorIDs), y = np.array(track_elementIDs), symbol = 's', size = 15, brush = (0, 0, 255, 20)
    #     # )

    #     hit_display_plot_item = self.hit_display_plot_widget.getPlotItem()
    #     hit_display_plot_item.clear()
    #     hit_display_plot_item.addItem(self.hit_display)
    #     # hit_display_plot_item.addItem(self.track_display)
    #     hit_display_plot_item.setTitle(f'SpinQuest | Hit Distribution | Total Events: {number_of_events_in_spill}')
 