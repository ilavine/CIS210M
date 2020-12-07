"""
Program Name:  simple_stack.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This is just a simple stack implementation. 
       
"""
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
