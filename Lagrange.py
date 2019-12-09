#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:29:35 2019

@author: marceldann
"""
from sympy import symbols,factor
from sympy.plotting import plot

def Lagrange(xWerte,yWerte):
    n = len(xWerte)-1
    x = symbols('x')
    v,i,k,m,Summe = 0,0,0,0,0
    h = 1
    L,S,Produkt = [],[],[]

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

print(Lagrange([-4,-2,0,2,4,6],[-2,-1,1,0,2,2]))
plot(Lagrange([-4,-2,0,2,4,6],[-2,-1,1,0,2,2]),ylim=[-10,10])