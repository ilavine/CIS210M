# -*- coding: utf-8 -*-
"""
Program Name:   Queue.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This program demonstrates the implementation of Queue. 
       
"""
print('This program demonstrates the implementation of Queue.\n')
input('Press Enter To Start The Program\n')

from collections import deque
import time

class Queue():
    
    def __init__(self):
        self.queue = deque()
        self.size = 0
        
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
        
    def dequeue(self, item):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else: 
            return None
        
    def peek(self):
        if self.size > 0:
            ret_val = self.queue.popleft()
            self.queue.appendleft(ret_val)
            return ret_val
        else:
            return None
        
    def get_size(self):
        return self.size

q = Queue()
#driver code
print('''
Enqueue numbers:
1
21
30
''')
q.enqueue(1)
q.enqueue(21)
q.enqueue(30)
time.sleep(1)
print('The size of the queue:', q.get_size())
time.sleep(1)
print('\nThe element at the front position', q.peek())
time.sleep(1)
print('''
Dequeue numbers:
1
21
30
''')
q.dequeue(1)
q.dequeue(21)
q.dequeue(30)
time.sleep(1)
print('The size of the queue:', q.get_size())
