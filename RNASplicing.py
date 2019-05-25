# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 14:32:33 2016

@author: hristodimitrov
"""
rnaCodoneTable = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", 
"GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", 
"AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A", "UCC" : "S", 
"CCC" : "P", "ACC" : "T", "GCC" : "A", "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", 
"UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "UAU" : "Y", "CAU" : "H", "AAU" : "N", 
"GAU" : "D", "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "UAA" : "", "CAA" : "Q", 
"AAA" : "K", "GAA" : "E", "UAG" : "", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "UGU" : "C", 
"CGU" : "R", "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", 
"UGA" : "", "CGA" : "R", "AGA" : "R", "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" }

def removeFromDnaString(dnaSequence, intron):
    return dnaSequence.replace(intron, "")

def readFile():
    fastaFile = open("FastaSample.fasta", "r")
    stringFile = ""
    result = []
    for x in fastaFile:
        stringFile += x

    splittedString = stringFile.split(">")

    for x in splittedString:
        sequence = ""
        splittedRosalindSequence = x.split("\n")
        flag = 0
        for s in splittedRosalindSequence:
            if flag != 0:
                sequence += s
            flag = 1
        result.append(sequence)
    fastaFile.close()
    del result[0]
    return result

fileAsList = readFile()
dnaSequence = fileAsList[0]
del fileAsList[0]
for intron in fileAsList:
    dnaSequence = removeFromDnaString(dnaSequence, intron)

rnaSequence = dnaSequence.replace("T","U")
splitRnaSequence = [rnaSequence[x:x+3] for x in range(0,len(rnaSequence),3)]
result = ""
for kodon in splitRnaSequence:
    result = result + rnaCodoneTable[kodon]
    
print (result)
