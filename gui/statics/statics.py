import numpy as np

_APPLICATION_NAME = "SpinQuest E1039 | Online Reconstruction GUI"
_WINDOW_MAIN_APP_WIDTH = 1000
_WINDOW_MAIN_APP_HEIGHT = 1000

# ========== FILEPATHS ========== 
_PATH_FOR_RAW_DATA = "/data4/e1039_data/online/sraw/"
_PATH_FOR_RECONSTRUCTED_DATA = "/home/e1039orgpu/Jay/Reconstructed_jun24/"

# ========== LEPTONS ========== 

# === ELECTRONS
_MASS_OF_ELECTRON_IN_GEV = 0.00051099895000
_MASS_OF_ELECTRON_UPPER_ERROR_IN_GEV = 0.00000000000015
_MASS_OF_ELECTRON_LOWER_ERROR_IN_GEV = 0.00000000000015

# === MUONS
_MASS_OF_MUON_IN_GEV = .1056583755
_MASS_OF_MUON_UPPER_ERROR_IN_GEV = 0.0000000023
_MASS_OF_MUON_LOWER_ERROR_IN_GEV = 0.0000000023

# === TAUS
_MASS_OF_TAU_IN_GEV = 1.77693
_MASS_OF_TAU_UPPER_ERROR_IN_GEV = 0.00009
_MASS_OF_TAU_LOWER_ERROR_IN_GEV = 0.00009

# ========== MESONS ========== 

# === PI PLUS
_MASS_OF_PI_PLUS_IN_GEV = .13957039
_MASS_OF_PI_PLUS_UPPER_ERROR_IN_GEV = 0.0000001
_MASS_OF_PI_PLUS_LOWER_ERROR_IN_GEV = 0.0000001

# === PI MINUS
_MASS_OF_PI_MINUS_IN_GEV = .13957039
_MASS_OF_PI_MINUS_UPPER_ERROR_IN_GEV = 0.0000001
_MASS_OF_PI_MINUS_LOWER_ERROR_IN_GEV = 0.0000001

# === PI ZERO
_MASS_OF_PI_ZERO_IN_GEV = .1349768
_MASS_OF_PI_ZERO_UPPER_ERROR_IN_GEV = 0.0000005
_MASS_OF_PI_ZERO_LOWER_ERROR_IN_GEV = 0.0000005

# === J PSI
_MASS_OF_J_PSI_IN_GEV = 3.096900
_MASS_OF_J_PSI_UPPER_ERROR_IN_GEV = 0.000006
_MASS_OF_J_PSI_LOWER_ERROR_IN_GEV = 0.000006

# === PSI (2S)
_MASS_OF_PSI_2S_IN_GEV = 3.686097
_MASS_OF_PSI_2S_UPPER_ERROR_IN_GEV = 0.000011
_MASS_OF_PSI_2S_LOWER_ERROR_IN_GEV = 0.000011

# ========== BARYONS ========== 

# === PROTON
_MASS_OF_PROTON_IN_GEV = .93827208816
_MASS_OF_PROTON_UPPER_ERROR_IN_GEV = 0.00000000029
_MASS_OF_PROTON_LOWER_ERROR_IN_GEV = 0.00000000029

# ========== PHYSICS ========== 
_ENERGY_OF_BEAM_IN_GEV = 120.0

_PROBABILITY_DIMUON_EVENT = 0.75

_FOUR_MOMENTUM_OF_BEAM = np.array([
    _ENERGY_OF_BEAM_IN_GEV,
    np.sqrt(np.power(_ENERGY_OF_BEAM_IN_GEV, 2) - np.power(_MASS_OF_PROTON_IN_GEV, 2)),
    0.0,
    0.0])

_FOUR_MOMENTUM_OF_PROTON_TARGET = np.array([
    _MASS_OF_PROTON_IN_GEV,
    0.0,
    0.0,
    0.0])

_FOUR_MOMENTUM_OF_CENTER_OF_MOMENTUM = _FOUR_MOMENTUM_OF_BEAM + _FOUR_MOMENTUM_OF_PROTON_TARGET

_CENTER_OF_MOMENTUM_MANDELSTAM_S = np.power(_FOUR_MOMENTUM_OF_CENTER_OF_MOMENTUM[0] , 2)- np.power(_FOUR_MOMENTUM_OF_CENTER_OF_MOMENTUM[1], 2) + np.power(_FOUR_MOMENTUM_OF_CENTER_OF_MOMENTUM[2], 2) + np.power(_FOUR_MOMENTUM_OF_CENTER_OF_MOMENTUM[3], 2)

# === DETECTOR

_DETECTOR_GROUPS = ["Station 1", "Hodo", "DP-1", "Station 2", "Hodo", "DP-2", "Station 3+", "Station 3-", "Hodo", "Prop", "Hodo", "Prop", "Hodo", "Prop"]
_DETECTOR_NAMES = []

