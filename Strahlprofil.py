# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:27:53 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

csv_path_a = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_a.csv"
csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv"

a_72 = pd.read_csv(csv_path_a, delimiter=";", skiprows=3, nrows=1, usecols=[1,2,3,4,5,6,7,8]) #Daten für 7,2 cm
a_45 = pd.read_csv(csv_path_a, delimiter=";", skiprows=6, nrows=1, usecols=[1,2,3,4,5,6,7,8]) 
a_105 = pd.read_csv(csv_path_a, delimiter=";", skiprows=9, nrows=1, usecols=[1,2,3,4,5,6])
# Vielleicht Teil b in eigenen Code auslagern 
#data_b = pd.read_csv(csv_path_b, delimiter=";") 
