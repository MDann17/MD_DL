#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 11:52:52 2019

@author: marceldann
"""

Data = open("rucksack.txt")
data = Data.read().splitlines()
inhalt,gewicht, wert = [], [], []
for line in data:
    inhalt.append(line.split(";")[0])
    gewicht.append(line.split(";")[1])
    wert.append(line.split(";")[2])

gewicht = [float(i) for i in gewicht]
wert = [float(i) for i in wert]

maxGewicht = 500
eta = []
inhaltValue = []
i = 0

while i < len(wert):
    x = wert[i]/gewicht[i]
    eta.append(x)
    i += 1

sortiert1Inhalt = [x for y, x in sorted(zip(eta, inhalt))]
sortiert2Wert = [x for y, x in sorted(zip(eta, wert))]
sortiert3Gewicht = [x for y, x in sorted(zip(eta, gewicht))]
      
eta.sort(reverse=True)  
sortiert1Inhalt.reverse() 
sortiert2Wert.reverse() 
sortiert3Gewicht.reverse()

wc = 0
vc = 0
vcMax = maxGewicht*max(eta)

RucksackInhalt =[]

k = 0
while k < len(eta):
    t = wc + sortiert3Gewicht[k]
    if t < maxGewicht:
        RucksackInhalt.append(sortiert1Inhalt[k])
        wc = t
        k += 1
    else:
        k += 1
        
print(RucksackInhalt)