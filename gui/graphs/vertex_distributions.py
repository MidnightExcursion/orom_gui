from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit

import numpy as np

import pyqtgraph as pg


class VertexDistributions(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()
    
    def initialize_ui(self):
        layout = QVBoxLayout()

        self.vertex_x_plot = pg.PlotWidget()
        self.vertex_y_plot = pg.PlotWidget()
        self.vertex_z_plot = pg.PlotWidget()

        self.vertex_x_plot.setBackground('white')
        self.vertex_y_plot.setBackground('white')
        self.vertex_z_plot.setBackground('white')
        
        vertex_x_plot_item = self.vertex_x_plot.getPlotItem()
        vertex_y_plot_item = self.vertex_y_plot.getPlotItem()
        vertex_z_plot_item = self.vertex_z_plot.getPlotItem()

        vertex_x_plot_item.showGrid(x = True,y = True)
        vertex_x_plot_item.setTitle('SpinQuest | Vertex Distribution Along X')
        vertex_x_plot_item.setLabel('bottom',"Event ID")
        vertex_x_plot_item.setLabel('left',"X Vertex (cm)")

        vertex_y_plot_item.showGrid(x = True,y = True)
        vertex_y_plot_item.setTitle('SpinQuest | Vertex Distribution Along Y')
        vertex_y_plot_item.setLabel('bottom',"Event ID")
        vertex_y_plot_item.setLabel('left',"Y Vertex (cm)")

        vertex_z_plot_item.showGrid(x = True,y = True)
        vertex_z_plot_item.setTitle('SpinQuest | Vertex Distribution Along Z')
        vertex_z_plot_item.setLabel('bottom',"Event ID")
        vertex_z_plot_item.setLabel('left',"Z Vertex (cm)")

        layout.addWidget(self.vertex_x_plot)
        layout.addWidget(self.vertex_y_plot)
        layout.addWidget(self.vertex_z_plot)

        self.setLayout(layout)

    def update_vertex_data(self, npz_data):
        """
        # Description:
        Upon initialization, we queue into the directory with
        all the reconstructed data is located and simply
        display it. We outsource this particular functionality
        to another function located in `modules/physics/`

        # Arguments:
        (npz_data): `.npz` file
            We require that an `.npz` file is supplied with
            the relevant data. It turns out that the 22-27th
            columns of the entire rank-2 matrix file are what
            is required for the vertex distribution.
        """

        plus_muon_x_vertex_distribution = npz_data[21]
        minus_muon_x_vertex_distribution = npz_data[24]
        plus_muon_y_vertex_distribution = npz_data[22]
        minus_muon_y_vertex_distribution = npz_data[25]
        plus_muon_z_vertex_distribution = npz_data[23]
        minus_muon_z_vertex_distribution = npz_data[26]

        plus_muon_x_vertex_data = plus_muon_x_vertex_distribution[(plus_muon_x_vertex_distribution >= -1000) & (plus_muon_x_vertex_distribution <= 1000)]
        minus_muon_x_vertex_data = minus_muon_x_vertex_distribution[(minus_muon_x_vertex_distribution >= -1000) & (minus_muon_x_vertex_distribution <= 1000)]
        plus_muon_y_vertex_data = plus_muon_y_vertex_distribution[(plus_muon_y_vertex_distribution >= -1000) & (plus_muon_y_vertex_distribution <= 1000)]
        minus_muon_y_vertex_data = minus_muon_y_vertex_distribution[(minus_muon_y_vertex_distribution >= -1000) & (minus_muon_y_vertex_distribution <= 1000)]
        plus_muon_z_vertex_data = plus_muon_z_vertex_distribution[(plus_muon_z_vertex_distribution >= -1000) & (plus_muon_z_vertex_distribution <= 1000)]
        minus_muon_z_vertex_data = minus_muon_z_vertex_distribution[(minus_muon_z_vertex_distribution >= -1000) & (minus_muon_z_vertex_distribution <= 1000)]

        plus_muon_x_vertex_histogram_data, plus_muon_x_vertex_bins = np.histogram(plus_muon_x_vertex_data, bins = 100)
        minus_muon_x_vertex_histogram_data, minus_muon_x_vertex_bins = np.histogram(minus_muon_x_vertex_data, bins = 100)
        plus_muon_y_vertex_histogram_data, plus_muon_y_vertex_bins = np.histogram(plus_muon_y_vertex_data, bins = 100)
        minus_muon_y_vertex_histogram_data, minus_muon_y_vertex_bins = np.histogram(minus_muon_y_vertex_data, bins = 100)
        plus_muon_z_vertex_histogram_data, plus_muon_z_vertex_bins = np.histogram(plus_muon_z_vertex_data, bins = 100)
        minus_muon_z_vertex_histogram_data, minus_muon_z_vertex_bins = np.histogram(minus_muon_z_vertex_data, bins = 100)
        
        self.vertex_x_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_x_vertex_bins[:-1],
            height = plus_muon_x_vertex_histogram_data,
            width = (plus_muon_x_vertex_bins[1] - plus_muon_x_vertex_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2),
            brush = pg.mkBrush(255, 0, 0, 20) # Transparent brush
        )
        
        self.vertex_x_minus_muon_histogram = pg.BarGraphItem(
            x = minus_muon_x_vertex_bins[:-1],
            height = minus_muon_x_vertex_histogram_data,
            width = (minus_muon_x_vertex_bins[1] - minus_muon_x_vertex_bins[0]),
            pen = pg.mkPen(color=(0, 0, 255, 255), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)  # Transparent brush
        )
        
        self.vertex_y_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_y_vertex_bins[:-1],
            height = plus_muon_y_vertex_histogram_data,
            width = (plus_muon_y_vertex_bins[1] - plus_muon_y_vertex_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)  # Transparent brush
        )

        self.vertex_y_minus_muon_histogram = pg.BarGraphItem(
            x = minus_muon_y_vertex_bins[:-1],
            height = minus_muon_y_vertex_histogram_data,
            width = (minus_muon_y_vertex_bins[1] - minus_muon_y_vertex_bins[0]),
            pen = pg.mkPen(color=(0, 0, 255, 255), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)   # Transparent brush
        )
        
        self.vertex_z_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_z_vertex_bins[:-1],
            height = plus_muon_z_vertex_histogram_data,
            width = (plus_muon_z_vertex_bins[1] - plus_muon_z_vertex_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)  # Transparent brush
        )
        
        self.vertex_z_minus_muon_histogram = pg.BarGraphItem(
            x = minus_muon_z_vertex_bins[:-1],
            height = minus_muon_z_vertex_histogram_data,
            width = (minus_muon_z_vertex_bins[1] - minus_muon_z_vertex_bins[0]),
            pen = pg.mkPen(color=(0, 0, 255, 255), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)   # Transparent brush
        )
        
        vertex_x_plot_item = self.vertex_x_plot.getPlotItem()
        vertex_x_plot_item.clear()
        vertex_y_plot_item = self.vertex_y_plot.getPlotItem()
        vertex_y_plot_item.clear()
        vertex_z_plot_item = self.vertex_z_plot.getPlotItem()
        vertex_z_plot_item.clear()

        vertex_x_plot_item.addItem(self.vertex_x_plus_muon_histogram)
        vertex_x_plot_item.addItem(self.vertex_x_minus_muon_histogram)
        vertex_y_plot_item.addItem(self.vertex_y_plus_muon_histogram)
        vertex_y_plot_item.addItem(self.vertex_y_minus_muon_histogram)
        vertex_z_plot_item.addItem(self.vertex_z_plus_muon_histogram)
        vertex_z_plot_item.addItem(self.vertex_z_minus_muon_histogram)