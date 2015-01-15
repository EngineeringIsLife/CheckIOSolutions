# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 18:52:08 2015

@author: EngineeringIsLife
"""

def rotate_map_clockwise(map_array):
    transposed_map = zip(*map_array)           # Transpose matrix
    rotated_map = []
    for row in transposed_map:
        rotated_map.append(''.join(row[::-1])) # Reverse row
    return rotated_map


def recall_password(grille, pw_map):
    pw = ''
    for rotations in range(4):
        for rowcount, row in enumerate(grille):
            for symbolcount, symbol in enumerate(row):
                if symbol == 'X':
                    pw += pw_map[rowcount][symbolcount]
        grille = rotate_map_clockwise(grille)
    return pw


print recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'
     
print recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'