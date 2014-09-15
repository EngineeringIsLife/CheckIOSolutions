# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:19:30 2014

@author: EngineeringIsLife
"""

def check_connection(network, first, second):
    for connection in network:
        if first in connection:
            if second in connection:
                return True
            shorter_network = tuple(x for x in network if x is not connection)
            drone1,drone2 = connection.split("-")
            next_drone = drone1 if drone1 not in first else drone2
            if check_connection(shorter_network, next_drone, second):
                return True
    return False
      
   
print check_connection(("s3-s4","s2-s1","s1-s3","s4-s1","s4-s5","s6-s5"),"s6","s2")

print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
     "scout2", "scout3") == True
print check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout") == False
