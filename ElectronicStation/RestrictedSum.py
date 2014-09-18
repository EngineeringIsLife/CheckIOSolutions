# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:00:28 2014

@author: EngineeringIsLife
"""

def get(currentList, currentVal):
    currentVal += currentList.pop()
    if currentList:
        currentVal = get(currentList, currentVal)
    return currentVal

def checkio(data):
    return get(data, 0)

print checkio([1, 2, 3])# == 6
print checkio([2, 2, 2, 2, 2, 2])# == 12