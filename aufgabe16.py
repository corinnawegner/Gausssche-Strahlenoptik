# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:41:57 2022

@author: corin
"""

import numpy as np

def omegasq(wvl, L, R):
    return (wvl*np.pi* np.sqrt((L/2)*(R-(L/2))))

wvl=632*10**(-9)
L = 0.045 #45mm
R = 0.05 #50mm

print("Omega^2 = ", omegasq(wvl, L, R))

def rayleigh(w):
    return (np.pi*w**2)/wvl

print("rayleigh = ", rayleigh(omegasq(wvl, L, R)))