# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 12:59:01 2014

@author: EngineeringIsLife
"""

def checkio(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    most = 0
    symbol = ''
    for alpha in alphabet:
        counter = text.count(alpha)
        if counter > most:
            symbol = alpha
            most = counter
    return symbol
        
    
print checkio("Hello World!") == "l"
print checkio("How do you do?") == "o"
print checkio("One") == "e"
print checkio("Oops!") == "o"
print checkio("AAaooo!!!!") == "a"
print checkio("abe") == "a"

"""
Example:
def checkio(text):
    text = text.lower() 
    d = {k:text.count(k) for k in text if k.isalpha()} 
    return max(sorted(d.keys()), key = lambda k: d[k]) 
"""