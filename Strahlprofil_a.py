# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:27:53 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from functools import partial #https://stackoverflow.com/questions/61675014/integral-with-variable-limits-in-python

csv_path_a = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_a.csv"
csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv" # Vielleicht Teil b in eigenen Code auslagern 

a_72 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5,6,7,8]) #Daten für 7,2 cm
a_45 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4,5,6,7,8]) 
a_105 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4,5,6])
data_a = [a_45, a_72, a_105]

h = 6.62607015*10**(-34)
c = 299792458
wvl = 632.8*10**(-9)
e = 1.602176634*10**(-19)
distLS = 15.5 #Distance lens-fibre end (Source of laser beam)
Rd = 10**4 #Resistance of the photodiode in ohm
x = np.linspace(-10,10, 100)

#the positions must be arranged symmetrically around zero (zero-centered):
v1 = 12.8 #Verschiebung für rot
v2 = 1.2 #Verschiebung für blau
v3 = 6.9 # Verschiebung für grün
#normalized micrometer positions:
x72 = a_72.values[0]-v1 
x45 = a_45.values[0]-v2
x105 = a_105.values[0]-v3

maxints = []
omegas = []

def P(U, R):
    return (h*c*U)/(wvl*R*e*0.75)

def gaussint(x, I0, w):
    inner = lambda xp: np.exp((-2*xp**2)/(w**2))
    #inteqrate.quad kann keine Integrationsgrenzen als Variablen haben, darum kompliziertere Lösung:
    integral = np.array(list(map(partial(integrate.quad, inner, b=np.inf), x)))[:,0]
    return I0*integral

def rayleigh(w):
    return (np.pi*w**2)/wvl

plt.plot(x72, P(a_72.values[1], Rd), 'ro', label="8,3 +- 0,2cm")
plt.plot(x45, P(a_45.values[1], Rd), 'bo', label="11,0 +- 0,2 cm")
plt.plot(x105, P(a_105.values[1], Rd), 'go', label="5,0 +- 0,2 cm")

#8,3cm fit
popt, cov = curve_fit(gaussint, x72, P(a_72.values[1], Rd), bounds=(0, 15))
maxintensity, omega = popt
plt.plot(x, gaussint(x, maxintensity, omega), 'r') 
#popt, cov = curve_fit(gaussint, x72new[2:], P((a_72.values[1]), Rd)[2:])
#maxintensity, omega = popt
maxints.append(maxintensity)
omegas.append(omega)
#plt.plot(x72[2:], gaussint(x72new[2:], maxintensity, omega), 'r')
print("8,3cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)

#11cm fit
popt, cov = curve_fit(gaussint, x45, P(a_45.values[1], Rd), bounds=(0, 15))
maxintensity, omega = popt
plt.plot(x, gaussint(x, maxintensity, omega), 'b')
print("11cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)

#5,0cm fit
popt, cov = curve_fit(gaussint, x105, P(a_105.values[1], Rd), bounds=(0, 15))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas.append(omega)
plt.plot(x, gaussint(x, maxintensity, omega), 'g')
print("5,0cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)

plt.xlabel("x-x_0 in mm (zero-centered micrometer position)")
plt.ylabel("power in mW") #Milli weil die Spannungen in mV angegeben sind
plt.legend(title="Distance razor blade - fibre end")
plt.title("cross section profile of collimated beam")
plt.savefig("part a: cross section profile of collimated beam.png", dpi=400)

print("waist: (", np.mean(omegas), "+-", np.std(omegas), ") mm")
rays = [rayleigh(i)/10**6 for i in omegas] #10**6 weil millimeter umrechnen
print("rayleigh length: (", np.mean(rays), "+-", np.std(rays), ") mm")
