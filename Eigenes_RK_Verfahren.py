#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:52:13 2019

@author: marceldann
"""

from sympy import symbols
import sympy
y = symbols('y')
t = symbols('t')

yAnf = y*sympy.sin(t)**2

def Testverfahren(t0, y0, Ziel,h):
    Schrittweite = Ziel/h
    i = 0
    yi_List =[]
    ti_List = []
    yi_List.append(y0)
    ti_List.append(t0)
    k1 = float(yAnf.subs([(y,y0),(t,t0)]))
    yi_1 = y0+h/2*k1
    ti_h = t0+h/2
    k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
    
    while i < Schrittweite:
        ti = ti_List[-1] + h
        ti_List.append(ti)       
        yneu = yi_List[-1] + (h/4)*(k1+3*k2)
        yi_List.append(yneu)
        k1 = float(yAnf.subs([(y,yi_List[-1]),(t,ti_List[-1])]))
        yi_1 = yi_List[-1]+h/2*k1
        ti_h = ti_List[-1]+h/2
        k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
        
        i += h
    
    return yneu

print("Testverfahren:",Testverfahren(0,1,5,1))

def Heun(t0, y0, Ziel,h):
    Schrittweite = Ziel/h
    i = 0
    yi_List =[]
    ti_List = []
    yi_List.append(y0)
    ti_List.append(t0)
    k1 = float(yAnf.subs([(y,y0),(t,t0)]))
    yi_1 = y0+h*k1
    ti_h = t0+h
    k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
    
    while i < Schrittweite:
        ti = ti_List[-1] + h
        ti_List.append(ti)       
        yneu = yi_List[-1] + (h/2)*(k1+k2)
        yi_List.append(yneu)
        k1 = float(yAnf.subs([(y,yi_List[-1]),(t,ti_List[-1])]))
        yi_1 = yi_List[-1]+h*k1
        ti_h = ti_List[-1]+h
        k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
        
        i += h
    
    return yneu

print("Heun:",Heun(0,1,5,1))