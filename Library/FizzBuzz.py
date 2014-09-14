# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 17:56:34 2014

@author: EngineeringIsLife
"""

def checkio(number):
    output = ""
    
    if number % 3 is 0:
        output = "Fizz"

    if number % 5 is 0:
        if output is not "":
            output += " "
        output += "Buzz"

    if output is "":
        output = str(number)
    return output
    

print checkio(100)
print checkio(15)
print checkio(6)
print checkio(5)
print checkio(7)