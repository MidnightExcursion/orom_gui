import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import pyqtgraph as pg

from gui.graphs.mass_histogram import MassHistogram

class MassHistogramTab(QWidget):
    def __init__(self):
        super().__init__()

        self.name = "Mass Histogram"

        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()
        self.mass_histogram = MassHistogram()
        layout.addWidget(self.mass_histogram)
        self.setLayout(layout)

    def update_histogram_data(self, output_data):
        """
        # Description:
        Simply provide a slot for the incoming data that gets
        immediately passed to the `MassHistogram` class for processing.
        """
        self.mass_histogram.update_histogram_data(output_data)