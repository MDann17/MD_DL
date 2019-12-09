#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:10:11 2019

@author: marceldann
"""
import random
import scipy.integrate as integrate
#import matplotlib.pyplot as plt
from sympy import symbols, exp
x = symbols('x')

result = integrate.quad(lambda x: exp(x), -1, 1)
print("Exakter Wert:",result)

def MonteCarlo(Funktion, UGrenze, OGrenze,N):
    yO = 2.718281828459045235360287 + 0.1
    yU = 0.36787944117144232159 - 0.1 
    X = []
    Y = []
    for xi in range(N):
        xi = float(random.uniform(-1,1))
        xi = round(xi,3)
        X.append(xi)
    
    for y in range(N):
        y = float(random.uniform(yU,yO))
        y = round(y,3)
        Y.append(y)
    
    YKleiner = []    
    z = 0
    
    while z < N:
        if Y[z] < Funktion.subs(x,X[z]):
            YKleiner.append(Y[z])
            z += 1
        else:
            z += 1

    
    n = len(YKleiner)
    Integral = (n/N)*abs((yO - yU)*(UGrenze - OGrenze))
    Integral = round(Integral,3)
    
    return Integral

print(MonteCarlo(exp(x),-1,1,10000))   