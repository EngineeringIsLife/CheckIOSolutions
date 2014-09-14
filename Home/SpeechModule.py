# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 18:20:57 2014

@author: EngineeringIsLife
"""

FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = " hundred "

def checkio(number):
    str_h, str_d, str_u = '','',''
    
    if number >= 100:
        hundred = number//100
        number  = number - hundred*100
        str_h = FIRST_TEN[hundred] + HUNDRED
    
    if number >= 20:
        str_d = OTHER_TENS[number//10-2] + ' '
        str_u = FIRST_TEN[number%10]
        
    else:
        str_u = FIRST_TEN[number]
        
    return (str_h+str_d+str_u).rstrip()

print checkio(4)=='four'
print checkio(143)=='one hundred forty three'
print checkio(12)=='twelve'
print checkio(101)=='one hundred one'
print checkio(212)=='two hundred twelve'
print checkio(40)=='forty'