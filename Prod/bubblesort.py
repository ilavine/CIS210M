'''
Program Name:  bubblesort.py

Writen by:     Iuliia Lavine

Date:          30 November 2020

Synopsis:      This is the implementation of bubblesort algorithm.
	       This is also a bubblesort algorithm visualization.
'''


import random
from random import randint
import matplotlib.pyplot as plt


numberList = [randint(1, 100) for i in range(0, 10)]

def bubbleSort(numberList): #bubblesort implementation
    
    # run loops two times: one for walking throught the array 
    # and the other for comparison
    for i in range(len(numberList)): #for loop for scanning the List
        for j in range(0, len(numberList) - i - 1): #for loop for comparing the list

            #sorting the list in descending order
            if numberList[j] > numberList[j + 1]:
                
                # swap if the element found is greater than the next element
                (numberList[j], numberList[j + 1]) = (numberList[j + 1], numberList[j])

#testing the function                
bubbleSort(numberList) 
  
print ("Sorted array is:") 
for i in range(len(numberList)): 
    print ("%d" %numberList[i]),  

def plotting(): #bubblesort implementation with matplotlib plotting 
    
    theList = 40 #set the lenght of the list
    myList = [randint(1, 100) for i in range(0, 40)] 
    random.shuffle(myList)

    plotting = bubbleSort(myList)

    fig, ax = plt.subplots() 
    ax.set_title("Bubble Sort O(n)") 
    bar_sub = ax.bar(range(len(myList)), myList, align="edge")

    ax.set_xlim(0, theList) 
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes) 
    iteration = [0]

    plt.show() 
    plt.close() 
    

if __name__ == '__main__':
    plotting()