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

    def update_hit_data(self, hit_data, single_event_data, event_number):
        """
        Update the tab with the hit data and track data.

        :param hit_data: A rank-3 numpy array where the first index is 
                         the event number, and each event is a rank-2 matrix of 0s and 1s.
        :param track_data: Additional track data (not used in this example).
        """
        self.hit_display_plot.update_hit_data(hit_data, single_event_data, event_number)