# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:39:52 2015

@author: hristodimitrov
"""
def searchForRestrictedSite(sequence, complementarySequence, wordLength):
    index = 1
    for i in range (1, len(sequence) - wordLength):
        sequencePart = sequence[i:wordLength+1]
        print sequencePart
        complementaryPart = complementarySequence[:wordLength]
        print complementaryPart
        reverseComplementaryPart = complementaryPart[::-1]
        print reverseComplementaryPart
        if sequencePart == reverseComplementaryPart:
            print index, wordLength

def getStringFromFile(fileObject):
    stringFile = ""
    for x in fileObject:
        stringFile += x
        
    return stringFile
    
def getComplementarySequence(sequence):
    complementarySequence = ""
    for i in rosalindSequence:
        if i == "A":
            complementarySequence += "T"
        if i == "T":
            complementarySequence += "A"
        if i == "G":
            complementarySequence += "C"
        if i == "C":
            complementarySequence += "G"
    return complementarySequence

fastaFile = open("FastaRestrictionSites.fasta", "r")
stringFile = getStringFromFile(fastaFile)

rosalindSequence = stringFile[12:]
print rosalindSequence
complementarySequence = getComplementarySequence(rosalindSequence)

print complementarySequence

searchForRestrictedSite(rosalindSequence, complementarySequence, 4)
