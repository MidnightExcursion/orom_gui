import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QVBoxLayout, QWidget

class HitDisplayPlot(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        
        self.initialize_ui()

    def initialize_ui(self):
        layout = QVBoxLayout()
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('white')
        plot_item = self.plot_widget.getPlotItem()

        plot_item.showGrid(x=True, y=True)
        plot_item.setTitle('SpinQuest | Hit Distribution')
        plot_item.setLabel('bottom', "Detector ID")
        plot_item.setLabel('left', "Element ID")

        layout.addWidget(self.plot_widget)
        self.setLayout(layout)

    def update_hit_data(self, hit_data):
        """
        Update the scatter plot with the hit data from all events.

        :param hit_data: A rank-3 numpy array where the first index is 
                         the event number, and each event is a rank-2 matrix of 0s and 1s.
        """
        number_of_events_in_spill = len(hit_data)
        hit_detectorIDs = []
        hit_elementIDs = []

        for hit_matrix_for_event in hit_data:
            hit_indices = np.argwhere(hit_matrix_for_event == 1)
            hit_detectorIDs.extend(hit_indices[:, 0])  # column indices
            hit_elementIDs.extend(hit_indices[:, 1])  # row indices

        # Create a scatter plot item with aggregated hit coordinates
        hit_display = pg.ScatterPlotItem(
            x=np.array(hit_detectorIDs), y=np.array(hit_elementIDs), symbol='s', size=15, brush=(255, 0, 0, 5)
        )

        plot_item = self.plot_widget.getPlotItem()
        plot_item.clear()
        plot_item.addItem(hit_display)
        plot_item.setTitle(f'SpinQuest | Hit Distribution | Total Events: {number_of_events_in_spill}')