# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:05:53 2022

@author: corin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 00:53:58 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from functools import partial
import collections 

csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv"

b_10 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5])
b_9 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4])
b_11 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4])
b_6 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=12, nrows=2, usecols=[1,2,3,4,5])
b_3 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=15, nrows=2, usecols=[1,2,3,4,5,6])
b_14 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=18, nrows=2, usecols=[1,2,3,4,5,6]) #14,3cm
b_17 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=21, nrows=2, usecols=[1,2,3,4,5,6])
data = [b_3, b_6, b_9, b_10, b_11, b_14, b_17]

Rd = 10*10**3
#f = 100 #mm

lin = np.linspace(-0.8,0.8,100)
lin2 = np.linspace(-1.5, 1.5, 100)
maxints=[]
omegas= {}
localwaists=[]

def P(U, R):
    h = 6.62607015*10**(-34)
    c = 299792458
    wvl = 632.8*10**(-9)
    e = 1.602176634*10**(-19)
    return (h*c*U)/(wvl*R*e*0.75)

def localwaist(z, omega_0, rayleigh):
    #rayleigh = np.pi*(omega_0**2)/(632.8*10**(-9)
    return omega_0*np.sqrt(1+(z**2)/(rayleigh**2))

#lokaler Strahlradius bestimmen
def gaussint(x, I0, w):
    inner = lambda xp: np.exp((-2*xp**2)/(w**2))
    #inteqrate.quad kann keine Integrationsgrenzen als Variablen haben, darum kompliziertere Lösung:
    integral = np.array(list(map(partial(integrate.quad, inner, b=np.inf), x)))[:,0]
    return I0*integral

#zero-centering 
v1 = 5.7 #Verschiebung für rot
v2 = 6.2 #Verschiebung für blau
v3 = 2.3 # Verschiebung für grün
v4 = 5.7 #gelb
v5 = 14 #türkis
v6 = 14 #magenta
v7 = 10 #schwarz
    
#roter fit: 
popt, cov = curve_fit(gaussint, b_10.values[0]-v1 , P(b_10.values[1], Rd), bounds=(0,1))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[0] = omega
print("Rot: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin, gaussint(lin, maxintensity, omega), 'r')

#roter fit: 
popt, cov = curve_fit(gaussint, b_9.values[0]-v2 , P(b_9.values[1], Rd), bounds=(0,1))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[-1] = omega
print("Blau: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin, gaussint(lin, maxintensity, omega), 'b')

#grüner fit
popt, cov = curve_fit(gaussint, b_11.values[0]-v3 , P(b_11.values[1], Rd),bounds=(0,1))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[1] = omega
print("Grün: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin, gaussint(lin, maxintensity, omega), 'g')

#nahe z=0
plt.plot(b_10.values[0]-v1, P(b_10.values[1], Rd), 'ro', label="0,0 cm")
plt.plot(b_9.values[0]-v2, P(b_9.values[1], Rd), 'bo', label="-1,0 cm")
plt.plot(b_11.values[0]-v3, P(b_11.values[1], Rd), 'go', label="1,0 cm")
plt.legend()
plt.xlabel("x-x_0 in mm")
plt.ylabel("Power in mW") 
plt.title("Cross section profile focused beam (near focal point)")
plt.savefig("Cross section profile focused beam (near focal point).png", dpi=400)
plt.clf()

#gelber fit
popt, cov = curve_fit(gaussint, b_6.values[0]-v4 , P(b_6.values[1], Rd), bounds=(0,10))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[-4] = omega
print("Gelb: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin2, gaussint(lin2, maxintensity, omega), 'y')

#türkiser fit
popt, cov = curve_fit(gaussint, b_3.values[0]-v5 , P(b_3.values[1], Rd), bounds=(0,10))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[-7] = omega
print("türkis: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin2, gaussint(lin2, maxintensity, omega), 'c')

#magenta fit
popt, cov = curve_fit(gaussint, b_14.values[0]-v6 , P(b_14.values[1], Rd), bounds=(0,10))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[4.3] = omega
print("magenta: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin2, gaussint(lin2, maxintensity, omega), 'm')

#schwarzer fit
popt, cov = curve_fit(gaussint, b_17.values[0]-v7 , P(b_17.values[1], Rd), bounds=(0,10))
maxintensity, omega = popt
maxints.append(maxintensity)
omegas[7] = omega
print("schwarz: I_0:", maxintensity, "Strahltaille:", omega)
plt.plot(lin2, gaussint(lin2, maxintensity, omega), 'k')

plt.plot(b_6.values[0]-v4, P(b_6.values[1], Rd), 'yo', label="-4,0 cm")
plt.plot(b_3.values[0]-v5, P(b_3.values[1], Rd), 'co', label="-7,0 cm")
plt.plot(b_14.values[0]-v6, P(b_14.values[1], Rd), 'mo', label="4,3 cm")
plt.plot(b_17.values[0]-v7, P(b_17.values[1], Rd), 'ko', label="7,0 cm")
plt.legend()
plt.xlabel("x-x_0 (zero-centered values) in mm")
plt.ylabel("Power in W") 
plt.title("Cross section profile focused beam (far from focal point)")
plt.savefig("Cross section profile focused beam (far from focal point).png", dpi=400)
plt.clf()

##waist bestimmen
z = sorted(omegas)
o = [omegas[i] for i in z]
popt, err = curve_fit(localwaist, z, o, absolute_sigma="True") #fitted localwaist an die z-Werte zusammen mit den dazugehörigen omegas
waist, zR = popt
plt.plot(z, o, 'ro', label="data")
#localwaist(z, omega_0, rayleigh)
for i in z:
    localwaists.append(localwaist(i, waist, zR)) 
#plt.plot(z, localwaist(z, o)) 
plt.plot(z, localwaists, 'b', label = "fit")
plt.vlines(0, 0, 1.7, 'y', '--', label="focal position")
plt.xlabel("z in cm")
plt.ylabel("omega(z) in mm")
plt.legend()
title = "beam waist against razor position from focal point"
plt.title(title)
plt.savefig("beam waist against razor position from focal point.png", dpi=400)
print("waist: (", waist, "+-", np.sqrt(err[0,0]), ") mm")
print("rayleigh length: (", zR, "+-", np.sqrt(err[1,1]), ") mm") 