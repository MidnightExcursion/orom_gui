from PyQt5.QtWidgets import QWidget, QVBoxLayout

import numpy as np

import pyqtgraph as pg

class MomentumDistributions(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()
    
    def initialize_ui(self):
        layout = QVBoxLayout()

        self.momentum_px_plot = pg.PlotWidget()
        self.momentum_py_plot = pg.PlotWidget()
        self.momentum_pz_plot = pg.PlotWidget()

        self.momentum_px_plot.setBackground('white')
        self.momentum_py_plot.setBackground('white')
        self.momentum_pz_plot.setBackground('white')
        
        momentum_px_plot_item = self.momentum_px_plot.getPlotItem()
        momentum_py_plot_item = self.momentum_py_plot.getPlotItem()
        momentum_pz_plot_item = self.momentum_pz_plot.getPlotItem()

        momentum_px_plot_item.showGrid(x = True,y = True)
        momentum_px_plot_item.setTitle('SpinQuest | $p_{x}$ Distribution')
        momentum_px_plot_item.setLabel('bottom',"p_{x}", units = 'GeV')
        momentum_px_plot_item.setLabel('left',"Counts", units = 'N')

        momentum_py_plot_item.showGrid(x = True,y = True)
        momentum_py_plot_item.setTitle('SpinQuest | $p_{y}$ Distribution')
        momentum_py_plot_item.setLabel('bottom',"p_{x}", units = 'GeV')
        momentum_py_plot_item.setLabel('left',"Counts", units = 'N')

        momentum_pz_plot_item.showGrid(x = True,y = True)
        momentum_pz_plot_item.setTitle('SpinQuest | $p_{z}$ Distribution')
        momentum_pz_plot_item.setLabel('bottom',"p_{x}", units = 'GeV')
        momentum_pz_plot_item.setLabel('left',"Counts", units = 'N')

        layout.addWidget(self.momentum_px_plot)
        layout.addWidget(self.momentum_py_plot)
        layout.addWidget(self.momentum_pz_plot)

        self.setLayout(layout)

    def update_momentum_distribution(self, slice_of_events_and_kinematics, event_number_index):
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

        # (1.1): Obtain the column corresponding to the positive muons's p_{x}:
        positive_muon_momentum_x = slice_of_events_and_kinematics[:, 17] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[17]

        # (1.2): Obtain the column corresponding to the positive muons's p_{y}:
        positive_muon_momentum_y = slice_of_events_and_kinematics[:, 18] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[18]

        # (1.3): Obtain the column corresponding to the positive muons's p_{z}:
        positive_muon_momentum_z = slice_of_events_and_kinematics[:, 19] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[19]

        # (1.4): Obtain the column corresponding to the negative muons's p_{x}:
        negative_muon_momentum_x = slice_of_events_and_kinematics[:, 20] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[20]

        # (1.5): Obtain the column corresponding to the negative muons's p_{y}:
        negative_muon_momentum_y = slice_of_events_and_kinematics[:, 21] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[21]

        # (1.6): Obtain the column corresponding to the negative muons's p_{z}:
        negative_muon_momentum_z = slice_of_events_and_kinematics[:, 22] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[22]

        plus_muon_x_vertex_histogram_data, plus_muon_x_momentum_bins = np.histogram(positive_muon_momentum_x, bins = 100)
        plus_muon_y_vertex_histogram_data, plus_muon_y_momentum_bins = np.histogram(positive_muon_momentum_y, bins = 100)
        plus_muon_z_vertex_histogram_data, plus_muon_z_momentum_bins = np.histogram(positive_muon_momentum_z, bins = 100)
        
        self.momentum_px_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_x_momentum_bins[:-1],
            height = plus_muon_x_vertex_histogram_data,
            width = (plus_muon_x_momentum_bins[1] - plus_muon_x_momentum_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )
        
        self.momentum_py_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_y_momentum_bins[:-1],
            height = plus_muon_y_vertex_histogram_data,
            width = (plus_muon_y_momentum_bins[1] - plus_muon_y_momentum_bins[0]),
            pen = pg.mkPen(color=(0, 0, 255, 255), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )
        
        self.momentum_pz_plus_muon_histogram = pg.BarGraphItem(
            x = plus_muon_z_momentum_bins[:-1],
            height = plus_muon_z_vertex_histogram_data,
            width = (plus_muon_z_momentum_bins[1] - plus_muon_z_momentum_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )
        
        momentum_px_plot_item = self.momentum_px_plot.getPlotItem()
        momentum_px_plot_item.clear()
        momentum_py_plot_item = self.momentum_py_plot.getPlotItem()
        momentum_py_plot_item.clear()
        momentum_pz_plot_item = self.momentum_pz_plot.getPlotItem()
        momentum_pz_plot_item.clear()

        momentum_px_plot_item.addItem(self.momentum_px_plus_muon_histogram)
        momentum_py_plot_item.addItem(self.momentum_py_plus_muon_histogram)
        momentum_pz_plot_item.addItem(self.momentum_pz_plus_muon_histogram)