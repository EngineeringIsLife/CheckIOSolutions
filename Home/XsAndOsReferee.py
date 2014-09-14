# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 14:32:33 2014

@author: EngineeringIsLife
"""

def checkio(game_result):
    """ 8 possibilities: 3x horizontal, 3x vertical, 2x cross """    
    for s in game_result:      # horizontal
        if s.count(s[0]) is 3 and s[0] is not ".":
            return s[0]
            
    for i in range(3):  # vertical
        if [s[i] for s in game_result].count(s[i][0]) is 3 and s[i][0] is not ".":
            return s[i][0]
            
    if [game_result[i][i] for i in range(3)].count(game_result[0][0]) is 3 and game_result[0][0] is not ".":   # cross top-left to bottom-right
        return game_result[0][0]
    if [game_result[i][-1-i] for i in range(3)].count(game_result[0][2]) is 3 and game_result[0][2] is not ".": # cross top right to bottom-left
        return game_result[0][2]
    return "D"
    
    

print checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
print checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
print checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"