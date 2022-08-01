import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.constants as const
c, posNo = const.c, []

importDist = np.loadtxt("Computing Project/Distance_Mpc.txt", skiprows=0)
importSpec = np.loadtxt(
    "Computing Project/Halpha_spectral_data.csv", skiprows=4, delimiter=",")
importDist = np.sort(importDist, axis=0, kind='quicksort')
importSpec, freqSpec = np.sort(
    importSpec, axis=0, kind='quicksort'), importSpec[0]

for i in range(len(importDist)):
    if int(importDist[i][2]) == 1:
        posNo.append(i)

posNoSpec = [x+1 for x in posNo]
starDist, starSpec = importDist[posNo], importSpec[posNoSpec]


def fitFunc(x, mu, sigma, m, c):
    line = m*x + c
    gaussian = ((sigma*np.sqrt(2*np.pi))**(-1))*np.exp(-(x-mu)**2/(2*sigma**2))
    return gaussian + line


for i in range(2):
    plt.plot(freqSpec[1:], starSpec[i][1:], 'x')
    fitSpec = opt.curve_fit(fitFunc, freqSpec[1:], starSpec[i][1:])
    plt.xlabel("f (Hz)")
    plt.ylabel("Intensity (arbitrary units)")
    plt.show()


print("End")
