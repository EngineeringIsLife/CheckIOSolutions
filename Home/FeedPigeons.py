# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 17:39:52 2014

@author: EngineeringIsLife
"""

def checkio(food):
    pigeons,pigeons_to_come = 0,1
    while pigeons+pigeons_to_come <= food:  # Enough food left for all?
        pigeons += pigeons_to_come          # They are coming...
        food -= pigeons                     # Feed 'em
        pigeons_to_come += 1                # Next time there will be one more...
    return max(pigeons,food)                # Enough food left to feed a new one at least once?

print checkio(1) == 1
print checkio(2) == 1
print checkio(3) == 2
print checkio(5) == 3
print checkio(10) == 6