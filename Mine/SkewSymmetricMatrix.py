# -*- coding: utf-8 -*-
"""
Created on Tue Dec 09 20:29:08 2014

@author: EngineeringIsLife
"""

def checkio(matrix):
    matrixtrans = [[0 for i in range(len(matrix[j]))] for j in range(len(matrix))]
    for row in range(len(matrix)):
        for item in range(len(matrix[row])):
            matrixtrans[item][row] = -1 * matrix[row][item]        
    return matrixtrans == matrix
        

print checkio([
    [ 0,  1,  2],
    [-1,  0,  1],
    [-2, -1,  0]]) == True
print checkio([
    [ 0,  1, 2],
    [-1,  1, 1],
    [-2, -1, 0]]) == False
print checkio([
    [ 0,  1, 2],
    [-1,  0, 1],
    [-3, -1, 0]]) == False
