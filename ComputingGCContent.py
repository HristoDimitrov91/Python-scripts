# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:21:12 2015

@author: hristodimitrov
"""
def computeGCContent(dna):
    if len(dna) == 0:
        return
    guanine = "G"
    cytosine = "C"
    length = len(dna)
    
    countGuanine = dna.count(guanine, 0, length)
    countCytosine = dna.count(cytosine, 0, length)
    
    return (countCytosine + countGuanine) / float(length)
    
maxGCContent = 0.0
resultGCContent = 0.0
resultName = ""

fastaFile = open("FastaSample.fasta", "r")
stringFile = ""
for x in fastaFile:
    stringFile += x
    
splittedString = stringFile.split(">")    

splittedString.remove('')
for x in splittedString:
    sequence = ""
    rosalindNameIdentifier = x[:13]
    rosalindSequence = x[13:]
    splittedRosalindSequence = rosalindSequence.split("\n")
    for s in splittedRosalindSequence:
        sequence += s
    gcContent = computeGCContent(sequence)
    if gcContent > maxGCContent:
        resultName = rosalindNameIdentifier
        resultGCContent = gcContent
        maxGCContent = gcContent

fastaFile.close()

print (resultName)
print (round(resultGCContent * 100, 6))

