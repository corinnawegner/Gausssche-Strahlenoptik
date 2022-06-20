# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:41:36 2022

@author: corin
"""

# Bestimmen Sie zuerst die Transmission der Spiegel für die vorhandene Wellenlänge. Welche
#Reflektivität R und Finesse F sind zu erwarten
# Welcher Resonatorkonfiguration entspricht diese Anordnung? Welchen Strahlparameter w0 der Gaußschen Moden erwarten
# Sie für das Lichtfeld im Resonator?
# Wie groß sollte der Abstand der Linse vom Einkoppelspiegel sein?
#Zunächst: Was erwarten Sie für eine Transmissionsfunktion für einen Resonator, der aus Planspiegeln aufgebaut wird und auf den eine monochromatische Lichtwelle trifft? Wie erklären
#Sie sich das Auftreten von mehr als einem Transmissionsmaximum bei dem gerade aufgebauten Resonator?
#In einer Periode sollten jetzt nur noch zwei
#beinahe identische Transmissionsmaxima sichtbar sein. Warum? Drucken Sie das Oszilloskopbild aus. Schätzen Sie das Verhältnis des freien Spektralbereichs zur Linienbreite ab, welche
#Finesse ergibt sich auf diese Weise?

Rd = 100*10**(4) # Widerstand der Diode (bessere Messung)
U_b = 29*10**(-3) #V (+-1mV) Spannung mit beiden Spiegeln
U_1 = 55*10**(-3) # Spannung mit vorderem Spiegel
U_2 = 46*10**(-3) # Spannung mit hinterem Spiegel
U_o = 472*10**(-3) #Spannung ohne Spiegel

 
