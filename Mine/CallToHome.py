# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 21:34:38 2014

@author: EngineeringIsLife
"""
import re
import math

def total_cost(calls):
    cost = 0
    free = 0
    last_date = []
    
    for call in calls:
        duration = math.ceil(int(re.findall(r"\w+",call)[-1])/60.0)        
        new_date = re.findall(r"\w+-\w+-\w+", call)
        
        if last_date != new_date:   # New Day: New cheaper minutes
            free = 100
            
        cost += min(duration, free)
        if duration > free:
            duration -= free
            free = 0
        else:
            free -= duration
            duration = 0
            
        cost += duration * 2
        last_date = new_date
    return int(cost)
            

print total_cost(("2014-01-01 01:12:13 181",
            "2014-01-02 20:11:10 600",
            "2014-01-03 01:12:13 6009",
            "2014-01-03 12:13:55 200")) == 124

print total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4