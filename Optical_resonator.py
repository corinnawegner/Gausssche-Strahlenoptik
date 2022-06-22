# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:41:36 2022

@author: corin
"""
import numpy as np
 
#check if T+R=1, wie kann man die Reflektivität unabhängig von T messen?
# Welchen Strahlparameter 
# w0 der Gaußschen Moden erwarten Sie für das Lichtfeld im Resonator?
# Zunächst: Was erwarten Sie für eine Transmissionsfunktion für einen Resonator, 
# der aus Planspiegeln aufgebaut wird und auf den eine monochromatische Lichtwelle
# trifft? Wie erklären Sie sich das Auftreten von mehr als einem Transmissionsmaximum 
# bei dem gerade aufgebauten Resonator?
# In einer Periode sollten jetzt nur noch zwei
# beinahe identische Transmissionsmaxima sichtbar sein. Warum? Drucken
# Sie das Oszilloskopbild aus. Schätzen Sie das Verhältnis des freien 
# Spektralbereichs zur Linienbreite ab, welche Finesse ergibt sich auf diese Weise?

Rd = 100*10**(4) # Widerstand der Diode (bessere Messung)
U_b = 29*10**(-3) # Spannung mit beiden Spiegeln
U_1 = 55*10**(-3) # Spannung mit vorderem Spiegel
U_2 = 46*10**(-3) # Spannung mit hinterem Spiegel
U_o = 472*10**(-3) # Spannung ohne Spiegel
dU = 0.1*10**(-3) # Fehler der Spannungen

def Transmission(Uin, Uout, delta_U):
    error = np.sqrt(((2*Uout*delta_U/(Uin**2))**2)+((2*(Uout**2)*delta_U/(Uin**3))**2))
    return (Uout/Uin)**2, error

def Total_Transmission_from_Single_Ts(T1, T2, err1, err2):
    Ttot = np.sqrt(T1*T2)
    error = np.sqrt(((T1*err2/2*np.sqrt(T1*T2))**2)+((T2*err1/2*np.sqrt(T1*T2))**2))
    return Ttot, error

def Reflectivity(t):
    return 1-t #Der Fehler ist gleich der Fehler von T

def Finesse(R):
    return np.pi*np.sqrt(R)/(1-R)

def Finesse_from_figure(FSR, FWHM, err):
    error = np.sqrt(((err*FWHM**(-2))**2)+((err*FSR/(FWHM**2))**2))
    return FSR/FWHM, error

T = Transmission(U_o, U_b, dU)
T1 = Transmission(U_o, U_1, dU)
T2 = Transmission(U_o, U_2, dU)
Tp = Total_Transmission_from_Single_Ts(T1[0], T2[0], T1[1], T2[1])

#Transmission der Spiegel bestimmen:
print("Transmissivity:")
print("Total Transmission: T=", T[0], "+-", T[1])
print("Transmission of first mirror: T1=", T1[0], "+-", T[1])
print("Transmission of second mirror: T2=", T2[0], "+-", T[1])
print("Calculated total Transmission from T1 an T2: Tp =", Tp[0], "+-", T[1])
#Unterschied von T und Tp: Absorption der Spiegel? Muss man diskutieren 

#Erwartete Reflektivität und Finesse:
print("Reflectivity:")
print("Expected Reflectivity (if T+R=1): R= ", Reflectivity(T[0]), "+-", T[1])
print("Expected Reflectivity (if T+R=1): Rp= ", Reflectivity(Tp[0]), "+-", Tp[1])
print("Expected Reflectivity (if T+R=1): R1= ", Reflectivity(T1[0]), "+-", T1[1])
print("Expected Reflectivity (if T+R=1): R2= ", Reflectivity(T2[0]), "+-", T2[1])

#Finesse
print("Finesse:")
print("Finesse from total R: F=", Finesse(Reflectivity(T[0])))
print("Finesse from Rp: Fp =", Finesse(Reflectivity(Tp[0])))
print("Finesse from figure: Ffig = ", Finesse_from_figure(10, 3, 1)[0], "+-", Finesse_from_figure(10, 3, 1)[1])

#print(Total_Transmission_from_Single_Ts(Reflectivity(T1[0]), Reflectivity(T2[0]), T1[1], T2[1]))
