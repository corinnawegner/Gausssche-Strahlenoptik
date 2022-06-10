# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 00:53:58 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv"

b_10 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5])
b_9 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4])
b_11 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4])
b_6 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=12, nrows=2, usecols=[1,2,3,4,5])
b_3 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=15, nrows=2, usecols=[1,2,3,4,5,6])
b_14 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=18, nrows=2, usecols=[1,2,3,4,5,6]) #14,3cm
b_17 = pd.read_csv(csv_path_b, delimiter=";", header=None, skiprows=21, nrows=2, usecols=[1,2,3,4,5,6])

plt.plot(b_10.values[0]-b_10.values[0][0], b_10.values[1], 'ro', label="10,0 cm")
plt.plot(b_9.values[0]-b_9.values[0][0], b_9.values[1], 'bo', label="9,0 cm")
plt.plot(b_11.values[0]-b_11.values[0][0], b_11.values[1], 'go', label="11,0 cm")
plt.plot(b_6.values[0]-b_6.values[0][0], b_6.values[1], 'yo', label="6,0 cm")
plt.plot(b_3.values[0]-b_3.values[0][0], b_3.values[1], 'co', label="3,0 cm")
plt.plot(b_14.values[0]-b_14.values[0][0], b_14.values[1], 'mo', label="14,0 cm")
plt.plot(b_17.values[0]-b_17.values[0][0], b_17.values[1], 'ko', label="17,0 cm")

# Zur Übersichtlichkeit: near focal point in extra plot?
