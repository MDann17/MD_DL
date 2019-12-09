#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:46:32 2019

@author: marceldann
"""

from sympy import symbols
#import math
import matplotlib.pyplot as plt
import numpy as np
from sympy.plotting import plot
from matplotlib import pyplot as plt

X = np.array([-4, -2, 0, 2, 4, 6])
v = np.vander(X)
V = np.empty([6,6])
i=0
run = True
while run == True:
    
    V[i,0] = v[i,5]
    V[i,1] = v[i,4]
    V[i,2] = v[i,3]
    V[i,3] = v[i,2]
    V[i,4] = v[i,1]
    V[i,5] = v[i,0]
    i += 1
    if i == 6:
        run = False
#print(v)
#print(V)

y = np.array([-2, -1, 1, 0, 2, 2])
a = np.linalg.solve(V, y)
a = [float(i) for i in a]
x = symbols('x')
p1 = plot(a[0]+a[1]*x+a[2]*x**2+a[3]*x**3+a[4]*x**4+a[5]*x**5)

plt.axis([-8, 8, -5, 5])
plt.title('Vandermonde')
plt.plot(X,y,'ro',label = 'Punkte')
plt.plot(p1,label = 'Funktion')
plt.legend()
plt.show()