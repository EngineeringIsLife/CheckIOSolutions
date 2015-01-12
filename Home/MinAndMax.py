# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 17:57:12 2014

@author: EngineeringIsLife
"""

def min(*args, **fcn_in):
    lastlevel = iter(args[0] if len(args) is 1 else args)
    best = next(lastlevel)
    fcn = fcn_in["key"] if fcn_in else lambda x: x
    for arg in lastlevel:
        if fcn(arg) < fcn(best):
            best = arg
    return best
    
def max(*args, **fcn_in):
    lastlevel = iter(args[0] if len(args) is 1 else args)
    best = next(lastlevel)
    fcn = fcn_in["key"] if fcn_in else lambda x: x
    for arg in lastlevel:
        if fcn(arg) > fcn(best):
            best = arg
    return best

#max(3, 2) == 3
print min({1, 2, 3, 4, -10})
print min(abs(i) for i in range(-10, 10))
print max(abs(i) for i in range(-10, 10))
print min(3, 2) == 2
print min(2, 3) == 2
print min([1, 2, 0, 3, 4]) == 0
print max([1, 2, 0, 3, 4]) == 4
print min("hello") == "e"
print min(3.2,2,key=int) == 2
print min(2.2, 5.6, 5.9,2.1, key=int) == 2.2# == 5.6
print max(2.2, 5.6, 5.9, key=int) == 5.6
print min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]