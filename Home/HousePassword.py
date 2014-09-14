# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 20:03:25 2014

@author: EngineeringIsLife
"""

def checkio(data):
    if len(data) < 10:
        return False
        
    digit = False
    for i in data:
        if i.isdigit():
            digit = True
            break
    if digit == False:
        return False
            
    upper = False
    for i in data:
        if i.isupper():
            upper = True
            break
    if upper == False:
        return False

    lower = False
    for i in data:
        if i.islower():
            lower = True
            break
    if lower == False:
        return False
    
    return True

print checkio('A1213pokl') == False
print checkio('bAse730onE') == True
print checkio('asasasasasasasaas') == False
print checkio('QWERTYqwerty') == False
print checkio('123456123456') == False
print checkio('QwErTy911poqqqq') == True