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


    
def RSL(num, start = 0, end = 1000000): #creates Random Sorted List
    list1 = [] 
    tmp = random.randint(start, end) 
      
    for x in range(num): 
          
        while tmp in list1: 
            tmp = random.randint(start, end) 
              
        list1.append(tmp) 
          
    list1.sort() 
      
    return list1

def index(indx):
    indx = []
    for i in range(0, 1000000):
        indx.append('zzz, ') #this is my index
        
    return indx
 
'''       
def Number(y): #finds the largest number in the list
    
    y = x[-1] 
    
    return y


def Number2(newList): #finds the second largest number in the list

    x.remove(Number(y))
    newList = x[-1]
    
    return newList
'''   

#variables

indx = []
x = RSL(1000000, 0, 999999)
#y = []
#newList = []
theIndex = index(indx)

#driver code

for i in range(len(x)):
    ptr = int(x[i])
    theIndex[ptr] = theIndex[ptr] + str(i)

for i in range(len(theIndex)):
     print(theIndex[i])

     
     
'''
#prints
indexList = [-3] #creates a new list
indexList.append(Number(y)) #adds a new value
print('first list: ', indexList) #prints the list

indexList2 = [-5] #creates a new list
indexList2.append(indexList) #adds a value
indexList2.append(Number2(newList)) #adds a seconds value

print('second list: ', indexList2) #prints the nested list
'''