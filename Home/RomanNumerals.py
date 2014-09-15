# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 18:06:01 2014

@author: EngineeringIsLife
"""

ROMAN   = {0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
factor1 = {1:1, 4:1, 5:5, 9:1}
factor2 = {1:0, 4:5, 5:0, 9:10}


def checkio(decimal):    
    solution = ''        
    for i in [1000,100,10,1]:
        for j in [9,5,4,1]:
            while decimal >= j * i:
                solution += ROMAN[factor1[j]*i] + ROMAN[factor2[j]*i]
                decimal  -= j * i    
    return solution

print checkio(6)  == 'VI'
print checkio(76) == 'LXXVI'
print checkio(13) == 'XIII'
print checkio(44) == 'XLIV'
print checkio(1984) == 'MCMLXXXIV'
print checkio(3999) == 'MMMCMXCIX'