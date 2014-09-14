# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 16:03:58 2014

@author: EngineeringIsLife
"""

from collections import deque

def letter_queue(commands):
    queue = deque()
    for s in commands:
        if "POP" in s and len(queue):
            queue.popleft()
        elif "PUSH" in s:
            queue.append(s[-1])
    return "".join(queue)

print letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
print letter_queue(["POP", "POP"]) == ""
print letter_queue(["PUSH H", "PUSH I"]) == "HI"
print letter_queue([]) == ""