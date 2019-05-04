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
        :param f: target frequency
        :param sample_rate: samples per second
        """

        w0 = (2 * np.pi * self.target_freq) / self.sample_rate
        self.normalize = np.exp(1j * w0 * sample_rate)
        self.coeffs = np.array([(-1j) * w0 * k for k in range(sample_rate)])

    def filter(self, samples):
        """
        Goertzel filter equation
        :param samples: array of samples
        :returns: amplitude
        """

        self.calculate_coeff(self.target_freq, self.sample_rate)
        y = np.abs(self.normalize * np.dot(self.coeffs, samples)

        return y
