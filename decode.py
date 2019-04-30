"""
Decode a wav file using a Goertzel filter.
"""

from goertzel import Goertzel
import numpy as np
import os
from scipy.io import wavfile

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data')

filepath = os.path.join(DATA, "schneider.wav")

# Read sample rate and data from audio file
rate, data = wavfile.read(filepath)

# set target frequency
freq = 160

# create filter and get the output magnitude
g_filter = Goertzel(rate, freq)
magnitude = g_filter.filter(data)
