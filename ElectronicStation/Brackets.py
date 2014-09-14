# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:27:33 2014

@author: EngineeringIsLife
"""

def checkio(expression):
    symbols = {'{':'}', '[':']', '(':')'}
    brackets = []
    for c in expression:
        if c in symbols.keys():         # Open bracket
            brackets.append(c)        
        elif c in symbols.values():     # Try to close bracket
            if len(brackets) and c is symbols[brackets[-1]]: # Bracket can be closed
                brackets.pop()
            else:                       # Bracket cannot be closed
                return False
    return not len(brackets)            # Unclosed brackets left?
            

print checkio("((5+3)*2+1)") == True
print checkio("{[(3+1)+2]+}") == True
print checkio("(3+{1-1)}") == False
print checkio("[1+1]+(2*2)-{3/3}") == True
print checkio("(((1+(1+1))))]") == False
print checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
print checkio("2+3") == True