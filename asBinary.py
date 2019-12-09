#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:35:20 2019

@author: marceldann
"""

def asBinary(Umzurechnen, nachkomma):
    Zahl, Komma = str(Umzurechnen).split(".")
    Zahl = int(Zahl)
    Komma = int(Komma)
    Nachkommastellen = len(str(Komma))
    Teiler = 10**Nachkommastellen
    Komma1 = Komma/Teiler
    i=1
    ListeVorkomma = []
    ListeNachkomma = []
    ListeBias = []
    
    while Zahl > 0.5:
        Zahl1 = Zahl%2
        if Zahl1 == 1:
            ListeVorkomma.append(1)
            Zahl = (Zahl/2) - 0.5
        else:
            ListeVorkomma.append(0)
            Zahl = Zahl/2
                
        while i < 30:       
            Komma1 = Komma1*2
            if Komma1 > 1:
                ListeNachkomma.append(1)
                Komma1 = Komma1 - 1
            else:
                ListeNachkomma.append(0)
            i = i+1
            
        
    ListeVorkomma.reverse()
    del ListeVorkomma[0]
    addiert = ListeVorkomma + ListeNachkomma
    Exponent = len(ListeVorkomma)
    Bias = 127 + Exponent
    
    while Bias > 0.5:
        Bias1 = Bias%2
        if Bias1 == 1:
            ListeBias.append(1)
            Bias = (Bias/2) - 0.5
        else:
            ListeBias.append(0)
            Bias = Bias/2
    
    ListeBias.reverse()
    Final = ListeBias + addiert
    Final = Final[:32]
    return Final

print(asBinary(18.4, 0))
