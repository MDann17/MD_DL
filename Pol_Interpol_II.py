#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:25:00 2019

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
        
    return factor(Summe)

print(Approximieren(1/(x**2+1),[-2,-1.5,-1,0.5,1,1.5,0,2,2.5,2.7]))
p1=plot(Approximieren(1/(x**2+1),[-2,-1.5,-1,0.5,1,1.5,0,2,2.5,2.7]),ylim=[-0.1,2],xlim=[-3,3],legend = True)

print(Approximieren(1/(x**2+1),[-2,-1,0.5,1,0,2]))
p2=plot(Approximieren(1/(x**2+1),[-2,-1,0,1,2]),ylim=[-0.1,2],xlim=[-3,3])
p3=plot(Approximieren(1/(x**2+1),[-2,-1,-0.5,0,0.5,1,2]),ylim=[-0.1,2],xlim=[-3,3])
p1.append(p2[0])
p1.append(p3[0])
p1[0].line_color='r'
p1[0].label = '$n = 10$'
p1[1].line_color='g'
p1[1].label = '$n = 5$'
p1[2].line_color='b'
p1[2].label = '$n = 7$'
p1.show()








