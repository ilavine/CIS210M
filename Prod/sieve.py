"""
Program Name:  sieve.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This is the implementation of Sieve_of_Eratosthenes

Helpful links: https://www.youtube.com/watch?v=pKvGYOnO9Ao

       
"""
"""
Program Name:  sieve.py
Writen by:     Iuliia Lavine
Date:          10 November 2020
Synopsis:      This is the implementation of Sieve_of_Eratosthenes

Helpful links: https://www.youtube.com/watch?v=pKvGYOnO9Ao

       
"""

from stack import Stack
import random
import time

def sieve(n):
	for i in n:
		for j in n:
			if j != i and j%i == 0:
				n.remove(j)
	return n


print('''
This is the implementation of Sieve of Eratosthenes.\n
To make it work, let's populate our stack with 100 numbers.\n''')
input('\nPress Enter To Execute The Algorithm\n')
#implementing a Stack
stack = Stack()
data = [random.randint(2,100) for _ in range(100)]
stack.push(data)
print("\nPushing values to Stack\n\n",data)
time.sleep(1)
print ('''
\nExecuting the algorithm\n
Sieve of Eratosthenes contains the following data\n''')
numbers = data
print(*data, sep=' ')
time.sleep(3)
print ("\nPrinting prime numbers:\n")
time.sleep(3)
primes = sieve(data)
print(*primes, sep=' ')


