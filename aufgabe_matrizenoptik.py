# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:07:40 2022

@author: corin
"""

import numpy as np
from scipy.optimize import fsolve

w0 = 10**(-3)
wl = 632.8*10**(-9) #wavelength
w0p = 5*10**(-6)
f1 = 50*10**(-3)
f2 = 100*10**(-3)

z_R = (np.pi*w0**2)/wl
z_Rp = (np.pi*w0p**2)/wl


def f(x): #fehlt noch was
    C = x/(f1*f2) - (1/f1) - (1/f2)
    D = 1 - x/f2
    f = (z_R / ((D**2)+(z_R**2)*C**2)) - z_Rp
    return f

Lnegative = fsolve(f, 0.01) #0.01 als Schätzwert, von da aus wird bis zur nächsten Nullstelle iteriert
L = fsolve(f, 0.5)
print(Lnegative, L)