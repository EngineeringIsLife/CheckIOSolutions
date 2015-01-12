# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 21:26:04 2014

@author: EngineeringIsLife
"""


# from itertools import product -> can replace 2-dimensional for-loops
# example: for x,y in product(range(sizex), range(sizey)) ... iterates over
# every possible element.

def checkio(pattern, image):
    # Get dimensions
    psizex, psizey = len(pattern[0]), len(pattern)
    isizex, isizey = len(image[0]),   len(image)
    
    # Split in rows and columns
    imgrows, imgcols = image,   zip(*image)
    patrows, patcols = pattern, zip(*pattern)
    
    # Iterate through image
    for posx in range(isizex-psizex+1):
        for posy in range(isizey-psizey+1):
            match = 1   # Remains 1 as long as no dismatch appeared
            for i in range(psizey): # Check rows in current snippet
                if imgrows[posy+i][posx:posx+psizex] != patrows[i]:
                    match = 0
                    break
            for i in range(psizex): # Check columns in current snippet
                if imgcols[posx+i][posy:posy+psizey] != patcols[i] or match == 0:
                    match = 0
                    break
                
            if match:   # Match detected - Mark image
                for i in range(psizey):
                    for j in range(psizex):
                        imgrows[posy+i][posx+j] += 2
                imgcols = zip(*imgrows) # Update columns
    return imgrows
    

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
