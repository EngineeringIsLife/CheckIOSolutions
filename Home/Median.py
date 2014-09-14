# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 19:30:50 2014

@author: EngineeringIsLife
"""

def checkio(data):
    data.sort()
    midID = len(data)//2

    if len(data) % 2 is 1:
        return data[midID]
    else:
        return (data[midID-1] + data[midID]) / 2.0
    
print checkio([1, 2, 3, 4, 5]) == 3
print checkio([3, 1, 2, 5, 3]) == 3
print checkio([1, 300, 2, 200, 1]) == 2
print checkio([3, 6, 20, 99, 10, 15]) == 12.5