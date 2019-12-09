#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:35:04 2019

@author: marceldann
"""

from sympy import symbols
x = symbols('x')
import scipy.integrate as integrate
import matplotlib.pyplot as plt

result = integrate.quad(lambda x: 1/(x**2+1), -5, 5)
print("Exakter Wert:",result)

def Trapez(Funktion, Schrittweite, OGrenze, UGrenze):
    n = Schrittweite
    Faplot = []
    Bereich = OGrenze - UGrenze
    h = Bereich/n
    X = []
    i = 0
    z = 1
    Mitte = 0
    X.append(UGrenze)
    Fa = 0

    while X[i] < OGrenze:
        i = i+1
        XNeu = X[i-1] + h
        X.append(XNeu)
        
    while z < n-1:    
        Mitte += 2*Funktion.subs(x,X[z])
        z += 1
        
    Fa = (h/2)*((Funktion.subs(x, UGrenze)+Mitte+Funktion.subs(x,OGrenze)))
    
    Error = Fa-result[0]
    Faplot.append(abs(Error))

    return Fa,Error

print("Trapez:",Trapez(1/(x**2+1),50,5,-5))

def Simpson(Funktion, Schrittweite, OGrenze, UGrenze):
    #import pdb; pdb.set_trace() #Debug Funktion
    n = Schrittweite
    FaSplot = []
    Bereich = OGrenze - UGrenze
    h = Bereich/n
    X = []
    i = 0
    j = 0
    z = 1
    Mitte1 = 0
    Mitte2 = 0
    X.append(UGrenze)

    while X[i] < OGrenze:
        i = i+1
        XNeu = X[i-1] + h
        X.append(XNeu)
    
    while j <= n-1:    #Mitte berechnen mit *4
        Xm = (X[j]+X[j+1])/2
        Mitte1 += 4*Funktion.subs(x,Xm)    
        j += 1
    
    while z <= n-1:    #Mitte berechnen mit *2
        Mitte2 += 2*Funktion.subs(x,X[z])
        z += 1
        
    FaS = (h/6)*((Funktion.subs(x,UGrenze)+Mitte1+Mitte2+Funktion.subs(x,OGrenze)))    
    
    Error = FaS-result[0]
    FaSplot.append(abs(Error))

    return FaS,Error

print("Simpson:",Simpson(1/(x**2+1),50,5,-5))
#plt.plot(Simpson(1/(x**2+1),1,5,-5),'r',label='Simpson')
#plt.plot(Trapez(1/(x**2+1),1,5,-5),'g',label='Trapez')
#plt.axis([-1, 15, -2, 5])
#plt.legend()

def DreiAchtel(Funktion, Schrittweite, OGrenze, UGrenze):
    #import pdb; pdb.set_trace() #Debug Funktion
    n = Schrittweite
    Fa38plot = []
    XM1 =[]
    XM2=[]
    Bereich = OGrenze - UGrenze
    h = Bereich/n
    X = []
    i = 0
    j = 0
    z = 1
    Mitte1 = 0
    Mitte2 = 0
    Mitte3 = 0
    X.append(UGrenze)

    while X[i] < OGrenze:
        i = i+1
        XNeu = X[i-1] + h
        X.append(XNeu)
    
    while j <= n-1:    #Mitte berechnen mit *4
        Zw = (X[j+1]-X[j])/3
        Xm1 = X[j]+Zw
        Xm2 = X[j]+2*Zw
        Mitte1 += 3*Funktion.subs(x,Xm1)  
        Mitte2 += 3*Funktion.subs(x,Xm2)  
        XM1.append(Xm1)
        XM2.append(Xm2)
        j += 1
    
    while z <= n-1:    #Mitte berechnen mit *2
        Mitte3 += 2*Funktion.subs(x,X[z])
        z += 1
        
    Fa38 = (h/8)*((Funktion.subs(x,UGrenze)+Mitte1+Mitte2+Mitte3+Funktion.subs(x,OGrenze)))    
    
    Error = Fa38-result[0]
    Fa38plot.append(abs(Error))

    return Fa38,Error

print("3/8:",DreiAchtel(1/(x**2+1),50,5,-5))


def Milne(Funktion, Schrittweite, OGrenze, UGrenze):
    #import pdb; pdb.set_trace() #Debug Funktion
    n = Schrittweite
    FaMplot = []
    Bereich = OGrenze - UGrenze
    h = Bereich/n
    X = []
    i = 0
    j = 0
    z = 1
    Mitte1 = 0
    Mitte2 = 0
    Mitte3 = 0
    Mitte4 = 0
    X.append(UGrenze)

    while X[i] < OGrenze:
        i = i+1
        XNeu = X[i-1] + h
        X.append(XNeu)
    
    while j <= n-1:    #Mitte berechnen mit *4
        Zw = (X[j+1]-X[j])/4
        Xm1 = X[j]+Zw
        Xm2 = X[j]+2*Zw
        Xm3 = X[j]+3*Zw
        Mitte1 += 32*Funktion.subs(x,Xm1)  
        Mitte2 += 12*Funktion.subs(x,Xm2)
        Mitte3 += 32*Funktion.subs(x,Xm3)
        j += 1
    
    while z <= n-1:    #Mitte berechnen mit *2
        Mitte4 += 14*Funktion.subs(x,X[z])
        z += 1
        
    FaM = (h/90)*((7*Funktion.subs(x,UGrenze)+Mitte1+Mitte2+Mitte3+Mitte4+7*Funktion.subs(x,OGrenze)))    
    
    Error = FaM-result[0]
    FaMplot.append(abs(Error))

    return FaM,Error

print("Milne:",Milne(1/(x**2+1),50,5,-5))















