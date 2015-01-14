# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 22:27:22 2015

@author: EngineeringIsLife
"""

import re

times = {'hour':1.0, 'minute':1.0/60, 'second':1.0/3600}

def getAbsoluteHours(clocktime):
    return float(clocktime[0]) + float(clocktime[1]) / 60 + float(clocktime[2]) / 3600


def broken_clock(starting_time, wrong_time, error_description):
    start = getAbsoluteHours(starting_time.split(':'))
    broke = getAbsoluteHours(wrong_time.split(':'))
    num_str,denom_str = error_description.split('at')
    
    for key in times.keys():
        if key in num_str:
            num = float(re.search(r'[+-]\d+',num_str).group()) * times[key]
        if key in denom_str:
            denom = float(re.search(r'\d+',denom_str).group()) * times[key]
    
    rt = (broke + start * num/denom) / (1 + num/denom)

    s = int(rt * 3600) % 60
    m = int(rt * 60) % 60
    h = int(rt) % 24
        
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
    


print broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') ==  '00:00:10'
print broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') ==  '06:10:30'
print broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') ==  '14:00:00'
print broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') ==  '07:05:05'
print broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') ==  '00:00:22'