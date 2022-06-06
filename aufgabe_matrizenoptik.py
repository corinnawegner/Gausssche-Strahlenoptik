# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 11:07:40 2022

@author: corin
"""

import numpy as np

w0 = 10**(-3)
wl = 632.8*10**(-9) #wavelength
w0p = 5*10**(-6)
f1 = 50*10**(-3)
f2 = 100*10**(-3)

z_R = (np.pi*w0**2)/wl
z_Rp = (np.pi*w0p**2)/wl

L = f1 - (f1*f2**2)/z_R*z_R**2
print(L)