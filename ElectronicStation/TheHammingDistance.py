# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 17:56:16 2014

@author: EngineeringIsLife
"""

def checkio(n, m):
    n,m = bin(n)[2:],bin(m)[2:]
    n = n.zfill(len(m))
    m = m.zfill(len(n))
    distance = 0
    for i in range(len(m)):
        distance += m[i] not in n[i]
    return distance

    

print checkio(117, 17) == 3
print checkio(1, 2) == 2
print checkio(16, 15) == 5
print checkio(16, 128)