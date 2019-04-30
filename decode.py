"""
Decode a wav file using a Goertzel filter
"""

import numpy as np
import wave
from goertzel import Goertzel

wavfile = wave.open("", 'rb')

wavfile.close
