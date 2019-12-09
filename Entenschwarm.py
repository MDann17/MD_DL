#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:18:02 2019

@author: marceldann
"""
Enten = []
anzahlEnten = range(1,260,1)
j = 0
for n in anzahlEnten:
    j = j + n
    if 1000 < j < 10000:
        if j%2 == 0:
            Enten.append(j)     
        
anzahlEntenklein1 = range(1,260,1)
z = 0
for m in anzahlEntenklein1:
    z = z + m
    if 500 < z < 5000:
        #print("Mögliche Reihen bei 500 - 5000 Enten: \t\t", z)
        if z*2 in Enten:
            print("Möglich",z*2)              

