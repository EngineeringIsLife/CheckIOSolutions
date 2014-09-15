# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 22:32:20 2014

@author: EngineeringIsLife
"""

def safe_pawns(pawns):
    counter = 0
    for pawn in pawns:
        x,y = pawn
        needed1 = chr(ord(x)+1) + chr(ord(y)-1)
        needed2 = chr(ord(x)-1) + chr(ord(y)-1)
        if needed1 in pawns or needed2 in pawns:
            counter += 1
    return counter
    
print safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
print safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1