#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 11:35:04 2019

@author: marceldann
"""

from sympy import symbols
x = symbols('x')

def Trapez(Funktion, Schrittweite, OGrenze, UGrenze):
    n = Schrittweite
    Bereich = OGrenze - UGrenze
    h = Bereich/n
    X = []
    i = 0
    z = 1
    Mitte = 0
    X.append(UGrenze)

    while X[i] < OGrenze:
        i = i+1
        XNeu = X[i-1] + h
        X.append(XNeu)
        
    while z < n-1:    
        Mitte += 2*Funktion.subs(x,X[z])
        z += 1
        
    Fa = (h/2)*((Funktion.subs(x, UGrenze)+Mitte+Funktion.subs(x,OGrenze)))

    return Fa

print(Trapez(1/(x**2+1),1000,5,-5))