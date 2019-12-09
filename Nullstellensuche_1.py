#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:38:05 2019

@author: marceldann
"""
from sympy import *
import math
import matplotlib.pyplot as plt
x = symbols('x')

def Newton(Funktion, x0, epsi):
    x = symbols('x')
    xi = x0
    iteration = xi
    Ableitung = diff(Funktion,x)
    Funktion1 = Funktion.subs(x, xi)
    Ableitung1 = Ableitung.subs(x, xi)
    Schritte = []
    Gegenwert = []
    it = True
    
    while it == True:
        xi = iteration
        Funktion1 = Funktion.subs(x, xi)
        Ableitung1 = Ableitung.subs(x, xi)
        iteration = xi - (Funktion1/Ableitung1)
        Schritte.append(iteration)
        if len(Gegenwert) < len(Schritte):
            Gegenwert.append(log(2))
        plt.plot(Schritte)
        plt.plot(Gegenwert)
        #print(iteration)
        if abs(iteration - xi) < epsi:
            it = False
    
    return iteration, Schritte, Gegenwert
    
def zentrDif(Funktion, x0, epsi):
    x = symbols('x')
    xi = x0
    iteration1 = xi
    h = 0.00000000000001
    Funktion2 = Funktion.subs(x, x0+(h/2))
    Funktion3 = Funktion.subs(x, x0-(h/2))
    Ableitung = ((Funktion2-Funktion3)/h)
    Ableitung1 = Ableitung.subs(x, xi)
    Schritte = []
    Gegenwert = []
    it = True
    
    while it == True:
        xi = iteration1
        Funktion1 = Funktion.subs(x, xi)
        Ableitung1 = Ableitung.subs(x, xi)
        iteration1 = xi - (Funktion1/Ableitung1)
        Schritte.append(iteration1)
        if len(Gegenwert) < len(Schritte):
            Gegenwert.append(log(2))
        plt.plot(Schritte)
        plt.plot(Gegenwert)
        #print(iteration1)
        if abs(iteration1 - xi) < epsi:
            it = False
    
    return iteration1, Schritte, Gegenwert

def Bisektion(Funktion, a, b, epsi):
    x = symbols('x')
    m = (a+b)/2
    Funktion4 = Funktion.subs(x, m)
    Schritte = []
    Gegenwert = []
    run = True
    
    while run == True:
        Funktion4 = Funktion.subs(x, m)
        Schritte.append(m)
        if len(Gegenwert) < len(Schritte):
            Gegenwert.append(log(2))
        plt.plot(Schritte)
        plt.plot(Gegenwert)
        #print(m)
        if abs(a-m) < epsi:
            run = False
        if Funktion4 < 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    
    return m, Schritte, Gegenwert
                
print("Newtonverfahren mit analytisch exakter Ableitung:", Newton((1/3)*x**3-2*x+1,-2,10**-6)[0])
plt.figure(1)
plt.subplot(2,2,1)
plt.plot(Newton(math.e**x - 2, 1, 10**-6) [1],label = 'Iterationsschritte')
plt.plot(Newton(math.e**x - 2, 1, 10**-6) [2],label = 'ln(2)')
plt.yscale('log')
plt.xscale('log')
plt.title('Newtonverfahren mit analytisch exakter Ableitung')
plt.legend()
#print("Newtonverfahren mit einer über zentrale Differenzen approximierten Ableitung:", zentrDif(math.e**x -2,3,10**-6)[0])
plt.figure(1)
plt.subplot(2,2,2)
plt.plot(zentrDif(math.e**x - 2, 1, 10**-6) [1],label = 'Iterationsschritte')
plt.plot(zentrDif(math.e**x - 2, 1, 10**-6) [2],label = 'ln(2)')
plt.yscale('log')
plt.xscale('log')
plt.title('Zentrale Differenzen approximierten Ableitung')
plt.legend()
#print("Ansatz über Bisektion:", Bisektion(math.e**x - 2, 0, 6, 10**-6)[0])
plt.figure(1)
plt.subplot(2,2,3)
plt.plot(Bisektion(math.e**x - 2, 0, 6, 10**-6) [1],label = 'Iterationsschritte')
plt.plot(Bisektion(math.e**x - 2, 0, 6, 10**-6) [2],label = 'ln(2)')
plt.yscale('log')
plt.xscale('log')
plt.title('Ansatz über Bisektion')
plt.legend()
#plt.show()






























