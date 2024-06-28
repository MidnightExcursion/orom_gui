from PyQt5.QtWidgets import  QWidget, QGridLayout, QPushButton, QMessageBox

from gui.widgets.light_indicator import LightIndicator

from gui.graphs.hit_matrix import HitDisplayPlot
from gui.graphs.mass_histogram import MassHistogram

class MainMenuTab(QWidget):
    def __init__(self, tab_widget):
        super().__init__()

        self.name = "Dashboard"

        self.tab_widget = tab_widget

        self.initialize_ui()

    def initialize_ui(self):

        main_menu_tab_layout = QGridLayout()

        self.hit_display_plot = HitDisplayPlot()
        self.mass_histogram = MassHistogram()
        
        main_menu_tab_layout.addWidget(self.hit_display_plot, 0, 0)
        main_menu_tab_layout.addWidget(self.mass_histogram, 0, 1)

        self.setLayout(main_menu_tab_layout)