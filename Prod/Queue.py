# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 01:37:39 2020

@author: iulii
"""

from collections import deque

class Queue():
    
    
    def __init__(self):
        
        self.queue = deque()
        self.size = 0
        
    def enqueue(self, item):
        
        self.queue.append(item)
        self.size += 1
        
    def dequeue(self):
        
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else: 
            return None
        
    def peek(self, queue):
        
        if self.size > 0:
            ret_val = self.queue.popleft()
            queue.appendleft(ret_val)
            return ret_val
        else:
            return None
        
    def get_size(self):
        
        return self.size