import os

import numpy as np

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import  QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QMessageBox, QLineEdit

from gui.widgets.light_indicator import LightIndicator

from gui.statics.statics import _PATH_FOR_RECONSTRUCTED_DATA

class CentralMenu(QWidget):

    state_updated = pyqtSignal(dict)

    def __init__(self):

        # (1): Initialize the QWidget superclass:
        super().__init__()

        # (2): Obtain the directory that contains reconstructed data:
        self.current_directory = _PATH_FOR_RECONSTRUCTED_DATA

        # (3): Sort ALL the files in the given directory (if it's an .npz file):
        self.sorted_files = sorted([file for file in os.listdir(self.current_directory) if (file.endswith('.npz') or file.endswith('.npy'))])

        # (4): Set the current file index to 0 to indicate that we haven't chosen a file yet but just want something to display:
        self.current_file_index = 0

        # (5): Set the "reconstruction flag" to be True:
        self._ONLNE_RECONSTRUCTION_SETTING = True

        # (6): Initialize the UI:
        self.initialize_ui()

        # (7): Once the UI has been initialized, we propagate the first piece of data:
        self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)

    def initialize_ui(self):
        
        # (1): Initialize the top-level HBox that has (i) light and (ii) 3x3 button menu:
        horizonal_box_layout_for_light_and_buttons = QHBoxLayout()

        # (2.1): Initialize first child component of top-level HBox: light indicator:
        self.light_indicator = LightIndicator()

        # (2.2): Initialize the second child component of top-level HBox: 3x3 button menu:
        self.button_menu_grid_layout = QGridLayout()
        self.button_menu_grid = QWidget()

        # (3): Initialize each 1x3 HBox button layout:

        vertical_box_layout_for_menu_buttons = QVBoxLayout()

        vertical_box_layout = QVBoxLayout()

        self.textbox = QLineEdit(self)
        self.textbox.setReadOnly(True)

        self.textbox_run_number = QLineEdit(self)
        self.textbox_run_number.setReadOnly(True)

        self.textbox_spill_number = QLineEdit(self)
        self.textbox_spill_number.setReadOnly(True)

        self.textbox_event_number = QLineEdit(self)
        self.textbox_event_number.setReadOnly(True)

        button_current_run = QPushButton("[ Current Run ]")
        button_current_run.setCheckable(False)
        button_current_run.clicked.connect(self.button_current_clicked)

        button_previous_run = QPushButton("[ Previous Run ]")
        button_previous_run.setCheckable(False)
        button_previous_run.clicked.connect(self.button_previous_clicked)
        
        button_next_run = QPushButton("[ Next Run ]")
        button_next_run.setCheckable(False)
        button_next_run.clicked.connect(self.button_next_clicked)

        button_current_spill = QPushButton("[ Current Spill ]")
        button_current_spill.setCheckable(False)
        button_current_spill.clicked.connect(self.button_current_clicked)

        button_previous_spill = QPushButton("[ Previous Spill ]")
        button_previous_spill.setCheckable(False)
        button_previous_spill.clicked.connect(self.button_previous_clicked)
        
        button_next_spill = QPushButton("[ Next Spill ]")
        button_next_spill.setCheckable(False)
        button_next_spill.clicked.connect(self.button_next_clicked)

        button_current_event = QPushButton("[ Current Event ]")
        button_current_event.setCheckable(False)
        button_current_event.clicked.connect(self.button_current_clicked)

        button_previous_event = QPushButton("[ Previous Event ]")
        button_previous_event.setCheckable(False)
        button_previous_event.clicked.connect(self.button_previous_clicked)
        
        button_next_run_event = QPushButton("[ Next Event ]")
        button_next_run_event.setCheckable(False)
        button_next_run_event.clicked.connect(self.button_next_clicked)

        self.button_menu_grid_layout.addWidget(button_current_run, 0, 0)
        self.button_menu_grid_layout.addWidget(button_previous_run, 0, 1)
        self.button_menu_grid_layout.addWidget(button_next_run, 0, 2)

        self.button_menu_grid_layout.addWidget(button_current_spill)
        self.button_menu_grid_layout.addWidget(button_previous_spill)
        self.button_menu_grid_layout.addWidget(button_next_spill)

        self.button_menu_grid_layout.addWidget(button_current_event)
        self.button_menu_grid_layout.addWidget(button_previous_event)
        self.button_menu_grid_layout.addWidget(button_next_run_event)

        self.button_menu_grid.setLayout(self.button_menu_grid_layout)

        horizonal_box_layout_for_light_and_buttons.addWidget(self.light_indicator)
        horizonal_box_layout_for_light_and_buttons.addWidget(self.button_menu_grid)

        vertical_box_layout.addLayout(horizonal_box_layout_for_light_and_buttons)
        vertical_box_layout.addWidget(self.textbox)
        vertical_box_layout.addWidget(self.textbox_run_number)
        vertical_box_layout.addWidget(self.textbox_spill_number)
        vertical_box_layout.addWidget(self.textbox_event_number)

        self.setLayout(vertical_box_layout)

    def confirm_button_press(self):
        """
        # Description:
        If the reconstruction loop is `LIVE`, then we need
        to verify that the user wants to momentarily disable
        it in order to display earlier reconstructed data.
        """

        if self._ONLNE_RECONSTRUCTION_SETTING == True:
            print("> Request to turn online monitoring off...")
            reply = QMessageBox.question(self,
                        'Confirmation',
                        'Performing this action will stop the live reconstruction feed. Proceed?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                self._ONLNE_RECONSTRUCTION_SETTING = False
                self.light_indicator.status = 'ORANGE'
                self.light_indicator.update_color()
                return True
            else:
                return False
            
        elif self._ONLNE_RECONSTRUCTION_SETTING == False:
            print("> Request to turn online monitoring ON...")
            reply = QMessageBox.question(self,
                        'Confirmation',
                        'Would you like to turn online reconstruction back on?',
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No)
                
            if reply == QMessageBox.Yes:
                self._ONLNE_RECONSTRUCTION_SETTING = True
                self.light_indicator.status = 'RED'
                self.light_indicator.update_color()
        else:
            print(f"> Bug in code....")

    def button_previous_clicked(self):
        print(f"> PREVIOUS initiated: Reco on? {self._ONLNE_RECONSTRUCTION_SETTING}. Current index: {self.current_file_index}")

        # (1.1): If online reconstruction is on:
        if self._ONLNE_RECONSTRUCTION_SETTING:

            did_user_turn_off_orom = self.confirm_button_press()

            if did_user_turn_off_orom:
                print("> Previous button clicked!")
                self._ONLNE_RECONSTRUCTION_SETTING = False
                self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)
            else:
                print("> Ignored.")

        # (1.2): If online reconstruction is off:
        else:
            print('asdas')
            if self.current_file_index == 0:
                print('asfsd')
                pass
            else:
                print('sd')
                self.current_file_index = self.current_file_index - 1
                self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)

        print('zz')

    def button_next_clicked(self):
        print(f"> NEXT initiated: Reco on? {self._ONLNE_RECONSTRUCTION_SETTING}. Current index: {self.current_file_index}")
        
        # (1.1): If online reconstruction is on:
        if self._ONLNE_RECONSTRUCTION_SETTING:

            did_user_turn_off_orom = self.confirm_button_press()

            if did_user_turn_off_orom:
                print("> Next button clicked!")
                self._ONLNE_RECONSTRUCTION_SETTING = False
                self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)
            else:
                print("> Ignored.")

        # (1.2): If online reconstruction is off:
        else:

            print('a')

            # (1.2.1): If the current file index is already at the "most recent file", then ignore:
            if self.current_file_index == len(self.sorted_files) - 1:
                print('z')
                pass
            else:
                print('ff')
                self.current_file_index = self.current_file_index + 1
                self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)

    def button_current_clicked(self):
        print(f"> CURRENT initiated: Reco on? {self._ONLNE_RECONSTRUCTION_SETTING}. Current index: {self.current_file_index}")
        
        # (1.1): If online reconstruction is on:
        if self._ONLNE_RECONSTRUCTION_SETTING:

            pass

        # (1.2): If online reconstruction is off:
        else:

            did_user_turn_on_orom = self.confirm_button_press()

            if did_user_turn_on_orom:
                print("> Current button clicked!")
                self._ONLNE_RECONSTRUCTION_SETTING = True
                self.load_file_contents(self._ONLNE_RECONSTRUCTION_SETTING)
            else:
                print("> Ignored.")

    def load_file_contents(self, turned_on_orom_boolean):
        """
        # Description: 
        This function will read the CentralMenu's state
        and propagate it to all of the tabs that utilize it. 
        """

        self.current_file_index = 0 if turned_on_orom_boolean else self.current_file_index

        self.current_event_number_index = 0

        # (1): Obtain the name of the file:
        name_of_current_file = self.sorted_files[self.current_file_index]
        
        # (2): We find the filepath of the file that we are reading:
        file_path = os.path.join(self.current_directory, name_of_current_file)

        # (3): Use NumPy's `.npy` file-reader function to read the file:
        file_data = np.load(file_path)

        # # (4): The `.npz` file contains three pieces of relevant data:
        print(f"> Run {file_data['output_data'][0, 34]}, Spill {file_data['output_data'][0, 36]}, Event {file_data['output_data'][0, 35]}")
        print(file_data['output_data'][0, 38])

        # # (4.1): [1] | Physics Data:
        output_data = file_data['output_data']

        # (4.2): [2] | Hit Matrix
        hit_matrix = file_data['hit_matrix']

        # (4.3): [3] | Track Data:
        track_data = file_data['Tracks']

        # (5): We obtain the name of the file so we can propagate it to the CentralMenu textbox:
        filename_data = f"> Current File: {self.sorted_files[self.current_file_index]}"
        
        # (6): This follows from (3): we put the filename into the textbox with .setText()
        current_run_number = output_data[0, 34]
        current_spill_number = output_data[0, 36]
        current_event_number = output_data[0, 35]
        
        self.textbox.setText(filename_data)
        self.textbox_run_number.setText(f"> Run: {current_run_number}")
        self.textbox_spill_number.setText(f"> Spill: {current_spill_number} ")
        self.textbox_event_number.setText(f"> Event: {current_event_number}")


        # # (5): Finally, we emit the file name and the file data to all of the tabs of the GUI:
        self.state_updated.emit({
            'filename': name_of_current_file,
            'filepath': file_path,
            'file_output_data': output_data,
            'file_hit_matrix': hit_matrix,
            'file_track_data': track_data
            })

