import os

import numpy as np

from numba import njit

from gui.statics.statics import _MASS_OF_MUON_IN_GEV, _MASS_OF_PROTON_IN_GEV
from gui.statics.statics import _PATH_FOR_RECONSTRUCTED_DATA
from gui.statics.statics import _PROBABILITY_DIMUON_EVENT

def calculate_invariant_mass(slice_of_events_and_kinematics):
    """
    # Description:
    We reconstruct the invariant mass of the dimuon pair in
    the lab frame.
    """

    positive_muon_momentum_x = slice_of_events_and_kinematics[:, 0]
    positive_muon_momentum_y = slice_of_events_and_kinematics[:, 1]
    positive_muon_momentum_z = slice_of_events_and_kinematics[:, 2]
    negative_muon_momentum_x = slice_of_events_and_kinematics[:, 3]
    negative_muon_momentum_y = slice_of_events_and_kinematics[:, 4]
    negative_muon_momentum_z = slice_of_events_and_kinematics[:, 5]

    energy_of_proton_beam_in_GeV = 120.0

    momentum_of_beam = np.array([
        0.0,
        0.0,
        np.sqrt(energy_of_proton_beam_in_GeV * energy_of_proton_beam_in_GeV - _MASS_OF_PROTON_IN_GEV * _MASS_OF_PROTON_IN_GEV),
        energy_of_proton_beam_in_GeV])
    
    momentum_target = np.array([0.0, 0.0, 0.0, _MASS_OF_PROTON_IN_GEV])
    momentum_center_of_mass = momentum_of_beam + momentum_target

    # (): Calculate the first component of p_{mu}:
    energy_of_positive_muon = np.sqrt(positive_muon_momentum_x * positive_muon_momentum_x + positive_muon_momentum_y * positive_muon_momentum_y + positive_muon_momentum_z * positive_muon_momentum_z + _MASS_OF_MUON_IN_GEV * _MASS_OF_MUON_IN_GEV)
    
    four_momentum_positive_muon = np.array([
        energy_of_positive_muon,
        positive_muon_momentum_x, 
        positive_muon_momentum_y,
        positive_muon_momentum_z])

    energy_of_negative_muon = np.sqrt(negative_muon_momentum_x * negative_muon_momentum_x + negative_muon_momentum_y * negative_muon_momentum_y + negative_muon_momentum_z * negative_muon_momentum_z + _MASS_OF_MUON_IN_GEV * _MASS_OF_MUON_IN_GEV)
    
    four_momentum_negative_muon = np.array([
        energy_of_negative_muon,
        negative_muon_momentum_x,
        negative_muon_momentum_y,
        negative_muon_momentum_z])

    total_momentum_four_vector = four_momentum_positive_muon + four_momentum_negative_muon

    invariant_dimuon_mass_squared = np.power(total_momentum_four_vector[0], 2) - (np.power(total_momentum_four_vector[1], 2) + np.power(total_momentum_four_vector[2], 2) + np.power(total_momentum_four_vector[3], 2))
    
    invariant_dimuon_mass_squared_no_negative_masses = [mass for mass in invariant_dimuon_mass_squared if mass >= 0]
    
    invariant_dimuon_mass = np.sqrt(invariant_dimuon_mass_squared_no_negative_masses)

    return invariant_dimuon_mass


def obtain_verticies(file_path):
    """
    # Description:
    Given a `.npy` or `.npz` file, extract the vertex information for
    each event.
    
    # Arguments:

    # Returns:
    """

    print(f"Reading file: {file_path}")
    data = np.load(file_path)

    # Extract file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    try:
        return data[21], data[24], data[22], data[25], data[23], data[26], file_name
    
    except IndexError as ERROR:
        print(f"Error: {ERROR}. Make sure the file contains data[21], data[22], data[23], data[24], data[25], and data[26].")


class FourVector:
    def __init__(self, zeroth_component, first_component, second_component, third_component):
        self.zeroth_component = zeroth_component
        self.first_component = first_component
        self.second_component = second_component
        self.third_component = third_component
