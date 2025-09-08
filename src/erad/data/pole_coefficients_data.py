from erad.enums import PoleClass, PoleConstructionMaterial

""" This module contains pole coefficients data from Darestani et al. (2019) Tables 14-20"""
Darestani2019_PoleCoefficients = {
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_1): {
        'mu_coefficients': [5.581, -4.306E-3, -2.408E-2, 5.986E-3, 2.569E-5, -1.231E-3, 3.524E-3,  0, -1.324E-5, -1.327E-4],
        'sigma_coefficients': [ 2.974E-01 , -1.411E-03, -9.462E-03, -2.678E-03, 7.782E-06, -5.088E-05, 6.199E-04, 6.805E-06, 5.630E-05, 6.037E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_2): {
        'mu_coefficients': [5.770, -6.730E-03, -3.904E-02, 6.090E-03, 4.342E-05, -1.383E-03, 4.972E-03, 0, 0, -1.328E-04],
        'sigma_coefficients': [2.080E-01, -5.938E-04, -3.661E-03, -2.254E-03, 3.320E-06, 0, 2.357E-04, 3.039E-06, 1.932E-05, 6.262E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_3): {
        'mu_coefficients': [5.874, -8.946E-03, -5.238E-02, 6.291E-03, 5.994E-05, -1.468E-03, 6.167E-03, 0, 0, -1.342E-04],
        'sigma_coefficients': [1.698E-01, -1.165E-04, 0, -2.016E-03, 0, 0, 0, 9.217E-07, 0, 6.326E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_4): {
        'mu_coefficients': [5.930E0, -1.091E-02, -6.420E-02, 6.387E-03, 7.453E-05, -1.521E-03, 7.169E-03, 0, 0, -1.352E-04],
        'sigma_coefficients': [1.568E-01, 0, 0, -1.990E-03, 0, 0, 0, 0, 0, 6.428E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_5): {
        'mu_coefficients': [6.029, -1.378E-02, -8.249E-02, 6.381E-03, 9.546E-05, -1.561E-03, 8.640E-03, 0, 0, -1.358E-04],
        'sigma_coefficients': [1.743E-01, -1.431E-04, 0, -2.042E-03, 1.085E-06, 0, 0, 0, 0, 6.477E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_6): {
        'mu_coefficients': [6.111, -1.683E-02, -9.992E-02, 6.409E-03, 1.182E-04, -1.597E-03, 1.002E-02, 0, 0, -1.365E-04],
        'sigma_coefficients': [1.535E-01, 1.930E-04, 2.421E-03, -1.790E-03, 0, 0, 0, -3.331E-06, -3.473E-05, 6.519E-05]
    },
    (PoleConstructionMaterial.WOOD, PoleClass.CLASS_7): {
        'mu_coefficients': [6.130, -1.873E-02, -1.130E-01, 6.291E-03, 1.314E-04, -1.595E-03, 1.101E-02, 0, 0, -1.371E-04],
        'sigma_coefficients': [1.460E-01, 3.313E-04, 2.857E-03, -1.609E-03, 0, -1.538E-05, 0, -6.106E-06, -5.067E-05, 6.576E-05]
    },
}




