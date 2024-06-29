import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from gui.modules.physics.calculate_physics import calculate_invariant_mass

from gui.statics.statics import _MASS_OF_J_PSI_IN_GEV, _MASS_OF_PSI_2S_IN_GEV
from gui.statics.statics import _PATH_FOR_RECONSTRUCTED_DATA
from gui.statics.statics import _PROBABILITY_DIMUON_EVENT


class MassHistogram(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()

        self.mass_histogram_plot = pg.PlotWidget()
        self.mass_histogram_plot.setBackground('white')
        plot_item = self.mass_histogram_plot.getPlotItem()
        
        # mass_plot_font = pg.Qt.QtGui.QFont('Times New Roman')
        # mass_plot_font.setPixelSize(22)

        plot_item.showGrid(x = True, y = True)
        plot_item.setTitle('SpinQuest | Invariant Mass Reconstruction')
        plot_item.setLabel('bottom',"Mass [GeV]")
        plot_item.setLabel('left',"Counts [N]")

        # tick_font = {'color': 'k', 'font-size': '16pt', 'font-family': 'Arial'}

        # tick_marks_bottom = plot_item.getAxis('bottom')
        # tick_marks_left = plot_item.getAxis('left')

        # tick_marks_bottom.tickFont = mass_plot_font
        # tick_marks_bottom.setTickFont(pg.Qt.QtGui.QFont('Arial', 16))
        # tick_marks_bottom.setPen(pg.mkPen('white'))

        # tick_marks_bottom.tickFont = mass_plot_font
        # tick_marks_left.setTickFont(pg.Qt.QtGui.QFont('Arial', 16))
        # tick_marks_left.setPen(pg.mkPen('white'))

        layout.addWidget(self.mass_histogram_plot)
        self.setLayout(layout)

    def update_histogram_data(self, npz_file):
        """
        # Description:
        Upon initialization, we queue into the directory with
        all the reconstructed data is located and simply
        display it. We outsource this particular functionality
        to another function located in `modules/physics/`

        # Arguments:
        (npz_file):
            We require only the 4th and 28h-33rd column
            of the `.npz` file to make the mass plot.
        """
    
        # (1): The dimuon probability is the 4th column in the `.npy` file!
        dimuon_probability = npz_file[:, 3]

        # (2): We then filter all the events based on this condition:
        data_with_possible_dimuons = npz_file[(dimuon_probability > _PROBABILITY_DIMUON_EVENT)]

        # hits_missing = data_with_possible_dimuons[:, 6:9]
        # all_vtx_pred = data_with_possible_dimuons[:, 9:18]
        # z_vtx_pred = data_with_possible_dimuons[:, 18:27]

        # (3): Kinematic data occurs in columns 28-33. They are:
        # target_pred = data_with_possible_dimuons[:, 27:33]
        events_positive_muon_momentum_x = data_with_possible_dimuons[:, 26]
        events_positive_muon_momentum_y = data_with_possible_dimuons[:, 27]
        events_positive_muon_momentum_z = data_with_possible_dimuons[:, 28]
        events_negative_muon_momentum_x = data_with_possible_dimuons[:, 29]
        events_negative_muon_momentum_y = data_with_possible_dimuons[:, 30]
        events_negative_muon_momentum_z = data_with_possible_dimuons[:, 31]

        # This will be a rank-2 matrix with: [events, momentum] -> [events, mass]
        mass_array = calculate_invariant_mass(data_with_possible_dimuons[:, 26:32])

        # Create a histogram item
        mass_histogram, bins = np.histogram(mass_array, bins = np.linspace(0., 10.0, 301))

        self.mass_histogram = pg.BarGraphItem(
            x = bins[:-1],
            height = mass_histogram,
            width = (bins[1] - bins[0]),
            pen = pg.mkPen('black'),
            brush = pg.mkBrush('white'))
        
        histogram_plot = self.mass_histogram_plot.getPlotItem()
        histogram_plot.clear()
        histogram_plot.addItem(self.mass_histogram)

        vertical_line_j_psi_mass = pg.InfiniteLine(
            angle = 90,
            movable = False,
            pen = pg.mkPen('red'))
        vertical_line_j_psi_mass.setPos(_MASS_OF_J_PSI_IN_GEV)
        histogram_plot.addItem(vertical_line_j_psi_mass)

        vertical_line_j_2s_mass = pg.InfiniteLine(
            angle = 90,
            movable = False,
            pen = pg.mkPen('red'))
        vertical_line_j_2s_mass.setPos(_MASS_OF_PSI_2S_IN_GEV)
        histogram_plot.addItem(vertical_line_j_2s_mass)

        # target_prob = data_with_possible_dimuons[:, 33]
        # metadata_filtered = data_with_possible_dimuons[:, 34:]

        # mass = calcVariables(target_pred)[0]
        # trans = calcVariables(target_pred)[1]
        # beamline = (trans < 1)
        # x1, x2 = calcVariables(target_pred)[2:4]
        # x_cuts = (x1 - x2 > -0.1) & (x1 - x2 < 0.9) & (x2 > 0.05)
        # filt = x_cuts & beamline 