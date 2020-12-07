# -*- coding: utf-8 -*-
"""
Program Name:   StackProgram


Written by:     Iuliia Lavine


Date:           20 September 2020


Synopsis:      This program pushes 1000000 random elements to a stack 
"""

# imports 

import random
import timeit



# classes


class Node:
  def __init__(self):
    self.data = None # contains the data

 

class StackNode:
  def __init__(self):
    self.maxNode = None # contains the data  
    self.nextNode = None

 

class Stack: # defines a Stack class to implement operations on functions
  def __init__(self):
    self.head = None      
        
  def push(self, node): # pushes numbers to a stack
     
    toAdd = StackNode()       
    if self.head:
      toAdd.nextNode = self.head
      if node.data > self.head.maxNode.data:
        toAdd.maxNode = node
      else:
        toAdd.maxNode = self.head.maxNode               
    else:
      toAdd.maxNode = node
    self.head = toAdd 

    
# main operations
  
stack = Stack()
for i in range (0,1000000):
  node = Node()
  node.data = random.randint(0,1000000) # pushes 1000000 random numbers from 0 to 1000000
  print("Pushing to stack: " + str(node.data)) # prints all the numbers being pushed
  stack.push(node)
 
# Measures the execution time of the Stack program  
elapsed_time = timeit.timeit(Stack, number=100)/100
print('Time elapsed: ', elapsed_time)
