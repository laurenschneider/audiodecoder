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

# set target frequencies
mark_freq = 2225
space_freq = 2025

# create two filters
mark_filter = Goertzel(rate, mark_freq)
space_filter = Goertzel(rate, space_freq)

bit_string = ''

# for all samples in numpy array of data
for i in range(0, data.size):

    # for each chunk of 160 samples
    if i%160 == 0:
        start = i - 159
        end = i - 1
        samples = data[start:end]

        # get amplitutes of sample set
        mark_amp = mark_filter.filter(samples)
        space_amp = space_filter.filter(samples)

        if mark_amp > space_amp:
            # bit is 1
            to_add = '1'
        else:
            # bit is zero
            to_add = '0'
        bit_string = bit_string + to_add

# total message
message = ''

for x in range(0, len(bit_string)):
    if x%10 == 0:
        start = x - 9
        end = x - 1
        message = message + chr(int(bit_string[start:end],2))
