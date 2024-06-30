from PyQt5.QtWidgets import QWidget, QGridLayout

import numpy as np

import pyqtgraph as pg

class MomentumDistributions(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()
    
    def initialize_ui(self):

        self.overall_grid_layout = QGridLayout()

        self.momentum_px_plot = pg.PlotWidget()
        self.momentum_py_plot = pg.PlotWidget()
        self.momentum_pz_plot = pg.PlotWidget()

        self.per_event_momentum_px_plot = pg.PlotWidget()
        self.per_event_momentum_py_plot = pg.PlotWidget()
        self.per_event_momentum_pz_plot = pg.PlotWidget()

        self.momentum_px_plot.setBackground('white')
        self.momentum_py_plot.setBackground('white')
        self.momentum_pz_plot.setBackground('white')

        self.per_event_momentum_px_plot.setBackground('white')
        self.per_event_momentum_py_plot.setBackground('white')
        self.per_event_momentum_pz_plot.setBackground('white')
        
        momentum_px_plot_item = self.momentum_px_plot.getPlotItem()
        momentum_py_plot_item = self.momentum_py_plot.getPlotItem()
        momentum_pz_plot_item = self.momentum_pz_plot.getPlotItem()

        per_event_momentum_px_plot = self.per_event_momentum_px_plot.getPlotItem()
        per_event_momentum_py_plot = self.per_event_momentum_py_plot.getPlotItem()
        per_event_momentum_pz_plot = self.per_event_momentum_pz_plot.getPlotItem()

        momentum_px_plot_item.showGrid(x = True,y = True)
        momentum_px_plot_item.setTitle(f'SpinQuest | px Distribution | Total Events:')
        momentum_px_plot_item.setLabel('bottom',"p_{x}", units = 'GeV')
        momentum_px_plot_item.setLabel('left',"Counts", units = 'N')

        momentum_py_plot_item.showGrid(x = True,y = True)
        momentum_py_plot_item.setTitle(f'SpinQuest | py Distribution | Total Events:')
        momentum_py_plot_item.setLabel('bottom',"p_{y}", units = 'GeV')
        momentum_py_plot_item.setLabel('left',"Counts", units = 'N')

        momentum_pz_plot_item.showGrid(x = True,y = True)
        momentum_pz_plot_item.setTitle(f'SpinQuest | pz Distribution | Total Events:')
        momentum_pz_plot_item.setLabel('bottom',"p_{z}", units = 'GeV')
        momentum_pz_plot_item.setLabel('left',"Counts", units = 'N')

        per_event_momentum_px_plot.showGrid(x = True,y = True)
        per_event_momentum_px_plot.setTitle(f'SpinQuest | px Distribution | Event Number:')
        per_event_momentum_px_plot.setLabel('bottom',"p_{x}", units = 'GeV')
        per_event_momentum_px_plot.setLabel('left',"Counts", units = 'N')
        
        per_event_momentum_py_plot.showGrid(x = True,y = True)
        per_event_momentum_py_plot.setTitle(f'SpinQuest | py Distribution | Event Number:')
        per_event_momentum_py_plot.setLabel('bottom',"p_{y}", units = 'GeV')
        per_event_momentum_py_plot.setLabel('left',"Counts", units = 'N')

        per_event_momentum_pz_plot.showGrid(x = True,y = True)
        per_event_momentum_pz_plot.setTitle(f'SpinQuest | pz Distribution | Event Number:')
        per_event_momentum_pz_plot.setLabel('bottom',"p_{z}", units = 'GeV')
        per_event_momentum_pz_plot.setLabel('left',"Counts", units = 'N')

        self.overall_grid_layout.addWidget(self.momentum_px_plot, 0, 0)
        self.overall_grid_layout.addWidget(self.momentum_py_plot, 1, 0)
        self.overall_grid_layout.addWidget(self.momentum_pz_plot, 2, 0)

        self.overall_grid_layout.addWidget(self.per_event_momentum_px_plot, 0, 1)
        self.overall_grid_layout.addWidget(self.per_event_momentum_py_plot, 1, 1)
        self.overall_grid_layout.addWidget(self.per_event_momentum_pz_plot, 2, 1)

        self.setLayout(self.overall_grid_layout)

    def update_momentum_distribution(self, slice_of_events_and_kinematics, event_number):
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
            is required for the momentum distribution.
        """

        number_of_events_in_spill = len(slice_of_events_and_kinematics)

        # (1.1): Obtain the column corresponding to the positive muons's p_{x}:
        positive_muon_momentum_x = slice_of_events_and_kinematics[:, 17] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[17]
        per_event_positive_muon_momentum_x = slice_of_events_and_kinematics[event_number + 1, 17]

        # (1.2): Obtain the column corresponding to the positive muons's p_{y}:
        positive_muon_momentum_y = slice_of_events_and_kinematics[:, 18] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[18]
        per_event_positive_muon_momentum_y = slice_of_events_and_kinematics[event_number + 1, 18]

        # (1.3): Obtain the column corresponding to the positive muons's p_{z}:
        positive_muon_momentum_z = slice_of_events_and_kinematics[:, 19] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[19]
        per_event_positive_muon_momentum_z = slice_of_events_and_kinematics[event_number + 1, 19]

        # (1.4): Obtain the column corresponding to the negative muons's p_{x}:
        negative_muon_momentum_x = slice_of_events_and_kinematics[:, 20] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[20]
        per_event_negative_muon_momentum_x = slice_of_events_and_kinematics[event_number + 1, 20]

        # (1.5): Obtain the column corresponding to the negative muons's p_{y}:
        negative_muon_momentum_y = slice_of_events_and_kinematics[:, 21] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[21]
        per_event_negative_muon_momentum_y = slice_of_events_and_kinematics[event_number + 1, 21]
        
        # (1.6): Obtain the column corresponding to the negative muons's p_{z}:
        negative_muon_momentum_z = slice_of_events_and_kinematics[:, 22] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[22]
        per_event_negative_muon_momentum_z = slice_of_events_and_kinematics[event_number + 1, 22]

        positive_muon_x_vertex_histogram_data, positive_muon_x_momentum_bins = np.histogram(positive_muon_momentum_x, bins = 100)
        positive_muon_y_vertex_histogram_data, positive_muon_y_momentum_bins = np.histogram(positive_muon_momentum_y, bins = 100)
        positive_muon_z_vertex_histogram_data, positive_muon_z_momentum_bins = np.histogram(positive_muon_momentum_z, bins = 100)
        negative_muon_x_vertex_histogram_data, negative_muon_x_momentum_bins = np.histogram(negative_muon_momentum_x, bins = 100)
        negative_muon_y_vertex_histogram_data, negative_muon_y_momentum_bins = np.histogram(negative_muon_momentum_y, bins = 100)
        negative_muon_z_vertex_histogram_data, negative_muon_z_momentum_bins = np.histogram(negative_muon_momentum_z, bins = 100)
        
        per_event_positive_muon_x_momentum_histogram_data, per_event_positive_muon_x_momentum_bins = np.histogram(per_event_positive_muon_momentum_x, bins = 100)
        per_event_positive_muon_y_momentum_histogram_data, per_event_positive_muon_y_momentum_bins = np.histogram(per_event_positive_muon_momentum_y, bins = 100)
        per_event_positive_muon_z_momentum_histogram_data, per_event_positive_muon_z_momentum_bins = np.histogram(per_event_positive_muon_momentum_z, bins = 100)
        per_event_negative_muon_x_momentum_histogram_data, per_event_negative_muon_x_momentum_bins = np.histogram(per_event_negative_muon_momentum_x, bins = 100)
        per_event_negative_muon_y_momentum_histogram_data, per_event_negative_muon_y_momentum_bins = np.histogram(per_event_negative_muon_momentum_y, bins = 100)
        per_event_negative_muon_z_momentum_histogram_data, per_event_negative_muon_z_momentum_bins = np.histogram(per_event_negative_muon_momentum_z, bins = 100)

        self.momentum_px_positive_muon_histogram = pg.BarGraphItem(
            x = positive_muon_x_momentum_bins[:-1],
            height = positive_muon_x_vertex_histogram_data,
            width = (positive_muon_x_momentum_bins[1] - positive_muon_x_momentum_bins[0]),
            pen = pg.mkPen(color= (255, 0, 0, 150), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )
        
        self.momentum_py_positive_muon_histogram = pg.BarGraphItem(
            x = positive_muon_y_momentum_bins[:-1],
            height = positive_muon_y_vertex_histogram_data,
            width = (positive_muon_y_momentum_bins[1] - positive_muon_y_momentum_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 150), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )
        
        self.momentum_pz_positive_muon_histogram = pg.BarGraphItem(
            x = positive_muon_z_momentum_bins[:-1],
            height = positive_muon_z_vertex_histogram_data,
            width = (positive_muon_z_momentum_bins[1] - positive_muon_z_momentum_bins[0]),
            pen = pg.mkPen(color=(255, 0, 0, 150), width=2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )

        self.momentum_px_negative_muon_histogram = pg.BarGraphItem(
            x = negative_muon_x_momentum_bins[:-1],
            height = negative_muon_x_vertex_histogram_data,
            width = (negative_muon_x_momentum_bins[1] - negative_muon_x_momentum_bins[0]),
            pen = pg.mkPen(color= (0, 0, 255, 150), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )
        
        self.momentum_py_negative_muon_histogram = pg.BarGraphItem(
            x = negative_muon_y_momentum_bins[:-1],
            height = negative_muon_y_vertex_histogram_data,
            width = (negative_muon_y_momentum_bins[1] - negative_muon_y_momentum_bins[0]),
            pen = pg.mkPen(color = (0, 0, 255, 150), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )
        
        self.momentum_pz_negative_muon_histogram = pg.BarGraphItem(
            x = negative_muon_z_momentum_bins[:-1],
            height = negative_muon_z_vertex_histogram_data,
            width = (negative_muon_z_momentum_bins[1] - negative_muon_z_momentum_bins[0]),
            pen = pg.mkPen(color = (0, 0, 255, 150), width=2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )

        self.per_event_momentum_px_positive_muon_histogram = pg.BarGraphItem(
            x = per_event_positive_muon_x_momentum_bins[:-1],
            height = per_event_positive_muon_x_momentum_histogram_data,
            width = (per_event_positive_muon_x_momentum_bins[1] - per_event_positive_muon_x_momentum_bins[0]),
            pen = pg.mkPen(color = (255, 0, 0, 150), width = 2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )

        self.per_event_momentum_py_positive_muon_histogram = pg.BarGraphItem(
            x = per_event_positive_muon_y_momentum_bins[:-1],
            height = per_event_positive_muon_y_momentum_histogram_data,
            width = (per_event_positive_muon_y_momentum_bins[1] - per_event_positive_muon_y_momentum_bins[0]),
            pen = pg.mkPen(color = (255, 0, 0, 150), width = 2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )

        self.per_event_momentum_pz_positive_muon_histogram = pg.BarGraphItem(
            x = per_event_positive_muon_z_momentum_bins[:-1],
            height = per_event_positive_muon_z_momentum_histogram_data,
            width = (per_event_positive_muon_z_momentum_bins[1] - per_event_positive_muon_z_momentum_bins[0]),
            pen = pg.mkPen(color = (255, 0, 0, 150), width = 2),
            brush = pg.mkBrush(255, 0, 0, 20)
        )

        self.per_event_momentum_px_negative_muon_histogram = pg.BarGraphItem(
            x = per_event_negative_muon_x_momentum_bins[:-1],
            height = per_event_negative_muon_x_momentum_histogram_data,
            width = (per_event_negative_muon_x_momentum_bins[1] - per_event_negative_muon_x_momentum_bins[0]),
            pen = pg.mkPen(color = (0, 0, 255, 150), width = 2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )

        self.per_event_momentum_py_negative_muon_histogram = pg.BarGraphItem(
            x = per_event_negative_muon_y_momentum_bins[:-1],
            height = per_event_negative_muon_y_momentum_histogram_data,
            width = (per_event_negative_muon_y_momentum_bins[1] - per_event_negative_muon_y_momentum_bins[0]),
            pen = pg.mkPen(color = (0, 0, 255, 150), width = 2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )

        self.per_event_momentum_pz_negative_muon_histogram = pg.BarGraphItem(
            x = per_event_negative_muon_z_momentum_bins[:-1],
            height = per_event_negative_muon_z_momentum_histogram_data,
            width = (per_event_negative_muon_z_momentum_bins[1] - per_event_negative_muon_z_momentum_bins[0]),
            pen = pg.mkPen(color = (0, 0, 255, 150), width = 2),
            brush = pg.mkBrush(0, 0, 255, 20)
        )
        
        momentum_px_plot_item = self.momentum_px_plot.getPlotItem()
        momentum_px_plot_item.clear()
        momentum_py_plot_item = self.momentum_py_plot.getPlotItem()
        momentum_py_plot_item.clear()
        momentum_pz_plot_item = self.momentum_pz_plot.getPlotItem()
        momentum_pz_plot_item.clear()

        per_event_momentum_px_plot_item = self.per_event_momentum_px_plot.getPlotItem()
        per_event_momentum_px_plot_item.clear()
        per_event_momentum_py_plot_item = self.per_event_momentum_py_plot.getPlotItem()
        per_event_momentum_py_plot_item.clear()
        per_event_momentum_pz_plot_item = self.per_event_momentum_pz_plot.getPlotItem()
        per_event_momentum_pz_plot_item.clear()

        momentum_px_plot_item.addItem(self.momentum_px_positive_muon_histogram)
        momentum_px_plot_item.addItem(self.momentum_px_negative_muon_histogram)
        momentum_py_plot_item.addItem(self.momentum_py_positive_muon_histogram)
        momentum_py_plot_item.addItem(self.momentum_py_negative_muon_histogram)
        momentum_pz_plot_item.addItem(self.momentum_pz_positive_muon_histogram)
        momentum_pz_plot_item.addItem(self.momentum_pz_negative_muon_histogram)

        momentum_px_plot_item.setTitle(f'SpinQuest | px Distribution | Total Events: {number_of_events_in_spill}')
        momentum_px_plot_item.setTitle(f'SpinQuest | py Distribution | Total Events: {number_of_events_in_spill}')
        momentum_px_plot_item.setTitle(f'SpinQuest | pz Distribution | Total Events: {number_of_events_in_spill}')
        per_event_momentum_px_plot_item.setTitle(f'SpinQuest | px Distribution | Event Number: {event_number}')
        per_event_momentum_py_plot_item.setTitle(f'SpinQuest | py Distribution | Event Number: {event_number}')
        per_event_momentum_pz_plot_item.setTitle(f'SpinQuest | pz Distribution | Event Number: {event_number}')

        per_event_momentum_px_plot_item.addItem(self.per_event_momentum_px_positive_muon_histogram)
        per_event_momentum_py_plot_item.addItem(self.per_event_momentum_py_positive_muon_histogram)
        per_event_momentum_pz_plot_item.addItem(self.per_event_momentum_pz_positive_muon_histogram)
        per_event_momentum_px_plot_item.addItem(self.per_event_momentum_px_negative_muon_histogram)
        per_event_momentum_py_plot_item.addItem(self.per_event_momentum_py_negative_muon_histogram)
        per_event_momentum_pz_plot_item.addItem(self.per_event_momentum_pz_negative_muon_histogram)