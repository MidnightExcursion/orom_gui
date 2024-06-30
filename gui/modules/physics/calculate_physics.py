import os

import numpy as np

from numba import njit

from gui.statics.statics import _MASS_OF_MUON_IN_GEV, _MASS_OF_PROTON_IN_GEV
from gui.statics.statics import _PATH_FOR_RECONSTRUCTED_DATA
from gui.statics.statics import _PROBABILITY_DIMUON_EVENT


def calculate_dimuon_four_momentum_sum(slice_of_events_and_kinematics):
    pass

def calculate_invariant_mass(slice_of_events_and_kinematics):
    """
    # Description:
    We reconstruct the invariant mass of the dimuon pair in
    the lab frame.
    """

    # (1): Obtain the columns containing momenta for the plus and minus muon:

    # (1.1): Obtain the column corresponding to the positive muons's p_{x}:
    positive_muon_momentum_x = slice_of_events_and_kinematics[:, 0] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[0]

    # (1.2): Obtain the column corresponding to the positive muons's p_{y}:
    positive_muon_momentum_y = slice_of_events_and_kinematics[:, 1] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[1]

    # (1.3): Obtain the column corresponding to the positive muons's p_{z}:
    positive_muon_momentum_z = slice_of_events_and_kinematics[:, 2] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[2]

    # (1.4): Obtain the column corresponding to the negative muons's p_{x}:
    negative_muon_momentum_x = slice_of_events_and_kinematics[:, 3] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[3]

    # (1.5): Obtain the column corresponding to the negative muons's p_{y}:
    negative_muon_momentum_y = slice_of_events_and_kinematics[:, 4] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[4]

    # (1.6): Obtain the column corresponding to the negative muons's p_{z}:
    negative_muon_momentum_z = slice_of_events_and_kinematics[:, 5] if slice_of_events_and_kinematics.ndim == 2 else slice_of_events_and_kinematics[5]

    energy_of_proton_beam_in_GeV = 120.0

    momentum_of_beam = np.array([
        0.0,
        0.0,
        np.sqrt(energy_of_proton_beam_in_GeV * energy_of_proton_beam_in_GeV - _MASS_OF_PROTON_IN_GEV * _MASS_OF_PROTON_IN_GEV),
        energy_of_proton_beam_in_GeV])
    
    momentum_target = np.array([0.0, 0.0, 0.0, _MASS_OF_PROTON_IN_GEV])
    momentum_center_of_mass = momentum_of_beam + momentum_target

    # (): Calculate the first component of p_{mu}:
    energy_of_positive_muon = np.sqrt(
        positive_muon_momentum_x * positive_muon_momentum_x + 
        positive_muon_momentum_y * positive_muon_momentum_y + 
        positive_muon_momentum_z * positive_muon_momentum_z + 
        _MASS_OF_MUON_IN_GEV * _MASS_OF_MUON_IN_GEV)
    
    four_momentum_positive_muon = np.array([
        energy_of_positive_muon,
        positive_muon_momentum_x, 
        positive_muon_momentum_y,
        positive_muon_momentum_z])

    energy_of_negative_muon = np.sqrt(
        negative_muon_momentum_x * negative_muon_momentum_x + 
        negative_muon_momentum_y * negative_muon_momentum_y + 
        negative_muon_momentum_z * negative_muon_momentum_z + 
        _MASS_OF_MUON_IN_GEV * _MASS_OF_MUON_IN_GEV)
    
    four_momentum_negative_muon = np.array([
        energy_of_negative_muon,
        negative_muon_momentum_x,
        negative_muon_momentum_y,
        negative_muon_momentum_z])

    total_momentum_four_vector = four_momentum_positive_muon + four_momentum_negative_muon

    invariant_dimuon_mass_squared = np.power(total_momentum_four_vector[0], 2) - (np.power(total_momentum_four_vector[1], 2) + np.power(total_momentum_four_vector[2], 2) + np.power(total_momentum_four_vector[3], 2))

    if isinstance(invariant_dimuon_mass_squared, np.ndarray):
        invariant_dimuon_mass_squared_no_negative_masses = [mass for mass in invariant_dimuon_mass_squared if mass >= 0]
    else:
        invariant_dimuon_mass_squared_no_negative_masses = invariant_dimuon_mass_squared if invariant_dimuon_mass_squared >= 0 else []

    
    invariant_dimuon_mass = np.sqrt(invariant_dimuon_mass_squared_no_negative_masses)

    return invariant_dimuon_mass

def calculate_transverse_momentum(four_momentum_positive_muon, four_momentum_negative_muon):
    """
    # Description:
    We simply calculate the transverse momentum of the mother particle.
    """

    total_transverse_momentum = np.sqrt(np.power(four_momentum_positive_muon[3], 2) + np.power(four_momentum_negative_muon[3], 2))

    return total_transverse_momentum

def calculate_x1():
    pass

def calculate_cosine_theta(four_momentum_positive_muon, four_momentum_negative_muon, dimuon_invariant_mass, transverse_momentum):
    """
    # Description:
    Calculate the cosine of the lab angle.
    """
    cosine_theta = np.arctan2(
         2.0 * (
        four_momentum_negative_muon[3] * four_momentum_positive_muon[2] - four_momentum_positive_muon[3] * four_momentum_negative_muon[2]
        ) / dimuon_invariant_mass / np.sqrt(dimuon_invariant_mass * dimuon_invariant_mass + transverse_momentum * transverse_momentum)
    )
    return cosine_theta

def calculate_sine_theta(cosine_theta):
    """
    # Description:
    Calculate the sine of the angle simply using the familiar trigonometric
    identity:

    $$sin^{2}(x) + cos^{2}(x) = 1$$.
    """
    sine_theta = np.sqrt(1. - np.power(cosine_theta, 2))
    return sine_theta


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
