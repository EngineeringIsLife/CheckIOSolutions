# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:00:28 2014

@author: EngineeringIsLife
"""


def checkio(data):
    return data[0]+checkio(data[1:]) if len(data) > 1 else data[0]

print checkio([1, 2, 3])# == 6
print checkio([2, 2, 2, 2, 2, 2])# == 12