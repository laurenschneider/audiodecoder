"""
Module to create a Goertzel filter
"""

import numpy as np

class Goertzel():
    def __init__(self):

        self.normalize = 0
        self.coeffs = 0


    def calculate_coeff(self, f, sample_rate):
        """
        Precompute coefficients needed for filter equation.
        Coeff formulas courtesy of Prof. Morrisey
        :param f: target frequency
        :param sample_rate: samples per second
        """

        # TODO: what's n ?????

        w0 = (2 * np.pi * f) / sample_rate
        self.normalize = np.exp(1j * w0 * n)
        self.coeffs = np.array([(-1j) * w0 * k for k in range(n)])

    def filter(self, samples, f):
        """
        Goertzel filter equation
        :param samples: array of samples
        :param f: target frequency
        """

        # todo: what's x ???

        sample_rate = 0
        self.calculate_coeff(f, sample_rate)
        y = np.abs(self.normalize * np.dot(self.coeffs, samples)
