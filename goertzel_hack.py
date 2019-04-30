import numpy as np

# Goertzel algorithm

# precompute constants needed

target_freq = 0
sampling_rate = 0
block_size = 0
pi = 3.14

k = 0.5 + ((block_size * target_freq) / sampling_rate)
omega = ((2 * pi) / block_size) * k

sine = np.sin(omega)
cosine = np.cos(omega)
coeff = 2 * cosine

q1 = 0
q2 = 0

# process the sample
for i in range(0, N):
    q0 = coeff * q1 - q0 + sample # TODO: sample???
    q2 = q1
    q1 = q0
