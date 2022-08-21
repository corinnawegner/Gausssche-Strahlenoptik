# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:26:20 2022

@author: corin
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import scipy.integrate as integrate
from functools import partial

def gaussint(x, I0, w):
    inner = lambda xp: np.exp((-2*xp**2)/(w**2))
    #inteqrate.quad kann keine Integrationsgrenzen als Variablen haben, darum kompliziertere Lösung:
    integral = np.array(list(map(partial(integrate.quad, inner, b=np.inf), x)))[:,0]
    return I0*integral

x= np.linspace(-10,10,100)
plt.plot(x, gaussint(x-3, 0.3, 3))