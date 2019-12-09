#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:50:45 2019

@author: marceldann
"""
"""
y' = y · sin2 t ; y(0) = 1
korrekter Wert für y(5)=13.96"""

from sympy import symbols
import sympy
y = symbols('y')
t = symbols('t')

yAnf = y*sympy.sin(t)**2

def EulPolygon(t0, y0, Schrittweite):
    f_ti_yi = y0
    i = 0
    yi_List =[]
    ti_List = []
    yi_List.append(y0)
    ti_List.append(t0)
    f_ti_yi = float(yAnf.subs([(y,yi_List[0]),(t,ti_List[0])]))
    
    while i <=4:
        ti = ti_List[-1] + Schrittweite
        ti_List.append(ti)
        
        yneu = yi_List[-1] + f_ti_yi * Schrittweite
        yi_List.append(yneu)
        f_ti_yi = float(yAnf.subs([(y,yi_List[-1]),(t,ti_List[-1])]))
        
        i += Schrittweite
    
    return yneu

print("Eulersches Polygonzugverfahren:",EulPolygon(0,1,0.5))


def VerbesserterEuler(t0, y0, Ziel, h):
    Schrittweite = Ziel/h
    i = 0
    yi_List =[]
    ti_List = []
    yi_List.append(y0)
    ti_List.append(t0)
    k1 = float(yAnf.subs([(y,y0),(t,t0)]))
    yi_1 = y0+(h/2)*k1
    ti_h = t0+h/2
    k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
    
    while i < Schrittweite:
        ti = ti_List[-1] + h
        ti_List.append(ti)
        
        yneu = yi_List[-1] + h*k2
        yi_List.append(yneu)
        k1 = float(yAnf.subs([(y,yi_List[-1]),(t,ti_List[-1])]))
        yi_1 = yi_List[-1]+(h/2)*k1
        ti_h = ti_List[-1]+h/2
        k2 = float(yAnf.subs([(y,yi_1),(t,ti_h)]))
        
        i += h
    
    return yneu

print("Verbessertes Eulerverfahren:",VerbesserterEuler(0,1,5, 0.5))


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

print("Heun:",Heun(0,1,5,0.5))


def Klassich_Runge_Kutta(t0, y0, Ziel, h):
    Schrittweite = Ziel/h
    i = 0
    yi_List =[]
    ti_List = []
    yi_List.append(y0)
    ti_List.append(t0)
    k1 = float(yAnf.subs([(y,y0),(t,t0)]))
    yi_k2 = y0+(h/2)*k1
    ti_k2 = t0+h/2
    k2 = float(yAnf.subs([(y,yi_k2),(t,ti_k2)]))
    yi_k3 = y0+(h/2)*k2
    ti_k3 = t0+h/2
    k3 = float(yAnf.subs([(y,yi_k3),(t,ti_k3)]))
    yi_k4 = y0+h*k3
    ti_k4 = t0+h
    k4 = float(yAnf.subs([(y,yi_k4),(t,ti_k4)]))

    
    while i < Schrittweite:
        ti = ti_List[-1] + h
        ti_List.append(ti)       
        yneu = yi_List[-1] + h/6*(k1+2*k2+2*k3+k4)
        yi_List.append(yneu)
        k1 = float(yAnf.subs([(y,yi_List[-1]),(t,ti_List[-1])]))
        yi_k2 = yi_List[-1]+(h/2)*k1
        ti_k2 = ti_List[-1]+h/2
        k2 = float(yAnf.subs([(y,yi_k2),(t,ti_k2)]))
        yi_k3 = yi_List[-1]+(h/2)*k2
        ti_k3 = ti_List[-1]+h/2
        k3 = float(yAnf.subs([(y,yi_k3),(t,ti_k3)]))
        yi_k4 = yi_List[-1]+h*k3
        ti_k4 = ti_List[-1]+h
        k4 = float(yAnf.subs([(y,yi_k4),(t,ti_k4)]))
        
        i += h
    
    return yneu

print("Klassisches Runge_Kutta_Vefahren:",Klassich_Runge_Kutta(0,1,5,0.5))


