# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:35:08 2015

@author: hristodimitrov
"""

months = 34
litter = 2

pairsThatCannotReproduce = 1
pairsThatCanReproduce = 0
totalPairs = 1

for i in range(1,months):
 
    pairsThatCannotReproduce = pairsThatCanReproduce * litter
    pairsThatCanReproduce = totalPairs
    totalPairs = pairsThatCannotReproduce + pairsThatCanReproduce
    
print totalPairs
    