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

distLS = 15.5 #Distance lense-fibre end (Source of laser beam)
Ud = 10 #Resistance of the photodiode in kiloohm
#normalized micrometer positions:
x72 = a_72.values[0]-a_72.values[0][0] 
x72new = a_72.values[0]-a_72.values[0][2]
x45 = a_45.values[0]-a_45.values[0][0]
x105 = a_105.values[0]-a_105.values[0][0]

def P(U, R):
    h = 6.62607015*10**(-34)
    c = 299792458
    wvl = 632.8*10**(-9)
    e = 1.602176634*10**(-19)
    return (h*c*U)/(wvl*R*e*0.75)

def gaussint(x, I0, w):
    inner = lambda xp: np.exp((-2*xp**2)/(w**2))
    #inteqrate.quad kann keine Integrationsgrenzen als Variablen haben, darum kompliziertere Lösung:
    integral = np.array(list(map(partial(integrate.quad, inner, b=np.inf), x)))[:,0]
    return I0*integral

plt.plot(x72, P(a_72.values[1], 10), 'ro', label="8,3cm")
plt.plot(x45, P(a_45.values[1], 10), 'bo', label="11,0 cm")
plt.plot(x105, P(a_105.values[1], 10), 'go', label="5,0 cm")
plt.xlabel("x-x_0 (normalized micrometer position)")
plt.ylabel("power in mW")
plt.legend(title="Distance razor blade - fibre end")
plt.title("cross section profile of collimated beam")

#8,3cm fit
popt, cov = curve_fit(gaussint, x72, P(a_72.values[1], 10))
maxintensity, omega = popt
plt.plot(x72, gaussint(x72, maxintensity, omega), 'r--') #Die ersten beiden Werte sind schlecht
popt, cov = curve_fit(gaussint, x72new[2:], P((a_72.values[1]), 10)[2:])
maxintensity, omega = popt
plt.plot(x72[2:], gaussint(x72new[2:], maxintensity, omega), 'r')
print("8,3cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)

#11cm fit
popt, cov = curve_fit(gaussint, x45, P(a_45.values[1], 10))
maxintensity, omega = popt
plt.plot(x45, gaussint(x45, maxintensity, omega), 'b')
print("11cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)

#5,0cm fit
popt, cov = curve_fit(gaussint, x105, P(a_105.values[1], 10))
maxintensity, omega = popt
plt.plot(x105, gaussint(x105, maxintensity, omega), 'g')
print("5,0cm:\n", "I_0:", maxintensity, "Strahltaille:", omega)


#Muss noch y-Werte in Lichtleistungen umrechnen (und ylabel anpassen!)
#Fehlerrechnung
#Aufgaben Seite 14 und 15
#Fehler bei 8,3 cm: Wahrscheinlich nicht als ersten Wert die stelle gewählt, an der die Rasierklinge
#gerade noch so nicht in den strahl hineinragt, sondern schon früher gemessen (rasierklinge war noch lange nicht am strahl dran)
#Offset durch Hintergrundhelligkeit abziehen: wurde gemacht durch normalisierte spannung

