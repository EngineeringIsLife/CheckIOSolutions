# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 16:55:28 2014

@author: EngineeringIsLife
"""

def weak_point(matrix):
    index  = range(len(matrix))
    rowsum = [0 for i in index]
    colsum = [0 for i in index]
    for row in index:
        for col in index:
            rowsum[row] += matrix[row][col]
            colsum[col] += matrix[row][col]
    
    return [rowsum.index(min(rowsum)), colsum.index(min(colsum))]
    

print weak_point([[7, 2, 7, 2, 8],
            [2, 9, 4, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [3, 3]
print weak_point([[7, 2, 4, 2, 8],
            [2, 8, 1, 1, 7],
            [3, 8, 6, 2, 4],
            [2, 5, 2, 9, 1],
            [6, 6, 5, 4, 5]]) == [1, 2]