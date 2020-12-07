# -*- coding: utf-8 -*-
"""
Program Name:   StackProgram


Written by:     Iuliia Lavine


Date:           20 September 2020


Synopsis:      This program pushes 1000000 random elements to a stack 
"""

# imports 

import random
import time

print('This program pushes 1000000 random elements to a stack\n')
input('\nPress Enter To Start The Program\n')

# classes


class Node:
  def __init__(self):
    self.data = None # contains the data

 

class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)


    
# main operations
start_time = time.time()  
stack = Stack()
for i in range (0,1000000):
  data = random.randint(0,1000000) # pushes 1000000 random numbers from 0 to 1000000
  print("Pushing to stack: " + str(data)) # prints all the numbers being pushed
  stack.push(data)
end_time = time.time()
total_time = int(end_time - start_time) 
# Measures the execution time of the Stack program  
print('\nTime elapsed: ',round(total_time, 8),' seconds')
print('\nThe size of the stack:', stack.size())
