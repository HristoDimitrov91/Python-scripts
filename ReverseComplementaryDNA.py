# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:05:33 2015

@author: hristodimitrov
"""

dna = "CCTATTTAAGAAAGTAGGCTCCCGCGACTAGTTTATGATTGCCCTTTGGATCTAGTGACCTTCAGGTGCCTTTCTCAGATGTACCCCGATGTGGAGTGAAAGAGATTTAATAGATACTAGTTGGTGTTGATGTCTGAAAAGCATCCGAACTTGTCTGGCGCCGTATCAGGCGCAGTTCCCCGCTATCCGGGGTGTATGAATGCTATCTGCGTACCGTGAATGACTAGCACTGTTCAAGTGCCATGTGGGTGGCCGAAGTAGTCGTCAGAGATGGACATGAAAAGACGACAGGTGCCATTTACTCGGTATGACCCCACACGTATACGATGGTGCTTGTACATCTTTTTGCCTTATAAAAGCAAGGGTCGCTCAGGGTAAAAAGGAGTACCCCATTCCCGGTACCGGTTCATACATGAACCCCTTTTGGTAGCTGTAGGAGGTCGATCCCATCCTTTCGAACCGGGCTAATGGGGGAATACCCGTGTGTTTTTCATGTTTGGGATTCTACCAAACTGCGTGGGGTAACTGCTTGGCGCGGGCTGGGGAGTCATTGGAAAGTAAGCCAGAGAGATAAGGAGCATAACCGACCGCTAACCGGGCTGCCTCCACAGACCTGGAGAAGCAGCCCACTGGACCAACGAAGCAGTTGCAACTTTCACTTGCTTCATATTAATCCTAATCTTTTCCCCCGGGTAAGGTTGCCTCAGACAATCCCGTTCGCATGGTCAGTACAAAAGGATGTTAGGTCCGCTGCCCCAGTACGTGGCACATCCGGCCTTGAGAACAGCCGAACATGAGAGGACAGTCGACACTATTAGTCGCAAGTTGCGAACCATTGCATAGTCGAAGTTTGCGAACTCTCTGGCAAGCTAAGGCCTTACAAGAGGAGAAAGTGTACAAGTGTTAACCATAAGCTCCTCGCTTCTACG"
result = ""
for i in dna:
   if i == "A":
      result = result + "T"
   if i == "T":
      result = result + "A"
   if i == "G":
      result = result + "C"
   if i == "C":
      result = result + "G"

revComplDna = result[::-1]
print revComplDna