# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:27:53 2022

@author: corin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

csv_path_a = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_a.csv"
csv_path_b = r"C:/Users/corin/Gausssche-Strahlenoptik/Strahlprofil_b.csv" # Vielleicht Teil b in eigenen Code auslagern 

a_72 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=3, nrows=2, usecols=[1,2,3,4,5,6,7,8]) #Daten für 7,2 cm
a_45 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=6, nrows=2, usecols=[1,2,3,4,5,6,7,8]) 
a_105 = pd.read_csv(csv_path_a, delimiter=";", header=None, skiprows=9, nrows=2, usecols=[1,2,3,4,5,6])
data_a = [a_45, a_72, a_105]

distLS = 15.5 #Distance lense-fibre end (Source of laser beam)

plt.plot(a_72.values[0]-a_72.values[0][0], a_72.values[1], 'ro', label="8,3cm")
plt.plot(a_45.values[0]-a_45.values[0][0], a_45.values[1], 'bo', label="11,0 cm")
plt.plot(a_105.values[0]-a_105.values[0][0], a_105.values[1],'go', label="5,0 cm")
plt.xlabel("normalized micrometer position")
plt.ylabel("voltage in mV")
plt.legend(title="Distance razor blade - fibre end")
#Muss noch y-Werte in Lichtleistungen umrechnen (und ylabel anpassen!)
#Fehler?
#Aufgaben Seite 14 und 15
#Fehler bei 8,3 cm: Wahrscheinlich nicht als ersten Wert die stelle gewählt, an der die Rasierklinge
#gerade noch so nicht in den strahl hineinragt, sondern schon früher gemessen (rasierklinge war noch lange nicht am strahl dran)

# def lichtleistung(U):
