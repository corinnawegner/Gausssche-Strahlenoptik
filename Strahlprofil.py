# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:27:53 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_path_a = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_a.csv"
csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv" # Vielleicht Teil b in eigenen Code auslagern 

a_72 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5,6,7,8]) #Daten für 7,2 cm
a_45 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4,5,6,7,8]) 
a_105 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4,5,6])
data_a = [a_45, a_72, a_105]

print(a_72.values[0])
plt.plot(a_72.values[0], a_72.values[1], 'ro', label="7,2cm")
# muss noch machen, dass erste column die x-Achse und die zweite die y-Achse ist

# def lichtleistung(U):
