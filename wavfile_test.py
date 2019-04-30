from scipy.io import wavfile
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, 'data')

filepath = os.path.join(DATA, "schneider.wav")

fs, data = wavfile.read(filepath)

print("type of each sample: ")
print(type(data[0]))
