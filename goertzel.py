"""
Module to create a Goertzel filter
"""

import numpy as np

class Goertzel():

    def __init__(self, rate, freq):
        self.normalize = 0
        self.coeffs = 0
        self.sample_rate = rate
        self.target_freq = freq


    def calculate_coeff(self):
        """
        Precompute coefficients needed for filter equation.
        Coeff formulas courtesy of Prof. Massey
        """
        n = 160

        w0 = (2 * np.pi * self.target_freq) / self.sample_rate
        self.normalize = np.exp(1j * w0 * n)
        self.coeffs = np.array([np.exp((-1j) * w0 * k) for k in range(n)])

    def filter(self, samples):
        """
        Goertzel filter equation
        :param samples: array of samples
        :returns: amplitude
        """

        #self.calculate_coeff()
        y = self.normalize * 160 * np.dot(self.coeffs, samples)
        ampl = np.abs(y)

        return ampl
