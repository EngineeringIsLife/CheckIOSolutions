# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 21:26:04 2014

@author: EngineeringIsLife
"""
def checkpatternline(patternline, line):
    psize = len(patternline)
    lsize = len(line)
    pos = []
    for i in range(lsize):
        if patternline == line[i:i+psize]:
            pos.append(i)
            i += psize
    return pos

# Working for specific cases - still not fully functional
def checkio(pattern, image):
    s = len(pattern[0])
    l = len(image[0])
    #print "s: ", s
    #print "l: ", l
    for rowcount, row in enumerate(image):
        if rowcount == l-1: break
        #print "Vorher: ", row
        for i in range(l-s+1):
            if image[rowcount][i:i+s] == pattern[0] and image[rowcount+1][i:i+s] == pattern[1]:
                for j in range(s):
                    image[rowcount+0][i+j] += 2
                    image[rowcount+1][i+j] += 2
        #print "Nachher: ", row
    #print image
    return image            
            
"""
def checkio(pattern, image):
    s = len(pattern[0])
    l = len(image[0])
    #print "s: ", s
    #print "l: ", l
    for rowcount, row in enumerate(image):
        if rowcount == l-1: break
        #print "Vorher: ", row
        for i in range(l-s+1):
            if image[rowcount][i:i+s] == pattern[0] and image[rowcount+1][i:i+s] == pattern[1]:
                for j in range(s):
                    image[rowcount+0][i+j] += 2
                    image[rowcount+1][i+j] += 2
        #print "Nachher: ", row
    #print image
    return image
"""

print checkio([[1, 0], [1, 1]],
        [[0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [1, 0, 1, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                               [0, 3, 3, 0, 0],
                               [3, 2, 1, 3, 2],
                               [3, 3, 0, 3, 3],
                               [0, 1, 1, 0, 0]]

print checkio([[1, 1], [1, 1]],
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]) == [[3, 3, 1],
                         [3, 3, 1],
                         [1, 1, 1]]
                         