#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:57:49 2019

@author: marceldann
"""

def Maschinenzahl(Umzurechnen, Basis, Mantisse):
    Zahl, Komma = str(Umzurechnen).split(".")
    Zahl = int(Zahl)
    Komma = int(Komma)
    Nachkommastellen = len(str(Komma))
    Teiler = 10**Nachkommastellen
    Komma1 = Komma/Teiler
    i=0
    ListeVorkomma = []
    ListeNachkomma = []
    ListeBias = []
    test =[]
        
    if Basis == 3:
        while Zahl > 0:
            Zahl1 = Zahl%3
            if Zahl1 > 0:  
                ListeVorkomma.append(Zahl1)
                Zahl = Zahl/3
                Zahl, Komma0 = str(Zahl).split(".")
                Zahl = int(Zahl)
                  
            else:
                ListeVorkomma.append(0)
                Zahl = Zahl/3
                Zahl, Komma0 = str(Zahl).split(".")
                Zahl = int(Zahl)
                          
        while i < 30:
            Komma1 = Komma1 * 3
            if Komma1 < 3 and Komma1 >= 1:
                Zahl2, Komma2 = str(Komma1).split(".")
                Zahl2 = int(Zahl2)
                Komma2 = int(Komma2)
                Nachkommastellen1 = len(str(Komma2))
                Teiler1 = 10**Nachkommastellen1
                Komma1 = Komma2/Teiler1
                Komma1 = round(Komma1, 3)
                ListeNachkomma.append(Zahl2)
            else:
                ListeNachkomma.append(0)
            i = i + 1
                
        ListeVorkomma.reverse()
        #del ListeVorkomma[0]
        addiert = ListeVorkomma + ListeNachkomma
        Exponent = len(ListeVorkomma)
        Bias = 127 + Exponent
        
        while Bias > 0.5:
            Bias1 = Bias%3
            if Bias1 == 1:
                ListeBias.append(Bias1)
                Bias = Bias/3
                Bias, Komma3 = str(Bias).split(".")
                Bias = int(Bias)

            else:
                ListeBias.append(0)
                Bias = Bias/3
                Bias, Komma3 = str(Bias).split(".")
                Bias = int(Bias)
        
        ListeBias.reverse()
        Final = ListeBias + addiert
        Final = Final[:32]
    return addiert

print(Maschinenzahl(10.456, 3, 0))