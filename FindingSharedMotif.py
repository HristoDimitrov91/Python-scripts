# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:18:01 2016

@author: hristodimitrov
"""
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

def checkOtherSequences(sequence, list):
    for element in list:
        if sequence not in element:
            return False
    return True

def generateSequences(length, originalSequence):
    sequences = []
    for i in range(0, len(originalSequence) - length + 1):
        sequences.append(originalSequence[i:length+i])
    return sequences

def getLongestMatch():
    fileAsList = readFile()
    firstSequence = fileAsList[0]
    result = ""
    sequenceLength = len(firstSequence)
    for i in range(sequenceLength-1, -1, -1):
        sequences = generateSequences(i, firstSequence)
        for sequence in sequences:
            if checkOtherSequences(sequence, fileAsList):
                result = sequence
                return result

result = getLongestMatch()
print result