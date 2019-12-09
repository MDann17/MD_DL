#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 11:03:11 2019

@author: marceldann
"""

from sympy import *
#import math
import matplotlib.pyplot as plt
#from scipy import interpolate
import numpy as np
x = symbols('x')

def Interpolation(Funktion, x0, epsi):
    #x = symbols('x')
    
    x0 = np.arange(-10,10,(20/101))
    #y = [(1/3)*x**3-2*x+1 for x in x0]
    y = (1/3)*x0**3-2*x0+1
    plt.plot(x0, y, 'bo')
    i = 0
    while i < 100:
        Funktion1 = Funktion.subs(x, x0[i])
        Funktion2 = Funktion.subs(x, x0[i+1])
        #print(Funktion1, Funktion2)
        if Funktion1 < 0 and Funktion2 > 0 or Funktion1 > 0 and Funktion2 < 0:
            i += 1
            x1 = (-(Funktion1) / ((Funktion2 - Funktion1)/(x0[i+1]-x0[i]))) + x0[i]
            #x1 = interpolate.interp1d(t[i], Funktion3,kind='zero')
            #print(x0[i],x0[i+1],Funktion1,Funktion2)
            print(x1)
            #plt.plot(x1, 0, 'o')
            plt.plot(x1, 0, 'ro')
            plt.axvline(x1,color='r', linestyle= '--')

        i += 1
    #f = interpolate.interp1d(x0, u)
    #plt.plot(x0, y, 'o',color = 'b')
    #plt.plot(x1, 0, 'o')
    #plt.axvline(x1,color='r', linestyle= '--')


    return x0,y, x1, Funktion1

#plt.plot(Interpolation((1/3)*x**3-2*x+1,4,10**-6)[0][1])
#plt.plot(Interpolation((1/3)*x**3-2*x+1,4,10**-6)[2])

print(Interpolation((1/3)*x**3-2*x+1,4,10**-6)[0])

