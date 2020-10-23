#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:31:25 2020

@author: hanabillings
"""

"""

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

"""

def getMotif(sequences):
    pos = []
    i = 0
    sequence = sequences[0]
    substring = sequences[1]
    for i in range(0, len(sequence)):
        if sequence[i:(i+len(substring))] == substring:
            pos.append(i+1)
    return pos
    
    

sequences = "GATATATGCATATACTT", "ATAT" 
print(getMotif(sequences))
