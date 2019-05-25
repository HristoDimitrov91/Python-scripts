# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:15:51 2016

@author: hristodimitrov
"""

monthsToLive = 17
monthsToReproduce = 97
count = 1

matrix = [[0 for x in range(monthsToLive)] for y in range(monthsToReproduce)]

matrix[0][0] = 1

print (matrix)

for i in range(1,monthsToReproduce):
    matrix[i][0] = count - matrix[i-1][0]
    localCount = matrix[i][0]
    for j in range(1, monthsToLive):
        matrix[i][j] = matrix[i-1][j-1]
        localCount = localCount + matrix[i][j]
    count = localCount

print (count)