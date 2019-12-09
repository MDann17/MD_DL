#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:54:01 2019

@author: marceldann
"""

def Euler(pferd, ochse):
    gesamt = 1770
    x = 57
    y = 0
    z = 0
    
    while z < x:
        if gesamt%(x * pferd + y * ochse) != 0:
            x = x - 1
            y = y + 1
        z+=1
        
    return x, y
        
print(Euler(31,21))
    