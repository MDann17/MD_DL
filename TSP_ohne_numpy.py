#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:12:14 2019

#@author: marceldann
"""

import matplotlib.pyplot as plt
import math

m = 0
c = 0
b = 0
d = 2
e = 3
distAlt = 1000000

Data = open("tsp01.data.txt")
data = Data.read().splitlines()
x,y = [], []
for line in data:
    x.append(line.split()[0])
    y.append(line.split()[1])
X = [float(i) for i in x]
Y = [float(i) for i in y]
X.remove(8.0)
Y.remove(124.0)
start = [8.0,124.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

while c < 15:
    while m < len(X):
        distNeu = math.sqrt((X[m] - start[b])**2 + (Y[m] - start[b+1])**2)
        indizeX = X[m] 
        indizeY = Y[m]
        if distNeu <= distAlt:
            distAlt = distNeu
            start[d] = indizeX
            start[e] = indizeY
            m += 1
            
        else:
            m += 1
            
    if indizeX in X:
        X.remove(start[d])
        
    if indizeY in Y:
        Y.remove(start[e])

    m = 0
    b += 2
    d += 2
    e += 2
    distAlt = 100000
    c += 1
print(data,x)    
plt.plot(start[0::2],start[1::2])
