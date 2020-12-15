# -*- coding: utf-8 -*-
"""

Program Name:  bubblesort.py
Writen by:     Iuliia Lavine
Date:          30 November 2020
Synopsis:      This is the implementation of bubblesort and insertion sort algorithms.


https://stackoverflow.com/questions/997322/why-is-my-bubble-sort-in-python-so-slow
https://www.geeksforgeeks.org/python-program-for-insertion-sort/
"""
from random import randint
import time


#here we build our random numbers
arr1 = [randint(1, 999) for i in range(0, 1000)]
#print(arr1)
arr2 = [randint(1, 999) for i in range(0, 10000)]
#print(arr2)
arr3 = [randint(1, 999) for i in range(0, 20000)]


def bubbleSort(arr, max):
    for n in range(0,max): #upper limit varies based on size of the list
        temp = 0
        for i in range(1, max): #keep this for bounds purposes
            temp = arr[i]
            if arr[i] < arr[i-1]:
                arr[i] = arr[i-1]
                arr[i-1] = temp
                
def insertionSort(arr): 
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
           arr[j+1]=arr[j]
           j=j-1
        arr[j+1]=key


    
#driver code.
input('Press Enter to execute the BubbleSort Algorithm (array contains 1000 number from 1 to 999)\n') 
begin = time.time()
bubbleSort(arr1, 1000)
for i in range(len(arr1)):
    print(arr1[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}") 
 
input('Press Enter to execute the BubbleSort Algorithm (array contains 10000 number from 1 to 999)\n')
begin = time.time()
bubbleSort(arr2, 10000)
for i in range(len(arr2)):
    print(arr2[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}") 

input('Press Enter to execute the BubbleSort Algorithm (array contains 20000 number from 1 to 999)\n')
begin = time.time()
bubbleSort(arr3, 20000)
for i in range(len(arr3)):
    print(arr3[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}") 
    
input('Press Enter to execute the InsertionSort Algorithm (array contains 1000 number from 1 to 999)\n')     
begin = time.time()
insertionSort(arr1)
for i in range(len(arr1)):
    print(arr1[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}") 
    
input('Press Enter to execute the InsertionSort Algorithm (array contains 10000 number from 1 to 999)\n')
begin = time.time()
insertionSort(arr2)
for i in range(len(arr2)):
    print(arr2[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}")   
 
input('Press Enter to execute the InsertionSort Algorithm (array contains 20000 number from 1 to 999)\n')
begin = time.time()
insertionSort(arr2)
for i in range(len(arr3)):
    print(arr3[i])
end = time.time()
print(f"Total runtime of the algorithm is {end - begin}")   
   
time.sleep(5)