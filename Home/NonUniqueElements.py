# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 18:29:51 2014

@author: EngineeringIsLife
"""

def checkio(data):
    uniques = []
    for i in set(data):
        if data.count(i) == 1:
            uniques.append(i)
        
    for i in uniques:
        data.remove(i)
    return data
        
        
        
print checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
print checkio([1, 2, 3, 4, 5]) == []
print checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
print checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9] 
