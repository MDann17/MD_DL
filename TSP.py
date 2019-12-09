#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 12:30:25 2019

@author: marceldann
"""
import numpy as np
import matplotlib.pyplot as plt
import math
#import time

#start = time.time()

fobj = open("tsp01.data.txt")

for line in fobj:
    #plt.plot(line.rstrip()[1])
    print(line.rstrip())
fobj.close()
"""
Daten = np.loadtxt("tsp01.data.txt")
x = Daten[0:15, 0]
y = Daten[0:15, 1]
i = 1
j = 0
distNeu = 10000

Nachbar = np.array([])
Nachbar = np.append(Nachbar, [distNeu])
plt.plot(Nachbar)
#distNeu = math.sqrt((x[3] - x[0])**2 + (y[3] - y[0])**2)
#print(distNeu)
while i <= 16:
    dist = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
    if dist < distNeu:
        distNeu = dist
        np.delete(Nachbar, -1)
        Nachbar = np.append(Nachbar, [dist])
        i += 1
        print(Nachbar)
        #plt.plot(Nachbar)
    
    
#print(dist)
#print(x, y)
#print(Daten)
#plt.scatter(x, y)

#print(Nachbar)
#end = time.time()
#print(end-start)"""