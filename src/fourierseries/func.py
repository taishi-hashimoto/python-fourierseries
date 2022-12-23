"Some functions"
import numpy as np
from scipy.signal import square, sawtooth


def square_wave(x, T):
    "Periodic square wave for test plot."
    return square((x) * 2*np.pi/T)


def triangular_wave(x, T):
    "Periodic triangular wave for test plot."
    return sawtooth((x-0.5) * 2*np.pi/T, width=0.5)
