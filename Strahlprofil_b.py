# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 00:53:58 2022

@author: corin
"""

# Task: d bestimmen Sie aus dem Verlauf von w(z) den
#Waist w0 dieses Strahls mithilfe eines Fit-Programms. Dabei passen Sie die Funktion von w(z)
#nach Gl. (11) an die gemessenen Werte w1(z1), w2(z2),... an. Die Position des waist z0 ist dabei
#ein unbekannter Parameter, welcher gleichzeitig angepasst werden muss. Bestimmen Sie aus
#dem Waist w0 auch die Rayleigh-Länge zR

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from functools import partial

csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv"

b_10 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5])
b_9 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4])
b_11 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4])
b_6 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=12, nrows=2, usecols=[1,2,3,4,5])
b_3 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=15, nrows=2, usecols=[1,2,3,4,5,6])
b_14 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=18, nrows=2, usecols=[1,2,3,4,5,6]) #14,3cm
b_17 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=21, nrows=2, usecols=[1,2,3,4,5,6])
data = [b_10, b_9, b_11, b_6, b_3, b_14, b_17]
#data.remove(b_3)

Rd = 10
f = 100 #mm

maxints=[]
omegas=[]
zvals=[0,-1,1,-4,-7,4,7]
localwaists=[]

def P(U, R):
    return (U**2)/R

def localwaist(z, omega_0):
    rayleigh = np.pi*(omega_0**2)/(632.8*10**(-9))
    return omega_0*np.sqrt(1+(z**2)/(rayleigh**2))

#lokaler Strahlradius bestimmen
def gaussint(x, I0, w):
    inner = lambda xp: np.exp((-2*xp**2)/(w**2))
    #inteqrate.quad kann keine Integrationsgrenzen als Variablen haben, darum kompliziertere Lösung:
    integral = np.array(list(map(partial(integrate.quad, inner, b=np.inf), x)))[:,0]
    return I0*integral

for d in data:
    popt, cov = curve_fit(gaussint, d.values[0]-d.values[0][0] , P(d.values[1], 10))
    maxintensity, omega = popt
    maxints.append(maxintensity)
    omegas.append(omega)
    print("I_0:", maxintensity, "Strahltaille:", omega)

#nahe z=0
#plt.plot(b_10.values[0]-b_10.values[0][0], P(b_10.values[1], Rd), 'ro', label="(10,0+-0,2) cm")
#plt.plot(b_9.values[0]-b_9.values[0][0], P(b_9.values[1], Rd), 'bo', label="9,0+-0,2 cm")
#plt.plot(b_11.values[0]-b_11.values[0][0], P(b_11.values[1], Rd), 'go', label="11,0+-0,2 cm")
#plt.plot(b_10.values[0]-b_10.values[0][0], gaussint(b_10.values[0]-b_10.values[0][0], maxints[0], omegas[0]), 'r')
#plt.plot(b_9.values[0]-b_9.values[0][0], gaussint(b_9.values[0]-b_9.values[0][0], maxints[1], omegas[1]), 'b')
#plt.plot(b_11.values[0]-b_11.values[0][0], gaussint(b_11.values[0]-b_11.values[0][0], maxints[2], omegas[2]), 'g')
#plt.xlabel("x-x_0")
#plt.ylabel("Power in ...W")
#plt.legend("Distance lens (f=100mm) - razor blade") #also z-10cm
#plt.title("Cross section profile focused beam (near focal point)")
#plt.savefig()
#plt.clf()
#große z
#plt.plot(b_6.values[0]-b_6.values[0][0], P(b_6.values[1], Rd), 'yo', label="6,0+-0,2 cm")
plt.plot(b_3.values[0]-b_3.values[0][0], P(b_3.values[1], Rd), 'co', label="3,0+-0,2 cm")
#plt.plot(b_14.values[0]-b_14.values[0][0], P(b_14.values[1], Rd), 'mo', label="14,3+-0,2 cm")
#plt.plot(b_17.values[0]-b_17.values[0][0], P(b_17.values[1], Rd), 'ko', label="17,0+-0,2 cm")
#plt.plot(b_6.values[0]-b_6.values[0][0], gaussint(b_6.values[0]-b_6.values[0][0], maxints[3], omegas[3]), 'y')
plt.plot(b_3.values[0]-b_3.values[0][0], gaussint(b_3.values[0]-b_3.values[0][0], maxints[4], omegas[4]), 'c')
#plt.plot(b_14.values[0]-b_14.values[0][0], gaussint(b_14.values[0]-b_14.values[0][0], maxints[5], omegas[5]), 'm')
#plt.plot(b_17.values[0]-b_17.values[0][0], gaussint(b_17.values[0]-b_17.values[0][0], maxints[6], omegas[6]), 'k')
plt.xlabel("x-x_0")
plt.ylabel("Power in ...W")
plt.legend("Distance lens (f=100mm) - razor blade") #also z-10cm
plt.title("Cross section profile focused beam (far from focal point)")
#plt.savefig()
plt.clf()

#waist bestimmen
#Fehlerquelle: Mehr Messungen wären nötig
# b_3 liefert negativen waist ??? 
popt, cov = curve_fit(localwaist, zvals, omegas)
waist = popt
plt.plot(zvals, omegas, 'ro')
for i in zvals:
    localwaists.append(localwaist(i, waist))
plt.plot(zvals, localwaists, 'r')
print(waist)
print(localwaists)

