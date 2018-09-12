# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 15:43:41 2016

@author: hristodimitrov
"""
import re
proteinPattern = ""

dnaCodoneTable = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V", "TTC" : "F", "CTC" : "L", "ATC" : "I", 
"GTC" : "V", "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V", "TTG" : "L", "CTG" : "L", 
"ATG" : "M", "GTG" : "V", "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A", "TCC" : "S", 
"CCC" : "P", "ACC" : "T", "GCC" : "A", "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A", 
"TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A", "TAT" : "Y", "CAT" : "H", "AAT" : "N", 
"GAT" : "D", "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D", "TAA" : "", "CAA" : "Q", 
"AAA" : "K", "GAA" : "E", "TAG" : "", "CAG" : "Q", "AAG" : "K", "GAG" : "E", "TGT" : "C", 
"CGT" : "R", "AGT" : "S", "GGT" : "G", "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G", 
"TGA" : "", "CGA" : "R", "AGA" : "R", "GGA" : "G", "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G" }

def getProtein(sequence):
    splitRnaSequence = [sequence[x:x+3] for x in range(0,len(sequence),3)]
    result = ""
    for kodon in splitRnaSequence:
        result = result + dnaCodoneTable[kodon]
    return result

dnaSequence = "CGGCAACTAGTGCCCGGAACTTGGCTTCAGCCGATTATACTAATGGTTTCACCGCGTTTCTCGCCAGCCGTCTTGTGACATTAGTATGGTTATAAGAGATGTAACCTTCTCCTTGCAGCGTAGGGATCAACGACTTAGTCTAAGAAGAGAAACTGTCAGAATTTCACCCACCCAGTCCTCAATTCCATTTCTGCAACGTCACCCGAGCGAAGTCACGAAGAACTTGCTGACCGCAGAGCAGGAGACAAACAATAAGCATCATTGTCACTGGCTTAGGCGCCTTTCGGACCATGCCCGCATACTTCCGCAGAGTCGGTAAACGGCCTATGCCATGTATCTCTTACGACAGTGATCCATCAAGTAATAGTTACTGGACTCACTAAGCTGGCGTGTCGTCCGCAAGCAACAAAACCATTACTTCAGTGATATGGCCAAGAGGTCGTGACAACACGTAGGCTGGCTTTTCGAATTATTCCCAATCGTGATTAAGTCTAACGTTGCTCGGAATTCGCTAGTACCAGCAAAAGGATCGACCGTGTAACGATGACTTAGGCCATTCTGAGGAAACAAGCCGCGCAAACTCTCTCCCCCGCCGGACAGGACACGAATCGGACCACCGTCCCCGTTCGCCAATGCCGACACGTGGCTGTCGCGTACGATCTTGGTAATACCGATGGGAAACTTCAGTTACGGTTTGTGACGAGAAAGAAGCGAGTGTCTTATGGCTAAGGTAACCAACTTGACTGTGCCAGGATCTTAAAACCACCCGTTTAGTGACCCCAAAACAAAGTTGTGCGTGCCTAATAGGACATACTTAGGTTAGCTGGTGCTTCGGCCTATCGTAACTGGGTAGGTGTGGGTTATCTTGCTGTCGAATGGGGCAGGTCCTTGGATGTCCGGCGCGTGC"
proteinList = []
result = ""
for i in dnaSequence:
   if i == "A":
      result = result + "T"
   if i == "T":
      result = result + "A"
   if i == "G":
      result = result + "C"
   if i == "C":
      result = result + "G"

dnaSequenceReverseComplement = result[::-1]

print dnaSequence
print dnaSequenceReverseComplement

dnaMatches = re.match(proteinPattern, dnaSequence)
dnaReverseComplementMatches = re.match(proteinPattern, dnaSequenceReverseComplement)

if dnaMatches:
    for match in dnaMatches.groups():
        protein = getProtein(match)
        proteinList.append(protein)

if dnaReverseComplementMatches:
    for match in dnaReverseComplementMatches.groups():
        protein = getProtein(match)
        proteinList.append(protein)

print proteinList