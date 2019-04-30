"""
Decode a wav file using a Goertzel filter.
Logic for wav file reading inspired by Bart Massey's pdx-cs-sound project.
"""

from goertzel import Goertzel
import numpy as np
import os
import wave

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data')

filepath = os.path.join(DATA, "")
wavfile = wave.open(filepath, 'rb')

# Channels per frame.
#channels = wavfile.getnchannels()

# Bytes per sample.
#width = wavfile.getsampwidth()

# Sample rate
rate = wavfile.getframerate()

# Number of frames.
num_frames = wavfile.getnframes()

# Length of a frame
#frame_width = width * channels

# Get all samples
samples = wavfile.readframes(num_frames)


wavfile.close
