#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:40:18 2019

@author: marceldann
"""

from sympy import symbols,factor
from sympy.plotting import plot
x = symbols('x')

def Approximieren(Funktion,xWerte):
    x = symbols('x')
    v,i,k,m,Summe,y = 0,0,0,0,0,0
    h = 1
    L,S,Produkt,yWerte = [],[],[],[]
    n = len(xWerte)-1
    
    while y < len(xWerte):
        Y = Funktion.subs(x, xWerte[y])
        yWerte.append(Y)
        y += 1
        
    while n >= v:
        for j in range(len(xWerte)): 
            if j != v:
                l1 = (x-xWerte[j])/(xWerte[v]-xWerte[j])
                L.append(l1)   
        v += 1
        
    while i < len(L):
        p = L[i]*L[i+h]
        h += 1
        
        while h < n:
            p *= L[i+h]
            h += 1
        
        Produkt.append(p)
        h = 1
        i += n
     
    while k <= n:
        s = Produkt[k]*yWerte[k] 
        S.append(s)
        k += 1
        
    while m <= n:
        Summe += S[m]
        m += 1
        
    return factor(Summe),yWerte

#print(Approximieren(1/(x**2+1),[-2,-1.5,-1]))
p1 = plot(Approximieren(1/(x**2+1),[-2,-1.5,-1]),ylim=[-0.1,2],xlim=[-2,2.5])
#print(Approximieren(1/(x**2+1),[-0.5,0,0.5]))
p2 = plot(Approximieren(1/(x**2+1),[-1,0,0.5]),ylim=[-0.1,2],xlim=[-0.5,0.5])
#print(Approximieren(1/(x**2+1),[0.5,1,1.5]))
p3 = plot(Approximieren(1/(x**2+1),[0.5,1,1.5]),ylim=[-0.1,2],xlim=[0.5,1.5])
p1.append(p2[0])
p1.append(p3[0])
p1[0].line_color='r'
p1[1].line_color='g'
p1.show()
p1.legend