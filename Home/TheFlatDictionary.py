# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:18:06 2014

@author: EngineeringIsLife
"""

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if len(v) is 0:
                v = ""
            if isinstance(v, dict):# and len(v) is not 0:
                stack.append((path + (k,), v))
                #print v
            else:
                #print v
                result["/".join((path + (k,)))] = v
    return result
    
print flatten({"key": "value"}) == {"key": "value"}, "Simple"
print flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}, "Nested"
print flatten({"empty": {}}) == {"empty": ""}, "Empty value"
print flatten({"name": {"first": "One",
                "last": "Drone"},
                "job": "scout",
                "recent": {},
                "additional": {
                "place": {
                "zone": "1",
                "cell": "2"}}}
) == {"name/first": "One",
      "name/last": "Drone",
      "job": "scout",
      "recent": "",
      "additional/place/zone": "1",
      "additional/place/cell": "2"}