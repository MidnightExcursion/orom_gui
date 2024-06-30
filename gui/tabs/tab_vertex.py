import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from gui.graphs.vertex_distributions import VertexDistributions

class VertexTab(QWidget):
    def __init__(self):
        super().__init__()

        self.name = "Vertex Display"

        self.initialize_ui()

    def initialize_ui(self):

        layout = QVBoxLayout()
        self.vertex_distribution = VertexDistributions()
        layout.addWidget(self.vertex_distribution)
        self.setLayout(layout)

    def update_vertex_data(self, npy_file):
        self.vertex_distribution.update_vertex_data(npy_file)