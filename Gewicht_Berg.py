#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:42:05 2019

@author: marceldann
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:14:50 2019

@author: marceldann
"""

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy import integrate
import math
#import pdb; pdb.set_trace()

fig = plt.figure()
ax = plt.axes(projection='3d')

X_Data = open("Zollernberg.X_data.txt")
Y_Data = open("Zollernberg.Y_data.txt")
H_Data = open("Zollernberg.H_data.txt")
x_data = X_Data.readline().split()
y_data = Y_Data.readline().split()
h_data = H_Data.readline().split()
    
new_x_data = []
new_y_data = []
new_h_data = []

new_x_data = [float(i) for i in x_data]
new_y_data = [float(i) for i in y_data]
new_h_data = [float(i) for i in h_data]

i = 0
x_data_interp = []
y_data_interp = []
h_data_interp = []

while i < len(new_h_data): # um x,y,h - Daten über 650m zu bekommen
    if new_h_data[i] > 650.0:
        h_data_interp.append(new_h_data[i])
        x_data_interp.append(new_x_data[i])
        y_data_interp.append(new_y_data[i])    
    i = i+1
    
h_data_interp_new = []
r = 0

while r < len(h_data_interp)-1: # Neues Array für h_Daten - 650m rechnen, damit der "neue" Berg bei h=0 "anfängt"
    x = h_data_interp[r]-650.0
    h_data_interp_new.append(x)
    r += 1
    
hx = 108/6 #Breitengrad sind 74,2km; Abstand zwischen geg. x-Werten mit Zwischenschritt (1 Breitengrad überspringen) sind 108m
hy = 42/6 #Längengrad sind 111,3km; Abstand zwischen geg. y-Werten mit Zwischenschritt (1 Längengrad überspringen) sind 42m
d = hx * hy
Mitte1,Mitte2,Mitte7,Mitte8 = 0,0,0,0
Liste,Liste2,Liste3=[],[],[]
l = 0
s = 1
m = 0
count = 1
Volumen_2,Volumen_3 = 0,0

myset = set(x_data_interp) #Gibt mir nur die unterschiedlichen Zahlen aus
Verschiedene_X_Werte = list(myset) #formt daraus wieder eine Liste
Verschiedene_X_Werte.sort()

while m < len(Verschiedene_X_Werte):
    while count == 1:         
        while x_data_interp[l] == Verschiedene_X_Werte[m]:
            Xm = h_data_interp_new[s]
            Mitte1 += 4*Xm  
            Xm_2 = h_data_interp_new[s+1]
            Mitte2 += 2*Xm_2
            Liste.append(l)         
            l += 1
            s += 2
        count += 1
        m += 1    
        Volumen_1 = (h_data_interp_new[0]+Mitte1+Mitte2+h_data_interp_new[Liste[-1]])

    while count%2 == 0 and count != len(Verschiedene_X_Werte):
        Liste1 = []   
        Mitte3,Mitte4 = 0,0
        while x_data_interp[l] == Verschiedene_X_Werte[m]:
            if s <= len(h_data_interp_new)-1:
                Xm_3 = h_data_interp_new[s]
                Mitte3 += 16*Xm_3  
            if s <= len(h_data_interp_new)-2:
                Xm_4 = h_data_interp_new[s+1]
                Mitte4 += 8*Xm_4
            Liste1.append(l)
            l += 1
            s += 2
        count += 1
        m += 1
        Volumen_2 += (4*h_data_interp_new[Liste1[0]]+Mitte3+Mitte4+4*h_data_interp_new[Liste1[-1]])
       
    while count%2 != 0 and count != len(Verschiedene_X_Werte):
        Liste2 = [] 
        Mitte5,Mitte6 = 0,0
        while x_data_interp[l] == Verschiedene_X_Werte[m]:
            if s <= len(h_data_interp_new)-1:
                Xm_5 = h_data_interp_new[s]
                Mitte5 += 8*Xm_5  
            if s <= len(h_data_interp_new)-2:
                Xm_6 = h_data_interp_new[s+1]
                Mitte6 += 4*Xm_6
            Liste2.append(l)
            l += 1
            s += 2
        count += 1
        m += 1
        Volumen_3 += (2*h_data_interp_new[Liste2[0]]+Mitte5+Mitte6+2*h_data_interp_new[Liste2[-1]])
    
    while count == len(Verschiedene_X_Werte):
        Liste3 = [] 
        while x_data_interp[l] == Verschiedene_X_Werte[m] and l< len(h_data_interp_new):
            if s <= len(h_data_interp_new)-1:
                Xm_7 = h_data_interp_new[s]
                Mitte7 += 4*Xm_7 
            if s <= len(h_data_interp_new)-2:
                Xm_8 = h_data_interp_new[s+1]
                Mitte8 += 2*Xm_8
            Liste3.append(l)
            l += 1
            s += 2
        count += 1
        m += 1
        Volumen_4 = (h_data_interp_new[Liste3[0]]+Mitte7+Mitte8+h_data_interp_new[Liste3[-1]])

Volumen = d*(Volumen_1 + Volumen_2 + Volumen_3 + Volumen_4)/(10**9)#dadurch in km^3
Richtige_Einheit = Volumen * 10**15 *10**-6 # zuerst in cm^-3, danach in Tonnen
Gewicht = 2.8 * Richtige_Einheit
    
ax.plot_trisurf(x_data_interp, y_data_interp, h_data_interp, cmap='viridis', edgecolor='none')
axes = plt.gca()
axes.set_xlim([8.95,8.98])
axes.set_ylim([48.3,48.336])
axes.set_zlim([566.837,839.33])
print(Volumen,Gewicht)