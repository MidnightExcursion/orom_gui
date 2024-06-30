import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import pyqtgraph as pg

from gui.graphs.momentum_distributions import MomentumDistributions

class MomentumDistributionTab(QWidget):
    def __init__(self):
        super().__init__()

        self.name = "Momentum Distribution"

        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()

        self.momentum_distribution = MomentumDistributions()

        layout.addWidget(self.momentum_distribution)

        self.setLayout(layout)

    def update_momentum_distribution(self, output_data, event_number_index):
        """
        # Description:
        Simply provide a slot for the incoming data that gets
        immediately passed to the `MomentumDistributions` class for processing.

        # Arguments:
        `output_data`: ListType
            some sort of insane array that we'll analyze.

        `event_number_index`: int
            The current event number plus one to turn it into its corresponding index.
        """
        self.momentum_distribution.update_momentum_distribution(output_data, event_number_index)