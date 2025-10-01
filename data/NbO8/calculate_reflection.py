import numpy as np
import matplotlib.pyplot as plt


def KM_reflection(filename):
    data = np.loadtxt(filename, skiprows=1)
    absorbance = data[:,1]
    reflect = (absorbance + 1) - 0.5 * np.sqrt(4*(absorbance+1)**2 - 4)
    return reflect

abs_file = 'K3NbO8_brown.txt'

for point in KM_reflection(abs_file):
    print(point)
