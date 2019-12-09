#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:03:16 2019

@author: marceldann
"""

from sympy import *
import math
import matplotlib.pyplot as plt


def Newton(Funktion, x0, epsi):
    x = symbols('x')
    #while x0 < 10:
    xi = x0
    iteration = xi
    Ableitung = diff(Funktion,x)
    Funktion1 = Funktion.subs(x, xi)
    Ableitung1 = Ableitung.subs(x, xi)
    it = True
    while it == True:
        xi = iteration
        Funktion1 = Funktion.subs(x, xi)
        Ableitung1 = Ableitung.subs(x, xi)
        iteration = xi - (Funktion1/Ableitung1)
        #print(iteration)
        if abs(iteration - xi) < epsi:
            it = False

        #x0 + 0.5
        #if x0 == 0:
         #   x0 = 0.5
    t = range(-10,10)
    u = [x**2-2 for x in t]
    #plt.plot(t,u)
    #plt.grid(True)

    return float(iteration)

print("x0 = -0.1; Newtonverfahren mit analytisch exakter Ableitung:", Newton(x**2-2,-0.1,10**-6))
print("x0 = 0.1; Newtonverfahren mit analytisch exakter Ableitung:", Newton(x**2-2,0.1,10**-6))
#plt.scatter(-0.1,0)
#plt.scatter(0.1,0)

def Newton(Funktion, x0, epsi):
    x = symbols('x')
    xi = x0
    iteration = xi
    Ableitung = diff(Funktion,x)
    Funktion1 = Funktion.subs(x, xi)
    Ableitung1 = Ableitung.subs(x, xi)
    it = True
    
    while it == True:
        xi = iteration
        Funktion1 = Funktion.subs(x, xi)
        Ableitung1 = Ableitung.subs(x, xi)
        iteration = xi - (Funktion1/Ableitung1)
        #print(iteration)
        if abs(iteration - xi) < epsi:
            it = False
    
    t1 = range(-4,4)
    u1 = [x**3-4*x-1 for x in t1]
    #plt.plot(t1,u1)
    #plt.grid(True)
    
    return float(iteration),x0

print("x0 = -1; Newtonverfahren mit analytisch exakter Ableitung:", Newton(x**3-4*x-1,-1,10**-6))
print("x0 = -0.9; Newtonverfahren mit analytisch exakter Ableitung:", Newton(x**3-4*x-1,-0.9,10**-6))
print(" x0 = 1.2; Newtonverfahren mit analytisch exakter Ableitung:", Newton(x**3-4*x-1,1.2,10**-6))
#plt.scatter(-1,0)
#plt.scatter(-0.9,0)
#plt.scatter(1.2,0)

def Newton(Funktion, x0, epsi):
    x = symbols('x')
    xi = x0
    iteration = xi
    Ableitung = diff(Funktion,x)
    Funktion1 = Funktion.subs(x, xi)
    Ableitung1 = Ableitung.subs(x, xi)
    it = True
    
    while it == True:
        xi = iteration
        Funktion1 = Funktion.subs(x, xi)
        Ableitung1 = Ableitung.subs(x, xi)
        iteration = xi - (Funktion1/Ableitung1)
        #print(iteration)
        if abs(iteration - xi) < epsi:
            it = False
    
    t2 = range(-8,8)
    u2 = [sin(x) for x in t2]
    #plt.plot(t2,u2)
    #plt.grid(True)
    
    return float(iteration)

print("x0 = -2; Newtonverfahren mit analytisch exakter Ableitung:", Newton(sin(x),-2,10**-6))
print("x0 = 2; Newtonverfahren mit analytisch exakter Ableitung:", Newton(sin(x),2,10**-6))
print("x0 = 3.5; Newtonverfahren mit analytisch exakter Ableitung:", Newton(sin(x),3.5,10**-6))
print("x0 = -3.5; Newtonverfahren mit analytisch exakter Ableitung:", Newton(sin(x),-3.5,10**-6))
#plt.scatter(-2,0)
#plt.scatter(2,0)
#plt.scatter(3.5,0)
#plt.scatter(-3.5,0)























