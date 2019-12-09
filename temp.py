# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import numpy as np
import matplotlib.pyplot as plt

def heron(a,epsi):
    x=a
    error =1
    grafik = []
    
    while error > epsi:
        y=(x**2+a)/(2*x)
        error = abs(a-y**2)
        grafik.append(error)
        x=y
        
    return y, grafik
    
plt.plot(heron(10, 10**-6)[1])

print("y: \t\t", heron(10, 10**-6)[0])
print("grafik: \t", heron(10, 10**-6)[1])