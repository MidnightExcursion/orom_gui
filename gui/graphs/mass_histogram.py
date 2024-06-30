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
        self.single_event_mass_histogram_plot = pg.PlotWidget()

        self.mass_histogram_plot.setBackground('white')
        self.single_event_mass_histogram_plot.setBackground('white')

        all_event_mass_histogram_plot_item = self.mass_histogram_plot.getPlotItem()
        single_event_mass_histogram_plot_item = self.single_event_mass_histogram_plot.getPlotItem()

        # mass_plot_font = pg.Qt.QtGui.QFont('Times New Roman')
        # mass_plot_font.setPixelSize(22)

        all_event_mass_histogram_plot_item.showGrid(x = True, y = True)
        all_event_mass_histogram_plot_item.setLabel('bottom',"Mass [GeV]")
        all_event_mass_histogram_plot_item.setLabel('left',"Counts [N]")

        single_event_mass_histogram_plot_item.showGrid(x = True, y = True)
        single_event_mass_histogram_plot_item.setLabel('bottom',"Mass [GeV]")
        single_event_mass_histogram_plot_item.setLabel('left',"Counts [N]")

        # tick_font = {'color': 'k', 'font-size': '16pt', 'font-family': 'Arial'}

        # tick_marks_bottom = all_event_mass_histogram_plot_item.getAxis('bottom')
        # tick_marks_left = all_event_mass_histogram_plot_item.getAxis('left')

        # tick_marks_bottom.tickFont = mass_plot_font
        # tick_marks_bottom.setTickFont(pg.Qt.QtGui.QFont('Arial', 16))
        # tick_marks_bottom.setPen(pg.mkPen('white'))

        # tick_marks_bottom.tickFont = mass_plot_font
        # tick_marks_left.setTickFont(pg.Qt.QtGui.QFont('Arial', 16))
        # tick_marks_left.setPen(pg.mkPen('white'))

        layout.addWidget(self.mass_histogram_plot)
        layout.addWidget(self.single_event_mass_histogram_plot)

        self.setLayout(layout)

    def update_histogram_data(self, npz_file, event_number):
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
        all_events_dimuon_probability = npz_file[:, 3]
        single_event_dimuon_probability = npz_file[event_number, 3]
        number_of_events_in_spill = len(all_events_dimuon_probability)

        # (2): We then filter all the events based on this condition:
        all_events_data_with_possible_dimuons = npz_file[(all_events_dimuon_probability > _PROBABILITY_DIMUON_EVENT)]
        is_single_event_a_dimuon_boolean = (single_event_dimuon_probability > _PROBABILITY_DIMUON_EVENT)
        print(is_single_event_a_dimuon_boolean)

        single_event_dimuon_warning_label = f'P(Dimuon Event) > {_PROBABILITY_DIMUON_EVENT}' if is_single_event_a_dimuon_boolean else 'WARNING: Not a dimuon event!'

        # (3): Kinematic data occurs in columns 25-30 --- see documentation:
        all_events_mass_array = calculate_invariant_mass(all_events_data_with_possible_dimuons[:, 26:32])
        single_event_mass_data = calculate_invariant_mass(npz_file[event_number, 26:32])

        # (4): Compute the histogram for the mass array:
        all_dimuon_events_mass_histogram, bins = np.histogram(all_events_mass_array, bins = np.linspace(0., 10.0, 301))
        single_event_mass_histogram, bins = np.histogram(single_event_mass_data, bins = np.linspace(0., 10.0, 301))

        # (5): Initialize a `pyqtgraph` bar graph to display all the dimuon events
        self.all_dimuon_events_mass_histogram = pg.BarGraphItem(
            x = bins[:-1],
            height = all_dimuon_events_mass_histogram,
            width = (bins[1] - bins[0]),
            pen = pg.mkPen('black'),
            brush = pg.mkBrush('white'))
        
        self.single_event_mass_histogram = pg.BarGraphItem(
            x = bins[:-1],
            height = single_event_mass_histogram,
            width = (bins[1] - bins[0]),
            pen = pg.mkPen('blue') if is_single_event_a_dimuon_boolean else pg.mkPen('orange'),
            brush = pg.mkBrush('white'))
        
        all_event_mass_histogram_plot_item = self.mass_histogram_plot.getPlotItem()
        all_event_mass_histogram_plot_item.clear()
        single_event_mass_histogram_plot_item = self.single_event_mass_histogram_plot.getPlotItem()
        single_event_mass_histogram_plot_item.clear()

        all_event_mass_histogram_plot_item.addItem(self.all_dimuon_events_mass_histogram)
        single_event_mass_histogram_plot_item.addItem(self.single_event_mass_histogram)

        all_event_mass_histogram_plot_item.setTitle(f'SpinQuest | Mass Spectrum | Total Events: {number_of_events_in_spill}')
        single_event_mass_histogram_plot_item.setTitle(f'SpinQuest | Mass Spectrum | Event Number: {event_number} | {single_event_dimuon_warning_label}')

        vertical_line_j_psi_mass = pg.InfiniteLine(
            angle = 90,
            movable = False,
            pen = pg.mkPen('red'))
        vertical_line_j_psi_mass.setPos(_MASS_OF_J_PSI_IN_GEV)

        vertical_line_j_2s_mass = pg.InfiniteLine(
            angle = 90,
            movable = False,
            pen = pg.mkPen('red'))
        vertical_line_j_2s_mass.setPos(_MASS_OF_PSI_2S_IN_GEV)
        
        
        all_event_mass_histogram_plot_item.addItem(vertical_line_j_2s_mass)
        all_event_mass_histogram_plot_item.addItem(vertical_line_j_psi_mass)
        single_event_mass_histogram_plot_item.addItem(vertical_line_j_2s_mass)
        single_event_mass_histogram_plot_item.addItem(vertical_line_j_psi_mass)

        # target_prob = data_with_possible_dimuons[:, 33]
        # metadata_filtered = data_with_possible_dimuons[:, 34:]

        # trans = calcVariables(target_pred)[1]
        # beamline = (trans < 1)
        # x1, x2 = calcVariables(target_pred)[2:4]
        # x_cuts = (x1 - x2 > -0.1) & (x1 - x2 < 0.9) & (x2 > 0.05)
        # filt = x_cuts & beamline 