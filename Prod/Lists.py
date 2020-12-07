# -*- coding: utf-8 -*-
"""
Program Name:   Lists


Writen by:      Iuliia Lavine


Date:           9 November 2020


Synopsis:      Creates a list of random numbers and works with a linked list.

               Can also find the largest number along with the second largest number
               in the list. Creates a nested list. 
                
"""
import random
import time

print('''
This program creates a list of random numbers and works with a linked list\n''')
input('Press Enter To Start The Program\n')

    
def RSL(num, start = 0, end = 100): #creates Random List
    list1 = [] 
    tmp = random.randint(start, end) 
      
    for x in range(num): 
          
        while tmp in list1: 
            tmp = random.randint(start, end) 
              
        list1.append(tmp) 
          
      
    return list1

def index(indx):
    indx = []
    for i in range(0, 101):
        indx.append('zzz, ') #this is my index
        
    return indx
 
 

#variables

indx = []
x = RSL(100, 0, 100)
theIndex = index(indx)

#driver code

for i in range(len(x)):
    ptr = int(x[i])
    theIndex[ptr] = theIndex[ptr] + str(i)
print('Creating a list...')
time.sleep(3)
for i in range(len(theIndex)):
     print(theIndex[i])

     

     
     

