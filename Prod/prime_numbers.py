"""
Program Name:    prime_numbers.py


Written by:      Iuliia Lavine


Date:           25 November 2020


Synopsis:      This program finds out whether a randomly generated number is prime
               by implementing a recursive function.
                
"""

from random import randint
import time

print('''
This program finds out whether a randomly generated number is prime
by implementing a recursive function.\n''')
input('Press Enter To Start The Program\n')

def numberList():
    numberList = [randint(1, 100) for i in range(0, 10)]
    return numberList

def getMessage1(parm):
    message = "Number parm1 is prime."
    message = message.replace("parm1", str(parm))
    return message

def getMessage2(parm):
    message = "Number parm1 is not prime."
    message = message.replace("parm1", str(parm))
    return message

a = numberList()
print('Random number list...\n', a)
input('\nPress Enter To Execute The Recursive Algorithm\n')
print('\nApplying the algorithm...\n')
time.sleep(3)

def isPrime(number, i = 2):
        
        if (number <= 2): 
            return getMessage1(number) if(number == 2) else getMessage2(number)
        if (number % i == 0): 
            return getMessage2(number)
        if (i * i > number): 
            return getMessage1(number)
        
        return isPrime(number, i + 1) 
	

theList = numberList()
for i in range(0, len(theList)):
    message = isPrime(theList[i])
    print(message)
