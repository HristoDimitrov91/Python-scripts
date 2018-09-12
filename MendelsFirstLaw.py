# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:31:08 2016

@author: hristodimitrov
"""
def propabilityOnlyHomoRecessive(homozigotRecessive, totalCount):
    result = 0.0
    result = (homozigotRecessive / totalCount) * ((homozigotRecessive - 1) / (totalCount - 1))
    return result
    
def propabilityOnlyHeterozigot(heterozigot, totalCount):
    result = 0.0
    result = (heterozigot / totalCount) * ((heterozigot - 1) / (totalCount - 1)) * 0.25
    return result
    
def propabilityHomoAndHeteroOne(heterozigot, homozigot, totalCount):
    result = 0.0
    result = (heterozigot / totalCount) * (homozigot / (totalCount - 1)) * 0.5
    return result
    
def propabilityHomoAndHeteroTwo(heterozigot, homozigot, totalCount):
    result = 0.0
    result = (homozigot / totalCount) * (heterozigot / (totalCount - 1)) * 0.5
    return result

homozigotDominant = 28.0
heterozigot = 24.0
homozigotRecessive = 15.0

totalCount = homozigotDominant + heterozigot + homozigotRecessive

propability = 0.0
propability += propabilityOnlyHomoRecessive(homozigotRecessive, totalCount)
propability += propabilityOnlyHeterozigot(heterozigot, totalCount)
propability += propabilityHomoAndHeteroOne(heterozigot, homozigotRecessive, totalCount)
propability += propabilityHomoAndHeteroTwo(heterozigot, homozigotRecessive, totalCount)

print 1 -propability