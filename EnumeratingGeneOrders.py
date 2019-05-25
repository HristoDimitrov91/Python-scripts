# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:16:14 2016

@author: hristodimitrov
"""
import itertools as it

permutationLength = 6
totalPermutations = 1

for i in range(1,permutationLength+1):
    totalPermutations = totalPermutations*i
print (totalPermutations)


gen = it.permutations(range(1,permutationLength+1))
string = ()
for i in gen:
    print (i)

print (string)