_DETECTOR_ARRANGEMENT = [
            {
                'label': 'Station 1',
                'detectors': [
                    {'name': 'D0V', 'elements': 201, 'id': 5},
                    {'name': 'D0Vp', 'elements': 201, 'id': 6},
                    {'name': 'D0Xp', 'elements': 160, 'id': 4},
                    {'name': 'D0X', 'elements': 160, 'id': 3},
                    {'name': 'D0U', 'elements': 201, 'id': 1},
                    {'name': 'D0Up', 'elements': 201, 'id': 2}
                ]
            },
            {
                'label': 'Hodo',
                'detectors': [
                    {'name': 'H1L', 'elements': 20, 'id': 33},
                    {'name': 'H1R', 'elements': 20, 'id': 34},
                    {'name': 'H1B', 'elements': 23, 'id': 31},
                    {'name': 'H1T', 'elements': 23, 'id': 32}
                ]
            },
            {
                'label': 'DP-1', 
                'detectors': [
                    {'name': 'DP1TL', 'elements': 80, 'id': 55},
                    {'name': 'DP1TR', 'elements': 80, 'id': 56},
                    {'name': 'DP1BL', 'elements': 80, 'id': 57},
                    {'name': 'DP1BR', 'elements': 80, 'id': 58}
                ]
            },
            {
                'label': 'Station 2',
                'detectors': [
                    {'name': 'D2V', 'elements': 128, 'id': 13},
                    {'name': 'D2Vp', 'elements': 128, 'id': 14},
                    {'name': 'D2Xp', 'elements': 112, 'id': 15},
                    {'name': 'D2X', 'elements': 112, 'id': 16},
                    {'name': 'D2U', 'elements': 128, 'id': 17},
                    {'name': 'D2Up', 'elements': 128, 'id': 18}
                ]
            },
            {
                'label': 'Hodo',
                'detectors': [
                    {'name': 'H2R', 'elements': 19, 'id': 36},
                    {'name': 'H2L', 'elements': 19, 'id': 35},
                    {'name': 'H2T', 'elements': 16, 'id': 38},
                    {'name': 'H2B', 'elements': 16, 'id': 37}
                ]
            },
            {
                'label': 'DP-2',
                'detectors': [
                    {'name': 'DP2TL', 'elements': 48, 'id': 59},
                    {'name': 'DP2TR', 'elements': 48, 'id': 60},
                    {'name': 'DP2BL', 'elements': 48, 'id': 61},
                    {'name': 'DP2BR', 'elements': 48, 'id': 62}
                ]
            },
            {
                'label': 'Station 3+',
                'detectors': [
                    {'name': 'D3pVp', 'elements': 134, 'id': 19},
                    {'name': 'D3pV', 'elements': 134, 'id': 20},
                    {'name': 'D3pXp', 'elements': 116, 'id': 21},
                    {'name': 'D3pX', 'elements': 116, 'id': 22},
                    {'name': 'D3pUp', 'elements': 134, 'id': 23},
                    {'name': 'D3pU', 'elements': 134, 'id': 24}
                ]
            },
            {
                'label': 'Station 3-',
                'detectors': [
                    {'name': 'D3mVp', 'elements': 134, 'id': 25},
                    {'name': 'D3mV', 'elements': 134, 'id': 26},
                    {'name': 'D3mXp', 'elements': 116, 'id': 27},
                    {'name': 'D3mX', 'elements': 116, 'id': 28},
                    {'name': 'D3mUp', 'elements': 134, 'id': 29},
                    {'name': 'D3mU', 'elements': 134, 'id': 30}
                ]
            },
            {
                'label': 'Hodo',
                'detectors': [
                    {'name': 'H3T', 'elements': 16, 'id': 40},
                    {'name': 'H3B', 'elements': 16, 'id': 39}
                ]
            },
            {
                'label': 'Prop',
                'detectors': [
                    {'name': 'P1Y1', 'elements': 72, 'id': 47},
                    {'name': 'P1Y2', 'elements': 72, 'id': 48}
                ]
            },
            {
                'label': 'Hodo',
                'detectors': [
                    {'name': 'H4Y1R', 'elements': 16, 'id': 42},
                    {'name': 'H4Y1L', 'elements': 16, 'id': 41}
                ]
            },
            {
                'label': 'Prop',
                'detectors': [
                    {'name': 'P1X1', 'elements': 72, 'id': 49},
                    {'name': 'P1X2', 'elements': 72, 'id': 50}
                ]
            },
            {
                'label': 'Hodo',
                'detectors': [
                    {'name': 'H4Y2R', 'elements': 16, 'id': 44},
                    {'name': 'H4Y2L', 'elements': 16, 'id': 43},
                    {'name': 'H4T', 'elements': 16, 'id': 46},
                    {'name': 'H4B', 'elements': 16, 'id': 45}
                ]
            },
            {
                'label': 'Prop',
                'detectors': [
                    {'name': 'P2X1', 'elements': 72, 'id': 51},
                    {'name': 'P2X2', 'elements': 72, 'id': 52},
                    {'name': 'P2Y1', 'elements': 72, 'id': 53},
                    {'name': 'P2Y2', 'elements': 72, 'id': 54}
                ]
            }
        ]

_MAXIMUM_ELEMENTID_IN_GIVEN_DETECTOR = [
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