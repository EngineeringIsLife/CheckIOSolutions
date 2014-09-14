# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 20:03:25 2014

@author: EngineeringIsLife
"""

def checkio(data):
    if len(data) < 10:
        return False
        
    digit, upper, lower = False, False, False    
    for i in data:
        if i.isdigit():
            digit = True
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
            
    return digit and upper and lower

print checkio('A1213pokl') == False
print checkio('bAse730onE') == True
print checkio('asasasasasasasaas') == False
print checkio('QWERTYqwerty') == False
print checkio('123456123456') == False
print checkio('QwErTy911poqqqq') == True