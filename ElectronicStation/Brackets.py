# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:27:33 2014

@author: EngineeringIsLife
"""

def checkio(expression):
    brackets = {'{':'}', '[':']', '(':')'}
    opened = []
    for c in expression:
        if c in brackets.keys():        # Open bracket
            opened.append(c)        
        elif c in brackets.values():    # Try to close bracket
            if not len(opened):         # Too much close brackets
                return False
            elif c is brackets[opened[-1]]: # Bracket can be closed
                opened.pop()
            else:                       # Bracket cannot be closed
                return False
    return not len(opened)              # Any unclosed brackets left?


print checkio("((5+3)*2+1)") == True
print checkio("{[(3+1)+2]+}") == True
print checkio("(3+{1-1)}") == False
print checkio("[1+1]+(2*2)-{3/3}") == True
print checkio("(((1+(1+1))))]") == False
print checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
print checkio("2+3") == True