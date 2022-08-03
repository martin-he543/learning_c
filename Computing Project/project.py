import numpy as np, matplotlib.pyplot as plt # IMPORT PYTHON LIBRARIES
import scipy.optimize as opt, scipy.constants as const
titleFont, axesFont, ticksFont, pointStyle, lineStyle = {'fontname': 'Bodoni 72', 'size': 8}, {'fontname': 'CMU Sans Serif', 'size': 8}, {'fontname': 'DM Mono', 'size': 5}, {'mew': 0.5, 'ms': 3, 'color': 'green'}, {'linewidth': 0.9, 'color': 'red'}
c, pi, fwhm_const, h_alpha, posNo, velocities = const.c, np.pi, 2*np.sqrt(2*np.log(2)), 656.26e-9, [], []
distImport = np.loadtxt("Computing Project/Distance_Mpc.txt", skiprows=0) # LOAD DATA FROM TEXT FILES
specImport = np.loadtxt("Computing Project/Halpha_spectral_data.csv", skiprows=4, delimiter=",")
distSort = distImport[np.argsort(distImport[:,0],axis=0)] # SORT DATA ACCORDING TO FIRST COLUMN
specSort = specImport[np.argsort(specImport[:,0], axis=0)]

for i in range(len(distSort)):
    if int(distSort[i][2]) == 1 : posNo.append(i)
distStar, specStar, specFreq = distSort[posNo], specSort[[x+1 for x in posNo]], specSort[0][1:]

def linear(x,m,c): return m*x+c
def gaussian(x,a,mu,sigma): return a*np.exp(-(x-mu)**2/(2*sigma**2))
def model(x,a,mu,sigma,m,c): return linear(x,m,c)+gaussian(x,a,mu,sigma)

for j in range(len(distStar)):
    plt.subplot(5,5,j+1)
    specStarData = specStar[j][1:]
    plt.plot(specFreq, specStarData, 'x', **pointStyle)
    plt.title("Observation Number: %d" %(distStar[j][0]), **titleFont)
    plt.xlabel("f (Hz)", **axesFont), plt.ylabel("Intensity", **axesFont), plt.xticks(**ticksFont), plt.yticks(**ticksFont)

    fitLinear,fitLinearCov = opt.curve_fit(linear,specFreq,specStarData)
    guess_m, guess_c = fitLinear[0], fitLinear[1]
    
    specStarGaussian = specStarData - linear(specStarData,guess_m,guess_c)
    indexMax = int(np.where(specStarGaussian == np.max(specStarGaussian))[0])
    guess_mu, guess_a = specFreq[indexMax], np.max(specStarData - linear(specFreq[indexMax],guess_m,guess_c))
    guess_fwhm = np.abs(specStarGaussian-guess_a/2)
    indexMin = np.sort(guess_fwhm)
    x1,x2 = specFreq[int(np.where(guess_fwhm == indexMin[0])[0])],specFreq[int(np.where(guess_fwhm == indexMin[1])[0])]
    guess_sigma = np.abs((x2-x1)/fwhm_const)

    guessInitial = [guess_a,guess_mu,guess_sigma,guess_m,guess_c]
    guessFinal, guessCov = opt.curve_fit(model,specFreq,specStarData,guessInitial)
    plt.plot(specFreq,model(specFreq,*guessFinal),**lineStyle)
    
    wavelengthRatio = (c/guessFinal[1])/h_alpha
    v = c*(wavelengthRatio**2 - 1)/((wavelengthRatio**2 + 1)*1000) # CONVERT TO km/s
    velocities.append(v)
    print("Plot: %d"%j)
    print("A = %r, μ = %r, σ = %r, m = %r, c = %r"%(guessInitial[0],guessInitial[1],guessInitial[2],guessInitial[3],guessInitial[4]))
    print("A = %r, μ = %r, σ = %r, m = %r, c = %r"%(guessFinal[0],guessFinal[1],guessFinal[2],guessFinal[3],guessFinal[4]))
    #print(fitLinearCov[0,0])

plt.show()

plt.plot(distStar[:,1],velocities,'x')
fitHubble, fitHubbleCov = opt.curve_fit(linear,distStar[:,1],velocities)
plt.plot(distStar[:,1],linear(distStar[:,1],*fitHubble))
plt.show()

print("Hubble Constant: (%d ± %d) km/s/Mpc " %(fitHubble[0],np.sqrt(np.abs(fitHubbleCov[0,0]))))

print("End")
