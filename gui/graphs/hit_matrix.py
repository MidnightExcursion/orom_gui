import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from gui.statics.statics import _DETECTOR_ARRANGEMENT

class HitDisplayPlot(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()

    def initialize_ui(self):
        layout = QHBoxLayout()
        
        self.all_event_hit_matrix = pg.PlotWidget()
        self.single_event_hit_matrix = pg.PlotWidget()

        self.all_event_hit_matrix.setBackground('white')
        self.single_event_hit_matrix.setBackground('white')

        all_event_hit_matrix_plot_item = self.all_event_hit_matrix.getPlotItem()
        single_event_hit_matrix_plot_item = self.single_event_hit_matrix.getPlotItem()

        all_event_hit_matrix_plot_item.showGrid(x = True, y = True)
        all_event_hit_matrix_plot_item.setTitle('SpinQuest | Hit Distribution for All Events')
        all_event_hit_matrix_plot_item.setLabel('bottom', "Detector ID")
        all_event_hit_matrix_plot_item.setLabel('left', "Element ID (Normalized by Maxmimum Element ID of Detector Array)")

        single_event_hit_matrix_plot_item.showGrid(x = True, y = True)
        single_event_hit_matrix_plot_item.setTitle('SpinQuest | Hit Distribution for Event')
        single_event_hit_matrix_plot_item.setLabel('bottom', "Detector ID")
        single_event_hit_matrix_plot_item.setLabel('left', "Element ID (Normalized by Maxmimum Element ID of Detector Array)")

        layout.addWidget(self.all_event_hit_matrix)
        layout.addWidget(self.single_event_hit_matrix)

        self.setLayout(layout)

    def update_hit_data(self, list_of_hit_matrices, single_hit_matrix, event_number):
        """
        # Description:
        Update the scatter plot with the hit data from all events.

        # Arguments:
        :param list_of_hit_matrices: A rank-3 numpy array where the first index is 
                         the event number, and each event is a rank-2 matrix of 0s and 1s.
        """

        # (1) Obtain the length of the incomig data --- that is the total number of dimuon events:
        number_of_events_in_spill = len(list_of_hit_matrices)

        # (2): Initialize empty lists that will store the points that have hits:

        # (2.1): The detector IDs that have hits go here; they function as the "x-coordinate"
        hit_detectorIDs = []

        # (2.2): The element IDs that have hits are here; they function as the "y-coordinate"
        hit_elementIDs = []

        max_ele = [
            200,
            200,
            168,
            168,
            200,
            200,
            128,
            128,
            112,
            112,
            128,
            128,
            134,
            134,
            112,
            112,
            134,
            134,
            20,
            20,
            16,
            16,
            16,
            16,
            16,
            16,
            72,
            72,
            72,
            72,
            72,
            72,
            72,
            72,
            200,
            200,
            168,
            168,
            200,
            200,
            128,
            128,
            112,
            112,
            128,
            128,
            134,
            134,
            112,
            112,
            134,
            134,
            20,
            20,
            16,
            16,
            16,
            16,
            16,
            16,
            72,
            72,
            72,
            72,
            72,
            72,
            72,
            72
            ]

        for hit_matrix in list_of_hit_matrices:
            
            # (): Obtain a list of lists --- the inner list is just the [row, column] index of hit_matrix with a 1 in it:
            hit_indices = np.argwhere(hit_matrix == 1)
            hit_indices = hit_indices.astype(float)

            for detectorID_and_elementID_pair in hit_indices:
                detectorID_index = int(detectorID_and_elementID_pair[0])
                elementID_index = int(detectorID_and_elementID_pair[1])
                detectorID_and_elementID_pair[1] = elementID_index / max_ele[detectorID_index]

            hit_detectorIDs.extend(hit_indices[:, 0])
            hit_elementIDs.extend(hit_indices[:, 1])

        hit_detectorIDs_for_event = []
        hit_elementIDs_for_event = []

        hit_indices_for_event = np.argwhere(single_hit_matrix == 1)
        hit_indices_for_event = hit_indices_for_event.astype(float)

        for detectorID_and_elementID_pair in hit_indices_for_event:
            detectorID_index = int(detectorID_and_elementID_pair[0])
            elementID_index = int(detectorID_and_elementID_pair[1])
            detectorID_and_elementID_pair[1] = elementID_index / max_ele[detectorID_index]

        hit_detectorIDs_for_event.extend(hit_indices_for_event[:, 0])
        hit_elementIDs_for_event.extend(hit_indices_for_event[:, 1])

        # Create a scatter plot item with aggregated hit coordinates
        hit_display = pg.ScatterPlotItem(
            x = np.array(hit_detectorIDs),
            y = np.array(hit_elementIDs),
            symbol = 's',
            size = 15,
            brush = (255, 0, 0, 5))
        
        hit_display_for_event = pg.ScatterPlotItem(
            x = np.array(hit_detectorIDs_for_event),
            y = np.array(hit_elementIDs_for_event),
            symbol = 's',
            size = 15,
            brush = (255, 0, 0, 5))

        all_event_hit_matrix_plot_item = self.all_event_hit_matrix.getPlotItem()
        single_event_hit_matrix_plot_item = self.single_event_hit_matrix.getPlotItem()

        all_event_hit_matrix_plot_item.clear()
        single_event_hit_matrix_plot_item.clear()

        all_event_hit_matrix_plot_item.addItem(hit_display)
        single_event_hit_matrix_plot_item.addItem(hit_display_for_event)

        all_event_hit_matrix_plot_item.setTitle(f'SpinQuest | Hit Distribution | Total Events: {number_of_events_in_spill}')
        single_event_hit_matrix_plot_item.setTitle(f'SpinQuest | Hit Distribution | Event Number: {event_number}')