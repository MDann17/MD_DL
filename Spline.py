#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:20:28 2019

@author: marceldann
"""

from sympy import symbols
x = symbols('x')

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt  

xm = np.array([-2,-1.5,-1,0,0.5,1,1.5])
ym = []
Funktion = 1/(x**2+1)
y = 0
while y < len(xm):
   Y = Funktion.subs(x, xm[y])
   ym.append(Y)
   y += 1

m = GEKKO()
m.x = m.Param(value=np.linspace(-2,1.5))
m.y = m.Var()
m.options.IMODE=2
m.cspline(m.x,m.y,xm,ym)
m.solve(disp=False)
#help(m.cspline)

plt.plot(xm,ym,'bo',label='data')
plt.plot(m.x.value,m.y.value,'r--',label='cubic spline')
plt.legend(loc='best')
plt.show()
