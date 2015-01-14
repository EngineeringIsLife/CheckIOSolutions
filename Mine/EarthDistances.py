# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 23:23:02 2015

@author: EngineeringIsLife
"""

import re
from math import sin, cos, acos, pi

R = 6371

def distance(position1, position2):
    
    lat1, long1 = re.findall(r'(\d+)\xb0(\d+)\S(\d+)\S+([NSWE])',position1)
    lat2, long2 = re.findall(r'(\d+)\xb0(\d+)\S(\d+)\S+([NSWE])',position2)
    
    lat1_deg  = sum([float(a)/(60**k) for k,a in enumerate(lat1[:-1])]) * pi / 180
    lat2_deg  = sum([float(a)/(60**k) for k,a in enumerate(lat2[:-1])]) * pi / 180
    long1_deg = sum([float(a)/(60**k) for k,a in enumerate(long1[:-1])]) * pi / 180
    long2_deg = sum([float(a)/(60**k) for k,a in enumerate(long2[:-1])]) * pi / 180
    
    lat1_deg  *= -1 if lat1[3] == 'S' else 1
    lat2_deg  *= -1 if lat2[3] == 'S' else 1
    long1_deg *= -1 if long1[3] == 'E' else 1
    long2_deg *= -1 if long2[3] == 'E' else 1
    
    # Seitenkosinussatz - http://de.wikipedia.org/wiki/Sph%C3%A4rische_Trigonometrie#Seiten-Kosinussatz
    cos_x = sin(lat1_deg) * sin(lat2_deg) + cos(lat1_deg) * cos(lat2_deg) * cos(long2_deg - long1_deg)
    dist = acos(cos_x) * R
    
    return round(dist, 1)

#print = distance(u"51°28'48''N 0°0'0''E", u"46°12'0''N, 6°9'0''E")
print distance(u"51°28'48''N 0°0'0''E", u"46°12'0''N, 6°9'0''E") == 739.2
print distance(u"90°0'0''N 0°0'0''E", u"90°0'0''S, 0°0'0''W") == 20015.1